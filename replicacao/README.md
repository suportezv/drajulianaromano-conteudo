# Replicação: como criar o estúdio de conteúdo de uma nova marca

Guia para replicar esta infraestrutura para qualquer cliente da agência. Os templates desta pasta não contêm nenhum dado de clientes anteriores; tudo que é específico da marca entra por placeholder.

## Placeholders usados nos templates

| Placeholder | O que é | Exemplo de formato |
|---|---|---|
| `{{MARCA}}` | Nome público da marca/criador | Nome como aparece no perfil |
| `{{REPO}}` | Nome do repositório do estúdio | `<slug-da-marca>-conteudo` |
| `{{CREDENCIAL}}` | Credencial completa do criador quando citado em texto público | Título profissional completo |
| `{{CTA}}` | CTA padrão da marca | Frase curta + "Link na bio." |

## Dados a coletar da marca antes de começar

1. Nome público e slug do repo.
2. Handle do Instagram e lista de redes conectadas (Facebook, TikTok, YouTube, LinkedIn, Pinterest).
3. Credencial completa do criador (como deve ser citada em público).
4. CTA padrão.
5. Posicionamento, persona/tom de voz e pilares de conteúdo.
6. Voz para narração: voice_id na ElevenLabs (ou amostra de áudio aprovada para clonar; exige plano pago).
7. Pasta de brutos no Google Drive (compartilhamento "qualquer pessoa com o link: leitor").
8. Cor de acento do lettering (padrão da agência se não houver manual da marca).

## Passo a passo

### 1. Repositório

Criar repo **público** `suportezv/{{REPO}}` (público é requisito: a mídia temporária para o Metricool é servida via raw.githubusercontent.com).

### 2. Infraestrutura compartilhada (copiar sem editar)

De qualquer estúdio existente da agência, copiar para o repo novo:

```
scripts/          (setup.sh e validate.sh são agnósticos de marca)
patches/          (video-use-is-portrait-source.patch)
.gitignore
assets/fonts/.gitkeep
projects/.gitkeep
```

### 3. Memória da marca (gerar dos templates)

Copiar `CLAUDE.template.md` para `CLAUDE.md` e `FRAMEWORK.template.md` para `FRAMEWORK.md` na raiz do repo novo, substituindo os placeholders:

```bash
sed -i 's/{{MARCA}}/Nome Da Marca/g; s/{{REPO}}/slug-conteudo/g' CLAUDE.md FRAMEWORK.md
```

Campos que ficarem sem resposta permanecem marcados **PENDENTE** no texto; a primeira sessão preenche e commita conforme forem confirmados.

### 4. Environment cloud (claude.ai/code)

No ícone de nuvem acima da caixa de mensagem, duplicar o environment padrão da agência (ou criar um novo com o nome do estúdio):

- Network access **Custom** com os domínios: `drive.google.com`, `drive.usercontent.google.com`, `api.elevenlabs.io`.
- Env var `ELEVENLABS_API_KEY` (chave `sk_` de 51 caracteres; nunca colar a chave no chat).
- Setup script: `bash scripts/setup.sh`.

Mudanças de environment valem apenas para sessões novas.

### 5. Conectores MCP (claude.ai, conta da agência)

Nas configurações de conectores, autorizar e habilitar no chat:

- **Google Drive** (conta com acesso às pastas de brutos).
- **Metricool** (conta da agência).
- **Kairogen** (conta da agência; conferir plano e créditos antes de usar).

### 6. Painel do Metricool

Conectar a marca nova no painel (Instagram e todas as demais redes dela), timezone America/Sao_Paulo. O blog_id pode ser anotado manualmente ou descoberto pela primeira sessão via `getBrandSettings` e commitado no `CLAUDE.md`.

### 7. Primeira sessão

Abrir sessão nova no environment do estúdio e colar o conteúdo de `PROMPT-INICIAL.template.md` com os placeholders preenchidos. A sessão vai rodar setup e validação, testar rede, conectores e chave, preencher os PENDENTE que conseguir e commitar tudo no `CLAUDE.md`.

## Checklist de validação final

1. `bash scripts/setup.sh` e `bash scripts/validate.sh` sem FALHOU.
2. Rede: `curl -s -o /dev/null -w "%{http_code}" https://drive.google.com/` responde HTTP (não 000).
3. Metricool: `getBrandSettings` lista a marca com o blog_id documentado.
4. ElevenLabs: chave validada (TTS, STT Scribe, sound-generation, voices_read); conferir plano e cota de caracteres.
5. Kairogen: `get_me_context` mostra plano pago e créditos.
6. Drive: conector lista arquivos; download direto por curl funciona na pasta de brutos.
7. `CLAUDE.md` e `FRAMEWORK.md` commitados com os dados da marca (sem PENDENTE crítico aberto).

## Regras da agência (valem para todas as marcas)

- Nunca usar travessão em texto público: reescrever a frase.
- Palavrão em vídeo se bipa, não se corta.
- Loudness final: -14 LUFS.
- Agendamento: sempre incluir todos os canais conectados da marca, exceto YouTube horizontal. YouTube entra como Short (`youtubeData: {type: "short", title, madeForKids: false}`); Instagram e Facebook como REEL; TikTok, LinkedIn e Pinterest com networkData padrão.
- Preview na conversa para aprovação antes de agendar; agendar como rascunho.
- Todo aprendizado novo vira commit no `CLAUDE.md` do estúdio.
