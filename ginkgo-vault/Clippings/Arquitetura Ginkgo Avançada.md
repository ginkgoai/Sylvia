---
title: "Arquitetura Ginkgo Avançada"
source: "https://chatgpt.com/c/6a5bd082-4cd8-83e9-a1f9-4d313f5dbd27"
author:
published:
created: 2026-07-18
description: "ChatGPT conversation with 6 messages"
tags:
  - "clippings"
---
**Você disse**

---

A estrutura do post é um bom protótipo, mas ainda funciona principalmente como uma **empresa encenada por arquivos Markdown**. Para a Ginkgo, a arquitetura deve operar como um sistema real: agentes recebem missões, consultam memória, executam ferramentas, produzem evidências, solicitam aprovação e registram tudo.

Não será um “grupo de chatbots”. Será o **sistema operacional corporativo da Ginkgo**.

---

## 1\. Visão geral

```
Mermaid
```

---

## 2\. Estrutura hierárquica

## Camada 1 — CEO humano

Você continua sendo a autoridade máxima para:

- visão e estratégia;
- prioridades;
- orçamento;
- contratos;
- pagamentos;
- credenciais críticas;
- mudanças irreversíveis;
- decisões institucionais.

A IA não substitui governança. Ela transforma sua decisão em execução coordenada.

---

## Camada 2 — Sexta-Feira

A **Sexta-Feira** é o cérebro executivo.

Ela não deve programar diretamente na maioria dos casos. Sua função é:

1. interpretar a solicitação;
2. identificar produto, prioridade e risco;
3. quebrar a missão em tarefas;
4. selecionar especialistas;
5. definir critérios de aceite;
6. controlar dependências;
7. solicitar aprovação quando necessário;
8. consolidar resultados;
9. registrar decisões;
10. atualizar memória corporativa.

### Exemplo

Entrada:

> “Adicione cobrança recorrente ao Leaf.”

A Sexta-Feira transforma isso em:

```yaml
mission:
  product: leaf
  objective: implementar cobrança recorrente
  priority: high
  risk: medium

agents:
  - product-manager
  - software-architect
  - backend-engineer
  - frontend-engineer
  - security-engineer
  - qa-engineer
  - devops-engineer

human_gates:
  - aprovação do modelo comercial
  - criação ou uso das credenciais de produção
  - autorização para deploy em produção
```

---

## Camada 3 — Diretor Executivo de Engenharia

O Diretor Executivo de Engenharia transforma estratégia em plano técnico.

Responsabilidades:

- coordenar projetos;
- controlar escopo;
- escolher fluxo de execução;
- impedir soluções excessivamente complexas;
- consolidar respostas dos especialistas;
- verificar critérios de aceite;
- produzir relatório executivo.

Ele funciona como um **chief of staff técnico**.

---

## Camada 4 — Agentes especialistas

### Núcleo estratégico

| Agente | Responsabilidade |
| --- | --- |
| Product Manager | Requisitos, valor para o usuário e escopo |
| CTO | Estratégia técnica e decisões de alto nível |
| Software Architect | Arquitetura, ADRs, integrações e limites |
| Project Manager | Planejamento, dependências e progresso |
| FinOps | Custos, tokens, infraestrutura e margem |

### Núcleo de engenharia

| Agente | Responsabilidade |
| --- | --- |
| Frontend Engineer | Interfaces, estado e integração web |
| Backend Engineer | APIs, regras, filas e serviços |
| AI Engineer | RAG, agentes, modelos, prompts e avaliações |
| Data Engineer | Bancos, pipelines, schemas e qualidade |
| Integration Engineer | n8n, webhooks, APIs e mensageria |
| DevOps Engineer | Docker, CI/CD, deploy e infraestrutura |

### Núcleo de proteção

| Agente | Responsabilidade |
| --- | --- |
| Security Engineer | Segredos, permissões, ameaças e hardening |
| QA Engineer | Testes, regressão e critérios de aceite |
| Compliance Agent | LGPD, retenção e rastreabilidade |
| Reliability Engineer | Logs, métricas, alertas e recuperação |

### Núcleo de experiência

| Agente | Responsabilidade |
| --- | --- |
| UX Researcher | Jornada, fricção e necessidades |
| UI Designer | Interface e design system |
| Technical Writer | Documentação e manuais |
| SEO/Growth Engineer | Descoberta, aquisição e instrumentação |

