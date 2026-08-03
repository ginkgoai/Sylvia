---
title: "Ginkgo Core - Site Ginkgo Leaf SaaS"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/694f04ff-b08c-832e-8952-8cca2e7204d8"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 26 de dez. às 18:59

![60da6621-0122-4d85-b719-bdec6c0e8adb.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000af6071f5bbf19f47c16da6e9&ts=495694&p=fs&cid=1&sig=586b5e763634eeb611ef44e97438d9660df6831fb6e786d264b6af4435632ef5&v=0)

vamos fazer um site para a ginkgo usando lovable visando apenas o leaf saas e a ginkgo storytelling e um breve resumo de tudo https://c3.ai/

sáb., 27 de dez. às 19:58

sáb., 27 de dez. às 21:21

## Rota 2 — Construir certo (multicanal IG + Whats)

A ideia: **1 cérebro (Callima/LEAF) + 2 portas (ManyChat IG + Evolution Whats) + 1 sistema nervoso (n8n) + 1 memória (Supabase/CRM)**.

Abaixo está o passo a passo separando **o que já está pronto** vs **o que precisa construir**, com blueprint técnico (n8n + Supabase + regras + integrações).

---

## 0) O que já temos pronto (stack atual)

**Você já tem:**

- **ManyChat** (Instagram DM / gatilhos / UI de conversa)
- **Evolution Manager** (WhatsApp Webhook / envio / sessões)
- **n8n** (orquestração)
- **Supabase** (dados / auth / storage)
- **Chatwoot** (handoff humano / inbox)
- **Stripe** (assinatura / upgrade)
- **Manus** (agente / “cérebro”)
- **Easypanel** (deploy)

**O que isso já permite hoje:**  
Conectar canais → n8n → agente → responder + registrar + handoff.

---

## 1) O que precisa ser construído (essencial para SaaS multicanal)

### A) Camada SaaS (multi-tenant + limites)

- Modelo de **empresa (tenant)**, **usuários**, **planos**, **limites por canal**
- Sync com Stripe (assinou → libera recursos / cancelou → restringe)

### B) Gateway de Mensagens (padronizar IG e Whats)

- Um “ **normalizador** ” no n8n: qualquer mensagem vira um objeto padrão (independente do canal)

### C) Memória e CRM (do cliente ou seu)

- Persistência de leads/conversas/deals
- Conector para CRM do cliente (ou usar Supabase como CRM Light)

### D) RAG / Knowledge Base por cliente

- Base de conhecimento por tenant (FAQ, catálogo, docs)
- Recuperação de contexto para respostas melhores

### E) Observabilidade + backup

- Logs, alertas e versionamento de fluxos (pra não morrer na praia)

---

## 2) Arquitetura final (mental graph)

**Instagram DM (ManyChat)**  
→ Webhook (n8n /ingress/manychat)  
→ Normalizador (payload padrão)  
→ Router (intenção + regras)  
→ Core (Manus/LLM + RAG + políticas)  
→ Persistência (Supabase/CRM)  
→ Resposta (ManyChat “send message”)  
→ (Opcional) “migrar para WhatsApp” via link wa.me

**WhatsApp (Evolution)**  
→ Webhook (n8n /ingress/evolution)  
→ mesmo pipeline acima  
→ Resposta via Evolution send message  
→ Handoff humano via Chatwoot quando necessário

---

## 3) Construção passo a passo (ordem que dá menos dor)

## Passo 1 — Definir os planos como “capabilities” (base / pro / omni)

Crie uma tabela mental de capacidades:

- **BASE**: 1 canal (IG ou WA), captação+FAQ, handoff, registro
- **TOP 1 (Callima Whats)**: Whats + followup + pipeline + relatórios
- **TOP 2 (Omni)**: Whats + IG + roteamento + CRM integrado + governança

**Isso vira variável no Supabase** e regra no n8n.

---

## Passo 2 — Criar o modelo SaaS no Supabase (multi-tenant)

Crie estas tabelas (mínimo viável, mas certo):

### tenants

- `id`
- `name`
- `plan` (base/pro/omni)
- `status` (active/past\_due/canceled)
- `created_at`

