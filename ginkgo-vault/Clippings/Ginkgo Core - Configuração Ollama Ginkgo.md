---
title: "Ginkgo Core - Configuração Ollama Ginkgo"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/69546258-6f44-832c-a2f4-ace9735be331"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
ter., 30 de dez. às 20:38

![f157c839-f4c5-4785-97b8-675eaec9d60c.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000009bc4720eb614b9478ba7a5b0&ts=495694&p=fs&cid=1&sig=d42dee354943df2018d349a6fcfd3ccdd3a01f262e87440730ab181e60203585&v=0)

como devemos configurar e como podemos usar ollama na ginkgo?

![c4d2e688-e751-4af7-9979-51991e9d15b6.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000008520720eb56ed69305c2f5fa&ts=495694&p=fs&cid=1&sig=e799db04dc9220b157734b35668d47a54c836b40f24406e1f29cfb527fb0876e&v=0)

Perfeito. Teu PC é **excelente** pra estratégia híbrida da Ginkgo. Dá pra extrair muito valor local antes de gastar 1 real com cloud.

Vou ser direto, técnico e prático.

---

## 🔧 Teu hardware (leitura fria)

- **CPU:** Ryzen 5 5600 (6c/12t) → ótimo pra orquestração e tasks paralelas
- **RAM:** 16 GB → limite prático, mas bem utilizável
- **GPU:** RTX 4060 (8 GB VRAM) → ouro para LLM local
- **SSD:** ok
- **OS:** Windows 11 Pro

👉 Conclusão:  
Tu roda **muito bem modelos 7B–8B quantizados**, com **contexto até ~16k**, e embeddings sem esforço.  
Modelos 13B já ficam no **limite** (possível, mas não confortável).

---

## 🧠 Estratégia final: “PC = Núcleo / Cloud = Expansão”

Pensa assim (analogia sci-fi):

- Teu PC = **Nave-mãe** (operações críticas, baratas, privadas)
- Cloud = **hiperespaço** (entra só quando precisa de força bruta)

---

## 1️⃣ O QUE RODAR NO TEU PC (Ollama local)

### ✅ Rodar SEM MEDO

Essas tasks são o coração da Ginkgo:

### 🔹 Classificação & Roteamento

- intenção do cliente
- urgência
- tipo de lead
- produto (Leaf / Wave / Pyre)
- risco / spam

👉 latência baixa, custo zero, perfeito local.

---

### 🔹 Extração estruturada (MUITO IMPORTANTE)

Transformar conversa em JSON:

```markdown
{
  "nome": "",
  "empresa": "",
  "cidade": "",
  "produto_interesse": "",
  "orcamento": "",
  "prazo": "",
  "nivel_interesse": ""
}
```

👉 Isso é **100% local** sempre.

---

### 🔹 Resumos operacionais

- resumo pro Chatwoot
- resumo pro CRM
- “o que já foi decidido”
- “pendências”

---

### 🔹 Embeddings (RAG)

- FAQ
- documentação
- contratos
- scripts de vendas

👉 Economia brutal aqui. Embedding em cloud é onde SaaS sangra.

---

### 🔹 Respostas curtas e médias

- FAQ
- onboarding
- respostas objetivas
- instruções

---

## 2️⃣ O QUE NÃO VALE RODAR NO PC

Essas vão para **hosted**:

- respostas **muito longas**
- persuasão premium (vendas high-ticket)
- contexto gigante (32k+)
- muitos usuários simultâneos
- operação 24/7 sem depender do teu PC ligado
- geração massiva (100 posts, 300 análises, etc.)

---

## 3️⃣ MODELOS IDEAIS PRA TEU PC (RTX 4060)

### 🟢 Modelo principal (chat / raciocínio)

Escolhe **UM** desses (ordem prática):

- **Qwen2.5 7B Instruct (Q4 ou Q5)** ⭐⭐⭐⭐⭐
- **Llama 3.1 8B Instruct (Q4)** ⭐⭐⭐⭐
- **Mistral 7B Instruct (Q4)** ⭐⭐⭐⭐

