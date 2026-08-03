---
title: "GKO - MCP Antigravity Checklist"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/696403d9-c31c-832d-91de-97a19b6df15c"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
dom., 11 de jan. às 17:12

Direto ao ponto.  
Pensa no **MCP do Antigravity** como um **porto espacial**: se faltar uma peça, a nave (Claude/AG) não acopla.

## O que o MCP do Antigravity PRECISA TER (checklist definitivo)

---

## 1️⃣ Um endpoint MCP realmente MCP

Sem isso, o Antigravity recebe HTML (login do n8n) e surta.

**Obrigatório:**

- Endpoint válido:
```markdown
https://SEU_DOMINIO/mcp-server/http
```

Teste mental:

> “Se eu abrir no navegador e vier tela de login do n8n → errado.”

---

## 2️⃣ Autenticação que o Antigravity entende

Hoje, na prática, **funciona assim**:

### ✅ Access Token (recomendado)

- Criado em **Settings → API Credentials → Access Tokens**
- Escopo: **full**
- Usado como:
```markdown
Authorization: Bearer SEU_TOKEN
```

⚠️ OAuth costuma falhar em setups self-hosted + proxy.

---

## 3️⃣ Workflows marcados como MCP Tools

Esse ponto mata 80% das integrações.

Cada workflow que vira “tool” precisa:

- ✅ Ativo
- ✅ Flag **Available in MCP** ligada
- Nome claro (ex: `ping_n8n`, `search_leads`, `create_ticket`)

Regra de ouro:

> **1 workflow = 1 tool MCP**

---

## 4️⃣ Entrada MCP válida no workflow

O workflow **PRECISA COMEÇAR** com:

- **MCP Trigger** (ou MCP-compatible entry)

Se começa com:

- Manual Trigger ❌
- Webhook ❌
- Cron ❌

→ O Antigravity ignora.

---

## 5️⃣ Output MCP-friendly (JSON limpo)

O retorno do workflow deve ser:

```markdown
{
  "success": true,
  "data": "...",
  "message": "ok"
}
```

Evite:

- Binary
- HTML
- Respostas gigantes sem estrutura

O MCP é um **contrato**, não um dump.

---

## 6️⃣ Reverse proxy NÃO pode quebrar headers

Esse é o vilão silencioso (especialmente Elestio).

Proxy precisa:

- Não remover `Authorization`
- Não redirecionar `/mcp-server/*`
- Não injetar login page

Se estiver usando:

- Nginx
- Traefik
- Cloudflare

➡️ garantir **pass-through total**.

Analogia:

> O proxy é o porteiro.  
> Se ele rasga o crachá, ninguém entra.

---

## 7️⃣ Variáveis de ambiente mínimas

No n8n:

```markdown
N8N_MCP_ENABLED=true
N8N_PROTOCOL=https
N8N_HOST=SEU_DOMINIO
```

Sem isso, o MCP sobe “capenga”.

---

## 8️⃣ O que o Antigravity espera encontrar

Quando conecta, ele faz algo como:

```markdown
{
  "tools": [
    {
      "name": "ping_n8n",
      "description": "Health check do n8n",
      "input_schema": {...}
    }
  ]
}
```

Se não listar tools → falha silenciosa.

---

## Diagnóstico rápido do teu print

Pelo print:

- ⚠️ **MCP Client com alerta vermelho**
- Workflow isolado, não conectado ao MCP Trigger
- Provável retorno HTML (login)

Tradução:

> O Antigravity está batendo na porta errada ou sem credencial.

---

## Setup que FUNCIONA SEM DOR

Experiência de guerra:

✅ n8n self-hosted via **Docker Compose / Easypanel**  
✅ Proxy simples (Nginx Proxy Manager)  
❌ Elestio costuma quebrar MCP  
❌ OAuth

---

## Próximo passo prático (sem filosofar)

Se quiser, eu te entrego:

1. **Workflow MCP mínimo funcional** (ping)
2. **mcp\_config.json** pronto pro Antigravity
3. **Checklist de proxy** pra Hostinger / Cloudflare
4. Arquitetura MCP → Leaf / Wave / Pyre (multi-tenant)

Diz:  
👉 *“Quero o setup mínimo funcionando agora”*  
ou  
👉 *“Quero MCP produção SaaS”*

E a nave decola. 🚀

## MCP em produção SaaS (multi-tenant): o que precisa existir

Pensa no MCP como **API de ferramentas**. Em SaaS, você precisa de 3 camadas: **Gateway (porteiro)** → **Router (cérebro)** → **Tools (mãos)**. Se misturar isso, vira distopia: um cliente chamando ferramenta do outro.

