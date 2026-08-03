---
title: "SaaS para Conexões IA"
source: "https://chatgpt.com/c/6a684a46-8534-83e9-8567-50ff8822ffd8"
author:
published:
created: 2026-07-28
description: "ChatGPT conversation with 5 messages"
tags:
  - "clippings"
---
A direção está correta, mas há uma peça crítica faltando e uma possível redundância:

> **Falta um backend próprio mínimo.**  
> **AnythingLLM provavelmente sobra no núcleo do produto.**

O stack enxuto não deveria ser apenas Claude conversando diretamente com n8n. Isso funcionaria para uma demonstração, mas ficaria frágil para usuários, créditos, permissões, auditoria e cobrança.

```
Frontend Ginkgo Connect
        ↓
Core API enxuta
        ↓
┌──────────────┬─────────────┬──────────────┐
│ PostgreSQL   │ Redis       │ Claude       │
│ Estado       │ Efêmero     │ Inteligência │
└──────────────┴─────────────┴──────────────┘
        ↓
Ginkgo Tool Gateway
        ↓
┌──────────────┬──────────────┬──────────────┐
│ n8n          │ MCPs         │ APIs diretas │
│ Workflows    │ padronizados │ específicas  │
└──────────────┴──────────────┴──────────────┘
```

## Stack final do MVP

```
Next.js
Fastify ou NestJS
PostgreSQL
n8n
Claude API / Bedrock
Stripe
OAuth Microsoft
Redis — opcional inicialmente
S3/MinIO — quando houver arquivos
AnythingLLM — opcional e interno
```

---

## 1\. O que falta: Core API

O Ginkgo Connect precisa de um pequeno serviço próprio, mesmo usando n8n.

Pode ser:

- Fastify;
- NestJS;
- ou até rotas server-side do Next.js na primeira versão.

Esse backend controla:

- organizações e usuários;
- autenticação;
- workspaces;
- conexões;
- permissões;
- créditos;
- cobrança;
- tarefas;
- execuções;
- auditoria;
- aprovação humana;
- limites de uso;
- comunicação com Claude;
- comunicação com n8n.

## Por que não deixar tudo no n8n?

Porque o n8n deve executar processos, não ser o sistema contábil do SaaS.

Uma cobrança de créditos precisa ser transacional:

```
1. Verificar saldo
2. Reservar créditos
3. Criar execução
4. Chamar Claude
5. Executar ferramentas
6. Medir consumo real
7. Debitar valor final
8. Estornar diferença
9. Registrar auditoria
```

Isso precisa acontecer de forma idempotente e consistente. Caso uma execução seja repetida após timeout, o usuário não pode ser cobrado duas vezes.

O n8n possui API pública, servidor MCP, ferramentas de gerenciamento de workflows e capacidade de atuar tanto como cliente quanto como servidor MCP. Isso é excelente para integração, mas não substitui a camada de domínio e cobrança do produto. [^1]

---

## 2\. PostgreSQL: obrigatório

Será a fonte oficial de verdade.

## O que armazenar

```
users
organizations
memberships
connectors
oauth_accounts
tasks
task_runs
tool_calls
credit_wallets
credit_ledger
subscriptions
approvals
audit_logs
prompt_versions
usage_events
```

## Regra estrutural

> Tudo que envolve dinheiro, permissão, histórico ou estado persistente vai para PostgreSQL.

Não coloque saldo de créditos apenas no Redis, no n8n ou no AnythingLLM.

## Vetores

Para o primeiro MVP, você pode usar:

```
PostgreSQL + pgvector
```

Isso evita adicionar Qdrant ou outro banco vetorial cedo demais.

Use para:

- glossário empresarial;
- instruções do cliente;
- documentação dos indicadores;
- descrições das tabelas;
- histórico resumido;
- conhecimento operacional.

---

## 3\. Redis: útil, mas não obrigatório no primeiro dia

Redis faz sentido para:

- cache;
- rate limiting;
- locks distribuídos;
- sessões temporárias;
- filas;
- jobs assíncronos;
- controle de concorrência;
- resultados temporários;
- proteção contra execução duplicada.

Redis Streams também pode funcionar como log de eventos e mecanismo de processamento com grupos de consumidores. [^2]

## MVP extremamente enxuto

Você pode começar sem Redis quando houver:

- poucos usuários;
- apenas uma instância de backend;
- baixo volume;
- execuções simples;
- n8n sem queue mode.

## Quando adicionar

Adicione Redis quando precisar de:

```
BullMQ
workers separados
múltiplas instâncias
execuções concorrentes
streaming de status
rate limit distribuído
n8n em queue mode
```

O queue mode do n8n utiliza Redis e é a arquitetura recomendada pelo próprio n8n para escalar workers. [^3]

Minha recomendação prática:

> Já deixe Redis no Docker Compose, mas não construa dependências complexas sobre ele na primeira sprint.

---

## 4\. n8n: permanece, mas com função bem definida

O n8n será o **sistema nervoso operacional**, não o cérebro nem o banco central.

## Responsabilidades corretas

- receber webhooks;
- executar integrações;
- consultar APIs;
- enviar e-mails;
- gerar relatórios;
- programar tarefas;
- fazer transformações;
- chamar sistemas externos;
- executar workflows aprovados;
- retornar resultados estruturados.

## Não deveria controlar

- saldo definitivo;
- assinatura;
- tenancy;
- permissões principais;
- auditoria oficial;
- plano contratado;
- regras centrais de negócio;
- identidade do usuário;
- política de acesso do agente.

## Formas de integração

O backend pode chamar o n8n por:

```
Webhook específico
API pública
MCP Server Trigger
Fila/evento
```

O n8n já possui MCP Client Tool para consumir servidores MCP externos e MCP Server Trigger para expor ferramentas e workflows a clientes MCP. [^4]

---

## 5\. Claude não deve ter acesso irrestrito ao n8n

Aqui está o maior ajuste na sua ideia.

Não entregue para Claude:

```
API administrativa completa do n8n
```

Isso permitiria, dependendo das ferramentas expostas:

- criar workflows;
- alterar workflows;
- apagar workflows;
- acessar credenciais indiretamente;
- executar processos errados;
- interferir em outros tenants.

O servidor MCP oficial do n8n atualmente pode expor ferramentas de construção, gerenciamento e execução de workflows. Para desenvolvimento interno isso é poderoso; para o agente de produção do cliente, é amplo demais. [^1]

## Modelo seguro

Claude recebe apenas ferramentas específicas:

```
powerbi_list_workspaces
powerbi_get_schema
powerbi_execute_read_query
generate_executive_report
send_report_email
create_monitoring_task
get_task_status
```

E não:

```
create_any_workflow
update_any_workflow
delete_workflow
list_all_credentials
execute_arbitrary_http_request
run_arbitrary_code
```

## Arquitetura

```
Claude
   ↓
Ginkgo Tool Gateway
   ↓
Allowlist de ferramentas
   ↓
Workflow específico do n8n
```

O gateway pode inicialmente ser apenas um módulo dentro do Core API. Não precisa nascer como outro microsserviço.

---

## 6\. MCP e API não precisam competir

Use cada um onde fizer mais sentido.

## MCP

Melhor para:

- descoberta dinâmica de ferramentas;
- padronização entre provedores;
- agentes escolhendo ferramentas;
- catálogo crescente de integrações;
- interoperabilidade entre modelos.

Claude pode acessar servidores MCP remotos diretamente pela Messages API, sem exigir um cliente MCP separado construído por você. [^5]

## API direta

Melhor para:

- ações críticas;
- cobrança;
- autenticação;
- operações de alta previsibilidade;
- integrações que não possuem MCP confiável;
- tarefas que exigem controle rígido;
- fallback de conectores em preview.

## n8n

Melhor para:

