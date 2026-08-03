# Auditoria de infra — onde roda o Brann-produto (motor Hermes)

> Pedida pelo Gabriel (2026-06-27). Lida do compose de prod + infra_alvo_vps + a config real do Hermes. honest-data, com números.

## Fato 1 — o local está MAXADO
Tua própria `infra_alvo_vps.md`: *"máquina HONRADO, 16GB, Docker VM 8GB — no limite… **Não cabe mais nada.**"* O **ai-stack** (n8n+Evolution+AnythingLLM+Postgres+Redis+Postiz+Temporal) + o **tronco** (api+web+db) já enchem a VM. **Não há espaço pro motor Hermes-produto rodar local.**

## Fato 2 — o motor Hermes é PESADO
Config real (`config.yaml`): `terminal.backend=docker` com **`container_memory: 5120` (5 GB) · `container_disk: 51200` (50 GB) · `container_persistent: true`** — POR code-exec. Multi-tenant = um sandbox de 5 GB persistente **por org**. Numa VM de 8 GB já cheia, **nem UM cabe**.

## Fato 3 — o compose de prod ainda não tem Hermes
`docker-compose.prod.yml` = postgres · redis · api · worker · web · cloudflared. Leve, cabe local (é a Fase-0 do túnel). O motor Hermes seria um serviço NOVO — que não cabe aqui.

## Conclusão — staging honesto (desbloqueia o demo)
A convergência "Brann = Hermes" **não é tudo-ou-nada**. Separa por peso:

**▸ Demo + primeiros clientes (Fase-0, LOCAL):**
Brann = o **delegate governado do tronco (M4-01, já funciona)** — chat de onboarding + config-writes governadas (configurar Callima, ofertas) pela Boundary. **Leve, roda local, suficiente pra "usuário entra → configura → usa".** O demo **NÃO precisa** do motor Hermes pesado. **Zero bloqueio de infra.**

**▸ Produção / Brann-Hermes-completo (Fase-1, VPS):**
O motor Hermes inteiro (tools, skills, learning-loop, code-exec) = serviço no compose, numa **VPS dedicada** (8 vCPU / 16–32 GB), com **sandbox ESCALÁVEL** — efêmero/right-sized **OU serverless (Modal/Daytona, que o Hermes suporta nativo — hiberna ocioso, custa ~nada)**, **NUNCA** 5 GB persistente por tenant. A convergência multi-tenant É o gatilho de migração que tua doc já listou ("vários tenants reais").

## Recomendação (resposta à pergunta "onde roda")
1. **Agora:** demo no **delegate leve** (M4-01) — segue sem esperar infra. A **Sexta-feira pessoal** (full Hermes, 1 profile) aparece no demo como **preview** do que o Brann vira.
2. **Brann = Hermes completo** = **Fase-1 na VPS**, sandbox **serverless** (Modal/Daytona), profile-per-tenant, governado por Laplace. Vira um serviço no `docker-compose.prod.yml` do deploy VPS.
3. **Não** subir o motor pesado no teu Windows nem no compose local — o `terminal.backend=docker` que apliquei é o caminho certo **no deploy VPS**, não no host pessoal.

## Decisão pendente (Gabriel)
- Topo: **demo no delegate leve agora + Hermes-completo na VPS depois** — fecha?
- Quando subir a VPS: 1 robusta (8vCPU/16-32GB) roda produto + motor; sandbox serverless pro code-exec dos tenants.

_Auditado pela Sexta-feira. O motor pesado mora em infra dedicada; o demo não espera por isso._