Não é necessário convocar todos para cada tarefa. Colocar 17 agentes para alterar a cor de um botão seria criar uma ONU dentro do Cursor.

---

## 3\. Roteador inteligente

O roteador escolhe os agentes com base em domínio, risco e complexidade.

## Matriz básica

```yaml
routing_rules:
  frontend:
    agents:
      - frontend-engineer
      - ui-designer
      - qa-engineer

  backend:
    agents:
      - backend-engineer
      - software-architect
      - qa-engineer

  database:
    agents:
      - database-architect
      - backend-engineer
      - security-engineer

  artificial_intelligence:
    agents:
      - ai-engineer
      - data-engineer
      - qa-engineer

  deployment:
    agents:
      - devops-engineer
      - security-engineer
      - reliability-engineer

  payments:
    agents:
      - backend-engineer
      - security-engineer
      - compliance-agent
      - qa-engineer

  critical_production:
    human_approval: required
```

## Classificação de complexidade

```yaml
complexity:
  trivial:
    max_agents: 1
    architecture_review: false

  low:
    max_agents: 2
    architecture_review: false

  medium:
    max_agents: 4
    architecture_review: true

  high:
    max_agents: 7
    architecture_review: true
    human_approval: required

  critical:
    max_agents: 10
    architecture_review: true
    security_review: true
    rollback_plan: required
    human_approval: required
```

---

## 4\. Estrutura do repositório

```
ginkgo-agentic-os/
├── README.md
├── AGENTS.md
├── .env.example
├── docker-compose.yml
│
├── .cursor/
│   ├── rules/
│   │   ├── global.mdc
│   │   ├── security.mdc
│   │   ├── testing.mdc
│   │   ├── documentation.mdc
│   │   └── human-gates.mdc
│   └── commands/
│       ├── start-mission.md
│       ├── architecture-review.md
│       ├── security-review.md
│       ├── generate-tests.md
│       └── release.md
│
├── agents/
│   ├── executive/
│   │   ├── sexta-feira.md
│   │   ├── engineering-director.md
│   │   └── task-router.md
│   │
│   ├── strategy/
│   │   ├── product-manager.md
│   │   ├── cto.md
│   │   ├── project-manager.md
│   │   └── finops.md
│   │
│   ├── engineering/
│   │   ├── software-architect.md
│   │   ├── frontend-engineer.md
│   │   ├── backend-engineer.md
│   │   ├── ai-engineer.md
│   │   ├── data-engineer.md
│   │   ├── integration-engineer.md
│   │   └── devops-engineer.md
│   │
│   ├── assurance/
│   │   ├── security-engineer.md
│   │   ├── qa-engineer.md
│   │   ├── compliance-agent.md
│   │   └── reliability-engineer.md
│   │
│   └── experience/
│       ├── ux-researcher.md
│       ├── ui-designer.md
│       ├── technical-writer.md
│       └── growth-engineer.md
│
├── governance/
│   ├── constitution.md
│   ├── authority-matrix.yaml
│   ├── human-action-policy.yaml
│   ├── risk-policy.yaml
│   ├── approval-policy.yaml
│   ├── secrets-policy.md
│   ├── data-retention-policy.md
│   └── definition-of-done.md
│
├── memory/
│   ├── company/
│   │   ├── vision.md
│   │   ├── principles.md
│   │   ├── architecture.md
│   │   ├── products.md
│   │   └── glossary.md
│   ├── decisions/
│   ├── lessons/
│   ├── incidents/
│   └── checkpoints/
│
├── products/
│   ├── leaf/
│   │   ├── README.md
│   │   ├── product.yaml
│   │   ├── architecture.md
│   │   ├── backlog.md
│   │   ├── requirements/
│   │   ├── adr/
│   │   ├── tests/
│   │   └── runbooks/
│   ├── wave/
│   ├── pyre/
│   ├── lexra/
│   └── laplace/
│
├── missions/
│   ├── inbox/
│   ├── active/
│   ├── blocked/
│   ├── review/
│   └── completed/
│
├── workflows/
│   ├── feature-development.yaml
│   ├── bug-fix.yaml
│   ├── security-incident.yaml
│   ├── release.yaml
│   ├── customer-onboarding.yaml
│   └── infrastructure-change.yaml
│
├── templates/
│   ├── mission.yaml
│   ├── task.yaml
│   ├── adr.md
│   ├── pull-request.md
│   ├── incident.md
│   ├── handoff.md
│   └── executive-report.md
│
├── orchestrator/
│   ├── src/
│   │   ├── router/
│   │   ├── planner/
│   │   ├── executor/
│   │   ├── approvals/
│   │   ├── memory/
│   │   ├── audit/
│   │   └── integrations/
│   └── tests/
│
├── integrations/
│   ├── github/
│   ├── n8n/
│   ├── supabase/
│   ├── redis/
│   ├── telegram/
│   ├── discord/
│   ├── clickup/
│   └── observability/
│
└── reports/
    ├── daily/
    ├── weekly/
    ├── releases/
    ├── costs/
    └── audits/
```

