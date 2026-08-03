# Auditoria ginkgo-tree (Fable) × leaf — e o casamento

## Descoberta principal
Temos DUAS implementações do MESMO produto, em fundações diferentes:

### A) ginkgo-tree (Fable) — o KERNEL/OS governado (o motor feito CERTO)
- `@ginkgo/core`: máquina de estados de Task + `resolveSkill` determinístico + TaskRunner. **REAL, 77/77 testes.**
- `@ginkgo/boundary`: Security Boundary de 8 passos (cofre AES-256-GCM, executor_ref HMAC, redação,
  VaultAccess). **REAL.** (segredo nunca toca Core/LLM/.env)
- `@ginkgo/db`: Prisma + Postgres + **pgvector**; 17 tabelas: Tenant/User/Membership/Task/Event/
  Evidence/TokenWallet/**TokenLedger (HOLD/SETTLEMENT/PURCHASE/GRANT)**/SkillRegistry/Secret/
  VaultAccess/Policy/BillingEvent + LEAF Conversation/ChatMessage/AgentProfile/AgentSend.
- **Economia de tokens REAL** (reserva/liquidação atômica, HOLD em CLASSIFIED, SETTLEMENT em COMMITTED)
  — é o nosso modelo GTK, já construído e testado.
- **HITL REAL** (R3 bloqueia com saldo retido, approve/reject serializável, resume lê decisão congelada).
- **WhatsApp LEAF REAL** (connect→espelho→**BRANN responde com LLM** via n8n executor cego + Evolution +
  confirmador independente). e2e ao vivo. Falta só o fundador parear um número real.
- **Stripe recarga de tokens REAL** (modo teste).
- Front Next.js 14: dashboard + inbox LEAF (3 colunas) + Financeiro + tasks/lineage + auth + landings.
  **PYRE/WAVE = shells honestos.**
- Docker compose (pg+pgvector/redis/n8n/api/worker/web/evolution/anythingllm/minio) — **imagens buildam
  e sobem** (provado em sessões passadas). Stack hoje parada.
- Governança: 9 invariantes, **Laplace** (plano de governança, sem cognição), **Hermes** (mente única),
  personas Brann/Callima/Nyra/Alfred/Shion, escada de maturidade, ADRs (produto unificado etc.).
- Gaps honestos (do próprio PRD): **UI/UX precisa polir** (apontado pelo fundador), PYRE/WAVE, RAG
  (pgvector ligado mas sem embeddings), assinaturas, MCP (só docs), event-bus real.

### B) leaf (o repo desta sessão) — o PRODUTO/UX polido, em fundação diferente
- Next.js 16 + **Supabase (GoTrue + RLS)** + Fastify, módulos convencionais (inbox, crm/leads, agents,
  billing, media, payments, scheduling, brann actions, ragEngine, aiGateway/tokenRouter, hitlManager).
- O que construímos nesta sessão: **Suite Shell + App Switcher**, **Inbox 3-pane**, **Kanban**, config
  da **Callima**, upload de KB, pricing — UX forte.
- NÃO tem o Kernel/Boundary/Evidence/Skills governados. Auth/DB diferentes (Supabase RLS, não JWT+Prisma).

## A tensão (honesto)
Estamos, em parte, **construindo duas vezes**: Inbox/Kanban/Shell que fizemos no repo `leaf`
(Supabase) já existem (Inbox/dashboard) ou são o gap (Kanban) no ginkgo-tree — só que o
ginkgo-tree tem a parte DIFÍCIL e CORRETA (Kernel/Boundary/tokens/HITL/WhatsApp) já testada.

## Recomendação: ginkgo-tree = TRONCO canônico; leaf = doador de UX
Motivos:
1. O que é **insubstituível** (Kernel governado, Security Boundary, ledger HOLD/SETTLEMENT,
   Evidence, loop WhatsApp/BRANN REAL e testado) vive no ginkgo-tree, 77/77 + e2e. Não se reconstrói.
2. O gap nº1 do ginkgo-tree é exatamente **UI/UX** + **Kanban/CRM** — que é o forte do `leaf`.
3. Logo: **portar a UX do leaf** (Suite Shell, App Switcher, Inbox polido, Kanban, config Callima,
   /pricing) para o **apps/web (Next 14) do ginkgo-tree**, ligada à API governada dele.
   A partir daí, **construir no ginkgo-tree** — não no leaf-Supabase.
4. As specs que escrevemos (Shell/Kanban/Pricing-GTK) viram guia de UX; o backend já existe no tronco
   (ledger de tokens = GTK; HITL = "Assumir"; Boundary = injeção de segredo dos provedores).
5. n8n: o ginkgo-tree já trata n8n como **executor cego** atrás do Boundary, com instância própria
   (5679) e workflows provisionados. O fluxo rico da CALLIMA (multimodal, debounce, áudio, mídia) que
   testamos aqui é o ALVO pro qual a Skill BRANN do tronco deve migrar.

## Pontas soltas (além do Docker)
- **Pareamento WhatsApp** pendente (fundador escaneia QR) → trava a prova do happy-path ao vivo.
- **Segredos externos** `[PREENCHER]` no .env (OpenRouter + Evolution) → mesmo bloqueio do crédito OpenRouter.
- **Duas bases divergentes** = a maior ponta solta: decidir o tronco AGORA evita seguir construindo 2x.
- **Baileys/Evolution = risco existencial** (WhatsApp não-oficial, dito no North Star deles) → reforça
  a migração pro **WhatsApp Cloud API** que já specamos.
- RAG sem embeddings, MCP só docs, sem event-bus real, sem assinaturas, PYRE/WAVE shells.
- Docker stack parada → precisa `up` + pareamento + chaves reais pra rodar ao vivo.

## Plano de unificação (se aprovado o tronco = ginkgo-tree)
1. Subir a stack do ginkgo-tree (Docker) e validar o que já roda (api/worker/web/n8n/evolution).
2. Fundador pareia o número → prova o loop BRANN ao vivo.
3. Portar a UX do leaf pro apps/web do tronco: Shell+AppSwitcher → Inbox (já existe, repaginar) →
   **Kanban (gap)** → config Callima → /pricing (mapeado no ledger real).
4. Migrar Callima (multimodal/mídia/áudio) como Skills atrás do Boundary.
5. Seguir o roadmap do PRD: trio BR (STT/TTS, agenda, Pix) → assinaturas → CRM → RAG → PYRE → WAVE.
6. Aposentar o leaf-Supabase como repo de produção (vira referência de UX).

## Alternativas (decisão do fundador)
- B) leaf = tronco, portar governança do ginkgo-tree pra ele → **descarta o que é mais difícil e
  testado**. Não recomendo.
- C) Manter os dois, front leaf → API ginkgo-tree → reconciliação de auth/DB cara e frágil. Não recomendo.
