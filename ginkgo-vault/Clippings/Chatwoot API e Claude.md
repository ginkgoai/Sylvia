---
title: "Chatwoot API e Claude"
source: "https://chatgpt.com/c/6a5d3815-e3bc-83e9-a8c9-f41e1fc11570"
author:
published:
created: 2026-07-19
description: "ChatGPT conversation with 2 messages"
tags:
  - "clippings"
---
**Você disse**

Chatwoot tem API? Pode ser conectado ao Claude para configuração e automações pelo agente?

---

Sim. O **Chatwoot foi projetado para isso**. Ele possui APIs REST, webhooks e integração com bots, o que o torna um bom candidato para ser controlado por um agente baseado no Claude.

A arquitetura típica seria:

```
Claude
    │
    ▼
Agente (n8n / MCP / Backend Python ou Node)
    │
    ├── Chatwoot API
    ├── Evolution API (WhatsApp)
    ├── CRM / PostgreSQL / Supabase
    ├── Stripe
    └── demais serviços
```

O agente não conversa diretamente com o Chatwoot. Ele utiliza a API para executar ações.

Exemplos do que o Claude pode fazer:

- Criar contatos.
- Criar e atualizar conversas.
- Responder mensagens.
- Alterar status (Open, Pending, Resolved).
- Adicionar tags.
- Atribuir atendimentos a operadores.
- Criar notas internas.
- Buscar histórico da conversa.
- Consultar inboxes, agentes e equipes.

Também é possível usar **webhooks**:

```
Cliente envia WhatsApp
        │
Evolution API
        │
Chatwoot
        │
Webhook
        │
Claude Agent
        │
RAG + Ferramentas
        │
Resposta
        │
API Chatwoot
```

### Configuração automática pelo agente

O Claude também pode auxiliar na configuração inicial se você expuser ferramentas para isso. Por exemplo:

- criar inboxes;
- cadastrar agentes;
- criar equipes;
- configurar automações e etiquetas;
- integrar canais;
- organizar permissões.

Algumas configurações mais profundas (como variáveis de ambiente, Docker Compose e instalação do servidor) continuam sendo feitas no servidor, não pela API pública.

### No seu ecossistema Ginkgo

Para a arquitetura do **Leaf**, eu manteria:

- **Chatwoot** → interface de atendimento humano.
- **Claude** → cérebro de decisão e orquestração.
- **n8n** → automações e integrações.
- **Brann** → identidade/persona operacional.
- **Supabase/PostgreSQL** → memória e CRM.
- **Evolution API** → WhatsApp.

Nesse modelo, o Chatwoot deixa de ser apenas um painel de atendimento e passa a ser uma **interface operacional** controlada pelo agente, que decide quando responder, quando escalar para um humano, quando consultar o RAG e quando acionar outros serviços. Isso se encaixa bem na arquitetura que você vem desenvolvendo para o Ginkgo Leaf.