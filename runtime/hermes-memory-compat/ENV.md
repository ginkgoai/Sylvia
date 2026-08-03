# ENV — fatos do ambiente (sem segredos)

## Máquina / paths
- SO: Windows + Docker Desktop. Projeto em **C:\sexta-feira** (sem espaços).
- Stack leaf (compose): `C:\Users\User\OneDrive\Área de Trabalho\G-Tech\Administração Interna\GITS FONTE\compose stack`
- Hermes nativo: `C:\Users\User\AppData\Local\hermes` (HERMES_HOME). Python venv:
  `C:\Users\User\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe`
- Skills Hermes: `%LOCALAPPDATA%\hermes\skills\` (sexta-n8n, sexta-status, sexta-rag).

## Serviços (rede docker `ai-stack`; host = localhost)
- n8n: host `localhost:5678` | interno `n8n:5678`
- evolution-api: host `localhost:8080` | interno `evolution-api:8080`
- anythingllm: host `localhost:3001` | interno `anythingllm:3001`
- postgres: host `localhost:5432` | interno `postgres:5432` (db aistack_db)
- redis: host `localhost:6379` | interno `redis:6379` (DBs: 0=BullMQ,1=Hermes,3=Callima,6=Evolution)

## n8n MCP (build-time, dirigido pelo host)
- Endpoint: `http://localhost:5678/mcp-server/http` (Streamable HTTP, JSON-RPC).
- Cliente local: `C:\sexta-feira\callima\n8n_mcp.py` (uso: `tools` | `call <tool> '<json>'`).
- Token em `C:\sexta-feira\callima\.n8n_mcp.token` (gitignored).
- NÃO conecta como conector do Claude (exige https+OAuth; http+token rejeitado).

## Credenciais n8n (nomes/IDs — segredos só no n8n)
- OpenRouter account — openRouterApi — `XxZ9pd0yUms0f8w7`
- Anthropic account — anthropicApi — `FmcBEbsrAPrHxSCG`
- Google Gemini(PaLM) — googlePalmApi — `Y0O7MUreBOYQ3yC8`
- OpenAI account — openAiApi — `G3zMpqV7Jywx5YTw`
- Evolution account — evolutionApi — `tWl4eIzULkFUsVvg`
- Redis Callima — redis — (PEGAR ID via list_credentials)
- Postgres — postgresql — (PEGAR ID)

## Workflows n8n
- CALLIMA — id `zo9FqQ9XVRcU8AJZ` (active:false). Nó de dados = `Dados1`
  (campos: INSTANCIA, NUMERO_LEAD, MENSAGEM, MENSAGEM_TIPO, fromMe, message_id, APIKEY...).
- Sub-workflow áudio "AUDIO BRANN" — id `8EoLKO7wdhv0ZLgz`.

## Sexta-feira (Hermes)
- Telegram bot "Friday"; allowed user id `7318821830`.
- Provider atual: Nous Portal (grátis) modelo `nvidia/nemotron-3-ultra:free`.
- DB role leitura: `sexta_app` (senha em C:\sexta-feira\.sexta_db_pw.txt).
- status_events: schema `sexta`, tabela `status_events` (append-only).
