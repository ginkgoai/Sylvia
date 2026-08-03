---
title: "GKO - Criar credenciais MCP Google Apify ElevenLabs"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68d75379-99ec-8322-a1ef-97d933db7e72"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 27 de set. às 0:05

Bora credenciar tudo certinho — sem gambiarra, sem dor de cabeça. Abaixo vai um passo a passo direto-ao-ponto pra criar e guardar credenciais de **MCP servers**, **Google Drive**, **Apify** e **ElevenLabs**, já no formato que casa com n8n, Docker/EasyPanel e teu agente BRANN.

---

## 0) Regras de ouro (vale pra todas)

1. **Nomes e `.env` padrão**
	- Use um `.env` único (produção) e um para **dev**.
		- Prefixe por ambiente: `PROD_…`, `DEV_…`.
		- Exemplos:
		```markdown
		PROD_GOOGLE_CLIENT_ID=
		PROD_GOOGLE_CLIENT_SECRET=
		PROD_GOOGLE_REFRESH_TOKEN=
		PROD_APIFY_TOKEN=
		PROD_ELEVENLABS_API_KEY=
		```
2. **Nunca commitar chave** em repositório. Se for usar Docker, prefira `env_file` + **secrets** quando possível.
3. **Privilégio mínimo**: só os escopos que você realmente precisa.
4. **Rotacione** chaves sensíveis a cada 60–90 dias (põe um lembrete).
5. **Teste rápido** (curl ou nó “ping”) sempre após criar.

---

## 1) Google Drive (OAuth de usuário – o mais simples com n8n)

> Ideal quando o agente age “como você”, acessando seu Drive.

**Passo a passo no Google Cloud Console**

1. Acesse o **Google Cloud Console** e crie um projeto (ou escolha um existente).
2. Em **APIs e serviços → Biblioteca**, **ative** a **Google Drive API**.
3. Vá em **Tela de consentimento OAuth**:
	- Tipo: *External* (se não for workspace) ou *Internal* (no Workspace).
		- Preencha nome do app, e-mail, domínio (se tiver), e **adicione escopos** que você precisa, ex.:
		- `.../auth/drive.readonly` (somente leitura)
				- `.../auth/drive` (leitura/escrita)
4. **Credenciais → Criar credenciais → ID do cliente OAuth 2.0**.
	- Tipo: **Aplicativo da Web** (para n8n em servidor) ou **Aplicativo para Desktop** (para testes locais).
		- Se for **n8n** em domínio: adicione **URI de redirecionamento**
		```markdown
		https://SEU-DOMINIO/rest/oauth2-credential/callback
		```
5. Salve o **Client ID** e o **Client Secret**.

**Conectar no n8n**

1. Em **Credentials → New**, escolha **Google Drive OAuth2 API**.
2. Selecione **“Custom App”** e cole **Client ID** e **Client Secret**.
3. Escopos: os mesmos que você habilitou (ex.: `drive.readonly` ou `drive`).
4. Clique **Connect OAuth2** → faça login na **conta que tem os arquivos/pastas** do Drive.
5. Ao concluir, o n8n guarda **access\_token** e **refresh\_token**. Copie os valores (se quiser espelhar no `.env`):
	```markdown
	PROD_GOOGLE_CLIENT_ID=xxx.apps.googleusercontent.com
	PROD_GOOGLE_CLIENT_SECRET=xxx
	PROD_GOOGLE_REFRESH_TOKEN=1//0g...
	```
6. Teste com um nó **Google Drive → List** (listar arquivos de uma pasta).

**Erros comuns & correção**

- `redirect_uri_mismatch`: o URI de callback do n8n não bate com o do Console. Corrija e salve.
- `insufficient_permissions`: faltou escopo na tela de consentimento ou no cred do n8n.
- Não aparece a pasta? É outra conta. Verifique qual conta autorizou o OAuth.

> **Dica:** Service Account para Drive funciona se **compartilhar a pasta** com o e-mail do service account. Mas no n8n, o **OAuth de usuário** costuma ser mais simples e compatível.

---

## 2) Apify (token simples, sem drama)

**Criar token**

1. Entre no painel **Apify** → **Settings/Account** → **API Tokens**.
2. **Generate new token**, nomeie (ex.: `n8n-prod-2025-09`) e copie.

**Salvar**

```markdown
PROD_APIFY_TOKEN=apify_api_xyz...
```

**Conectar no n8n**

- Em **Credentials → New**, escolha **Apify** e cole o token.
- Teste com nó **Apify → Run Actor** (ou HTTP Request com header `Authorization: Bearer ${PROD_APIFY_TOKEN}`).

**Teste rápido (curl)**

```markdown
curl -H "Authorization: Bearer $PROD_APIFY_TOKEN" https://api.apify.com/v2/me
```

**Erro comum**

- `401 Unauthorized`: token expirado/errado ou faltou o `Bearer`.

---

## 3) ElevenLabs (API Key para TTS/voz)

**Criar chave**

1. No painel **ElevenLabs** → **Profile → API Keys**.
2. **Create new key**, nomeie por ambiente (ex.: `prod-brann-audio`).

**Salvar**

```markdown
PROD_ELEVENLABS_API_KEY=eleven_...
```

**Conectar no n8n**

- Se existir **credential ElevenLabs**, selecione e cole a key.
- Se usar **HTTP Request**, adicione header:
	```markdown
	xi-api-key: {{$env.PROD_ELEVENLABS_API_KEY}}
	```
- Teste endpoint **GET** `https://api.elevenlabs.io/v1/user` (deve retornar dados da conta).

**Erros comuns**