👉 Contexto recomendado: **8k–16k**  
👉 VRAM segura: ~6–7 GB

---

### 🟢 Modelo de embeddings (obrigatório)

- **nomic-embed-text**

👉 Leve, rápido, perfeito pra Supabase / pgvector.

---

### 🟡 Testável (opcional, no limite)

- modelos 13B Q4 → só pra testes pontuais  
	Não recomendo produção no teu setup atual.

---

## 4️⃣ CONFIGURAÇÃO IDEAL DO OLLAMA (NO TEU CASO)

Na tela que tu mostrou:

### 🔧 Context length

- **16k** (padrão)
- sobe pra 32k **só se realmente precisar**

### 🔧 Expose to network

- **OFF**
- só localhost

### 🔧 Airplane mode

- opcional (pode deixar OFF)

---

## 5️⃣ ARQUITETURA GINKGO (DESENHO FINAL)

### 🔹 Local (PC)

```markdown
WhatsApp / Site
        ↓
     n8n / Manus
        ↓
     Ollama (PC)
  ├─ classifica
  ├─ extrai JSON
  ├─ resume
  └─ gera embeddings
```

### 🔹 Hosted (quando necessário)

```markdown
n8n / Manus
        ↓
Cloud LLM / Ollama hosted
        ↓
Resposta longa / pesada
```

---

## 6️⃣ ROTEADOR INTELIGENTE (regra de ouro)

No n8n cria um nó **AI\_ROUTER**:

### Envia pro PC quando:

- task = `classify | extract | summarize | embed`
- resposta curta
- lead frio/morno

### Envia pra cloud quando:

- task = `long_answer | persuasion | huge_context`
- lead quente
- PC offline
- fila > X segundos

👉 Isso é o que te permite **escalar a Ginkgo sem morrer em custo**.

---

## 7️⃣ PRÓXIMO PASSO (recomendado)

Se tu quiser, no próximo passo eu posso:

1. Te passar **os comandos exatos do Ollama** (pull dos modelos ideais)
2. Te dar o **JSON do nó HTTP do n8n** já pronto (local + fallback)
3. Desenhar o **“AI Router” padrão Ginkgo** (regras, campos, lógica)

Me diz só:  
👉 tu já está com **n8n rodando local, VPS ou ambos?**

A partir disso, a gente fecha o setup definitivo.

Sim. Dá pra orquestrar tudo com Manus + n8n + Hostinger (VPS) e transformar num “ **motor único** ” que alimenta **Leaf/Wave/Pyre** ao mesmo tempo — com isolamento por cliente e sem virar um monstro impossível de manter.

A chave é: **um Core (consciência) + 3 módulos (produtos) + um Router (cérebro de tráfego)**.

---

## 1) Arquitetura alvo: “Ginkgo Core + 3 Pods”

### Ginkgo Core (motor e consciência)

- **Manus**: regras, personas, prompts, “cérebro de negócio”
- **n8n**: execução/automação, webhooks, integrações, retries
- **DB (Supabase/Postgres)**: memória, clientes, planos, logs, eventos
- **Vector DB (pgvector/Qdrant)**: RAG por cliente/produto
- **Chatwoot**: handoff humano, inbox, auditoria de conversa
- **Ollama local + hosted**: inferência híbrida e barata
- **Storage (S3/Supabase Storage)**: arquivos, PDFs, mídias

### Pods (produtos)

- **Leaf Pod**: WhatsApp + atendimento + CRM + agenda + contratos
- **Wave Pod**: tráfego/CRM/campanhas + relatórios + tasks
- **Pyre Pod**: conteúdo + calendário + postagem + analytics

Cada “Pod” é um conjunto de fluxos + tabelas + prompts, mas todos usam o mesmo Core.

---

## 2) Como lançar os 3 juntos sem colapsar

O erro fatal é tentar “3 SaaS completos” ao mesmo tempo. O jeito certo é lançar **um Core único** e cada produto com **MVP funcional**.

### MVP de cada um (mínimo que vende)

**Leaf (MVP):**

- captação → qualificação → resposta → registro no CRM → handoff Chatwoot

**Wave (MVP):**

