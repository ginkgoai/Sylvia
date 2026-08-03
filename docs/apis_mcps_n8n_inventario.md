# Ginkgo — Inventário de APIs, MCPs e fluxos n8n (plataforma inteira)

Status: ✅ temos · 🟡 precisa configurar/creditar · 🔴 falta contratar · 👤 ação do founder.
Tudo passa pelo **Provider Router** (aiGateway/tokenRouter) — provedor escondido do usuário,
debita GTK. Fonte: `tokenizacao_arquitetura.md`, `suite_arquitetura_spec.md`.

## 1. Núcleo compartilhado (infra + IA core)
- **Supabase** (DB/Auth/Storage) ✅ · **Redis** (estado) ✅ · **n8n** (orquestração) ✅
- **Stripe** (billing USD + Connect) 🟡 configurar USD/global 👤
- **OpenRouter** (gateway LLM multi-modelo: Gemini/GPT/Claude…) 🟡 creditar 👤
- **Embeddings + pgvector** (RAG): provedor de embedding (OpenAI/Voyage/Cohere via OpenRouter)
  + extensão pgvector no Supabase 🟡
- **ASR/transcrição** (áudio/multimodal-in): Whisper (OpenAI) ou Groq/faster-whisper 🟡
- **E-mail transacional** (recibos, alertas): Resend ou AWS SES 🔴
- **Observabilidade/logs**: já há Datadog no ambiente; mínimo = logs estruturados ✅/🟡

## 2. Leaf / Callima (atendimento)
- **WhatsApp**: Evolution (não-oficial, hoje) ✅ → **WhatsApp Cloud API (Meta)** 🔴👤 (portfólio Meta)
- **Canais extras** (depois): Instagram Graph API, Messenger (mesmo portfólio Meta) 🔴👤
- **TTS**: ElevenLabs ✅ · **ASR**: Whisper 🟡 · **Multimodal** (imagem/doc): Gemini via OpenRouter 🟡
- **Google Calendar API** (agendamento) 🟡 (criar OAuth) 👤
- **Pagamento no chat**: Stripe (links) ✅ · Pix add-on BR: OpenPix/Asaas 🔴👤 (v2)

## 3. Pyre / Nyra (conteúdo)
- **Imagem**: Flux via **fal.ai** (ou Replicate/BFL) 🔴 · Ideogram/MJ (MJ sem API oficial) opcional
- **Vídeo**: **Seedance** / Kling / Runway / Luma 🔴 · **Avatar: HeyGen API** 🔴
- **Voz**: ElevenLabs ✅
- **Clips** (vídeo→shorts): ffmpeg (self-host) + Whisper (legenda) + LLM (highlights) 🟡
- **Tendências/Radar**: Bright Data / Nimble (no ambiente) ✅ · YouTube Data API 🔴👤 · X/TikTok opcional
- **Publicação**: Postiz ✅ (precisa fix Elasticsearch 🟡) → IG/FB/X/LinkedIn/TikTok/YouTube (tokens no Postiz)

## 4. Wave / Alfred (tráfego)
- **Meta Marketing API** (ler/gerir campanhas + Conversions API/CAPI) 🔴👤 (portfólio Meta)
- **Google Ads API** + **TikTok Marketing/Events API** 🔴👤 (depois do Meta)
- **Atribuição**: interna (usa `payments` + `leads`) ✅
- **Verba de mídia**: Modelo A = conta do cliente (sem API extra) · Modelo B = billing central (v2)

## 5. Espinha / governança (Sexta-feira · Brann · Hermes/Laplace)
- **LLM** (OpenRouter) ✅🟡 · **n8n** ✅ · **brann_actions/HITL** (interno) ✅
- **Alertas**: WhatsApp (Evolution/Cloud) ✅ · Discord (ginkgo-discord) ✅ · e-mail 🔴
- **Agendados** (briefings/monitor): n8n schedules ✅

## 6. MCPs (interface de ferramentas dos agentes)
- **MCP interno Ginkgo** (expõe leads/CRM/mídia/saldo GTK aos agentes, com governança) 🔴 (construir)
- **MCP Meta Ads / TikTok Ads** (wrapper das APIs de anúncio p/ o Alfred) 🔴
- **MCP web/tendências**: Bright Data / Nimble ✅ (já no ambiente)
- Provedores de geração (fal/HeyGen/ElevenLabs) entram via Provider Router (HTTP direto), não
  precisam ser MCP — MCP só onde o padrão de "ferramenta" ajuda (dados internos, contas conectadas).

## 7. Fluxos n8n por corpo
- **Leaf/Callima**: inbound (recebe WA→processa→responde) ✅ · ENVIAR MIDIA ✅ · AUDIO/TTS ✅ ·
  lead persistente ✅ · follow-up · handoff/alerta HITL · (novo) ingest WhatsApp Cloud API.
- **Pyre/Nyra**: Content Engine (Planner→Core→Atomizador→Asset→HITL→Postiz→Feedback) 🟡 (esqueleto
  LinkedIn feito) · pipelines de geração (imagem/vídeo/avatar→fal/Seedance/HeyGen) 🔴 ·
  ingest de Trends 🔴 · polling de Radar 🔴.
- **Wave/Alfred**: pull de gasto/métricas (schedule) 🔴 · sync de atribuição (lead won+payment→
  campanha) 🔴 · dispatch CAPI 🔴 · recomendações de otimização→HITL 🔴.
- **Cross**: webhooks Stripe (billing/top-up) 🔴 · webhooks Meta (messages/template status) 🔴 ·
  callbacks de provedores · hooks de débito GTK/governança.

## 8. Ação do founder (contas/chaves a criar) 👤
Meta (portfólio: WhatsApp Cloud + Marketing API + IG/Messenger) · OpenRouter (crédito) ·
Stripe (USD/global) · fal.ai · HeyGen · Seedance (ou alternativa de vídeo) · YouTube Data API ·
Google Cloud (Calendar OAuth) · Resend/SES (e-mail) · (v2) OpenPix/Asaas, Google/TikTok Ads.

## 9. Caminho crítico (o que destrava mais)
1. **OpenRouter (crédito)** → liga Callima + todo o compute. 2. **Portfólio Meta** → WhatsApp
oficial + Wave. 3. **Stripe USD** → billing/GTK. 4. **fal.ai + HeyGen** → Pyre Estúdio.
5. **Postiz/ES** → publicação do Pyre. Embeddings/pgvector → RAG melhor (não bloqueia v1).
