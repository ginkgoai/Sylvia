---
title: "Ginkgo Core - Limitações do agente conversacional"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/68eb1cd8-9b6c-832a-8ea5-6d582978a6ab"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
dom., 12 de out. às 0:14

2

e esses

e aqui?

massa — esse “estúdio” aí é um catálogo de serviços 1-click. Vou te dizer **o que é cada um** que aparece nos cards e **se entra no MVP Leaf agora**.

## O que é cada card e quando usar

- **Evo IA**  
	Plataforma/API de WhatsApp (é a Evolution).  
	**Para o Leaf:** essencial pro Brann falar por WhatsApp.  
	**Status:** **instala agora**.
- **Firecrawl**  
	Crawler que pega conteúdo de um site/URL e devolve texto/JSON.  
	**Para o Leaf:** onboarding automático — puxa site do cliente e alimenta o RAG.  
	**Status:** **instala agora**.
- **Milvus**  
	Banco vetorial open-source de alta performance.  
	**Para o Leaf:** alternativa ao pgvector/Supabase para memória vetorial.  
	**Status:** opcional. Se já usa Supabase (pgvector), pode **pular** por enquanto.
- **Ollama**  
	Servidor para rodar **modelos locais** (Llama, Mistral, etc.).  
	**Para o Leaf:** útil para POCs/offline, mas o MVP prioriza OpenAI/Gemini.  
	**Status:** **opcional** (não bloqueia nada).
- **OpenWebUI**  
	UI de chat para falar com modelos (inclui RAG básico).  
	**Para o Leaf:** redundante com Flowise.  
	**Status:** **pula** no MVP.
- **Zep**  
	“Long-term memory” (vetorial + memória conversacional) com API.  
	**Para o Leaf:** alternativa ao seu stack RAG.  
	**Status:** opcional. Você já tem Supabase + Flowise.
- **Botpress**  
	Plataforma de chatbots low-code.  
	**Para o Leaf:** não precisa (Flowise já cumpre esse papel).  
	**Status:** **pula**.
- **Mago-IA** (provavelmente *Mage-AI*)  
	Orquestrador de dados/ETL para pipelines.  
	**Para o Leaf:** você já usa **n8n** como esteira.  
	**Status:** **pula**.
- **Kokoro**  
	Servidor/modelo de **TTS** (voz sintética).  
	**Para o Leaf:** dá para baratear TTS do Brann, mas ElevenLabs/OpenAI TTS é mais plug-and-play.  
	**Status:** **opcional** (coloque depois, se quiser TTS self-hosted).
- **Caixa de entrada zero**  
	Ferramenta de gerenciamento de e-mail.  
	**Para o Leaf:** não é core.  
	**Status:** **pula**.
- **Parafuso / Faça Você Mesmo (Bolt DIY)**  
	Parece um gerador de apps com IA “faça-você-mesmo”.  
	**Para o Leaf:** desnecessário agora.  
	**Status:** **pula**.
- **Argilla** (na outra aba “Ferramentas de IA”)  
	Plataforma de **rotulagem/feedback** de dados para melhorar modelos.  
	**Para o Leaf:** ótimo para fase 2 (treinar respostas, curadoria de RAG).  
	**Status:** **legal mais pra frente**.

---

## Meu kit mínimo para o MVP (nessa tela)

1. **Evo IA (Evolution)** — canal WhatsApp do Brann.
2. **Firecrawl** — ingestão automática do site do cliente.
3. **(Opcional) Milvus** — só se você **não** for usar Supabase/pgvector.
4. **(Opcional) Kokoro** — se quiser TTS self-hosted (senão, ElevenLabs/OpenAI via n8n).

> O resto você já resolve com: **Flowise + n8n + Supabase + Stripe + Lovable + Notion/Pipefy + Sentry**.

---

## Ligações rápidas (como encaixa)

