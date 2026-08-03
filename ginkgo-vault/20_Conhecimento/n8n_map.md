# n8n — mapa de organização (mantido pela Sexta-feira)

**Regra-mestra:** separar por **tier de confiança / blast-radius**, NÃO uma n8n por SaaS.
Pasta organiza; **pasta NÃO isola** (credenciais e execução são compartilhadas na instância). Isolamento real = instância separada (ou n8n "Projects" Enterprise).
**Toda stack com dados vivos fica FORA do OneDrive** (named volumes / `C:\dev`) — OneDrive trunca dados.

## Duas instâncias, por propósito

### 1. Ginkgo Runtime (PRODUTO) — governado, multi-tenant
- Instância: tronco `ginkgo-tree` n8n **:5679** (indo p/ `C:\dev`, named volumes).
- Serve os 3 SaaS aos **CLIENTES**, por tenant, via Boundary (executor_ref assinado, honest-data): Leaf (whatsapp-send/Brann), Wave (ações de ad), Pyre (geração).
- **SAGRADA:** não recebe automação interna/marketing/experimento. Credenciais de cliente só aqui, resolvidas pelo Boundary (nunca soltas).

### 2. Ginkgo Ops (OPERADOR) — Ginkgo fazendo pra si
- Instância recomendada: **`ginkgo-ops`** dedicada (n8n + postgres + redis, named volumes, fora do OneDrive).
- *(Transitório: o ai-stack `:5678` hoje roda a Callima, mas usa binds `./data` em OneDrive = risco de corrupção → migrar/aposentar.)*
- Organizada por **pastas**; Sexta-feira gere:

  | Pasta | Conteúdo |
  |---|---|
  | `00_Social-Ginkgo` | redes sociais da própria Ginkgo (dogfood do Wave) |
  | `10_Content-Engine` | fábrica de conteúdo + biblioteca + autopost |
  | `20_Leaf` / `21_Wave` / `22_Pyre` (ops) | workflows internos/experimentais por SaaS (NÃO client-facing) |
  | `30_Automacoes` | glue interno: backups, alertas, cross-tool |
  | `60_Callima` | secretária (prototype, client-facing) — migra p/ Runtime quando madura |
  | `90_Sandbox` | experimentos |

## Credenciais (a guarda — já que pasta não isola)
Prefixo por domínio: `ginkgo_…` (operador) · `tenant_<org>_…` (cliente, só no Runtime) · `exp_…` (sandbox).

## Papel da Sexta-feira
Manter este mapa (instância → pasta → workflows → credenciais), ajudar a montar/editar workflows, documentar. **Operar o n8n ao vivo** (criar/rodar via API) só com conector n8n — a avaliar.

> Atualizar quando criar/mover workflow ou instância.

---

## Verificação da pasta LEAF (ai-stack :5678) — 2026-07-01, Sexta-feira
Fonte: export `CALLIMA_corrigido.json` (nó-a-nó) + `apis_mcps_n8n_inventario.md` §7 + arquitetura.

| Fluxo | Papel | Veredito |
|---|---|---|
| **Callima** (`zo9FqQ9XVRcU8AJZ`) | cérebro-interino: agent + Redis memory + Evolution + OpenAI/Gemini + code + sub-workflows | ✅ coração — lacunas: handoff, RAG, STT robusto |
| **AUDIO FEM / "AUDIO BRANN"** (`8EoLKO7wdhv0ZLgz`) | TTS ElevenLabs (via executeWorkflow) | ✅ → vira `channel.whatsapp.send-audio` |
| **ENVIAR MIDIA** | envio de mídia (executeWorkflow) | ✅ capacidade cega reutilizável |
| **pix_link** | link Pix in-chat | ✅ add-on BR (padrão = link Stripe) |
| **LEAF — Brann Actions Consumer** | consome ações governadas do Brann (elo pro tronco) | ✅ ponto de migração |
| **Content Engine — LinkedIn** | conteúdo LinkedIn | ❌ **é Pyre** → mover p/ `10_Content-Engine`/`22_Pyre` |

**Falta no LEAF:** handoff/alerta HITL (= F5) · follow-up (fase de disparos) · STT áudio-in (= loop 2; no alvo vira read-through do worker, não fluxo novo). *ingest WhatsApp Cloud API = futuro Meta.*

## Roadmap de migração (Ops interino → Runtime governado)
1. **🔴 Sair do OneDrive (urgente):** :5678 usa binds `./data` no OneDrive = risco de corrupção do cérebro que já vende → named volumes fora do OneDrive (ou instância `ginkgo-ops` dedicada).
2. **Content Engine → Pyre:** mover o fluxo LinkedIn (não é LEAF).
3. **Cognição → worker governado:** migrar o cérebro da Callima do n8n pro runtime do tronco (Boundary resolve credencial por-tenant); n8n vira só executor cego por capacidade → mata o clone-por-cliente.
4. **Capacidades cegas no Runtime :5679:** send-text ✓ · send-audio (novo) · send-media · pix-link — 1 por verbo, credencial injetada em runtime.

## Radiografia nó-a-nó (2026-07-01, via REST API `/api/v1/workflows`, dumps em `callima/leaf_dump/`)
49 workflows na instância; 6 LEAF exportados. **Achado: a Callima-n8n é bem mais completa que o trunk** — o "como deve ser" já existe (interino, single-tenant).

- **Callima** (58 nós, active): webhook→debounce(Redis)→`Route`[switch 6]. Agent `lc.agent`, cérebro `openrouter: openai/gpt-4.1-mini`, memória `Postgres Chat Memory`. Tools: Think, Calculator, Google Calendar, **RAG `base_conhecimento_callima`→AnythingLLM `workspace/callima`**, Gmail, MIDIA, PIX, Send Audio. Multimodal: **STT** (OpenAI transcribe), vídeo (Gemini), doc (Anthropic). Bridges: **[[LEAD]]→`/ingest/lead`** + **[[AGENDAR]]→Google Calendar+`/ingest/appointment`** (host.docker.internal:3333). TTS via [[AUDIO]]→AUDIO FEM. Handoff: IF "Intermediação Humana" (pausa existe; **alerta ao dono não aparece** = #15). Stripe/Pix embutidos.
- **AUDIO FEM** (7, active): TTS ElevenLabs (voz fixa `EXAVITQu4vr4xnSDxMaL`) → Evolution send-audio. ✅
- **ENVIAR MIDIA** (5, active): Evolution **send-image** só (estender p/ áudio/vídeo/doc depois).
- **LEAF — Brann Actions Consumer** (8, active): lê ações aprovadas do **Supabase do trunk** → claim idempotente → **envia e-mail via Resend** → marca+audita. ✅ (sender de e-mail + consumidor governado)
- **pix_link** (2, active): code gera link Pix. ✅
- **Content Engine — LinkedIn** (7, active=false): é **Pyre** → mover (fundador já moveu; confirmar que saiu do filtro).

**Correção honesta:** o que chamei antes de "lacunas" (RAG/STT/áudio) **existe no n8n**. A lacuna real é: (1) **multi-tenant** — tudo usa credencial única + 1 workspace RAG "callima" = UMA Callima (a do fundador); pra "cada cliente uma igual" precisa per-tenant (Boundary resolve cred + RAG por-tenant); (2) **handoff sem alerta ao dono** (#15); (3) **vive no n8n, não no runtime governado do trunk**.

**Reframe do Loop 2:** não é greenfield — é **PORTAR o cérebro provado da Callima-n8n → runtime governado do trunk** (Boundary + Evidence + per-tenant). Risco menor: a lógica já está provada nestes dumps.
