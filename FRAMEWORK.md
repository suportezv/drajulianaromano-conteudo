# Dra. Juliana Romano Conteúdo Studio: FRAMEWORK

Estúdio de edição e agendamento para as redes da **Dra. Juliana Romano**. Espelho do framework dos estúdios irmãos (`ana-conteudo` / `eita-conteudo`), adaptado para esta marca.

> Os blocos marcados **PENDENTE** dependem do briefing de posicionamento da marca e serão preenchidos e commitados quando confirmados com a agência.

## Persona e voz do perfil

- **PENDENTE**: persona, tom de voz e CTA padrão da Dra. Juliana Romano (definir no primeiro briefing).
- Quando a criadora do método EITA for citada, credencial sempre completa: **"Neurocientista criadora do método EITA"**.

### REGRAS INEGOCIÁVEIS

1. **Nunca usar travessão em texto público.** Reescrever a frase.
2. Credencial da criadora sempre completa: **"Neurocientista criadora do método EITA"**.
3. Palavrão em vídeo **se bipa, não se corta** (sine 1000 Hz curto, voz mutada no trecho).
4. Loudness final: **-14 LUFS**.

## Pilares de conteúdo

**PENDENTE**: definir com o primeiro briefing (nos estúdios irmãos os pilares são hipóteses iniciais validadas com desempenho).

## Assinaturas de edição

Herdadas do estúdio ana-conteudo (validadas nos testes 01 e 02 e na leva @luxosobrerodas):

- Hook verbal ou visual + título na tela nos **2 primeiros segundos**.
- Lettering condensado caps branco com sombra dura; acento **amarelo #FFE234** nas ênfases (fonte: Helvetica Neue Condensed Black no Mac; Liberation Sans Bold como fallback Linux). Cor de acento própria da marca: **PENDENTE confirmar**.
- Legendas frase a frase em branco (não karaokê), terço inferior, SEMPRE por último no filter chain.
- Cortes secos; punch-ins de zoom 1.10 a 1.22x; freeze frames P&B com card para punchlines; cutaways como payoff de piada.
- Palavrão não corta: **bipa**.
- Trilha discreta (vol ~0.12 a 0.15) gerada via ElevenLabs sound-generation; SFX (whoosh, impact, riser, scratch) sincronizados aos cortes.
- Duração alvo: **20 a 60s**. Loudness final: **-14 LUFS**.

## Fórmula da caption

1. Hook em 1 linha (dor ou cena concreta, sem travessão)
2. 2 a 3 parágrafos curtos
3. CTA da marca (**PENDENTE definir**)
4. Pergunta de engajamento

## Fluxo por vídeo

1. Bruto (Drive público ou anexo na conversa) + briefing (pilar, mensagem central, duração, data)
2. Proxy SDR (se HLG) + transcrição Scribe (timestamps por palavra)
3. Decupagem/cortes (mapear falas de impacto e picos de áudio)
4. Cor
5. Lettering/motion (PIL, PNGs com fade de alpha)
6. **Legendas por último**
7. Trilha + SFX (sound-generation; batidas detectadas por script)
8. Preview 720p+ para aprovação na conversa
9. Caption
10. Agendamento no Metricool como rascunho (marca desta criadora; melhor horário: medir após conectar a marca)

## Padrão de thumbnail (YouTube vídeo longo)

Padrão em duas fases. A v1 (frames de vídeo, usada nas capas do Mounjaro e das Razões da Obesidade) foi **liberada provisoriamente em 2026-09-02 apenas por prazo; NÃO é o padrão aprovado**. O padrão definitivo está em **`design-system/CAPAS.md`**: foto profissional do Drive (nunca frame), fundo ilustrado gerado por IA, rim light/glow e grading amarrando foto ao fundo, prop 3D com seta, texto com gradiente dourado. A base estética segue sendo **thumb de performance, estilo YouTube agressivo**; as thumbs elegantes na paleta da marca NÃO são o padrão das capas de vídeo (a paleta elegante fica para o feed, capas de Instagram, banner e documentos).

- **Fundo escuro dramático** (preto/quase preto com glow colorido, fogo, textura) ou o próprio cenário do vídeo saturado e escurecido nas bordas.
- **Texto gigante em caps, fonte condensada pesada (Anton/Impact-like)**: branco + **amarelo #FFE234** como dupla principal, com **contorno preto grosso** e sombra dura; vermelho para palavras de perigo, verde para promessa/solução. 2 a 4 linhas curtas na metade esquerda.
- **Selos/badges rotacionados** com borda branca: vermelho "CUIDADO!", verde para afirmação; balões e interrogações quando o tema é dúvida.
- **Foto dela grande à direita com expressão exagerada** (choque, mão na boca, dedo em riste, mãos na cabeça); frame do próprio vídeo serve, com contraste/saturação levantados.
- **Props e grafismos**: produto em cena (caneta, caixa de remédio), setas grossas vermelhas/amarelas apontando, X vermelho sobre comida, inset de foto com borda branca.
- Sem travessão no lettering; produto citado por nome apenas quando o vídeo já o faz.
- Fluxo prático: extrair frame expressivo do bruto (folha de contato com ffmpeg), recortar a região da pessoa, subir saturação/contraste, compor com texto e grafismos.

## Gotchas técnicos

Ver a seção "Gotchas essenciais" do `CLAUDE.md` deste repo (herdados e validados no ana-conteudo). Detalhes completos e histórico: repo `suportezv/ana-conteudo`.
