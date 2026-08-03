# Sexta-feira — Sistema de Memória & Aprendizado Contínuo (a construir)

Objetivo: a Sexta-feira lembra cada conversa/prompt, aprende com elas, e absorve insights do
fundador via Obsidian (`_inbox`) — memória persistente + auto-refino + checkpoint padronizados.

## Memória canônica = UMA vault Obsidian (fim das duas memórias)
Local: `C:\sexta-feira\` aberto como vault no Obsidian (consolidar `docs/` + `memory/` aqui).
Estrutura:
- `HANDOFF.md` · `CHECKPOINT.md` · `00_INDEX.md` — estado rolante (ler no início).
- `CONTEXT_LOG.md` — append-only: cada sessão (data, decisões, prompts, aprendizados).
- `_inbox/` — **DROPS do fundador** (Obsidian Web Clipper / notas) → ingeridos a cada sessão.
- `prompts/` — todo prompt mandado pro Claude Code, versionado (pra refinar com o tempo).
- `decisions/` — ADRs (decisões com peso de lei). `learnings/` — padrões/insights destilados.
- `docs/` — specs (já existentes).

## Protocolo padronizado (vira SKILL.md da Sexta-feira)
- **INÍCIO de sessão:** ler HANDOFF + CHECKPOINT + INDEX; **varrer `_inbox/`** → validar contra
  invariantes → integrar ao contexto → mover p/ processado + logar no CONTEXT_LOG.
- **DURANTE:** cada decisão/prompt relevante → append no CONTEXT_LOG + salvar prompt em `prompts/`.
- **CHECKPOINT (fim / perto do limite de contexto):** atualizar CHECKPOINT + HANDOFF, resumir a
  sessão no CONTEXT_LOG, destilar novo padrão em `learnings/`. (auto-refino + checkpoint)
- **CONSOLIDAÇÃO periódica:** comprimir CONTEXT_LOG → `learnings/` (dedupe/refina) = aprendizado contínuo.

## Injeção via Obsidian (o "seus insights somam no meu contexto")
Fundador clipa/escreve no `_inbox/` a qualquer momento → na próxima sessão a Sexta-feira lê primeiro,
valida e promove a canônico (log no CONTEXT_LOG). É o canal oficial de aprendizado dirigido por você.

## Evolução futura (opcional)
Vetorizar a vault (pgvector) p/ recall semântico real; e, em runtime, separar disto a memória
per-tenant do Kernel (P004) — nunca misturar dev-memory com memória de cliente.

## STATUS: A IMPLEMENTAR — tarefa #1 da próxima sessão.
Passos: 1) consolidar docs/+memory/ na vault; 2) criar HANDOFF/CHECKPOINT/CONTEXT_LOG/_inbox/
prompts/decisions/learnings; 3) escrever a SKILL.md do protocolo; 4) migrar o handoff atual; 5) você
abre a pasta no Obsidian e testa um clip no _inbox.
