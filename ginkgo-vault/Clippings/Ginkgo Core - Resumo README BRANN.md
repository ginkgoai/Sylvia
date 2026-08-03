---
title: "Ginkgo Core - Resumo README BRANN"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/6920c448-0698-8331-bda1-f6799b795bc9"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 21 de nov. às 16:57

README — BRANN (Agente Geral da Ginkgo) BRANN é o agente de IA da Ginkgo que atende pelo WhatsApp, entendendo intenções, respondendo de forma humanizada e registrando tudo na Supabase. Ele usa n8n, Redis e Postgres para orquestrar memória, fluxo e persistência. 🚀 Visão Geral Entrada: WhatsApp via Evolution API Motor: Fluxo no n8n (roteador + memória + core LLM) Cérebro: LLM com prompt mestre e persona BRANN Dados: Supabase (leads, conversas, agendamentos), Redis (memória curta), Postgres (persistência) Saída: Resposta no WhatsApp (texto, botões, mídia) Objetivo: atendimento objetivo, simpático e prático, levando o cliente a três caminhos principais: Assinatura Ginkgo (planos) Agendar Consultoria Falar com Humano 🧩 Arquitetura WhatsApp (Evolution API) │ ▼ \[Webhook IN\] → \[Normalizador\] │ ▼ \[Roteador de Intenção\] │ ├─► \[Core LLM BRANN\] │ │ │ ├─► Supabase (leads, conversas, tickets) │ ├─► Agenda (slots) │ └─► FAQ/Docs │ ▼ \[Persistência + Memória\] │ ▼ \[Send Message Evolution\] → WhatsApp 🎭 Persona do BRANN Tom: objetivo, simpático, direto Estilo: natural, frases curtas, sem jargão Missão: captar intenção → dar resposta clara → oferecer CTA (botões) Regras: Nunca deixar a conversa morrer Confirmar dados essenciais do lead (nome, telefone, origem) Oferecer sempre opções: planos, consultoria ou humano ⚙️ Estrutura de Código /brann /prompts core\_brann.md # persona e FAQ editável /n8n brann\_workflow.json # fluxo n8n exportado /schemas supabase.sql # tabelas leads, conversas, agendamentos /docs README.md # este arquivo 🔑 Variáveis de Ambiente Evolution API EVOLUTION\_BASE\_URL=https://seu-endpoint EVOLUTION\_TOKEN=xxxx EVOLUTION\_INSTANCE=BRANN ADMIN\_WA\_ID=55XXXXXXXXXXX Supabase SUPABASE\_URL=https://xxxx.supabase.co SUPABASE\_ANON\_KEY=... SUPABASE\_SERVICE\_ROLE=... Redis REDIS\_HOST=redis REDIS\_PORT=6379 REDIS\_PASSWORD= n8n N8N\_ENCRYPTION\_KEY=chaveforte32chars N8N\_WEBHOOK\_URL=https://n8n.suaurl.com/webhook 🗄️ Banco (Supabase) Leads: dados básicos (phone, nome, origem, estágio) Conversas: log (in/out, conteúdo, intenção, meta) Preferências: flags (quer plano, consultoria, orçamento) Agendamentos: slots, status, tipo (demo, consultoria) 🤖 Fluxo Passo a Passo Webhook IN: recebe mensagem da Evolution. Normalizador: extrai texto, áudio → texto, mídia. Memória curta: puxa últimas interações no Redis. Roteador: direciona intenção (planos, suporte, humano). Core BRANN: decide resposta + chama ferramentas (Supabase, Agenda, FAQ). Persistência: salva conversa, atualiza lead, registra evento. Saída: envia texto e botões (planos, consultoria, humano). Follow-ups: lembretes via cron n8n. 📝 Contrato de Mensagem Entrada: { "from": "55XXXXXXXXXXX", "text": "Quais planos vocês têm?" } Saída: { "reply\_text": "Temos três planos principais (Básico, Avançado, Futurista) e também On-Demand. Quer ver detalhes ou prefere marcar uma consultoria?", "buttons": \[ {"id": "SEE\_PLANS", "title": "Ver Planos"}, {"id": "BOOK", "title": "Agendar Consultoria"}, {"id": "HUMAN", "title": "Falar com Humano"} \] } ✅ Checklist de Ativação.env configurado Tabelas criadas na Supabase Workflow importado no n8n Webhook Evolution apontado para o n8n Teste inicial: enviar “Oi” → receber saudação + botões Handoff humano funcionando (ADMIN\_WA\_ID recebe alerta) 🔮 Roadmap Integração de pagamentos (checkout direto no plano) RAG com base de conhecimento Ginkgo Dashboard UI em tempo real (leads + conversas)

