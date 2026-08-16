# Feature Architecture — Sylvia Execution Fabric

**Status:** 📋 Specado  
**Data:** 2026-08-16  
**Escopo:** arquitetura de execução da Sylvia  
**Decisão canônica:** `ginkgo-vault/00_Cerebro/Decisoes/2026-08-16-openclaw-hermes-execution-fabric.md`

## 1. Resumo executivo

Sylvia permanece com **OpenClaw como runtime principal de identidade, canais, contexto e coordenação cognitiva**. Hermes deixa de ser tratado como runtime legado em desativação e passa a ocupar um papel explícito: **camada executiva universal** da Sylvia.

A regra é:

- **OpenClaw = quem Sylvia é e como ela pensa/coordena.**
- **Agent OS = o que Sylvia está autorizada a fazer.**
- **Hermes = como Sylvia executa trabalho técnico e operacional.**
- **OpenCode / Codex / Claude Code = workers especializados de engenharia.**
- **n8n = automação determinística e workflows repetíveis.**
- **GitHub = fonte de verdade do código, branches, PRs e histórico técnico.**
- **Laplace + memória canônica = contexto recuperável; não executor.**

OpenCode entra como executor de código preferencial para tarefas compatíveis com custo baixo/gratuito. Codex e Claude Code permanecem disponíveis como executores alternativos/premium conforme risco, complexidade, qualidade necessária ou fallback.

## 2. Objetivo da feature

Criar uma camada modular em que Sylvia possa receber uma intenção de alto nível e delegar execução sem acoplar sua cognição a um único executor, modelo ou ferramenta.

Exemplo:

```text
Fundador
  ↓
"Corrija o onboarding do Leaf"
  ↓
Sylvia / OpenClaw
  ↓ intenção + contexto + classificação
Agent OS
  ↓ política + risco + orçamento
Hermes
  ↓ missão técnica
Coding Router
  ├─ OpenCode
  ├─ Codex
  └─ Claude Code
  ↓
worktree/branch → implementação → gates → PR
  ↓
Hermes coleta resultado
  ↓
Sylvia interpreta e reporta
```

## 3. Não objetivos

Esta feature **não**:

- substitui OpenClaw pelo Hermes;
- dá acesso irrestrito do Hermes ou dos coding workers à produção;
- permite leitura de `.env`, chaves, tokens ou segredos por modelos;
- permite merge direto em `main` por padrão;
- transforma n8n em agente cognitivo;
- transforma OpenCode em cérebro da Sylvia;
- elimina Codex ou Claude Code.

## 4. Arquitetura alvo

```text
                         FUNDADOR
                            │
                            ▼
                 ┌────────────────────┐
                 │       SYLVIA       │
                 │      OpenClaw      │
                 │ identidade/canais  │
                 │ contexto/decisão   │
                 └─────────┬──────────┘
                           │ Mission
                           ▼
                 ┌────────────────────┐
                 │      AGENT OS      │
                 │ policy/risk/budget │
                 │ approval/audit     │
                 └─────────┬──────────┘
                           │ Authorized Mission
                           ▼
                 ┌────────────────────┐
                 │       HERMES       │
                 │ execution runtime  │
                 │ skills/tools/jobs  │
                 └─────────┬──────────┘
                           │
        ┌──────────────────┼─────────────────────┐
        │                  │                     │
        ▼                  ▼                     ▼
  CODING FABRIC           n8n              Browser/MCP/API
        │            deterministic          external tools
   ┌────┼─────┐       workflows
   ▼    ▼     ▼
OpenCode Codex Claude Code
   │
   ▼
GitHub worktree/branch/PR
```

Memória e conhecimento alimentam o plano, mas não ficam no caminho crítico de execução:

```text
Laplace / Supabase / ginkgo-vault
              ↑
              │ retrieval / evidence
              ↓
         Sylvia / OpenClaw
```

## 5. Responsabilidades por componente

### 5.1 OpenClaw — cérebro operacional da Sylvia

Responsável por:

- identidade e persona persistente;
- canais e conversação;
- heartbeat/proatividade;
- interpretação da intenção do fundador;
- composição de contexto;
- classificação de missão;
- decisão de delegar;
- síntese e comunicação do resultado.

OpenClaw **não deve executar diretamente toda tarefa técnica pesada** quando existir um executor especializado.

### 5.2 Agent OS — governança

Responsável por:

- classificar risco;
- conferir permissões;
- aplicar orçamento/teto de custo;
- exigir aprovação quando necessário;
- registrar auditoria;
- bloquear operações proibidas.

O Agent OS é a fronteira entre **"Sylvia quer"** e **"o sistema pode"**.

### 5.3 Hermes — sistema nervoso executivo

Responsável por:

- receber missões autorizadas;
- escolher/carregar skills;
- operar terminal e ferramentas permitidas;
- delegar para workers especializados;
- acompanhar processos longos;
- coletar stdout/stderr/resultados;
- acionar n8n, browser, MCPs e APIs autorizadas;
- devolver resultado estruturado à Sylvia.

Hermes não é a fonte de identidade ou memória canônica da Sylvia.

### 5.4 Coding Fabric

Camada especializada para engenharia de software.

```text
coding-router
├── executors
│   ├── opencode
│   ├── codex
│   └── claude-code
├── environments
│   ├── repository
│   ├── branch
│   ├── worktree
│   └── sandbox
├── gates
│   ├── diff-review
│   ├── lint
│   ├── typecheck
│   ├── unit-tests
│   ├── integration-tests
│   ├── build
│   ├── secret-scan
│   └── security-review
└── delivery
    ├── commit
    ├── push-branch
    ├── pull-request
    ├── human-approval
    └── deploy
```

## 6. Estratégia de executores de código

### OpenCode

Papel padrão: **worker commodity / custo baixo**.

Usar para:

- implementação bem delimitada;
- bugs simples/médios;
- refactors locais;
- testes;
- documentação técnica;
- tarefas paralelizáveis em worktrees.

### Codex

Usar quando:

- a tarefa se beneficiar de engenharia/autonomia mais forte;
- houver necessidade de revisão independente;
- OpenCode falhar ou produzir resultado abaixo dos gates.

### Claude Code

Usar quando:

- a tarefa exigir compreensão ampla do repositório;
- arquitetura/refactor complexo justificar custo maior;
- revisão adversarial ou segunda opinião for relevante.

A escolha é uma política do `coding-router`, não uma decisão permanente da Sylvia.

## 7. Routing inicial

| Tipo de missão | Executor preferencial | Fallback |
|---|---|---|
| pesquisa/análise | Hermes + browser/MCP | modelo alternativo |
| workflow repetível | n8n | Hermes |
| script pequeno | OpenCode | Codex |
| bug delimitado | OpenCode | Codex / Claude Code |
| feature média | OpenCode ou Codex | Claude Code |
| arquitetura crítica | Claude Code/Codex | revisão cruzada |
| code review | executor diferente do autor | Claude Code/Codex |
| operação externa | Hermes | somente após Agent OS |

## 8. Contrato de missão

Formato conceitual:

```yaml
mission:
  id: DEV-2026-xxxx
  requested_by: founder
  type: development
  objective: "corrigir onboarding do Leaf"
  repo: Ginkgo-Core/leaf
  risk: medium
  environment: non-production

context:
  sources:
    - sylvia-memory
    - repository
  secrets: forbidden

coding:
  executor: opencode
  fallback:
    - codex
    - claude-code
  mode: build

permissions:
  read_repo: true
  modify_worktree: true
  run_tests: true
  commit_branch: true
  push_branch: true
  open_pr: true
  merge_main: false
  deploy_prod: false
  read_secrets: false

quality_gates:
  lint: required
  typecheck: required_when_available
  tests: required
  build: required_when_available
  secret_scan: required
  independent_review: risk_based
```

## 9. Modos de autoridade do Coding Fabric

| Modo | Permissão |
|---|---|
| `INSPECT` | somente leitura/análise |
| `PLAN` | arquitetura e patch proposto, sem escrita |
| `BUILD` | editar somente branch/worktree autorizado |
| `TEST` | executar checks permitidos |
| `REVIEW` | revisar sem alterar |
| `PR` | commit/push/abrir PR |
| `PRODUCTION` | bloqueado por padrão; exige gate explícito |

## 10. Invariantes de segurança

1. **Nenhum coding worker lê segredos.** `.env`, credenciais, tokens e material sensível ficam fora do contexto.
2. **Nenhum worker trabalha diretamente na `main` por padrão.** Toda mutação de código ocorre em branch/worktree/sandbox.
3. **Processo finalizado não significa missão concluída.** `SUCCESS` exige quality gates.
4. **Implementador e reviewer podem ser modelos/executores diferentes** em missões de risco médio/alto.
5. **Deploy de produção não é consequência automática de PR verde.** É uma ação separada e governada.
6. **Toda missão deixa trilha auditável:** intenção, executor, modelo quando relevante, diff, checks, custo, resultado e decisão final.
7. **Material de cliente permanece escopado à tarefa** e nunca entra na memória global.

## 11. Lifecycle de uma missão de código

```text
RECEIVED
  ↓
CLASSIFIED
  ↓
AUTHORIZED
  ↓
CONTEXT_READY
  ↓
WORKTREE_CREATED
  ↓
EXECUTOR_SELECTED
  ↓
IMPLEMENTING
  ↓
VERIFYING
  ├─ diff
  ├─ lint
  ├─ typecheck
  ├─ tests
  ├─ build
  └─ security
  ↓
REVIEWED
  ↓
PR_READY
  ↓
AWAITING_APPROVAL
  ↓
MERGED / REJECTED / NEEDS_CHANGES
```