---

## 5\. Contrato padrão de agente

Cada agente deve ter identidade operacional, limites e formato de saída.

```yaml
---
id: backend-engineer
name: Backend Engineer
version: 1.0.0

mission:
  design_and_implement:
    - APIs
    - business_rules
    - queues
    - integrations
    - background_jobs

authority:
  may:
    - inspect_repository
    - propose_changes
    - create_branches
    - write_code
    - write_tests
    - open_pull_requests

  may_not:
    - deploy_to_production
    - access_payment_credentials
    - delete_production_data
    - change_billing
    - merge_own_pull_request

required_inputs:
  - mission
  - product_context
  - acceptance_criteria
  - architecture_constraints

required_outputs:
  - implementation_plan
  - changed_files
  - tests
  - risks
  - rollback_notes
  - evidence

escalation:
  architecture_conflict: software-architect
  security_risk: security-engineer
  missing_requirement: product-manager
  production_action: human-approval
---
```

Essa estrutura permite que o agente seja utilizado por Cursor, Codex, scripts Python ou outro runtime.

---

## 6\. Formato de missão

```yaml
mission_id: MIS-2026-0001
title: Implementar cobrança recorrente no Leaf
product: leaf

requested_by:
  type: human
  role: ceo

business_objective:
  description: permitir planos mensais com cobrança automática
  success_metric: assinatura criada e renovada sem intervenção manual

priority: high
risk_level: high

scope:
  include:
    - cadastro de plano
    - checkout
    - webhook
    - atualização de assinatura
    - cancelamento
    - logs
    - testes

  exclude:
    - marketplace
    - cobrança internacional
    - múltiplas moedas

acceptance_criteria:
  - pagamento confirmado atualiza assinatura
  - falha de pagamento não libera acesso
  - webhook duplicado não duplica registros
  - segredos não aparecem em logs
  - rollback documentado

human_approval:
  required_for:
    - credenciais de produção
    - ativação de cobrança real
    - deploy em produção
```

---

## 7\. Fluxo operacional completo

## Estado da missão

```
INBOX
  ↓
TRIAGE
  ↓
PLANNING
  ↓
APPROVED
  ↓
IN_PROGRESS
  ↓
TECHNICAL_REVIEW
  ↓
SECURITY_REVIEW
  ↓
QA
  ↓
HUMAN_GATE
  ↓
DEPLOYMENT
  ↓
MONITORING
  ↓
COMPLETED
```

Também devem existir:

```
BLOCKED
REJECTED
ROLLED_BACK
CANCELLED
```

## Ciclo prático

### 1\. Recepção

A Sexta-Feira recebe a solicitação por:

- Cursor;
- Codex;
- Telegram;
- painel web;
- GitHub Issue;
- formulário interno;
- webhook do n8n.

### 2\. Classificação

O roteador identifica:

- produto;
- domínio;
- risco;
- urgência;
- agentes necessários;
- permissões necessárias.

### 3\. Planejamento

O Diretor de Engenharia produz:

- plano;
- tarefas;
- dependências;
- critérios de aceite;
- estimativa;
- riscos;
- plano de rollback.

### 4\. Aprovação

Apenas quando a política exigir.

### 5\. Execução

O especialista:

- cria branch;
- altera código;
- gera testes;
- documenta;
- cria pull request;
- anexa evidências.