- intake do cliente (acessos/meta/google) → checklist → relatórios semanais automáticos → tasks

**Pyre (MVP):**

- briefing → geração de calendário → criação de posts → aprovação → postagem automática

Se esses 3 “ciclos” funcionarem, tu consegue vender e evoluir depois.

---

## 3) “Consciência” única: o Router de Inteligência

Tu precisa de um único endpoint que recebe tudo:

**`/ingest`**

- vem mensagem do WhatsApp
- vem pedido do painel
- vem evento do Instagram
- vem webhook do Stripe

E decide:

- qual produto (leaf/wave/pyre)
- qual cliente
- qual plano
- qual tarefa
- qual LLM (local vs hosted)

### Decisão (exemplo)

- task curta/estruturada → Ollama local
- task pesada/persuasiva → cloud/hosted
- se PC offline → hosted fallback

Isso vira a “consciência” de tudo.

---

## 4) Multi-tenant: 1 stack, 1000 clientes

Tu vai precisar disso desde o primeiro dia:

### Identidade mínima por cliente

- `tenant_id`
- `product` (leaf/wave/pyre)
- `plan`
- `channels` (whatsapp, insta, site…)
- `rate_limit`
- `allowed_tools`

### Isolamento de conhecimento

- RAG por `tenant_id`
- prompts com “context injection” por tenant
- logs separados por tenant

Sem isso, o sistema vira uma sopa e tu perde escala.

---

## 5) Hostinger/VPS: como organizar o deploy

No VPS (Hostinger), estrutura padrão:

**Reverse Proxy (Traefik ou Nginx)**

- roteia domínios/paths

**Containers**

- n8n
- Chatwoot
- Postgres (ou Supabase externo)
- Redis
- Qdrant (opcional)
- Evolution API (WhatsApp)
- MinIO (opcional)
- Ollama hosted (opcional)

O PC fica como “edge node” (inferência local). O VPS é o “datacenter”.

---

## 6) Painel SaaS (o que precisa existir pra vender)

Pra lançar os 3 juntos, o painel tem que ser simples e unificado:

### Onboarding único

1. cria conta
2. escolhe produto(s): Leaf/Wave/Pyre
3. conecta canais (WhatsApp, Meta, Google, etc.)
4. escolhe “perfil” (nicho, tom, objetivos)
5. “ativar agente”

### Monitoramento único

- status (verde/amarelo/vermelho)
- fila de mensagens
- últimos eventos (leads, posts, campanhas)
- handoff Chatwoot

Sem painel, suporte explode.

---

## 7) Fluxo de produção: “3 produtos, 1 pipeline”

Tu precisa de um pipeline único:

- **DEV** (tu)
- **STAGING** (testes)
- **PROD** (clientes)

E logs/observabilidade:

- latência por LLM
- erros por fluxo
- custo por tenant
- volume por canal

Sem isso, a distopia acontece: 3 SaaS viram 3 incêndios.

---

## 8) Caminho mais rápido: blueprint em 10 blocos

Se tu quiser lançar **Leaf/Wave/Pyre juntos**, faz nessa ordem:

1. **Auth + tenants + planos** (Stripe)
2. **Router `/ingest`** (n8n)
3. **DB base** (tenants, users, events, conversations)
4. **Leaf MVP** (WhatsApp → CRM → Chatwoot)
5. **Pyre MVP** (calendário → aprovação → postagem)
6. **Wave MVP** (checklist → relatórios semanais → tasks)
7. **RAG por tenant** (embeddings + busca)
8. **Fallback local/hosted** (Ollama)
9. **Painel unificado** (status + conexões + logs)
10. **Staging + monitoramento** (alertas)

---

## 9) Decisão estratégica (minha recomendação)

Dá pra lançar os 3 juntos, mas do jeito certo:

- **Um único Core + Router**
- **MVP de cada Pod**
- **Onboarding unificado**
- **Handoff humano**
- **Observabilidade desde o dia 1**

Isso é o “mech” completo: 3 braços, 1 cérebro.

---

## Próximo passo (sem enrolar)

