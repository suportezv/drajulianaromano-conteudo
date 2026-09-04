# Prompt para executar capa de YouTube no Claude Design

Template usado na capa da Menopausa (2026-09-04). Para uma capa nova: gerar os 3 assets
(fundo temático IA, recorte da foto do ensaio, prop 3D) via Higgsfield, trocar os textos
e as cores de acento pelo tema, e anexar os arquivos junto com o prompt.

## Anexos esperados

1. `fundo.png` — fundo temático 16:9 gerado por IA (nano_banana_pro), sem pessoas nem texto.
2. `foto-recorte.png` — foto do ensaio com fundo removido (Higgsfield remove_background).
3. `prop-balanca.png` — prop 3D com fundo removido.
4. `referencia-final.png` — render de referência (opcional, guia de composição).

Assets da capa da Menopausa (CDN do Higgsfield, abrir no navegador):

- fundo: https://d8j0ntlcm91z4.cloudfront.net/user_3Gxf3cva3WVcb6W9GRwN2TbNkt5/hf_20260904_191121_1396c91e-64d2-49be-b694-ab1e85338940.png
- recorte: https://d8j0ntlcm91z4.cloudfront.net/user_3Gxf3cva3WVcb6W9GRwN2TbNkt5/hf_20260904_191126_dc33e0ca-5749-453e-84cd-cddd3ccc096a.png
- prop: https://d8j0ntlcm91z4.cloudfront.net/user_3Gxf3cva3WVcb6W9GRwN2TbNkt5/hf_20260904_191342_aef157f7-ef1b-4818-b043-019e4dd9eb2b.png
- referência: https://d2ol7oe51mr4n9.cloudfront.net/user_3Gxf3cva3WVcb6W9GRwN2TbNkt5/0e6ddf72-d6c3-4477-bc37-4483f8788cd3.png
- foto original (Drive público): https://drive.usercontent.google.com/download?id=18004CM59gqY415qC7Qm8vASzktHHuRgt&export=download&confirm=t

## Prompt

```
Crie um artboard 1280x720 (capa de YouTube) para o canal da Dra. Ju Romano, no estilo
"thumb de performance" agressivo. Anexei 4 imagens: o fundo, o recorte da foto, o prop
e uma referência de composição final — reproduza a referência, melhorando acabamento.

FUNDO
- fundo.png cobrindo todo o artboard (cover), saturação +18%, contraste +6%.
- Gradiente escuro da esquerda por cima (rgba(8,4,16) 100% -> transparente em 62% da largura)
  para dar leitura ao texto.
- Vinheta sutil nas bordas (escurecer ~35%).

FOTO (lado direito)
- foto-recorte.png com altura 850px (18% maior que o artboard), ancorada no rodapé,
  encostada na borda direita (pode vazar ~6% para fora à direita e cortar a base).
- Tratamento: filter: contrast(1.13) saturate(1.15) brightness(1.02).
- Rim light: drop-shadow(-6px 0 6px rgba(255,90,220,0.85)) na borda esquerda (magenta)
  e drop-shadow(8px -2px 10px rgba(255,214,120,0.7)) na direita (dourado).
- Glow roxo grande atrás dela (elipse #A83CBE desfocada ~70px, blend screen) e sombra
  preta desfocada projetada à esquerda dela sobre o fundo.

TEXTO (coluna esquerda, fonte Anton do Google Fonts, tudo CAPS)
- Bloco inclinado: skewX(-7deg) e rotate(1.6deg) no conjunto.
- Linha 1 "ENGORDOU NA": 118px, branco #FFFFFF, contorno preto 10px, sombra dura
  7px 8px rgba(0,0,0,0.85). Posição ~x30 y40.
- Linha 2 "MENOPAUSA?": 158px, colada na linha 1 (line-height ~0.95). Preenchimento com
  gradiente vertical dourado #FFF096 -> #CE6E08 (background-clip: text), contorno preto
  11px (fazer em camada duplicada atrás), glow dourado externo suave
  (drop-shadow 0 0 18px rgba(255,200,60,0.55)) e sombra dura preta.
- Faixa vermelha: retângulo #C41018 com cantos 8px, borda inferior mais escura #8C060E,
  rotacionado -2.4deg, em ~x48 y455; dentro, "A CULPA NÃO É SUA" em Anton 48px branco.
  Sombra dura preta na faixa.

ELEMENTOS DE APOIO
- Duas interrogações "?" em Anton amarelo #FFE234 com contorno preto 8px e sombra:
  uma 120px rotacionada -14deg em ~x730 y25, outra 85px rotacionada 12deg em ~x1165 y150.
- Seta curva amarela #FFE234 com contorno preto grosso, saindo de baixo da faixa
  (~x165 y580) e apontando para a balança (~x505 y645), ponta triangular cheia.
- prop-balanca.png com 460px de largura em ~x530, vazando ~35px abaixo do rodapé;
  contraste +12%, saturação +20%, brilho +8%; glow magenta desfocado atrás
  (rgba(255,60,160)) e sombra preta desfocada abaixo.

ORDEM DAS CAMADAS (de trás pra frente): fundo -> gradiente escuro -> glow roxo ->
sombra da foto -> foto -> glow do prop -> sombra do prop -> prop -> seta ->
interrogações -> bloco de texto -> faixa -> vinheta.

REGRAS: nunca usar travessão em texto; não adicionar outros textos, logos ou marcas
d'água; manter a área da esquerda legível em miniatura (teste mental a 320px de largura).
```

## Paleta de acentos por tema (referência das capas antigas)

- Perigo/alerta: fundo fogo/vermelho, faixa vermelha #C41018, palavras-chave em amarelo #FFE234.
- Promessa/solução: verde #17B24A na faixa ou palavra-chave.
- Dúvida/pergunta: interrogações amarelas, fundo roxo/azulado com glow.
- Keyword principal: sempre gradiente dourado #FFF096 -> #CE6E08 com contorno preto.
