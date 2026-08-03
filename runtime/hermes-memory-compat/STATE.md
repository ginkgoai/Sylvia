# STATE — estado vivo do projeto (fonte única)

> Atualizar a CADA passo. Data da última atualização: 2026-06-10.

## Direcao atual — 2026-07-15

- Prioridade comercial: Leaf como produto recorrente, com a Agencia Mode feita
  manualmente para operar influenciadores, produtos digitais, estrategia,
  conteudo, trafego e crescimento.
- Wave e Pyre nao sao SaaS de venda nesta etapa; viram capacidades internas da
  agencia ate que a operacao manual prove o fluxo e a margem.
- Sexta-feira MVP: conversa persistente, memoria por evidencia, leitura da
  saude do Leaf e briefing executivo orientado a receita e lucro.
- O Leaf recebeu atividades persistentes por lead e campanhas manuais com
  calendario, canal, publico, criativo e aprovacao. As migracoes ainda precisam
  ser aplicadas no ambiente de desenvolvimento/implantacao controlado.
- O restante deste arquivo e historico operacional de junho e precisa ser
  reconciliado com execucoes atuais antes de orientar uma decisao critica.

## Onde estamos
Fase 1 ("a espinha") da Sexta-feira em andamento + endurecimento da CALLIMA
(produto). Modo de modelo: **grátis** (Nous `nemotron-3-ultra:free`) até injetar
billing; trocar pro Claude Sonnet depois.

## FEITO (provado)
- Stack `leaf` (Docker): postgres, redis, n8n (+worker, modo fila/BullMQ),
  evolution-api (v2.3.7), anythingllm. Stub FastAPI "hermes" aposentado.
- `sexta.status_events` criada no Postgres do leaf + role `sexta_app`
  (INSERT/SELECT, append-only provado).
- Hermes Agent v0.16.0 instalado NATIVO (C:\Users\User\AppData\Local\hermes).
- Sexta-feira conversando no **Telegram** (bot "Friday"), persona SOUL.md,
  allowlist 7318821830. Critério nº1 provado (no modelo grátis).
- Skills Hermes instaladas: `sexta-n8n` (n8n read-only), `sexta-status`
  (lê status_events), `sexta-rag` (AnythingLLM query).
- Bridges (C:\sexta-feira\bridges): n8n_client.py (read-only OK),
  db/status_reader.py (OK), rag/anythingllm_client.py (fiação OK; motor do
  AnythingLLM pendente — ver LEARNINGS).
- n8n MCP (build) acessível via host: C:\sexta-feira\callima\n8n_mcp.py.
- CALLIMA: validação estrutural feita; JSON corrigido em
  C:\sexta-feira\callima\CALLIMA_corrigido.json (fixes offline aplicados).

## EM ANDAMENTO  (← retomar aqui)
**Config nó-a-nó da CALLIMA via n8n MCP (update_workflow / setNodeCredential).**
Credenciais já criadas pelo fundador: Evolution ("Evolution account",
id tWl4eIzULkFUsVvg), Redis (criada — pegar ID), Postgres (criada — pegar ID).
PRÓXIMA AÇÃO IMEDIATA: rodar list_credentials p/ pegar IDs de Redis e Postgres,
e aplicar setNodeCredential:
  - Evolution (tWl4eIzULkFUsVvg) → Ler, Typing Indicator, Evolution1, Evolution2
  - Redis (id) → CRIAR LISTA MSG, BUSCA MSGS, APAGA MSG
  - Postgres (id) → Postgres Chat Memory
  - Anthropic (FmcBEbsrAPrHxSCG) → Analyze document (quick win)
Antes de aplicar: confirmar formato da op via inputSchema de update_workflow
(estava buscando isso em dump.py).

## PRÓXIMOS
- Aplicar fixes estruturais validados no Callima vivo (CODE1/Evolution1/Dados1,
  entrega humanizada, sessionKey memória) via update_workflow — mostrar ops antes.
- Buffer race guard (#4) + ramo de documento/Finalize Track (#5) — exigem teste runtime.
- Tools restantes: Stripe, Calendar, Gmail, HubSpot, WhatsAuto, ElevenLabs.
- test_workflow (pin data) → publicar Callima.
- Voltar à Sexta-feira: motor AnythingLLM (RAG), ponte Claude+MCP Gmail/Calendar
  com gate, Dashboard Orb, conversão das cascas (trigger gated).

## Pendências do fundador
- Rotacionar tokens expostos no chat: Telegram bot, n8n API key, n8n MCP token, AnythingLLM key.
- Definir billing (Claude/OpenAI) p/ sair do modo grátis.


---
## UPDATE (ckpt 0002) — 2026-06-10
- Credenciais ANEXADAS no Callima: Evolution (4 nós), Redis (3 nós), Anthropic (Analyze document). 8/8 atômico OK.
- PRÓXIMO: fundador criar credencial **Postgres** (host postgres / aistack_db / aistack_user / aistack123 / 5432) → anexar em `Postgres Chat Memory` + setar sessionKey=NUMERO_LEAD.
- Depois: aplicar fixes estruturais no Callima vivo (mostrar ops) + tools restantes (Stripe/Calendar/Gmail/HubSpot/WhatsAuto/ElevenLabs).
