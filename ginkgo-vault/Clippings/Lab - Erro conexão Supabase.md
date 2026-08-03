---
title: "Lab - Erro conexão Supabase"
source: "https://chatgpt.com/g/g-p-6920bddfbb548191ac06d937cdb0b5c0/c/6929c13c-e09c-8331-af46-35a5b833ea74"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 28 de nov. às 12:35

sex., 28 de nov. às 15:07

onde conferimos

e se tirararmos o flowise e pausassemos o chatwoot, daria?

A Ginkgo não é uma “empresa de automação”.  
Ela está virando **uma operadora de infra + IA + serviços SaaS**, um *mini-AWS para pequenos negócios*, com agentes autônomos plugados em workflows.

Para isso funcionar **em escala**, você precisa de um conjunto de ferramentas essenciais — não só n8n, Supabase e Evolution, mas um ecossistema completo.

Abaixo está **a lista definitiva**, baseada no que você realmente vai precisar para:

- Ginkgo Leaf
- Ginkgo Wave
- Ginkgo Pyre
- Brann
- Infra do escritório digital
- Multi-clientes
- Monitoramento
- Gestão de agentes

E tudo que está no seu Easypanel.

Prepare-se: isto é o **roadmap oficial de infraestrutura da Ginkgo**.

---

## 🧬 GKO INFRA — O KIT ESSENCIAL PARA ESCALA E OPERAÇÃO TOTAL

## 1\. NÚCLEO OPERACIONAL (já instalado, mas precisa expansão)

Esses são o coração das suas operações:

### ✔ n8n (central de automações)

Necessário. Você já usa como cérebro operacional.

### ✔ Evolution API

Seu backbone para WhatsApp e agentes autônomos.

### ✔ Redis

Cache para memória curta dos agentes. Indispensável.

### ✔ Postgres

Memória longa, CRM, logs, tudo que é persistente.

---

## ⚡ 2. FERRAMENTAS QUE A GINKGO PRECISA OBRIGATORIAMENTE NA ESCALA

## (A) SUPABASE (você tem o template na tela) — INSTALAR

Isso é **obrigatório** para a Ginkgo virar SaaS de verdade:

- Storage de arquivos (Brann uploads, Pyre vídeos, Wave reports)
- Auth universal
- Funções serverless
- Rest API
- Realtime
- Gestão de usuários
- Multi-empresa

Supabase = **a espinha dorsal da Ginkgo**.  
Nada chega perto dele.

**Instalar assim que seu VPS tiver 16 GB RAM.**

---

## (B) PGADMIN — RECOMENDADO

Ferramenta para administrar o banco de dados com interface visual.

Por quê?

- visualizar tabelas, índices, triggers
- editar schemas
- testar queries
- analisar performance
- entender gargalos

Para uma empresa de IA e automações: obrigatório.

---

## (C) QDRANT — ESSENCIAL para IA Corporativa

A Ginkgo tem agentes autônomos.  
Logo, você precisa de **RAG sério**.

Qdrant (está na lista de apps do Easypanel) é:

- vetor storage
- busca semântica
- clustering
- embeddings persistentes
- base de conhecimento do Brann & Pyre & Leaf

Isso transforma seu agente em **“memória viva”** empresarial.

Não dá para escalar sem isso.

---

## (D) UP-TIME / STATUS PAGE — UptimeKuma

Está na lista → **Instalar**.

A Ginkgo tem clientes que dependem da Leaf/Wave operando 24h.  
Você precisa de:

- monitoramento
- alertas
- status page
- logs de downtime

Isso dá profissionalismo e evita prejuízos.

---

## (E) NGINX PROXY MANAGER ou TRAEFIK — para apontar domínios

**Essencial**.

Com vários serviços (Flowise, Evol, Supabase, Brann dashboard, Studio, etc), você vai precisar:

- HTTPS
- subdomínios (api.ginkgo, leaf.ginkgo, wave.ginkgo…)
- proxy reverso
- certificados automáticos

Sem isso, a infra fica feia e insegura.

---

## (F) PORTAINER — controle total dos containers

Está na lista → **Instalar**.

Com Portainer você:

- gerencia containers
- entende consumo
- vê logs rapidamente
- reinicia serviços em 1 clique
- cria stacks completas

Acelera a vida do DevOps (você).

---

## 🔮 3. CAMADA DE DESENVOLVIMENTO E PRODUTIVIDADE

