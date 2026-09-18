#!/usr/bin/env bash
# Roda o HyperFrames com o browser e a rota de rede certos deste container.
#
# Por que existe: `HYPERFRAMES_BROWSER_PATH` gravado no ~/.bashrc so vale em
# shell interativo/login; uma tool call do agente roda `bash -c`, que nao le o
# perfil, e ai o render falha procurando Chrome. Este wrapper garante os dois
# lados (browser e proxy) em qualquer shell.
#
# Uso: bash scripts/hyperframes.sh <subcomando> [args]
#      bash scripts/hyperframes.sh render --quality draft --output out.mp4
set -uo pipefail

export HYPERFRAMES_BROWSER_PATH="${HYPERFRAMES_BROWSER_PATH:-/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell}"
if [ ! -x "$HYPERFRAMES_BROWSER_PATH" ]; then
  echo "AVISO: browser nao encontrado em $HYPERFRAMES_BROWSER_PATH; o render local vai falhar" >&2
fi

# registry.npmjs.org vem em no_proxy e bate direto no firewall de egresso (403);
# roteando pelo agent proxy o npx resolve o pacote.
if [ -n "${HTTPS_PROXY:-}" ]; then
  export no_proxy="" NO_PROXY="" HTTP_PROXY="$HTTPS_PROXY"
  export SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}"
  export npm_config_proxy="$HTTPS_PROXY" npm_config_https_proxy="$HTTPS_PROXY"
  export npm_config_noproxy="" npm_config_cafile="$SSL_CERT_FILE"
fi

exec npx --yes hyperframes "$@"