- **Onboarding**: Lovable → n8n → **Firecrawl** (pega site) → Flowise RAG (Supabase ou Milvus).
- **Atendimento**: Brann (Flowise) → **Evo IA** (WhatsApp) via n8n/tools.
- **Voz (opcional)**: Brann → n8n → **Kokoro** /ElevenLabs → Evo IA (áudio).
- **Memória**: Supabase pgvector (ou Milvus se preferir gerenciar vetorial dedicado).

Quer que eu te passe os **webhooks n8n** prontos para integrar **Firecrawl → RAG** e **Evo IA** agora (payloads de exemplo e validações)?

Adiciona kokoro evo ia e firecrawl, esses eu te mostrei foram os que vi, tem algum outro que lembre? Para instalar no easypanel

bora! 👇 vou montar o **kit de serviços pra instalar no EasyPanel** começando pelos três que você citou e, em seguida, os “extras” que dão estabilidade, segurança e superpoder pro Leaf.

---

## Instale já (core do MVP)

### 1) Evo IA (WhatsApp)

- **Pra quê:** canal do Brann (texto, mídia e áudio).
- **No EasyPanel:** clique no card *Evo IA* e siga o wizard.
- **Como ligar:** no n8n crie `POST /wa/in` (entrada) e `POST /leaf/send-whatsapp` (saída).  
	No Flowise, adicione uma **HTTP Tool** apontando pro n8n.

### 2) Firecrawl

- **Pra quê:** onboarding automático → varre o site do cliente e gera conteúdo limpo pra RAG.
- **No EasyPanel:** card *Firecrawl*.
- **Como ligar:** n8n `POST /leaf/ingest` chama Firecrawl, normaliza e grava no seu vetor store (Supabase pgvector ou Milvus).  
	O Brann passa a ter contexto do cliente em minutos.

### 3) Kokoro (TTS self-hosted)

- **Pra quê:** voz do Brann barata/offline.
- **Como ligar:** n8n `POST /leaf/send-voice` → Kokoro (gera áudio) → envia via Evo IA.  
	No Flowise, exponha uma **HTTP Tool** `SEND_VOICE_REPLY`.

> Dica: mantenha também **OpenAI/ElevenLabs** como *fallback* de TTS; às vezes vale pela latência/estabilidade.

---

## Mais 8 que valem ouro (eu instalaria agora)

1. **Qdrant** *(ou Milvus, se você preferir)*
	- **Pra quê:** banco vetorial dedicado (mais simples que Milvus).
		- **Como ligar:** n8n upserta embeddings; Flowise usa retriever via HTTP/SDK.
		- Se já estiver confortável com **Postgres+pgvector**, pode adiar.
2. **Uptime-Kuma**
	- **Pra quê:** monitorar todos os webhooks (Flowise/n8n/Evo/Firecrawl).
		- Alerta rápido quando algo cai.
3. **GlitchTip** *(alternativa open-source ao Sentry)* ou **Sentry** SaaS
	- **Pra quê:** rastrear erros de fluxo e exceptions nos webhooks do n8n.
		- Integre o DSN nos seus nodes HTTP.
4. **Traefik** (ou **Caddy**) como reverse proxy com TLS/Rate-Limit
	- **Pra quê:** HTTPS, regras, *rate-limit* e cabeçalhos de segurança.
		- Coloque tudo atrás dele (Flowise, n8n, Evo, Kokoro, Firecrawl).
5. **oauth2-proxy** (ou **Authentik** se quiser IdP completo)
	- **Pra quê:** proteger painéis (Flowise/n8n/Uptime) com login Google/GitHub.
		- Uma camada de auth > password fraca exposta.
6. **MinIO** (S3 compatível)
	- **Pra quê:** mídia da Nyra (imagens/vídeos) e áudios do Brann.
		- Alternativa se não usar Supabase Storage.
7. **Healthchecks** (ou self-hosted *healthchecks/healthchecks*)
	- **Pra quê:** “ping” de jobs do Alphie (rotinas diárias/semanais) — se não pingar, alerta.
