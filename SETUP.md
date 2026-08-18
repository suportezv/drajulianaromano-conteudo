# Setup do Dra. Juliana Romano Conteúdo Studio

Espelho do setup do [`ana-conteudo`](https://github.com/suportezv/ana-conteudo) / [`eita-conteudo`](https://github.com/suportezv/eita-conteudo). No cloud, basta:

```bash
bash scripts/setup.sh
bash scripts/validate.sh
```

## Environment (Claude Code cloud)

Usar o environment **"ana-conteudo"** (ou duplicá-lo como "drajulianaromano-conteudo"): network **Custom** com `drive.google.com`, `drive.usercontent.google.com` e `api.elevenlabs.io` na lista de domínios, e a env var `ELEVENLABS_API_KEY` (chave `sk_` de 51 chars). Configura-se no seletor de nuvem acima da caixa de mensagem em claude.ai/code (não nas Configurações gerais). Mudanças valem para sessões novas.

## Conectores (cada um exige ação do usuário; peça na hora certa)

- **Google Drive**: conector oficial do Claude + pastas de brutos com "qualquer pessoa com o link: leitor" (download direto por curl, qualquer tamanho). Pasta de brutos desta marca: PENDENTE.
- **Metricool**: conta da agência (suporte@zavi.ag). **PENDENTE: conectar o conector MCP e a marca da Dra. Juliana Romano** no painel (blog_id PENDENTE).
- **Kairogen**: conta suporte@zavi.ag, plano Essential (`veo3-1-lite`).
- **ElevenLabs**: chave `sk_...` (51 chars) em `.env` na raiz do video-use. Voz da marca: PENDENTE.

## Validação final

1. `ffmpeg -filters | grep -cE "subtitles|zscale"` >= 2.
2. Transcrever 10s de um vídeo com o helper do video-use: JSON com timestamps por palavra.
3. Rede: `curl -s -o /dev/null -w "%{http_code}" https://drive.google.com/` responde HTTP (não 000).
4. Metricool: `getBrandSettings` lista a marca da Dra. Juliana Romano (após conectar).
5. Kairogen: `get_me_context` mostra plano e créditos.
6. Memória persistente: `CLAUDE.md` deste repo.
