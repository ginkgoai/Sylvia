---
title: "Ginkgo Core - Onboarding Leaf cliente"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/68fa61eb-3fac-8332-8ad7-fc6d3b5bf45d"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
qui., 23 de out. às 14:12

Perfeito — com base no **relatório** e no ecossistema que tu já estruturou (Lovable + Supabase + n8n + Notion + Hostinger/EasyPanel), o **onboarding do cliente Leaf** pode ser desenhado como uma jornada fluida e quase “autoinstalável”, misturando automação e experiência humana elegante.  
Vamos destrinchar isso em 3 camadas: experiência do cliente, operação interna e tecnologia.

---

### 1\. Experiência do Cliente

A ideia é que o cliente compre, configure e veja seu Brann funcionando **sem precisar falar com ninguém**, mas com toque humano se quiser.  
O fluxo ideal seria:

**Etapa 1 – Descoberta e compra**

- **Landing page feita no Lovable** (ou no app da Lasy IA) com login via Supabase (Google, e-mail, WhatsApp).
- Ele escolhe o plano (Starter, Basic, Avançado, Futurista).
- Pagamento via Stripe ou Hotmart.  
	Assim que confirmado, um webhook dispara o onboarding no n8n.

**Etapa 2 – Boas-vindas automatizada**

- O n8n envia um e-mail e mensagem de WhatsApp do próprio Brann:  
	“Ora pois, bem-vindo à tua automação Leaf! Vamos preparar o teu ambiente, não é?”
- O cliente é levado a um **painel Lovable** onde preenche informações: nome da empresa, setor, WhatsApp Business, Instagram e preferências de voz.

**Etapa 3 – Instalação e personalização**

- Ao enviar o formulário, o n8n cria automaticamente:
	- Uma instância do Brann (via Evolution API)
		- Um registro no Supabase (empresa, tokens, status)
		- Um fluxo de teste para validação.
- O cliente pode testar direto no WhatsApp (ex: “Olá Brann!” e o bot responde).

**Etapa 4 – Treinamento e suporte**

- Dentro do app/portal há uma aba “Aprender” com mini-tutoriais feitos pela **Nyra** (vídeos curtos, animações e FAQs).
- O Alphie monitora erros e tempo de resposta do Brann e envia relatórios semanais automáticos (Notion + Supabase + e-mail).

---

### 2\. Operação Interna

O processo é invisível para o cliente, mas orquestrado por ti:

- O **n8n** centraliza toda a lógica: onboarding, integração, alertas e renovações.
- O **Supabase** mantém registros e logs de cada cliente (status de pagamento, API keys, plano, data de ativação).
- O **Notion 3.0** funciona como CRM e centro de conhecimento — cada cliente ganha uma página com histórico, automações e scripts personalizados.
- O **Alphie** monitora uptime, envia alertas para o time e até pode sugerir upsells (“cliente X está usando 80% da capacidade do plano”).

---

### 3\. Infraestrutura Tecnológica

O relatório mostra que Lovable e Supabase são perfeitos para esse tipo de automação leve:

- Lovable gera o **frontend do portal de onboarding** com autenticação Supabase embutida.
- Supabase é o **banco unificado** de clientes e chaves API.
- n8n cuida de **webhooks, rotinas e integração** com Evolution API, Notion, Stripe, e-mail e WhatsApp.
- EasyPanel/Hostinger hospeda tudo.
- Kokoro ou ElevenLabs entram depois para gerar vozes personalizadas do Brann.

---

### Recomendações práticas

1. **Desenvolver o portal de onboarding** no **Lovable**: formulário + dashboard + guia interativo.
2. **Automatizar instalação** via n8n: quando o cliente conclui o formulário, o fluxo cria o workspace completo.
3. **Conectar Alphie** como supervisor técnico: se algum serviço falhar, ele alerta o time.
4. **Usar Notion** como painel interno de clientes.
5. **Usar Lasy IA ou Lovable Cloud** para gerar o app se quiser interface mobile (Lasy é mais visual, Lovable é mais Dev-Ops).

---

Se quiser, posso te guiar passo a passo na **criação do portal de onboarding Lovable + Supabase + n8n**, incluindo os prompts exatos para gerar o app no Lovable e os fluxos automáticos no n8n.  
Quer que eu monte essa sequência?

sim.