### 6\. Revisão

Nenhum agente aprova sozinho o próprio trabalho.

```
Autor → Revisor técnico → Segurança → QA → Humano, quando aplicável
```

### 7\. Deploy

DevOps executa somente após os gates obrigatórios.

### 8\. Aprendizado

Ao final:

- ADR registrada;
- lições adicionadas;
- custo calculado;
- memória atualizada;
- relatório consolidado.

---

## 8\. Protocolo de ação humana

Esta é uma das partes mais importantes.

## Sempre exigir aprovação

```yaml
human_action_required:
  - enviar_pagamentos
  - contratar_servicos
  - aceitar_termos
  - criar_contas_externas
  - compartilhar_credenciais
  - acessar_dados_pessoais_sensiveis
  - alterar_dns
  - excluir_banco_de_dados
  - executar_migracao_irreversivel
  - publicar_em_producao
  - enviar_comunicacao_juridica
  - alterar_precos
  - alterar_permissoes_administrativas
```

## Formato da solicitação

```markdown
## Ação humana necessária

**Missão:** MIS-2026-0001  
**Ação:** inserir chave de produção do gateway  
**Motivo:** o agente não possui permissão para acessar credenciais  
**Risco:** cobrança real será ativada  
**Local:** painel do provedor → Desenvolvedores → API Keys  

### Passos

1. Abra o painel.
2. Gere uma chave restrita.
3. Salve-a no gerenciador de segredos.
4. Não envie a chave pelo chat.
5. Confirme apenas que a operação foi concluída.
```

A IA explica o caminho, mas não pede que segredos sejam colados em conversa. Isso evita transformar automação em um vazamento com interface elegante.

---

## 9\. Memória corporativa

A memória deve possuir quatro níveis.

## Memória de execução

Redis:

- contexto temporário;
- locks;
- filas;
- sessões;
- status de missão.

## Memória operacional

PostgreSQL ou Supabase:

- missões;
- tarefas;
- aprovações;
- agentes;
- execuções;
- custos;
- incidentes;
- auditoria.

## Memória semântica

Vector store:

- documentação;
- decisões;
- requisitos;
- runbooks;
- histórico técnico;
- padrões da Ginkgo.

## Memória institucional

Git:

- constituição;
- políticas;
- ADRs;
- arquitetura;
- documentação;
- definições de produto.

O banco registra o que aconteceu. O Git registra o que oficialmente vale.

---

## 10\. Modelo de dados mínimo

```sql
create table missions (
  id uuid primary key,
  code text unique not null,
  product text not null,
  title text not null,
  status text not null,
  priority text not null,
  risk_level text not null,
  requested_by text not null,
  created_at timestamptz default now(),
  completed_at timestamptz
);

create table tasks (
  id uuid primary key,
  mission_id uuid references missions(id),
  assigned_agent text,
  title text not null,
  status text not null,
  dependencies jsonb default '[]',
  acceptance_criteria jsonb default '[]',
  evidence jsonb default '[]',
  created_at timestamptz default now()
);

create table approvals (
  id uuid primary key,
  mission_id uuid references missions(id),
  action_type text not null,
  requested_by_agent text not null,
  status text not null,
  approved_by text,
  requested_at timestamptz default now(),
  resolved_at timestamptz
);

create table executions (
  id uuid primary key,
  task_id uuid references tasks(id),
  agent_id text not null,
  model text,
  tool text,
  input_hash text,
  output_hash text,
  tokens_used bigint,
  estimated_cost numeric,
  started_at timestamptz,
  finished_at timestamptz
);

create table audit_events (
  id uuid primary key,
  mission_id uuid references missions(id),
  actor_type text not null,
  actor_id text not null,
  action text not null,
  payload jsonb,
  created_at timestamptz default now()
);
```

---

## 11\. Integração com Cursor e Codex

## Cursor

O Cursor funciona melhor como:

- ambiente interativo;
- leitura do repositório;
- implementação guiada;
- revisão visual;
- edição rápida;
- regras persistentes por projeto.

## Codex

O Codex pode ser utilizado como:

- executor de tarefas isoladas;
- geração de branches;
- implementação de issues;
- testes;
- correções;
- análise do repositório;
- produção de diffs verificáveis.

## Divisão recomendada