---

## 1) Arquitetura mínima (produção) — “cidade murada”

## A) Domínios e rotas (obrigatório)

- `mcp.seudominio.com` → endpoint MCP do n8n (`/mcp-server/http`)
- `n8n.seudominio.com` → UI do n8n (não precisa expor publicamente)
- `webhook.seudominio.com` → webhooks externos (separado do MCP)

**Por quê:** MCP é “canal privilegiado”. Separar reduz chance de cair no login HTML / redirects / WAF.

## B) Gateway / Reverse Proxy (obrigatório)

O proxy precisa:

- **preservar `Authorization`**
- **não redirecionar** `/mcp-server/http`
- **bloquear UI** do n8n no subdomínio do MCP (ideal: nem existir UI ali)

> MCP é o túnel de serviço. UI é a porta da frente. Não mistura.

## C) Autenticação (produção de verdade)

Você vai precisar de **2 níveis**:

1. **Auth do servidor MCP** (para o Antigravity entrar)
- `Authorization: Bearer <TOKEN_MCP_SERVIDOR>`
2. **Auth por tenant** (para o teu Router saber “quem é quem”)
- `X-Tenant-Id: <tenant_id>` (ou derivado do token do cliente)
- `X-Workspace: leaf|wave|pyre` (opcional, mas ajuda)

Sem isso, multi-tenant vira “open bar”.

## D) Isolamento de tenants (não-negociável)

Você tem 3 modelos (do mais simples ao mais robusto):

### Modelo 1 — Um n8n por tenant (mais seguro, mais caro)

- Cada cliente com instância + MCP token próprio
- Excelente pra início de SaaS B2B premium

### Modelo 2 — Um n8n central + Router (mais comum)

- Um MCP só
- Um workflow “Router” valida tenant e direciona para sub-workflows
- Requer disciplina forte + logs + rate limit

### Modelo 3 — Híbrido

- Clientes grandes: instância própria
- Clientes pequenos: multi-tenant no mesmo n8n

---

## 2) O que declarar no n8n (Tools MCP): funções obrigatórias

## Regra: “1 workflow = 1 tool”

Cada tool tem:

- nome estável (snake\_case)
- descrição curta
- input schema claro (campos)
- output sempre JSON

### Tool 0 — router\_dispatch (obrigatória em SaaS)

**Função:** recebe pedidos do Antigravity e roteia pro conjunto certo (Leaf/Wave/Pyre + tenant)

**Inputs**

- `tenant_id` (string) *(ou inferido por token)*
- `workspace` (`leaf|wave|pyre`)
- `action` (string)
- `payload` (object)

**Output**

- `success` (bool)
- `result` (object)
- `trace_id` (string)

---

## Pacote LEAF (WhatsApp / atendimento / vendas)

1. `leaf_lead_upsert`
- cria/atualiza lead (telefone, nome, tags, origem)
2. `leaf_conversation_log_append`
- grava mensagens, eventos, status (para memória/CRM)
3. `leaf_faq_answer`
- consulta base e devolve resposta curta (RAG do teu lado)
4. `leaf_catalog_search`
- filtra ofertas/planos/produtos (ou imóveis) por preferências
5. `leaf_appointment_create`
- cria agendamento (Google Calendar / Cal.com)
6. `leaf_quote_generate`
- gera proposta (texto + itens + preço) + link de pagamento
7. `leaf_contract_generate_pdf`
- gera contrato (template + dados) e retorna URL
8. `leaf_handoff_open_ticket`
- abre ticket (Chatwoot/CRM) e retorna ID

---

## Pacote WAVE (CRM / operações / analytics)

1. `wave_pipeline_move_deal`
- move card no funil + motivo
2. `wave_task_create`
- cria tarefa com SLA, prioridade, dono
3. `wave_kpi_snapshot`
- retorna KPIs (leads, conversão, receita, churn, NPS)
4. `wave_invoice_status`
- checa cobrança/assinatura (Stripe/Asaas)
5. `wave_alert_push`
- envia alerta (WhatsApp/Telegram/Discord) com severidade

---

## Pacote PYRE (conteúdo / social / automação)

1. `pyre_content_brief_create`
- cria briefing (tema, público, tom, CTA)
2. `pyre_script_generate`
- gera roteiro curto (Reel/TikTok)
3. `pyre_asset_generate_request`
- dispara geração (imagem/vídeo) via tua stack
4. `pyre_schedule_post`
- agenda post (plataforma, data, legenda, mídia)
5. `pyre_post_publish`
- publica agora

---

## Pacote CORE (produção, segurança, observabilidade)

