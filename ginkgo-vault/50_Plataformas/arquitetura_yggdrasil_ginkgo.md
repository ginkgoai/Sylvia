# Cérebro Agêntico Operacional — "Loki no Trono de Yggdrasil" no ginkgo-tree

> Reestruturação (2026-06-26) do conceito agêntico do fundador **sobre a arquitetura REAL** do `ginkgo-tree`.
> **Yggdrasil não é metáfora solta — é o próprio `ginkgo-tree`** (o tronco). Honest-engineering: cada conceito mapeado no componente real, com status (✅ existe · ⚠️ parcial · 🔜 próximo · ❌ white-space). Lei: o `ARCHITECTURE_AGENT_RUNTIME.md` do tronco prevalece.

## A tradução (o estilo → o real)
- **Yggdrasil (árvore cósmica)** = o **`ginkgo-tree`** (o tronco / monorepo). O ginkgo já é uma árvore; o repo já é tronco + branches + folhas.
- **Loki (a mente no trono)** = **Hermes** — a **mente ÚNICA** de todos os corpos: *"uma mente, três faces"*. Percebe → raciocina → **emite Task**. **Nunca executa efeito, nunca escolhe modelo, nunca toca segredo.**
- **O trono que governa** = **Laplace** — Kernel + Boundary + Policy + Observability. Não-cognitivo de propósito: *"a ausência de cognição É o modelo de segurança."*
- **Os nove reinos** = os tenants/domínios servidos.

## Mapa (conceito → ginkgo-tree → status)

