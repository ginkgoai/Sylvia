---
title: "Agente Jurídico"
source: "https://chatgpt.com/c/69b5a03d-c3dc-832b-a7be-e98754b09192"
author:
published:
created: 2026-07-13
description: "ChatGPT conversation with 110 messages"
tags:
  - "clippings"
---
**Você disse**

Pesquise esse repositório e me explique como e para que usar

---

**Você disse**

Sim

---

**Você disse**

---

**Você disse**

---

**Você disse**

Conseguimos conectar o OpenClaw ao https://eproc1g.tjrs.jus.br/ com login para atuar como um Agente especialista que controla o andamento de todos os processos e dispara relatório semanais e atualiza automaticamente em um site dashboard simples para visualização do cliente com login por número do processo e chave

---

**Você disse**

VAMOS FAZER

---

**Você disse**

foi o 1

---

**Você disse**

COLEI TODOS SEQUENCIALMENTE, E AGORA? ONDE ENTRA O OPENCLAW E O FUNCIONAMENTO DE TUDO

---

**Você disse**

passso a passo

---

**Você disse**

não achei o src, voce consegue acessar meu github, assim verifica automaticamente tudo depois que eu sync

---

**Você disse**

repo: agentjury branch?

---

**Você disse**

---

**Você disse**

fiz tudo ate o passo 5

---

**Você disse**

---

**Você disse**

fiz um ambiente no codex para o repo, como podemos usar?

---

**Você disse**

oq sao essas opcoes

---

**Você disse**

---

**Você disse**

---

**Você disse**

---

**Você disse**

---

**Você disse**

---

**Você disse**

---

**Você disse**

\# Evolução: JURY AGENT para SaaS Multi-tenant 🚀 O projeto atual ativou com sucesso o esqueleto de Fastify e provou o conceito local. Para transformar isso num SaaS de escalabilidade real (Múltiplos Advogados/Escritórios assinando), precisamos migrar o comportamento de "Agente Único" para uma "Plataforma Core". ## 1. Visão da Arquitetura SaaS Mínima - \*\*Monolito Modular (Fastify)\*\*: Continuamos no Node.js, mas rigorosamente guiados por um banco de dados relacional. - \*\*Isolamento por Tenant (Inquilino)\*\*: Cada chamada ao banco e cada processo monitorado carrega um `tenantId` (ID do Escritório). Onde hoje temos parâmetros soltos, teremos JWT ou Chaves de API para garantir segurança. - \*\*Processamento Assíncrono Contínuo (BullMQ + Redis)\*\*: Scrapers são pesados e frágeis. Nenhuma chamada de cliente (`GET /process/123`) fará scraping em tempo real. O cliente vai ler do \*nosso\* bando de dados (cacheado) enquanto os \*Workers\* rodam de madrugada buscando novidades no eProc. - \*\*Frontend / Dashboard Separado\*\*: O backend atual servirá apenas JSON para um futuro painel Web (React/Vue/Nextjs) ou para o próprio celular via Telegram. ## 2. Módulos Principais do SaaS 1. \*\*API Central\*\*: Endpoints RESTful protegidos por JWT. 2. \*\*Workers (Filas)\*\*: Exclusivos para gerenciar as "Rodadas de Identificação" no eProc sem travar a API. 3. \*\*Módulo de Integração (Cheerio/Playwright)\*\*: O motor puro, plugado apenas aos workers. 4. \*\*LLM Engine & Bot\*\*: As "Skills" conversacionais operando em cima dos resultados extraídos no nosso DB. ## 3. Pasta Ideal do Projeto Para suportar o SaaS sem a base virar uma bagunça, a estrutura deve evoluir de uma organização "por ferramenta" para uma "por contexto":

