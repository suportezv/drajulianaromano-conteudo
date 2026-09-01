# Design System · Dra. Juliana Romano

Sistema visual da marca para todas as peças do estúdio (capas de YouTube, posts, stories, documentos). Versão 1, montada em 2026-09-01 a partir da paleta oficial fornecida pela agência, do logo e da identidade observada no canal.

**Canvas editável no Claude Design**: https://claude.ai/code/artifact/234082d8-e98c-4cc9-9064-ec15b57f8c4a
Os arquivos-fonte do canvas estão em `canvas/` (editar aqui e republicar, ou editar direto no canvas).

## Cores

| Token | Hex | Papel |
|---|---|---|
| French Blue | `#7A96B8` | Primária (estrutura, destaques frios) |
| Gold | `#C9A24B` | Primária (destaque nobre, filetes, logo) |
| Navy | `#2B3A5E` | Primária (fundos escuros, texto sobre claro) |
| Champagne | `#E6CFA9` | Apoio (fundos quentes, detalhes) |
| Ivory | `#F6F1E6` | Apoio (fundo claro padrão, texto sobre navy) |

Regras: base clara em Ivory/Champagne (~60%), estrutura em Navy/French Blue (~30%), Gold só como destaque (~10%). Texto longo: Navy sobre Ivory ou Ivory sobre Navy. Gold nunca em corpo de texto. Sem verde/vermelho de alerta, sem neon, sem preto puro.

## Tipografia

- **Display**: Cormorant Garamond (600; itálico 500 para apoio). Caps com espaçamento aberto (0.12em a 0.42em), como no logo. Fallback: Georgia.
- **Apoio/corpo**: Jost (400 corpo, 600 destaques; caps 0.2em+ em eyebrows, botões, rótulos). Fallback: Segoe UI / system-ui.
- Escala de referência: H1 64px, H2 40px, eyebrow 14px, corpo 18px.

## Logo

Monograma circular dourado + wordmark. O arquivo oficial (SVG/PNG) deve ficar em `assets/logo/` (**PENDENTE: importar**; o canvas usa um desenho aproximado marcado para substituição).

## Aplicações no canvas

- **Capa YouTube (1280x720)**: variante escura (fundo Navy) e clara (fundo Ivory); texto gigante à esquerda, foto real da Dra. Ju recortada à direita, monograma + nome na base. Chip "Marca" alterna a cor de destaque.
- **Capa Instagram (1080x1350)**: foto dominante + faixa Navy inferior com eyebrow Gold, título Cormorant e handle.

## Regras editoriais (valem em toda peça)

- Nunca usar travessão em texto público; reescrever a frase.
- Tom: autoridade médica acolhedora, sem sensacionalismo agressivo. Credenciais: CRM-SP 138885, RQE 5246.

## Fontes de verdade e pendências

- Paleta e logo: fornecidos pela agência (2026-09-01).
- **PENDENTE**: validar contra o site https://drajulianaromano.com.br/ e o Instagram (bloqueados no environment desta sessão; liberar os domínios ou fornecer screenshots) e contra o brand book "Dra Juliana V2.pdf" do Drive (não é público; tornar acessível ou exportar as páginas-chave).