### tenant\_channels

- `tenant_id`
- `channel` (instagram / whatsapp)
- `provider` (manychat / evolution)
- `external_id` (ig\_page\_id, phone\_number\_id, etc.)
- `is_enabled`

### contacts

- `id`
- `tenant_id`
- `channel` (instagram/whatsapp)
- `external_user_id` (psid/ig user id / wa jid)
- `name`
- `phone`
- `email`
- `tags` (json)
- `created_at`

### conversations

- `id`
- `tenant_id`
- `contact_id`
- `channel`
- `status` (open/closed/handoff)
- `last_message_at`

### messages

- `id`
- `tenant_id`
- `conversation_id`
- `direction` (in/out)
- `text`
- `raw_payload` (json)
- `created_at`

### deals (pipeline)

- `id`
- `tenant_id`
- `contact_id`
- `stage` (lead/qualificado/proposta/fechado/perdido)
- `value_estimate`
- `notes`

### events (audit/logs)

- `tenant_id`
- `type` (webhook\_received, message\_sent, error, handoff)
- `payload` (json)
- `created_at`

**Políticas (RLS):**

- Tudo filtrado por `tenant_id`.
- Você (admin) vê tudo; cliente só o tenant dele.

---

## Passo 3 — Normalizador de mensagens (o “adaptador universal”)

No n8n, crie dois endpoints:

### A) POST /ingress/manychat

Recebe payload do ManyChat (IG DM).  
Transforma em:

```markdown
{
  "tenant_id": "…",
  "channel": "instagram",
  "provider": "manychat",
  "contact": {
    "external_user_id": "…",
    "name": "…",
    "phone": null,
    "email": null
  },
  "message": {
    "text": "…",
    "type": "text"
  },
  "meta": { "raw": { } }
}
```

### B) POST /ingress/evolution

Recebe payload do Evolution (Whats).  
Transforma no MESMO formato, mudando só `channel/provider`.

**Por que isso é crítico:**  
Você constrói **um único pipeline** pro cérebro. Sem duplicar lógica por canal.

---

## Passo 4 — Router de intenção + regras por plano

Após normalizar, aplique regras:

### Regras de plano (gating)

- Se `plan=base` e canal recebido não está habilitado → responder: “canal não ativo, fale pelo X”
- Se `plan=pro` → Whats liberado, IG bloqueado (ou limitado)
- Se `plan=omni` → tudo liberado

### Router de intenção (mínimo)

- `info/faq`
- `lead_capture`
- `pricing/plan`
- `schedule/demo`
- `handoff_human`
- `complaint/urgent`

Isso pode ser:

- Regras simples (keywords + contexto)
- Ou um “classificador” (LLM curto)

---

## Passo 5 — Core LLM (Manus) com ferramentas

O “Core” deve receber:

- `tenant_id`
- `channel`
- `contact context` (tags, estágio, histórico curto)
- `knowledge snippets` (RAG)
- `policies` (o que pode/não pode responder)

E devolver:

- `reply_text`
- `actions[]` (ex: salvar lead, mover estágio, pedir telefone, criar handoff)
- `handoff` (true/false)

---

## Passo 6 — Persistência & CRM (duas rotas)

### Rota A: CRM do cliente

Você cria um “conector” no n8n:

- Mapeia campos (`name`, `phone`, `source=instagram`, `stage=qualificado`)
- Atualiza CRM via API
- Supabase guarda **somente logs + chaves**

### Rota B: CRM Light (Supabase)

Você usa tabelas `contacts/deals` como CRM.  
Depois dá export / integração quando precisar.

**Recomendação prática:**  
Começa com **CRM Light** pra escalar onboarding. Integra CRM do cliente só nos planos TOP.

---

## Passo 7 — Resposta por canal (saída)

### Instagram (ManyChat)

Você tem duas opções:

1. n8n chama a API do ManyChat “Send Content” (resposta)
2. n8n retorna payload e ManyChat exibe via step

**Mais robusto:** opção 1 (n8n manda).

### WhatsApp (Evolution)

n8n chama node HTTP “sendMessage” no Evolution.

---

## Passo 8 — Handoff humano (Chatwoot)

