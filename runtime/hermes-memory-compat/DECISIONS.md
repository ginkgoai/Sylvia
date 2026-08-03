# DECISIONS — decisões de arquitetura (append-only)

- **Hermes Agent (Nous) como core da Sexta-feira**, nativo no Windows (não em
  docker-compose; ele é CLI/gateway). Porquê: é a forma oficial de distribuição;
  só o painel PTY do dashboard é WSL2-only e não usamos.
- **Projeto em C:\sexta-feira** (sem espaços). Porquê: paths com espaço quebram tooling Node.
- **Stub FastAPI "hermes" aposentado** do leaf. "Hermes" = agente Nous; n8n/PG/Redis/Evolution = braços.
- **status_events** no Postgres do leaf, schema `sexta`, role `sexta_app` só INSERT+SELECT (append-only).
- **Modelo em modo grátis (Nous :free)** agora; Claude Sonnet (claude-sonnet-4-6) quando houver billing. IDs reais: opus claude-opus-4-8, sonnet claude-sonnet-4-6, haiku claude-haiku-4-5-20251001.
- **Workflows do fundador = "cascas"**: a Sexta-feira é a porta única; cada casca
  ganha entrada Webhook e é disparada pela Sexta-feira com payload, atrás de gate
  de confirmação (dry-run por padrão). Começar pela mais simples; auto-post por último.
- **CALLIMA fica como produto** (agente vendas WhatsApp, gatilho Evolution). Não
  vira casca, não é disparada/personificada pela Sexta-feira (só observada).
- **n8n MCP (build) dirigido pelo host** (não conector Claude). Acesso de escrita
  tratado como capacidade sensível: inspeciona/valida livre, escreve/executa só com OK.
- **RAG via AnythingLLM**: workspaces `sexta-feira` (próprio) e `callima` (leitura).
  Tool da Callima `base_conhecimento_callima` (HTTP query, somente leitura).
- **Toolset enxuto da Callima** (least privilege): Memory, Think, Audio, Calculator,
  RAG, Calendar, CRM(HubSpot), Handoff/WhatsApp, Stripe(escopado). Sem admin/n8n.
