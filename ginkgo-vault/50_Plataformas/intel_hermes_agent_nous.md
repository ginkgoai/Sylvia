# Hermes Agent (Nous) × Ginkgo — entendimento CORRETO

> ⚠️ RETRATAÇÃO (2026-06-27): a versão anterior deste doc dizia "colisão de nome / construir vs adotar / renomear". **Estava errada.** Eu tinha buscado só no `ginkgo-tree` e não vi o Hermes Agent. O Gabriel corrigiu; reli o projeto. Abaixo, o correto.

## A verdade (medida no repo + compose)
O Gabriel **adotou o Hermes Agent da Nous Research de propósito** — ele É o motor cognitivo do Ginkgo.

- **Comentário no `ai-stack/docker-compose.yml`:** *"o antigo serviço FastAPI 'hermes' foi aposentado. O nome 'Hermes' agora pertence ao agente Nous (projeto Sexta-feira), que roda NATIVO no Windows (fora do compose) em `C:\sexta-feira`."*
- **`C:\sexta-feira`** = o projeto **Sexta-feira** (o Hermes Agent rodando nativo): `hermes/` + `hermes/skills/` + `memory/` (learning loop), `callima/`, `bridges/`, `dashboard-orb/`, `db/`, + o `ginkgo-vault/`.

## O modelo correto
- **Hermes Agent (Nous) = o motor = "Sexta-feira"** — nativo em `C:\sexta-feira`. Self-improving, skills, memória cross-session.
- **Rostos (personas, config por tenant):** **Brann** (LEAF) · **Alfred** (WAVE) · **Nyra** (PYRE) · e no tronco inteiro, **Sexta-feira**. Motor compartilhado; persona = nome/voz/escopo.
- **Laplace** (em `ginkgo-tree`: Kernel + Boundary + Política + Observabilidade) = a governança **sem cognição** que limita o motor. *"Hermes pensa; Laplace governa."*
- **`ginkgo-tree`** = camada de **produto + Kernel/Laplace** (api/worker/web · LEAF/Callima/dashboard/billing) que envelopa o motor. O "Hermes" da doc = o papel que o agente Nous preenche.
- **`ai-stack`** = infra de apoio (n8n, evolution, anythingllm, postgres, redis).

## A pergunta em aberto (confirmar com o Gabriel, não assumir)
A `ARCHITECTURE_AGENT_RUNTIME.md` §5 marca, no REAL-vs-CONCEITUAL, "delegate chama OpenRouter direto" como o real de hoje. O balão do Brann que testei (50 tokens) foi o **delegate próprio do worker** (ginkgo-tree), não vi roteamento explícito pro Hermes Agent.
→ **A confirmar:** o Brann do dashboard já roda ATRAVÉS do Hermes/Sexta-feira, ou ainda é o delegate do tronco e **plugar os dois é a meta**? Isso define o próximo passo de integração.

## Padrão útil (continua valendo)
O `self-improving-agent` (`.learnings/`) é o mesmo conceito do `memory/` do Hermes Agent — logar erros/correções/insights e promover pro contexto. Já temos material desta sessão (gotcha `127.0.0.1` do Prisma, `node --env-file` do worker, `next dev` podre).

_Corrigido pela Sexta-feira após reler o projeto._
