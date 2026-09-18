# Setup do Dra. Juliana Romano Conteúdo Studio

Espelho do setup dos estúdios irmãos. No cloud, basta:

```bash
bash scripts/setup.sh
bash scripts/validate.sh
```

## Environment (Claude Code cloud)

Usar o environment **"ana-conteudo"** (compartilhado entre os estúdios) ou duplicá-lo. Configura-se no seletor de nuvem acima da caixa de mensagem em claude.ai/code (não nas Configurações gerais). Os estúdios irmãos dizem que mudanças valem só para sessões novas; em 2026-09-18 chaves e hosts novos entraram na sessão aberta. Conferir com `printenv` e `curl -sv ... | grep CONNECT` antes de reiniciar.

**Campo de setup script: caminho absoluto, nunca relativo.** O boot roda com o diretório de trabalho no **pai** do repo, então `bash scripts/setup.sh` falha com `No such file or directory` e **exit 127**, e a sessão nasce sem `/workspace`, sem skills e sem ffmpeg. Como o environment "ana-conteudo" serve vários estúdios, o campo não pode citar o nome de um repo. Colar exatamente esta linha:

```bash
for p in ./scripts/setup.sh ./*/scripts/setup.sh; do [ -f "$p" ] && exec bash "$p"; done; p=$(find /home /workspace /repo /app /src -maxdepth 4 -type f -path "*/scripts/setup.sh" 2>/dev/null | head -1); [ -n "$p" ] && exec bash "$p"; echo "setup.sh nao encontrado no repo"; exit 1
```

Ela tenta o script na pasta atual, depois em qualquer subpasta (o caso do boot, que roda no pai), e por último procura no disco; o próprio `setup.sh` deriva o `REPO_ROOT` do `BASH_SOURCE`, então funciona seja qual for o diretório. **Testada em 2026-09-18 nos quatro cenários** (raiz do repo, pai, `/tmp` e `/`): os seis passos rodam e sai com **exit 0** em todos. Se um estúdio usar environment próprio, a alternativa fixa é `bash /home/user/<nome-do-repo>/scripts/setup.sh`.

### Allowlist de rede (Custom)

A entrada é literal por subdomínio (`www.googleapis.com` não cobre `generativelanguage.googleapis.com`). Diagnóstico: `curl -sv https://host/ 2>&1 | grep CONNECT`; `403` no CONNECT é allowlist.

| Host | Para quê | Estado em 2026-09-18 |
|---|---|---|
| `drive.google.com`, `drive.usercontent.google.com` | baixar brutos e capas | OK |
| `api.elevenlabs.io` | TTS, STT, SFX | OK |
| `github.com`, `api.github.com`, `objects.githubusercontent.com` | ffmpeg estático, clones, fontes | OK |
| `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org` | Python e Remotion (o setup roteia pelo agent proxy) | OK |
| `api.openai.com` | imagem por GPT (`gera_imagem.py`) | OK (liberado em 2026-09-18) |
| `generativelanguage.googleapis.com` | imagem por Gemini (`gera_imagem.py`) | OK (liberado em 2026-09-18) |
| `www.googleapis.com` | upload para o Drive (`sobe_para_drive.py`) | OK (liberado em 2026-09-18) |
| `cdn.jsdelivr.net` | GSAP de todo scaffold, exemplo e bloco do HyperFrames | OK (liberado em 2026-09-18) |
| `raw.githubusercontent.com` | registry de blocos do HyperFrames (`hyperframes add`, `catalog`) | OK (liberado em 2026-09-18; `catalog` lista ~400 blocos) |

Para as skills do hyperframes o `raw.githubusercontent.com` não é necessário (o setup registra a partir do clone local); só o registry de blocos depende dele.

### Variáveis de ambiente (nunca em arquivo do repo, nunca no chat)

| Variável | Para quê | Estado |
|---|---|---|
| `ELEVENLABS_API_KEY` | TTS, STT (Scribe), sound-generation | presente (`sk_`, 51 chars; plano free) |
| `OPENAI_API_KEY` | `gera_imagem.py openai` | presente; geração real validada em 2026-09-18 |
| `GEMINI_API_KEY` | `gera_imagem.py gemini` (chave válida não é quota: o projeto precisa estar no faturamento) | presente; geração real validada em 2026-09-18, quota OK |
| `GOOGLE_OAUTH_TOKEN` | `sobe_para_drive.py` (gerado no OAuth Playground, escopo `drive.file`, vale 1 h) | sob demanda |
| `HYPERFRAMES_BROWSER_PATH` | browser de render do HyperFrames (headless_shell do Playwright) | o `setup.sh` grava no perfil, mas o que vale é o wrapper `scripts/hyperframes.sh` |

## Conectores (cada um exige ação do usuário)

- **Google Drive**: conector oficial + pastas com "qualquer pessoa com o link: leitor". Brutos: `1fkXwabNwAX9jkoR-Po5tCSYdHq0kjgU4`; capas prontas: `1mR7g9h-SmryaQU5Zbpn8WfcpQ5UoQ54w`.
- **Metricool**: conta suporte@zavi.ag, marca **drajulianaromano**, **blog_id 6741531** (Instagram, TikTok e YouTube conectados).
- **Kairogen**: conta suporte@zavi.ag, **FREE com 0 créditos**.
- **ElevenLabs**: plano free; voz da marca PENDENTE.

## Validação final

1. `bash scripts/validate.sh` verde: ffmpeg com `subtitles`/`zscale`, `is_portrait_source` acertando retrato, paisagem e girado, rede, Remotion renderizando 1 frame, browser do HyperFrames, skills registradas.
2. Metricool: `getBrandSettings` lista "drajulianaromano" com blog_id 6741531.
3. Kairogen: `get_me_context` mostra plano e créditos.
4. Smoke dos scripts: `python3 scripts/gera_imagem.py --listar` (responde só com as chaves cadastradas), `python3 scripts/gera_lut_slog2.py /tmp/x.cube --size 17`.
5. Memória persistente: `CLAUDE.md` deste repo.

## Pendências de marca (bloqueiam produção de texto público)

Ver as seções marcadas **PENDENTE** no `FRAMEWORK.md`: persona e tom, CTA da caption, pilares, cor de acento do lettering e voz da ElevenLabs.

## Limitação conhecida do container (não é allowlist)

O Chromium não confia na CA do agent proxy: o banco NSS dele está vazio e o `certutil` não pode ser instalado (o apt responde 403). Com isso, qualquer asset remoto por HTTPS falha com `ERR_CERT_AUTHORITY_INVALID` quando o `check`, o `preview` ou o `validate` do HyperFrames abrem a página. O `render` não sofre, porque o compilador baixa pelo Node e embute. Regra do estúdio: **asset local**, com `bash scripts/vendor_gsap.sh <projeto>` antes do primeiro `check`. Nunca desligar verificação de TLS.

