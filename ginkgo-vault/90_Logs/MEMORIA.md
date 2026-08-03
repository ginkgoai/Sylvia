# MEMÓRIA DURÁVEL — Ginkgo (mantida pela Sexta-feira)

Destilado do que não pode se perder. Atualizo quando algo durável muda. Detalhe cronológico em `CONTEXT_LOG.md`.

## Decisões-mestras
- **Tronco canônico = `ginkgo-tree`** (Fable: Kernel/Boundary/tokens/HITL; back+front). `leaf` (Supabase) = doador de UX, aposentar após portar. Construir SEMPRE no tronco.
- **honest-data é lei:** a UI mostra estados/tokens REAIS; nunca sintetizar (ex.: bolha "enviada" só após confirmação do envio).
- **P004:** dev-memory ≠ runtime/tenant memory. Dado de tenant NUNCA entra no cofre. Memória de runtime do agente (lembrar do cliente a longo prazo): **não existe ainda** — fatia futura, não specada.

## Doutrina atual — Callima como engrenagem (MVP Leaf · rev. 2026-07-01)
- **MVP = Callima (WhatsApp) + painel web, LOCAL** (prod só na fase-com-renda). Enxuto: CRM, atendimento, dados, assistente web (Brann), secretária configurável que atende/entende/vende por **texto E áudio**. Resto é feature.
- **Transformar o que dá certo:** a Callima-n8n provada (58 nós: RAG AnythingLLM, STT, TTS, multimodal, bridges lead/agenda, memória, Stripe/Pix) vira **engine governada** no trunk. Não é greenfield — é PORT.
- **Multi-tenant automático:** per-tenant = ESTADO (config `agentProfile` + credenciais no cofre resolvidas pela Boundary por `org_id` + conhecimento RAG por-tenant). Uma base serve todos; fim do clone-por-cliente.
- **Brann = operador E editor:** o dono configura por conversa. Editor (escreve config) + Operador (ações governadas: conectar, ligar, adicionar conhecimento, handoff) — catálogo allowlisted (ADR 0004), sem god-mode; credencial=R3→HITL.
- **Chaves de provider (Groq/ElevenLabs/OpenAI) no COFRE, nunca `.env`** (invariante #8; secretScopes/Boundary). O model-router só NOMEIA o provider.
- **RAG:** AnythingLLM workspace-por-tenant atrás de Skill `leaf.rag.retrieve`; pgvector = upgrade interno futuro (absorve #13).
- Docs vivos: `50_Plataformas/leaf_callima_engine_padronizacao.md` (design/port) · `leaf_loop2_callima_spec.md` (fatias) · `leaf_mvp_plano_execucao.md` (plano 3-listas) · `20_Conhecimento/n8n_map.md` (radiografia nó-a-nó).

## Pricing (BRL — v2, confirmado 04/07)
**À la carte, independentes — fonte `apps/api/src/billing/catalog.ts`:** Leaf R$449 · Pyre R$899 · Wave R$1.199 · **SEM "Full"** (o R$2.497 era desconto-fake de R$50 → fere honest-data) · trial grátis 7–14d · **IMAGINE/enterprise = GTK (uso) + BYO** · Sinal R$100 (avulso) · top-ups GTK. Margem via modelos baratos no Provider Router. ⚠️ ainda há resíduo "Full" no RAG vendedor (`60_Callima/base_*`) e `leaf_piloto1_ginkgo_kit.md` — corrigir.

## Roster
Leaf=Brann · Pyre=Nyra · Wave=Alfred · Callima=secretária do cliente. Sexta-feira orquestra; Laplace governa.

## Estado de build (atualizar a cada fatia) — rev. 2026-07-03
- Gate **main 348/348** (local, 3 commits à frente de origin: S5 `7e6f0b5` → docs-sync `3f2a75a` → M5 ativação `194061c`). Código em **C:\dev**.
- **Loop 2 completo em código:** S1 STT → S2 TTS → S3 agendamento → S4 RAG per-tenant → **S5 handoff**. A Callima **atende · entende áudio · fala · agenda · fundamenta · passa pro humano E avisa**. **Loop core de atendimento fechado em código/gate; PROVA AO VIVO PENDENTE** (parear número + `RESEND_API_KEY` + `put-alert-channel.ts`).
- Callima-n8n (ai-stack) segue VIVA (prod interina) — vira rollback/teste após o cutover do número pro trunk.
- **Auditoria Fable (rev.2, 03/07):** doc-drift (PRD/CHECKPOINT/kickoff defasados → docs-sync é a próxima fatia, minha dívida de coesão); segurança n8n/Evolution (HMAC não-verificado, chave Evolution global, ingest token único = **#9 antes de terceiros**); Baileys existencial (mitiga via ChannelPort/multicanal). Regra de corte: passos 0–5 = 1º piloto governado; 6–9 = operação 10–50 tenants sem humano.
- **Decisões:** #3 provedores = **white-label compartilhado + Enterprise BYO provider-swappable** (`modelo_provedores_e_tiers.md`). Produtos: **PYRE=criação · WAVE=distribuição/ads/tracking · LEAF=conversão**. Multicanal spec cravada (`leaf_feature_multicanal.md`; gate técnico = App Review, não Meta Partner). Identidade dos agentes canônica (`brand/identidade_visual_agentes.md`).
- **Arquitetura de agentes + tiers (04/07, `arquitetura_agentes_e_tiers.md`):** Brann=**assistente/copiloto** (orquestra) · Callima=**secretária** (LEAF) · Nyra (PYRE) · Alfred (WAVE). **Sub-agentes governados delegados** (main→sub): **financeiro sob Alfred** (verba de ads + cobranças; benchmark Pierre.finance = **read-only**; nosso: read livre + dinheiro=HITL/PSP) · **Lexra jurídica** (contratos/DocuSign, futura, assinar=HITL). Nomes = renomeações, NÃO reservados: **Alphie→Alfred · Shion→Sexta-feira** (mesma entidade; orquestrador sempre existiu; avatares vieram depois). **Tier IMAGINE = institucional** (contratar a Ginkgo como empresa; custom; encaixa BYO/Odysseus). **Pricing v2: à la carte 449/899/1199, SEM Full**; decks antigos arquivados.
- **Ativação self-serve (M5) MERGEADA** (348/348): funil fechado em código — cadastra → org ativa sozinha (cofre semeado do PlatformSecret store, com proveniência + `webhookTokenHash` por org, encosta no #9) → conecta WhatsApp → configura com Brann → atendido pelo loop core → paga. Achado crítico ROOT-1 (org legada "surda") pego e corrigido.
- **Store de plataforma SEMEADO ✓ (04/07):** 4 chaves gravadas + **validadas no provider**; webhook-token migrado por org. Falta só: **parear o número de teste** (QR) → **e2e ao vivo**; `RESEND_API_KEY`+`EMAIL_FROM` no worker p/ alerta de handoff por e-mail. **Aprendizado/dívida:** dev sincroniza por `db push` (não migrate) → **drift migração×push** (migração `20260620100000` ficou "failed" no histórico) a limpar antes de CI/prod.
- **04/07 noite:** M5 mergeado+pushado (origin privado); store de plataforma semeado ✓; **connect/QR (M5c) DONE** — branch `feat/whatsapp-connect-surface` **381/381** (mergeável; migração nova `20260704000000`; dedup TOCTOU atômico; `/status` honesto). Bug era só de superfície (cartão só no empty-state da inbox). Página `/app/leaf/canal` com QR real renderizado. **Falta a ÚNICA ação física: parear o número (amanhã, celular em mãos).**
- **Design System gerado no Claude Design** (2 registros warm/neon ok; fontes = Space Grotesk/Hanken/JetBrains substitutas; ícones Lucide). Fix prioritário = **telas reais do produto** > fontes.
- **Próximo:** parear → **e2e ao vivo** → **#4 ofertas** (ARPU) → **#9** rotação + reconciliação migração×push. Ao mergear a M5c: a migração nova roda no boot da api (deve ir limpa; se crash-loop, é ela).

## Aprendizados (auto-aprendizado)
- **OneDrive corrompe repo git vivo** (trunca working tree; node_modules/lockfile/arquivos grandes). Cofre e código ficam FORA do OneDrive. Cofre → `C:\sexta-feira` (feito). Código → `C:\dev` (feito).
- Para ajuste verificável (ex.: contraste WCAG AA), **prova direta** (grep + cálculo + gate real) > orquestrar workflow multi-agente.
- Ritmo: fundador manda **1 prompt/sessão** pro Claude Code (no repo `ginkgo-tree`); eu (Sexta-feira) reviso o print e preparo o próximo. PRs limpos, local até decidir publicar.

## Preferências do fundador
- Responder em **pt-BR**, direto e técnico, conciso. Tratar como parceiro técnico sênior.

## Dependências externas (destravam P0)
Crédito OpenRouter (~$10) → liga Callima + compute · Portfólio Meta (WhatsApp Cloud + Marketing API) → canais oficiais + Wave · Stripe USD · fal.ai/HeyGen → Pyre · Postiz/Elasticsearch → Content Engine.
