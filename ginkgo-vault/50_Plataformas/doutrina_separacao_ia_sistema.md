# Doutrina — Separação IA ↔ Sistema (validação externa)

> 2026-07-01. A tese que rege o Ginkgo — **a IA interpreta; um sistema governado executa e é o registro** — não é preferência nossa: é o consenso de quem já se queimou. Aqui, as fontes (clipps do cofre) + como o Ginkgo já a encarna. Citável em produto/venda e como lastro de arquitetura.

## A tese
- **IA = intérprete/planejador** — probabilístico, não-reproduzível. Interpreta, resume, propõe.
- **Sistema governado = executor + sistema-de-registro** — determinístico, auditável. Decide o efeito, executa, guarda a prova.
- **honest-data é a consequência estrutural**, não uma feature: a fala só afirma o que o sistema **provou** (a Callima nunca diz "agendei"/"paguei" sem o efeito real).

## Validação externa (3 fontes independentes convergem)
- **gotoCobol — "por que projetos de IA são cancelados":** *"interpretar não é a mesma coisa que executar um processo de negócio"*. Projetos morrem quando pedem a um componente probabilístico pra ser o executor/decisor/registro. Em sistema que registra dinheiro, **previsibilidade > inteligência**.
- **Uplatz — AI-native data:** o agente nunca pode ter escrita/leitura crua — só via **API governada** + metadata/permissões; vector cru alucina em dado velho. Governança transforma o repositório de risco em sistema confiável.
- **agent-kernel — OS p/ agentes:** governança (hooks pré/pós, auditoria, traceability) é **first-class, não afterthought**; o modelo é peça trocável sobre um **kernel durável**.

## Onde o Ginkgo já encarna (ponto a ponto)
- **Callima/Hermes = o intérprete** — emite intenção, nunca executa efeito.
- **Boundary/Laplace = o executor governado + registro** — Task + orçamento + Evidence; segredo do cofre; confirmer independente.
- **honest-data** = a prova ancora a fala (o LLM nunca gera "configurei/agendei"; quem diz é o resultado real).
- **white-label + model-router** = o **moat é a governança/OS**, não o modelo. É a aposta **oposta** ao Sigma BankAI (que funde IA+execução e chama o modelo de moat — colapsa exatamente a separação que as outras fontes defendem, e quebra no primeiro processo determinístico).

## Implicações acionáveis (o que os clipps PUXAM)
1. **RAG per-tenant = governado** (metadata + permissões + Skill de escrita `adicionar_conhecimento`), NÃO similaridade crua do AnythingLLM. → embutir no prompt do RAG.
2. **Estado durável mora no sistema** (DB/Evidence), não na cabeça do modelo (P004: dev-memory ≠ tenant-memory; ADR-0004: criar seleciona poder, não concede). Nada de agente que se auto-modifica no runtime governado.
3. **O risco não é a arquitetura — é DISCIPLINA:** não deixar a conveniência colapsar a separação. Exemplo vivo: o quase-furo da `GROQ_API_KEY` no `.env` (violaria o #8 e escaparia da redação do Boundary) — a **auditoria adversarial pegou** antes do commit. O loop com auditoria É a disciplina operacionalizada.

> Fontes: `Clippings/` — "Por que tantos projetos de IA estão sendo cancelados" · "AI-Native Data Platforms (Uplatz)" · "yaalalabs/agent-kernel" · (contraponto) "Sigma BankAI".
