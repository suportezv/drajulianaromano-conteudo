import React from "react";
import { Composition } from "remotion";
import { CartaoTitulo } from "./CartaoTitulo";

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="CartaoTituloVertical"
      component={CartaoTitulo}
      durationInFrames={150}
      fps={30}
      width={1080}
      height={1920}
      defaultProps={{
        titulo: "Engordou na menopausa? A culpa não é sua",
        destaque: "culpa",
        rodape: "@drajulianaromano",
      }}
    />
    <Composition
      id="CartaoTituloQuadrado"
      component={CartaoTitulo}
      durationInFrames={150}
      fps={30}
      width={1080}
      height={1080}
      defaultProps={{
        titulo: "Engordou na menopausa? A culpa não é sua",
        destaque: "culpa",
        rodape: "@drajulianaromano",
      }}
    />
  </>
);
