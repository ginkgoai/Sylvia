---
title: "Ginkgo Core - Plataforma de agentes ElevenLabs"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/6916ae59-2fa0-832b-bc30-b4e2126e1278"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 14 de nov. às 1:21

A **Plataforma de Agentes do ElevenLabs** é basicamente o “cérebro operacional” para criar **assistentes de voz autônomos** — igual o BRANN, só que com foco TOTAL em voz, chamadas telefônicas e atendimento falado.

Pensa assim:  
Se o **BRANN** é o *corvo consultor* que conversa por WhatsApp…  
Os **Agentes ElevenLabs** são o *androide telefonista futurista*, que fala, entende, transcreve, responde e age — tudo em voz.

A lógica é:  
**um agente = uma IA completa**, com memória, regras, ferramentas e capacidade de manter diálogos longos.

---

## O que a Plataforma de Agentes faz (na lata)

Aqui está a visão mental, estilo grafo sci-fi:

```markdown
[Entrada de Voz]
      ↓
[Transcrição em tempo real]
      ↓
[Modelo de raciocínio]
      ↓
[Ferramentas / ações externas]
      ↓
[Geração de voz natural]
      ↓
[Resposta falada para o usuário]
```

É isso.  
Ela cria **um fluxo de pensamento + fala**, automático.

---

## O que você consegue construir ali

### 1) Atendentes virtuais por telefone

— Recebem ligações  
— Entendem tudo que a pessoa fala  
— Respondem com voz humana  
— Podem consultar APIs, bancos de dados e fazer ações

Ex.:  
O agente atende:  
“Olá, você gostaria de abrir um chamado? Qual é o problema?"  
A pessoa fala.  
O agente identifica e registra no CRM.

---

### 2) Agentes de voz internos (igual um Jarvis falado)

Você pode criar um assistente que:

- lê documentos
- agenda tarefas
- puxa dados externos
- responde perguntas complexas
- conversa com naturalidade realista

---

### 3) Atendentes híbridos (voz + ferramentas)

Isso é o ouro:

O agente pode acionar **Ferramentas (Tools)**, tipo:

- enviar WhatsApp
- usar n8n
- rodar workflows
- acessar APIs
- consultar sistemas
- enviar documentos
- atualizar registros

Ou seja:  
**É o “subworkflow falado”** — que você já usa com o BRANN, mas via voz.

---

### 4) Automação de suporte e SAC

Perfeito para negócios que ainda dependem de telefone.

- ligações recebidas
- follow-ups automáticos
- pré-atendimento
- triagem de chamados
- coleta de dados

---

## Para que serve na prática no seu ecossistema Ginkgo

Aqui é onde a mágica conecta com o que você está construindo:

### 1) Brann em modo voz (extensão via telefone ou áudio)

O mesmo agente que responde no WhatsApp pode ganhar:

- atendimento telefônico
- retorno de chamadas
- agendamento por voz
- suporte falado
- leitura de documentos com naturalidade

---

### 2) Subworkflows chamados por voz

Exemplo real:

Usuário:  
*"Brann, envia aquele contrato pro meu WhatsApp agora."*

Agente ElevenLabs:  
— aciona subworkflow  
— dispara PDF  
— confirma em voz

Isso já está pronto no ElevenLabs com a aba **Ferramentas**.

---

### 3) Suporte empresarial (Alphie) com voz natural

O Alphie poderia:

- explicar relatórios
- analisar arquivos
- dar insights estratégicos
- narrar briefings ou resumos diários
- atender telefone do escritório em Curitiba

---

### 4) Nyra em “modo narrador”

Para conteúdos:

- narração de Reels
- leitura de roteiros
- narração de posts virais
- vídeos humanizados para clientes

---

## Como funciona tecnicamente

### 1) Transcrição

Usa o modelo ElevenLabs de ASR  
(super preciso e rápido).

### 2) Raciocínio

Conecta com o modelo de linguagem deles ou de terceiros.  
Você pode usar prompts e lógica de comportamento.

### 3) Ações externas

Via “ **Ferramentas** ” (equivalente a Tools na OpenAI):

- webhooks
- APIs
- n8n
- bancos externos

### 4) Voz sintetizada

Usa as vozes de alta fidelidade do ElevenLabs.

Você escolhe velocidade, emoção, estilo, pausa, etc.

---

## O que aparece na sua tela agora?

A ABA  
**Conversas → Histórico**  
fica vazia porque:

- nenhum agente recebeu chamadas
- nenhum teste foi rodado
- nenhuma ferramenta foi acionada em produção