8. **FFmpeg** (container `jrottenberg/ffmpeg` em job/sidecar)
	- **Pra quê:** conversão de áudio (MP3 → OGG/OPUS) quando o Whats exigir formatos específicos.

---

## Mapa de ligação (mental map rápido)

```markdown
[Lovable] --(POST /onboarding)--> [n8n] --> cria customer/agents + Firecrawl --> [Qdrant/pgvector]
                                              ↘ envia arte inicial (Nyra) --> [MinIO/Supabase Storage]

[Evo IA] --(webhook /wa/in)--> [n8n] --> chama [Flowise/Brann] --> decide tools
                                     ↘ SEND_WHATSAPP / SEND_VOICE --> [Evo IA]

[Flowise/Brann] <--> [Retriever: Qdrant/pgvector] (namespace = customer_id)

[Alphie cron n8n] --> métricas/logs --> [GlitchTip/Sentry, Healthchecks] + [Notion/Pipefy]
```

**Tudo** publicado por trás do **Traefik/Caddy** com TLS e rate-limit, e **oauth2-proxy** nas rotas de admin.

---

## Ordem de instalação (sem stress)

1. **Traefik/Caddy** (proxy + TLS)
2. **Uptime-Kuma** e **GlitchTip/Sentry** (ver o mundo)
3. **Evo IA** (canal)
4. **Flowise** + **n8n** (cérebro + braços)
5. **Qdrant** *(ou pgvector que você já tem no Postgres)*
6. **Firecrawl** (ingestão)
7. **Kokoro** (voz) + **FFmpeg**
8. **MinIO** (se precisar de S3)
9. **oauth2-proxy** (travar os painéis)

---

## Checks de “deu boa”

- Evo IA gera **QR** e recebe/envia mensagens.
- `/onboarding` no n8n cria **customer**, dispara Firecrawl e popula o vetor store.
- Brann responde com RAG por `customer_id` e chama `LEAD_CREATE` / `SEND_WHATSAPP`.
- `SEND_VOICE_REPLY` toca áudio normal no Whats.
- Uptime-Kuma mostra tudo **verde**; GlitchTip/Sentry sem exceções.

---

## Extras que você pode considerar depois

- **Apify** (rastreamento avançado quando o site do cliente é chato).
- **Notion & Pipefy**: são SaaS, só configurar a integração (não precisam instalar).
- **MCP Bridge + Servers** (comms/docs/crm/memory) — se quiser padronizar tool-calls entre Flowise e n8n.

---

quer que eu te passe um **arquivo de serviços** (compose) com Traefik, Uptime-Kuma, GlitchTip, Evo, Qdrant, Firecrawl, Kokoro e FFmpeg já definidos pra colar no EasyPanel/Stacks?

Sim

perfeito — segue um **stack Compose base** pra colar no EasyPanel (Stacks) com o esqueleto dos serviços que combinamos. Eu priorizei **segurança (Traefik + TLS + rate-limit)** e **observabilidade (Uptime-Kuma + GlitchTip)**, e deixei tudo em duas redes (web e interna). Onde houver variáveis, estão com `PLACE_…` pra você preencher.

> Observação sincera: **Kokoro** e **Firecrawl** variam conforme imagem escolhida no catálogo do EasyPanel. Coloquei entradas funcionais com placeholders; se instalar por “card 1-click”, pode **remover** as seções correspondentes do compose e só apontar os URLs/portas nos seus webhooks.

---

## docker-compose.yml (cola no EasyPanel ▶ Stacks)

