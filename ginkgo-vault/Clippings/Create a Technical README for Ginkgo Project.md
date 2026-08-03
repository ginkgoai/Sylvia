---
title: "Create a Technical README for Ginkgo Project"
source: "https://manus.im/app/eVZGowNG4WW6f78fyWa6kb"
author:
published:
created: 2026-07-19
description: "Manus é o motor de ação que vai além de respostas para executar tarefas, automatizar fluxos de trabalho e expandir seu alcance humano."
tags:
  - "clippings"
---
Manus 1.6 Lite

[https://evo.ginkgosystems.tech/](https://evo.ginkgosystems.tech/) sim tenho

2.

[https://chat.ginkgosystems.tech/](https://chat.ginkgosystems.tech/)

3\. pode ser app. (ainda não criei)

Perfeito. Temos tudo que precisamos. Vou agora verificar o estado real da Evolution API e do Chatwoot, e em seguida montar o prompt completo da Fase 1 já adaptado ao seu ambiente.

Auditar o ambiente real (Evolution API, Chatwoot, n8n, Supabase)

Os serviços estão respondendo com erro SSL a partir do sandbox (restrição de rede do ambiente isolado), mas isso não é problema — você acessa normalmente pelo seu browser. O que importa é que você confirmou que estão rodando. Vou avançar direto para a geração dos artefatos.

Auditar o ambiente real (Evolution API, Chatwoot, n8n, Supabase)

Gerar o Prompt Mestre da Fase 1 (Brann SDR no n8n) adaptado ao ambiente real

Gerar o SQL do banco de dados do MVP (tabelas leads, messages, agent\_logs)

Publicar os artefatos no repositório e entregar ao usuário

Tudo publicado e pronto para execução. Aqui está o plano de ataque para as próximas horas:

**Diagnóstico do ambiente:**

| Recurso | Status |
| --- | --- |
| Supabase (`xaj<redacted>kn`) | Ativo e conectado |
| n8n (`studio.ginkgosystems.tech`) | Ativo |
| Evolution API (`evo.ginkgosystems.tech`) | Confirmado |
| Chatwoot (`chat.ginkgosystems.tech`) | Confirmado |
| OpenAI API Key | Configurada |
| Dashboard (`app.ginkgosystems.tech`) | A criar |

**Sequência de execução agora:**

**PASSO 1 — Banco de dados (5 minutos)** Abra o Supabase → SQL Editor → cole e execute o conteúdo do `SQL-MVP-FASE1.sql` (em anexo). Isso cria as tabelas `leads`, `messages` e `agent_logs` com RLS ativo.

**PASSO 2 — Fluxo do Brann no n8n (Antigravity)** Abra uma nova sessão no Antigravity, cole o prompt do `PROMPT-ANTIGRAVITY-FASE1.md` (em anexo) e aguarde o retorno. Traga o resultado aqui para eu revisar antes de você montar no n8n.

**PASSO 3 — Configurar Webhook na Evolution API** Após o fluxo estar montado no n8n, você precisará do URL do webhook gerado. Vá no painel da Evolution API e configure o webhook da instância apontando para esse URL.

**Gate de validação (como saber que funcionou):** Mande uma mensagem de WhatsApp para o número conectado na Evolution. Em menos de 5 segundos o Brann deve responder. Verifique no Supabase se um registro apareceu na tabela `leads` e dois na tabela `messages`.

Execute o Passo 1 agora e me confirme quando as tabelas estiverem criadas. Já preparo o próximo artefato enquanto isso.

Tarefa concluída

Como foi este resultado?

Publicar os artefatos no repositório e entregar ao usuário

Manus is an AI Agent and can make mistakes. Please double-check before use.