Assim que um agente atender:

- cada mensagem aparece
- cada fala é transcrita
- cada ação é logada
- cada interação vira histórico para auditoria

---

## Cenário prático para você:

**Brann Voz (telefone + WhatsApp + áudio)**

Você poderia usar assim:

1. Usuário liga para o número do Brann
2. O agente ElevenLabs atende
3. Brann identifica intenção
4. Chama subworkflow no n8n
5. Envia respostas por voz
6. Se necessário, envia documentos por WhatsApp

Isso cria a versão **multicanal completa** do Brann.

---

Se quiser, te guio agora a:

1. criar o primeiro agente
2. conectar ferramentas
3. conectar ao n8n
4. liberar chamadas
5. deixar funcionando com voz 100% natural

É só dizer: **“montar agente agora”**.

Então pensando na operação LEAF, brann, nyra e aphie a coexistência dos 3 como um ecossistema contratável e que corresponde e se adapta as 3 necessidades principais de qualquer pequeno e grande negocio, atendimento, social e gestão. faça um projeto escalável e replicavel como saas utilizando n8n, elevenlabs e supabase (aceito recomendação de integrações essenciais que você pensar). modelo de serviço vendavel como plataforma, cliente leigo assina ja configura mesmo entendendo nada de ia e automação -> USA SEM ERROS

Perfeito: LEAF = “tríade” BRANN (atendimento), NYRA (social) e ALPHIE (gestão).  
Vamos montar isso como um SaaS multi-tenant com n8n + Supabase + ElevenLabs, totalmente replicável.

---

## 1\. Visão geral do produto LEAF (como SaaS)

LEAF = plataforma onde o cliente assina e ganha 3 módulos:

1. **BRANN – Atendimento**
	- WhatsApp / Webchat.
		- Entende texto, áudio, imagem, vídeo.
		- Responde com texto, botões, áudios, documentos, etc.
2. **NYRA – Social**
	- Geração e agendamento de conteúdos (posts, stories, Reels).
		- Reciclagem de conteúdos (clipagem, variações).
		- Pode usar ElevenLabs para narração de vídeos.
3. **ALPHIE – Gestão**
	- Resumos de operação, follow-ups, lembretes.
		- Integra CRM/planilha, tarefas (Trello/Notion/Pipefy), agenda (Google Calendar).
		- Gera relatórios e “planos de ação”.

Tudo isso precisa ser:

- **Multi-tenant** (vários clientes na mesma infra).
- **Configuração guiada** (wizard simples).
- **Workflows únicos** reutilizados para todos, só mudando parâmetros.

---

## 2\. Arquitetura macro (blocos)

### Núcleo de dados – Supabase

- Postgres multi-tenant.
- Auth (login painel / portal do cliente).
- Storage (documentos, mídias, configs em JSON).
- Functions (lógica leve de backend, webhooks de checkout).

### Orquestração – n8n

- Workflows principais:
	- `WF_BRANN_CORE` (já é o que você tem no PDF, generalizado).
		- `WF_NYRA_CORE` (social).
		- `WF_ALPHIE_CORE` (gestão).
		- `WF_ONBOARDING` (pós-pagamento).
		- `WF_DOC_INGEST` (ingestão de conhecimento para RAG).
- Tudo parametrizado por `tenant_id`.

### Voz – ElevenLabs

- TTS para:
	- Respostas de voz do BRANN.
		- Narração de vídeos/roteiros da NYRA.
- No futuro: Agents de voz para atendimento telefônico.

### Mensageria / canais

- **Evolution API** para WhatsApp (BRANN).
- APIs Meta / Instagram / Facebook / TikTok (NYRA).
- E-mail (Postmark/Resend) para relatórios do ALPHIE.
- Google Calendar / Notion / Pipefy / Trello via n8n para ALPHIE.

### LLMs

- OpenAI GPT-4o/mini para raciocínio de todos os agentes (já está no fluxo do BRANN).
- Vetores: pgvector no próprio Supabase ou outra indexação.

---

## 3\. Modelo de dados (Supabase) – esqueleto

SQL simplificado (base multi-tenant):