Estados de falha devem ser explícitos: `BLOCKED`, `FAILED_EXECUTOR`, `FAILED_GATES`, `NEEDS_CONTEXT`, `NEEDS_APPROVAL`.

## 12. Exemplo operacional

Pedido:

```text
"Sylvia, verifique o Leaf e corrija o bug do onboarding."
```

Execução:

1. OpenClaw interpreta a intenção e recupera contexto relevante.
2. Sylvia classifica como `development/debug`.
3. Agent OS autoriza execução não-produtiva.
4. Hermes recebe a missão.
5. Coding Router escolhe OpenCode.
6. Hermes cria/seleciona branch ou worktree isolado.
7. OpenCode analisa e implementa.
8. Hermes executa os quality gates.
9. Se falhar, tenta correção ou fallback conforme política.
10. Se passar, cria commit/push/PR.
11. Sylvia recebe resultado estruturado e apresenta resumo ao fundador.
12. Merge/deploy seguem seus próprios gates.

## 13. Estratégia de custo

O sistema deve otimizar **custo × risco × complexidade**, não fidelidade a fornecedor.

```text
baixo risco + tarefa delimitada
→ OpenCode/modelo econômico

complexidade média
→ OpenCode ou Codex

alto risco / arquitetura
→ executor premium + revisão independente

falha recorrente
→ escalonamento automático de executor
```

Registrar custo por missão quando a API/provedor fornecer dados suficientes.

## 14. Relação com n8n

Hermes e n8n são complementares:

- Hermes: tarefas abertas, interpretação, ferramentas, exceções, coordenação de workers.
- n8n: sequências determinísticas, integrações estáveis, retries e automações repetíveis.

Quando um processo deixar de ser exploratório e se tornar repetível, a tendência é **promovê-lo de missão Hermes para workflow n8n**.

## 15. Fases de implementação

### Fase A — arquitetura e governança

- [ ] formalizar contrato de missão;
- [ ] definir matriz de permissões;
- [ ] definir eventos/auditoria;
- [ ] definir protocolo OpenClaw → Agent OS → Hermes.

### Fase B — Hermes executor

- [ ] reativar/configurar Hermes como execution runtime;
- [ ] impedir uso como memória/cérebro canônico;
- [ ] registrar skill routing;
- [ ] integrar logs estruturados.

### Fase C — OpenCode

- [ ] instalar OpenCode no runtime do Hermes;
- [ ] carregar skill oficial/compatível;
- [ ] configurar providers/modelos permitidos;
- [ ] validar execução em repo descartável;
- [ ] validar sessão longa e retorno estruturado.

### Fase D — GitHub isolation

- [ ] branch/worktree por missão;
- [ ] commit/push controlados;
- [ ] PR automático;
- [ ] proteção de `main`;
- [ ] secret scanning.

### Fase E — Coding Router

- [ ] OpenCode como executor padrão elegível;
- [ ] Codex como fallback/alternativa;
- [ ] Claude Code como fallback/alternativa;
- [ ] regras de custo/risco/complexidade;
- [ ] revisão cruzada.

### Fase F — operação

- [ ] métricas por missão;
- [ ] dashboard de jobs;
- [ ] orçamento por executor;
- [ ] retries controlados;
- [ ] promoção de tarefas repetíveis para n8n.

## 16. Critério de pronto da feature

A feature é considerada operacional quando:

1. um pedido em linguagem natural chega à Sylvia/OpenClaw;
2. vira uma missão estruturada e autorizada;
3. Hermes recebe a missão sem acesso a segredos;
4. um coding worker atua em ambiente isolado;
5. checks são executados automaticamente;
6. resultado inválido não é marcado como sucesso;
7. uma PR é produzida sem tocar diretamente na `main`;
8. Sylvia consegue explicar o que mudou, os checks, o risco e o que requer aprovação;
9. logs permitem reconstruir toda a cadeia de decisão e execução.

## 17. Decisão arquitetural final

```text
OpenClaw não será substituído por Hermes.
Hermes não será aposentado.

OpenClaw = cérebro/runtime principal da Sylvia.
Hermes = executor universal governado.
OpenCode = coding worker preferencial elegível.
Codex + Claude Code = executores alternativos/premium.
n8n = automação determinística.
Agent OS = fronteira de autorização.
GitHub = fonte de verdade e entrega de engenharia.
```

A arquitetura deve permanecer substituível: nenhum componente executor pode se tornar indispensável à identidade ou à memória da Sylvia.