## (G) Visual Studio Code Server (está na imagem)

Instalar.

Você edita:

- fluxos
- arquivos
- scripts
- configurações
- front-end dos SaaS
- automações da Manus
- modelos do Brann

Direto no servidor.

É o **quartel-general de desenvolvimento**.

---

## (H) GIT SERVER (opcional) – Gitea ou Forgejo

Para código privado da Ginkgo:

- Leaf
- Pyre
- Wave
- Agents
- API
- Scripts
- n8n workspaces

Serve como GitHub privado interno.

---

## 🛰 4. CAMADA DE OBSERVABILIDADE / MONITORAMENTO

## (I) Prometheus + Grafana

Ambiente empresarial precisa disso.

Você mede:

- latência do Brann
- consumo de CPU do Wave
- erro do Pyre
- carga do Evolution
- queries lentas do Postgres
- fila do Redis
- saúde do Supabase

Isso vira dados valiosos para tomada de decisão.

---

## 🔐 5. CAMADA DE SEGURANÇA

## (J) Crowdsec

Firewall comportamental, protege contra:

- brute force
- DDOS
- scanners
- bots
- ataques de API

Barreira essencial quando sua empresa crescer.

---

## 🧩 6. CAMADA DE ARMAZENAMENTO E BACKUP

## (K) MinIO (caso queira sua própria “AWS S3”)

Para:

- vídeos do Pyre
- assets gerados
- PDFs
- dumps do Qdrant

Supabase Storage já resolve 90%.  
Mas MinIO é o **modo enterprise**.

---

## 🤖 7. CAMADA DE AGENTES (IA Autônoma)

## (L) OLLAMA (está listado!)

Rodar modelos localmente:

- LLaMA
- Mistral
- Qwen
- Hermes

Para:

- automações internas
- reduzir custo de API
- criar agentes especializados offline
- RAG local

Ginkgo com IA local → diferencial competitivo enorme.

---

## 🌍 8. CAMADA DE COLABORAÇÃO E DOCUMENTAÇÃO

## (M) Wiki.js

Documentação interna:

- APIs
- RAG
- modelos
- pipelines
- SOPs (padrões operacionais)
- configuração dos clientes

Seu time vai precisar disso.

---

## 💼 9. CAMADA DE DASHBOARD / CLIENTE

## (N) Umami ou Plausible (analytics)

Para:

- analisar acesso aos sites Ginkgo
- medir uso do Leaf dashboard
- entender comportamento dos clientes

---

## 🎯 LISTA FINAL (o “KIT GINKGO ENTERPRISE”)

As ferramentas essenciais para a Ginkgo escalar:

### Infra core

- Supabase
- Postgres
- Redis
- n8n
- Qdrant
- Evolution API

### Produtividade

- PGAdmin
- VSCode Server
- Gitea/Forgejo
- Portainer

### Segurança

- Crowdsec
- UptimeKuma (monitoramento)
- Nginx Proxy Manager

### IA

- Ollama
- Qdrant (já citado, mas é IA também)

### Documentação

- Wiki.js

### Analytics

- Umami
- Prometheus + Grafana

---

## 🚀 Quer que eu prepare a arquitetura exata com tudo isso instalado no seu novo VPS KVM 4?

Eu monto:

- diagrama
- ordem de instalação
- subdomínios
- segurança
- organização por projetos (studio, ginkgo-core, ginkgo-agents, ginkgo-clients)
- RAM reservada por serviço
- plano de escalabilidade

Só pedir:  
**quer a arquitetura Ginkgo Enterprise pronta?**

sim. não esquecemos nada? e para o pyre e wave conseguimos instalar algo hospedado? para fazer essas funções. instalar a lovart ou o clickup e a manus, essas ferramentas

Vamos fechar isso com precisão de arquiteto de dados + visão estratégica de CEO da Ginkgo.

Primeiro: **não esquecemos nada** do núcleo crítico.  
O que falta agora é **distinguir o que pode ser hospedado** e o que **jamais será self-hosted** por design.

E saber exatamente **como montar o Leaf, Wave e Pyre** em uma infraestrutura unificada.

Abaixo vai o manual completo, na lata.

---

## 🧬 PARTE 1 — Existem 3 tipos de ferramentas na Ginkgo

Para não se enrolar, divida assim:

---

## TIPO A — Ferramentas que você pode (e deve) hospedar no seu servidor

