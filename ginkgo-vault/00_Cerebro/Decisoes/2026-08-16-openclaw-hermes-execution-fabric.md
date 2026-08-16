# Decisão — OpenClaw como cérebro, Hermes como executor e Coding Fabric

**Data:** 2026-08-16 · **Status:** Confirmada pelo fundador nesta sessão

## Decisão

1. **OpenClaw permanece como runtime principal da Sylvia** para identidade, canais, heartbeat, contexto, coordenação cognitiva e comunicação.
2. **Hermes não será aposentado.** A decisão de 2026-08-03 é parcialmente superada apenas no ponto que o classificava como runtime legado em desativação.
3. Hermes passa a ser a **camada executiva universal governada** da Sylvia: terminal, skills, browser, MCPs/APIs, coordenação de jobs e delegação para workers especializados.
4. A autorização de ações fica separada da execução por uma camada de **Agent OS / policy gate**, responsável por risco, permissões, orçamento, aprovações e auditoria.
5. É criada a arquitetura de **Coding Fabric**, com OpenCode, Codex e Claude Code como executores substituíveis.
6. **OpenCode** será o executor de código preferencial elegível para tarefas delimitadas e de menor custo, sem exclusividade.
7. **Codex e Claude Code** permanecem como alternativas/fallbacks e podem ser preferidos em tarefas de maior complexidade, risco, revisão ou necessidade de segunda opinião.
8. **n8n continua sendo a camada de automação determinística**. Processos estabilizados e repetitivos devem tender a migrar de missões abertas do Hermes para workflows n8n.
9. **GitHub é a fonte de verdade da engenharia**: coding workers atuam em branch/worktree/sandbox; `main` não recebe escrita direta por padrão.
10. Nenhum executor de código recebe segredos, `.env`, tokens ou credenciais. Produção e merge seguem gates independentes.
11. "Processo terminou" não equivale a "missão concluída": uma missão de engenharia só pode ser marcada `SUCCESS` depois dos quality gates aplicáveis.

## Contrato conceitual

```text
Fundador
  ↓
Sylvia / OpenClaw
  ↓ intenção + contexto
Agent OS
  ↓ autorização
Hermes
  ├─ Coding Fabric → OpenCode / Codex / Claude Code → GitHub
  ├─ n8n
  ├─ Browser
  └─ MCPs / APIs
  ↓ resultado estruturado
Sylvia
```

## Invariantes

- Cognição e identidade da Sylvia não dependem do Hermes.
- Execução técnica não precisa ocorrer dentro do OpenClaw.
- Workers são substituíveis por política de custo × risco × complexidade.
- Segredos ficam fora da cognição e fora do contexto dos coding workers.
- `main` e produção são fronteiras protegidas.
- Toda missão relevante deixa trilha auditável.

## Spec

Arquitetura completa: `docs/feature_sylvia_execution_fabric.md`.

## Relação com a decisão de 2026-08-03

Permanece válida a decisão de que Sylvia usa OpenClaw como runtime principal e mantém cognição agnóstica de runtime. É **revogado apenas o entendimento de que Hermes deveria entrar em desativação**. Hermes retorna com função diferente da Sexta-feira v1: não como cérebro, mas como executor subordinado e governado.