Bora montar o **onboarding Leaf** ponta-a-ponta — 100% “self-service” pro cliente, mas com Alphie de olho em tudo e o Brann recebendo a pessoa no WhatsApp. Vou te entregar os blocos **copiar-e-colar**: prompt do Lovable (portal de onboarding), schema do Supabase, variáveis `.env`, e 5 workflows n8n (compra → provisionamento → conexão WhatsApp/Evolution → mensagem de teste → monitoramento/boas-vindas). Onde fizer sentido, eu aponto as ancoragens técnicas do teu relatório.

---

## 0) Visão rápida do que vamos criar

- **Portal de Onboarding (Lovable)** com login Supabase, checkout (Stripe/Hotmart), formulário de empresa, checklist e “testar meu Brann”. Lovable já integra bem com Supabase e autenticação, inclusive com funções edge e gestão de segredos.
	relatorio
	relatorio
- **Base Supabase** com tabelas: `customers`, `installations`, `channels`, `secrets`, `usage_logs` e RLS. Supabase entrega DB + auth + storage + APIs instantâneas.
	relatorio
- **n8n** orquestrando tudo (webhooks, filas, retries, monitoramento e integrações).
	relatorio
- **EasyPanel/Hostinger** pra subir n8n e apps rapidamente (templates, SSL, painel em `:3000`).
	relatorio
- **Notion 3.0 (Agentes)** pra playbooks, runbooks e relatórios automáticos semanalmente (Alphie “curador”).
	relatorio
	relatorio

---

## 1) Portal de onboarding no Lovable (prompt pronto)

No Lovable, cria um projeto novo e usa este prompt:

```markdown
Crie um portal de onboarding para o produto "Leaf" com:

1) Autenticação Supabase (e-mail e Google). Páginas: /login, /signup, /app.
2) Dashboard /app com 4 cards: 
   A) "Plano e Pagamento" (mostra status do plano, link para checkout/portal do cliente via Stripe ou Hotmart).
   B) "Minha Empresa" (form com: company_name, segment, whatsapp_business, instagram, website, preferred_voice).
   C) "Instalação do Brann" (botão "Provisionar" chama endpoint /api/provision com body do formulário).
   D) "Testes" (input para enviar mensagem 'ping' ao WhatsApp e exibir resposta do Brann).
3) Admin area oculta /admin (apenas role=admin) para ver lista de clientes, status e logs.
4) Integração Supabase:
   - Tabelas: customers, installations, channels, secrets, usage_logs (crie migrations automáticas).
   - Policies (RLS): cada user só enxerga seus registros.
5) Edge functions:
   - POST /api/provision: valida dados, cria linhas em installations, channels, secrets com status "pending", e dispara webhook para n8n (URL em variável).
   - POST /api/test-whatsapp: envia mensagem "Olá Brann!" via n8n webhook.
6) Settings:
   - Armazene chaves e endpoints (N8N_WEBHOOK_BASE, EVOLUTION_BASE_URL, etc.) em segredos do app.
   - Use TOASTs e loader states em todas as ações.
7) UI:
   - Design clean, dark-friendly, com passos numerados e uma barra de progresso (25/50/75/100%).
   - Página de FAQ com dúvidas comuns e links de ajuda.
8) Esquema de erros e reexecução:
   - Se provisionamento falhar, mostrar botão "Tentar novamente" que reposta para /api/provision.
```

Por que Lovable aqui? Ele já cobre **autenticação**, **integração com Supabase** e **edge functions**, além de guardar **segredos** — perfeito pro painel de onboarding.

relatorio

relatorio

relatorio

---

## 2) Supabase — SQL (copiar e colar em “SQL editor”)

