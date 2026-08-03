---
title: "Ginkgo Core - Arquitetura LEAF como SaaS"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/6943a06a-2034-832d-8c6f-86aa7f84adfc"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
qui., 18 de dez. às 3:34

Qual a Arquitetura da implementação e ajuste do LEAF como SaaS, o que é preciso construir, passo a passo, levando em conta o agente Brann, pessoa contrata = adaptamos o Brann para a empresa contratante = implementação = teste = produção. Algo assim

## Arquitetura do LEAF como SaaS (com Brann “clonado” por cliente)

Pense no LEAF como um **“kernel”** (core) + **“mods por cliente”** (config + conhecimento + integrações). O Brann é o “processo” que roda em cima disso: mesma engine, personalidade consistente, mas **contexto/brand/FAQ/catálogos/integrações** mudam por empresa.

Stack-base (coerente com o que vocês já vêm usando):

- **WhatsApp (Evolution API)** → entrada e envio de mensagens
- **n8n** → orquestração (roteador, filas, fallback humano, logs)
	relatorio
- **Supabase (Postgres + Auth + Storage + Edge Functions)** → dados, RLS/segurança, arquivos, funções
	relatorio
- **Lovable** (opcional, mas bom) → painel web rápido (admin do cliente + onboarding)
	relatorio
- **EasyPanel/Hostinger** → deploy e operação do n8n/serviços
	relatorio

---

## 1) O que precisa existir (blocos de construção)

### A. Núcleo do SaaS (multi-tenant)

1. **Tenant Manager**
- Criação de empresa (tenant)
- Domínio/ID do tenant
- Plano (Basic/Intermediário/3)
- Status (trial/ativo/suspenso)
- Limites (mensagens/mês, canais, integrações)
2. **Config Store (por tenant)**
- Persona/voz do Brann (parâmetros, não reescrever do zero)
- Brand kit (nome, tom, cores, links)
- Regras do negócio (horários, áreas atendidas, SLA, política)
- Integrações (tokens Gmail/Sheets/CRM/Calendar etc.) guardadas como “secrets”
3. **Knowledge Base (por tenant)**
- FAQ / políticas / produtos / serviços / scripts
- Documentos (PDF/links) versionados
- RAG: embeddings por tenant (se usar)
4. **Observability & Billing**
- Logs estruturados por tenant
- Métricas (volume, tempo de resposta, handoff)
- Auditoria (quem viu o quê)
- Cobrança (Stripe/Asaas/etc.) + bloqueio automático por inadimplência

> Multi-tenant: o mais simples e eficiente é **um banco com tabelas multi-tenant** + **RLS por tenant\_id** (segurança “de ferro”)
> 
> relatorio
> 
> .

---

## 2) Pipeline “assinou → adaptamos Brann → implementa → testa → produção”

### Fase 0 — Preparar o “LEAF Core” (feito uma vez)

**Objetivo:** deixar o sistema “industrial”, pronto pra replicar.

1. **Schema no Supabase**  
	Tabelas mínimas (sugestão):
- `tenants`
- `tenant_users` (quem administra)
- `channels` (whatsapp instances, instagram etc.)
- `secrets` (referências; segredo real fica em vault/n8n creds)
- `kb_sources` (docs/FAQ)
- `kb_chunks` (se usar RAG)
- `contacts` (leads/clientes do cliente)
- `conversations`
- `messages`
- `tickets` (handoff humano)
- `events` (agendamentos)
- `usage_metrics`
2. **RLS**
- Tudo com `tenant_id`
- Policies: usuário só acessa seu tenant
	relatorio
3. **n8n “BRANN-CORE” (template)**  
	Workflows padrão:
- `INBOUND` (Webhook Evolution) → normaliza → identifica tenant → roteia intenção
- `BRAIN` (LLM) → carrega config do tenant → carrega KB → responde
- `TOOLS` (Sheets/Gmail/Calendar/CRM) → ações
- `HUMAN HANDOFF` (Chatwoot/WhatsApp humano) → abre ticket
- `OBS` (log + métricas + alertas)
4. **Painel Admin (Lovable ou outro)**
- Tela “Onboarding Wizard”
- Upload de materiais
- Ajuste de scripts/FAQ
- Conectar integrações
- Ver conversas/tickets/relatórios
	relatorio