| Loki / Yggdrasil | ginkgo-tree (real) | Status |
|---|---|---|
| Yggdrasil (árvore cósmica) | **ginkgo-tree** (tronco/monorepo) | ✅ |
| Loki Core no trono (orchestrator) | **Hermes** — mente única, perceive→reason→**emite Task** | ✅ engine real (`hermes.reply`, `hermes.chat`) |
| Quem governa o trono | **Laplace** — Kernel+Boundary+Policy+Observability | ✅ |
| Raiz / North Star | Maximizar valor ao cliente — governado e honesto | — |
| Tronco (core memory & state) | **Kernel** (`packages/core`: states, contratos Zod, `resolveSkill`, `TaskRunner`) + **pgvector** por-tenant | ✅ Kernel · ⚠️ embeddings faltam |
| Ramos (domínios estratégicos) | **LEAF / WAVE / PYRE** = faces **Brann / Nyra / Alfred** do Hermes | ✅ LEAF · 🔜 PYRE/WAVE conceituais |
| Folhas/twigs (ações atômicas) | **Skills → Tasks** executados pela **Boundary** (n8n cego / MCP / API) | ✅ LEAF skills + executor n8n |
| Pruning (mata branch ruim) | **Maturity ladder** `simulation→shadow→production` + HITL + evidência (invariante #7) | ✅ |
| Sacred Timeline (caminho aprovado) | **Decisão Congelada** + **registry epochs** (`resolveSkill` roda 1×, congelado na lineage) | ✅ |
| Timelines paralelas (multiverso) | paralelismo de execução de branches | ❌ white-space |
| Hierarquia de propósito | **uma mente → faces** (`max_risk`, `skill_scope`) → **sub-agentes** (subset herdado; teto = `min(face, tenant)`) | ✅ persona/topology registry |
| Vector Store "Yggdrasil Memory" | **pgvector por-tenant** (P004), RAG-native — Brann alimenta, todos leem | ⚠️ pronto, embeddings/memória faltam |
| Multi-vector RAG + hybrid + rerank | memória em camadas bruto/refinado/RAG (task #13) | 🔜 a desenhar |
| n8n flows = "portais dimensionais" | **n8n** executor cego, versionado — 2 instâncias (Runtime governado `:5679` + Ops) | ✅ |
| Skills/Tools registry vetorizado | **Skill Registry** event-sourced (Intent→Skill, resolves-never-executes) + Persona Registry | ✅ (discovery por similaridade = 🔜) |
| Observability "árvore de timelines" | **Laplace Observability** + dashboard ("analista de operação") | ✅ plano · 🔜 painel visual |
| Self-improvement loop | skills agent-authored nascem em `simulation`, promovidas com evidência | 🔜 ladder existe, geração não |

## Os 4 Ramos funcionais (hierarquia de propósito sob o Hermes)
> **Dois eixos ortogonais, não confundir:** as **3 faces** (Brann/Alfred/Nyra) = *quem* atende (persona por plataforma); os **4 ramos** = *como* o Hermes age (capacidades que TODAS as faces usam). **Hermes no topo orquestrando**; cada ramo é uma sub-árvore de propósito com tags vetorizadas.

1. **Ramo de Execução (Action Branches)** — Skills (`docx/pdf/pptx/xlsx/ffmpeg` no plano Cowork; `LEAF_SKILLS` no produto), Tools (function calling), APIs externas, MCPs. No tronco = **Skills governadas pela Boundary** (efeito = Task + budget + evidência). Regra de ouro (ADR 0002): **MCP percebe (lê) · Skill age (efeito pela Boundary).** ✅ Skill Registry + Boundary · 🔜 catálogo amplo.
2. **Ramo de Integrações & Automação** — **n8n = "portais dimensionais"** (workflows reutilizáveis, executores cegos; 2 instâncias: Runtime governado `:5679` + Ops). Trigger: o Hermes detecta o padrão → invoca o fluxo via webhook/API. **← é exatamente o `[[AGENDAR]]` → branch determinístico que estamos construindo.** 🔜 versionar + **embedar cada fluxo no vector store** (discovery por similaridade). ✅ executor n8n real.
3. **Ramo de RAG & Conhecimento** — **pgvector por-tenant (P004) = "Yggdrasil Memory"**. Multi-vector RAG (chunks + metadata + **hierarchical purpose tags**), Hybrid Search (keyword + vector + **graph traversal** dos relacionamentos de propósito), Self-Improvement Loop (artefato novo → auto-chunk + index). ⚠️ pgvector pronto, embeddings/memória em camadas (bruto/refinado/RAG) = task #13.
4. **Ramo de Canais (Communication & Multi-Modal)** — os **Channel Adapters**: WhatsApp (Callima/Evolution), Chat (`hermes.chat` na dashboard), Email (Gmail→Resend), Docs/Slides/Vídeo/Imagem. Multi-modal embeddings (texto+imagem+áudio) — a Callima já faz STT/TTS + análise de imagem/vídeo/doc. ✅ WhatsApp+chat+áudio+visão · 🔜 email · docs/slides/vídeo via Ramo de Execução.

**Decisão (Loki):** Hermes embeda a query → similarity search na hierarquia de propósito → escolhe **ramo + folha** → dispara (Skill/n8n/MCP/canal) → observa → **prune** (maturity ladder) → **weave** o sucesso na Sacred Timeline + atualiza a memória.

## Como Loki opera (mapeado, honest-data)
1. **Input → percebe + RAG** (purpose hierarchy + memória por-tenant). _RAG ⚠️ embrionário._
2. **Decompose →** quebra em **Tasks** (sub-árvore de propósito).
3. **Plan →** `resolveSkill` **congela a decisão** na lineage. _Paralelismo de timelines = ❌._
4. **Execute →** a **Boundary** executa o Skill (n8n cego / MCP / API). **O Hermes nunca toca o efeito nem o segredo.**
5. **Observe & Reflect →** confirmer independente + Laplace Observability → **prune** (ladder).
6. **Weave →** o **resultado real** entra na Sacred Timeline (lineage) + atualiza memória/dashboard. **Honest-data: só confirma no sucesso.**
7. **Output →** canal certo (Callima fala) + atualiza a hierarquia de propósito.

## Onde a fatia de hoje encaixa
A primeira folha que estamos endurecendo é o **ramo LEAF**:
> **Callima** (a folha que o cliente toca) ← **Brann** (a face orquestradora do Hermes no LEAF) → **Task** → **Boundary** executa → **resultado real** → Callima confirma.

O `[[AGENDAR]]` é a **primeira twig determinística** desse ramo (ver `arquitetura_callima_hermes.md`). Cada nova skill = uma twig nova, governada, registrada — **sem inchar a folha**.

## Honest-engineering (real vs north star)
- **REAL hoje:** Kernel (Tasks / HOLD-SETTLEMENT / HITL / lineage), Security Boundary (vault inject/redact, `executor_ref` HMAC, confirmer independente), Skill Registry, **LEAF vivo** (`hermes.reply`/`hermes.chat`, WhatsApp, inbox/CRM, **bridge `/ingest/lead` provado**), billing Stripe + carteira GTK, shell da dashboard.
- **NORTH STAR (aspiracional):** memória vetorial/embeddings, PYRE/WAVE (Nyra/Alfred), timelines paralelas, skills agent-authored, engine completo de purpose-hierarchy, discovery vetorizado de skills.
- **A regra:** Yggdrasil é o **norte**; a **escada** (maturity ladder + o loop COWORK/CODE) é **como** subimos — sem pular degrau, sem prometer o que não existe.

_Mantido pela Sexta-feira. O `ginkgo-tree` **é** a Yggdrasil; este doc é o mapa do trono._
