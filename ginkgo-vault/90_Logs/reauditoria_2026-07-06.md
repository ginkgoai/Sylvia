# RE-AUDITORIA COMPLETA — Ginkgo AI Systems (2026-07-06)

> Auditoria read-only em 3 frentes paralelas (trunk/arquitetura/Hermes · vault/estratégia · n8n/Skills/segurança), cada achado com evidência `arquivo:linha`. Nada foi modificado pelos auditores. Síntese pela Sexta-feira.

## Veredito global
**🟢 O núcleo governado é REAL, não só documentado.** Kernel puro + Boundary (chokepoint 8 passos) + cofre AES-256-GCM + os 9 invariantes + honest-data estão **implementados de fato** e testados. LEAF vivo em código; PYRE/WAVE = shells "ComingSoon" honestos (zero dado simulado, por construção).
**🔴 Dois vermelhos localizados:** (1) **drift de pricing** — o "Full R$2.497" morto ainda vaza em 4 docs, inclusive na MEMORIA e no RAG que a Callima lê; (2) **escala multi-tenant autônoma** (10–50 tenants sem humano) tem bloqueadores reais: sem RLS, fila sem fairness, sem rotação de chave, e o happy-path de **envio nunca rodou vivo**. Para o **piloto single-tenant, nada disso trava.**

## Scorecard
| Área | Saúde | Nota |
|---|:---:|---|
| Estrutura/stack do trunk | 🟢 | pnpm/TS, Kernel/Boundary/db/leaf/api/worker/web; 25 models, 4 ADRs, higiene rara (0 FIXME/HACK real) |
| Framework **Hermes** | 🟢 | Existe no trunk (não é host externo); é o agente conversacional do LEAF |
| 9 invariantes / governança | 🟢 | Todos sólidos; 2 pontos "staged" (egress bloqueio, sandbox real) |
| 3 dashboards LEAF/PYRE/WAVE | 🟢 | LEAF real (inbox/CRM/agenda/ofertas/canal-QR); PYRE/WAVE shells honestos |
| Gate de testes | 🟡 | **381** confirmado (estático) na branch connect; não rodei (symlinks pnpm ausentes no mount) |
| Git | 🟢 | branch `feat/whatsapp-connect-surface` = **+2/−0** de origin/main (FF limpo: M5b Ofertas + M5c QR) |
| Migração Prisma | 🟢 | o drift "db push" foi **aposentado no F1-02**; `migrate deploy` é lei; a "failed" é artefato de banco, SQL é limpo |
| Segurança (single-tenant) | 🟡 | fundações verdes; dívidas #9 mapeadas |
| Segurança (50 tenants autônomos) | 🔴 | RLS, fairness, rotação, prova de envio = bloqueadores |
| n8n Callima (produção interina) | 🟡 | vive e fatura (single-tenant, ~58 nós, ~17 exec/dia) — mas em OneDrive (risco) |
| Port n8n→Skills (S1–S5) | 🟡 | registrado no código (11 skills), **sem cutover nem prova viva** |
| Cofre/provedores | 🟢 design / 🟡 disco | router puro + AES + VaultAccess; mas chaves vivas no `.env` de dev + master sem rotação |
| RAG multi-tenant | 🟡 | por-tenant travado no trunk (slug persistido); n8n interino usa 1 workspace único |
| Vault/docs coerência | 🟡 | doutrina forte; drift concentrado em pricing e resíduos "nome reservado" |
| Sexta-feira (papel/memória) | 🟢 | MEMORIA/CONTEXT_LOG fiéis; só o pricing embutido precisa corrigir |

## "Os 3 corpos" — resolvido
= **"uma mente, três faces"** (`arquitetura_yggdrasil_ginkgo.md:8`). O **Hermes é a mente única**; os **3 corpos = as 3 faces-agente**, uma por produto: **Brann (LEAF) · Nyra (PYRE) · Alfred (WAVE)**. NÃO são os tiers (449/899/1199) nem o modelo operacional. **Nuance a cravar:** no LEAF há **dois personagens** — Brann (face-Hermes, copiloto de config) + **Callima** (secretária que o cliente vê). Se pensar em "3 produtos", os rostos visíveis são Callima/Nyra/Alfred; se pensar em arquitetura, os corpos são Brann/Nyra/Alfred. Vale uma frase-âncora oficial.

## Hermes — saúde
**Existe e está saudável.** Lei conceitual em `docs/ARCHITECTURE_HERMES.md` ("membrana IA↔contratos; cria Task, nunca executa/escolhe modelo/toca segredo"). **Runtime real** = `apps/worker/src/hermes-chat-delegate.ts` (o concierge do Brann): percepção só com dado real da org, LLM via OpenRouter com **chave do cofre por invocação**, honest-data ancorado no resultado real do upsert/embed (nunca no que o LLM diz). Testado (`brann.test.ts` 19 + `brann-onboarding.test.ts` 25). **Drift:** o doc diz "No code" — falso hoje (o delegate existe). Corrigir o doc.

## Correção honesta (eu tinha mischaracterizado)
O **"HMAC não-verificado no webhook Evolution"** que eu vinha repetindo **está impreciso**: o webhook Evolution→trunk **valida bearer token por-org** (`timingSafeEqual`, `channels.ts:31-34,147-156`) — não usa HMAC. O HMAC não-verificado real é o hop **worker→n8n** (defense-in-depth, o lado n8n 2.x não roda Code pra verificar). Ou seja: o ingest público **está autenticado**; a lacuna é o elo interno FIRST_PARTY. Menos grave do que a memória dizia.