```
Sexta-Feira
    ↓ planeja
GitHub Issue
    ↓ define missão e critérios
Codex
    ↓ implementa em branch
Pull Request
    ↓ revisado por agentes
Cursor
    ↓ inspeção humana e ajustes
CI/CD
    ↓ validação
Deploy autorizado
```

Cursor é o cockpit. Codex é a equipe de drones. GitHub é a caixa-preta que impede todos de jurarem que “estava funcionando antes”.

---

## 12\. Integração com a stack Ginkgo

```yaml
interface:
  - cursor
  - codex
  - telegram
  - discord
  - web_dashboard

orchestration:
  - python
  - n8n
  - temporal_optional

memory:
  short_term: redis
  operational: postgresql
  business: supabase
  semantic: vector_store
  institutional: git

execution:
  - github
  - docker
  - portainer
  - ssh_restricted
  - ci_cd

observability:
  - structured_logs
  - metrics
  - traces
  - alerts
  - cost_tracking

secrets:
  - docker_secrets
  - vault_optional
  - environment_variables
  - github_actions_secrets
```

---

## 13\. Governança constitucional

O arquivo `governance/constitution.md` deve estabelecer:

```markdown
# Constituição Operacional Ginkgo

1. Nenhum agente possui autoridade ilimitada.
2. Toda ação deve ser associada a uma missão.
3. Toda missão deve possuir responsável e critérios de aceite.
4. Nenhum agente aprova integralmente o próprio trabalho.
5. Ações críticas exigem aprovação humana.
6. Segredos não podem ser registrados em prompts, logs ou documentos.
7. Toda alteração de arquitetura deve gerar ADR.
8. Toda alteração em produção deve possuir rollback.
9. Toda execução deve produzir evidência verificável.
10. Nenhuma pessoa recebe autoridade apenas por vínculo familiar.
11. Autoridade depende de competência, função e permissão formal.
12. O custo de IA e infraestrutura deve ser mensurável por produto.
13. A memória institucional somente muda mediante registro versionado.
14. Em caso de conflito, segurança e integridade prevalecem sobre velocidade.
```

---

## 14\. Prompt mestre para Cursor ou Codex

