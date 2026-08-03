# Ginkgo — Handoff: feito / o que falta / logins / APIs / tarefas suas

## ✅ Feito (minha parte, sem gastar LLM)
- Callima (template WhatsApp): texto+áudio, anti-silêncio, lead memory, debounce — validado.
- ENVIAR MIDIA: redesenhado (send-image) e **validado no seu WhatsApp**.
- Email consumer (brann_actions→Resend): **testado, e-mail entregue**.
- Content Engine — LinkedIn (esqueleto, inativo) criado no n8n (id k82S6bzBEqtIU5ps).
- LEAF MVP (Claude Code): Tasks 1–7 + 6 fixes de segurança + 1ª suíte de testes + SETUP real.
- Credenciais ligadas: Supabase, Resend, Google Calendar, Gmail, Evolution, Gemini, Stripe.
- Docs de arquitetura: presença digital, content engine, design tokens, mídia, áudio, bridge,
  e o prompt do Claude Code p/ aplicar tokens no dashboard.

## ⏳ Pronto pra construir, MAS travado em algo seu (não é "minha parte" ainda)
- **Social Publisher** (brann_actions approved → Postiz) → preciso da **API key do Postiz** + confirmar a URL.
- **Ligar Content Engine** → preciso do **crédito OpenRouter** + **org_id da Ginkgo**.
- **Ponte n8n↔Supabase** (engine único: instance→org, agent_config) → faço junto da virada OpenRouter (precisa testar com LLM vivo).
- **Atomizador** (IG/Reels/X) → crédito OpenRouter + APIs de imagem/vídeo.
- **WhatsApp do Brann** → portfólio Meta BR.

## 🔑 LOGINS / CONTAS (você cria e me dá acesso/ID)
- [ ] **Postiz API key** — gerar em Settings do Postiz + confirmar URL (interna do docker).
- [ ] **Org "casa" da Ginkgo** no dashboard LEAF — cadastrar a própria Ginkgo (dogfooding) → me passar o `org_id`.
- [ ] **Meta Business BR** — novo portfólio (WhatsApp Cloud API) — só p/ WhatsApp do Brann (depois).
- [x] Resend ✅ · [x] Google OAuth (Calendar+Gmail) ✅ · [x] Evolution ✅ · [x] Supabase ✅.

## 💳 APIs / CRÉDITOS (pagos)
- [ ] **OpenRouter — crédito** 🔴 (o gate principal: acende Callima, Brann, Content Engine).
- [ ] **Imagem** — Nano Banana (você já tem key, **rotacionar**) e/ou Ideogram (carrossel c/ texto).
- [ ] **Vídeo/motion** — fal.ai (1 conta = vários modelos) + Creatomate ou JSON2Video (edição template). Fase de escala.
- [ ] **Música** (YouTube lofi) — Suno/Udio ou Epidemic Sound. Fase 2.
- [x] ElevenLabs ✅ · [x] Gemini ✅ · [x] Postiz (self-host) ✅ · [x] Resend ✅.

## 🔴 SUAS TAREFAS (humano, fora do código) — por prioridade
1. **Rotacionar chaves vazadas** (Supabase service_role, Google, OpenAI, Anthropic) nos dashboards.
2. **Crédito no OpenRouter** (destrava quase tudo).
3. **Criar org "casa" da Ginkgo** no dashboard → me mandar o org_id.
4. **Gerar API key do Postiz**.
5. **Unificar marca** (checklist handles/bio/logo/link; aposentar G-Tech).
6. **Aplicar design tokens**: colar o prompt do Claude Code (doc dashboard_tokens_e_marca) no dashboard.
7. (depois) Portfólio **Meta BR**; **CNPJ → OpenPix**.

## ▶️ O que EU faço assim que cada gate cair
- **OpenRouter** → virar Callima p/ OpenRouter, testar Content Engine, calibrar áudio emocional, fechar ponte n8n↔Supabase.
- **Postiz key + org Ginkgo** → construir Social Publisher (approved→Postiz) e ativar o Content Engine.
- **Meta BR** → WhatsApp do Brann.
- **Imagem/Vídeo** → Atomizador (IG/Reels/TikTok) reusando o mesmo Brief.

## Postiz — estado (2026-06-18, PAUSADO por decisão)
- Causa do "Failed to fetch": acesso por 127.0.0.1 (origem) → use sempre `localhost:5000`.
- Causa do 502: Postiz `latest` exige **Temporal** (7233). Adicionei serviço `temporal`
  (auto-setup → Postgres compartilhado) no compose + `TEMPORAL_ADDRESS=temporal:7233` no Postiz.
  Backup: `docker-compose.yml.bak-temporal`.
- Resultado: orchestrator + workers conectaram no Temporal OK; **backend ainda não sobe** por
  limite do Temporal SQL visibility: "cannot have more than 3 search attribute of type Text".
  → Postiz latest precisa de **Elasticsearch** (visibility avançada) OU pin de versão antiga.
- **Decisão: pausar.** `docker compose stop postiz temporal` (parados, reversível).
- Retomar quando construir o **Social Publisher** (= crédito OpenRouter): subir ES + start, ou pinar Postiz.
- Org "casa" Ginkgo criada: `6696c0e0-b24b-42cc-8595-83e42d530fbc` (já no Content Engine).
