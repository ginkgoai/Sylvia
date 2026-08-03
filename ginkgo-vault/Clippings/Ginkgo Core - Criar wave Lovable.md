---
title: "Ginkgo Core - Criar wave Lovable"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/690a3fae-9114-8327-a702-4ad84b51a7d2"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
Segue o prompt completo para a Lovable, com **todas** as menções à Ginkgo explicadas de forma operacional. Copie e cole.

---

## Título

Ginkgo Wave — Automação de Tráfego, Conteúdo e Conversão com IA

## Descrição geral

Construa um web app SaaS chamado **Ginkgo Wave**. O Wave é o módulo de **aquisição e crescimento** do ecossistema **Ginkgo AI Systems**. Ele integra anúncios, conteúdo, CRM, WhatsApp, automações n8n e IA para gerar, nutrir e converter leads.

## O que é “Ginkgo AI Systems”

- **Holding de produtos de IA**. Pilares:
	- **Leaf**: agentes de atendimento e operações.
		- **Wave**: tráfego, conteúdo e conversão.
		- **Golden Leaf**: marketplace de templates.
		- **Academy**: treinamentos.
- O **Wave** deve operar **sozinho**, mas prever integrações nativas com Leaf e Nyra.

## Identidade visual Ginkgo

- Cores: **#0EA5E9** (azul), **#0B1220** (fundo escuro), **#FFFFFF** (texto), acentos com **#A7F3D0**.
- Tipos: Inter ou Sora.
- UI SaaS minimalista. Cartões com cantos 16–20px. Sombra leve. Ícones lineares.

---

## Requisitos funcionais

## 1) Autenticação e planos

- E-mail + senha. Magic link opcional.
- Planos: **Básico**, **Avançado**, **Futurista**.
- Bloqueios por feature flag por plano.

## 2) Dashboard

- KPI cards: CPC, CPA, ROAS, Leads, Conversões, Receita.
- Gráficos de séries por canal (Meta, Google, TikTok).
- **Recomendações IA**: lista priorizada com ação sugerida e impacto estimado.

## 3) Campanhas

- Listar campanhas por canal.
- Criar/editar: objetivo, orçamento, público, criativos.
- **Assistente IA**: gerar rascunho de campanha a partir de metas.
- Estado: rascunho, ativa, pausada, encerrada.

## 4) Conteúdo (Nyra integrado)

- Gerar post, legenda, variações de anúncio, roteiro de vídeo.
- Biblioteca de criativos com tags.
- Agendar postagem.
- Métrica por peça: impressões, cliques, CTR, custo, conversões atribuídas.

## 5) Leads e CRM

- Tabela de leads com fases do funil: Capturado → Qualificado → Oportunidade → Cliente.
- Campos: nome, contato, origem, interesse, nota, owner.
- Segmentação por regras.
- Ações em lote: e-mail, WhatsApp, marcar etapa.

## 6) Automação (n8n)

- Tela de **Triggers**: evento → ação.
- Exemplos de gatilhos: “Lead criado”, “Campanha abaixo do ROAS alvo”, “Mensagem WhatsApp recebida”, “Pagamento aprovado”.
- Ações: “Enviar para fluxo n8n”, “Criar tarefa”, “Gerar áudio/arte com IA”, “Disparar e-mail/WhatsApp”.

## 7) WhatsApp (Evolution API)

- Caixa de entrada vinculada ao lead.
- Enviar/receber texto, áudio, arquivo.
- Modelos prontos: confirmação, cobrança, follow-up.

## 8) Pagamentos e checkout

- Stripe e Hotmart.
- Webhooks para ativar plano e registrar cliente.

## 9) Configurações do workspace

- Chaves API por canal.
- Domínio de LP, pixel/gtag.
- Times e permissões.

---

## Arquitetura técnica

## Páginas e rotas

- `/login`, `/signup`, `/billing`
- `/dashboard`
- `/campaigns` e `/campaigns/:id`
- `/content` e `/content/new`
- `/leads` e `/leads/:id`
- `/automation/triggers`
- `/inbox/whatsapp`
- `/settings/general`, `/settings/integrations`, `/settings/team`, `/settings/plan`

## Componentes principais

- `KpiCard`, `TimeseriesChart`, `RecommendationList`
- `CampaignTable`, `CampaignEditor`, `AudienceForm`
- `ContentGenerator`, `ContentLibrary`
- `LeadTable`, `LeadProfile`, `SegmentBuilder`
- `TriggerBuilder`, `ActionPicker`
- `WhatsAppThread`, `MessageComposer`
- `ApiKeyForm`, `TeamManager`, `PlanGate`

