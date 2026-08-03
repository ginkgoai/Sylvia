---
title: "Arquitetura Ginkgo AI"
source: "https://chatgpt.com/c/6a5bd28f-8e6c-83e9-bb04-dcc2b1f531fe"
author:
published:
created: 2026-07-18
description: "ChatGPT conversation with 2 messages"
tags:
  - "clippings"
---
**Você disse**

---

A leitura correta para a **Ginkgo AI Systems** é:

Não construir um monólito gigante com Leaf, Pyre, Wave, billing, agentes e integrações misturados. Também não transformar cada função em um container independente só porque Docker deixa isso visualmente bonito. Isso seria trocar um prédio organizado por uma cidade distópica onde cada cômodo exige passaporte.

O guia acerta no princípio central: começar com fronteiras modulares fortes e extrair serviços somente quando existir uma dor operacional concreta. O caminho é um espectro, não uma decisão binária.

## Arquitetura recomendada para a Ginkgo

```
GINKGO CONTROL PLANE
┌─────────────────────────────────────────────────────────────────┐
│ Organizações │ Usuários │ Planos │ Billing │ Permissões │ Audit │
│ Entitlements │ Onboarding │ Configurações │ Secrets │ API Keys  │
└──────────────────────────────┬──────────────────────────────────┘
                               │ APIs + eventos
          ┌────────────────────┼────────────────────┐
          │                    │                    │
┌─────────▼─────────┐ ┌────────▼────────┐ ┌─────────▼─────────┐
│       LEAF        │ │      PYRE       │ │       WAVE        │
│ Monólito modular  │ │ Monólito modular│ │ Monólito modular  │
│ CRM               │ │ Conteúdo        │ │ Campanhas         │
│ Conversas         │ │ Aprovações      │ │ Orçamentos        │
│ Pipeline          │ │ Calendário      │ │ Relatórios        │
│ Agenda            │ │ Publicação      │ │ Otimização        │
└─────────┬─────────┘ └────────┬────────┘ └─────────┬─────────┘
          └────────────────────┼────────────────────┘
                               │
                     INTEGRATION / AI PLANE
┌─────────────────────────────────────────────────────────────────┐
│ n8n │ Evolution API │ Chatwoot │ Stripe │ Meta │ Google │ Email │
│ LiteLLM │ Laplace/RAG │ Workers │ Redis Queue │ Object Storage  │
└─────────────────────────────────────────────────────────────────┘
```

## 1\. Ginkgo Control Plane

Deve ser um **monólito modular central**, responsável pelo ecossistema:

- organizações e tenants;
- usuários, equipes e permissões;
- planos, assinaturas e limites;
- billing e entitlements;
- onboarding;
- API keys e credenciais;
- auditoria;
- configuração dos produtos.

Ele não executa todas as operações do Leaf ou Pyre. Ele determina **quem pode acessar o quê, em qual plano e com quais limites**.

É o sistema nervoso central, não cada músculo do corpo.

## 2\. Leaf, Pyre e Wave

Cada produto deve começar como uma aplicação própria, porém internamente modular.

Exemplo do Leaf:

```
leaf/
├── modules/
│   ├── crm/
│   ├── contacts/
│   ├── conversations/
│   ├── pipeline/
│   ├── scheduling/
│   ├── automation/
│   └── reporting/
├── shared/
├── infrastructure/
└── api/
```

Regras:

- um módulo não acessa diretamente tabelas internas de outro;
- comunicação entre módulos por interfaces explícitas;
- regras de negócio ficam dentro do produto;
- integrações externas entram por adapters;
- o banco pode ser compartilhado inicialmente, mas cada módulo deve possuir suas próprias tabelas ou schemas.

Exemplo:

```
leaf_crm.*
leaf_conversations.*
leaf_scheduling.*
leaf_automation.*
```

O módulo de conversas não deveria executar:

```sql
SELECT * FROM leaf_crm.contacts;
```

Ele deveria chamar algo como:

```typescript
contactsService.getContactByPhone(phone);
```

Essa disciplina permite transformar o módulo em serviço futuramente sem realizar uma lobotomia no sistema inteiro.

## 3\. O papel correto do n8n

O n8n deve ser a **camada de orquestração**, não o local definitivo das regras críticas do negócio.

Bom uso:

```
Webhook
  → normalização
  → chamada da API Leaf
  → execução do agente
  → envio pela Evolution
  → gravação do resultado
```

Uso perigoso:

```
Workflow com 140 nodes
  → regras comerciais
  → controle de planos
  → cálculo financeiro
  → estado do CRM
  → retries improvisados
  → JavaScript espalhado
```

Nesse segundo cenário, o workflow vira um monólito visual sem tipagem, testes ou fronteiras. Um espaguete com neon.

A regra deve ser:

> O n8n coordena. As aplicações decidem.

## 4\. Serviços que já justificam separação

Algumas funções da Ginkgo têm características operacionais diferentes e podem existir como serviços ou workers independentes desde cedo:

### Gateway de IA

LiteLLM ou equivalente para:

- roteamento de modelos;
- fallback;
- rate limits;
- registro de consumo;
- custo por tenant;
- políticas de modelo.

