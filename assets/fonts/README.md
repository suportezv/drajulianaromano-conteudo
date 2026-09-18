# Fontes da marca (arquivos locais)

Google Fonts fica fora da allowlist do environment, então as fontes oficiais do site vivem aqui como TTF variável (licença SIL OFL 1.1, textos ao lado):

- `PlayfairDisplay[wght].ttf`: display (títulos, palavra-chave, cartões Remotion).
- `Montserrat[wght].ttf`: apoio e corpo.

O `scripts/setup.sh` copia tudo de `assets/fonts/*.ttf` para `~/.fonts` e roda `fc-cache`; a partir daí o Chromium/headless_shell (Remotion, Playwright) e o PIL (`ImageFont.truetype` pelo caminho do arquivo) enxergam as famílias pelo nome. Origem: sparse clone de `github.com/google/fonts` (`ofl/playfairdisplay`, `ofl/montserrat`), 2026-09-18.