- orquestrações com vários passos;
- webhooks;
- notificações;
- integrações rápidas;
- tarefas recorrentes;
- transformação de dados;
- operações periféricas.

Não transforme MCP em religião. Às vezes uma chamada REST validada é um bisturi; colocar um agente no meio seria operar com um sabre de luz dentro de um elevador.

---

## 7\. AnythingLLM: onde entra e onde sobra

AnythingLLM já oferece:

- RAG;
- workspaces;
- agentes;
- ferramentas personalizadas;
- MCP;
- API;
- agent flows;
- tarefas programadas. [^6]

Isso significa que ele se sobrepõe a:

- parte do n8n;
- parte do backend;
- parte do MCP Gateway;
- parte da interface;
- parte da memória/RAG.

## Problema

Você passaria a ter três orquestradores:

```
Claude decide
AnythingLLM decide
n8n decide
```

Quando algo falhasse, surgiria a pergunta clássica de uma distopia corporativa:

> Quem exatamente tomou essa decisão?

E a resposta seria: “talvez um dos três”.

## Minha recomendação

### Não usar AnythingLLM no runtime principal do MVP

O caminho produtivo seria:

```
Core API → Claude → ferramentas → n8n/MCP/API
```

### Usar AnythingLLM internamente

Ele pode ser útil como:

- laboratório de prompts;
- console operacional;
- ambiente rápido para testar RAG;
- base de conhecimento da equipe;
- prototipagem de agentes;
- ferramenta de suporte;
- playground administrativo.

Assim ele acelera o desenvolvimento sem se tornar uma dependência estrutural do produto.

## Quando usar no produto

Somente se você decidir que o Ginkgo Connect terá desde o começo:

- workspaces documentais;
- upload de documentos;
- chat RAG completo;
- gestão de bases de conhecimento;
- agentes configuráveis pelo cliente.

Mesmo nesse caso, eu o colocaria atrás da Core API, nunca como fonte oficial de usuários, créditos ou permissões.

---

## Stack enxuta recomendado

## MVP v0.1

```
Frontend:
Next.js + TypeScript + shadcn/ui

Backend:
Fastify ou NestJS

Persistência:
PostgreSQL + pgvector

Orquestração:
n8n

Inteligência:
Claude via API/Bedrock

Autenticação:
Supabase Auth, Clerk ou Auth.js

Pagamentos:
Stripe

Integrações:
OAuth + APIs + MCPs

Arquivos:
S3/MinIO, apenas quando necessário
```

## Ainda não obrigatório

```
Redis
BullMQ
AnythingLLM
Qdrant
Kubernetes
Kafka
microsserviços separados
```

---

## MVP com escala moderada

Quando entrar volume:

```
Next.js
Core API
PostgreSQL + pgvector
Redis
BullMQ workers
n8n queue mode
Claude
Ginkgo Tool Gateway
S3/MinIO
Stripe
Sentry
OpenTelemetry
```

---

## Divisão definitiva de responsabilidades

| Componente | Responsabilidade |
| --- | --- |
| Core API | Regras do SaaS, usuários, créditos e segurança |
| PostgreSQL | Fonte oficial de verdade |
| Redis | Cache, filas, locks e estado temporário |
| Claude | Planejamento, interpretação e geração |
| n8n | Execução de processos e integrações |
| MCP | Interface padronizada para ferramentas |
| APIs | Integrações determinísticas e específicas |
| AnythingLLM | Laboratório/RAG interno opcional |
| S3/MinIO | Arquivos, relatórios e exportações |
| Stripe | Assinaturas, recargas e pagamentos |

## Veredito

Sua composição:

```
n8n
PostgreSQL
Redis
AnythingLLM
Claude
APIs
MCPs
```

Deveria ser ajustada para:

```
Core API
PostgreSQL
n8n
Claude
APIs e MCPs
Stripe
OAuth
```

E então:

```
Redis → adicionar conforme concorrência
AnythingLLM → manter como ferramenta interna opcional
S3/MinIO → adicionar quando houver arquivos
```

A arquitetura mais enxuta e sólida é:

> **Claude pensa.  
> O Core API governa.  
> O n8n executa.  
> O PostgreSQL se lembra.  
> O Redis acelera.  
> MCP e APIs conectam.**

Sem o Core API, temos uma automação. Com ele, temos um SaaS.

---

**Você disse**

Okay, remova as inconsistências técnicas, e vasculhe no nosso