```
Você atuará como arquiteto principal responsável por construir o
Ginkgo Agentic Engineering OS.

OBJETIVO

Criar uma empresa virtual de engenharia de software operada por agentes
especialistas, com governança, memória, auditoria, permissões, aprovação
humana e integração com ferramentas reais.

O sistema não deve ser apenas uma coleção de prompts Markdown.
Ele deve possuir contratos estruturados, estados de missão, persistência,
roteamento, logs, gates de aprovação e mecanismos de execução.

ARQUITETURA OBRIGATÓRIA

1. Executive Orchestrator chamado Sexta-Feira.
2. Diretor Executivo de Engenharia.
3. Task Router baseado em domínio, risco e complexidade.
4. Agentes especialistas:
   - CTO
   - Product Manager
   - Project Manager
   - Software Architect
   - Frontend Engineer
   - Backend Engineer
   - AI Engineer
   - Data Engineer
   - Integration Engineer
   - DevOps Engineer
   - Security Engineer
   - QA Engineer
   - Compliance Agent
   - Reliability Engineer
   - UX Researcher
   - UI Designer
   - Technical Writer
   - FinOps

5. Workflow de missões:
   INBOX
   TRIAGE
   PLANNING
   APPROVED
   IN_PROGRESS
   TECHNICAL_REVIEW
   SECURITY_REVIEW
   QA
   HUMAN_GATE
   DEPLOYMENT
   MONITORING
   COMPLETED

6. Estados alternativos:
   BLOCKED
   REJECTED
   CANCELLED
   ROLLED_BACK

7. Protocolo obrigatório de ação humana para:
   - pagamentos
   - credenciais
   - contratos
   - exclusões
   - alterações irreversíveis
   - produção
   - DNS
   - permissões administrativas
   - dados sensíveis

8. Memória:
   - Redis para estado temporário
   - PostgreSQL para missões e auditoria
   - Vector store para recuperação semântica
   - Git para memória institucional

9. Integrações:
   - GitHub
   - Cursor
   - Codex
   - n8n
   - Supabase
   - Redis
   - Docker
   - Telegram
   - Discord

10. Segurança:
   - princípio do menor privilégio
   - nenhum segredo em logs
   - isolamento por ferramenta
   - aprovação para produção
   - trilha de auditoria
   - rollback obrigatório
   - agente não aprova o próprio trabalho

ESTRUTURA

Crie:

- README.md
- AGENTS.md
- diretório agents/
- diretório governance/
- diretório memory/
- diretório products/
- diretório missions/
- diretório workflows/
- diretório templates/
- diretório orchestrator/
- diretório integrations/
- diretório reports/
- regras do Cursor em .cursor/rules/
- comandos do Cursor em .cursor/commands/
- modelos YAML para missões, tarefas e aprovações
- schemas SQL
- Docker Compose para ambiente local
- testes mínimos
- documentação de execução

STACK INICIAL

- Python 3.12
- FastAPI
- Pydantic
- PostgreSQL
- Redis
- SQLAlchemy
- Alembic
- Docker Compose
- GitHub Actions
- pytest
- structured logging

REGRAS DE IMPLEMENTAÇÃO

- Use tipagem estática.
- Separe domínio, aplicação e infraestrutura.
- Evite dependência direta entre agentes e provedores de LLM.
- Crie interfaces substituíveis para modelos e ferramentas.
- Cada agente deve possuir contrato YAML.
- Cada execução deve gerar um audit event.
- Cada missão deve possuir critérios de aceite.
- O sistema deve funcionar inicialmente sem interface gráfica.
- Crie uma CLI e uma API.
- Não implemente complexidade desnecessária.
- Não faça deploy.
- Não use credenciais reais.
- Não execute ações externas irreversíveis.

ORDEM DE TRABALHO

1. Analise os requisitos.
2. Gere architecture.md.
3. Gere ADR-0001.
4. Crie a árvore de diretórios.
5. Implemente os modelos de domínio.
6. Implemente o mecanismo de estados.
7. Implemente o roteador.
8. Implemente aprovação humana.
9. Implemente auditoria.
10. Implemente persistência.
11. Implemente a CLI.
12. Implemente a API.
13. Adicione testes.
14. Adicione Docker Compose.
15. Documente a execução.
16. Gere relatório final com:
    - arquivos criados
    - decisões
    - riscos
    - pendências
    - próximos passos

Antes de alterar arquivos, apresente o plano.
Ao encontrar uma decisão crítica, registre uma ADR.
Ao precisar de credencial ou ação externa, interrompa e produza
uma solicitação de ação humana.
```

---

## 15\. Roadmap de implementação

## Fase 1 — Constituição e simulação

Prazo operacional: primeira versão.

- estrutura de pastas;
- agentes Markdown/YAML;
- políticas;
- modelos de missão;
- workflows;
- ADRs;
- regras do Cursor;
- comandos manuais.

Nesta fase, o sistema ainda é dirigido dentro do IDE, mas já possui disciplina.

## Fase 2 — Orquestrador executável

- FastAPI;
- CLI;
- PostgreSQL;
- Redis;
- máquina de estados;
- roteador;
- auditoria;
- aprovações;
- integração GitHub.

Aqui a empresa deixa de ser teatro documental e ganha sistema nervoso.

## Fase 3 — Execução automatizada

- Codex por tarefa;
- criação automática de branches;
- pull requests;
- execução de testes;
- revisão multiagente;
- relatórios;
- Telegram e Discord.

## Fase 4 — Operação corporativa

- dashboard;
- custos por produto;
- métricas de produtividade;
- controle de permissões;
- incidentes;
- deploy supervisionado;
- integração com Leaf, Wave, Pyre e Laplace.

## Fase 5 — Autonomia limitada

- planejamento recorrente;
- manutenção preventiva;
- identificação de dívida técnica;
- criação automática de propostas de melhoria;
- acompanhamento de produtos;
- execução autônoma apenas em ambientes isolados.

---

## 16\. Primeiro MVP recomendado

O primeiro MVP não deve tentar administrar toda a Ginkgo.

Ele deve executar muito bem este ciclo:

```
Pedido humano
→ missão estruturada
→ roteamento
→ plano
→ aprovação
→ implementação em branch
→ testes
→ pull request
→ revisão
→ relatório
```

### Escopo inicial

