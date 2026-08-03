---
title: "GKO - Vercel e Ginkgo integração"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69190b5b-7c44-8325-8a6f-60ad039e2158"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
Boa, agora é a pergunta certa:  
“Vercel, Manus, Lovable… é tudo a mesma coisa ou cada uma tem seu slot no tabuleiro?”

Resposta curta:  
**não tem nada a ver uma com a outra**.  
Cada uma entra em uma camada diferente do ecossistema Ginkgo/Leaf.

Vou separar como se fosse **camadas de um mecha gigante**:

---

## 1\. Vercel = Onde o usuário enxerga e clica (camada de interface + edge)

Você usa a Vercel para:

- Sites, landings, painéis do Leaf/Brann/Nyra/Alphie
- Dashboards de cliente (configurações, métricas, logs, billing)
- Micro-APIs e serverless/edge functions leves
- Webhooks rápidos (Stripe, Supabase, Evolution API, etc.)

Ela é a **infraestrutura de deploy** da parte visual + algumas funções leves de back-end.  
Não gera código sozinha, não cria agente, não conversa com ninguém.  
Ela só **roda** o que você construiu.

Pensa: Vercel = “onde o seu SaaS vive e responde.”

---

## 2\. Lovable = Fábrica de código (copiloto de desenvolvimento)

Lovable entra em outro ponto do mapa:

- Te ajuda a **criar** o front-end que vai ser deployado na Vercel
- Monta painéis em Next.js/React, APIs, componentes, CRUD básico etc.
- É o “dev assistente” que acelera você a ter um MVP bonitinho e funcional

Fluxo típico:

1. Você usa **Lovable** para gerar o app (dashboard Leaf, painel de cliente, etc.)
2. Quando estiver OK → conecta com GitHub
3. **Vercel** puxa do GitHub → builda → deploya

Ou seja:

- Lovable = **constrói a nave**
- Vercel = **bota a nave para voar**

---

## 3\. Manus (Manus.im) = Camada de bot/conversação pronta

Manus é outra coisa ainda:  
Ela entra como **plataforma de chatbots/assistentes** pronta para uso, normalmente:

- Para embutir chat em site (widget)
- Para criar assistentes conversacionais rapidamente
- Pode atuar como canal de atendimento em vez de você montar tudo na unha

Ela encaixa:

- No site que está hospedado na **Vercel** (widget de chat incorporado)
- Como uma camada de interface conversacional ligada à sua stack (n8n, Supabase, etc.)
- Em cenários onde você quer um chat rápido e enxuto, sem reinventar tudo

Você pode ter, por exemplo:

- Frontend do Leaf/Brann rodando na Vercel
- Um widget do Manus embutido nesse frontend
- O Manus falando com APIs/n8n que você controla

Mas:  
Manus não substitui Vercel.  
Nem Vercel substitui Manus.  
São peças diferentes do ecossistema.

---

## Pensando em ecossistema Ginkgo/Leaf (prático):

### Se você quer:

1. **Site + painel + onboarding + página pública**  
	→ Vercel (deploy) + Lovable (ajudar a construir)
2. **Agente conversando dentro do site com chat bolado**  
	→ Widget (Manus ou outro) embedado no site hospedado na Vercel  
	→ Conectado com n8n, Supabase, ElevenLabs, etc.
3. **Plataforma SaaS vendável que cliente configura sozinho**
	- Lovable: para te ajudar a criar o painel/admin
		- Vercel: para hospedar tudo (painéis, docs, landings)
		- n8n + Supabase: cérebro e automação por trás
		- Manus (opcional): como “interface de chat” simples se você não quiser construir tudo do zero via WhatsApp/Brann

---

## Regra mental rápida para não se perder

- **Vercel** → Onde o app vive e é servido para o mundo
- **Lovable** → Quem te ajuda a construir o app (front/back) mais rápido
- **Manus** → Quem coloca uma “boca de chat” pronta, plugável, no seu app/site