```
text
src/
 ├── api/          # Servidor, Rotas, Middlewares (JWT e Tenant Scope)
 ├── core/         # Regras de Negócio Puras (Ex: services/processService.ts)
 ├── infra/        # Adaptadores (Prisma/Postgres, Redis, APIs de Terceiros)
 ├── workers/      # Jobs do BullMQ (worker de Scraping, worker de Alertas)
 ├── engine/       # A "Mágica" do eProc (auth, scraper, parser, diff)
 ├── bot/          # Lexra e Skills do Telegram
 └── utils/        # Loggers, formatadores, encrypters
```
\## 4. O Que Fica vs Deixado para Depois \*\*🟢 AGORA (Foco no Backing Sólido):\*\* - Instalação e modelagem do ORM (Prisma + Postgres). - Acoplamento do Parser/Scraper real aos Workers (para gravar no Postgres). - Autenticação e restrição da API baseada em Tenant. - Webhooks internos ou disparo do Bot do Telegram ao detectar diffs. \*\*🔴 DEPOIS (Pós-MVP):\*\* - Portal de Assinaturas & Faturamento (Stripe/MercadoPago). - Front-end complexo de Dashboard (Painel do Advogado). - Extração de diários oficiais completos. ## 5. Backlog de Evolução (5 Etapas) ### 📦 Etapa 1: Base de Dados & Multi-Tenancy (ORM) - Instalar Prisma ORM e modelar PostgreSQL para o domínio. - Tabelas primárias: `Tenant`, `Process`, `ProcessMovement` e `EprocCredential` criptografada. ### ⚙️ Etapa 2: A Esteira de Dados (Workers + Engine) - Plugar Scraper/Parser ao BullMQ. - O Worker fará polling silencioso nos processos ativos por `tenantId`, executará o `diff-engine` e sincronizará diferenças pro banco em background. ### 🛡️ Etapa 3: Proteção da API (JWT) - Implementar autenticação via JWT no Fastify. - Garantir que qualquer chamada à rota `GET /process/123` pertença exclusivamente ao Tenant em questão, servindo os dados capturados assincronamente. ### 🤖 Etapa 4: Integração do Bot Lexra - Ancorar os mocks do `telegram/bot.ts` e do OpenClaw no serviço Real. - O Bot só responderá processos do Tenant injetado e disparará LLM calls para simplificação via OpenRouter. ### 🚀 Etapa 5: Preparação Produtiva (Deploy) - Mover varíaveis em `.env.example`, arrumar `Dockerfile` e gerenciar `winston` logging level pro ambiente de staging (Render/AWS). --- > \[!IMPORTANT\] > Usuário, avalie os entregáveis deste plano. Concordando com o fluxo e com a ideia de priorizarmos o \*\*Prisma (Banco de Dados Relaional)\*\* como pontapé inicial, posso dar inicio a \*\*Etapa 1\*\*. O que achou? FOI FEITA A FASE 1

---

**Você disse**

---

**Você disse**

---

**Você disse**

---

**Você disse**

Como validamos o que esta sendo feito no codex e no antigravity

---

**Você disse**

---

**Você disse**

consegue analisar

---

**Você disse**

como abro ali o projeto que o codex editou e unifico os dois

---

**Você disse**

git@github.com:gingkosystems/agentjury.git uso este link no terminal dentro da pasta essa?

---

**Você disse**

---

**Você disse**

---

**Você disse**

onde e fetch

---

**Você disse**

cliquei e agr

---

**Você disse**

PS C:\\Users\\User\\OneDrive\\Área de Trabalho\\G-Tech\\Administração Interna\\JURY AGENT\\juryagent\\agentjury> npm install up to date, audited 171 packages in 1s 49 packages are looking for funding run `npm fund` for details 1 critical severity vulnerability To address all issues, run: npm audit fix Run `npm audit` for details. PS C:\\Users\\User\\OneDrive\\Área de Trabalho\\G-Tech\\Administração Interna\\JURY AGENT\\juryagent\\agentjury> npm run dev > agentjury@1.0.0 dev > npm run build && node dist/index.js > agentjury@1.0.0 build > tsc -p tsconfig.json Backend rodando na porta 3333 \[MonitorWorker\] started with interval 15000ms 🟡 Atualização no processo PROC-001 Resumo: Distribuído Data: 2026-01-03 Urgência: MEDIUM \[NotificationService\] Failed channel=telegram process=PROC-001 TELEGRAM\_BOT\_TOKEN não configurado 🟡 Atualização no processo PROC-001 Resumo: Concluso para decisão Data: 2026-01-08 Urgência: MEDIUM \[NotificationService\] Failed channel=telegram process=PROC-001 TELEGRAM\_BOT\_TOKEN não configurado 🟡 Atualização no processo PROC-001 Resumo: Atualização diária automática Data: 2026-04-10 Urgência: MEDIUM \[NotificationService\] Failed channel=telegram process=PROC-001 TELEGRAM\_BOT\_TOKEN não configurado \[MonitorService\] PROC-001 snapshot=snapshot\_1 newMovements=3 🟡 Atualização no processo PROC-002 Resumo: Distribuído Data: 2026-01-03 Urgência: MEDIUM \[NotificationService\] Failed channel=telegram process=PROC-002 TELEGRAM\_BOT\_TOKEN não configurado 🟡 Atualização no processo PROC-002 Resumo: Concluso para decisão Data: 2026-01-08 Urgência: MEDIUM \[NotificationService\] Failed channel=telegram process=PROC-002 TELEGRAM\_BOT\_TOKEN não configurado 🟡 Atualização no processo PROC-002 Resumo: Atualização diária automática Data: 2026-04-10 Urgência: MEDIUM \[NotificationService\] Failed channel=telegram process=PROC-002 TELEGRAM\_BOT\_TOKEN não configurado \[MonitorService\] PROC-002 snapshot=snapshot\_5 newMovements=3 copiei o resultado do comando

