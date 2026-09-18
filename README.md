# Dra. Juliana Romano Conteúdo Studio

Estúdio de edição e agendamento de conteúdo para as redes da **Dra. Juliana Romano**. Estúdio irmão do [`ana-conteudo`](https://github.com/suportezv/ana-conteudo), do [`eita-conteudo`](https://github.com/suportezv/eita-conteudo) e do [`profissioai-conteudo`](https://github.com/suportezv/profissioai-conteudo); mesma infraestrutura, posicionamento desta marca.

- **`FRAMEWORK.md`**: persona, regras, pilares, assinaturas de edição, escolha do framework de motion e fluxo por vídeo.
- **`CLAUDE.md`**: memória persistente do projeto (IDs, contas, gotchas, cinto de ferramentas).
- **`projects/`**: um subdiretório por vídeo (briefing, transcrição, scripts de edição, caption).
- **`scripts/`**: setup e validação do ambiente (Linux/cloud) e as ferramentas genéricas de produção (abaixo).
- **`remotion/`**: composições React (cartões de título 1080x1920 e 1080x1080). Paleta e fonte só em `remotion/src/marca.ts`.
- **`design-system/`**: tokens, logo, canvas e o estudo das capas de YouTube.
- **`assets/fonts/`**: Playfair Display e Montserrat locais (Google Fonts fica fora da allowlist).
- **`patches/`**: histórico; o patch do video-use foi aposentado em 2026-09-18 (o `validate.sh` testa comportamento).

## Primeiro uso (cloud)

```bash
bash scripts/setup.sh      # 6 passos; avisa em vez de derrubar o boot: ler a saída
bash scripts/validate.sh   # tem que ficar verde (os hosts "opcionais" só avisam)
```

Depois: coloque o bruto no Drive (pasta pública) ou anexe na conversa, escreva o briefing em `projects/<nome>/` e peça a edição.

## Ferramentas em `scripts/`

Todas genéricas (nenhuma referência de marca) e lendo chaves **só** de variável de ambiente.

| Script | O que faz |
|---|---|
| `decupar.py` | Decupa vídeo por **âncoras de texto** ("de tal frase até tal frase") casadas contra a transcrição com timestamp por palavra. Junta trechos, gira, aplica LUT, normaliza áudio |
| `relatorio_decupagem.py` | Retranscreve as peças finais e monta o relatório do que ficou e do que caiu |
| `gera_lut_slog2.py` | Gera LUT 3D de S-Log2/S-Gamut para Rec.709 (`colour-science`) |
| `zip_index_remoto.py` | Lista e extrai arquivos de um ZIP gigante no Drive por *range request*, sem baixar o ZIP |
| `gera_imagem.py` | Gera imagem pela OpenAI ou pelo Gemini, mesma interface (`OPENAI_API_KEY` / `GEMINI_API_KEY`) |
| `sobe_para_drive.py` | Sobe arquivos para uma pasta do Drive com token de acesso pronto |

| Serviço | Uso | Configuração |
|---|---|---|
| Google Drive | Brutos e capas | Conector oficial + pastas públicas + `drive.google.com` e `drive.usercontent.google.com` liberados |
| Metricool | Agendamento | Marca **drajulianaromano**, blog_id **6741531** (Instagram, TikTok, YouTube) |
| ElevenLabs | Transcrição, trilha, SFX, TTS | `ELEVENLABS_API_KEY` (`sk_...`, 51 chars) na env var do environment; o setup grava no `.env` do video-use |
| Kairogen | B-roll por IA | Conta suporte@zavi.ag, **FREE com 0 créditos** (2026-09-18) |
| OpenAI / Gemini | Imagem por `gera_imagem.py` | `OPENAI_API_KEY` / `GEMINI_API_KEY` + hosts liberados: **pendentes neste environment** |

> Este repositório é **público** de propósito: o agendamento no Metricool depende de servir mídia por `raw.githubusercontent.com`. Nunca commitar chaves aqui.
