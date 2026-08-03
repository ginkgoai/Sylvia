---
title: "Ginkgo Core - Onboarding automático Leaf"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/68fb075d-ffa8-832d-92e0-9e998ccfc157"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 24 de out. às 1:58

Me ajude a visualizar como vai ser feito o onboarding automático do cliente que assina o Leaf, como aplicaremos um Brann, Nyra e Alphie quase que imediatamente, rapidez, como assinar Netflix.

Onboarding “estilo Netflix” do Leaf: compra → provisionamento → ativação. Sem fricção. Em minutos.

## Fluxo de ponta a ponta

1. **Compra**
- Checkout (Stripe/Hotmart) com 2 campos extras: WhatsApp e domínio da empresa.
- Webhook `checkout.completed` → n8n “Leaf-Provision”.
2. **Provisionamento**
- n8n cria `tenant` no Supabase: `tenants`, `users`, `agents`, `pipelines`, `secrets`.
- Gera credenciais e tokens (Evolution API, Supabase, Storage, Logs).
- Sobe 3 workflows base por tenant: `Brann-Inbox`, `Nyra-Social`, `Alphie-Backoffice`.
- Cria sessão WhatsApp via Evolution API e valida QR.
3. **Ativação guiada no WhatsApp (Brann)**
- Mensagem 0: “Bem-vindo ao Leaf. Vamos ligar tudo agora.”
- Perguntas rápidas: setor, objetivo principal, fontes de conteúdo, horários de atendimento.
- Brann salva respostas em `tenant_settings` e ativa os fluxos.
4. **Conteúdo e canais (Nyra)**
- Conecta Instagram/TikTok/LinkedIn via OAuth link único.
- Nyra puxa 3 referências do cliente (site, drive, posts) e gera 7 rascunhos.
- Agenda a primeira semana e envia preview no WhatsApp para 1-tap “Aprovar/Editar/Descartar”.
5. **Operação e métricas (Alphie)**
- Liga painel do tenant: tickets, SLAs, vendas, posts aprovados, custos de API.
- Integra planilha/CRM do cliente. Importa contatos. Ativa lembretes operacionais.

## Workflows n8n mínimos (por tenant)

- **Leaf-Provision (Webhook)**
	- Trigger: `POST /webhooks/leaf/provision`
		- Steps: validar pagamento → criar registros no Supabase → gerar `.env` do tenant → criar filas Redis → disparar “Send-Welcome”.
- **Send-Welcome (HTTP → Evolution API)**
	- Mensagem WhatsApp com link mágico de onboarding e QR.
- **Brann-Inbox (Webhook Evolution)**
	- Classifica intenção (FAQ, lead, suporte).
		- RAG com base do cliente (folder no Storage “/kb/\<tenant>”).
		- Handoff humano se `confidence < 0.6` ou palavra-chave.
- **Nyra-Social (Cron + OAuth)**
	- Gera pauta semanal + 7 criativos.
		- Fila de aprovação no WhatsApp.
		- Posta e coleta métricas.
- **Alphie-Backoffice (Cron + DB)**
	- Consolida métricas, custos, erros.
		- Envia relatório diário 08:00.

## Estrutura de dados essencial (Supabase)

- `tenants(id, name, whatsapp, domain, plan, status)`
- `secrets(tenant_id, key, value)` → Evolution, IG, OpenAI/Claude, ElevenLabs, etc.
- `kb_docs(tenant_id, url, vector_id)`
- `campaigns(tenant_id, platform, status, scheduled_at)`
- `tickets(tenant_id, channel, subject, status, assignee)`

## Variáveis de ambiente por tenant

```markdown
TENANT_ID=
EVOLUTION_API_URL=
EVOLUTION_INSTANCE=
EVOLUTION_TOKEN=
SUPABASE_URL=
SUPABASE_ANON=
SUPABASE_SERVICE=
OPENAI_API_KEY=   # ou Claude
ELEVENLABS_API_KEY=
SOCIAL_INSTAGRAM_OAUTH_CLIENT_ID=
SOCIAL_INSTAGRAM_OAUTH_SECRET=
```

## Webhook de compra → exemplo de payload

```markdown
{
  "event": "checkout.completed",
  "tenant": {
    "company": "Acme Odonto",
    "whatsapp": "+55XXXXXXXXXXX",
    "domain": "acme.com.br",
    "plan": "Leaf-Básico"
  },
  "billing": {
    "provider": "stripe",
    "subscription_id": "sub_123",
    "email": "ops@acme.com.br"
  }
}
```

## Script inicial do Brann (WhatsApp)

1. “Escolha foco inicial: Leads, Suporte ou Conteúdo.”
2. “Horário de atendimento humano?”
3. “Envie 3 links que representem sua marca.”
4. Botões: **Ativar Brann**, **Ativar Nyra**, **Ativar Alphie**.
5. Confirmou → Brann envia “pronto” + teste de respostas + CTA para aprovar a pauta da Nyra.

## Experiência do usuário

- **Assinou** → WhatsApp chega em instantes com link/QR.
- **Responde 4 passos** → Brann assume atendimento.
- **Vê 7 posts** sugeridos → aprova com um toque.
- **Recebe painel** do Alphie com métricas e status.

## Fail-safes

- Se QR não for lido em 15 min: fallback para onboarding web.
- Se OAuth social falhar: Nyra opera em “rascunho por WhatsApp”.
- Se RAG vazio: Brann cai para FAQ padrão e coleta conteúdo.

## Cancelamento/upgrade

- Comando WhatsApp: “cancelar” ou “upgrade”.
- n8n “Leaf-Billing” pausa ou troca plano e desativa agentes.

## Entregáveis prontos para você

- 3 n8n templates versionados por tenant.
- SQL de criação de tabelas e políticas RLS.
- Mensagens padrão do Brann e botões de aprovação da Nyra.
- Painel Alphie com 4 widgets: Leads, Tempo de resposta, Calendário de posts, Custos.

Quer que eu gere:

1. os JSONs dos 3 workflows n8n,
2. o SQL do Supabase com RLS,
3. os textos prontos do Brann/Nyra para colar?