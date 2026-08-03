# LEAF — Feature: Callima Outbound (prospecção ativa sequencial) — spec 2026-07-06

> Vira a Callima de **inbound-only** (cliente fala primeiro) para **também outbound**: puxa uma cartela de leads do Kanban e **aborda um a um, sequencialmente**, prospecta e vende — com o inbound assumindo assim que o lead responde. Fatia **pós-core** (depois do QR/e2e ao vivo). Governança herdada: honest-data, Task+budget, Events, maturity ladder, money=HITL.

## Decisões travadas (fundador, 06/07)
1. **Canal/risco = opt-in only no Baileys.** Só aborda leads **com consentimento/mornos**; nada de frio total. Dá pra fazer já, sem depender do portfólio Meta. Cloud API oficial = upgrade futuro.
2. **HITL = aprovar a campanha, solta auto.** O dono revisa **mensagem-modelo + cartela + cadência UMA vez** (essa aprovação É a attestation); a engine dispara sequencialmente sozinha, dentro dos limites.
3. **Cartela = import manual (CSV/colar)** no board "não abordado" (nome, telefone, flag opt-in, campos livres).

## 🔴 Guardrails de risco (NÃO-NEGOCIÁVEIS — é o que protege o ativo)
Outbound no WhatsApp não-oficial (Baileys/Evolution) queima número fácil. A honest-data se estende a **honest-consent**:
- **Opt-in obrigatório por lead** — importar exige a flag `optIn=true` (ou comprovante de origem). Sem opt-in ⇒ o lead **não entra na fila de abordagem** (fica em "não abordado" mas inelegível, com badge).
- **Cadência humana:** 1 lead por vez por-org, intervalo com **jitter** (ex.: 3–8 min), **só horário comercial** (config por-org/timezone), **teto diário** por número, **warm-up** (número novo começa com poucas aberturas/dia e sobe).
- **Opt-out é lei:** qualquer "pare/parar/sair/não quero/descadastrar" ⇒ **kill-switch permanente** desse lead (nunca re-contatar, marca `optOut=true`), imediato.
- **Sinal de ban ⇒ pausa automática** da campanha (se a instância Evolution reportar desconexão/erro em sequência).
- **1 número = 1 instância** (o caveat de sempre): usar o número de teste até o cutover.

## Modelo de dados
**Reusa (já existe):** `Lead` (`status`, `stage`/`PipelineStage`, `intentScore`, `source`, `phone`, upsert idempotente por `(orgId, phone)`), `Pipeline`/`PipelineStage` (colunas dinâmicas via StageManager), `Conversation`, `Task`/`Ledger`/`Evidence`, cofre.
**Adiciona (fatias):**
- `Lead`: `optIn Boolean @default(false)`, `optOut Boolean @default(false)`, `lastOutboundAt`, `outboundAttempts Int @default(0)` (ou tudo em `customFields` na 1ª fatia p/ evitar migração destrutiva — decidir).
- `OutboundCampaign` (nova): `id, orgId, name, status(draft|approved|running|paused|done), templateMessage, cadenceConfig(json: intervalo/jitter/horário/teto/warmup), stageFromId, approvedBy, approvedAt, createdAt`. A **aprovação** grava `approvedBy/At` = a attestation.
- `OutboundAttempt` (nova, append-only p/ auditoria): `id, orgId, campaignId, leadId, taskId, sentAt, outcome(sent|replied|no_reply|opted_out|failed)`.

## Estágios do Kanban (mapa — via PipelineStage dinâmico)
O dono cria/usa um pipeline com as colunas que ele descreveu. Mapa honest-data (card só anda com **Event provado**, nunca pintado):

| Coluna (stage) | Entra quando | Event |
|---|---|---|
| **Não abordado** | lead importado, ainda sem 1º toque | `lead.imported` |
| **Conversando** | 1º toque **enviado E** lead **respondeu** | `lead.contacted` + `lead.replied` |
| **Frio** | N follow-ups sem resposta (ou opt-out) | `lead.cold` / `lead.opted_out` |
| **Convertido** | pagamento confirmado (webhook) | `lead.converted` |
| **Perdido** | recusou / inelegível | `lead.lost` |

> Nuance: **"Frio" (coluna/estágio)** ≠ **"Frio" (badge de temperatura derivada do `intentScore`)**. São dois eixos; o spec não os funde. O 1º toque **enviado mas sem resposta** fica em "Não abordado" (sub-estado "abordado, aguardando") — só vira "Conversando" com resposta real.

## Engine sequencial (o "um a um")
Um **dispatcher no worker** (BullMQ repeatable / cron por-org):
1. Se a campanha está `running` e dentro do horário/teto/warm-up → pega o **próximo lead elegível** (stage="não abordado", `optIn=true`, `optOut=false`, não abordado ainda), **ordenado** (FIFO ou por intentScore).
2. Cria **1 Task governada** `leaf.outbound.reach_out` (budget HOLD→SETTLE) que envia o 1º toque via Skill.
3. Aguarda o **jitter** antes do próximo. **Concorrência = 1 por-org** (parece humano + evita o head-of-line que a auditoria pegou).
4. Sem resposta em X h → agenda follow-up (`leaf.outbound.followup`, até N). Depois de N → `lead.cold`.
5. Resposta do lead → **para o outbound** desse lead; o **loop inbound da Callima assume** a conversa (é a Callima de sempre).