Eu te entrego agora o desenho operacional (tabelas + endpoints + fluxos n8n) se tu escolher 1 destas duas estratégias:

**A) “3 juntos” (MVP triplo)**  
Leaf/Wave/Pyre com escopo mínimo e launch simultâneo.

**B) “Leaf primeiro, mas preparado pros 3”**  
Core + Router + Tenants + Leaf completo; Wave/Pyre entram plugando.

Se tu for pragmático pra produção: **B** é o mais seguro.  
Se tu quer marketing de “suite completa”: **A** é possível, com escopo controlado.

Escolha A ou B e eu te mando o blueprint técnico (estrutura de DB + endpoints + fluxos).

B.

## Estratégia B: Leaf primeiro, mas com o Core pronto pros 3

Objetivo: lançar o **Leaf em produção** sem gambiarra, com a arquitetura já preparada pra “plugar” Wave e Pyre depois, sem reescrever tudo.

A seguir está o **blueprint técnico** (Core + Router + DB + Fluxos n8n + Deploy Hostinger + Local/Hosted Ollama).

---

## 1) Ginkgo Core (o que existe desde o dia 1)

## Serviços (VPS Hostinger)

- **Reverse Proxy** (Traefik ou Nginx Proxy Manager)
- **n8n** (orquestração)
- **Evolution API** (WhatsApp)
- **Chatwoot** (handoff humano)
- **Postgres** (ou Supabase externo)
- **Redis** (fila/cache/memória curta)
- **Vector**: pgvector no Postgres (começa simples)
- **Storage**: Supabase Storage ou MinIO (opcional no início)
- **Ollama hosted** (opcional já no início como fallback)

## PC (Edge)

- **Ollama local** (classificar/extrair/resumir/embeddings)

---

## 2) Router único: /ingest (a “consciência”)

Tudo entra por um único fluxo no n8n.

### Entrada (webhook)

`POST /ingest`

Payload mínimo:

```markdown
{
  "channel": "whatsapp",
  "tenant_id": "tnt_123",
  "from": "+55...",
  "message": "texto...",
  "message_id": "xxx",
  "timestamp": 123456
}
```

### Saída (decisão do Router)

```markdown
{
  "product": "leaf",
  "task": "answer|extract|handoff",
  "llm_route": "local|hosted|cloud",
  "priority": "low|medium|high"
}
```

**Regras iniciais (Leaf):**

- `extract`, `classify`, `summarize` → **local**
- resposta curta/FAQ → **local**
- lead quente, negociação, texto longo → **hosted/cloud**
- PC offline → **hosted fallback**

---

## 3) Banco de dados (mínimo viável multi-tenant)

## Tabelas essenciais (Postgres/Supabase)

1. `tenants`
- `id`, `name`, `plan`, `status`, `created_at`
2. `channels`
- `id`, `tenant_id`, `type` (whatsapp), `provider` (evolution), `config_json`, `status`
3. `conversations`
- `id`, `tenant_id`, `channel_id`, `contact_id`, `status`, `last_message_at`
4. `messages`
- `id`, `tenant_id`, `conversation_id`, `role` (user/assistant/system), `content`, `raw_json`, `created_at`
5. `contacts`
- `id`, `tenant_id`, `phone`, `name`, `tags`, `lead_score`
6. `events`
- `id`, `tenant_id`, `type` (webhook\_received, routed, replied, handoff), `payload_json`, `created_at`
7. `kb_documents` (RAG)
- `id`, `tenant_id`, `source`, `title`, `content`, `metadata_json`
- embeddings via pgvector em tabela pareada: `kb_embeddings`

> Isso já nasce preparado pro Wave/Pyre porque tudo tem `tenant_id` e `type`.

---

## 4) Leaf MVP (produção): fluxos n8n

## Fluxo 1 — INGEST\_WHATSAPP

**Trigger:** Webhook do Evolution API  
**Etapas:**

1. validar `tenant_id` (mapeamento por número/instância)
2. gravar `event` + `message`
3. chamar **ROUTER** (LLM local)
4. decidir `task`

## Fluxo 2 — LEAF\_EXTRACT

**Objetivo:** preencher CRM/contato