- 1 orquestrador;
- 1 roteador;
- 6 agentes;
- 1 produto piloto;
- GitHub;
- PostgreSQL;
- Redis;
- CLI;
- aprovação pelo Telegram;
- zero deploy automático em produção.

### Agentes iniciais

```
Sexta-Feira
Engineering Director
Software Architect
Backend Engineer
Frontend Engineer
QA Engineer
Security Engineer
```

### Produto piloto

**Leaf**, por já concentrar:

- frontend;
- backend;
- banco;
- WhatsApp;
- IA;
- CRM;
- pagamentos;
- integrações;
- requisitos de segurança.

Ele é o melhor laboratório. Se a arquitetura sobreviver ao Leaf, o restante parecerá uma estação orbital depois de construir a Estrela da Morte — só que com menos problemas regulatórios.

---

**Você disse**

Perfeito, e lembra que havíamos mudado o codinome de sexta-feira

---

Sim. O codinome **Sexta-Feira foi substituído por SYLVIA**.

A separação correta ficou:

- **SYLVIA** — assistente executiva, interface do fundador e orquestradora central da Ginkgo.
- **Laplace** — núcleo cognitivo: RAG, memória, conhecimento corporativo e recuperação de contexto.
- **Ginkgo Agentic Engineering OS** — sistema operacional que governa missões, agentes, aprovações, auditoria e execução.

Portanto, na arquitetura anterior:

```
Sexta-Feira
↓
SYLVIA
```

A hierarquia oficial passa a ser:

```
Gabriel / CEO
     ↓
SYLVIA
Executive Orchestrator
     ↓
Engineering Director
     ↓
Task Router
     ↓
Agentes especialistas
     ↓
Ferramentas e ambientes de execução
```

Com o núcleo abaixo:

```
SYLVIA
   ├── consulta → Laplace
   ├── delega → agentes especialistas
   ├── executa → Cursor, Codex, GitHub e n8n
   ├── controla → permissões e aprovações
   └── registra → memória, ADRs e auditoria
```

Também devemos renomear:

```
agents/executive/sexta-feira.md
```

para:

```
agents/executive/sylvia.md
```

E o identificador:

```yaml
id: sylvia
name: SYLVIA
role: executive-orchestrator
```

**Laplace não substitui SYLVIA.** Laplace é o cérebro documental e semântico; SYLVIA é a entidade executiva que conversa, decide, coordena e governa. Em analogia simples: Laplace é a biblioteca neural da nave; SYLVIA está na ponte de comando.

---

**Você disse**

Perfeito. Relembre mais, condense e cruze todos os dados de conversas anteriores e faça um readme completo e detalhado

---

## README mestre consolidado

Criei a versão canônica cruzando as decisões recentes com a arquitetura anterior do **Ginkgo Agent OS**, Human Oversight, Ginkgo Brain/Laplace, produtos, agentes, infraestrutura e schema multi-tenant.

O documento possui **2.494 linhas** e consolida:

- **Fundador → SYLVIA → Laplace → Hermes Agent → Ginkgo Agent OS**;
- SYLVIA como interface executiva privada;
- Laplace como memória, contexto, RAG e inferência;
- Hermes como motor técnico de execução;
- Leaf + Brann, Wave + Alfred, Pyre + Nyra e Learn + Euclid;
- Command, Ginkgo Office, Ginkgo Source, Lexra, Atlas e Callima;
- correção das nomenclaturas antigas;
- governança humana e familiar por competência;
- matriz de risco e approval gates;
- Cursor, Codex, GitHub e n8n;
- arquitetura multi-tenant com RLS;
- contratos de agentes, ferramentas e missões;
- máquina de estados;
- Execution Ledger;
- schemas SQL;
- observabilidade, FinOps e segurança;
- estrutura completa de repositório;
- roadmap de implementação;
- prompt permanente de arquitetura;
- constituição operacional.

Decisões conflitantes foram explicitamente resolvidas: **Sexta-Feira e CEO Fantasma viraram nomenclaturas históricas; Wave e Pyre permanecem produtos ativos; Pyre não é runtime; OpenClaw passa a ser componente opcional, subordinado à arquitetura Laplace–Hermes.**

GINKGO\_AGENTIC\_OS\_MASTER\_README\_v3.md