```markdown
-- SCHEMA BASE
create table public.customers (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  email text not null,
  company_name text,
  segment text,
  created_at timestamptz default now()
);

create table public.installations (
  id uuid primary key default gen_random_uuid(),
  customer_id uuid not null references public.customers(id) on delete cascade,
  plan text not null default 'starter',
  status text not null default 'pending', -- pending|provisioning|active|error|suspended
  evolution_instance_id text, -- id da sessão Evolution/WhatsApp
  webhook_secret text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create table public.channels (
  id uuid primary key default gen_random_uuid(),
  installation_id uuid not null references public.installations(id) on delete cascade,
  channel text not null, -- 'whatsapp'
  identifier text,       -- phone number / waid
  status text not null default 'pending',
  created_at timestamptz default now()
);

create table public.secrets (
  id uuid primary key default gen_random_uuid(),
  installation_id uuid not null references public.installations(id) on delete cascade,
  key text not null,
  value text not null,
  created_at timestamptz default now()
);

create table public.usage_logs (
  id bigint primary key generated always as identity,
  installation_id uuid not null references public.installations(id) on delete cascade,
  event text not null, -- 'provision.start' | 'provision.done' | 'ping.sent' | ...
  metadata jsonb,
  created_at timestamptz default now()
);

-- RLS
alter table public.customers enable row level security;
alter table public.installations enable row level security;
alter table public.channels enable row level security;
alter table public.secrets enable row level security;
alter table public.usage_logs enable row level security;

create policy "Customers by owner"
on public.customers for all
using (auth.uid() = user_id)
with check (auth.uid() = user_id);

create policy "Installations by customer owner"
on public.installations for all
using (customer_id in (select id from public.customers where user_id = auth.uid()))
with check (customer_id in (select id from public.customers where user_id = auth.uid()));

create policy "Channels by installation owner"
on public.channels for all
using (installation_id in (select i.id from public.installations i join public.customers c on c.id=i.customer_id where c.user_id=auth.uid()))
with check (installation_id in (select i.id from public.installations i join public.customers c on c.id=i.customer_id where c.user_id=auth.uid()));

create policy "Usage logs read-only by owner"
on public.usage_logs for select
using (installation_id in (select i.id from public.installations i join public.customers c on c.id=i.customer_id where c.user_id=auth.uid()));

-- (Opcional) Secrets não visíveis ao cliente (só server role)
create policy "Secrets server-only" on public.secrets
for all using (false) with check (false);
```

Supabase entrega **APIs instantâneas, auth e storage**; Lovable conecta e cria tabelas/policies automaticamente se você quiser; e RLS é prática recomendada.

relatorio

relatorio

relatorio

---

## 3) Variáveis de ambiente (n8n + portal)

Cria um `.env` (ou use Secrets no EasyPanel/Lovable Cloud):

```markdown
# Geral
APP_ENV=production
SUPABASE_URL=...
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE=...

# n8n
N8N_HOST=automacao.seudominio.com
WEBHOOK_URL=https://automacao.seudominio.com/
N8N_ENCRYPTION_KEY=chave-grande-aleatoria
N8N_WEBHOOK_BASE=https://automacao.seudominio.com/webhook/

# Evolution API (WhatsApp)
EVOLUTION_BASE_URL=https://evolution.seudominio.com
EVOLUTION_API_KEY=xxxxx
EVOLUTION_INSTANCE_ID=auto (deixe o workflow criar)
DEFAULT_WA_NUMBER=55XXXXXXXXXXX

# Payments
STRIPE_WEBHOOK_SECRET=whsec_xxx
HOTMART_WEBHOOK_SECRET=xxx

# Notion
NOTION_TOKEN=secret_xxx
NOTION_DB_CLIENTS=xxx
```

Hospedar com **EasyPanel** é direto (templates, SSL, painel).

relatorio

relatorio

---

## 4) Workflows n8n (5 peças chaves)

## 4.1 purchase\_webhook (Stripe/Hotmart → Supabase)

**Trigger:** Webhook `/webhook/purchase`  
**Nós principais:**

- Function (validate signature)
- HTTP Request → Stripe/Hotmart (fetch purchase)
- Supabase (Upsert em `customers` + `installations` com `status='pending'`, define `plan`)
- Set → `provision_token`
- HTTP Request → Lovable `/api/provision` (passa `user_id`, `company_name`, `plan`, `provision_token`)
- Create Log (`usage_logs`: `provision.start`)

> Dica: usa o **“queue mode”** do n8n em produção pra robustez.
> 
> relatorio

## 4.2 provision\_client (Lovable → Evolution → Supabase)

**Trigger:** Webhook `/webhook/provision` (recebe do Lovable)  
**Nós:**

- Supabase → pega `installation_id` e dados do formulário
- HTTP Request → Evolution API (criar/pegar `instance_id`, parear número)
- Supabase → salva `evolution_instance_id`, `channel.status='active'`, `installations.status='provisioning'`
- Test Ping (vide 4.3)
- Se OK: `installations.status='active'` + log `provision.done`
- Se falha: `installations.status='error'` (+ retry agendado)

## 4.3 whatsapp\_test\_message (ping “Olá Brann!”)

**Trigger:** Webhook `/webhook/test-wa`  
**Nós:**