```markdown
version: "3.9"

networks:
  web:
    external: false
  internal:
    external: false

volumes:
  traefik_acme: {}
  kuma_data: {}
  glitchtip_data: {}
  evo_data: {}
  qdrant_data: {}
  kokoro_cache: {}

services:
  # ─────────────────────────────────────────────────────────────
  # REVERSE PROXY + TLS + RATE LIMIT
  # ─────────────────────────────────────────────────────────────
  traefik:
    image: traefik:v2.10
    command:
      - --providers.docker=true
      - --providers.docker.exposedbydefault=false
      - --entrypoints.websecure.address=:443
      - --certificatesresolvers.cf.acme.tlschallenge=true
      - --certificatesresolvers.cf.acme.email=${CF_EMAIL}
      - --certificatesresolvers.cf.acme.storage=/acme/acme.json
      # middlewares (rate limit + headers)
      - --api.dashboard=true
    ports:
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - traefik_acme:/acme
    environment:
      CF_DNS_API_TOKEN: ${CF_TOKEN}
    networks: [ web ]
    labels:
      - traefik.enable=true
      # Protege o dashboard com basic auth (opcional – troque o hash)
      - traefik.http.routers.traefik.rule=Host(\`${TRAEFIK_HOST}\`)
      - traefik.http.routers.traefik.service=api@internal
      - traefik.http.routers.traefik.entrypoints=websecure
      - traefik.http.routers.traefik.tls.certresolver=cf
      - traefik.http.middlewares.sec-headers.headers.stsSeconds=31536000
      - traefik.http.middlewares.sec-headers.headers.stsIncludeSubdomains=true
      - traefik.http.middlewares.sec-headers.headers.contentTypeNosniff=true
      - traefik.http.middlewares.rate.limit.average=30
      - traefik.http.middlewares.rate.limit.burst=60

  # ─────────────────────────────────────────────────────────────
  # UPTIME-KUMA (monitoramento)
  # ─────────────────────────────────────────────────────────────
  uptime-kuma:
    image: louislam/uptime-kuma:1
    volumes:
      - kuma_data:/app/data
    networks: [ web ]
    labels:
      - traefik.enable=true
      - traefik.http.routers.kuma.rule=Host(\`${KUMA_HOST}\`)
      - traefik.http.routers.kuma.entrypoints=websecure
      - traefik.http.routers.kuma.tls.certresolver=cf
      - traefik.http.routers.kuma.middlewares=sec-headers@docker

  # ─────────────────────────────────────────────────────────────
  # GLITCHTIP (erros/telemetria) – usa PostgreSQL e Redis existentes
  # ─────────────────────────────────────────────────────────────
  glitchtip:
    image: glitchtip/glitchtip:latest
    environment:
      SECRET_KEY: ${GLITCHTIP_SECRET}
      DATABASE_URL: ${GLITCHTIP_DATABASE_URL}   # ex: postgres://user:pass@host:5432/glitchtip
      REDIS_URL: ${GLITCHTIP_REDIS_URL}         # ex: redis://redis:6379/0
      DEFAULT_FROM_EMAIL: ${GLITCHTIP_FROM}
      EMAIL_URL: ${GLITCHTIP_EMAIL_URL}         # ex: smtp://user:pass@mailhost:587
      GLITCHTIP_DOMAIN: ${GLITCHTIP_HOST}
    depends_on: []
    networks: [ web, internal ]
    labels:
      - traefik.enable=true
      - traefik.http.routers.glitch.rule=Host(\`${GLITCHTIP_HOST}\`)
      - traefik.http.routers.glitch.entrypoints=websecure
      - traefik.http.routers.glitch.tls.certresolver=cf
      - traefik.http.routers.glitch.middlewares=sec-headers@docker
    # primeira vez rode 'python manage.py migrate' (veja pós-instalação)

  # ─────────────────────────────────────────────────────────────
  # EVOLUTION API (WhatsApp do Brann)
  # ─────────────────────────────────────────────────────────────
  evo:
    image: atendai/evolution-api:latest
    environment:
      # Ajuste conforme sua distro da Evolution
      SERVER_URL: https://${EVO_HOST}
      AUTHENTICATION_TOKEN: ${EVO_API_KEY}
      # DB: por padrão usa SQLite local; se quiser Postgres, configure aqui
      # DATABASE_URL: ${EVO_DATABASE_URL}
      # STORAGE_DIR para arquivos temporários
    volumes:
      - evo_data:/evolution
    networks: [ web, internal ]
    labels:
      - traefik.enable=true
      - traefik.http.routers.evo.rule=Host(\`${EVO_HOST}\`)
      - traefik.http.routers.evo.entrypoints=websecure
      - traefik.http.routers.evo.tls.certresolver=cf
      - traefik.http.routers.evo.middlewares=sec-headers@docker,rate@docker
      - traefik.http.middlewares.rate.limit.average=50
      - traefik.http.middlewares.rate.limit.burst=100

  # ─────────────────────────────────────────────────────────────
  # QDRANT (vetor store)
  # ─────────────────────────────────────────────────────────────
  qdrant:
    image: qdrant/qdrant:latest
    networks: [ internal, web ]
    volumes:
      - qdrant_data:/qdrant/storage
    labels:
      - traefik.enable=true
      - traefik.http.routers.qdrant.rule=Host(\`${QDRANT_HOST}\`)
      - traefik.http.routers.qdrant.entrypoints=websecure
      - traefik.http.routers.qdrant.tls.certresolver=cf
      - traefik.http.routers.qdrant.middlewares=sec-headers@docker
    # se preferir manter Qdrant só na rede interna, remova as labels e expose internamente

  # ─────────────────────────────────────────────────────────────
  # FIRECRAWL (self-host) – preencha variáveis; ou remova se usar 1-click
  # ─────────────────────────────────────────────────────────────
  firecrawl:
    image: ghcr.io/mendableai/firecrawl:latest
    environment:
      PORT: 3002
      LOG_LEVEL: info
      OPENAI_API_KEY: ${OPENAI_API_KEY}
      # Firecrawl precisa de DB + Redis. Use os que já tem:
      DATABASE_URL: ${FIRECRAWL_DATABASE_URL}  # ex: postgres://user:pass@host:5432/firecrawl
      REDIS_URL: ${FIRECRAWL_REDIS_URL}        # ex: redis://redis:6379/2
      # se usar chave SaaS, FIRECRAWL_API_KEY=... (opcional)
    networks: [ web, internal ]
    labels:
      - traefik.enable=true
      - traefik.http.routers.firecrawl.rule=Host(\`${FIRECRAWL_HOST}\`)
      - traefik.http.routers.firecrawl.entrypoints=websecure
      - traefik.http.routers.firecrawl.tls.certresolver=cf
      - traefik.http.routers.firecrawl.middlewares=sec-headers@docker

  # ─────────────────────────────────────────────────────────────
  # KOKORO TTS (self-host) – substitua a imagem pela que o EasyPanel oferece
  # ─────────────────────────────────────────────────────────────
  kokoro:
    image: ghcr.io/hexgrad/kokoro-tts-server:latest   # ajuste para a imagem do seu catálogo
    environment:
      PORT: 8020
      # configure modelos/idiomas conforme a imagem escolhida
    networks: [ web, internal ]
    labels:
      - traefik.enable=true
      - traefik.http.routers.kokoro.rule=Host(\`${KOKORO_HOST}\`)
      - traefik.http.routers.kokoro.entrypoints=websecure
      - traefik.http.routers.kokoro.tls.certresolver=cf
      - traefik.http.routers.kokoro.middlewares=sec-headers@docker
    volumes:
      - kokoro_cache:/cache

  # ─────────────────────────────────────────────────────────────
  # FFmpeg util (para jobs de conversão via docker exec / sidecar)
  # ─────────────────────────────────────────────────────────────
  ffmpeg:
    image: jrottenberg/ffmpeg:6.1-ubuntu
    command: ["-version"]
    networks: [ internal ]
    # use via \`docker run --rm --network=<stack> jrottenberg/ffmpeg ...\`
```

