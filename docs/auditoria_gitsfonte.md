# Auditoria — GITS FONTE (estado + o que é ruído)

Objetivo: GITS FONTE = lar ÚNICO da plataforma (3 corpos, back+front, site/vendas, n8n,
hermes, agents). Hoje há **várias gerações acumuladas** — mapa e recomendação abaixo.

## Estado atual (8 pastas top-level)
| Pasta | O que é | git/pkg | últ. | tam* | Veredito |
|---|---|---|---|---|---|
| **ginkgo-tree** | TRONCO canônico (Fable: Kernel/Boundary/3 corpos, back+front) | repo aninhado (.git em ginkgo-tree/ginkgo-tree) | 20/06 | 1736 MB | **MANTER (canônico)** |
| **compose stack** | Ops vivo: n8n workflows, **hermes**, ginkgo-discord, ginkgo-vault, data | sem git | 20/06 | 192 MB | **MANTER (infra viva — roda a Callima)** |
| **landing page ginkgo-sale** | Site institucional (ginkgo-ai-site-main) + portfolio | sem git | 19/06 | 255 MB | **MANTER (site)** — checar `portfolio` |
| **leaf** | MVP Supabase (github gingkosystems/leaf) = doador de UX | repo `leaf` | 20/06 | 15 MB | **MANTER TEMP** → arquivar após portar UX |
| **ginkgo-dashboard** | Geração ANTIGA "ginkgo-platform" (pkg ginkgo-leaf), superseded pelo tronco | repo `ginkgo-platform` | commit 27/04 | 41 MB | **MOVER (legado)** |
| **wave** | Cópia do leaf (pkg LEAF-leaf), SEM git — não é o Wave real | sem git | — | 563 MB | **MOVER (legado/ruído)** |
| **agents** | Experimentos: "agent jury", "ginkgo-s-plus" | sem git | 07/06 | 222 MB | **MOVER (referência)** — checar antes |
| **pyre** | ginkgo-pyre (stub antigo) | sem git | 27/04 | 1 MB | **MOVER (legado)** |
*tam = sem node_modules (aprox.).

## Diagnóstico
GITS FONTE virou um "cemitério de gerações": o **tronco** (ginkgo-tree) é o canônico; ao lado
convivem o platform antigo (ginkgo-dashboard), scaffolds per-corpo velhos (pyre, wave=cópia de
leaf), experimentos (agents) e o MVP (leaf). Isso confunde e ocupa ~830 MB+ de ruído.

## Recomendação — GITS FONTE limpa (foco: plataforma)
**MANTER (4):** `ginkgo-tree` (tronco) · `compose stack` (ops/infra viva) · `landing page
ginkgo-sale` (site) · `leaf` (temporário, doador de UX até portar).

**MOVER PRA FORA → `_legacy_ginkgo\` (irmã da GITS FONTE, NÃO deletar):**
- `ginkgo-dashboard` (platform antigo) — história no GitHub (gingkosystems/ginkgo-platform), seguro arquivar.
- `wave` (cópia de leaf, sem git) — 563 MB, maior ganho.
- `pyre` (stub antigo).
- `agents` (experimentos) — **conferir conteúdo antes** (222 MB; pode ter algo útil de prompt/jury).

**LIMPEZA (no que fica):**
- Achatar `ginkgo-tree\ginkgo-tree` → subir 1 nível (fim do duplo-aninhamento).
- `ginkgo-tree` (1.7 GB): apagar `.next`/build e `backups/` versionados que incham (regeneráveis).
- Apagar `node_modules` de leaf/ginkgo-dashboard/wave antes de arquivar (regeneráveis; menos churn OneDrive).
- `landing page ginkgo-sale/portfolio`: conferir — se não for o site, é ruído.

## Visão-alvo (futuro próximo)
GITS FONTE = **ginkgo-tree** (plataforma: back, front, 3 corpos) + **site** + **compose stack**
(ops, até integrar n8n/hermes como infra do tronco). leaf sai após portar a UX. Nome ideal do
tronco sem duplo-aninhamento.

## Cuidados antes de mover (IMPORTANTE)
1. **Não mover o que roda:** `compose stack` fica (Callima/Hermes vivos).
2. **Repos git:** confirmar `git push` em dia (ginkgo-dashboard, leaf) — história fica salva no
   GitHub antes de arquivar local.
3. **OneDrive:** mover pastas grandes gera sync; melhor apagar node_modules/.next primeiro.
4. **Mover, nunca deletar** nesta fase — `_legacy_ginkgo` guarda tudo até validarmos o tronco 100%.
5. Eu NÃO movo nada sem seu OK (operação de alto impacto na sua workspace).

## Ganho estimado
Mover wave+agents+ginkgo-dashboard+pyre ≈ **~830 MB** (+ node_modules de cada) fora da GITS FONTE,
deixando 4 pastas claras e sem ambiguidade de "qual é o real".

---
## 2ª passada (interna às 4 pastas vivas) — AGUARDA OK (nada movido)
Lembrete de propósito: tudo é a plataforma Ginkgo; n8n terá pastas com tudo pra stack/leaf/dark-social,
orquestrado pela Sexta-feira. Logo: workflows = ATIVO (relocar, não descartar).

### A) Ruído claro → _legacy_ginkgo (ou apagar)
- `landing page ginkgo-sale/ginkgo-ai-site-main.zip` (167 MB) — zip do site (a pasta extraída está do lado).
- `ginkgo-tree/ginkgo-tree/_quarantine/editar/stack aelora` — projetos NÃO-Ginkgo (Aelora/Hamateatsu/
  codex zips, audit, inventario.csv). Ruído real.
- `compose stack/docker-compose.yml.bak-C0.1` + `.bak-temporal` — backups antigos do compose (pequenos).

### B) ATIVO valioso → RELOCAR (não é lixo)
- `ginkgo-tree/ginkgo-tree/_quarantine/editar/workflows` = **121 workflows n8n** (auto-post multi-rede,
  vídeo viral, bots WhatsApp, SEO, scrapers, RAG). Mover pra uma **biblioteca** da plataforma:
  sugestão `compose stack/workflows/_biblioteca/` (matéria-prima p/ Pyre, redes dark, Wave).

### C) Regeneráveis (apagar só com OK; NÃO quebra Docker — tronco roda em container)
- `ginkgo-tree/ginkgo-tree/node_modules` + `apps/web/.next` (regenera com pnpm install/build).
- `leaf/node_modules` + `leaf/apps/web/.next` (leaf é doador; pode enxugar).

### D) Funcional — MANTER (não mexer)
- `ginkgo-tree/ginkgo-tree/backups/` = dumps de DR reais (F1) — manter (opção de tirar do repo depois p/ não inchar).
- compose stack: data, ginkgo-vault, hermes, ginkgo-discord, workflows, PROJETO. Tudo plataforma.

### E) Reestruturação (delicada, DEPOIS que o Claude Code soltar o tronco)
- Achatar `ginkgo-tree/ginkgo-tree` → `ginkgo-tree` (fim do duplo-aninhamento) e re-apontar docker compose.

Ordem segura quando você der OK: A (mover) → B (relocar workflows) → C (apagar regeneráveis) → E (depois).