- `401` / `403`: header incorreto (tem que ser `xi-api-key`) ou key inválida.
- Voz não encontrada: confira o **voice\_id** escolhido.

---

## 4) MCP Servers (Model Context Protocol)

A lógica é: cada servidor MCP lê **variáveis de ambiente** com suas credenciais e expõe **tools** ao agente (BRANN). Você passa o `.env` para o contêiner/serviço do servidor.

**Padrão de `.env` (exemplo genérico)**

```markdown
# Google
PROD_GOOGLE_CLIENT_ID=
PROD_GOOGLE_CLIENT_SECRET=
PROD_GOOGLE_REFRESH_TOKEN=

# Apify
PROD_APIFY_TOKEN=

# ElevenLabs
PROD_ELEVENLABS_API_KEY=
```

**Exemplo Docker/EasyPanel (genérico)**

```markdown
services:
  mcp-google-drive:
    image: ghcr.io/sua-org/mcp-google-drive:latest
    env_file: .env
    environment:
      GOOGLE_CLIENT_ID: ${PROD_GOOGLE_CLIENT_ID}
      GOOGLE_CLIENT_SECRET: ${PROD_GOOGLE_CLIENT_SECRET}
      GOOGLE_REFRESH_TOKEN: ${PROD_GOOGLE_REFRESH_TOKEN}

  mcp-apify:
    image: ghcr.io/sua-org/mcp-apify:latest
    env_file: .env
    environment:
      APIFY_TOKEN: ${PROD_APIFY_TOKEN}

  mcp-elevenlabs:
    image: ghcr.io/sua-org/mcp-elevenlabs:latest
    env_file: .env
    environment:
      ELEVENLABS_API_KEY: ${PROD_ELEVENLABS_API_KEY}
```

> Os nomes das imagens/vars variam por servidor MCP específico. A regra é essa: **mapear as credenciais via env** exatamente como o server espera. Se o server permite config por arquivo (ex.: `mcp.config.json`), você referencia `process.env.VAR`.

**Wire-up no agente**

- No **cliente MCP** (teu agente/runner), aponte para os endpoints/ports dos servidores acima.
- Garanta health-check: suba cada server e use uma tool simples para “pingar” (ex.: listar arquivos no Drive, pegar `me` no Apify, `user` no ElevenLabs).

---

## 5) n8n: boas práticas de credenciais

- **Credentials por serviço**:
	- *Google Drive OAuth2 API*: um cred por ambiente (ex.: `google-drive-prod`).
		- *Apify*: um cred simples com o token.
		- *ElevenLabs*: um cred simples com a API key.
- **Referências**: nos nós, selecione o **credential** pelo nome.
- **Base URL do n8n**: em produção, defina `N8N_HOST` / `N8N_PROTOCOL` / `WEBHOOK_URL` certinho pra o OAuth voltar pro callback correto.

**Docker do n8n (essencial para OAuth)**

```markdown
services:
  n8n:
    image: n8nio/n8n:latest
    env_file: .env
    environment:
      N8N_HOST: automacoes.seu-dominio.com
      N8N_PROTOCOL: https
      WEBHOOK_URL: https://automacoes.seu-dominio.com/
      N8N_SECURE_COOKIE: true
    ports:
      - "5678:5678"
```

---

## 6) Checklist Ninja de Teste (cola e executa)

1. **Google Drive**
	- No n8n: nó *Google Drive → List* em uma pasta pública e outra privada. Rodar.
		- Se falhar, checar escopos e conta logada.
2. **Apify**
	- `curl https://api.apify.com/v2/me` com `Authorization: Bearer`.
		- No n8n: rodar um Actor simples (ex.: “hello world”/demo).
3. **ElevenLabs**
	- `GET /v1/user` (HTTP Request).
		- Rodar **TTS** com uma voz padrão para um texto curto (“Teste BRANN”).
4. **MCP**
	- Do agente, chamar a tool de **listar arquivos** (Drive), **get me** (Apify), **get user** (ElevenLabs).
		- Se a tool não aparece: checar variáveis e logs do server MCP.

---

## 7) Pega-ratão clássico (e como evitar)

- **Google `redirect_uri_mismatch`**: o callback no Console e no n8n **devem ser idênticos**.
- **Drive com Service Account “vazio”**: esqueceu de **compartilhar a pasta** com o e-mail do service account.
- **Apify 401**: faltou `Bearer` ou token expirado.
- **ElevenLabs 401/403**: header `xi-api-key` errado (ou key inválida).
- **n8n atrás de proxy**: `N8N_HOST/WEBHOOK_URL` mal configurados quebram o OAuth.
- **Escopo grande demais**: aprovação de verificação do app (Google) pode travar. Use só o necessário.

---

## 8) Prontos pra colar: blocos.env de exemplo

```markdown
# === PROD ===
PROD_GOOGLE_CLIENT_ID=xxx.apps.googleusercontent.com
PROD_GOOGLE_CLIENT_SECRET=xxx
PROD_GOOGLE_REFRESH_TOKEN=1//0g...

PROD_APIFY_TOKEN=apify_api_xyz...
PROD_ELEVENLABS_API_KEY=eleven_abc...

# n8n
N8N_HOST=automacoes.seu-dominio.com
N8N_PROTOCOL=https
WEBHOOK_URL=https://automacoes.seu-dominio.com/
N8N_SECURE_COOKIE=true
```

---

Quer o próximo passo já mastigado? Posso te entregar os **arquivos de credenciais do n8n** (export JSON) e um **compose** base dos MCP servers com as `environment` prontas pra produção. Depois disso, o BRANN só precisa apertar “play” e cantar no teu ouvido com voz de locutor épico.