Essas viram parte da **infra Ginkgo Core** e entregam escala real:

### ✔ Supabase (storage, auth, rest, realtime)

### ✔ Qdrant

### ✔ Ollama

### ✔ Portainer

### ✔ Nginx Proxy Manager

### ✔ Redis

### ✔ Postgres

### ✔ UptimeKuma

### ✔ VSCode Server

### ✔ PGAdmin

### ✔ Grafana + Prometheus

### ✔ Crowdsec

Essas **sim** são a base do Leaf, Pyre, Wave e futuros agentes.

---

## TIPO B — Ferramentas que NÃO podem ser self-hosted (por design, API fechada)

Você citou:

- **Lovart / Nano Banana**
- **ClickUp**
- **Manus**

Essas são **SaaS fechados**.  
Não existe versão self-hosted delas nem “instalável”.

### ✔ Por que isso importa?

Porque:

- **Pyre (social media)** precisa usar Lovart (ou Lovable) como API → SaaS externo.
- **Wave (gestor de tráfego)** precisa usar ClickUp/Manus como API → SaaS externo.
- **Leaf & Brann** usam Evolution + Supabase + Qdrant → self-hosted híbrido.

Então a arquitetura correta da Ginkgo é:

---

## 🧱 TIPO C — Ferramentas SaaS externas que VOCÊ usa via API

Essas ferramentas **continuam externas**, mas entram dentro da sua ORQUESTRA com n8n + Supabase + Qdrant.

### ✔ Lovart

Gerador de imagens e vídeos.  
→ Pyre usa isso.

### ✔ ClickUp

Gerenciamento de tarefas.  
→ Wave usa isso.

### ✔ Manus

Orquestrador de agentes / workflows.  
→ Pyre e Wave usam isso.

### ✔ ElevenLabs

→ Brann (áudios)

### ✔ Stripe

→ Ginkgo pagamentos

### ✔ Notion (opcional)

→ base de conhecimento

### ✔ Discord

→ community + suporte

Essas NÃO entram no servidor.  
Você as integra via API dentro do n8n/Manus.

---

## 🧬 PARTE 2 — Arquitetura oficial de cada produto Ginkgo

## 🔥 1. Ginkgo Leaf (Atendimento/automações via Brann)

**Hospedado no seu servidor (100% seu)**

### Núcleo:

- Evolution API
- n8n
- Supabase
- Qdrant
- Redis
- Postgres
- UptimeKuma
- Nginx Proxy Manager

### APIs externas:

- ElevenLabs (áudio)
- Stripe (cobrança)

---

## 🔥 2. Ginkgo Wave (Gestor de tráfego autônomo)

**Misto: seu servidor + ClickUp/Manus**

### No servidor (seu):

- n8n
- Supabase
- Qdrant
- Redis
- Ollama (para IA local se quiser)

### externo:

- ClickUp → dashboards, tasks
- Manus → agente Alfred interno
- Lovart/Nano Banana → materiais
- Google Ads API / Meta Ads API → automações

---

## 🔥 3. Ginkgo Pyre (Social Media Autônomo)

**Misto: seu servidor + Lovart/Manus**

### No servidor:

- n8n
- Supabase
- Qdrant
- Redis
- Ollama (opcional)

### Externos:

- Lovart/Nano Banana → imagens/vídeos
- Manus → agente criativo
- TikTok/Instagram API → postagens
- Ginkgo Qdrant → memória de nicho/perfil

---

## 🧠 PARTE 3 — Dá para instalar Lovart/ClickUp/Manus no servidor?

### ❌ Lovart → NÃO

É um SaaS proprietário.  
Mas você pode usar a **API Pro** (Nano Banana) dentro do n8n.

### ❌ ClickUp → NÃO

É SaaS fechado.  
Você usa a API (GET tasks, POST tasks, automations, etc.)

### ❌ Manus → NÃO

Também é SaaS.  
Mas você pode integrar **profundamente** com supabase + n8n + leaf.

---

## 🚀 PARTE 4 — O que instalar AGORA no seu servidor (checklist final)

Se a Ginkgo fosse uma nave, isso seria o painel de controle:

## 🔵 Infra Core (obrigatório)

- Supabase
- Postgres
- Redis
- Qdrant
- Ollama
- n8n
- Evolution API
- Nginx Proxy Manager
- UptimeKuma
- Portainer
- PGAdmin

## 🟣 Observabilidade (empresarial)