- Ollama local extrai JSON (nome, intenção, orçamento, etc.)
- atualiza `contacts`, adiciona tags e lead\_score

## Fluxo 3 — LEAF\_ANSWER

**Objetivo:** responder no WhatsApp

- buscar contexto curto (últimas N mensagens)
- se precisar de RAG: consulta `kb_documents` via similaridade
- gerar resposta (local ou hosted/cloud)
- registrar `message assistant`
- enviar via Evolution API

## Fluxo 4 — LEAF\_HANDOFF\_CHATWOOT

**Objetivo:** quando precisa de humano

- criar/atualizar conversa no Chatwoot
- atribuir para inbox/time
- enviar mensagem ao usuário: “encaminhei pra um humano”

## Fluxo 5 — HEALTH + FALLBACK

- checar se Ollama local responde
- se não: trocar `llm_route` para hosted automaticamente

---

## 5) Prompts “padrão Leaf” (para o Router)

### Prompt Router (classifica)

Retornar JSON estrito:

- `intent`: venda | suporte | orçamento | agendamento | humano
- `urgency`: low/med/high
- `needs_handoff`: true/false
- `next_action`: answer | extract | handoff
- `suggested_product`: leaf (no começo sempre leaf)

### Prompt Extractor (lead JSON)

Retornar JSON com campos fixos e “unknown” quando faltar.

### Prompt Answer (Brann/Leaf)

- curto, objetivo
- 2–3 bullets
- 1 CTA
- sempre registrar dados faltantes (“pra te ajudar, me diz X e Y”)

---

## 6) Local vs Hosted: política prática (com teu PC)

## Local (PC) faz sempre:

- roteamento
- extração
- resumo
- embeddings
- respostas curtas

## Hosted (VPS) faz:

- fallback 24/7
- respostas longas
- picos
- contexto maior

**Detalhe crítico:** o n8n no VPS chama teu PC via rede **apenas se estiver seguro**. Se não tiver VPN/ZeroTier/Tailscale, não chama direto. Alternativas:

- rodar um n8n “satélite” local
- ou usar o hosted como primário e local como “assistente” quando possível

---

## 7) Deploy na Hostinger (padrão simples)

Estrutura por docker-compose:

- `traefik` / `npm`
- `n8n`
- `postgres`
- `redis`
- `chatwoot`
- `evolution-api`
- (opcional) `ollama`

Domínios:

- `api.ginkgo...` → webhooks/n8n
- `chat.ginkgo...` → chatwoot
- `wa.ginkgo...` → evolution
- `app.ginkgo...` → painel (depois)

---

## 8) Painel (MVP) — mínimo pra não morrer no suporte

Mesmo que seja simples no começo:

- conectar WhatsApp (QR / status)
- status do agente (on/off)
- inbox (link pro Chatwoot)
- logs recentes (erros / últimas mensagens)
- configurar “tom” + FAQ básica

---

## 9) Roadmap: do Leaf ao Wave/Pyre sem dor

Quando Leaf estiver liso:

- **Wave** pluga no mesmo `/ingest` como canal “ads/analytics events”
- **Pyre** pluga como “content tasks” + calendário + postagem

Nada muda no Core. Só adiciona Pods.

---

## 10) Próximo passo imediato (execução)

Escolhe 1 destes caminhos de implementação (eu recomendo o 1):

### Caminho 1 (mais seguro)

- Tudo “server-first” no VPS (n8n + evolution + chatwoot)
- Ollama local só como **auxiliar** quando possível
- Hosted LLM garante 24/7

### Caminho 2 (mais barato, mais frágil)

- Ollama local é o principal
- VPS é só orquestrador + fallback
- depende do teu PC ligado

---

## Agora, pra eu fechar o blueprint com comandos e peças copiáveis

Sem pergunta longa. Só responde com uma linha:

**Tu vai usar o WhatsApp via Evolution API no VPS Hostinger (sim/não)?**  
Se sim, eu já te passo:

- mapa de endpoints (Evolution → n8n)
- payloads padrão
- estrutura mínima do docker-compose
- e os prompts JSON do Router/Extractor prontos.