Quando `handoff=true`:

- Criar conversa/ticket no Chatwoot
- Anexar resumo automático:
	- intenção
		- dados coletados
		- histórico curto
		- próximos passos sugeridos

E marcar conversa como `handoff` em `conversations`.

---

## Passo 9 — Base de conhecimento (RAG)

Para OMNI/PRO, crie:

- `knowledge_sources` (tipo: faq/pdf/url)
- `knowledge_chunks` (texto + embedding + tenant\_id)

Ingestão:

- cliente envia PDF/FAQ/link
- n8n processa
- salva chunks
- embeddings (pode ser via provider que você já usa)
- consulta por similaridade por tenant

**MVP RAG simples:** FAQ + catálogo em tabela mesmo, sem chunking.  
Depois evolui.

---

## Passo 10 — Stripe → Supabase (ativação automática)

Criar webhooks Stripe:

- `checkout.session.completed`
- `invoice.payment_succeeded`
- `invoice.payment_failed`
- `customer.subscription.deleted`

Ações:

- atualizar `tenants.plan` e `tenants.status`
- habilitar/desabilitar `tenant_channels`
- (opcional) mandar mensagem no Whats/Email “assinatura ativa / falhou”

---

## 4) Blueprint de Workflows n8n (nomes prontos)

Crie estes workflows:

1. **INGRESS\_MANYCHAT**  
	Webhook → Normalize → Upsert Contact → Push to ROUTER
2. **INGRESS\_EVOLUTION**  
	Webhook → Normalize → Upsert Contact → Push to ROUTER
3. **ROUTER\_CORE**  
	Load Tenant + Plan Gate → Intent Router → (RAG fetch) → Manus Core → Persist → Dispatch → (handoff)
4. **DISPATCH\_MANYCHAT**  
	Send message via ManyChat API
5. **DISPATCH\_EVOLUTION**  
	Send message via Evolution API
6. **HANDOFF\_CHATWOOT**  
	Create conversation + add notes + notify
7. **STRIPE\_WEBHOOKS**  
	Update tenant plan/status + enable channels
8. **KNOWLEDGE\_INGEST**  
	Upload/URL → chunk → embed → store
9. **OBS\_ALERTS**  
	On error → log event → notify WhatsApp admin

---

## 5) O que construir primeiro (sequência de execução)

Se você seguir essa ordem, em 1–2 ciclos já tem OMNI funcionando:

1. **Supabase multi-tenant (tabelas + RLS básico)**
2. **Ingress IG + Ingress WA normalizados**
3. **Router + Core (Manus) + Dispatch**
4. **Chatwoot handoff**
5. **Stripe gating de plano**
6. **RAG (mínimo)**
7. **Observabilidade + backup**

---

## 6) Entrega “pronta pra vender” (sem virar custom)

Quando isso estiver de pé, você consegue vender upgrade assim:

- Base: 1 canal + CRM light
- Pro: Whats + pipeline + followup + relatórios
- Omni: IG + Whats + roteamento + CRM do cliente + governança + RAG

---

## Próximo passo imediato (sem pergunta aberta)

Escolha um para começarmos agora (eu te guio clique a clique no n8n / Supabase):

**A)** Montar as tabelas Supabase + RLS (multi-tenant)  
**B)** Fazer o normalizador do ManyChat (IG) + Evolution (WA) no n8n  
**C)** Desenhar o workflow ROUTER\_CORE (intenção + manus + persist + dispatch)

Se você quer velocidade sem retrabalho: **começa por (B)** e em seguida (A).

Abaixo está o **resumo completo, técnico e estratégico do SaaS LEAF**, escrito **exatamente no formato ideal para contextualizar a Manus** (como cérebro/agent framework).  
Isso não é copy de site — é **documentação viva de produto**.

---

## LEAF — Resumo Completo do SaaS

**Contexto oficial para Manus (Agente Central)**

## 1\. O que é o LEAF

O **LEAF** é um **SaaS de agentes de IA para atendimento, vendas e operação**, focado em empresas que precisam escalar conversas, leads e processos **sem perder controle, dados ou qualidade**.

