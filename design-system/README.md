# Design System · Dra. Juliana Romano

Sistema visual da marca para todas as peças do estúdio (capas de YouTube, posts, stories, documentos). **Versão 2 (2026-09-01)**: validado contra o site oficial (fontes, logo, copy e posicionamento), a paleta oficial da agência e o padrão de capas do canal.

**Canvas editável no Claude Design**: https://claude.ai/code/artifact/234082d8-e98c-4cc9-9064-ec15b57f8c4a
Arquivos-fonte do canvas em `canvas/`; tokens em `tokens.css` e `tokens.json`; logo em `assets/logo/`.

## Cores

| Token | Hex | Papel |
|---|---|---|
| French Blue | `#7A96B8` | Primária (estrutura, destaques frios) |
| Gold | `#C9AA6E` | Primária (dourado exato do logo; filetes, títulos, detalhes) |
| Navy | `#2B3A5E` | Primária (fundos escuros, texto sobre claro) |
| Champagne | `#E6CFA9` | Apoio (fundos quentes, detalhes) |
| Ivory | `#F6F1E6` | Apoio (fundo claro padrão, texto sobre navy) |

Regras: base clara Ivory/Champagne (~60%), estrutura Navy/French Blue (~30%), Gold só como destaque (~10%). Texto longo: Navy sobre Ivory ou Ivory sobre Navy. Gold nunca em corpo de texto. Sem verde/vermelho de alerta, sem neon, sem preto puro.

**Legado** (não usar em peças novas): petróleo do site atual (`#1F3642`, `#3B5E70`, `#6C8FA3`), vinho do favicon (`#6F2848`) e a versão verde do logo usada no banner atual do YouTube. A nova identidade substitui todas.

## Tipografia (fontes oficiais do site)

- **Display**: Playfair Display (600-800; itálico para ênfase elegante). Caps com espaçamento aberto em eyebrows. Fallback: Georgia.
- **Apoio/corpo**: Montserrat (400 corpo, 600-800 destaques; caps 0.2em+ em rótulos e botões). Fallback: Segoe UI / system-ui.
- Escala: H1 64px, H2 40px, eyebrow 14px, corpo 18px.

## Logo (oficial, extraído do site)

- `assets/logo/logo-horizontal-dourado.png`: monograma + wordmark dourados, para fundo claro.
- `assets/logo/logo-horizontal-branco.png`: monograma dourado + wordmark branco, para fundo escuro.
- `assets/logo/monograma-dourado.png`: símbolo isolado (também usado como marca d'água nas capas).
- Dourado do logo: `#C9AA6E`. Para impressão/alta resolução, pedir o vetor (SVG/AI) à cliente.

## Voz e posicionamento (do site)

- Promessa: "Eu não só te ajudo a emagrecer, te ajudo a se tornar **bela, magra e livre** do efeito sanfona."
- **Método Bella & Magra**, 3 pilares (nomes completos da bio do canal): Medicina Metabólica em 360º, Remodelação Corporal Avançada, Código Secreto do Inconsciente. Instituto Romano.
- Público: **mulheres 35+**. Especialidade: nutrologia e emagrecimento feminino. Assinatura pessoal: **Mãe, Médica e CEO**. Tom: autoridade médica que acolhe; provocação elegante, sem terrorismo.
- CTA institucional: "Sua transformação começa com uma decisão."
- Credenciais sempre completas: CRM-SP 138885, RQE 5246.

## Aplicações no canvas

- **Capa YouTube (1280x720)**: variante escura (Navy, tema alerta) e clara (Ivory, tema pergunta); texto gigante à esquerda (Montserrat caps + palavra-chave em Playfair), foto oficial recortada da Dra. Ju à direita, monograma como marca d'água, logo na base. Chip "Marca" alterna a cor de destaque.
- **Capa Instagram (1080x1350)**: foto dominante + bloco Navy inferior com eyebrow Gold, título Playfair e logo.
- **Banner YouTube (2048x1152)**: substitui o banner verde atual; conteúdo dentro da área segura de 1235x338 (logo, promessa em Playfair itálico, assinatura Mãe, Médica e CEO, foto oficial).

## Regras editoriais (valem em toda peça)

- Nunca usar travessão em texto público; reescrever a frase.
- Loudness de vídeo -14 LUFS; palavrão se bipa, não se corta.