- Prometheus
- Grafana
- Loki (logs)
- Crowdsec (segurança)

## 🟠 Desenvolvimento

- VSCode Server
- Gitea (Git privado opcional)

## 🟢 Documentação

- Wiki.js

---

## 🛰 PARTE 5 — Resultado final: cada produto Ginkgo opera assim

### Leaf:

→ 100% self-hosted  
→ IA híbrida (OpenAI + local via Ollama)  
→ WhatsApp via Evolution  
→ Armazenamento via Supabase  
→ RAG via Qdrant

### Wave:

→ self-hosted + ClickUp  
→ dashboards + criação de tarefas + IA via Manus  
→ planejamento, estratégia e ações via n8n

### Pyre:

→ self-hosted + Lovart  
→ vídeos, imagens, social posts  
→ programação automática  
→ memória criativa via Qdrant

---

## 🎯 Gabriel, a verdade final:

**Você já tem o núcleo. Agora você precisa do “Ginkgo Engine” completo:**

- Supabase (coluna vertebral)
- Qdrant (memória)
- Ollama (IA local)
- n8n (orquestrador)
- Evolution API (comunicação)
- Observabilidade (segurança + logs + métricas)

E então integrar com:

- ClickUp
- Manus
- Lovart
- Stripe

Isso te dá uma empresa **completamente autônoma**, capaz de operar dezenas de clientes.

---

## 👇 Se quiser, eu monto a arquitetura Ginkgo Enterprise V1.0 completa:

- diagrama da infra
- ordem de instalação
- subdomínios
- distribuição de RAM
- fluxo de dados
- stack por produto
- checklists técnicos

**Quer que eu entregue a GINKGO ENTERPRISE V1.0 pronta?**

Sim.

Perfeito. Vamos cravar a **GINKGO ENTERPRISE V1.0**.

Vou te entregar:

1. Desenho lógico da infra
2. O que vai em cada “projeto” do Easypanel
3. Ordem de instalação
4. Subdomínios
5. Orçamento de RAM/CPU (pensando no KVM 4 – 16GB / 4vCPU)
6. Stack de cada produto (Leaf, Wave, Pyre)
7. Checklists de operação

---

## 1\. Visão geral – “nave-mãe” Ginkgo

Pensa em 4 anéis:

1. **Core de Infra** – tudo que mantém a nave viva
2. **Camada de IA & Dados** – memória, vetores, modelos
3. **Camada de Orquestração** – n8n, Evolution, Manus
4. **Camada de Produtos** – Leaf, Wave, Pyre (painéis, APIs, automações)

### Diagrama lógico simplificado

```markdown
[ Usuários / Clientes ]
             |
      (Sites / Landings)
             |
     ┌────────────────┐
     │  Produtos      │
     │ Leaf / Wave /  │
     │ Pyre / Portais │
     └────────┬───────┘
              |
     ┌────────▼─────────┐
     │ Orquestração     │
     │ n8n + Evolution  │
     │ (Manus / APIs)   │
     └────────┬─────────┘
              |
┌─────────────▼─────────────┐
│ IA & Dados                │
│ Supabase + Postgres       │
│ Qdrant + Redis + Ollama   │
└─────────────┬─────────────┘
              |
┌─────────────▼─────────────┐
│ Infra Core                │
│ Easypanel, Nginx Proxy,   │
│ Portainer, Uptime,        │
│ Prometheus/Grafana, etc.  │
└───────────────────────────┘
```

O fluxo do BRANN que você já montou encaixa dentro desse anel de orquestração/IA (Webhook → processamento mídia → memória → RAG → resposta). Visao-geral-do-fluxo

---

## 2\. Organizar em “projetos” no Easypanel

### Projeto 1 – infra-core

Para tudo que é base:

- **nginx-proxy-manager** (ou outro reverse proxy)
- **uptime-kuma**
- **portainer**
- **prometheus + grafana**
- **crowdsec** (se usar)

### Projeto 2 – gko-db

Camada de dados:

- **postgres (principal)** – banco mestre da Ginkgo
- **redis (global)**
- **supabase** (quando instalar self-hosted; se usar cloud, fica só Postgres+Redis aqui)
- **qdrant**
- **ollama**

### Projeto 3 – studio

Onde já estão:

- **n8n**
- **flowise** (pode deixar desligado quando não usar)
- **pgadmin**
- **vscode-server**

### Projeto 4 – evo

