# LEAF · Callima como Engrenagem — Padronização & Port (design)

> 2026-07-01. Aprovado pelo fundador: **transformar a Callima-n8n provada em engrenagem governada, multi-tenant automática, configurável por prompt** (Brann = **operador + editor**). RAG = **AnythingLLM workspace-por-tenant** atrás de Skill (pgvector = upgrade interno futuro). Fonte da verdade do comportamento = os dumps em `callima/leaf_dump/`.

## 0. Princípio da engrenagem
Uma base de código governada serve **todos** os tenants. Per-tenant = **estado, não código**:
- **config** (`agentProfile` expandido) · **credenciais** (cofre, resolvidas pela Boundary por `org_id`) · **conhecimento** (RAG por-tenant).

A engrenagem gira igual pra todo mundo; só o estado muda. Isso mata o clone-por-cliente e é o que faz virar SaaS. O dono **gira a engrenagem conversando com o Brann**; a engrenagem lê o estado do tenant e roda.

## 1. Catálogo de capacidades (nó n8n provado → Skill padrão do trunk)

| Capacidade | Skill (executorRef) | Risco | Efeito / Evidence | Fonte n8n (dump) | Estado no trunk |
|---|---|---|---|---|---|
| Ingerir mensagem | (webhook canal) | R1 | espelho Conversation/ChatMessage | `Webhook` + Evolution | ✅ existe |
| Debounce anti-runaway | (worker) | — | agrupa antes de responder | `ESPERA`+Redis | ✅ existe (brann-debouncer) |
| Responder texto | `leaf.reply.whatsapp` | R1 | send + `observed:` | `Callima` agent + `Gemini Brain` | ✅ existe |
| **Transcrever áudio (STT)** | `leaf.stt.transcribe` | R1 | `stt:transcribed:` | `OpenAI` transcribe | 🔨 novo (P1) |
| **Responder por voz (TTS)** | `leaf.reply.whatsapp.audio` | R1 | send-audio + `observed:` | `AUDIO FEM` (ElevenLabs) | 🔨 novo (P2) |
| **Recuperar conhecimento (RAG)** | `leaf.rag.retrieve` | R1 | chunks citáveis | `base_conhecimento_callima`→AnythingLLM | 🔨 novo (P3) |
| Enviar mídia | `leaf.send.media` | R1 | send + `observed:` | `ENVIAR MIDIA` (send-image) | 🔨 novo (blind) |
| Capturar lead | `lead.capture` | R1 | Lead + evento | `Parse/Save Lead`→`/ingest/lead` | ✅ existe (nativo) |
| **Agendar** | `leaf.appointment.book` | R3* | evento real + `/ingest/appointment` | `Parse Agendar`→Google Calendar | 🔨 novo (P4, cred Google por-tenant) |
| Enviar oferta / link Pix | `leaf.offer.send` / `payment.pix.link` | R1 | link real | `PIX` / `pix_link` | 🟡 parcial (offers ✅; pix novo) |
| E-mail transacional | `leaf.email.send` | R1 | envio Resend + audit | `Brann Actions Consumer` (Resend) | ✅ existe |
| **Handoff + alerta ao dono** | `leaf.handoff` | R1 | pausa IA + alerta + surface | `Intermediação Humana` (só pausa) | 🔨 novo (P5) |
| Multimodal (vídeo/doc) | `leaf.multimodal.understand` | R1 | entendimento | `Analyze video/document` (Gemini/Anthropic) | 🔜 fast-follow |

\* agendar = R3 se injeta credencial Google do tenant (HITL na 1ª conexão; execução recorrente é R1 sob mandato, padrão do WhatsApp connect).

**Regra de padronização:** no trunk, o `Route [switch 6 marcadores]` do n8n **deixa de ser switch de marcador** — vira **tool-calling do agente** (o LLM escolhe a Skill; cada efeito passa pela Boundary). Marcadores `[[LEAD]]/[[AGENDAR]]/[[AUDIO]]` são um hack de n8n que a governança substitui.

## 2. Schema de config per-tenant (`agentProfile` expandido)
O que o Brann escreve por tenant (tudo lido pela engrenagem em runtime):
- `agentName`, `businessName`, `persona` (extraInstructions) — ✅ existe
- `enabled` (ligar/desligar) — ✅ existe
- `voice`: `{ enabled, voiceId }` — TTS on/off + voz (🔨)
- `knowledge`: ref do workspace RAG do tenant + fontes (🔨)
- `offers`: [Offer] — ✅ existe
- `handoff`: `{ gatilhos, notifyChannels: [whatsapp|discord|email], notifyTarget }` (🔨)
- `connectedAccounts`: `{ whatsapp(instância Evolution), google(Calendar/Gmail), stripe }` — **refs**; segredos no cofre (🔨)
- `model`: **white-label-locked** (não editável pelo dono)

