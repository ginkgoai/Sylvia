# Callima → Hermes: estado real + plano de migração

> Pergunta do Gabriel (2026-06-27): "usamos o mesmo OpenRouter da Callima, tá ok? o Hermes já cumpre o papel?" — resposta honesta abaixo, com o plano de unificação sem derrubar venda.

## Estado real (honest-data — o que RODA hoje)

Existem **duas implementações** que conversam com OpenRouter:

1. **Callima no n8n** (workflow `zo9FqQ9XVRcU8AJZ`) — **a que fatura**. Serve o WhatsApp ao vivo. Usa uma **credencial OpenRouter configurada no próprio n8n** (key da plataforma/Ginkgo). Governança = tags determinísticas (`[[LEAD]]`, `[[AGENDAR]]`) + branches do n8n (uma Boundary de pobre, mas honesta).

2. **Tronco (Brann + cognição worker-side)** — **já é Hermes de verdade**:
   - `hermes-chat-delegate.ts` (o Balão do Brann no dashboard) chama OpenRouter real, via **Kernel Task + cofre + Boundary + economia de token** → marcado **🟢 REAL** na doc.
   - A `openrouter_api_key` vive **no COFRE por org** (AES-256-GCM, via `put-secret.ts`), **nunca** no env do worker — modelo **per-tenant**.
   - O design é **cognição worker-side, NUNCA n8n** (CHECKPOINT: "the agent is ALIVE: inbound → Kernel Task → REAL LLM").
   - M4-01 (`feat/brann-onboarding`) adicionou: **Model Router por papel** (`brann.concierge`→forte `BRANN_MODEL`, `callima.reply`→barato `CALLIMA_MODEL`) + concierge de onboarding + config-write governado.

**Resumo:** o **Hermes-engine existe e roda** (no Balão do Brann). A **Callima ao vivo ainda é o n8n** — uma ilha separada. Falta **mover o atendimento de WhatsApp do n8n → worker do tronco**, aí a Callima vira face real do Hermes.

## OpenRouter — mesmo? está ok?

- **n8n** usa a credencial OpenRouter dele (key Ginkgo). **Tronco** usa `openrouter_api_key` **por org, no cofre**.
- **Mesma CONTA?** quase certo (você tem uma OpenRouter só). **Mesma KEY?** só se você carregou a mesma key na org Ginkgo via `put-secret.ts`. _As duas estão cifradas — não dá pra ler o valor e comparar; você sabe se são iguais._
- **Está ok?** Sim. E o modelo do tronco (**key per-tenant no cofre**) é o **alvo** — melhor que a credencial única do n8n. Caveats: custo/rate-limit/rotação compartilhados se for a mesma key (mede custo no `token_ledger`, não no painel da OpenRouter).
- ⚠️ Achado conhecido (doc backend, [high]): o **egress allowlist é decorativo** (só `log()`, não bloqueia) — endurecer antes de prod robusta.

## Plano de migração (strangler-fig, zero downtime)

> Princípio: **não refatorar o money-maker no meio do lançamento.** A Callima-n8n é "boa o bastante" pra vender. Migra quando o tronco estiver em **paridade comprovada**.

1. **Shadow** — o worker do tronco consome o **mesmo webhook da Evolution** em paralelo, gera resposta mas **NÃO envia** (só loga). Compara tronco-Callima × n8n-Callima no tráfego real. _Mede antes de trocar._
2. **Canary** — roteia **1 número de teste** (o teu) pro caminho do tronco; n8n segue servindo o resto. Valida ponta-a-ponta: LLM + envio + `[[AGENDAR]]`/`[[LEAD]]` viram **Skills governadas reais** pela Boundary.
3. **Cutover por-tenant** — vira tenant a tenant (webhook da Evolution → worker do tronco, não n8n). Cada virada é **reversível** (reaponta o webhook).
4. **Aposenta a cognição no n8n** — quando todos os tenants estão no tronco, o n8n fica só com o que é bom (glue visual) ou sai do caminho da Callima.

### Quando
- **Agora:** NÃO. Termina o demo + pega os primeiros clientes na Callima-n8n.
- **Gatilho:** tronco-Callima em paridade (shadow-testada) **E** fôlego pós-lançamento.
- **Risco se cedo:** quebra a venda ao vivo. **Risco se tarde:** duas implementações divergindo (drift).

_Mantido pela Sexta-feira._