O LEAF não é um “chatbot”.  
Ele é um **sistema operacional de conversas e fluxos comerciais**, com:

- múltiplos canais (WhatsApp, Instagram)
- um cérebro central (IA + regras)
- persistência de dados
- handoff humano estruturado
- governança SaaS (planos, limites, logs)

---

## 2\. Filosofia do produto

Princípios que guiam TODA a lógica do LEAF:

1. **Um cérebro, múltiplos canais**  
	A inteligência é centralizada. Canais são apenas interfaces.
2. **Automação com controle humano**  
	IA opera, humano assume quando importa — com contexto completo.
3. **Dados pertencem ao cliente**  
	LEAF integra ou cria bancos, nunca sequestra informação.
4. **SaaS, não serviço artesanal**  
	Tudo é replicável, versionado e controlado por plano.

---

## 3\. Arquitetura conceitual (alto nível)

### Camadas do LEAF

1. **Canais (Entrada)**
	- WhatsApp (Evolution API)
		- Instagram DM (ManyChat)
2. **Orquestração**
	- n8n (roteamento, regras, integrações)
3. **Cérebro**
	- Manus (LLM + ferramentas + políticas)
4. **Memória / Dados**
	- Supabase (CRM light, logs, histórico)
		- ou CRM do cliente (HubSpot, PipeDrive, etc.)
5. **Handoff humano**
	- Chatwoot (inbox, tickets, contexto)
6. **Governança SaaS**
	- Stripe (planos, upgrades, limites)
		- Controle multi-tenant

---

## 4\. Papel específico da Manus (muito importante)

A **Manus é o cérebro cognitivo do LEAF**, responsável por:

- interpretar intenção da mensagem
- decidir ações (responder, perguntar, salvar, escalar)
- usar ferramentas (CRM, banco, agenda, catálogo)
- respeitar políticas do plano contratado
- manter coerência de persona (Callima / LEAF)

A Manus **NÃO**:

- recebe payload cru de canal
- gerencia webhooks
- fala diretamente com WhatsApp ou Instagram

Ela recebe sempre um **contexto limpo, estruturado e seguro**.

---

## 5\. Modelo SaaS (multi-tenant)

O LEAF opera em **multi-tenant real**, onde:

- Cada empresa = 1 tenant
- Cada tenant possui:
	- plano ativo
		- canais habilitados
		- limites de uso
		- base de dados própria
		- configurações próprias

A Manus **sempre recebe o `tenant_id`** e deve:

- agir exclusivamente dentro daquele contexto
- nunca misturar dados entre empresas
- respeitar limites e permissões do plano

---

## 6\. Planos do LEAF (lógica funcional)

### Plano BASE (Starter)

- 1 canal (WhatsApp **ou** Instagram)
- FAQ + triagem
- captação de leads
- handoff humano
- registro básico de dados

Uso típico:

- atendimento inicial
- captura fora do horário
- resposta automática simples

---

### Plano TOP 1 — Callima WhatsApp

- WhatsApp completo
- qualificação inteligente
- follow-ups
- pipeline de vendas
- relatórios
- CRM integrado (ou Supabase)

Uso típico:

- vendas
- agendamentos
- serviços recorrentes

---

### Plano TOP 2 — Callima OMNI

- WhatsApp + Instagram
- roteamento IG → Whats
- CRM avançado
- tratamento e normalização de dados
- base de conhecimento (RAG)
- governança completa

Uso típico:

- negócios com tráfego social
- equipes comerciais
- escala real

---

## 7\. Fluxo padrão de uma conversa

### Exemplo: Instagram → WhatsApp

1. Lead envia DM no Instagram
2. ManyChat captura e envia para n8n
3. n8n normaliza mensagem
4. n8n carrega contexto do tenant
5. n8n chama Manus com:
	- histórico resumido
		- dados do lead
		- regras do plano
		- conhecimento do negócio
6. Manus decide:
	- responder
		- coletar dados
		- mover estágio
		- migrar para WhatsApp
7. Resposta volta ao canal correto
8. Dados persistidos
9. Se necessário, handoff humano

---

## 8\. Dados e Memória (como o LEAF “lembra”)

O LEAF mantém memória em camadas:

1. **Memória curta**
	- contexto recente da conversa
2. **Memória longa**
	- histórico de mensagens
		- dados do lead
		- estágio no funil
		- preferências
3. **Conhecimento do negócio (RAG)**
	- FAQs
		- catálogos
		- PDFs
		- regras internas

A Manus **consulta essas camadas antes de responder**.

---

## 9\. Handoff humano (regra de ouro)

A IA **NUNCA compete com o humano**.

A Manus deve sinalizar handoff quando:

- pedido crítico
- reclamação
- negociação sensível
- lead muito quente
- erro ou ambiguidade

No handoff, o humano recebe:

- resumo automático
- dados já coletados
- intenção detectada
- sugestão de próximo passo

---

## 10\. Observabilidade e segurança

O LEAF registra:

- todas as mensagens
- decisões da IA
- ações executadas
- erros e exceções

Isso permite:

- auditoria
- melhoria contínua
- confiabilidade enterprise

---

## 11\. Diferencial do LEAF (posição de mercado)

O LEAF se posiciona como:

> **“Um time digital que opera conversas e processos comerciais 24/7, com inteligência, dados e controle.”**

Ele não compete com:

- bots simples
- automações rasas
- chat genérico

Ele compete com:

- contratação de equipe
- perda de leads
- processos manuais
- caos operacional

---

## 12\. Resumo final (1 parágrafo para Manus)

> O LEAF é um SaaS multi-tenant de agentes de IA para atendimento e vendas, com múltiplos canais (WhatsApp e Instagram), um cérebro central (Manus), orquestração via n8n, persistência de dados em Supabase ou CRM do cliente, handoff humano estruturado e governança por planos. A Manus atua como o núcleo cognitivo, tomando decisões com base em contexto, dados, regras de plano e conhecimento do negócio, sempre respeitando limites, segurança e separação entre clientes.

---

Se quiser, no próximo passo eu posso:

- converter isso em **prompt system oficial da Manus**
- gerar a **versão “think” + “act” separadas**
- criar **diagramas mentais (graph-style)** para documentação interna

Qual você quer agora?

sáb., 27 de dez. às 23:42

Perfeito. Abaixo está um **mix realista e estratégico de FAQs** que **clientes B2B realmente perguntam** antes, durante e depois da contratação de um SaaS como o **LEAF**.  
Isso já vem **pronto para**: site, WhatsApp, ManyChat, base RAG da Manus e treino do Callima.

Vou organizar por **blocos mentais**, porque é assim que o cliente pensa.

---

## 🔹 FAQ — VISÃO GERAL DO LEAF

**O que exatamente é o LEAF?**  
O LEAF é um agente de IA que automatiza atendimento, captação de leads e rotinas operacionais em canais como WhatsApp e Instagram, com controle humano quando necessário.

**O LEAF é só um chatbot?**  
Não. Chatbots respondem perguntas. O LEAF **entende intenção, executa ações, registra dados, qualifica leads e integra com sistemas**.

**O LEAF substitui pessoas?**  
Não. Ele remove tarefas repetitivas. Pessoas entram quando a conversa exige decisão humana.

**O LEAF serve para qualquer tipo de negócio?**  
Ele é ideal para negócios que recebem mensagens recorrentes: serviços, imobiliárias, clínicas, e-commerces, delivery e times comerciais.

---

## 🔹 FAQ — CANAIS (WhatsApp / Instagram)

**O LEAF funciona no WhatsApp?**  
Sim. Utilizamos WhatsApp via API oficial, com atendimento 24/7 e histórico completo.

**O LEAF funciona no Instagram?**  
Sim. Através de automação de DM (ex: ManyChat), integrado ao mesmo cérebro do WhatsApp.

**WhatsApp e Instagram usam a mesma IA?**  
Sim. É **um único cérebro**, com múltiplos canais de entrada.

**Posso começar só com WhatsApp ou só com Instagram?**  
Sim. O multicanal é um upgrade, não uma obrigação.

**O LEAF pode migrar uma conversa do Instagram para o WhatsApp?**  
Sim. Quando faz sentido (orçamento, fechamento, dados sensíveis).

---