---

## .env (exemplo mínimo)

```markdown
# Cloudflare (Traefik)
CF_EMAIL=seu-email@dominio.com
CF_TOKEN=PLACE_CLOUDFLARE_API_TOKEN

# Hosts públicos (subdomínios)
TRAEFIK_HOST=proxy.seudominio.com
KUMA_HOST=uptime.seudominio.com
GLITCHTIP_HOST=errors.seudominio.com
EVO_HOST=wa.seudominio.com
QDRANT_HOST=qdrant.seudominio.com
FIRECRAWL_HOST=crawl.seudominio.com
KOKORO_HOST=tts.seudominio.com

# GlitchTip
GLITCHTIP_SECRET=PLACE_SUPER_SECRET
GLITCHTIP_DATABASE_URL=postgres://user:pass@postgres_host:5432/glitchtip
GLITCHTIP_REDIS_URL=redis://redis_host:6379/1
GLITCHTIP_FROM=ops@seudominio.com
GLITCHTIP_EMAIL_URL=smtp://usuario:senha@smtp.seudominio.com:587

# Evolution API
EVO_API_KEY=PLACE_EVO_TOKEN

# Firecrawl
OPENAI_API_KEY=PLACE_OPENAI
FIRECRAWL_DATABASE_URL=postgres://user:pass@postgres_host:5432/firecrawl
FIRECRAWL_REDIS_URL=redis://redis_host:6379/2
```