- Supabase → resolve `installation_id` + número
- HTTP Request → Evolution `/message/sendText` body: `{ to: <DEFAULT_WA_NUMBER>, text: "Olá Brann!" }`
- Response → devolve “enviado” + guarda em `usage_logs` evento `ping.sent`

## 4.4 welcome\_sequence (boas-vindas e hand-holding)

**Trigger:** quando `installations.status` muda para `active`  
**Nós:**

- WhatsApp → mensagem do Brann (texto+áudio TTS Kokoro): “Bem-vindo! Vamos validar 3 coisinhas…”
- Notion → cria página do cliente com checklist “Primeira Semana”
- E-mail → onboarding pack (FAQ + vídeos rápidos da **Nyra**)

## 4.5 alphie\_monitor (saúde, alertas e relatórios)

**Schedule:** a cada 5 min (health) + semanal (relatório)  
**Nós:**

- Health checks (Evolution status, latência do WhatsApp, fila do n8n)
- Supabase → insere `usage_logs` com métricas
- Notion → atualiza página do cliente (quadro “Sinais vitais”)
- Se anomalia: WhatsApp para time técnico + e-mail para Gabriel com resumo

**Por que n8n?** Ele é o “maestro” que conecta Supabase, Notion, Evolution e pagamentos, com triggers, webhooks, loops e integrações.

relatorio

relatorio

> Observação: se quiser, eu te mando depois os **JSONs desses 5 workflows** já com os nós HTTP/Supabase/Function preenchidos.

---

## 5) Mensagens de boas-vindas do Brann (pronto pra colar)

**Texto (WhatsApp):**

> Ora pois, bem-vindo ao Leaf! Já conectei o teu número e preparei os passos iniciais.
> 
> 1. Responde “testar” para eu validar áudio e memória curta.
> 2. Envia a tua bio/serviços (texto ou PDF) para eu treinar respostas.
> 3. Diz “catálogo” quando quiser ver templates de mensagens.

**Áudio (Kokoro) – prompt:**

> Voz amigável portuguesa PT-PT, ritmo médio, tom consultivo. Conteúdo igual ao texto acima.

---

## 6) Tela “Minha Empresa” — campos e validação

- **company\_name** (obrigatório), **segment**, **whatsapp\_business** (regex +55…), **instagram**, **website**, **preferred\_voice** (select: “Kokoro-Warm”, “Kokoro-Neutral”).
- Salva no Supabase e deixa o botão “ **Provisionar** ” só habilitar quando `company_name` e `whatsapp_business` estiverem preenchidos.

---

## 7) Notion 3.0 (Agente do Alphie)

No Notion, cria:

- **DB “Clientes Leaf”** (colunas: Empresa, Plano, Health, Último ping, Uptime 7d, Links úteis)
- **Agente** com instruções: “Ler métricas do Supabase semanalmente e atualizar ‘Relatório Semanal’ com: volume de mensagens, tempo médio de resposta, top 5 FAQs, sugestões de melhoria.”  
	Essa automação é suportada pelos **agentes do Notion 3.0** com memória e acesso a bases; conecta com n8n para coleta/entrega.
	relatorio
	relatorio

---

## 8) Segurança e segredos

- **Segredos no Lovable** (chaves de APIs) e **Creds no n8n** — não hardcode.
	relatorio
- **RLS no Supabase** já aplicado no schema acima.
	relatorio
- **Backups** periódicos do Supabase e export de workflows n8n.
	relatorio

---

## 9) Infra: subir tudo rápido no EasyPanel/Hostinger

- Cria VPS, instala **EasyPanel** (acessa em `http://IP:3000`), configura domínio e SSL.
- Adiciona app n8n via **template** e define `N8N_ENCRYPTION_KEY`, `WEBHOOK_URL` etc.
	relatorio
	relatorio

---

## 10) Fluxo do cliente (resumo prático)

1. Cliente compra → webhook confirma plano → cria `customer` e `installation`.
2. Cliente preenche **Minha Empresa** → clica **Provisionar** → n8n cria Evolution/WhatsApp, salva chaves, roda teste.
3. Status muda para **active** → Brann manda boas-vindas + Alfie cria página no Notion + Nyra envia micro-tutoriais.
4. Alphie monitora saúde e envia relatórios semanais.

---

Quer o **pacote com os 5 workflows n8n em JSON** e o **esqueleto do app Lovable** com as rotas/edge functions já nomeadas como descrevi? Eu já te mando numa tacada só para colar e subir.