Eles não competem.  
Eles se somam, em camadas diferentes.

---

Se quiser, no próximo passo eu posso montar um **diagrama da stack Leaf/Ginkgo** com esses 3 bem posicionados:

- Usuário → Site (Vercel)
- Chat no site (Manus ou widget custom)
- Painel de config (Lovable + Vercel)
- Orquestração e IA (n8n, Supabase, Evolution, etc.)

sáb., 15 de nov. às 21:31

Então me ajude a visualizar com clareza e detalhes. Ginkgo Leaf um SaaS, uma plataforma intuitiva que qualquer pessoa consegue entrar e assinar sua automação de agentes de ia, 3 níveis, ATENDIMENTO (Um atendente vendedor humanizado, capaz de entender qualquer contexto e se adaptar ao negócio da pessoa, manda áudio e conversa normalmente, ele é integrado ao WhatsApp), SOCIAL (Uma plataforma conversacional de ia que cria, clona, sugere, e até posta automaticamente nas redes sociais vinculadas pelo usuário posts, vídeos virais tudo voltado para o nicho e negócio pessoal configurado no onboarding de assinatura, e terceiro assistência (agente gestor, fazendo integração e organização de CRM, chatwoot e funções de um assistente geral.) Tudo isso com plataformas front visuais, futuristas, intuitivas e fáceis tudo voltado a temática logos e padrão Ginkgo

Vamos desenhar isso como se fosse o “painel de comando” da Ginkgo Leaf.

Vou dividir em 3 visões:

1. Visão do cliente leigo (o que ele vê e sente)
2. Estrutura de telas da plataforma (como fica o front futurista)
3. Arquitetura por baixo (onde entram Vercel, n8n, Supabase, WhatsApp, redes sociais, Chatwoot etc.)

---

## 1\. Visão do cliente leigo: a jornada Leaf

Pensa na jornada assim:

1. Ele cai numa **landing da Leaf**
	- Visual Ginkgo (cores, logos, corvo, folha etc.)
		- Explicação simples:
		- Nível 1: Atendimento
				- Nível 2: Social
				- Nível 3: Assistência
		- Ele escolhe o plano e clica em “Começar”.
2. Ele cria conta e entra no **Onboarding Guiado**  
	Um wizard em 3 etapas, sempre com visual futurista, textos simples e exemplo na tela:
	- Etapa 1 – Sobre o negócio
		- Nome do negócio
				- Nicho (imobiliária, clínica, loja online, infoproduto…)
				- Público-alvo
				- Oferta principal
		- Etapa 2 – Canais e integrações
		- Conectar WhatsApp (via QR / Evolution API)
				- Conectar redes sociais (Meta/Instagram, TikTok, etc.) – se tiver plano Social
				- Conectar CRM / Chatwoot (ou usar o interno Leaf) – se tiver Assistência
		- Etapa 3 – Personalização dos agentes
		- Atendimento: nome do atendente, tom de voz, como trata o cliente
				- Social: voz da marca, temas, frequência de posts
				- Assistência: tipo de organização (vendas, serviços, atendimentos recorrentes)
3. Ao concluir, ele cai no **Dashboard Leaf**:  
	Uma tela com 3 grandes cards, cada um representando um “módulo/agente”:
	- Card 1 – Atendimento (ATIVADO / PAUSADO)
		- Card 2 – Social (ATIVADO / PAUSADO)
		- Card 3 – Assistência (ATIVADO / PAUSADO)
	Cada card mostra mini-métricas:
	- Atendimento: leads do dia, conversas, taxa de resposta
		- Social: posts publicados, alcance estimado, próximos posts agendados
		- Assistência: tarefas abertas, alertas, integrações funcionando ou com erro
	Daqui ele consegue clicar em “Ver detalhes” e entrar em cada módulo.

---

## 2\. Estrutura de telas da plataforma Leaf

### 2.1. Dashboard principal (home da Leaf)

Menu lateral:

- Dashboard
- Atendimento
- Social
- Assistência
- Conteúdos & Base de conhecimento
- Integrações
- Configurações (conta, billing, equipe)

No centro, aquele painel com visão geral dos 3 agentes.

---

### 2.2. Módulo Atendimento (Agente vendedor no WhatsApp)

Objetivo: **atendente-vendedor humanizado no WhatsApp**, manda áudio, responde, entende o negócio.

Telas internas:

1. **Visão Geral**
	- Status do agente (online/offline)
		- Gráfico de conversas por dia
		- Leads captados
		- Vendas/fechamentos (se integrado ao CRM)
2. **Configuração de Persona**
	- Nome do atendente (João, Ana, Brann, etc.)
		- Tom de voz (formal, casual, engraçado, técnico)
		- Frases de saudação, despedida, reengajamento
		- Idiomas que ele usa
3. **Regras de Atendimento**
	- Horários em que o agente responde sozinho
		- Quando chamar humano (palavras-chave, situações críticas)
		- Tipos de fluxo: pré-venda, pós-venda, suporte, agendamento
4. **Treinamento**
	- Upload de PDFs, docs, textos
		- FAQ do negócio
		- Produtos/serviços (tabela simples): nome, preço, descrição
		- Tudo isso vai para a base vetorial do agente
5. **Conversas & Monitoramento**
	- Lista de conversas recentes
		- Visualização de histórico por contato
		- Botão “assumir conversa” (handoff humano)

Front: interface limpa, cards, gráficos, botões grandes e poucos campos por tela.

---

### 2.3. Módulo Social (Plataforma de IA para conteúdo e posts automáticos)

Objetivo: **Nyra as a Service** – cria, clona, sugere e posta.

Telas internas:

1. **Visão Geral**
	- Calendário com posts agendados
		- Posts publicados recentemente
		- Métricas básicas (impressões, cliques, engajamento – quando possível)
2. **Conexões de Redes**
	- Conectar/gerenciar: Instagram, TikTok, Facebook, LinkedIn, X…
		- Ver status de autenticação
		- Botão “reautorizar” quando token expira
3. **Configuração de Marca**
	- Nicho principal
		- Temas de conteúdo
		- Tipo de conteúdo desejado (educativo, prova social, bastidores, ofertas etc.)
		- Estilo visual (cores, referências, vibe)
4. **Geração de Conteúdo**
	- Tela com:
		- Campo “ideia geral”
				- Botão “Gerar 10 ideias de posts”
				- Lista de posts sugeridos com:
			- Legenda
						- Sugestão de imagem/vídeo
						- CTA
						- Hashtags
		- Botão “Aprovar & agendar” ou “Editar antes de postar”
5. **Biblioteca de Mídia**
	- Imagens, vídeos e templates mais usados
		- Possível categorização por campanha/tema

---

### 2.4. Módulo Assistência (Agente gestor – CRM, Chatwoot, rotinas)

Objetivo: **Alphie/Alfred** – o cérebro organizador.

Telas internas:

1. **Painel de Operações**
	- Leads por etapa do funil
		- Tarefas abertas (follow-up, propostas, contratos)
		- Alertas (integração falhou, fila de mensagens, etc.)
2. **Pipelines & CRM**
	- Kanban simples:
		- Novo lead → Em conversa → Proposta enviada → Cliente → Pós-venda
		- Cada card com: contato, origem, valor estimado, dono responsável
3. **Integrações**
	- Chatwoot ligado/desligado
		- Pipefy/Notion/Trello (se você quiser usar)
		- Ferramentas externas (Google Sheets, ERP etc.)
4. **Regras & Automação**
	- “Quando lead entra em etapa X → faça Y”
		- Ex.: entrou em “Proposta enviada” → mandar lembrete 48h depois
				- Entrou em “Cliente” → gerar contrato + mandar mensagem de boas-vindas
5. **Relatórios**
	- Relatório semanal automático (pode ir pro WhatsApp do dono)
		- Resumo: quantos leads, quantas vendas, onde está travando

---

## 3\. Arquitetura por baixo: onde cada peça entra

Agora o “raio-x” da máquina:

```markdown
Mermaid
```

Em camadas:

### 3.1. Camada Visual (Front – Vercel + Lovable)

- Você desenha o painel e landing da Leaf em **Next.js/React**
- Pode usar **Lovable** para acelerar a criação desse front
- Esse código vai para o GitHub
- A **Vercel** faz o deploy:
	- Landing
		- Dashboard Leaf
		- Rotas /dashboard, /onboarding, /billing
		- Edge functions para algumas chamadas rápidas

### 3.2. Camada de Lógica & Orquestração (n8n)

- Cada módulo é um conjunto de workflows:
	- Atendimento:
		- Webhook de mensagem do WhatsApp (Evolution)
				- Chamada ao modelo (LLM) com contexto do negócio (Supabase + RAG)
				- Lógica de resposta, áudio (ElevenLabs), etc.
				- Registro no CRM/Chatwoot
		- Social:
		- Pipelines para gerar ideias de posts
				- Geração de copy + assets
				- Agendamento e postagem via API das redes
				- Leitura de métricas quando possível
		- Assistência:
		- Sync com CRM/Chatwoot
				- Gatilhos de mudança de etapa
				- Geração de relatórios
				- Notificações ao dono (WhatsApp/Email)
- O front (Vercel) fala com o n8n via APIs seguras.

### 3.3. Camada de Dados (Supabase)

- Auth: login, usuários, equipe
- Dados do negócio: configurações do cliente Leaf
- Logs básicos (opcional)
- Base vetorial para conhecimento dos agentes (docs, FAQs etc.)

### 3.4. Canais externos

- **WhatsApp** → Evolution API conectada ao n8n
- **Redes Sociais** → APIs (Meta, TikTok, etc.)
- **Chatwoot** → central de atendimento unificada
- **ElevenLabs** → geração de áudio para o atendente

---

## Mental model final

Ginkgo Leaf é:

- Um **painel futurista (Vercel)**
- Com 3 “portais”:
	- Atendimento (WhatsApp)
		- Social (Redes)
		- Assistência (Operações)
- Cada portal é só a “cara bonita” de um conjunto de **workflows n8n + dados Supabase + canais externos**.

Assinou → respondeu um onboarding guiado → conectou canais → os 3 agentes entram em operação quase sozinhos.

Se quiser no próximo passo, eu monto:

- Estrutura de tabelas no Supabase para Leaf
- Ou o mapa de rotas (URL) do front `/onboarding`, `/dashboard/social`, `/agents/support` etc.

Monte a estrutura completa, todos os passos, do zero ao deploy em etapas passo a passo especificado.

Vou montar isso como um blueprint completo de fábrica de SaaS: do “nada” até o Leaf rodando em produção com os 3 agentes.

Pensa em FASES. Se você seguir de cima pra baixo, sai um MVP sólido.

---

## FASE 0 – Decisões de stack (travando a base)

**Infra principal:**

- Frontend + painel: **Next.js** + React
- Deploy frontend + APIs leves: **Vercel**
- Auth + banco + vetor: **Supabase**
- Orquestração/agentes: **n8n** (na sua VPS)
- WhatsApp: **Evolution API**
- Social: APIs oficiais (Meta/IG, TikTok, etc.)
- Atendimento centralizado: **Chatwoot**
- Áudio: **ElevenLabs** (pode vir depois)
- Pagamento: **Stripe** (ou outro gateway BR, mas vamos supor Stripe)

Opcional para acelerar:

- **Lovable**: para scaffolding do app (painel + telas)
- **Manus**: widget de chat no site (se quiser algo web além do WhatsApp)

---

## FASE 1 – Preparar terreno (contas, projetos, repositório)

1. Criar repositório no GitHub:
	- Nome sugerido: `ginkgo-leaf-app`
		- Monorepo opcional, mas para agora: 1 repo = front + APIs.
2. Criar projeto no **Supabase**:
	- Projeto: `ginkgo-leaf`
		- Ativar:
		- Auth (e-mail + senha; futuramente OAuth)
				- Database (Postgres)
				- Storage (para uploads se quiser)
3. Garantir **n8n** rodando na VPS:
	- URL pública: `https://automations.ginkgo.../n8n` (exemplo)
		- Com:
		- Webhook URLs acessíveis publicamente
				- Credenciais para Evolution, Supabase, Chatwoot, etc.
4. Criar conta na **Vercel**:
	- Conectar com GitHub
		- Preparar espaço para o app `ginkgo-leaf-app`
5. Criar conta no **Stripe**:
	- Configurar produtos e planos Leaf:
		- `leaf-attendance`
				- `leaf-social`
				- `leaf-assistance`
				- Ou 3 planos combinados
6. Configurar **Evolution API**:
	- Instância criada e testada
		- Saber:
		- Base URL
				- API key/token
				- Número de WhatsApp vinculado
7. Configurar **Chatwoot** (pode ser em outro servidor ou SaaS):
	- Criar inbox específica para cada cliente ou usar tags/attributes
		- Gerar API key

---

## FASE 2 – Modelagem do produto Leaf (lógica de negócios)

Definir claramente:

1. **Planos**:
	- Plano 1: **Atendimento**
		- Plano 2: **Atendimento + Social**
		- Plano 3: **Atendimento + Social + Assistência**
2. **Limites**:
	- Quantos WhatsApps por conta? (1 no começo)
		- Quantos perfis de rede social?
		- Quantos agentes (user seats) internos?
3. **Onboarding Único**:
	- 3 etapas:
		1. Dados do negócio
				2. Conexões (WhatsApp, redes, CRM/Chatwoot)
				3. Personalização dos agentes

Tudo isso precisa ser refletido no banco.

---

## FASE 3 – Modelagem do banco (Supabase)

### 3.1. Tabelas principais

Sugestão de esquema simples:

```markdown
users (já vem do Supabase auth)
- id
- email
- full_name

organizations
- id
- owner_user_id (FK -> users.id)
- name
- niche
- created_at

subscriptions
- id
- organization_id (FK)
- stripe_customer_id
- stripe_subscription_id
- plan_tier (enum: 'ATTENDANCE' | 'ATTENDANCE_SOCIAL' | 'FULL')
- status (active, trialing, canceled)
- created_at

business_profiles
- id
- organization_id (FK)
- business_name
- niche
- offer_main
- target_audience
- language
- timezone

channels_whatsapp
- id
- organization_id (FK)
- evo_instance_url
- evo_instance_token
- phone_number
- status (connected, pending, error)

channels_social
- id
- organization_id (FK)
- platform (instagram, tiktok, facebook, linkedin, x)
- handle
- access_token
- refresh_token
- status

integrations_chatwoot
- id
- organization_id (FK)
- chatwoot_base_url
- api_token
- inbox_id

agent_settings_attendance
- id
- organization_id (FK)
- agent_name
- tone (formal, casual, friendly, humorous)
- greeting_message
- handoff_rules (jsonb)
- working_hours (jsonb)

agent_settings_social
- id
- organization_id (FK)
- brand_voice_description
- content_pillars (jsonb: lista de temas)
- post_frequency (jsonb)
- auto_post_enabled (boolean)

agent_settings_assistance
- id
- organization_id (FK)
- crm_type (internal, chatwoot, pipefy, notion, trello)
- alert_channels (jsonb: whatsapp/email)
- reporting_frequency (daily, weekly)

crm_leads
- id
- organization_id
- name
- phone
- email
- source (whatsapp, instagram, landing)
- stage (new, in_conversation, proposal, won, lost)
- value
- assigned_to_user_id (nullable)
- created_at
- updated_at
```

### 3.2. Base vetorial (RAG dos agentes)

Você pode usar:

- Tabela `documents` + `documents_embeddings` no Supabase (ou pgvector):
	- `documents`:
		- id, organization\_id, title, content, type (faq, product, policy), created\_at
		- `document_embeddings`:
		- document\_id, embedding (vector), metadata (jsonb)

Isso vai alimentar o “cérebro” dos agentes.

---

## FASE 4 – Construção do frontend (Next.js + Vercel)

### 4.1. Criar app base

No seu repo:

```markdown
npx create-next-app@latest ginkgo-leaf-app
# Typescript, App Router, Tailwind (recomendado)
```

Instalar:

- `@supabase/supabase-js`
- `@stripe/stripe-js`
- `@headlessui/react` (se quiser UI)
- `lucide-react` ou similar para ícones

### 4.2. Estrutura de rotas

Sugerido (App Router):

- `/` → Landing pública
- `/auth/sign-in`
- `/auth/sign-up`
- `/onboarding` → wizard inicial
- `/dashboard` → visão geral
- `/dashboard/attendance`
- `/dashboard/social`
- `/dashboard/assistance`
- `/integrations`
- `/billing`

### 4.3. Layout Ginkgo futurista

- Navbar com logo Ginkgo Leaf
- Sidebar nas rotas `/dashboard/*`
- Cards grandes pra cada agente
- Hints e tooltips explicando cada campo (pensando no leigo)

### 4.4. Onboarding UI

Um wizard em 3 steps:

1. Dados do negócio:
	- Form conecta direto em `business_profiles`
2. Conexões:
	- Botões:
		- “Conectar WhatsApp” → chama backend que gera link/QR da Evolution
				- “Conectar Instagram” → redireciona para OAuth da Meta
3. Agentes:
	- Form de persona do atendente
		- Form de voz da marca social
		- Preferências de relatórios do assistente

---

## FASE 5 – Backend: APIs e Webhooks (Vercel + n8n)

### 5.1. API routes no Next/Vercel

Criar handlers para:

- `POST /api/onboarding/complete`
	- Salva tudo no Supabase
		- Cria registros base de config
		- Dispara call para n8n configurar workflows do cliente (opcional)
- `POST /api/stripe/webhook`
	- Recebe eventos de pagamento
		- Atualiza `subscriptions` no Supabase
- `POST /api/integrations/evolution/callback`
	- (Opcional) se Evolution tiver callback, registrar conexão concluída
- `POST /api/social/oauth/callback`
	- Salva `channels_social`

Essa camada é o “tradutor” entre front ↔ Supabase ↔ n8n.

### 5.2. Conexão front ↔ n8n

No n8n, você cria webhooks como:

- `https://seu-n8n/webhook/leaf/attendance/{organization_id}/config`
- `https://seu-n8n/webhook/leaf/social/{organization_id}/config`

Do lado do Next.js, você chama esses endpoints quando:

- Onboarding termina
- Configs de agentes são alteradas

---

## FASE 6 – Workflows n8n por módulo

### 6.1. Módulo Atendimento (WhatsApp + BRANN)

Workflow principal: `leaf-attendance-router`

Fluxo:

1. **Webhook Evolution**:
	- Trigger: mensagem recebida no WhatsApp
		- Entrada: `phone`, `message`, `audio?`, metadata
2. **Buscar contexto do cliente:**
	- Node HTTP Request → Supabase (API REST ou RPC)
		- Puxa:
		- `business_profiles`
				- `agent_settings_attendance`
				- Docs relevantes (RAG) se quiser enriquecer prompt
3. **Se áudio**:
	- Enviar para Speech-to-Text (Whisper/ElevenLabs/Kokoro)
		- Resultado vira `user_message`
4. **Chamar LLM (BRANN)**:
	- Node OpenAI/LLM
		- Prompt inclui:
		- Persona do agente
				- Contexto do negócio
				- Histórico recente da conversa (pode vir do Chatwoot ou Supabase)
5. **Opcional: transformar resposta em áudio**:
	- ElevenLabs: texto → áudio
		- Enviar via Evolution API (mensagem de áudio)
6. **Registro no CRM**:
	- Criar/atualizar lead em `crm_leads`
		- Adicionar nota no Chatwoot (via API)
7. **Enviar resposta**:
	- Node HTTP Request → Evolution (enviar texto e/ou áudio)

---

### 6.2. Módulo Social (Nyra-as-a-Service)

Workflows:

1. `leaf-social-ideas-generator`
	- Trigger: HTTP (chamado pelo front quando cliente clica “Gerar ideias”)
		- Pega:
		- `business_profiles`
				- `agent_settings_social`
		- LLM gera lista de ideias → devolve pro front
2. `leaf-social-post-creator`
	- Trigger: HTTP (quando cliente aprova um post)
		- Gera:
		- Legenda refinada
				- Sugestão de imagem (prompt para IA de imagem)
		- Opcional: já chama IA de imagem (Runway/MJ/etc.)
3. `leaf-social-scheduler`
	- Trigger: Cron (de hora em hora, por exemplo)
		- Busca posts agendados em tabela `scheduled_posts`
		- Para cada:
		- Publica via API da rede social correspondente
				- Marca como publicado
				- Salva resultado (link, métricas iniciais)

---

### 6.3. Módulo Assistência (Alphie/Alfred)

Workflows:

1. `leaf-assistance-crm-sync`
	- Trigger: Webhooks de Chatwoot, WhatsApp, etc.
		- Mantém `crm_leads` atualizado
2. `leaf-assistance-alerts`
	- Trigger: Cron (a cada X minutos)
		- Regras:
		- Lead parado há X dias → manda mensagem pro dono no WhatsApp
				- Muitas conversas sem resposta → alerta
3. `leaf-assistance-reports`
	- Trigger: Cron (diário/semanal)
		- Calcula:
		- Leads novos
				- Conversões
				- Atendimentos
				- Posts publicados
		- Gera resumo com LLM (texto bonitinho)
		- Envia:
		- WhatsApp do dono
				- E-mail opcional

---

## FASE 7 – Deploy e ambientes

### 7.1. Ambientes

- **Dev**:
	- Supabase dev
		- Projeto Vercel dev
		- n8n dev (pode ser só um fluxo separado)
- **Prod**:
	- Supabase prod
		- Vercel prod (conectado ao branch `main`)
		- n8n prod (workflows finalizados)

### 7.2. Variáveis de ambiente (Vercel)

Configurar em Vercel:

- `NEXT_PUBLIC_SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY` (no backend apenas)
- `STRIPE_PUBLIC_KEY`
- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`
- `N8N_BASE_URL`
- `N8N_WEBHOOK_TOKEN` (se usar autenticação)
- Outros que forem necessários

---

## FASE 8 – Roteiro de teste fim-a-fim (MVP)

1. Criar conta de teste na Leaf (signup)
2. Fazer onboarding completo:
	- Preencher dados do negócio
		- Pular integrações se quiser (mas testar depois)
		- Configurar nome do atendente e voz da marca
3. Conectar WhatsApp (Evolution) e mandar mensagem:
	- Ver se:
		- Mensagem chega no n8n
				- Agente responde
				- Lead é criado no CRM
				- Chatwoot recebe log (se configurado)
4. Testar Social:
	- Conectar pelo menos uma rede (ex.: Instagram)
		- Gerar 5 ideias de posts
		- Aprovar 1
		- Agendar e ver se é publicado
5. Testar Assistência:
	- Criar leads falsos em várias etapas
		- Rodar workflow de relatório manualmente
		- Ver relatório chegando no seu WhatsApp/e-mail
6. Testar Stripe:
	- Criar assinatura de teste
		- Ver atualização de `subscriptions` no Supabase

---

Se você quiser o próximo nível, posso:

- Detalhar o **SQL/Tabela por tabela** do Supabase
- Ou montar a **árvore de pastas** do projeto Next (`app/`, `components/`, `lib/`, etc.) para você já ir criando no VS Code.