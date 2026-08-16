# Hermes — Execution Runtime da Sylvia

**Status:** arquitetura aprovada; implementação pendente.

Hermes não é mais o cérebro da Sylvia e também não é um componente a ser aposentado. Seu papel oficial é **executor universal governado**.

Fonte arquitetural: `../../docs/feature_sylvia_execution_fabric.md`.

## Contrato

Hermes recebe uma missão já interpretada pela Sylvia/OpenClaw e autorizada pelo Agent OS.

```text
Sylvia/OpenClaw
  ↓ Mission
Agent OS
  ↓ Authorized Mission
Hermes
  ├─ Coding Fabric
  ├─ n8n
  ├─ browser
  ├─ MCPs
  └─ APIs
  ↓ Execution Result
Sylvia/OpenClaw
```

## Hermes pode

- operar terminal dentro do escopo autorizado;
- carregar skills permitidas;
- executar jobs e acompanhar processos;
- usar browser/MCP/API aprovados;
- disparar workflows n8n autorizados;
- delegar engenharia a OpenCode, Codex e Claude Code;
- operar repositórios somente segundo as permissões da missão;
- retornar logs e resultado estruturado.

## Hermes não pode por padrão

- substituir a identidade/memória canônica da Sylvia;
- ler segredos ou `.env` para alimentar modelos;
- alterar `main` diretamente;
- fazer deploy de produção apenas porque os testes passaram;
- gastar dinheiro, publicar, enviar ou apagar conteúdo externo sem gate aplicável;
- marcar missão de engenharia como sucesso sem checks.

## Coding Fabric

OpenCode é o executor preferencial elegível para tarefas delimitadas e econômicas. Codex e Claude Code permanecem disponíveis como fallback, alternativa ou reviewer independente.

A instalação/configuração real do OpenCode deve ocorrer somente na fase de implementação da spec; este arquivo **não afirma que OpenCode já esteja instalado**.

## Resultado mínimo de missão

Hermes deve devolver, quando aplicável:

```yaml
mission_id: DEV-...
status: SUCCESS | FAILED_GATES | BLOCKED | NEEDS_APPROVAL | NEEDS_CHANGES
executor: opencode | codex | claude-code | n8n | hermes
summary: "..."
artifacts:
  branch: "..."
  commit: "..."
  pull_request: "..."
checks:
  lint: pass | fail | skipped
  typecheck: pass | fail | skipped
  tests: pass | fail | skipped
  build: pass | fail | skipped
  security: pass | fail | skipped
approval_required: true | false
```

## Regra de promoção para n8n

Se uma tarefa executada pelo Hermes se tornar estável, previsível e repetitiva, avaliar sua transformação em workflow n8n. Hermes resolve exceções e tarefas abertas; n8n industrializa o processo.