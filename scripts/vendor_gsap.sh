#!/usr/bin/env bash
# Traz o GSAP para dentro de um projeto HyperFrames e aponta o HTML para a copia local.
#
# Por que: o Chromium deste container nao confia na CA do agent proxy (o banco NSS
# esta vazio e o certutil nao pode ser instalado), entao toda tag <script> apontando
# para o cdn.jsdelivr.net falha com ERR_CERT_AUTHORITY_INVALID quando o `check`, o
# `preview` ou o `validate` abrem a pagina no browser. O `render` nao sofre com isso
# (o compilador baixa pelo Node e embute), mas o `check` e o portao obrigatorio do
# fluxo. Bundle local tambem deixa o render deterministico, que e o que o proprio
# HyperFrames recomenda na mensagem de aviso.
#
# Uso: bash scripts/vendor_gsap.sh <pasta-do-projeto> [versao]
set -euo pipefail

PROJ="${1:?uso: vendor_gsap.sh <pasta-do-projeto> [versao]}"
VER="${2:-3.14.2}"
[ -f "$PROJ/index.html" ] || { echo "nao achei $PROJ/index.html"; exit 1; }
mkdir -p "$PROJ/assets/vendor"
DEST="$PROJ/assets/vendor/gsap.min.js"

# 1) copia do clone do hyperframes (offline, sempre presente depois do setup)
CLONE="${TOOLS_DIR:-/workspace}/heygen-com/hyperframes/skills/talking-head-recut/assets/vendor/gsap.min.js"
if [ -s "$CLONE" ]; then
  cp "$CLONE" "$DEST"
else
  # 2) npm pack (registry.npmjs.org passa pelo agent proxy)
  TMP="$(mktemp -d)"
  ( cd "$TMP"
    export no_proxy="" NO_PROXY="" HTTP_PROXY="${HTTPS_PROXY:-}" \
           npm_config_proxy="${HTTPS_PROXY:-}" npm_config_https_proxy="${HTTPS_PROXY:-}" \
           npm_config_noproxy="" npm_config_cafile="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}"
    npm pack "gsap@$VER" --silent >/dev/null
    tar -xzf "gsap-$VER.tgz" package/dist/gsap.min.js )
  cp "$TMP/package/dist/gsap.min.js" "$DEST"; rm -rf "$TMP"
fi

# Aponta TODO HTML do projeto para a copia local (idempotente). Blocos do registry
# entram em compositions/ com a mesma tag de CDN, entao o index.html sozinho nao basta.
n=0
while IFS= read -r f; do
  rel=$(python3 -c "import os,sys; print(os.path.relpath('$PROJ/assets/vendor/gsap.min.js', os.path.dirname(sys.argv[1])))" "$f")
  if grep -q 'cdn\.jsdelivr\.net/npm/gsap@' "$f"; then
    sed -i -E "s#https://cdn\.jsdelivr\.net/npm/gsap@[0-9.]+/dist/gsap\.min\.js#$rel#g" "$f"
    n=$((n+1))
  fi
done < <(find "$PROJ" -name '*.html' -not -path '*/node_modules/*')
echo "GSAP local em $DEST ($(wc -c < "$DEST") bytes); $n arquivo(s) HTML reapontados"