## Top riscos para operar 10–50 tenants SEM humano (ordenados)
1. 🔴 **Sem RLS + fila global sem fairness** — 1 query sem `where:{orgId}` vaza cross-tenant (sem rede); 1 tenant barulhento (5 replies a 30–50s) congela os 5 slots e **para os outros 49** (head-of-line).
2. 🔴 **Happy-path de envio nunca rodou vivo** — o `brann-confirmer` faz parse defensivo de 2 shapes presumidos do `findMessages` da Evolution; risco de **100% das respostas ROLLED_BACK** no 1º pareamento real.
3. 🟠 **Chave Evolution global + Evolution SPOF + sem rotação de cofre** — blast-radius total de canal e de segredos.
4. 🟠 **Egress "decorativo"** — o Boundary só **loga** a allowlist, não bloqueia (`boundary-executor.ts:85-88`); uma key pode sair pra qualquer destino.
5. 🟠 **Atomicidade/TOCTOU** — worker morre entre efeito e COMMITTED → Task presa GATED com WhatsApp já enviado + budget preso.
6. 🟡 **Janela do ingest-token global legado** — até `scripts/migrate-webhook-tokens.ts` rodar em todas as instâncias e o global ser removido.
> Todos honestamente documentados pela própria equipe (`docs/ESTUDO_ARQUITETURA_BACKEND.md`). Regra de corte do projeto: passos 0–5 = 1º piloto governado; 6–9 = 10–50 tenants sem humano.

## Próximas tasks para o Code (Fable) — priorizado
1. **[P0]** Mergear `feat/whatsapp-connect-surface` → main (FF de 2 commits; destrava o QR). Já com 381 testes.
2. **[P0]** **HMAC do corpo** no elo worker→n8n (e endurecer antes de exposição pública do ingest).
3. **[P0]** Concluir migração de token **por-org** e **remover** o caminho global (kill-switch permanente).
4. **[P1]** **Rotação/versionamento de chave** do cofre (`keyVersion` no formato `iv:tag:ct:v` + DEK-envelope, ou script de re-cifragem).
5. **[P1]** **`catalog.ts` pricing v2**: à la carte independente + trial, **remover o Full**; alinhar `apps/api/src/billing/catalog.ts` ↔ espelho em `apps/web/lib/types.ts`.
6. **[P1]** Reconciliar a migração `20260620100000` onde estiver "failed" (`migrate resolve --applied`); cobrir o gotcha do `pnpm exec` engolir args no `db-migrate.sh`.
7. **[P1]** **RLS no Postgres** (defense-in-depth ao `where:{orgId}`) + `org_id` como FK.
8. **[P2]** **Fila com fairness por-tenant** (round-robin/quota) — resolve o head-of-line.
9. **[P2]** **Egress bloqueado** (proxy real, não log) + imutabilidade da Evidence no DB (trigger BEFORE UPDATE/DELETE).
10. **[P2]** Atualizar docs defasados: `ARCHITECTURE_HERMES.md` ("No code" falso), `LEAF_DOSSIE.md`/`ANDAMENTO.md`/`CHECKPOINT.md` (contagens antigas).
11. **[P3]** `brann-paired-e2e`: congelar fixture real do `confirmer.findMessages` num unit após o 1º pareamento.

## Drift de docs a corrigir (vault) — priorizado
- **🔴 P0 Pricing (Full R$2.497 morto):** `MEMORIA.md` (l.20 e l.31) · `60_Callima/base_conhecimento_callima.md` (l.27 — **é o RAG vendedor**) · `60_Callima/base-conhecimento-callima.md` (stale total) · `leaf_piloto1_ginkgo_kit.md` (l.17,25 + link Stripe). **Reconciliar as "3 Callimas"** (2 arquivos base_/base- divergentes = fonte-da-verdade ambígua do RAG).
- **🟡 P1 "Nomes reservados" (já decidido, resíduos):** `arquitetura_agentes_e_tiers.md` **l.3** (cabeçalho contradiz o corpo) · `inventario_visual.md` **l.37** (contradiz a l.62) · `sintese_decks_fonte.md` l.194/227 ("avaliar 4º orquestrador Shion" — superado).
- **⚪ P2 higiene:** MEMORIA título "Pricing (USD)" com conteúdo BRL; `contexto-callima.md` aponta p/ paths fora do vault; `identidade-ginkgo.md` semente vazia; pastas `30_Estrategia`/`80_Performance` vazias.

## Ações AO VIVO pendentes (máquina do fundador — não alcanço do sandbox)
- **A. Scan do QR + parear** → prova e2e da Callima governada. ⚠️ o trunk usa **número de teste** (parear o +5553 derruba a Callima interina que fatura). ⚠️ é o **momento da verdade do envio** (risco nº2 acima) — se todas as respostas voltarem ROLLED_BACK, é o parse do `brann-confirmer`.
- **B. Testar a dashboard LEAF como usuário normal** → precisa do stack `app` no ar (`docker compose --profile app --profile infra up -d`). Dá pra eu dirigir via **Claude-in-Chrome** se o app estiver em `localhost:3000` e a extensão conectada (cadastro → `/app/leaf/*` → falar com o Brann → conferir honest-data em inbox/CRM/agenda/ofertas/canal).
- **C.** `RESEND_API_KEY`+`EMAIL_FROM` no worker p/ o alerta de handoff por e-mail.