[![](https://chatgpt.com/images/ecosystem/apps/github/icon.png)](https://chatgpt.com/plugins/plugin_connector_1p_1a69035c238881919c4190932b2df699?plugin_detail_origin=inline_selection_pill)

[GitHub](https://chatgpt.com/plugins/plugin_connector_1p_1a69035c238881919c4190932b2df699?plugin_detail_origin=inline_selection_pill) qualquer peça útil e essencial. Também faça uma pesquisa web e encontre alguma ferramenta igual ou similar já validada e pegue todo o marketing e institucional deles / faça uma engenharia reversa possível depois cruze com a nossa identidade.

---

**Você disse**

Todo esse escopo e Stack técnica, desenhe uma série de prompts para o Codex iniciar a construção em um repositório dedicado do zero, que vai pegar apenas o que precisa como você designou dos outros repositórios e criar o que falta.

---

A base correta deve partir principalmente do **`ginkgo-tree`**, não do `ginkgo-platform`. O primeiro já contém TaskRunner determinístico, reserva e liquidação atômica de créditos, BullMQ, aprovação humana, cofre de segredos, Security Boundary, evidências e testes.

Do `ginkgo-platform`, aproveitaremos padrões de monorepo, interface visual e abstração inicial de provedores. O executor n8n atual será tratado como anti-exemplo, pois aceita URLs arbitrárias e não implementa autenticação, política de ferramentas, idempotência ou auditoria.

Os prompts seguem o padrão recomendado oficialmente para o Codex: começar com planejamento, estruturar cada tarefa como uma issue, fornecer caminhos de arquivos, manter contexto persistente em `AGENTS.md` e exigir testes antes da conclusão. [^7]

## Ordem de execução

Execute **um prompt por vez**, em uma branch separada. Não entregue ao Codex todos simultaneamente. O objetivo é construir uma estação orbital módulo por módulo, não lançar vinte foguetes amarrados com fita isolante.

---

## Bloco 1 — Fundação, governança e infraestrutura

## GINKGO CONNECT — SÉRIE DE PROMPTS PARA CODEX

## Bloco 1: fundação técnica, Kernel, banco, segurança e execução

---

## PROMPT 00 — Reconhecimento e plano de extração

## Modo

Use primeiro o modo de planejamento/Ask. Não altere nenhum arquivo nesta tarefa.

## Objetivo

Planejar a construção de um novo repositório chamado `ginkgo-connect`, usando apenas componentes essenciais dos repositórios Ginkgo existentes.

## Repositório de destino

`ginkgoai/ginkgo-connect`

O repositório de destino começa vazio.

## Repositórios doadores

Analise como fontes somente leitura:

- `ginkgoai/ginkgo-tree`
- `ginkgoai/ginkgo-platform`
- `ginkgoai/ai-stack`

Não modifique os repositórios doadores.

## Arquitetura-alvo

```markdown
apps/
  web/                  Next.js
  api/                  Fastify
  worker/               BullMQ

packages/
  core/                 Estado, políticas, risco, orçamento e evidências
  db/                   Prisma, PostgreSQL e repositórios
  boundary/             Segredos, execução governada e confirmação
  connectors/           Registro e adaptadores de integrações
  llm/                  Claude e abstração de provedores
  shared/               Schemas, eventos e tipos
  ui/                   Componentes compartilhados

infra/
  n8n/
  postgres/
  redis/
  docker/
```

## Componentes que devem ser avaliados para reaproveitamento

Do `ginkgo-tree`:

- `packages/core`
- `packages/boundary`
- `packages/db`
- `apps/worker`
- `test/kernel-flow.test.ts`
- `test/boundary.test.ts`
- `docker-compose.prod.yml`
- `packages/db/prisma/schema.prisma`
- implementação de reserva, liquidação e liberação de orçamento
- ciclo de vida de Task
- Evidence append-only
- aprovação humana
- SecretResolver
- VaultAccess
- executor n8n governado, caso exista

Do `ginkgo-platform`:

- estrutura Turborepo
- configuração pnpm
- componentes de dashboard
- padrões de Fastify
- interface conceitual do `aiGateway.ts`

Não reutilizar diretamente:

- `packages/agents/src/tools/n8nExecutor.ts`
- `apps/api/src/services/tokenRouter.ts`
- migrations duplicadas ou conflitantes
- código CRM, WhatsApp, leads, personas, Souls, Leaf, Pyre ou Wave

Do `ai-stack`:

- configuração do n8n em queue mode
- PostgreSQL e Redis no Docker Compose
- healthchecks
- separação entre n8n main e worker

## Escopo travado do MVP

- Primeiro conector: Power BI.
- Operações somente leitura.
- Claude como modelo inicial.
- Modelo de créditos próprios.
- n8n como executor cego de workflows.
- PostgreSQL como fonte oficial de verdade.
- Redis para filas, locks e cache.
- MCP e REST como transportes intercambiáveis.
- AnythingLLM fora do caminho crítico.
- RAG opcional e desativado por padrão.
- Nenhum acesso administrativo do Claude ao n8n.
- Nenhum marketplace público de MCPs no MVP.
- Nenhuma criação de workflows pelo usuário.
- Nenhuma edição de dados no Power BI.

## Entrega

Produza:

1. Mapa dos arquivos que devem ser copiados ou adaptados.
2. Mapa dos arquivos que devem ser criados do zero.
3. Dependências que serão mantidas.
4. Dependências que serão descartadas.
5. Riscos técnicos.
6. Sequência de implementação.
7. ADRs iniciais necessários.
8. Diagrama da arquitetura.
9. Checklist de migração sem dívida técnica.

Não escreva código nesta etapa.

---

## PROMPT 01 — Inicialização do monorepo e constituição do projeto

## Objetivo

Inicialize o repositório vazio `ginkgo-connect` como um monorepo TypeScript production-ready.

## Requisitos

Configure:

- pnpm workspaces
- Turborepo
- TypeScript strict
- ESLint
- Prettier
- Vitest
- Husky ou mecanismo equivalente de pre-commit
- commitlint
- lint-staged
- Docker Compose para desenvolvimento
- variáveis de ambiente validadas
- CI inicial no GitHub Actions

## Estrutura

```markdown
apps/web
apps/api
apps/worker

packages/core
packages/db
packages/boundary
packages/connectors
packages/llm
packages/shared
packages/ui

docs/adr
docs/architecture
docs/product
infra/n8n
infra/docker
```

## Criar AGENTS.md

O arquivo deve instruir permanentemente o Codex:

- trabalhar uma fatia vertical por vez;
- nunca colocar segredos no Core;
- nunca confiar em `orgId` enviado pelo cliente;
- obter a organização exclusivamente do JWT;
- não criar dados mockados em telas de produção;
- não debitar créditos sem transação atômica;
- não executar uma ferramenta sem política registrada;
- não considerar uma ação concluída sem Evidence válida;
- não expor API administrativa do n8n;
- não copiar módulos CRM, WhatsApp, Leaf, Pyre ou Wave;
- não adicionar dependências sem justificativa;
- rodar lint, typecheck, testes e build antes de concluir;
- documentar decisões importantes em ADR.

## Documentos iniciais

Criar:

- `README.md`
- `AGENTS.md`
- `docs/architecture/SYSTEM_OVERVIEW.md`
- `docs/architecture/SECURITY_MODEL.md`
- `docs/product/MVP_SCOPE.md`
- `docs/SOURCE_PROVENANCE.md`
- `docs/adr/0001-monorepo-and-boundaries.md`
- `docs/adr/0002-n8n-as-blind-executor.md`
- `docs/adr/0003-postgres-as-source-of-truth.md`
- `docs/adr/0004-provider-agnostic-llm.md`

## Proveniência

Em `SOURCE_PROVENANCE.md`, registre:

- arquivo de origem;
- repositório de origem;
- commit de origem;
- arquivo de destino;
- se foi copiado, adaptado ou reimplementado;
- alterações realizadas.

## Critérios de aceite

- `pnpm install` funciona.
- `pnpm lint` funciona.
- `pnpm typecheck` funciona.
- `pnpm test` funciona.
- `pnpm build` funciona.
- Docker Compose sobe PostgreSQL e Redis.
- Nenhuma chave ou segredo está versionado.
- Nenhum código de negócio foi implementado ainda.

Crie um commit apenas se todos os checks passarem.

Commit sugerido:

```markdown
chore: bootstrap ginkgo connect monorepo
```

---

## PROMPT 02 — Extração do Kernel de tarefas

## Objetivo

Adaptar do `ginkgo-tree` apenas o Kernel genérico necessário para governar tarefas do Ginkgo Connect.

## Fonte principal

Inspecione:

- `ginkgo-tree/packages/core`
- `ginkgo-tree/packages/core/src/runner.ts`
- `ginkgo-tree/packages/core/src/ports.ts`
- `ginkgo-tree/test/kernel-flow.test.ts`

## Destino

```markdown
packages/core/
```

## Conceitos obrigatórios

Implemente:

- `Task`
- `TaskState`
- `RiskLevel`
- `Maturity`
- `FrozenDecision`
- `EffectivePolicy`
- `SkillDefinition`
- `SkillExecutor`
- `KernelStore`
- `TaskRunner`

## Estados canônicos

```markdown
INGESTED
CLASSIFIED
PLANNED
BLOCKED
GATED
EXECUTED
VERIFIED
COMMITTED
FAILED
```

## Invariantes

1. Toda Task pertence a uma organização.
2. Toda Task recebe um orçamento estimado.
3. O orçamento é reservado antes da execução.
4. A decisão de ferramenta é congelada uma única vez.
5. Reentregas e retries devem ser idempotentes.
6. Operações de risco elevado podem exigir aprovação.
7. Toda execução produz Evidence.
8. Sem Evidence válida, a tarefa não pode chegar a `COMMITTED`.
9. Falhas devem ser persistidas como dados.
10. O Core nunca acessa segredos, HTTP, n8n, MCP ou APIs externas.

## Remover do código importado

- referências a Leaf;
- referências a Brann, Callima, Alfred ou Nyra;
- referências a WhatsApp;
- regras de CRM;
- políticas específicas de agentes;
- qualquer executor específico.

## Testes obrigatórios

- fluxo completo de tarefa somente leitura;
- retry de tarefa já concluída;
- retry concorrente;
- orçamento insuficiente;
- falha do executor;
- ausência de Evidence;
- aprovação exigida;
- aprovação duplicada;
- rejeição humana;
- liberação de reserva após falha;
- decisão congelada não muda durante replay.

## Critérios de aceite

- Core sem dependências de infraestrutura.
- Core sem acesso a variáveis de ambiente.
- Core 100% testável em memória.
- Cobertura mínima de 90% no pacote.
- Todos os testes passam.

Commit sugerido:

```markdown
feat(core): add deterministic governed task kernel
```

---

## PROMPT 03 — Banco, multi-tenancy e livro-razão

## Objetivo

Construir o pacote `@ginkgo-connect/db` usando Prisma e PostgreSQL.

## Fonte de referência

Analise:

- `ginkgo-tree/packages/db`
- `ginkgo-tree/packages/db/prisma/schema.prisma`
- implementação de wallet atômica do `ginkgo-tree`
- `ginkgo-platform/apps/api/migrations/001_token_engine_schema.sql`

Use o schema antigo apenas como referência conceitual. Não copie migrations conflitantes.

## Modelos mínimos

Implemente:

### Identidade

- User
- Organization
- Membership
- Session ou integração com o provedor de autenticação

### Conexões

- ConnectorDefinition
- Connection
- ConnectionCredential
- ConnectionScope
- ConnectionHealthCheck

### Tarefas

- Task
- FrozenDecision
- TaskEvent
- Evidence
- Approval
- ToolCall

### Créditos

- CreditWallet
- CreditHold
- CreditLedger
- PricingVersion
- UsageRecord

### Segurança

- Secret
- VaultAccess
- SecurityViolation

### Operação

- ScheduledTask
- NotificationDestination
- IdempotencyKey

## Regras obrigatórias

- Toda tabela de cliente deve carregar `organizationId`.
- Chaves únicas devem impedir duplicação por idempotency key.
- Evidence deve ser append-only.
- CreditLedger deve ser append-only.
- Segredos devem ser armazenados cifrados.
- Tokens OAuth nunca podem aparecer em logs.
- Valores monetários usam inteiros em centavos.
- Créditos usam inteiros, nunca ponto flutuante.
- Timestamps usam UTC.
- O banco não deve armazenar apenas o saldo: o ledger é a trilha oficial.
- O saldo pode ser materializado, mas precisa ser reconciliável pelo ledger.

## Transações atômicas

Implemente funções ou métodos transacionais para:

- reservar créditos;
- liquidar custo real;
- liberar reserva;
- creditar recarga;
- impedir saldo negativo;
- impedir liquidação duplicada;
- reconciliar carteira com ledger.

## Segurança multi-tenant

A API nunca recebe `organizationId` como autoridade do cliente.

O contexto da organização deve vir de:

```markdown
JWT autenticado
→ Membership
→ OrganizationContext
```

## Testes obrigatórios

- duas organizações não acessam dados entre si;
- hold concorrente;
- settlement concorrente;
- settlement duplicado;
- rollback;
- reconciliação de saldo;
- idempotência de recarga;
- append-only de Evidence;
- append-only do ledger.

## Critérios de aceite

- migrations reproduzíveis;
- seed apenas com catálogos, nunca dados falsos de usuário;
- banco sobe do zero;
- testes de integração passam em PostgreSQL real;
- schema documentado.

Commit sugerido:

```markdown
feat(db): add tenant-safe task and credit ledger
```

---

## PROMPT 04 — Security Boundary e cofre de segredos

## Objetivo

Adaptar o Security Boundary do `ginkgo-tree` para o Ginkgo Connect.

## Fontes principais

Analise:

- `ginkgo-tree/packages/boundary/src/boundary-executor.ts`
- `ginkgo-tree/specs/M2-01-security-boundary.md`
- `ginkgo-tree/test/boundary.test.ts`

## Destino

```markdown
packages/boundary/
```

## Responsabilidades

A Boundary será o único ponto autorizado a:

- recuperar credenciais;
- injetar credenciais;
- chamar executores externos;
- aplicar política de saída;
- redigir segredos;
- revogar leases;
- confirmar resultados;
- registrar violações.

## Pipeline obrigatório

```markdown
VALIDATE
→ CLASSIFY TRUST
→ LOAD POLICY
→ CHECK EGRESS
→ RESOLVE SECRETS
→ EXECUTE
→ CONFIRM
→ REDACT
→ REVOKE
```

## Contratos

Implemente:

- `BoundaryPolicy`
- `BoundaryDelegate`
- `SecretResolver`
- `SecretLease`
- `BoundaryConfirmer`
- `BoundaryExecutor`
- `Redactor`
- `ExecutorIntegrityValidator`

## Regras

- Executor com segredo deve possuir assinatura ou hash de integridade.
- Executor desconhecido falha fechado.
- Ferramenta third-party não autorizada falha fechado.
- Segredo não entra no Core.
- Segredo não entra em `FrozenDecision`.
- Segredo não entra em Evidence.
- Segredo não entra em erros.
- Segredo deve ser revogado em bloco `finally`.
- O executor não pode autodeclarar confirmação externa válida.
- A confirmação deve ocorrer por leitura independente quando aplicável.
- Falha na confirmação impede `COMMITTED`.

## Criptografia

Para desenvolvimento:

- AES-256-GCM;
- chave mestre em variável de ambiente;
- nonce individual;
- versionamento do formato cifrado.

Prepare interface para substituição futura por:

- AWS KMS;
- Vault;
- Secrets Manager.

## Testes obrigatórios

- segredo não aparece em logs;
- segredo não aparece em Evidence;
- segredo não aparece em exceção;
- hash inválido bloqueia execução;
- executor sem política bloqueia;
- segredo ausente bloqueia;
- confirmação forjada é rejeitada;
- lease é revogada após sucesso;
- lease é revogada após falha;
- organização A não resolve segredo da organização B.

Commit sugerido:

```markdown
feat(boundary): add governed secret and execution boundary
```

---

## PROMPT 05 — Worker, Redis e ciclo assíncrono

## Objetivo

Criar `apps/worker` para executar tarefas governadas usando BullMQ e Redis.

## Fontes

Analise:

- `ginkgo-tree/apps/worker`
- wiring do `TaskRunner`
- `ginkgo-tree/docker-compose.prod.yml`
- configuração queue mode de `ginkgoai/ai-stack`

## Arquitetura

```markdown
API
→ cria Task
→ reserva orçamento
→ publica Job
→ Worker
→ TaskRunner
→ Boundary
→ Executor
→ Evidence
→ Settlement
```

## Filas mínimas

- `tasks.execute`
- `tasks.resume`
- `tasks.reject`
- `connections.health`
- `scheduled.dispatch`
- `notifications.send`

## Regras

- Job ID deve derivar da Task ou idempotency key.
- Retry não pode cobrar novamente.
- Jobs devem possuir timeout.
- Backoff exponencial.
- Dead-letter flow após limite de tentativas.
- Eventos de falha devem ser persistidos.
- Jobs R3 não executam sem aprovação.
- Worker não recebe segredos diretamente pelo payload da fila.
- Payloads devem conter identificadores, nunca credenciais.

## Status e heartbeat

Implemente:

- heartbeat do worker;
- status da fila;
- job progress;
- tempo de espera;
- tempo de execução;
- último erro sanitizado.

## Testes

- job duplicado;
- worker morre durante execução;
- retry após timeout;
- settlement não duplicado;
- tarefa bloqueada não executa;
- tarefa aprovada retoma;
- segredo não aparece no Redis;
- dead-letter registra falha.

## Docker

Adapte o Compose para:

- PostgreSQL;
- Redis com persistência;
- API;
- worker;
- healthchecks;
- redes internas;
- volumes nomeados.

Ainda não adicione n8n nesta tarefa.

Commit sugerido:

```markdown
feat(worker): add durable governed task execution
```

---

## PROMPT 06 — Gateway de modelos e Claude

## Objetivo

Criar um gateway de LLM provider-agnostic em `packages/llm`.

## Referência

Analise a interface de:

```markdown
ginkgo-platform/apps/api/src/services/aiGateway.ts
```

Aproveite apenas:

- formato de request;
- formato de response;
- medição de tokens;
- medição de latência;
- suporte a AbortSignal.

Não copie a implementação limitada.

## Arquitetura

```markdown
LLMGateway
  ├── AnthropicProvider
  ├── AwsClaudeProvider
  └── FakeProvider para testes
```

O primeiro provider funcional deve ser Claude.

## Contratos

Implemente:

- `LLMRequest`
- `LLMResponse`
- `LLMUsage`
- `LLMProvider`
- `ModelRoute`
- `ModelRouter`
- `ToolDefinition`
- `ToolCallProposal`

## Responsabilidade do modelo

Claude pode:

- interpretar intenção;
- decompor tarefas;
- escolher ferramentas registradas;
- construir parâmetros;
- analisar resultados;
- gerar explicações;
- gerar relatórios.

Claude não pode:

- receber credenciais;
- escolher URL arbitrária;
- acessar a API administrativa do n8n;
- criar ferramentas;
- modificar políticas;
- aumentar orçamento;
- liquidar créditos;
- marcar Evidence como confirmada;
- acessar dados de outra organização.

## Tool calling

A resposta do modelo deve gerar propostas estruturadas:

```markdown
{
  "tool": "powerbi.query_semantic_model",
  "arguments": {},
  "reason": "string",
  "expected_result": "string"
}
```

Toda proposta deve passar por:

```markdown
schema validation
→ registry lookup
→ policy evaluation
→ budget validation
→ Boundary
```

## Uso e custo

Registre:

- modelo;
- provider;
- input tokens;
- output tokens;
- cache tokens, quando disponíveis;
- latência;
- request ID do provider;
- custo real em unidade e moeda;
- pricing version;
- task ID;
- organization ID.

Não exponha custo interno completo ao cliente final.

## Testes

- provider fake;
- timeout;
- resposta inválida;
- tool call inexistente;
- parâmetros inválidos;
- modelo tentando elevar permissões;
- usage ausente;
- erro sanitizado;
- fallback controlado.

Commit sugerido:

```markdown
feat(llm): add claude gateway and governed tool proposals
```

---

## PROMPT 07 — Registro de conectores, ferramentas e MCP

## Objetivo

Construir `packages/connectors` como a camada universal de integrações.

## Conceito

MCP e REST são transportes. O domínio do produto trabalha com ferramentas Ginkgo normalizadas.

## Contrato central

```markdown
interface ConnectTool {
  id: string;
  connectorType: string;
  version: string;
  title: string;
  description: string;
  riskLevel: "R0" | "R1" | "R2" | "R3";
  operationType: "READ" | "WRITE";
  inputSchema: unknown;
  outputSchema: unknown;
  requiredScopes: string[];
  secretScopes: string[];
  egressAllowlist: string[];
  timeoutMs: number;
  estimatedCredits: number;
  execute(context: ToolExecutionContext): Promise<ToolExecutionResult>;
}
```

## Implementar

- ConnectorRegistry
- ToolRegistry
- ConnectionResolver
- MCPTransport
- RestTransport
- ToolPolicyEvaluator
- ToolSchemaValidator
- HealthCheckRunner
- ConnectorCapabilityCatalog

## Regras

- Ferramentas possuem IDs versionados.
- Nenhuma URL vem do prompt do usuário.
- Nenhuma URL vem da resposta do modelo.
- URLs e endpoints são definidos no registro.
- Cada ferramenta declara scopes.
- Cada ferramenta declara risco.
- Cada ferramenta declara orçamento estimado.
- Operações de escrita ficam desativadas no MVP.
- Ferramentas MCP externas não são confiáveis por padrão.
- Descrições de ferramentas externas devem ser sanitizadas.
- Prompt injection em metadata de ferramenta deve ser tratada como dado não confiável.

## Primeiros conectores

Crie conectores fake para testes:

- `demo.analytics`
- `demo.email`

Não implemente Power BI ainda.

## Testes

- registro duplicado;
- versão inválida;
- ferramenta não registrada;
- escopo insuficiente;
- operação WRITE bloqueada;
- endpoint arbitrário bloqueado;
- metadata maliciosa;
- output incompatível com schema;
- timeout;
- healthcheck.

Commit sugerido:

```markdown
feat(connectors): add governed tool and transport registry
```

---

## PROMPT 08 — Integração segura com n8n

## Objetivo

Adicionar n8n como executor de integrações, nunca como cérebro ou fonte oficial de verdade.

## Referências

Analise:

- `ginkgo-platform/packages/agents/src/tools/n8nExecutor.ts`
- configurações do `ginkgoai/ai-stack`
- padrões de Boundary do `ginkgo-tree`

O executor antigo deve ser substituído, não copiado.

## Topologia

```markdown
Claude
→ Tool Proposal
→ Registry
→ Policy
→ Boundary
→ N8nWorkflowDelegate
→ webhook específico
→ confirmação independente
```

## Não permitido

- Claude chamar API administrativa do n8n.
- Claude criar workflows.
- Claude editar workflows.
- Claude excluir workflows.
- Claude consultar credenciais.
- Usuário informar webhook arbitrário.
- Payload conter segredo persistente.
- Workflow alterar saldo de créditos.
- Workflow marcar tarefa como concluída.

## Implementar

- `N8nWorkflowDefinition`
- `N8nWorkflowRegistry`
- `N8nWorkflowDelegate`
- autenticação HMAC por requisição;
- timestamp e proteção contra replay;
- correlation ID;
- idempotency key;
- timeout;
- output schema;
- confirmação independente;
- healthcheck.

## Registro

Cada workflow permitido deve possuir:

```markdown
workflowKey
webhookUrl cifrada ou configurada
allowedToolIds
inputSchema
outputSchema
riskLevel
timeout
confirmationStrategy
activeVersion
```

## Infraestrutura

Adicionar ao Docker Compose:

- n8n main;
- n8n worker;
- queue mode;
- banco separado ou schema separado;
- Redis;
- `N8N_ENCRYPTION_KEY`;
- sem exposição pública da UI em produção;
- webhook ingress separado;
- healthchecks.

## Workflow inicial

Criar um workflow determinístico:

```markdown
connect.health.echo
```

Ele deve:

- receber payload assinado;
- validar campos;
- devolver correlation ID;
- não acessar sistemas externos;
- servir para teste end-to-end.

## Testes

- assinatura inválida;
- replay;
- workflow não registrado;
- timeout;
- resposta inválida;
- erro n8n;
- correlation ID incompatível;
- segredo vazado;
- chamada duplicada.

Commit sugerido:

```markdown
feat(n8n): add signed allowlisted workflow execution
```

---

## Bloco 2 — Produto, Power BI, créditos, interface e lançamento

## GINKGO CONNECT — SÉRIE DE PROMPTS PARA CODEX

## Bloco 2: produto SaaS, Power BI, créditos, frontend e produção

---

## PROMPT 09 — Autenticação e isolamento organizacional

## Objetivo

Implementar autenticação SaaS e multi-tenancy real.

## Componentes

Criar em `apps/api`:

- autenticação;
- organização;
- membros;
- convites;
- roles;
- middleware de contexto;
- rate limit;
- auditoria de acesso.

## Roles mínimas

```markdown
OWNER
ADMIN
OPERATOR
VIEWER
```

## Regras

- `organizationId` sempre deriva do token autenticado.
- Rotas cross-tenant retornam 404.
- OWNER pode gerenciar cobrança e conexões.
- ADMIN pode gerenciar conexões e tarefas.
- OPERATOR pode executar tarefas permitidas.
- VIEWER apenas consulta resultados.
- Contas suspensas não iniciam tarefas.
- Tokens expirados não executam workflows.
- Mudança de role gera evento de auditoria.

## OAuth de integrações

Não misture login do SaaS com conexões externas.

Modele separadamente:

```markdown
User Authentication
versus
Connection Authorization
```

## Testes

- acesso cross-tenant;
- role insuficiente;
- convite expirado;
- organização suspensa;
- token revogado;
- elevação de privilégio pelo payload;
- enumeração de IDs.

Commit sugerido:

```markdown
feat(auth): add organization-scoped access control
```

---

## PROMPT 10 — Connect Credits e Stripe

## Objetivo

Implementar o modelo comercial de assinatura mais créditos próprios.

## Princípio

O cliente compra unidades de execução do Ginkgo Connect.

O cliente não compra tokens crus de um provedor de LLM.

## Componentes

Implementar:

- carteira;
- saldo disponível;
- saldo reservado;
- ledger;
- pricing version;
- pacotes;
- assinatura;
- recarga avulsa;
- recarga automática opcional;
- limite mensal;
- spend cap;
- estimativa pré-execução;
- custo final;
- reembolso de diferença.

## Fluxo

```markdown
estimate
→ reserve
→ execute
→ measure
→ price
→ settle
→ release difference
```

## Stripe

Implementar:

- Checkout de assinatura;
- Checkout de recarga;
- Customer Portal;
- webhook assinado;
- idempotência por event ID;
- reconciliação;
- estados de assinatura.

## Eventos

```markdown
billing.subscription.activated
billing.subscription.updated
billing.subscription.cancelled
credits.hold.created
credits.hold.released
credits.settled
credits.topup.completed
credits.low_balance
```

## Regras

- Valores monetários em centavos.
- Créditos inteiros.
- Pricing version congelada por Task.
- Mudança de preço não altera tarefa em andamento.
- Webhook duplicado não credita duas vezes.
- Falha do modelo não deve liquidar custo integral indevido.
- Toda diferença entre estimativa e custo final deve ficar auditável.
- O cliente vê créditos consumidos.
- A operação interna registra também custo real do provider.

## Corrigir inconsistências antigas

Não reutilize o `tokenRouter.ts` do `ginkgo-platform`.

Ele realiza leitura e escrita separadas e conflita com os nomes do schema antigo.

Use exclusivamente transações ou funções atômicas.

## Testes

- recarga duplicada;
- hold concorrente;
- saldo insuficiente;
- settlement duplicado;
- mudança de pricing version;
- cancelamento;
- falha após hold;
- reconciliação.

Commit sugerido:

```markdown
feat(billing): add atomic connect credits and stripe
```

---

## PROMPT 11 — Conector Power BI somente leitura

## Objetivo

Implementar o primeiro conector real do Ginkgo Connect.

## Escopo

Power BI com autenticação Microsoft delegada e operações somente leitura.

## Componentes

Criar:

```markdown
packages/connectors/src/powerbi/
```

Inclua:

- manifest;
- OAuth;
- scope mapping;
- REST transport;
- MCP transport opcional;
- healthcheck;
- schema discovery;
- workspace discovery;
- semantic model discovery;
- query execution;
- result normalization;
- confirmer.

## Ferramentas mínimas

```markdown
powerbi.list_workspaces
powerbi.list_semantic_models
powerbi.get_model_schema
powerbi.list_measures
powerbi.execute_read_query
powerbi.get_report_metadata
powerbi.health_check
```

## Restrições

- Nenhuma ferramenta WRITE.
- Bloquear DAX potencialmente não permitido.
- Bloquear queries sem limite razoável.
- Aplicar timeout.
- Aplicar limite de linhas.
- Aplicar limite de payload.
- Nunca registrar conteúdo completo de datasets em logs.
- Nunca enviar mais dados ao modelo do que o necessário.
- Respeitar as permissões efetivas da identidade conectada.
- Renovar tokens OAuth no backend.
- Armazenar refresh token cifrado pela Boundary.

## Estratégia de transporte

Implemente:

```markdown
PowerBIConnector
  → PowerBIRestAdapter
  → PowerBIMcpAdapter opcional
```

A interface pública do conector não deve depender do transporte.

O MVP deve continuar funcionando caso o transporte MCP seja desativado.

## Confirmação

Para consultas de leitura, Evidence deve registrar:

- ferramenta;
- modelo semântico consultado;
- hash dos parâmetros;
- quantidade de linhas;
- horário;
- status;
- request ID externo, quando existente;
- hash do resultado normalizado.

Não grave o dataset completo na Evidence.

## Testes

- token expirado;
- refresh;
- escopo insuficiente;
- workspace inexistente;
- dataset inexistente;
- consulta inválida;
- limite de linhas;
- timeout;
- isolamento entre organizações;
- fallback de transporte;
- sanitização de erro Microsoft.

## Entrega adicional

Criar documentação:

- configuração do aplicativo Microsoft;
- permissões necessárias;
- troubleshooting;
- checklist para administrador do tenant;
- limites do modo somente leitura.

Commit sugerido:

```markdown
feat(powerbi): add governed read-only connector
```

---

## PROMPT 12 — API de tarefas e experiência conversacional

## Objetivo

Criar a API que transforma uma solicitação em linguagem natural em uma Task governada.

## Rotas mínimas

```markdown
POST   /v1/tasks/estimate
POST   /v1/tasks
GET    /v1/tasks
GET    /v1/tasks/:id
POST   /v1/tasks/:id/approve
POST   /v1/tasks/:id/reject
POST   /v1/tasks/:id/retry
GET    /v1/tasks/:id/events
GET    /v1/tasks/:id/evidence

POST   /v1/chat/sessions
POST   /v1/chat/sessions/:id/messages
GET    /v1/chat/sessions/:id
```

## Fluxo

```markdown
mensagem
→ classificação
→ descoberta de conexão
→ proposta de ferramentas
→ estimativa
→ criação da Task
→ hold de créditos
→ fila
→ execução
→ análise
→ Evidence
→ settlement
→ resposta
```

## Separação conceitual

Chat não é a fonte oficial da operação.

A Task é a fonte oficial.

Toda ação iniciada pelo chat deve possuir Task ID.

## Resposta da API

Retorne:

- task ID;
- status;
- estimativa;
- créditos reservados;
- plano de execução resumido;
- necessidade de aprovação;
- progresso;
- resultado;
- Evidence resumida.

## Streaming

Implemente SSE para:

- status;
- progresso;
- tool calls;
- resultado parcial permitido;
- conclusão;
- falha.

Não envie secrets, prompts internos ou chain-of-thought.

## Casos iniciais

- “Liste meus workspaces.”
- “Quais modelos semânticos estão disponíveis?”
- “Qual foi o faturamento do período?”
- “Compare este período com o anterior.”
- “Gere um resumo executivo.”

## Testes

- mensagem duplicada;
- sessão de outra organização;
- saldo insuficiente;
- conexão inativa;
- modelo propõe ferramenta proibida;
- desconexão do SSE;
- retry;
- resposta parcial sem conclusão.

Commit sugerido:

```markdown
feat(api): add governed conversational task execution
```

---

## PROMPT 13 — Frontend, onboarding e central operacional

## Objetivo

Construir a interface do Ginkgo Connect em `apps/web`.

## Identidade

Nome:

```markdown
Ginkgo Connect
```

Headline:

```markdown
Coloque a IA para trabalhar.
```

Princípios visuais:

- preto, grafite, branco e dourado Ginkgo;
- aparência operacional e premium;
- pouca decoração;
- informação verificável;
- status real;
- motion discreto;
- nenhuma estética infantil;
- nenhuma tela cheia de métricas falsas.

## Rotas

```markdown
/
 /login
 /signup
 /onboarding
 /dashboard
 /connections
 /connections/power-bi
 /workbench
 /tasks
 /tasks/[id]
 /automations
 /credits
 /audit
 /settings
```

## Onboarding

Fluxo:

```markdown
Criar conta
→ criar organização
→ escolher Power BI
→ autenticar Microsoft
→ selecionar workspace
→ selecionar modelo semântico
→ executar healthcheck
→ executar consulta de validação
→ receber primeira análise
```

## Dashboard

Mostrar dados reais:

- créditos disponíveis;
- tarefas em execução;
- tarefas concluídas;
- conexões ativas;
- alertas;
- consumo no período;
- tempo economizado, somente se houver metodologia documentada.

## Workbench

Elementos:

- campo “O que você quer que a IA faça?”;
- sugestões de tarefas;
- seletor de conexão;
- estimativa pré-execução;
- modo rápido/preciso/profundo;
- execução em tempo real;
- cards de tool calls;
- resultado;
- Evidence;
- créditos consumidos.

## Tela da Task

Mostrar timeline:

```markdown
Recebida
Classificada
Planejada
Aguardando aprovação
Executada
Verificada
Concluída
```

Exibir:

- ferramenta;
- justificativa resumida;
- custo estimado;
- custo final;
- resultado;
- provas;
- erros;
- retry permitido.

## Estados obrigatórios

- loading;
- vazio;
- sem conexão;
- sem saldo;
- permissão insuficiente;
- integração degradada;
- tarefa bloqueada;
- tarefa falhou;
- offline;
- sucesso.

## Segurança de UX

- Nunca mostrar conexão “ativa” sem healthcheck válido.
- Nunca mostrar tarefa “concluída” antes de `COMMITTED`.
- Nunca esconder créditos consumidos.
- Nunca mostrar provider ou API key ao usuário comum.
- Nunca permitir operação indisponível apenas porque existe um botão mockado.

## Critérios de aceite

- responsivo;
- acessível;
- sem dados mockados em produção;
- skeletons;
- error boundaries;
- testes de componentes principais;
- testes Playwright do onboarding.

Commit sugerido:

```markdown
feat(web): add connect onboarding and task command center
```

---

## PROMPT 14 — Automações programadas e notificações

## Objetivo

Permitir que usuários transformem consultas em tarefas recorrentes.

## Casos

- resumo diário;
- relatório semanal;
- comparação mensal;
- alerta de queda;
- monitoramento de indicador.

## Modelos

Implementar:

- ScheduledTask
- ScheduleVersion
- DeliveryDestination
- DispatchRun

## Regras

- Use cron validado.
- Armazene timezone da organização.
- Toda execução cria uma Task independente.
- Cada execução possui estimate, hold e settlement.
- Tarefa sem saldo não executa.
- Tarefa com conexão inválida não executa.
- Tarefa desativada não entra na fila.
- Alteração do schedule cria nova versão.
- Não permitir frequência abaixo do limite operacional definido.
- Evitar sobreposição por lock distribuído.
- Configurar limite de concorrência por organização.

## Destinos iniciais

- dashboard;
- e-mail.

n8n pode executar a entrega de e-mail, mas não decidir o conteúdo nem cobrar créditos.

## Templates

- resumo executivo;
- alerta de anomalia;
- comparação de períodos;
- relatório de indicadores.

## Testes

- timezone;
- horário de verão;
- execução duplicada;
- saldo insuficiente;
- conexão vencida;
- schedule alterado;
- lock;
- envio falha;
- retry de notificação sem repetir análise.

Commit sugerido:

```markdown
feat(automations): add scheduled governed analysis
```

---

## PROMPT 15 — RAG opcional com AnythingLLM

## Objetivo

Adicionar suporte opcional a glossários e documentação empresarial, sem colocar AnythingLLM no caminho crítico.

## Referências

Analise:

- `ginkgo-tree/apps/worker/src/anythingllm.ts`
- `ginkgo-tree/specs/M4-rag-callima.md`
- configuração AnythingLLM do `ginkgoai/ai-stack`

## Arquitetura

```markdown
KnowledgeProvider
  ├── NoopKnowledgeProvider
  ├── PgVectorKnowledgeProvider
  └── AnythingLLMKnowledgeProvider
```

O provider padrão do MVP deve ser:

```markdown
NoopKnowledgeProvider
```

ou pgvector, caso o escopo documental seja habilitado.

AnythingLLM deve funcionar como serviço opcional por Docker profile:

```markdown
docker compose --profile rag up
```

## Conteúdos suportados

- glossário de KPIs;
- definição de medidas;
- regras empresariais;
- descrição de tabelas;
- notas sobre relatórios;
- instruções de interpretação.

## Regras

- workspace isolada por organização;
- slug persistido, não derivado;
- API key da plataforma não aparece em logs;
- falha do RAG não derruba consulta Power BI;
- resultado sem evidência documental deve ser identificado;
- conteúdo recuperado é dado não confiável;
- documentos não podem alterar políticas do sistema;
- prompt injection documental deve ser neutralizada.

## Testes

- isolamento;
- timeout;
- workspace inexistente;
- documento malicioso;
- falha de embedding;
- fallback;
- ausência de resultado;
- provider desativado.

Commit sugerido:

```markdown
feat(knowledge): add optional tenant-isolated rag
```

---

## PROMPT 16 — Observabilidade, auditoria e segurança

## Objetivo

Tornar cada execução rastreável sem vazar conteúdo sensível.

## Implementar

- logs estruturados;
- correlation ID;
- trace ID;
- métricas;
- OpenTelemetry;
- error tracking;
- painel interno de saúde;
- auditoria;
- alertas operacionais.

## Métricas

- tarefas por estado;
- latência total;
- latência por ferramenta;
- latência do modelo;
- falhas por conector;
- retries;
- dead letters;
- custo real;
- créditos cobrados;
- margem por ação;
- saldo reservado;
- conexões degradadas;
- uso por organização.

## Logs proibidos

- access token;
- refresh token;
- API key;
- segredo;
- conteúdo integral de dataset;
- prompts internos;
- headers de autorização;
- chain-of-thought.

## Auditoria

Registrar:

- ator;
- organização;
- ação;
- recurso;
- resultado;
- IP resumido ou tratado conforme política;
- user agent;
- timestamp;
- correlation ID;
- task ID.

## Segurança

Adicionar:

- rate limiting;
- CSP;
- CORS restritivo;
- proteção CSRF quando aplicável;
- validação Zod;
- headers seguros;
- proteção contra SSRF;
- allowlist de egress;
- limite de payload;
- rotação de segredo;
- scanner de dependências;
- secret scanning;
- CodeQL;
- backup e restore.

## Testes adversariais

- SSRF por parâmetro;
- prompt injection por metadata MCP;
- tentativa de chamar URL arbitrária;
- exfiltração de segredo;
- cross-tenant;
- replay de webhook;
- bypass de aprovação;
- ledger duplicado;
- tool output malicioso;
- query excessiva.

Commit sugerido:

```markdown
feat(security): add observability and adversarial controls
```

---

## PROMPT 17 — Deploy, CI/CD e operação

## Objetivo

Preparar ambiente local, staging e produção.

## Topologia inicial

```markdown
web
api
worker
postgres
redis
n8n-main
n8n-worker
cloudflared ou reverse proxy
anythingllm opcional
```

## Criar

- `docker-compose.yml`
- `docker-compose.prod.yml`
- Dockerfiles multi-stage;
- `.env.example`;
- migrations no boot controlado;
- healthchecks;
- readiness;
- liveness;
- scripts de backup;
- script de restore;
- runbook;
- rollback;
- deploy guide.

## CI

Pipeline:

```markdown
install
→ lint
→ typecheck
→ unit tests
→ integration tests
→ build
→ dependency audit
→ secret scan
→ container build
```

## CD

- deploy em staging;
- smoke tests;
- aprovação para produção;
- migrations antes do tráfego;
- rollback documentado;
- nenhuma migration destrutiva automática.

## Documentos

Criar:

- `docs/operations/DEPLOYMENT.md`
- `docs/operations/RUNBOOK.md`
- `docs/operations/BACKUP_RESTORE.md`
- `docs/operations/INCIDENT_RESPONSE.md`
- `docs/operations/N8N_OPERATIONS.md`
- `docs/operations/POWERBI_TROUBLESHOOTING.md`

## Critérios de aceite

- ambiente limpo sobe com um comando;
- migrations funcionam;
- seed de catálogo funciona;
- healthchecks passam;
- backup e restore testados;
- nenhum banco exposto publicamente;
- n8n editor não fica público;
- staging separado de produção.

Commit sugerido:

```markdown
chore(infra): add production deployment and runbooks
```

---

## PROMPT 18 — Site institucional e marketing do produto

## Objetivo

Construir o site institucional do Ginkgo Connect sem prometer integrações inexistentes.

## Posicionamento

```markdown
Ginkgo Connect
Coloque a IA para trabalhar.
```

## Promessa

```markdown
Conecte seus sistemas, delegue tarefas e acompanhe cada execução com validação, limites e histórico.
```

## Diferenciação

O mercado normalmente vende:

- infraestrutura para desenvolvedores;
- autenticação gerenciada;
- milhares de APIs;
- servidores MCP;
- ferramentas para agentes.

O Ginkgo Connect deve vender para o operador empresarial:

- conexão guiada;
- tarefas em linguagem natural;
- consumo previsível;
- aprovação;
- validação;
- histórico auditável;
- resultado operacional.

## Estrutura da landing page

1. Hero.
2. Demonstração do Power BI.
3. “Escolha, delegue, acompanhe”.
4. Casos de uso.
5. Como funciona.
6. Segurança e governança.
7. Connect Credits.
8. Integrações atuais.
9. Roadmap de integrações.
10. FAQ.
11. CTA final.

## Hero

Headline:

```markdown
Coloque a IA para trabalhar.
```

Subheadline:

```markdown
Conecte o Power BI, delegue análises e acompanhe cada tarefa sendo executada, validada e entregue.
```

CTA principal:

```markdown
Conectar meu Power BI
```

CTA secundário:

```markdown
Ver como funciona
```

## Mensagens permitidas

- Power BI disponível.
- Outras integrações “em breve”.
- Operações somente leitura.
- Créditos previsíveis.
- Histórico e auditoria.
- Aprovação humana.
- Conexão validada.

## Mensagens proibidas

- “Milhares de integrações”, enquanto não existirem.
- “Totalmente autônomo”, sem limites.
- “Zero risco”.
- “Substitui sua equipe”.
- “Dados 100% seguros”.
- “Ilimitado”.
- “Conecta qualquer sistema”.

## Identidade

- preto;
- grafite;
- dourado;
- tipografia forte;
- visual de infraestrutura inteligente;
- diagramas de conexões;
- pequenos sinais de atividade;
- nenhuma árvore genérica de banco de imagens;
- nenhuma estética de chatbot colorido.

## SEO inicial

Crie conteúdo para:

- IA para Power BI;
- conectar Claude ao Power BI;
- análise automatizada de Power BI;
- agente de IA para dados;
- automação de relatórios Power BI;
- MCP empresarial;
- IA conectada aos sistemas da empresa.

## Critérios de aceite

- Lighthouse satisfatório;
- responsivo;
- acessível;
- copy sem claims falsos;
- CTA conectado ao onboarding;
- analytics com consentimento;
- política de privacidade;
- termos;
- página de subprocessadores;
- página de segurança.

Commit sugerido:

```markdown
feat(marketing): add ginkgo connect institutional site
```

---

## PROMPT 19 — Auditoria final e candidato a MVP

## Objetivo

Auditar todo o repositório e preparar o primeiro release candidate.

Não implemente novas features nesta tarefa, salvo correções necessárias para atender critérios já definidos.

## Auditoria

Verifique:

### Escopo

- Power BI somente leitura.
- Claude governado.
- Créditos próprios.
- n8n executor cego.
- MCP opcional.
- AnythingLLM opcional.
- Nenhum código Leaf, Pyre, Wave ou WhatsApp.

### Segurança

- nenhum segredo no Core;
- nenhum segredo na fila;
- nenhum segredo nos logs;
- nenhum endpoint arbitrário;
- nenhum acesso administrativo do modelo;
- isolamento multi-tenant;
- aprovação funcional;
- Evidence obrigatória;
- SSRF bloqueado;
- webhooks assinados.

### Financeiro

- hold atômico;
- settlement atômico;
- rollback;
- idempotência;
- pricing version;
- Stripe duplicado não credita novamente;
- reconciliação.

### Operação

- retry;
- timeout;
- dead letter;
- healthchecks;
- backup;
- restore;
- observabilidade;
- alertas.

### Produto

- onboarding completo;
- primeira consulta;
- task timeline;
- créditos;
- conexão real;
- estados de erro;
- ausência de mocks.

## Teste end-to-end obrigatório

```markdown
signup
→ organização
→ recarga em modo teste
→ conexão Microsoft
→ seleção de workspace
→ healthcheck
→ estimativa
→ hold
→ consulta Power BI
→ análise Claude
→ Evidence
→ settlement
→ resultado no dashboard
```

## Entregáveis

- relatório de auditoria;
- matriz requisito versus evidência;
- lista de riscos;
- lista de itens bloqueadores;
- lista de itens pós-MVP;
- changelog;
- versão;
- tag de release;
- documentação de demonstração;
- script de demo;
- seed somente de catálogo;
- evidência dos testes executados.

## Gate final

Somente criar a tag se:

```markdown
pnpm lint
pnpm typecheck
pnpm test
pnpm test:integration
pnpm test:e2e
pnpm build
```

estiverem verdes.

Tag sugerida:

```markdown
v0.1.0-rc.1
```

Commit sugerido:

```markdown
release: prepare ginkgo connect v0.1.0-rc.1
```

## Estratégia de reaproveitamento

A regra para o Codex deve ser:

```
Copiar conceitos comprovados.
Extrair componentes genéricos.
Reescrever acoplamentos.
Descartar dívida técnica.
```

### Fonte principal

`ginkgo-tree`:

- Kernel;
- TaskRunner;
- wallet atômica;
- BullMQ;
- Evidence;
- Security Boundary;
- SecretResolver;
- HITL;
- infraestrutura Docker.

O repositório declara esses componentes como reais e testados, incluindo reserva/liquidação atômica, Boundary, Stripe, multi-tenancy e ciclo completo de Task.

### Fonte secundária

`ginkgo-platform`:

- shell do monorepo;
- padrões Fastify;
- componentes web;
- interface de gateway de IA.

Não reutilizar o motor de créditos atual nem o executor n8n genérico. O primeiro faz atualização de saldo por leitura e escrita separadas; o segundo executa uma URL recebida na configuração sem controles suficientes.

### Infraestrutura

`ai-stack`:

- n8n queue mode;
- n8n worker;
- Redis;
- PostgreSQL;
- healthchecks;
- AnythingLLM opcional.

## Norte competitivo incorporado

Pipedream, Composio e Zapier validam o valor de autenticação gerenciada, ferramentas para agentes e conexões via MCP. Pipedream destaca managed auth, servidores MCP e ferramentas pré-construídas; Composio vende conexão segura entre agentes e ferramentas empresariais; Zapier MCP combina autenticação, ações habilitadas e rate limiting. [^8]

O corte estratégico da Ginkgo é diferente:

> **Eles vendem infraestrutura de conexão.  
> O Ginkgo Connect vende o trabalho conectado, governado e comprovado.**

O primeiro prompt deve ser executado em modo de planejamento. A partir do Prompt 01, cada etapa entra em Code Mode, uma branch por prompt, sem avançar enquanto o gate anterior estiver vermelho.

[^1]: [docs.n8n.io](https://docs.n8n.io/connect/connect-to-n8n-mcp-server?utm_source=chatgpt.com)

[^2]: [redis.io](https://redis.io/docs/latest/develop/data-types/streams/?utm_source=chatgpt.com)

[^3]: [docs.n8n.io](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode?utm_source=chatgpt.com)

[^4]: [docs.n8n.io](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp?utm_source=chatgpt.com)

[^5]: [docs.anthropic.com](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector?utm_source=chatgpt.com)

[^6]: [docs.anythingllm.com](https://docs.anythingllm.com/mcp-compatibility/overview?utm_source=chatgpt.com)

[^7]: [openai.com](https://openai.com/business/guides-and-resources/how-openai-uses-codex/?utm_source=chatgpt.com)

[^8]: [pipedream.com](https://pipedream.com/connect?utm_source=chatgpt.com)