---

## Pós-instalação (checklist rápido)

1. **DNS** → crie os subdomínios no Cloudflare apontando para sua VPS.
2. **Suba o stack** → no EasyPanel, Stack ▶ Deploy.
3. **Evolution** → acesse `https://wa.seudominio.com`, crie **instância** e gere o **QR**; pareie o WhatsApp Business.
4. **GlitchTip**
	- Rode migrações (uma vez):
		```markdown
		docker compose exec glitchtip python manage.py migrate
		docker compose exec glitchtip python manage.py createsuperuser
		```
		- Cole o DSN do GlitchTip nos seus webhooks do n8n/Flowise.
5. **Qdrant** → crie a collection `leaf_${customer_id}` (ou deixe o n8n criar on-demand).
6. **Firecrawl** → teste `GET https://crawl.seudominio.com/health`. Configure seu n8n `/leaf/ingest` para chamar `POST /crawl` e gravar no vetor store.
7. **Kokoro** → confirme a rota `https://tts.seudominio.com/health` (ou a rota que a imagem fornecer). Ligue no n8n `POST /leaf/send-voice`.
8. **Uptime-Kuma** → adicione monitores de: `wa`, `crawl`, `tts`, `qdrant`, seus webhooks do n8n e os endpoints do Flowise.

---

## Por que esse arranjo funciona

- **Traefik** garante HTTPS e *rate-limit* em tudo.
- **Uptime-Kuma + GlitchTip** te dizem *quando* e *onde* quebrou.
- **Evolution** é o canal do Brann; **Kokoro** dá voz; **FFmpeg** resolve formatos.
- **Firecrawl** alimenta o cérebro (RAG) automaticamente.
- **Qdrant** é o vetor store dedicado (ou use seu pgvector atual).

---

### Dicas finais de segurança

- Proteja painéis (`uptime`, `glitchtip`, `proxy`) atrás de **Cloudflare Access** ou **oauth2-proxy** (se quiser te passo um middleware pronto).
- Habilite **rate limit** por rota no Traefik (já deixei um padrão).
- Ative **assinatura de webhooks** (Stripe/Evolution/Lovable) e **idempotência** no n8n.

Se quiser, eu te mando também os **endpoints do n8n** (JSON de import) que conversam com esses serviços:  
`/wa/in`, `/leaf/send-whatsapp`, `/leaf/send-voice`, `/leaf/ingest`, `/alphie/report-weekly`.