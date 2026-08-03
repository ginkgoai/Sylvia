# Hierarquia de capacidades do Hermes (Sexta-feira / Brann)

> Arquitetado com o Gabriel (2026-06-27). Como o motor Hermes alcança o mundo, organizado por **blast-radius** (raio de dano), governado por Laplace, pronto pra produção multi-tenant. Princípio: **least-privilege + contenção**.

## O princípio (a inversão que torna o uso natural)
A camada mais **sensível** (shell do host) fica no **topo** da atenção de governança e é o **último recurso**; a mais **contida** (serviço dockerizado) é a **base** e o **primeiro reach** pra rotina.
→ **O agente sobe a escada só quando a de baixo não resolve — e a cada degrau pra cima, o Laplace aperta.**
Toda **percepção** (leitura) é livre nas camadas (ADR 0002); todo **efeito** atravessa a Boundary como Skill governada, custe o que custar.

## A escada (apex sensível ▲ → base contida ▼)

**▲ 0 · Shell do HOST (PowerShell/nativo)** — toca o host inteiro. Blast-radius **MÁXIMO**.
- Governança: **R3 · HITL · só persona confiável**. **Só a Sexta-feira (você).** NUNCA um Brann de cliente.
- Uso: ops de host raríssimas, com aprovação explícita.

**1 · Python (sandbox)** — código arbitrário, mas num **container** (`terminal.backend=docker`).
- Blast-radius: contido ao sandbox. Governança: R2/R3, sandboxed.
- Quem: Sexta-feira + Brann (container **per-tenant**). Uso: transforms, lógica custom que nenhuma tool estruturada cobre.

**2 · MCPs / APIs** — MCP servers (percepção) + REST direto.
- Blast-radius: bounded pelo contrato da tool. Governança: **ler = livre · agir = Skill** pela Boundary.
- Quem: todos. Uso: perceber o mundo, chamar APIs definidas.

**3 · Integrações** — Stripe, Resend, Google (Cal/Gmail/Drive), Pix, Ads (depois).
- Blast-radius: escopo concedido. Governança: efeito = Skill (R2) · **dinheiro/credencial = R3/HITL**.
- Quem: todos (scopes per-tenant). Uso: ações em serviços externos contratados.

**▼ 4 · Serviços DOCKERIZADOS** — n8n (fluxos), AnythingLLM (RAG), Supabase (dados/auth), Evolution (WhatsApp), Postiz (social).
- Blast-radius: contido a cada serviço (tem a própria fronteira). Governança: read = livre · write/trigger = Skill (R1/R2).
- Quem: todos. **A base — onde a rotina mora.** Isolado per-tenant (workspace RAG do org, instância Evolution do org…).

## Onde os EFEITOS viram reais (o chokepoint)
As camadas são onde o agente **percebe** + o **menu** de Skills. Mas **todo efeito** — de qualquer camada — atravessa **um portão**: a **Security Boundary do ginkgo-tree = Laplace** (Task + orçamento + evidência + segredo do cofre + HITL se R3). **O Hermes pensa nas camadas; o Laplace é o portão de todo efeito.** (ADR 0002.)

## Split de produção (quem alcança até onde)
| Persona | Teto de camada | Por quê |
|---|---|---|
| **Sexta-feira** (você, pessoal) | **0** (host shell), governado | É o teu Jarvis — confiança alta, mas R3/HITL no host |
| **Brann / Nyra / Alfred** (cliente) | **1** (Python sandbox per-tenant) | **NUNCA** toca o host (camada 0). Container isolado por org. |
| **Sub-agentes do usuário** (ADR 0004) | **≤ teto do principal** | Herança: subconjunto estrito, risco ≤ pai |

Laplace impõe o teto **por Task** — não confia na persona, **verifica** no plano.

## Primeiro passo concreto (o bug vira arquitetura)
`terminal.backend = docker` (o conserto do `/bin/bash`) **É** implementar a camada 1: a execução de código sai do **host** (camada 0, perigosa) pro **sandbox** (camada 1, contida). Resolver o bug = começar a escada certa.

_Arquitetado com o Gabriel. Vira a base do tool-registry do Hermes + dos tetos de Laplace por persona._
