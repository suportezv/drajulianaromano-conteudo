#!/usr/bin/env python3
"""Gera imagem pela OpenAI ou pelo Gemini, com a mesma interface.

As chaves vem das variaveis de ambiente OPENAI_API_KEY e GEMINI_API_KEY.
Nenhuma chave e aceita por argumento: linha de comando vaza em historico e
em lista de processos.

Aceita imagens de referencia com --ref (repetivel): a OpenAI passa a usar o
endpoint de edicao e o Gemini recebe as imagens como partes inline. Serve para
compor uma cena a partir de uma foto real em vez de inventar a pessoa.

Uso:
    python3 scripts/gera_imagem.py openai "um gato de oculos" saida.png
    python3 scripts/gera_imagem.py gemini "um gato de oculos" saida.png --modelo gemini-3-pro-image
    python3 scripts/gera_imagem.py openai "capa com esta pessoa" capa.png --ref foto.jpg --tamanho 1536x1024
    python3 scripts/gera_imagem.py gemini "capa com esta pessoa" capa.png --ref foto.jpg --proporcao 16:9
    python3 scripts/gera_imagem.py --listar
"""
import argparse
import base64
import json
import os
import subprocess
import sys

OPENAI_URL = "https://api.openai.com/v1/images/generations"
OPENAI_EDIT_URL = "https://api.openai.com/v1/images/edits"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent"

PADRAO = {"openai": "gpt-image-2", "gemini": "gemini-3-pro-image"}