```markdown
-- Quem é o cliente
create table tenants (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  plan text not null, -- leaf_basic, leaf_plus, leaf_futurist
  status text not null default 'active',
  created_at timestamptz default now()
);

-- Usuários do painel
create table users (
  id uuid primary key default gen_random_uuid(),
  tenant_id uuid references tenants(id),
  email text unique not null,
  role text not null default 'owner',
  created_at timestamptz default now()
);

-- Configuração dos 3 agentes por tenant
create table agent_configs (
  id uuid primary key default gen_random_uuid(),
  tenant_id uuid references tenants(id),
  agent_type text not null, -- 'brann' | 'nyra' | 'alphie'
  status text not null default 'enabled',
  settings jsonb not null default '{}'::jsonb, -- prompts, persona, limites
  channels jsonb not null default '{}'::jsonb, -- whatsapp, insta, etc
  created_at timestamptz default now()
);

-- Fonte de conhecimento (RAG)
create table knowledge_sources (
  id uuid primary key default gen_random_uuid(),
  tenant_id uuid references tenants(id),
  agent_type text not null,
  name text,
  kind text, -- 'pdf', 'site', 'faq', 'planilha'
  location text, -- url ou storage path
  status text default 'ready',
  created_at timestamptz default now()
);

-- Logs de mensagens (para debug/analytics)
create table message_logs (
  id bigserial primary key,
  tenant_id uuid references tenants(id),
  agent_type text,
  channel text, -- 'whatsapp', 'instagram', 'email', 'voice'
  external_id text, -- id da msg no canal
  direction text, -- 'in' | 'out'
  payload jsonb,
  created_at timestamptz default now()
);
```

Isso já te dá:

- Multi-tenant real.
- Config central de BRANN/NYRA/ALPHIE por cliente.
- Histórico completo para auditoria e BI.

---

## 4\. n8n – design dos workflows (replicáveis)

### 4.1. BRANN – WF\_BRANN\_CORE

Baseado no PDF:

1. `Webhook (Evolution)` recebe qualquer mensagem.
2. `Function EXTRAIR_MIDIA` normaliza e detecta `mediaType` (audio / video / image / text).
3. `Switch` roteia por tipo.
4. Nós de IA:
	- Áudio → transcrição.
		- Vídeo → transcrição/resumo.
		- Imagem → descritor/OCR.
		- Texto → opcional resumos/saneamento.
5. Tudo vira `text` → `Chat Model BRANN (OpenAI)` com:
	- memória no Postgres (Supabase).
		- ferramentas (sub-workflows, buscas, etc.).
6. `Parser → Switch out.type` → `HTTP Evolution` para enviar:
	- texto, botões, listas, imagens, áudio, `audio_key` (sub-workflow).
7. `Set + HTTP` para gravar log em `message_logs`.

Multi-tenant:

- No início do fluxo:
	- `Function` resolve `tenant_id` a partir do número (`phone`) consultando Supabase (`select tenant_id from agent_configs where channels->>'whatsapp_number' = phone`).
		- `Set` com `tenant_id` em `json`.
- Chat Model BRANN recebe:
	- prompt base global + contexto do `tenant_id` (busca config e conhecimento no Supabase).
- Environment/global vars só para coisas comuns (chaves de API), não para dados de cliente.

---

### 4.2. NYRA – WF\_NYRA\_CORE

Fluxo mínimo para v1:

1. `Webhook` (painel ou WhatsApp) recebe pedido do cliente:  
	“quero 3 posts por semana sobre X”.
2. `Function` identifica `tenant_id` + preferências de conteúdo da `agent_configs` (`settings->'nyra'`).
3. `Chat Model NYRA` gera:
	- ideias + roteiros + legendas (JSON padronizado).
4. `HTTP` grava tudo em `supabase.posts_drafts`.
5. Sub-workflow:
	- Geração de imagem/vídeo (ou integração com outro serviço).
		- Upload para Storage Supabase.
6. Agendamento:
	- n8n + APIs do Instagram/TikTok/YouTube.
		- Tabela `scheduled_posts` no Supabase com `status`.

Cliente leigo só escolhe:

- nicho,
- tom de voz,
- frequência,
- redes.

NYRA cuida do resto.

---

### 4.3. ALPHIE – WF\_ALPHIE\_CORE

MVP simples:

1. Cron job no n8n (a cada X min).
2. Para cada `tenant_id`:
	- ler tarefas abertas (Trello/Notion/Pipefy via API).
		- ler próximos eventos (Google Calendar).
		- ler oportunidades (ex: planilha/CRM).
3. `Chat Model ALPHIE`:
	- sintetiza “estado do dia” (resumo).
		- gera 3–5 ações prioritárias.
4. Saída:
	- mensagem diária no WhatsApp (via Evolution) para o dono.
		- e/ou e-mail de relatório.