## 3. Catálogo de ferramentas do Brann (operador + editor)
Cada ferramenta = Skill pelo Boundary, com teto de risco. ADR 0004: o Brann opera um **allowlist** — "criar seleciona poder, não concede".

**EDITOR (escreve config per-tenant):**
- `configurar_callima` (nome/negócio/persona) — ✅ · `cadastrar_oferta` — ✅
- `adicionar_conhecimento` (cola texto/URL → workspace RAG do tenant) — 🔨
- `definir_voz` (liga TTS + escolhe voz) — 🔨 · `definir_handoff` (regras + canal de alerta) — 🔨

**OPERADOR (executa ação governada):**
- `conectar_whatsapp` (QR) — **R3 → HITL** · `conectar_google` (OAuth Calendar/Gmail do cliente) — **R3 → HITL**
- `ligar_callima` / `desligar_callima` — ato isolado (honest-data)
- `pausar_conversa` / `assumir_conversa` (handoff manual)

honest-data em tudo: a confirmação vem do **write/efeito real**, nunca do texto do LLM (padrão do "inteira").

## 4. RAG per-tenant (decisão travada)
- **Agora:** AnythingLLM com **1 workspace por tenant** (`workspace/<org_id>`), atrás da Skill `leaf.rag.retrieve`. Reusa o que já funciona, entrega rápido, isola por tenant.
- `adicionar_conhecimento` cria/atualiza o workspace do tenant (embed no AnythingLLM).
- **Depois (upgrade interno, invisível):** trocar o backend por **pgvector no trunk** mantendo a MESMA interface `leaf.rag.retrieve` — absorve o #13 (bruto/refinado/RAG) quando a governança/consolidação justificar.

## 5. Sequenciamento do port (por valor × risco) — Loop 2 revisado
- **P0 · Núcleo que já vende, agora config-driven per-tenant:** `leaf.reply.whatsapp` lê persona + conhecimento + ofertas do `agentProfile`/RAG do tenant (não mais hardcode). Base multi-tenant.
- **P1 · STT** (`leaf.stt.transcribe`) — entende áudio. *(era S1)*
- **P2 · TTS** (`leaf.reply.whatsapp.audio` + n8n `send-audio` cego) — responde por voz. *(S2)*
- **P3 · RAG per-tenant** (`leaf.rag.retrieve` + `adicionar_conhecimento`) — entende fundamentado. *(S3)*
- **P4 · Agenda** (`leaf.appointment.book`, Google por-tenant) — agenda de verdade.
- **P5 · Handoff + alerta** (`leaf.handoff`) — passa pro dono e avisa. *(S4)*
- **P6 · Brann operador** (conectar contas, definir_voz/handoff) — expande o catálogo de ferramentas.
- **Fast-follow:** multimodal (vídeo/doc), send-media extras, pgvector.

Cada P = 1 loop/PR do Fable, gate `build && typecheck && test` verde + teste da fatia + honest-data.

## 6. Guardrails (transversais, inegociáveis)
honest-data estrutural (efeito → prova → fala) · Boundary resolve credencial por-tenant (nunca solta) · dinheiro/credencial = R3 → HITL · Brann opera catálogo allowlisted (sem god-mode) · white-label (modelo escondido, não editável) · multi-tenant (org_id do token; cross-tenant ⇒ 404).

**Chaves de provider (Groq/ElevenLabs/OpenAI-embeddings) = COFRE, nunca `.env`.** São segredos governados (igual `openrouter_api_key` do M3-03): declaradas em `secretScopes` da Skill, injetadas pela Boundary por invocação, redigidas/auditadas/revogáveis. `.env` escaparia da redação (o redator do Boundary só protege o que está em `secretScopes`). O **model-router só NOMEIA o provider**; a chave vem do cofre. São chaves de **plataforma** (contas da Ginkgo, white-label) — provisionadas via `put-secret` no mesmo fluxo do `evolution_api_key`.

> Próximo: fundador revisa este doc → eu solto os prompts do Fable P0→P6, um por vez, com QA-gate a cada fatia.