## Skills novas (governadas — ADR 0004; nascem em simulação→shadow→produção)
- **`leaf.outbound.reach_out`** — R2 · secretScope `evolution_api_key` · egress WhatsApp/Evolution · honest-data (só afirma "abordado"/move card **após envio confirmado**; falha ⇒ `task.failed`, card não anda). Emite `lead.contacted`.
- **`leaf.outbound.followup`** — R2 · idem, com contador de tentativas.
- **`leaf.outbound.optout`** — R1 · marca `optOut=true`, remove da fila, emite `lead.opted_out` (kill-switch; disparado por detecção de intenção de saída no inbound).
- Aprovação da campanha = gate **HITL** (a Task de "abrir campanha" espera o Aprovar do dono = attestation; só então o dispatcher liga).

## Fluxo ponta-a-ponta
Import CSV (opt-in) → leads em "Não abordado" → dono **abre campanha** (revisa modelo + cartela + cadência) → **Aprovar (HITL)** → dispatcher **abre 1 a 1** com cadência humana → lead responde → **Callima inbound assume** → agenda/vende → `convertido` (pagamento) ou `frio` (N sem resposta) → **board reflete cada passo, provado por Event**.

## Controle / monitoramento / desligamento (obrigatório)
- **Pausar/retomar** campanha a 1 clique; **teto diário** e **warm-up** configuráveis.
- **Kill-switch opt-out** por lead (permanente) + **auto-pausa em sinal de ban**.
- O dono **vê cada passo no board + aba Atividade** (Tasks/Evidence): quem foi abordado, quando, resultado — honest-data, auditável.
- Métrica derivada: abordados/dia, taxa de resposta, conversão por campanha (do Ledger/Events, não inventada).

## Fatiamento (fatias Fable — pós-core)
- **S1** — modelo: `OutboundCampaign`/`OutboundAttempt` + `optIn/optOut` no Lead + **import CSV** (endpoint + upsert idempotente por telefone) → coluna "Não abordado". Gate.
- **S2** — **dispatcher sequencial** (repeatable job, concorrência 1, cadência/jitter/horário/teto/warm-up) em **simulação** (propõe, não envia) → **shadow** (loga o que enviaria). Gate.
- **S3** — Skill `leaf.outbound.reach_out` (R2, honest-data) → **produção opt-in**; card anda por Event. Gate.
- **S4** — `followup` + `optout` (kill-switch) + transição "frio". Gate.
- **S5** — **UI "Abrir campanha"** (modelo + cartela + cadência + Aprovar/HITL) + go-live com leads opt-in reais. Gate.

## Dependências / riscos
- **Baileys ban** = risco residual mesmo com cadência (não-oficial). Mitiga com opt-in + limites; **Cloud API oficial** (quando o portfólio Meta sair) é o hardening real (template + opt-in nativo).
- Reforça a prioridade da **fila com fairness por-tenant** (auditoria #P2): com campanhas rodando, o global sem fairness starva mais fácil.
- Reusa a **prova de envio** (o `brann-confirmer`) — depende do happy-path de envio estar provado (pós-pareamento). Outbound **não** pode ir a produção antes disso.

## Fora de escopo (por ora)
- **Lead Finder** (gerar/qualificar leads) — **NÃO construir do zero.** Candidato a **parceria: Ledger Lead Finder** (tool de um amigo do fundador — scraping Google Maps/LinkedIn + **scoring** + CRM próprio; parceria/integração possível). Fronteira limpa: **Ledger = fonte de leads scored → nosso ingest "não abordado" → Callima faz o outbound governado + conversa + prova.** Não reconstruímos o scraping (a parte legal-cinza é do parceiro). Governança: lead scored ≠ opt-in → **cold → email/manual, nunca auto-WhatsApp**; LGPD → Ledger=controller, nós=processor (pedir **DPA**). Integração: começa CSV/webhook → evolui p/ API/Events. Motores alternativos: Apify/PhantomBuster.
- **Frio total** (sem opt-in) — vetado por risco.
- **Multicanal** (Instagram/Messenger) — depois do WhatsApp + App Review. Caminho oficial = **Meta Instagram Messaging API** (precisa do portfólio Meta). O `supreme-gg-gg/instagram-cli` (MIT, one-turn commands + SKILL.md p/ agentes) dá acesso programático a DMs, MAS **não-oficial (login user/pass = ban), projeto explicitamente ANTI-bot, fere ToS da Meta** → referência, não outbound governado.

---
## Atualização — aprendizados do Mailerfind (06/07, ver `benchmark_mailerfind.md`)
- **🔑 Canal de COLD = EMAIL, não WhatsApp.** Mailerfind prova que cold-email (com warmup + deliverability + opt-out) é bem mais defensável e menos "banível" que cold no WhatsApp. **Regra revisada:** cold outbound = **email** (CAN-SPAM/opt-out); **WhatsApp = só warm/opt-in** (a decisão original vira o trilho warm). O engine sequencial + guardrails valem pros dois canais.
- **Requisito de engenharia novo:** deliverability + **email warmup** (inbox vs spam) pro canal email.
- **Wizard de campanha (roubar o UX):** analisar negócio → fonte de leads → **3 modelos IA (variantes + regerar + variáveis)** → conectar canal → **tela "Excelente! encontramos X, modelo pronto"** (honest-data com números provados) → **Aprovar** = o HITL de campanha.
- **Lead Finder** (scraping/enriquecimento IG/social) = fonte de cartela além do CSV — vira spec próprio, com flag de ToS/scraping (§4 do benchmark).