5. Logs em `message_logs`.

Depois você expande para:

- responder perguntas,
- abrir cards,
- marcar reuniões, etc.

---

## 5\. Fluxo de Onboarding – cliente leigo (USA SEM ERROS)

Objetivo: **nunca tocar em n8n manualmente por cliente**.

### 5.1. Passo a passo operacional

1. **Checkout**
	- Stripe/Hotmart: produto = plano Leaf (Basic/Plus/Futurist).
		- Webhook → `WF_ONBOARDING`.
2. **Criar tenant**
	- n8n → Supabase:
		```markdown
		POST /rest/v1/tenants
		{ "name": "<Nome da Empresa>", "plan": "<plano>" }
		```
		- cria usuário owner (e-mail do checkout).
		- cria registros padrão em `agent_configs` para:
		- BRANN (WhatsApp),
				- NYRA (social),
				- ALPHIE (gestão).
3. **Enviar link de configuração**
	- e-mail + WhatsApp:  
		“Clique aqui para configurar em 3 passos. Leva 5–10 minutos.”
4. **Wizard (no painel web – pode ser Lovable/Next)**
	1. **Empresa & Persona**
		- nome da marca,
				- nicho,
				- tom de voz (formal / consultivo / descontraído),
				- horário de atendimento.
		2. **Canais**
		- BRANN: número WhatsApp → instrução: “abra o QR agora e escaneie”.
				- NYRA: conectar Instagram (OAuth) → pergunta: quantos posts/semana.
				- ALPHIE: conectar Google Calendar / Trello (OAuth simples).
		3. **Objetivos**
		- prioridade: vendas, suporte, marca, organização.
				- limites: máximo de mensagens/dia, máximos de posts, etc.
5. **Provisionamento automático**
	- Ao concluir o wizard:
		- Atualiza `agent_configs.settings` com JSON final.
				- Ativa flags `status = 'enabled'`.
				- Dispara um teste automático:
			- BRANN envia “Olá, aqui é o seu atendente Leaf. Estou pronto.”
						- NYRA gera 1 conteúdo de teste.
						- ALPHIE manda 1 mini-relatório de boas-vindas.
6. **Modo “à prova de leigo”**
	- Campos obrigatórios validados lado cliente + server.
		- Valores padrão seguros (se não preencher, não quebra).
		- Em qualquer falha de canal:
		- log no `message_logs` + alerta pro humano.
				- resposta fallback: “Seu canal X ainda não está configurado, vamos ajustar.”

---

## 6\. Integrações essenciais recomendadas

- **Evolution API** – backbone de WhatsApp.
- **OpenAI** – raciocínio de todos os agentes.
- **ElevenLabs** – voz (áudios do BRANN, narrações da NYRA, relatórios falados do ALPHIE).
- **Stripe ou Hotmart** – cobrança recorrente + webhooks.
- **Google Calendar / Trello / Notion / Pipefy** – ALPHIE.
- **Supabase Functions** – endpoints rápidos (por ex. “/leaf/config/:tenant\_id” que n8n consome).

---

## 7\. Checklist de “pronto para rodar”

1. **Supabase**
	- Tabelas criadas (tenants, users, agent\_configs, knowledge\_sources, message\_logs).
		- Policies configuradas p/ multi-tenant (RLS por `tenant_id`).
		- Chaves de serviço prontas no n8n.
2. **n8n**
	- `WF_BRANN_CORE` rodando com media router + BRANN + envio Evolution.
		- `WF_NYRA_CORE` gerando e salvando conteúdos.
		- `WF_ALPHIE_CORE` enviando resumos diários para 1 tenant de teste.
		- `WF_ONBOARDING` recebendo webhook do checkout e criando tenants.
3. **Canais**
	- Evolution conectado a um número de teste.
		- Conta de Instagram/TikTok de sandbox conectada.
		- Google Calendar/Trello de teste conectados.
4. **Voz**
	- ElevenLabs configurado com 1 voz padrão da marca.
		- Sub-workflow de áudio plugado no `out.type = "audio"` do BRANN.
5. **Painel**
	- Wizard em 3 passos funcionando.
		- Cliente consegue: assinar → configurar → receber 3 mensagens de teste (BRANN, NYRA, ALPHIE) sem falar “prompt” uma única vez.

---

Se quiser, no próximo passo posso:

- desenhar um fluxo específico em “estilo do PDF do BRANN” para NYRA e ALPHIE,
- ou escrever os `settings` JSON padrão que vão dentro de `agent_configs` para cada um dos três.