Segue uma versão mais organizada e “pronta pra repo” do README do BRANN.

---

## BRANN — Agente Geral da Ginkgo (WhatsApp)

BRANN é o agente oficial de atendimento da Ginkgo no WhatsApp.

Ele:

- entende intenções,
- responde de forma humanizada,
- registra leads e conversas na Supabase,
- usa n8n, Redis e Postgres para orquestrar memória, fluxo e persistência.

> Foco: transformar qualquer conversa em oportunidade — assinatura, consultoria ou contato humano.

---

## 🧠 Visão Geral

**Entrada:**  
WhatsApp via Evolution API

**Motor de Orquestração:**  
n8n (webhooks + roteador de intenção + integrações)

**Cérebro (LLM):**  
Modelo + prompt mestre da persona BRANN

**Dados:**

- Supabase (Postgres) → leads, conversas, agendamentos, preferências
- Redis → memória curta (janela recente de mensagens)
- Postgres (via Supabase) → persistência de longo prazo

**Saída:**  
Resposta no WhatsApp (texto, botões, mídia, áudios se habilitado)

**Objetivo principal:**  
Atendimento objetivo, simpático e prático, sempre conduzindo para três caminhos:

1. Assinatura Ginkgo (planos)
2. Agendar Consultoria
3. Falar com Humano

---

## 🧩 Arquitetura WhatsApp (Evolution API → n8n → BRANN)

```markdown
[WhatsApp User]
      │
      ▼
[ Evolution API ]
      │  (Webhook IN)
      ▼
[ n8n - Webhook Node ]
      ▼
[ Normalizador de Mensagem ]
      │ ──► (áudio → texto, extrair texto, metadados)
      ▼
[ Roteador de Intenção ]
      ├─► [ Core LLM BRANN ]
      │     ├─► Supabase (leads, conversas, tickets, preferências)
      │     ├─► Agenda (slots de horários)
      │     └─► FAQ / Base de Docs (RAG, se habilitado)
      │
      └─► [ Handoff Humano / Suporte ]
              └─► ADMIN_WA_ID
      ▼
[ Persistência + Memória ]
      ├─► Redis (memória curta)
      └─► Supabase (log completo)
      ▼
[ Evolution Send Message ]
      ▼
[ WhatsApp User ]
```

Infra recomendada: n8n rodando em VPS (Hostinger + EasyPanel), Supabase como backend gerenciado (Postgres + Auth + Storage) e Redis para fila/memória, integrados em um mesmo ecossistema de automação.

relatorio

---

## 🎭 Persona do BRANN

**Tom:** objetivo, simpático, direto.  
**Estilo:** natural, frases curtas, sem jargão técnico desnecessário.  
**Missão:** entender a intenção → responder claro → oferecer um CTA útil.

**Regras centrais:**

1. Nunca deixar a conversa morrer.
2. Confirmar dados essenciais do lead:
	- Nome
		- Telefone (já vem do WhatsApp, mas confirmar se é o de contato)
		- Origem / como nos encontrou (opcional, mas recomendado)
3. Sempre oferecer opções:
	- Ver/assinar planos
		- Agendar consultoria
		- Falar com humano
4. Manter contexto das últimas mensagens (memória curta), mas registrar tudo na Supabase (memória longa).
5. Ser propositivo: sugerir próximo passo em vez de só responder “sim” ou “não”.

---

## 🧱 Tech Stack

