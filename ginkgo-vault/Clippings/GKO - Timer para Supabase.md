---
title: "GKO - Timer para Supabase"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69a1b889-7304-8327-9765-6728cf973804"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 27 de fev. às 12:30

Você está tentando “pingar” o Supabase pra ele não hibernar — ideia certa. O erro que apareceu é simples: você está tentando **inserir na tabela errada**.

Na sua tela, o node “Create a row” está apontando pra **`n8n_chat_histories`**, que tem `session_id` como **NOT NULL**. Como você não está mandando `session_id`, ele explode com:

> null value in column "session\_id" … violates not-null constraint

A solução profissional é: **criar uma tabela só de keepalive** (ou manter 1 único registro e só atualizar), e o seu timer escreve nela.

---

## Opção A (recomendada): 1 linha fixa + UPDATE (não cresce o banco)

### 1) Crie a tabela no Supabase (SQL Editor)

```markdown
create table if not exists public.keepalive (
  id text primary key,
  last_ping timestamptz not null default now(),
  source text
);

insert into public.keepalive (id, source)
values ('SUPABASE_KEEPALIVE', 'bootstrap')
on conflict (id) do nothing;
```

### 2) No n8n (seu workflow da imagem)

**Node 1 — Schedule Trigger**

- Cron: a cada **6 horas** (ou 12h). (Pode ser 1h se você quiser, mas é overkill.)

**Node 2 — Supabase**

- Resource: **Row**
- Operation: **Update**
- Table: **keepalive**
- Filter/Where:
	- `id` = `SUPABASE_KEEPALIVE`
- Fields to update:
	- `last_ping` = `={{ $now }}`
		- `source` = `n8n`

Pronto. Zero crescimento infinito.

---

## Opção B: INSERT (mais simples, mas cresce)

Se preferir “Create row”, faça assim:

### 1) SQL

```markdown
create table if not exists public.keepalive_log (
  id bigserial primary key,
  pinged_at timestamptz not null default now(),
  source text
);
```

### 2) n8n

- Operation: **Create**
- Table: **keepalive\_log**
- Fields:
	- `source` = `n8n`
		- (não precisa mandar `pinged_at`, o default resolve)

---

## Credencial do Supabase no n8n (ponto crítico)

Se essa tabela tiver RLS ativo, use **Service Role Key** no n8n (ou desative RLS nessa tabela). Keepalive é infraestrutura; faz sentido deixar **sem RLS** ou com policy bem permissiva só pra esse caso.

**Checklist rápido**

- ✅ Node Supabase apontando pra `keepalive` / `keepalive_log` (não `n8n_chat_histories`)
- ✅ Campos obrigatórios preenchidos (ou com default)
- ✅ Chave/credencial com permissão (ideal: service role)
- ✅ Schedule rodando (6h/12h)

---

## Por que o seu fluxo falhou

Você criou um “timer”, mas ele está tentando registrar na tabela de **histórico de chat** do Brann (`n8n_chat_histories`). Essa tabela exige `session_id` porque é memória/conversa — não é lugar de heartbeat.

---

Se você quiser, te digo exatamente **como configurar o node Supabase “Update”** com os cliques (campo por campo) baseado no seu print — mas a correção estrutural é essa: **keepalive em tabela própria + update de uma linha fixa**. Isso é o “marca-passo” do projeto: simples, barato e não incha o banco.

![27e041d6-fece-4f2c-89a4-208816fe2caa.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000f51c71f5b10af8f7d67859c3&ts=495692&p=fs&cid=1&sig=50e9160997936ad8f7e9a2bb9a15a28582fe4baf34e0da16d2d78461177e34da&v=0)

Perfeito. Agora você está no caminho certo.  
O erro atual é simples e técnico:

> **“At least one select condition must be defined”**

Você está usando **Update**, mas não definiu qual linha deve ser atualizada.

O Supabase precisa de um **WHERE**.

---

## 🔧 COMO CORRIGIR NO N8N (PASSO A PASSO)

No node **Update row**:

## 1️⃣ Vá em Select Conditions

Clique em **Add Condition**

Configure exatamente assim:

- **Field Name** → `id`
- **Operator** → `Equals`
- **Value** → `SUPABASE_KEEPALIVE`

Agora o Supabase sabe qual linha atualizar.

---

## 🔥 IMPORTANTE

Isso só funciona se essa linha já existir.

Confirme no Supabase SQL Editor:

```markdown
select * from keepalive;
```

Se não existir, rode:

```markdown
insert into public.keepalive (id, source)
values ('SUPABASE_KEEPALIVE', 'bootstrap')
on conflict (id) do nothing;
```

---

## ✅ Sua configuração final no n8n deve ficar assim:

**Operation:** Update  
**Table:** keepalive

### Select Conditions:

| Field | Operator | Value |
| --- | --- | --- |
| id | Equals | SUPABASE\_KEEPALIVE |

### Fields to Send:

- `last_ping` → `{{ $now }}`
- `source` → `n8n`

---

## 🧠 O que está acontecendo tecnicamente

Update sem WHERE = risco de atualizar tudo  
Por isso o node bloqueia.

Você agora está criando um **heartbeat persistente controlado**, não um log infinito.

---

## ⏱ Melhor Frequência

• A cada 6 horas → suficiente  
• A cada 1 hora → mais seguro  
• A cada 5 minutos → exagero

Supabase free hiberna após inatividade, então 1h ou 6h mantém acordado.

---

Se quiser, posso te mandar:

- Versão alternativa usando **RPC**
- Versão via **HTTP Request direto na REST API**
- Ou versão ultra limpa que só faz `select 1`

Mas com essa condição adicionada, já resolve.