## Modelos (Supabase)

- `users(id, email, name, role)`
- `workspaces(id, name, plan, owner_id)`
- `workspace_users(workspace_id, user_id, role)`
- `integrations(workspace_id, provider, access_token, meta)`
- `campaigns(id, workspace_id, channel, objective, budget, status, kpis_json)`
- `creatives(id, workspace_id, type, title, content, metrics_json, tags)`
- `leads(id, workspace_id, name, phone, email, source, stage, score, owner_id, notes)`
- `events(id, workspace_id, type, payload_json, created_at)`
- `automations(id, workspace_id, trigger_json, actions_json, enabled)`
- `messages(id, workspace_id, lead_id, channel, direction, content, meta)`
- `recommendations(id, workspace_id, title, reason, action_json, impact_score, status)`
- `billing_customers(id, workspace_id, provider, external_id, plan, status)`

Índices por `workspace_id` e por `created_at` onde aplicável.

## Env vars esperadas

```markdown
SUPABASE_URL
SUPABASE_ANON_KEY
OPENAI_API_KEY
N8N_WEBHOOK_URL
EVOLUTION_API_BASE_URL
EVOLUTION_API_TOKEN
STRIPE_PK
STRIPE_SK
HOTMART_WEBHOOK_SECRET
GOOGLE_ADS_OAUTH
META_ADS_TOKEN
TIKTOK_ADS_TOKEN
```

---

## Integrações detalhadas da Ginkgo

## Leaf (quando presente)

- Leaf = agentes de atendimento. O Wave pode enviar **tarefas** ao Leaf: “ligar para lead”, “gravar áudio”, “coletar documentos”.
- Protocolo: **HTTP webhook** assíncrono. Payload com `lead_id`, `task_type`, `params`.
- Leaf responde com `status` e `result_url` ou `transcript`.

## Nyra (conteúdo)

- Nyra = motor de criação. O Wave chama Nyra para gerar textos, variações, thumbnails.
- Entrada: `goal`, `brand_tone`, `constraints`.
- Saída: `assets[]` com tipo, título, corpo, anexos.

## Golden Leaf (futuro)

- Marketplace de templates. O Wave deve “instalar” templates de automação e dashboards.

---

## IA e recomendações

## Prompts base

- “Você é o otimizador de crescimento do Ginkgo Wave. Gere recomendações priorizadas para aumentar ROAS ou reduzir CAC usando métricas recentes e histórico. Saída: título, racional, ação com parâmetros, risco, impacto estimado.”

## Ações IA automáticas

- Ajuste de orçamento com teto ±20%.
- Pausa de anúncios com CTR < x ou CPA > y.
- Sugestões de novos públicos lookalike.
- Geração de 3 variações de criativo quando queda de performance for detectada.

---

## Automação n8n

## Trigger JSON (exemplo)

```markdown
{
  "on": "lead.created",
  "filters": {"source": ["meta_ads", "lp"]},
  "actions": [
    {"type": "webhook", "url": "{{N8N_WEBHOOK_URL}}/lead-new", "payload": {"lead_id": "{{lead.id}}" }},
    {"type": "whatsapp.template", "template": "welcome_lead", "to": "{{lead.phone}}"}
  ]
}
```

## Eventos emitidos

- `lead.created`, `lead.updated`, `lead.stage_changed`
- `campaign.kpi_dropped`, `campaign.paused`, `creative.generated`
- `billing.plan_activated`, `billing.payment_failed`

---

## WhatsApp via Evolution API

## Funções

- Listar conversas por `lead_id`.
- Enviar texto/áudio/arquivo.
- Webhook receptor salva `messages`.

## Fluxo simples

1. Lead criado → checar telefone.
2. Se válido → enviar mensagem de boas-vindas.
3. Registrar resposta no `messages`.
4. Opcional: chamar Leaf para áudio com voz.

---

## Billing

## Stripe

- Checkout de assinatura por plano.
- Webhooks: `checkout.session.completed` → atualizar `billing_customers.status="active"` e `workspaces.plan`.

## Hotmart

- Webhook de compra/assinatura.
- Mapear produto → plano.
- Idem atualização de status.

---

## Permissões

- **Owner**: tudo.
- **Manager**: campanhas, leads, conteúdo, automações.
- **Agent**: leads e inbox.
- **Viewer**: somente leitura.