- **evolution-api**
- **evolution-api-db**
- **evolution-api-redis**

### Projeto 5 – chatwoot (quando estiver usando)

- chatwoot
- chatwoot-db
- chatwoot-redis
- chatwoot-sidekiq

---

## 3\. Ordem de instalação recomendada (KVM 4 – 16GB)

Sequência para não quebrar nada:

1. **Upgrade VPS para KVM 4 (16GB)** – já vimos.
2. **Infra Core**
	- nginx-proxy-manager
		- portainer
		- uptime-kuma
3. **Dados & IA**
	- qdrant
		- ollama
		- (se decidir: supabase self-hosted)
4. **Ferramentas Dev & DB**
	- pgadmin
		- vscode-server
5. **Observabilidade**
	- prometheus + grafana
6. **Ajustar n8n / Evolution / Chatwoot** para rodar atrás do proxy com domínios bonitos.

---

## 4\. Subdomínios sugeridos

Usando `ginkgosystems.tech` como base (ajuste pro seu domínio):

- **Infra**
	- `panel.ginkgosystems.tech` → Easypanel
		- `portainer.ginkgosystems.tech` → Portainer
		- `status.ginkgosystems.tech` → UptimeKuma
		- `metrics.ginkgosystems.tech` → Grafana
- **Dados / IA**
	- `db.ginkgosystems.tech` → PGAdmin
		- `studio-code.ginkgosystems.tech` → VSCode Server
		- `qdrant.ginkgosystems.tech` → Qdrant UI (se expuser)
		- `ollama.ginkgosystems.tech` → Ollama API (ou só interno)
- **Orquestração**
	- `n8n.ginkgosystems.tech` → n8n
		- `evo.ginkgosystems.tech` → Evolution API
		- `chatwoot.ginkgosystems.tech` → Chatwoot (quando ativo)
- **Produtos**
	- `leaf.ginkgosystems.tech`
		- `wave.ginkgosystems.tech`
		- `pyre.ginkgosystems.tech`

Cada produto pode ser um front (Next.js/Manus/Lovable) falando com APIs internas.

---

## 5\. Orçamento de RAM / CPU (KVM 4 – 16GB / 4vCPU)

Alocação alvo (não é “limite fixo”, é referência para você medir no Portainer/Grafana):

- **Postgres + Supabase stack:** ~4GB
- **Redis + Qdrant + Ollama:** ~3GB
- **n8n + Evolution + Flowise:** ~3GB
- **Chatwoot stack:** ~2GB (quando ligado)
- **Infra (proxy, uptime, portainer, grafana, etc.):** ~1–2GB
- **Folga / pico:** ~2GB

Se ver que Chatwoot quase não é usado, pode desligar quando não precisar e liberar ~1–1.5GB.

---

## 6\. Produto por produto – como fica a stack

### 6.1 Ginkgo Leaf (BRANN / atendimento inteligente)

**Backbone técnico:**

- **Evolution API** – canal WhatsApp
- **n8n** – fluxo de:
	- webhook Evolution
		- extração de mídia (como no PDF) Visao-geral-do-fluxo
		- transcrição (OpenAI / Ollama)
		- consulta de memória (Supabase + Qdrant)
		- chamada do modelo (OpenAI / Ollama)
		- envio da resposta via Evolution
- **Supabase / Postgres** –
	- `customers`
		- `chat_histories`
		- `kb_chunks` (se decidir centralizar RAG)
		- configurações por cliente (persona, limites, etc.)
- **Qdrant** – vetores de:
	- documentos da Ginkgo
		- documentos de clientes
		- FAQs
- **Redis** – memória de curto prazo / filas rápidas
- **Ollama** – modelos locais para tasks específicas (resumo, classificação, checagens)

**APIs externas:**

- OpenAI / Claude (modelo principal do Brann, se não usar só local)
- ElevenLabs (áudio)
- Stripe (assinaturas Leaf)

---

### 6.2 Ginkgo Wave (gestor de tráfego)

**No servidor Ginkgo:**

- n8n → orquestra campanhas, lê métricas, dispara planos de ação
- Supabase → armazena:
	- contas de anúncios do cliente
		- campanhas, conjuntos, criativos
		- histórico de performance
- Qdrant → memória do “Alfred” de tráfego (o que funcionou / não funcionou por nicho)
- Ollama / OpenAI → análise de métricas, sugestões de teste A/B, criação de plano