1. `core_healthcheck`
- ping geral + status serviços
2. `core_secret_get`
- pega segredo por tenant (sem vazar)
3. `core_audit_log_write`
- loga ação com `tenant_id`, `actor`, `tool`, `payload_hash`
4. `core_rate_limit_check`
- valida limites por tenant
5. `core_failover_route`
- se serviço caiu, escolhe rota alternativa (ex: fallback provider)

> Se tu tiver só 5 tools no começo, que sejam:  
> `router_dispatch`, `core_healthcheck`, `leaf_lead_upsert`, `leaf_quote_generate`, `wave_kpi_snapshot`.

---

## 3) O que declarar no Antigravity (funções): como “o AG enxerga”

No Antigravity, você vai declarar um **server MCP** e ele vai “importar” as tools do n8n. Em produção, você quer:

## A) 1 server MCP por ambiente

- `mcp-prod` → produção
- `mcp-staging` → homolog

## B) Categorizar tools por “domínio” (para evitar o AG chamar coisa errada)

Você vai apresentar as tools como um catálogo lógico:

### Categoria: leaf.\*

- `leaf.lead_upsert`
- `leaf.quote_generate`
- `leaf.contract_generate_pdf`
- etc.

### Categoria: wave.\*

- `wave.kpi_snapshot`
- `wave.task_create`

### Categoria: pyre.\*

- `pyre.schedule_post`
- `pyre.post_publish`

### Categoria: core.\*

- `core.healthcheck`
- `core.audit_log_write`

Mesmo que no n8n o nome seja `leaf_lead_upsert`, no Antigravity tu “expõe” como `leaf.lead_upsert` (mais limpo).  
Se não der alias no AG, mantém no padrão `leaf_lead_upsert` mesmo — só não mistura.

## C) Política de uso (guardrails)

No Antigravity você precisa impor regras para o agente:

- sempre enviar `tenant_id`
- nunca chamar tools fora do workspace do pedido
- logar `trace_id` em toda ação
- exigir `dry_run=true` para ações destrutivas (ex: deletar, cancelar)

**Padrão recomendado de inputs para TODAS as tools:**

- `tenant_id` (string)
- `trace_id` (string)
- `dry_run` (bool, default false)
- `payload` (object)

Assim o AG vira um piloto profissional, não um estagiário com botão nuclear.

---

## 4) Convenção de nomes e schemas (pra não virar caos)

## Naming

- `leaf_*`, `wave_*`, `pyre_*`, `core_*`
- sem espaços
- sem versionar no nome (versiona no schema: `schema_version`)

## Output padrão (todas)

```markdown
{
  "success": true,
  "trace_id": "…",
  "data": {},
  "error": null
}
```

## Erros padrão

```markdown
{
  "success": false,
  "trace_id": "…",
  "data": null,
  "error": { "code": "TENANT_FORBIDDEN", "message": "…" }
}
```

---

## 5) Fluxo operacional (como roda na vida real)

1. Antigravity recebe uma intenção (“criar proposta pro lead X”)
2. Antigravity chama `router_dispatch` com `tenant_id`, `workspace=leaf`, `action=quote_generate`
3. Router valida:
	- tenant existe?
		- token pode?
		- rate limit ok?
4. Router executa tool real (ex: `leaf_quote_generate`)
5. Router grava audit (`core_audit_log_write`)
6. Retorna JSON pro Antigravity com `trace_id`

---

## 6) O “mínimo de produção” que eu recomendo pra tua Ginkgo

Se tu quer lançar Leaf/Wave/Pyre juntos sem virar refém de bugs:

### MVP de Tools (12 total)

**CORE (4):**

- `core_healthcheck`
- `core_audit_log_write`
- `core_secret_get`
- `core_rate_limit_check`

**LEAF (4):**

- `leaf_lead_upsert`
- `leaf_conversation_log_append`
- `leaf_quote_generate`
- `leaf_handoff_open_ticket`

**WAVE (2):**

- `wave_task_create`
- `wave_kpi_snapshot`

**PYRE (2):**

- `pyre_content_brief_create`
- `pyre_schedule_post`

Isso já vende, entrega, mede e escala.

---

## Próximo passo (prático)

Eu posso te devolver já no formato “copy-paste”:

1. A lista final de tools com **descrição + inputs exatos + outputs** (contrato MCP)
2. O desenho do **Router multi-tenant** (validação + roteamento + auditoria)
3. Padrão de **permissões por workspace** (Leaf não chama Wave sem autorização)

Para isso, me diz só 1 coisa (sem debate):  
Você vai de **Modelo 1 (1 n8n por cliente)** ou **Modelo 2 (n8n central multi-tenant)**?