---

## Experiência inicial (onboarding)

1. Criar workspace.
2. Conectar canais de anúncio.
3. Conectar WhatsApp.
4. Instalar 3 automações recomendadas.
5. Gerar primeira campanha com IA.
6. Importar leads CSV.
7. Ativar checkout do plano.

---

## Seed de dados para protótipo

- 3 campanhas por canal com KPIs falsos coerentes.
- 20 leads variados por origem.
- 10 criativos com métricas.
- 4 recomendações IA pendentes.

---

## Critérios de aceite

- Dashboard com KPIs e gráfico funcionando com dados de seed.
- CRUD completo: campanhas, criativos, leads, automações.
- Envio/recebimento WhatsApp simulado.
- Tela de recomendações IA com ação aplicável.
- Integrações configuráveis por workspace.

---

## Roadmap curto

- V1: métricas unificadas, geração de criativo, CRM, automações básicas, WhatsApp, Stripe.
- V1.1: segmentação avançada, funis custom, A/B de criativos.
- V1.2: templates do Golden Leaf, integração Leaf full-duplex.

---

Quer que eu entregue também um **roteiro de componentes + pseudo-código de serviços** para a Lovable gerar arquivos e chamadas padrão?

deixe claro que todas interações e configurações vao ser feita via linguagem natural.

Prompt completo revisado para **Lovable**, versão final com **interações e configurações 100% em linguagem natural** — pronto para colar e gerar o app Ginkgo Wave:

---

## Título

**Ginkgo Wave — Automação de Tráfego e Crescimento com IA em Linguagem Natural**

---

## Descrição geral

Crie um **web app SaaS completo** chamado **Ginkgo Wave**, pertencente à holding **Ginkgo AI Systems**.  
O Wave é o **sistema de automação de tráfego, conteúdo e conversão com IA conversacional**, onde **todas as ações, configurações e comandos são feitos via linguagem natural** — o usuário conversa com a IA para **criar campanhas, configurar automações, conectar APIs e visualizar dados**, sem menus complexos.

O app deve ser **totalmente interativo por texto ou voz**, com uma interface fluida tipo dashboard SaaS e design **futurista, limpo e responsivo**, padrão Ginkgo.

---

## 🌳 O que é Ginkgo AI Systems

A **Ginkgo AI Systems** é uma holding de produtos e agentes de inteligência artificial.  
Cada produto é um módulo especializado:

- **Ginkgo Leaf** → agentes de atendimento e operação.
- **Ginkgo Wave** → automação de tráfego, marketing e crescimento.
- **Ginkgo Golden Leaf** → marketplace de templates IA.
- **Ginkgo Academy** → treinamento em IA e automação.

Todos compartilham a mesma identidade visual, núcleo técnico e integração via **n8n**, **Supabase**, **Evolution API** e **OpenAI API**.

---

## 💡 Conceito central do Wave

O **Wave** é o cérebro de **crescimento e tráfego** da Ginkgo.  
Seu diferencial: **o usuário não clica, conversa.**  
A IA entende intenções, responde em linguagem natural e executa ações diretas.

Exemplos:

- “Crie uma campanha no Meta Ads para gerar leads de imóveis.”
- “Mostre as campanhas com melhor custo por clique.”
- “Conecte meu WhatsApp e avise novos leads automaticamente.”
- “Crie um anúncio para Instagram Reels com foco em engajamento.”
- “Pause as campanhas com ROI abaixo de 2.”

Tudo ocorre via diálogo no painel central do app, com exibição visual das ações realizadas.

---

## 🧭 Estrutura funcional (via linguagem natural)

### 1) Painel conversacional (núcleo central)

- Campo de texto e microfone → comandos e perguntas.
- A IA responde e executa diretamente.
- Histórico de interações.
- Modo voz (TTS/STT).
- Resultados apresentados em cards e gráficos automáticos.

### 2) IA de automação

- Interpreta comandos e converte em fluxos (ex: “quando novo lead chegar, envie mensagem” → cria trigger n8n).
- Recomenda melhorias automáticas nas campanhas.
- Explica o que está fazendo (“ok, ajustei o orçamento em 15% com base no CPA médio”).

### 3) Campanhas

- Criar, editar e pausar campanhas por voz ou texto.
- Explicações automáticas dos resultados.
- Sugestões de otimização.

### 4) Conteúdo (Nyra integrado)

