# Leaf — Loop de Excelência (estado atual → produto final)

> Criado 2026-06-25 pela Sexta-feira, após avaliação completa do repo `ginkgo-tree` + docs do cofre.
> Objetivo: levar do estado atual ao **produto final** em loop, dividindo **[CODE]** (Claude Code, tronco) e **[COWORK]** (Sexta-feira, Callima/n8n), chamando o fundador só pro importante.

## Objetivo final (excelência)
Callima (como está, vendendo) **+ skills/tools funcionando + alimentando a dashboard por usuário** — multi-tenant, honest-data, self-serve: cliente assina → conecta WhatsApp → Callima atende → o cliente vê leads/conversas/plano na dashboard dele.

## Estado atual (avaliação 25/jun)
- **Dashboard (tronco) ~80% pronta** em `feat/leaf-leads` (10 commits à frente da main, subsume todas as branches): multi-tenant + auth (JWT tenant-from-token, Google OAuth) · **bridge API `POST /ingest/lead`** (token por-org, hash, idempotente) · `/app/leads` · **inbox WhatsApp** (mirror + QR + status + composer humano honesto) · **CRM/Kanban** · **billing + assinaturas Stripe** · Kernel/Boundary · **111 testes + CI**.
- **Callima (n8n) viva e vendendo:** OpenRouter `gpt-4.1-mini`, links Stripe, proativa, áudio (em teste).
- **ELO CRÍTICO FALTANDO:** a Callima **não tem nó HTTP** chamando o `/ingest/lead` → dashboard vazia. **#1 blocker.**
- **Riscos:** `feat/leaf-leads` e `feat/pricing-gtk` **só locais** (nunca deram push) = risco de backup. Nada na main, nada deployado.

## Trilha [CODE] — produto (Claude Code no ginkgo-tree, loop estilo continuous-claude)
1. **Merge `feat/leaf-leads` → main + push tudo** (mata risco de backup, liga CI na main). ← PRIMEIRA
2. **Provisionar ingest token** da org do fundador (`scripts/put-ingest-token.ts`) + garantir a api up e alcançável pelo container n8n. (dá o token + URL pra mim)
3. Auto-link leads ingeridos → pipeline default (aparecem no Kanban, não só na lista).
4. Transcript da conversa por lead (popular/expor `Lead.conversationId` end-to-end).
5. **Conhecimento (KB) editável + ingestão RAG** — a maior feature nova ("cole a URL do seu site e o agente aprende").
6. Onboarding self-serve (parear WhatsApp + ligar Callima + revelar token — substitui os scripts manuais).
7. Hardening (rate-limit no ingest/webhook, helmet) + LGPD (retenção/deleção de ChatMessage) + email transacional.
8. Deploy (VPS) quando o caixa justificar.

## Trilha [COWORK] — Callima/n8n (Sexta-feira no ai-stack)
1. **Wirar o bridge: Callima → `POST /ingest/lead`** (nó HTTP após `Save Lead`, header `x-ginkgo-service-token`). ← PRIMEIRA (depende de [CODE]-2)
2. Realinhar **RAG** (Secretária→Leaf/Wave/Pyre + Stripe).
3. **Ativar skills uma a uma** (agora que OpenRouter entrou): Gmail → Calendar → Media → Payment. Cada uma isolada (caso-feliz + erro) antes da próxima.
4. **Handoff real** (Gmail + WhatsApp pro fundador + dashboard) — hoje "encaminho pro humano" vai pra lugar nenhum.
5. Fechar **áudio** (campo alinhado — em teste) + polish.
6. Processo de **clonagem por cliente** (manual interino → automático quando o LEAF SaaS assumir).