---

### Fase 1 — Venda/assinatura (gatilho)

**Entrada:** pagamento confirmado (webhook de pagamento).

No webhook:

1. Criar `tenant`
2. Criar usuário admin
3. Criar workspace de configs default
4. Abrir “tarefa automática” de onboarding (checklist)

---

### Fase 2 — Onboarding (coleta de dados “cirúrgica”)

**Objetivo:** capturar 20% de info que gera 80% de acerto.

Checklist (form wizard):

- Segmento + oferta principal
- Horários + região atendida + exceções
- Lista de serviços/produtos + preços (ou “sob consulta”)
- Políticas (troca, cancelamento, prazos, garantias)
- Tom de voz (ex.: formal, direto, descontraído)
- FAQ top 30 (pode começar com 10 e crescer)
- Quem é humano responsável pelo handoff
- Integrações: Gmail/Sheets/Calendar/CRM

Saída: alimenta `config_store` e `kb_sources`.

---

### Fase 3 — “Adaptar o Brann” (parametrização, não reinvenção)

Aqui você não cria outro Brann. Você aplica um **overlay por tenant**:

1. **System Prompt fixo (Brann Core)**
- Persona, ética, formato de resposta, limites, handoff
2. **Tenant Prompt (overlay)**
- “Você está operando para a empresa X…”
- Tom/estilo
- Objetivos (vender/agendar/suporte)
- Regras (o que pode/não pode prometer)
3. **Ferramentas habilitadas por plano**
- Basic: atendimento + captação + registro
- Intermediário: + criação/postagem (se for parte do Leaf 2)
- Estágio 3: + site/app (como projeto/entrega)

---

### Fase 4 — Implementação técnica (conectar canais e ferramentas)

1. **WhatsApp**
- Criar/validar instância Evolution
- Webhook apontando para `n8n/INBOUND`
- Validar template de mensagens, mídia, áudio
2. **Credenciais**
- N8n credentials por tenant (isoladas)
- Guardar referências no Supabase; segredo real no n8n/vault
	relatorio
3. **KPIs e alertas**
- Alerta de falha de envio
- Alerta de pico de erros LLM
- Alertas de quota/uso

---

### Fase 5 — Testes (sandbox → staging)

Você precisa de um “modo simulação”:

**Suite de testes mínima**

- 30 perguntas comuns (FAQ)
- 10 cenários de vendas
- 10 cenários de reclamação/estorno
- 10 cenários de handoff

Critérios de aprovação:

- Taxa de resposta correta (manual) > X%
- Handoff disparando nos casos certos
- Registros no CRM/planilha batendo
- Tempo de resposta dentro do SLA

---

### Fase 6 — Produção

1. Trocar `WEBHOOK_URL` para produção
2. Ativar billing + quotas
3. Iniciar monitoramento
4. “Primeira semana assistida”
- revisão diária de conversas
- ajustes no overlay/FAQ
- criação de macros

---

## 3) Operação contínua (o SaaS de verdade)

### A. Ciclo de melhoria (“autotune” controlado)

- Relatório semanal por tenant (top dúvidas, pontos de falha, oportunidades)
- Backlog de KB (novas entradas/ajustes)
- Ajuste de roteamento de intenção no n8n

### B. Versionamento

- `Brann Core` versionado (v1, v2…)
- `Tenant Overlay` versionado (rollback fácil)
- Migrações de DB controladas

### C. Segurança

- RLS por tenant\_id
	relatorio
- Logs com mascaramento (tokens, dados sensíveis)
- Backup (Supabase + export workflows n8n)
	relatorio

---

## 4) Resultado: “Netflix do atendimento”

O cliente **assina**, preenche o wizard, conecta integrações, e em poucas horas o Brann já responde com a cara da empresa. Você vira a “nave-mãe” e cada cliente é um “módulo acoplado” — escalável, replicável, e com controle.

Se você quiser, eu te devolvo isso no formato **Blueprint de implementação** (checklists + tabelas do Supabase + lista de workflows n8n “BRANN-CORE” com nomes e entradas/saídas) para você literalmente transformar em projeto dentro do teu repositório.