- Criação de anúncios, legendas e criativos.
- Usuário pede em linguagem natural (“gera 3 variações de texto para vídeo de barbearia moderna”).
- IA retorna cards editáveis.

### 5) Leads e CRM

- Conversa tipo “mostre meus leads quentes da semana”.
- Filtro automático e exibição.
- Envio de mensagens e follow-ups direto por comando.

### 6) Automação e integrações

- Configurações com frases simples:
	- “Conecte minha conta Meta Ads.”
		- “Ative o webhook do Stripe.”
		- “Avise no WhatsApp sempre que alguém preencher o formulário.”

### 7) Relatórios e métricas

- Consultas diretas: “qual campanha teve o melhor CTR ontem?”
- Gráficos e painéis gerados on-the-fly.

---

## 🎨 Design Ginkgo

- Paleta: azul #0EA5E9, branco #FFFFFF, fundo escuro #0B1220, acentos verde-água #A7F3D0.
- Layout SaaS moderno tipo Linear/Notion.
- Tipografia Sora ou Inter.
- Cantos arredondados 2xl, sombras suaves, ícones lineares.
- Estilo “futurismo funcional”: minimalista, luz difusa e efeitos de brilho sutil.

---

## ⚙️ Stack técnica sugerida

- **Frontend:** React (Next.js)
- **Banco:** Supabase
- **Automação:** n8n (via webhooks)
- **IA:** OpenAI API (com funções tool calling)
- **Mensageria:** Evolution API (WhatsApp)
- **Checkout:** Stripe e Hotmart
- **Autenticação:** Supabase Auth (e-mail / magic link)

---

## 🧱 Estrutura de rotas

- `/` → Painel IA (chat central)
- `/insights` → Resumo de métricas
- `/campaigns` → Campanhas (visualização gerada por IA)
- `/leads` → Leads e CRM
- `/content` → Biblioteca de criativos
- `/settings` → Conexões, equipe, planos
- `/billing` → Assinaturas e pagamento

---

## 🧩 Integrações automáticas da Ginkgo

### Ginkgo Leaf

Permite que o Wave envie **tarefas de contato** (“peça para o Brann confirmar o número do cliente”).  
Via webhook JSON com `lead_id` e `task`.

### Nyra

Gera automaticamente criativos, textos e anúncios sob comando natural.  
Entrada: descrição ou objetivo.  
Saída: cards de conteúdo prontos para publicação.

### Golden Leaf

Futuro marketplace.  
Wave deve permitir “instalar” templates de automações e dashboards prontos via um simples comando:

> “Instale o template de automação para e-commerce da Golden Leaf.”

---

## 🤖 IA de comando (core do sistema)

- Baseada em modelo GPT-4 ou 4o-mini.
- Função principal: interpretar texto/voz e chamar as ações certas (API, SQL, webhook).
- Deve explicar cada ação de modo legível.
- Pode manter **contexto de conversa** (“lembre que a campanha imobiliária é prioridade”).

---

## 🧠 Exemplos de uso real

- “Crie uma campanha de tráfego no Instagram para captar leads de corretor.”
- “Analise qual anúncio está gastando mais do que o retorno.”
- “Gere um vídeo curto para o TikTok com base nesse texto.”
- “Envie mensagem para todos os leads de ontem.”
- “Pause todas as campanhas com ROI menor que 2.”

---

## 🔒 Estrutura de segurança

- Permissões por workspace e plano.
- Logs de todas as ações da IA.
- Histórico de configurações executadas via linguagem natural.

---

## 🚀 Onboarding inicial

Fluxo conversacional:

1. IA pergunta nome da empresa.
2. Oferece conectar APIs (“quer conectar sua conta de anúncios agora?”).
3. Sugere primeiro fluxo automatizado (“criei um funil básico com anúncio + WhatsApp + relatório diário”).
4. Mostra tutorial natural em diálogo (“tudo aqui é conversando comigo — tente pedir ‘mostre meus leads’”).

---

## ✅ Critérios de entrega

- Interface conversacional 100% funcional.
- Cada comando de linguagem natural deve **executar ou simular** uma ação real (criar campanha, gerar post, listar leads).
- Dashboard dinâmico com gráficos IA.
- Integrações via Supabase + n8n.
- Suporte a voz opcional (TTS/STT).

---

Deseja que eu agora monte a **estrutura JSON hierárquica de páginas, componentes e funções IA** para colar no editor de fluxos da Lovable (formato “esqueleto funcional”) — ou prefere gerar primeiro o **protótipo visual navegável** com base nesse prompt?