## 🔹 FAQ — IMPLEMENTAÇÃO

**Quanto tempo leva para implementar o LEAF?**  
Normalmente entre **7 e 14 dias**, dependendo da complexidade do negócio.

**Preciso mudar meus processos para usar o LEAF?**  
Não. O LEAF se adapta ao seu processo atual e depois sugere melhorias.

**Preciso ter conhecimento técnico?**  
Não. Toda a configuração é guiada e o uso é simples.

**Vocês fazem o setup inicial?**  
Sim. A implementação é feita pela equipe da Ginkgo ou de forma assistida, conforme o plano.

---

## 🔹 FAQ — DADOS, CRM E INTEGRAÇÕES

**O LEAF salva os dados dos clientes?**  
Sim, sempre com controle e organização.

**Os dados ficam comigo ou com vocês?**  
Os dados **pertencem ao cliente**. O LEAF apenas processa e organiza.

**Posso integrar com meu CRM atual?**  
Sim. Integramos com CRMs existentes ou criamos um CRM leve inicial.

**O LEAF pode usar minha base atual de clientes?**  
Sim. Podemos importar e adaptar a base existente.

**O LEAF gera relatórios?**  
Sim. Relatórios de leads, conversões, gargalos e performance.

---

## 🔹 FAQ — IA, CONTROLE E SEGURANÇA

**A IA responde qualquer coisa sozinha?**  
Não. O LEAF opera com **regras, limites e políticas claras**.

**Posso definir o que a IA pode ou não responder?**  
Sim. O comportamento é totalmente configurável.

**E se a IA errar?**  
Erros são registrados, corrigidos e usados para melhoria contínua.

**Existe handoff para atendimento humano?**  
Sim. Quando necessário, a conversa é transferida com todo o contexto.

**O LEAF segue LGPD?**  
Sim. O sistema é projetado com boas práticas de segurança e privacidade.

---

## 🔹 FAQ — PLANOS E LIMITES

**O que muda entre os planos?**  
Quantidade de canais, nível de automação, integrações, relatórios e governança.

**Posso começar no plano básico e fazer upgrade depois?**  
Sim. O upgrade é imediato.

**Existe fidelidade ou contrato longo?**  
Depende do plano. Em geral, modelo mensal, estilo SaaS.

**O LEAF funciona 24/7 mesmo?**  
Sim. Ele não depende de horário comercial.

---

## 🔹 FAQ — RESULTADOS E EXPECTATIVAS

**O LEAF garante aumento de vendas?**  
Ele **remove gargalos comuns** que impedem vendas: demora, falta de follow-up e desorganização.

**Em quanto tempo vejo resultados?**  
Normalmente nas primeiras semanas de uso.

**O LEAF pode escalar com meu negócio?**  
Sim. Ele foi pensado para crescer junto com a operação.

---

## 🔹 FAQ — SUPORTE E OPERAÇÃO

**Quem dá suporte após a implementação?**  
A equipe da Ginkgo, com apoio do próprio LEAF.

**O LEAF precisa de manutenção constante?**  
Não. Ajustes pontuais e melhorias contínuas são feitas conforme uso.

**Se eu cancelar, perco meus dados?**  
Não. Os dados podem ser exportados.

---

## 🔹 FAQ — PERGUNTAS “DESCONFIADAS” (as mais importantes)

**Isso já funciona em empresas reais?**  
Sim. O LEAF foi desenhado a partir de problemas reais de operação.

**Isso não é só hype de IA?**  
Não. O foco é **processo, dados e resultado**, não buzzword.

**O que diferencia vocês de outros bots?**  
O LEAF não responde só mensagens — ele **opera o negócio**.

---

## Como usar isso agora (recomendado)

Você pode:

1. **Colar tudo como base RAG** da Manus
2. Usar versões curtas no site
3. Criar respostas automáticas no WhatsApp/Instagram
4. Treinar o Callima para objeções reais

Se quiser, no próximo passo eu:

- transformo isso em **JSON estruturado para RAG**
- separo por **intenção (pré-venda, técnica, objeção)**
- crio a **versão “resposta curta de chat” vs “resposta longa”**

Qual você quer?