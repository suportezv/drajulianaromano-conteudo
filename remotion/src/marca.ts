/**
 * Paleta e tokens da Dra. Juliana Romano, espelhando design-system/tokens.json.
 *
 * Os NOMES das chaves sao o contrato compartilhado entre os estudios irmaos
 * (Aurora.tsx e CartaoTitulo.tsx leem daqui e vao sem edicao de um estudio
 * para outro). Por isso os nomes ainda falam em "rosa" e "violeta": aqui eles
 * carregam o papel, nao a cor. O papel de cada um:
 *   rosaVivo   = destaque (palavra-chave do titulo e 1a mancha da aurora)
 *   violeta    = 2a mancha da aurora
 *   ciano      = 3a mancha da aurora
 *   rosaSuave  = 4a mancha da aurora
 *   auroraBase = fundo claro
 *   tinta      = texto
 */
export const marca = {
  /** goldDeep: o Gold puro (#C9AA6E) nao tem contraste sobre Ivory para texto. */
  rosaVivo: "#A6874B",
  /** Gold do logo. */
  rosa: "#C9AA6E",
  /** Champagne. */
  rosaSuave: "#E6CFA9",
  /** French Blue. */
  violeta: "#7A96B8",
  /** Blue Mist. */
  ciano: "#BFC9DC",
  /** French Blue (sem neon nesta marca). */
  azulNeon: "#7A96B8",
  /** Navy. */
  azulProfundo: "#2B3A5E",
  /** Navy Ink: fundo escuro. Sem preto puro nesta marca. */
  fundoEscuro: "#1C2740",
  superficie: "#2B3A5E",
  /** Ivory: base clara dos fundos aurora. */
  auroraBase: "#F6F1E6",
  /** Navy: texto sobre claro (regra do design system). */
  tinta: "#2B3A5E",
  /** Playfair Display e a display do site; sem rede no render, cai para Georgia. */
  fonte: '"Playfair Display", Georgia, "Times New Roman", serif',
} as const;