---

Direto ao ponto:

---

A raiz é **a pasta onde está o `package.json`**

No seu print:

```
agentjury/
 ├─ src/
 ├─ package.json  ← 🔥 AQUI É A RAIZ
 ├─ tsconfig.json
```

👉 então a raiz é:

```
C:\Users\User\OneDrive\...\agentjury
```

---

## 🧠 O QUE FAZER

## 👉 1. Criar arquivo.env

Na raiz (mesmo nível do `package.json`)

### No VSCode:

- botão direito na pasta `agentjury`
- `New File`
- nome:
```
.env
```

---

## 👉 2. Colar dentro:

```
TELEGRAM_BOT_TOKEN=SEU_TOKEN_AQUI
TELEGRAM_CHAT_ID=SEU_CHAT_ID_AQUI
```

---

## ⚠️ IMPORTANTE

Esse projeto **provavelmente usa `process.env` direto**, então:

👉 se não tiver `dotenv` instalado, pode não funcionar automaticamente

---

## 🔍 TESTE RÁPIDO

Depois de criar `.env`, roda:

```bash
npm run dev
```

Se continuar erro:

```
TELEGRAM_BOT_TOKEN não configurado
```

👉 então precisa ativar dotenv

---

## 🔧 CASO PRECISE (ativar dotenv)

## 1\. instalar:

```bash
npm install dotenv
```

## 2\. abrir:

```
src/index.ts
```

ou

```
src/api/server.ts
```

## 3\. adicionar no topo:

```typescript
import 'dotenv/config'
```

---

## 🧠 COMO PEGAR O CHAT ID (rápido)

1. manda mensagem pro bot
2. acessa:
```
https://api.telegram.org/botSEU_TOKEN/getUpdates
```
3. procura:
```json
"chat": {
  "id": 123456789
}
```

---

## 🚀 RESUMO

```
Raiz = pasta com package.json
.env = criado ali
Cola token + chat_id
Roda npm run dev
```

---

## ⚡ OBSERVAÇÃO IMPORTANTE

Você NÃO precisa criar só Telegram.

Esse `.env` vira o **centro de controle do sistema** depois:

```
TELEGRAM
OPENAI
OPENROUTER
DATABASE
WEBHOOK_N8N
```

---

Se quiser, no próximo passo eu te mostro como:

👉 trocar Telegram por n8n (nível Ginkgo real)

---

**Você disse**

qual chat id

---

Você precisa do **ID do chat onde o bot vai enviar mensagens**.  
Existem 2 cenários:

---

## 🧠 1. CHAT PRIVADO (mais simples)

👉 você conversando com o bot

## PASSO A PASSO

### 1\. Abre o Telegram

Procura seu bot

### 2\. Envia qualquer mensagem

Exemplo:

```
teste
```

---

### 3\. Abre no navegador:

```
https://api.telegram.org/botSEU_TOKEN/getUpdates
```

(substitui `SEU_TOKEN`)

---

### 4\. Procura isso no JSON:

```json
"chat": {
  "id": 123456789,
  "first_name": "...",
  "type": "private"
}
```

👉 esse número:

```
123456789
```

é o seu:

```
TELEGRAM_CHAT_ID
```

---

## 🧠 2. GRUPO (mais avançado)

Se quiser mandar pra grupo:

## passos:

1. adiciona o bot no grupo
2. manda uma mensagem no grupo
3. roda o mesmo link:
```
https://api.telegram.org/botSEU_TOKEN/getUpdates
```

---

Vai aparecer algo assim:

```json
"chat": {
  "id": -100987654321,
  "title": "Meu Grupo",
  "type": "supergroup"
}
```

👉 o ID será:

```
-100987654321
```

---

## ⚠️ IMPORTANTE

- ID de grupo sempre começa com `-100`
- ID privado é número normal

---

## 🔥 RESUMO RÁPIDO

```
1. manda mensagem pro bot
2. abre getUpdates
3. copia "chat.id"
4. coloca no .env
```

---

## ⚡ EXEMPLO FINAL.env

```
TELEGRAM_BOT_TOKEN=123456:ABC-XYZ
TELEGRAM_CHAT_ID=123456789
```

---

Se quiser, manda o JSON que apareceu pra você que eu te digo exatamente qual é o ID correto.

---

**Você disse**

ME DE UM RESUMO TECNICO DA AGENTE JURY

---

### Resumo técnico — Agente JURY

**JURY** é um **agente backend de monitoramento jurídico automatizado**, orientado a eventos, com pipeline de notificação inteligente e arquitetura extensível por canais (Telegram, futuros webhooks, etc.).

---

## 1\. Arquitetura geral

- **Stack**:
	- Node.js + TypeScript
		- Fastify (API HTTP)
		- Workers assíncronos (monitoramento periódico)
		- Sistema de eventos + snapshots
		- Notificações multicanal (Telegram implementado)
- **Execução**:
	- `npm run dev` → compila TS (`tsc`) → executa `dist/index.js`
		- API ativa na **porta 3333**

---

## 2\. Componentes principais

### 🔹 API (src/api)

- Endpoints REST para:
	- Health check
		- Consulta e acompanhamento de processos
- Prefixo padrão: `/api`
- Fastify com CORS configurado

---

### 🔹 MonitorService / MonitorWorker

- Worker periódico (ex.: a cada **15s**)
- Responsável por:
	- Verificar processos jurídicos
		- Gerar **snapshots**
		- Detectar **novos movimentos**
- Emite eventos quando há mudança relevante

Log típico:

```
[MonitorService] PROC-001 snapshot=snapshot_1 newMovements=3
```

---

### 🔹 Sistema de Eventos

- Cada mudança gera um **evento de processo**
- Eventos alimentam o pipeline de notificação
- Estados tratados:
	- Distribuído
		- Concluso para decisão
		- Atualização automática
- Cada evento possui:
	- Resumo
		- Data
		- Classificação de urgência (LOW / MEDIUM / HIGH)

---

### 🔹 NotificationService

- Orquestra envio de mensagens
- Canal-aware (cada canal é plugável)
- Atualmente:
	- **TelegramProvider** implementado
- Falhas de canal não quebram o sistema (fail-safe)

Exemplo de log:

```
[NotificationService] Failed channel=telegram TELEGRAM_BOT_TOKEN não configurado
```

---

## 3\. Pipeline lógico (fluxo mental)

```
Processo monitorado
        ↓
Snapshot comparado
        ↓
Novos movimentos detectados
        ↓
Evento criado
        ↓
Resumo + urgência gerados
        ↓
NotificationService
        ↓
Canal (Telegram)
```

Arquitetura de **event-driven monitoring**, não polling burro.

---

## 4\. Configuração via.env

A raiz do projeto (`agentjury/`) contém o `.env`.

Variáveis críticas:

```
TELEGRAM_BOT_TOKEN=xxxxx
TELEGRAM_CHAT_ID=yyyyy
```

Sem isso:

- Backend roda
- Monitor roda
- **Notificação falha silenciosamente** (by design)

---

## 5\. Estado atual do sistema

✅ Backend operacional  
✅ Monitoramento ativo  
✅ Detecção de eventos funcional  
⚠️ Telegram desativado por falta de credenciais  
⚠️ 1 vulnerabilidade crítica (dependência → `npm audit fix`)

---

## 6\. O que o JURY é, em essência

- Um **agente jurídico autônomo**
- Observa processos como um **sentinela**
- Resume o caos jurídico em sinais acionáveis
- Pronto para escalar para:
	- WhatsApp
		- Webhooks
		- Dashboards
		- IA de sumarização mais avançada

---

Se quiser, o próximo passo natural é:

- adicionar **OpenAI / LLM** no resumo,
- ou transformar isso num **produto SaaS jurídico** com múltiplos clientes e canais.

Diga qual direção você quer seguir.