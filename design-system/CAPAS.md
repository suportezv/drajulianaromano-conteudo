# Estudo definitivo: capas de vídeo longo do canal

Estudo feito em 2026-09-02 sobre as capas profissionais antigas do canal (baixadas em alta via i.ytimg.com; referências: "O Perigo do Mounjaro", "Contrave", "Emagreça e Nunca Mais Engorde", "Entenda as Diferenças", "Mitos e Verdades", "O Melhor Remédio para Emagrecer", "Mounjaro Realmente Funciona"). O padrão provisório usado nos 2 primeiros agendamentos (frames de vídeo, fundo chapado) fica substituído por este.

## Anatomia das capas de referência

1. **Foto profissional, nunca frame de vídeo.** Ensaio de estúdio (blazer branco com pedraria, colete preto, blazer azul), recorte limpo, pose com intenção (segurando canetas, mão no queixo, palma aberta, braços cruzados). Frame de vídeo só em último caso.
2. **Tratamento da foto (o que dá o efeito de qualidade/profundidade):**
   - grading amarrando a foto ao fundo (quente no fogo, frio no azul);
   - **rim light / glow colorido na borda do recorte** na cor do fundo;
   - contraste e nitidez altos, pele tratada;
   - leve sombra projetada da pessoa sobre o fundo.
3. **Fundos chamativos e temáticos, nunca chapados:** fogo/brasa com fumaça e fagulhas (perigo), explosão de raios dourado-vermelhos (impacto), roxo com glow (produto), vinho/magenta com props espalhados (editorial), preto com feixes (comparativo). Sempre com textura, partículas e luz direcional.
4. **Sistema de texto:** caps condensado extra bold; branco + amarelo-ouro (às vezes com **gradiente vertical dourado**) como dupla base; verde para promessa, vermelho para perigo; contorno preto grosso + sombra dura; **faixa de pincelada vermelha** atrás da palavra-chave; badge rotacionado com borda branca ("CUIDADO!").
5. **Prop gigante em destaque:** produto em close 3D (cápsulas, canetas, caixas) com **seta branca/vermelha estilizada** apontando; comparativos com X vermelho; insets de foto com borda.
6. **Composição:** foto ocupa 35-45% à direita (às vezes só rosto/busto), texto e prop na esquerda, leitura em Z, tudo respirando.

## Por que a v1 (frames) ficou pior

Frame de vídeo tem luz de gravação, ruído e sem recorte; sem rim light nem sombra a pessoa não descola do fundo; fundo chapado sem textura mata a profundidade; texto de uma cor só sem gradiente perde o acabamento; sem prop 3D falta âncora visual.

## Pipeline definitivo (validado em 2026-09-02 com a capa-piloto)

1. **Foto**: escolher no Drive (pastas ENSAIO JU ROMANO / retratos profissionais) pela pose que casa com o tema. **Sempre foto; frame só se não houver pose adequada.**
2. **Recorte**: remoção de fundo por IA (Higgsfield `remove_background`; Kairogen quando contratado).
3. **Fundo**: gerado por IA (Higgsfield `generate_image`, modelo nano_banana_pro; Kairogen quando contratado) com prompt temático: "YouTube thumbnail background only, no people, no text, [tema: brasas/raios/roxo/...], cinematic, 16:9".
4. **Props**: produto/ilustração gerados por IA quando não houver foto real.
5. **Composição**: sandbox do Higgsfield (`sandbox_exec`: Pillow + fontes + internet livre) com a receita: fundo cover 1280x720 + escurecimento à esquerda; glow laranja/da cor do fundo atrás do recorte (alpha borrado, blend screen); foto graduada (contraste 1.09, saturação 1.1, blend quente 5%); rim light fino na borda (alpha menos erosão, screen dourado); texto Anton com contorno e sombra; keyword com gradiente vertical dourado (255,232,130 → 212,120,20); faixa vermelha (160,16,16) rotacionada ~1.5º; badge com borda branca rotacionado ~3º.
6. **Saída**: upload para o storage do Higgsfield (media_upload + PUT + media_confirm) e agendamento com a URL; commit do PNG no repo quando o CDN estiver liberado no environment.

Capa-piloto de validação: https://d2ol7oe51mr4n9.cloudfront.net/user_3Gxf3cva3WVcb6W9GRwN2TbNkt5/44c238e8-18cf-4025-b764-c4565a40fe1e.png

## Bloqueios e dependências

- **Fotos do Drive não são públicas** (redirecionam para login). Liberar "qualquer pessoa com o link: leitor" na pasta DRA JULIANA ROMANO (um clique cobre as subpastas). Sem isso, só a foto do site está acessível.
- **Kairogen: 0 créditos** (plano free). Enquanto isso, Higgsfield da conta (plano Max, ~1497 créditos) cobre geração de fundo, remoção de fundo e o sandbox de composição.
- Environment local bloqueia os CDNs do Higgsfield (`d8j0ntlcm91z4.cloudfront.net`, `d2ol7oe51mr4n9.cloudfront.net`); liberar para permitir commit dos PNGs no repo e envio de arquivos na conversa. O agendamento não depende disso (o Metricool busca a URL server-side).