- **Canal:** WhatsApp (Evolution API)
- **Orquestração:** n8n
- **LLM:** OpenAI / outro provedor (configurável via env)
- **Banco:** Supabase (Postgres + Auth + Storage)
- **Memória curta / fila:** Redis
- **Hospedagem:** VPS + Docker (recomendado EasyPanel para gestão visual)

---

## 📁 Estrutura de Código (sugerida)

```markdown
/brann
  /prompts
    core_brann.md        # persona, regras, CTAs e FAQ editável
  /n8n
    brann_workflow.json  # fluxo principal do BRANN (export do n8n)
  /schemas
    supabase.sql         # tabelas: leads, conversas, agendamentos, preferencias
  /docs
    README.md            # este arquivo
```

---

## 🔑 Variáveis de Ambiente (.env)

### Evolution API

```markdown
EVOLUTION_BASE_URL=https://seu-endpoint-evolution.com
EVOLUTION_TOKEN=xxxx
EVOLUTION_INSTANCE=BRANN
ADMIN_WA_ID=55XXXXXXXXXXX  # número do WhatsApp que recebe alertas humanos
```

### Supabase

```markdown
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_ANON_KEY=xxxxxxxxxxxxxxxx
SUPABASE_SERVICE_ROLE=xxxxxxxxxxxxxxxx
SUPABASE_SCHEMA=public
```

### Redis

```markdown
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD= # opcional, mas recomendado em produção
```

### n8n

```markdown
N8N_ENCRYPTION_KEY=chaveforte32chars_no_minimo
N8N_WEBHOOK_URL=https://n8n.suaurl.com/webhook
N8N_BASIC_AUTH_USER=...
N8N_BASIC_AUTH_PASSWORD=...
```

### LLM (exemplo OpenAI)

```markdown
OPENAI_API_KEY=sk-xxxx
OPENAI_MODEL=gpt-4.1-mini
```

---

## 🗄️ Banco (Supabase) — Tabelas principais

### leads

- `id` (uuid, PK)
- `phone` (string, único por lead ativo)
- `nome` (string)
- `origem` (string, ex: “WhatsApp Orgânico”, “Instagram”, “Indicação”)
- `estagio` (enum: `novo`, `em_andamento`, `cliente`, `perdido`)
- `created_at`
- `updated_at`

### conversas

- `id` (uuid, PK)
- `lead_id` (fk → leads.id)
- `direction` (enum: `in`, `out`)
- `conteudo` (jsonb: texto, botões, mídia, intenção detectada)
- `intencao` (string: `planos`, `consultoria`, `suporte`, `outro`)
- `meta` (jsonb: score de intenção, tags, etc.)
- `created_at`

### preferencias

- `id` (uuid, PK)
- `lead_id` (fk)
- `quer_plano` (bool)
- `quer_consultoria` (bool)
- `tipo_plano_interesse` (string: `Basico`, `Avancado`, `Futurista`, `OnDemand`)
- `observacoes` (text)
- `updated_at`

### agendamentos

- `id` (uuid, PK)
- `lead_id` (fk)
- `tipo` (enum: `demo`, `consultoria`, `onboarding`)
- `slot_datetime` (timestamp)
- `status` (enum: `pendente`, `confirmado`, `cancelado`, `realizado`)
- `canal` (string: `WhatsApp`, `Google Meet`, etc.)
- `created_at`
- `updated_at`

---

## 🤖 Fluxo Passo a Passo (n8n)

1. **Webhook IN (Evolution → n8n)**
	- Recebe payload bruto da Evolution API (mensagem de texto, áudio, mídia, botões).
2. **Normalizador**
	- Extrai:
		- `from` (telefone)
				- `text` (mensagem pura)
				- `type` (texto, áudio, botão, mídia)
		- Se for áudio: envia para STT (Speech-to-Text) e retorna `text`.
3. **Memória Curta (Redis)**
	- Busca últimas N mensagens daquela `from` para contextualizar o LLM.
4. **Roteador de Intenção**
	- Envia prompt com:
		- contexto de conversas recentes,
				- mensagem atual,
				- persona do BRANN,
				- objetivos (planos, consultoria, humano).
		- LLM responde com:
		- texto de resposta,
				- intenção (`planos`, `consultoria`, `humano`, `faq`, etc.),
				- necessidade de ferramentas (ex: ler docs, buscar agenda, criar lead).