## Trilha [MULTI-TENANT] — "funciona pra qualquer cliente" (cada um na conta DELE)
Regra: cada skill usa a **credencial do próprio cliente** (calendário, email, WhatsApp, pagamento dele) — não a do fundador. Hoje = dogfood (conta do fundador). O padrão **já existe** no tronco: **Vault por-tenant + Boundary** (já resolve a chave do Evolution/WhatsApp por org).
1. **[CODE] Credenciais Google por-tenant:** onboarding conecta o Google do cliente (Calendar + Gmail, OAuth) → token criptografado por-tenant (estende o Vault) → Boundary resolve por `org_id`.
2. **[CODE] Appointment bridge:** modelo `Appointment` + `POST /ingest/appointment` (a Callima reporta o agendamento, igual o lead) → dashboard mostra a agenda do cliente. _(Email do cliente = automático: o Google manda convite/lembrete porque o evento nasce na conta DELE.)_
3. **[CODE] Credencial WhatsApp/Evolution por-tenant:** instância + chave do cliente no Vault (já parcialmente feito — `ChannelConnection`/`VaultAccess`).
4. **[RUNTIME] Resolver credencial do cliente em runtime:** em n8n a credencial é **estática por nó** → **clone-por-cliente** (interino, doc `clonagem-template-por-cliente`); no SaaS, **migrar a Callima pro runtime governado do tronco** (Boundary resolve creds por-tenant em execução). `n8n_map` já prevê.
5. **[CODE] Onboarding self-serve amarra tudo:** assina → conecta WhatsApp + Google → tudo nasce por-tenant.

## Roadmap por superfície de produto (fatias por valor × risco)
> Ordena as trilhas acima pela tese do `leaf_superficie_produto.md`: **a conversa é o produto; as telas são lentes.** Cada fatia tem **[COWORK]** (Sexta-feira/n8n) e **[CODE]** (tronco).

**Fase 1 — apertar o loop core** (Conversa → CRM → Agenda → Oferta→Checkout)
- Conversas (inbox) — ✅ · CRM auto-fill (`[[LEAD]]`→bridge) — ✅
- **Agenda** — [COWORK] portal `[[AGENDAR]]` (em andamento) · [CODE] appointment-bridge + tela Agenda (lançada). _Pronto = Callima agenda → evento real → tela + Google do dono._
- **Oferta→Checkout** — [CODE] registry de **Ofertas** por-tenant (produto/preço/link Stripe) + tela, alimenta a KB da Callima · [COWORK] Callima puxa a oferta do tenant + manda o checkout certo. _Pronto = dono pluga oferta → Callima vende com o link certo → pagamento real (webhook) cai em Dados._

**Fase 2 — Dados (o funil)**
- [CODE] analytics atendimentos→leads→agenda→checkout→venda (honest-data) + tela · [COWORK] garantir cada evento reportando pro tronco. _Pronto = dono vê o funil real._

**Fase 3 — Brann config (self-serve)**
- [CODE] Brann (`hermes.chat`) escreve a config por-tenant da Callima (persona/voz/permissões) no Persona/Face Registry, dentro do catálogo + teto de risco · [COWORK] Callima lê a config por-tenant → **fim do clone-por-cliente**. _Pronto = dono muda a Callima conversando; reflete no WhatsApp._

**Fase 4 — Disparos (governado, por último)**
- [CODE] campanhas com opt-in + rate-limit + templates aprovados + audit (WhatsApp/email) · [COWORK] portal de disparo determinístico só com opt-in. _Pronto = disparo com trava, sem queimar número._

**Transversais (sempre):** honest-data · governança (Boundary/permissões) · multi-tenant (creds + config por-tenant) · observabilidade.

**Fila imediata:** [COWORK] retomar `[[AGENDAR]]` (fatia #1) · [CODE] appointment-bridge (rodando) → depois **Ofertas registry + tela**.

## O loop (como iteramos)
- **Sexta-feira (eu):** rodo a trilha COWORK autônomo; mantenho o task board + `CONTEXT_LOG`; a cada fatia te entrego o próximo prompt do Code. Te chamo só pra: **credenciais, dinheiro, ou direção estratégica.**
- **Claude Code (você dispara):** roda a trilha CODE em loop (PRs autônomos → CI verde → merge), um prompt por fatia que eu te dou.
- **Milestone 1 (o que prova o produto):** bridge vivo = **primeiro lead da Callima aparece na `/app/leads`** (COWORK-1 + CODE-2).
- **"Excelência" = ** cliente real assina e usa self-serve · dashboard mostra dados vivos da Callima · multi-tenant isolado · hardened · deployado.

## Decisões que preciso do fundador (poucas)
1. **Integração local:** a api do tronco precisa rodar + ser alcançável pelo container n8n. Vou investigar; se precisar, te peço pra subir `pnpm dev`.
2. **Credenciais das skills:** Google OAuth + OpenPix App ID — peço quando chegar na COWORK-3.
3. Greenlight pra **mergear na main + push** (CODE-1).

_Mantido pela Sexta-feira. Atualizar a cada fatia._