def _post(url, cabecalhos, corpo):
    cmd = ["curl", "-s", "--max-time", "600", "-X", "POST", url]
    for k, v in cabecalhos.items():
        cmd += ["-H", f"{k}: {v}"]
    cmd += ["-H", "Content-Type: application/json", "--data-binary", "@-"]
    r = subprocess.run(cmd, input=json.dumps(corpo), capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return {"_bruto": r.stdout[:500], "_erro_curl": r.stderr[:300]}


def _mime(caminho):
    ext = os.path.splitext(caminho)[1].lower()
    return {".png": "image/png", ".webp": "image/webp"}.get(ext, "image/jpeg")


def _post_multipart(url, cabecalhos, campos, arquivos):
    """POST multipart via curl. `arquivos` e uma lista de (campo, caminho)."""
    cmd = ["curl", "-s", "--max-time", "900", "-X", "POST", url]
    for k, v in cabecalhos.items():
        cmd += ["-H", f"{k}: {v}"]
    for k, v in campos.items():
        cmd += ["-F", f"{k}={v}"]
    for campo, caminho in arquivos:
        cmd += ["-F", f"{campo}=@{caminho};type={_mime(caminho)}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return {"_bruto": r.stdout[:500], "_erro_curl": r.stderr[:300]}


def chave(nome):
    v = os.environ.get(nome, "")
    if not v:
        sys.exit(f"{nome} ausente no ambiente. Cadastre nas variaveis do environment.")
    return v


def openai_imagem(prompt, modelo, tamanho, qualidade, refs=()):
    cab = {"Authorization": f"Bearer {chave('OPENAI_API_KEY')}"}
    if refs:
        # Com referencia o endpoint e outro: /images/edits, multipart, e cada
        # arquivo vai em "image[]". O modelo compoe a cena a partir das fotos.
        d = _post_multipart(
            OPENAI_EDIT_URL, cab,
            {"model": modelo, "prompt": prompt, "size": tamanho,
             "quality": qualidade, "n": "1"},
            [("image[]", r) for r in refs],
        )
    else:
        d = _post(
            OPENAI_URL, cab,
            {"model": modelo, "prompt": prompt, "size": tamanho,
             "quality": qualidade, "n": 1},
        )
    if "error" in d:
        return None, d["error"].get("message", str(d["error"]))[:300]
    dados = (d.get("data") or [{}])[0]
    if dados.get("b64_json"):
        return base64.b64decode(dados["b64_json"]), None
    if dados.get("url"):  # modelos antigos devolvem URL em vez de base64
        r = subprocess.run(["curl", "-sL", "--max-time", "300", dados["url"]],
                           capture_output=True)
        return r.stdout, None
    return None, json.dumps(d)[:300]


def gemini_imagem(prompt, modelo, refs=(), proporcao=None):
    partes = [{"text": prompt}]
    for r in refs:
        with open(r, "rb") as fh:
            partes.append({"inline_data": {"mime_type": _mime(r),
                                           "data": base64.b64encode(fh.read()).decode()}})
    corpo = {"contents": [{"parts": partes}]}
    if proporcao:
        corpo["generationConfig"] = {"imageConfig": {"aspectRatio": proporcao}}
    d = _post(
        GEMINI_URL.format(modelo=modelo),
        {"x-goog-api-key": chave("GEMINI_API_KEY")},
        corpo,
    )
    if "error" in d:
        return None, f"{d['error'].get('code')}: {str(d['error'].get('message'))[:300]}"
    for cand in d.get("candidates", []):
        for parte in cand.get("content", {}).get("parts", []):
            dados = parte.get("inlineData") or parte.get("inline_data")
            if dados and dados.get("data"):
                return base64.b64decode(dados["data"]), None
    return None, json.dumps(d)[:400]


def listar():
    """Lista os modelos de imagem que cada conta enxerga hoje."""
    r = subprocess.run(["curl", "-s", "--max-time", "60",
                        "https://api.openai.com/v1/models",
                        "-H", f"Authorization: Bearer {chave('OPENAI_API_KEY')}"],
                       capture_output=True, text=True)
    ids = sorted(m["id"] for m in json.loads(r.stdout).get("data", []))
    print("OpenAI:", ", ".join(i for i in ids if "image" in i) or "nenhum")

    r = subprocess.run(["curl", "-s", "--max-time", "60",
                        "https://generativelanguage.googleapis.com/v1beta/models",
                        "-H", f"x-goog-api-key: {chave('GEMINI_API_KEY')}"],
                       capture_output=True, text=True)
    ms = [m["name"].split("/")[-1] for m in json.loads(r.stdout).get("models", [])]
    print("Gemini:", ", ".join(m for m in ms if "image" in m) or "nenhum")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("provedor", nargs="?", choices=["openai", "gemini"])
    ap.add_argument("prompt", nargs="?")
    ap.add_argument("destino", nargs="?")
    ap.add_argument("--modelo", default=None)
    ap.add_argument("--tamanho", default="1024x1024", help="so OpenAI")
    ap.add_argument("--qualidade", default="high", help="so OpenAI")
    ap.add_argument("--proporcao", default=None, help="so Gemini (ex.: 16:9)")
    ap.add_argument("--ref", action="append", default=[], metavar="ARQUIVO",
                    help="imagem de referencia; pode repetir")
    ap.add_argument("--listar", action="store_true", help="lista modelos e sai")
    a = ap.parse_args()

    if a.listar:
        listar()
        return
    if not (a.provedor and a.prompt and a.destino):
        ap.error("informe provedor, prompt e destino (ou use --listar)")

    for r in a.ref:
        if not os.path.isfile(r):
            ap.error(f"referencia nao encontrada: {r}")

    modelo = a.modelo or PADRAO[a.provedor]
    if a.provedor == "openai":
        img, erro = openai_imagem(a.prompt, modelo, a.tamanho, a.qualidade, a.ref)
    else:
        img, erro = gemini_imagem(a.prompt, modelo, a.ref, a.proporcao)

    if erro:
        sys.exit(f"falhou ({a.provedor}/{modelo}): {erro}")
    with open(a.destino, "wb") as fh:
        fh.write(img)
    ref_txt = f", {len(a.ref)} ref" if a.ref else ""
    print(f"{a.destino}  {len(img)/1000:.0f} KB  ({a.provedor}/{modelo}{ref_txt})")


if __name__ == "__main__":
    main()