### Workers de mídia

Separar geração e processamento de:

- imagem;
- vídeo;
- áudio;
- transcrição;
- embeddings;
- documentos.

Esses workloads exigem filas, retries, limites e eventualmente GPU própria.

### Entrada de webhooks

Um serviço leve para receber eventos de:

- WhatsApp;
- Stripe;
- Meta;
- Google;
- Telegram;
- parceiros.

Ele valida, registra e joga o evento na fila. Assim, picos externos não derrubam o produto principal.

### Laplace/RAG

Pode continuar separado porque possui:

- armazenamento vetorial;
- ingestão de documentos;
- embeddings;
- recuperação;
- políticas próprias de cache e memória.

## 5\. Banco de dados

Para o estágio atual:

```
PostgreSQL Cluster
├── ginkgo_control
├── leaf
├── pyre
├── wave
├── laplace
└── observability
```

Ou, inicialmente:

```
PostgreSQL
└── database ginkgo
    ├── schema control
    ├── schema leaf
    ├── schema pyre
    └── schema wave
```

A primeira opção oferece isolamento maior. A segunda reduz operação e custo.

O importante não é quantos servidores existem. É impedir acesso cruzado descontrolado.

Redis deve ficar responsável por:

- cache;
- sessões temporárias;
- locks;
- rate limiting;
- filas;
- estado transitório.

Não deve virar banco permanente disfarçado.

## 6\. Comunicação

Dentro de cada produto:

```
chamadas internas tipadas
```

Entre produtos e Control Plane:

```
HTTP interno ou eventos
```

Para operações assíncronas:

```
Outbox Pattern
   ↓
Redis Streams / BullMQ / RabbitMQ
   ↓
Worker
```

Eventos possíveis:

```
tenant.created
subscription.activated
lead.created
conversation.received
campaign.published
payment.failed
usage.limit_reached
```

Isso permite desacoplamento sem criar uma ópera espacial de Kafka, Kubernetes e 47 dashboards antes de haver usuários.

## 7\. Quando extrair um módulo

Extraia somente quando pelo menos um destes fatores existir:

1. Precisa escalar independentemente.
2. Exige hardware diferente, como GPU.
3. Possui SLA ou disponibilidade próprios.
4. Representa uma fronteira relevante de segurança.
5. Derruba outras funções quando falha.
6. Tem equipe própria e ciclo de deploy próprio.
7. Mudanças nele estão bloqueando o restante do produto.

“Talvez um dia tenhamos milhões de usuários” não é requisito técnico. É fanfic arquitetural.

## 8\. Infraestrutura recomendada agora

A stack atual suporta bem essa arquitetura:

```
Traefik
Docker Compose
Portainer
PostgreSQL
Redis / BullMQ
Supabase
Evolution API
Chatwoot
n8n
LiteLLM
Laplace
OpenTelemetry
Grafana / Loki / Prometheus
```

**Kubernetes ainda não é necessário.**

Kubernetes deve aparecer quando houver:

- múltiplos servidores;
- replicação automática;
- autoscaling real;
- dezenas de deploys independentes;
- necessidade madura de self-healing;
- equipe capaz de operá-lo.

Instalar Kubernetes antes disso é contratar um porta-aviões para atravessar uma piscina.

## Plano de evolução

### Fase 1 — Agora

- monorepo;
- Control Plane modular;
- Leaf, Pyre e Wave separados por aplicação;
- Postgres e Redis compartilhados em infraestrutura;
- contratos claros;
- regras críticas fora do n8n;
- workers para tarefas pesadas.

### Fase 2 — Clientes recorrentes

- outbox e eventos;
- billing por consumo;
- observabilidade central;
- idempotência;
- retries e dead-letter queue;
- schemas ou bancos separados;
- deploy independente por produto.

### Fase 3 — Escala real

- extrair processamento de mídia;
- separar webhook gateway;
- replicar workers;
- separar serviços com carga própria;
- múltiplos nós;
- avaliar Kubernetes ou Nomad.

### Fase 4 — Plataforma madura

- service catalog;
- contratos versionados;
- OpenTelemetry distribuído;
- políticas de tenancy;
- autoscaling;
- disaster recovery;
- ambientes regionais.

## Veredito

Para a Ginkgo, a arquitetura ideal não é simplesmente “monólito”.

É uma **plataforma modular composta por poucos sistemas coesos**:

```
1 Control Plane
3 produtos modulares
3–6 serviços de infraestrutura especializados
workers escaláveis
integrações governadas pelo n8n
```

Isso oferece simplicidade suficiente para uma operação enxuta e fronteiras suficientes para crescer sem reconstruir tudo. O próprio guia descreve o monólito modular como a combinação da organização dos microserviços com a simplicidade operacional de um único deploy; essa é exatamente a lógica que deve orientar cada produto da Ginkgo.

Os números apresentados no material — como “80%”, “1 milhão de requisições” ou “50 desenvolvedores” — devem ser tratados como heurísticas, não como gatilhos automáticos. O verdadeiro sensor é a dor operacional mensurável.