5. **Core BRANN (Ferramentas)**
	- Se `lead` novo: criar/atualizar na Supabase.
		- Se intenção = `consultoria`: consultar `agendamentos` disponíveis e sugerir horários.
		- Se intenção = `planos`: carregar detalhes dos planos e montar resposta com botões.
		- Se intenção = `humano`: criar ticket + notificar `ADMIN_WA_ID`.
6. **Persistência**
	- Gravar:
		- linha em `conversas` (in/out),
				- atualizar `estagio` do lead,
				- atualizar `preferencias` se detectar interesse em plano/consultoria.
7. **Saída (Evolution Send)**
	- Montar payload com:
		- texto final,
				- botões (até 3 principais: “Ver Planos”, “Agendar Consultoria”, “Falar com Humano”),
				- mídia (opcional, ex: PDF de apresentação).
		- Enviar resposta ao usuário via Evolution.
8. **Follow-ups (cron n8n)**
	- Workflows recorrentes para:
		- lembrar leads que não responderam,
				- confirmar agendamentos,
				- fazer pós-atendimento.

---

## 📝 Contrato de Mensagem

### Exemplo de Entrada (Simplificada)

```markdown
{
  "from": "55XXXXXXXXXXX",
  "text": "Quais planos vocês têm?",
  "type": "text"
}
```

### Exemplo de Saída (Resposta do BRANN)

```markdown
{
  "reply_text": "Temos três planos principais (Básico, Avançado e Futurista), além de uma opção On-Demand. Queres ver um resumo rápido ou já preferes marcar uma consultoria para te explicar tudo direitinho?",
  "buttons": [
    { "id": "SEE_PLANS", "title": "Ver Planos" },
    { "id": "BOOK", "title": "Agendar Consultoria" },
    { "id": "HUMAN", "title": "Falar com Humano" }
  ]
}
```

O n8n converte essa saída em um payload no formato esperado pela Evolution API (template/message com botões).

---

## ✅ Checklist de Ativação

1. **Infra &.env**
	- VPS rodando (n8n + Redis, se necessário).
		- Variáveis de ambiente configuradas (.env do n8n / container).
2. **Supabase**
	- Tabelas criadas a partir de `schemas/supabase.sql`.
		- Chaves (Anon + Service Role) copiadas e configuradas no n8n.
3. **n8n**
	- `brann_workflow.json` importado.
		- Webhook público funcionando (testado via curl/Postman).
		- Crons de follow-up ativados (opcional).
4. **Evolution API**
	- Instância criada (BRANN).
		- Webhook apontado para o endpoint do n8n.
		- Token e base URL configurados nas credenciais do n8n.
5. **Testes**
	- Enviar “Oi” → receber saudação + botões principais.
		- Criar lead novo no Supabase automaticamente.
		- Simular handoff humano → `ADMIN_WA_ID` recebe alerta.

---

## 🔮 Roadmap

- **Integração de pagamentos**
	- Checkout direto de planos (Stripe/Hotmart/Pagamentos nacionais).
		- Atualizar status do lead para “cliente” após pagamento.
- **RAG com Base de Conhecimento Ginkgo**
	- Ingestão de PDFs e docs (produtos, contratos, playbooks).
		- Respostas mais profundas e específicas, sempre com limite de tempo e objetividade.
- **Dashboard UI em tempo real**
	- Painel (Lovable ou outro front) com:
		- leads ativos,
				- status de conversas,
				- funil (visitante → lead → cliente),
				- performance do BRANN (taxa de agendamento, conversão, etc).
- **Áudio com TTS**
	- BRANN respondendo em áudio (voz própria) em casos específicos (pós-venda, follow-up, mensagens especiais).

---

Se quiser, no próximo passo posso montar:

- o `supabase.sql` com `CREATE TABLE` completo das quatro tabelas,
- ou o esqueleto do `brann_workflow.json` (em texto) para você importar direto no n8n.