**APIs externas:**

- ClickUp → tasks e quadros organizados. Wave atualiza tasks, status, prazos via n8n.
- Manus → front conversacional / assistente interno que conversa com o cliente sobre campanha
- Google Ads API / Meta Ads API / TikTok Ads API → leitura/escrita de campanhas
- Lovart/Nano Banana → criativos (quando Wave pedir “gerar banner/vídeo X”)

---

### 6.3 Ginkgo Pyre (social media)

**No servidor Ginkgo:**

- n8n → pipeline de conteúdo:
	- recebe pauta/brief
		- chama IA para roteiros/cópias
		- envia para Lovart gerar arte/vídeo
		- salva no Supabase ou MinIO
		- agendamento para postagem
- Supabase:
	- `social_posts`
		- `calendars`
		- `assets` (imagem/vídeo)
- Qdrant:
	- memória de tom de voz
		- histórico de posts que performaram
		- biblioteca de prompts por nicho
- Ollama / OpenAI:
	- geração de texto
		- variações de gancho
		- A/B de legendas

**APIs externas:**

- Lovart / Nano Banana → geração de imagem/vídeo
- Manus → “diretor criativo” conversacional
- Instagram / TikTok / X / YouTube API → publicação e insights

---

## 7\. Fluxo de dados típico (exemplos rápidos)

### 7.1 Leaf – atendimento no WhatsApp

1. Cliente manda mensagem/áudio → Evolution → Webhook n8n
2. n8n identifica tipo (texto/imagem/áudio) → transcreve/ou faz OCR → obtém `text`
3. n8n passa:
	- texto
		- contexto do cliente (plano, empresa)
		- histórico (buscado em Supabase)
		- docs relevantes (buscados em Qdrant)
4. Modelo (OpenAI/Ollama) responde no formato JSON `out`
5. n8n envia via Evolution (texto, botões, áudio)
6. n8n grava no Supabase:
	- mensagem, sessão, tags, métricas

---

### 7.2 Pyre – criação de post

1. Usuário define tema/objetivo (via Manus ou painel)
2. n8n recebe o pedido → chama IA para gerar:
	- ideia
		- roteiro
		- legenda
3. n8n chama Lovart/Nano Banana para gerar imagem/vídeo
4. Resultado é salvo no Supabase + metadata no Postgres/Qdrant
5. n8n agenda postagem no canal escolhido (Instagram/TikTok/etc.)

---

## 8\. Checklists essenciais

### 8.1 Antes de subir GINKGO ENTERPRISE V1.0

- VPS em **KVM 4 – 16GB** no mínimo
- Backup dos dados atuais (DB Evolution, n8n, Chatwoot)
- Instalar e configurar:
	- Nginx Proxy Manager
		- Portainer
		- UptimeKuma
- Colocar n8n e Evolution atrás do proxy com HTTPS
- Instalar Qdrant, testando conexão com n8n
- Instalar Ollama (se for usar modelos locais)
- Instalar PGAdmin e conectar ao Postgres “sp db”
- Definir subdomínios principais (panel, n8n, evo, etc.)

### 8.2 Para cada novo cliente Leaf/Wave/Pyre

- Criar registro do cliente em Supabase (org, planos, limites)
- Gerar/atribuir instância Evolution/WhatsApp
- Criar “workspace lógico” no n8n (tag + credenciais)
- Gerar chaves/API externas (ClickUp, Lovart, etc.)
- Popular Qdrant com:
	- docs
		- FAQ
		- contratos/modelos específicos
- Testar:
	- fluxo de onboarding
		- 3 conversas de exemplo
		- 1 criação de conteúdo (Pyre)
		- 1 ação de campanha (Wave)

### 8.3 Operação diária

- UptimeKuma sem alertas críticos
- Portainer sem containers reiniciando em loop
- Grafana: CPU < 70%, RAM livre > 20%
- Logs de erro do n8n/Evolution/Chatwoot checados ao menos 1x/dia
- Backups automáticos do Postgres rodando (snapshot ou dump)

---

Se quiser, no próximo passo eu posso:

1. Listar **comandos e telas** para instalar cada peça (ordem certinha no Easypanel).
2. Montar o **esquema de tabelas Supabase** padrão da Ginkgo (orgs, users, clientes, planos, históricos, etc.).
3. Definir um **template n8n** para novo cliente Leaf/Wave/Pyre (para você só duplicar e trocar variáveis).