# Plano de Implementação Detalhado para Dashboard de AIOps e Conversational AI

Este documento detalha o plano de implementação para a Dashboard de AIOps e Conversational AI, com foco em prompts específicos para serem utilizados com o Claude Code. A abordagem visa a construção modular e escalável, integrando as tecnologias definidas na arquitetura.

## 1. Visão Geral do Projeto

O objetivo é construir uma dashboard que centralize a monitorização, análise e interação com sistemas de automação e agentes de IA. A dashboard será capaz de visualizar métricas de desempenho, identificar anomalias (AIOps) e gerenciar interações conversacionais (Conversational AI), utilizando LLMs para processamento e geração de insights. A arquitetura é baseada em n8n, Supabase, Evolution API, Manus, OpenAI APIs e Claude.

## 2. Estrutura do Projeto

Conforme a arquitetura definida, a estrutura do projeto será organizada da seguinte forma:

```
/aiops-conversational-ai-dashboard
├── /frontend
│   ├── /src
│   │   ├── /components
│   │   ├── /pages
│   │   ├── /services (integração com backend/Supabase)
│   │   └── App.tsx
│   ├── package.json
│   └── tsconfig.json
├── /backend
│   ├── /src
│   │   ├── /routes
│   │   ├── /controllers
│   │   ├── /services (integração com Supabase, n8n, LLMs)
│   │   └── app.ts / app.py
│   ├── package.json / requirements.txt
│   └── Dockerfile
├── /n8n-workflows
│   ├── workflow-ingestao-logs.json
│   ├── workflow-processamento-whatsapp.json
│   └── workflow-disparo-alertas.json
├── /supabase
│   ├── /migrations
│   │   ├── 20230101000000_init.sql
│   │   └── ...
│   ├── /functions (Edge Functions)
│   │   ├── summarize-conversation.ts
│   │   └── anomaly-detection-webhook.ts
│   └── config.toml
├── /docker-compose.yml (para ambiente de desenvolvimento/local)
├── README.md
└── .env.example
```

## 3. Plano de Implementação por Camada com Prompts para Claude Code

### 3.1. Camada de Armazenamento de Dados (Supabase)

**Conceito:** Definir o esquema do banco de dados no Supabase para armazenar métricas de AIOps, logs de eventos, dados de conversação e configurações de agentes.

**Prompts para Claude Code:**

#### Prompt 3.1.1: Criação de Tabelas Iniciais no Supabase

```
"Crie um script SQL para o Supabase (PostgreSQL) que inclua as seguintes tabelas:

1.  **`metrics`**: Para armazenar métricas de AIOps.
    *   `id` (UUID, PK, default gen_random_uuid())
    *   `timestamp` (TIMESTAMP WITH TIME ZONE, NOT NULL, default now())
    *   `service_name` (TEXT, NOT NULL)
    *   `metric_name` (TEXT, NOT NULL)
    *   `value` (NUMERIC, NOT NULL)
    *   `unit` (TEXT)
    *   `metadata` (JSONB, default '{}')

2.  **`events`**: Para armazenar logs e eventos de sistema/aplicação.
    *   `id` (UUID, PK, default gen_random_uuid())
    *   `timestamp` (TIMESTAMP WITH TIME ZONE, NOT NULL, default now())
    *   `source` (TEXT, NOT NULL) - e.g., 'n8n', 'Evolution API', 'Manus'
    *   `event_type` (TEXT, NOT NULL) - e.g., 'workflow_executed', 'api_error', 'message_received'
    *   `severity` (TEXT, default 'INFO') - e.g., 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    *   `message` (TEXT, NOT NULL)
    *   `details` (JSONB, default '{}')

3.  **`conversations`**: Para armazenar o histórico de interações conversacionais.
    *   `id` (UUID, PK, default gen_random_uuid())
    *   `start_time` (TIMESTAMP WITH TIME ZONE, NOT NULL, default now())
    *   `end_time` (TIMESTAMP WITH TIME ZONE)
    *   `channel` (TEXT, NOT NULL) - e.g., 'whatsapp', 'telegram'
    *   `external_user_id` (TEXT, NOT NULL) - ID do usuário no canal externo
    *   `agent_id` (TEXT) - ID do agente que atendeu (se aplicável)
    *   `status` (TEXT, default 'OPEN') - e.g., 'OPEN', 'CLOSED', 'PENDING'
    *   `summary` (TEXT) - Resumo gerado por LLM
    *   `sentiment` (TEXT) - Sentimento geral da conversa (gerado por LLM)
    *   `main_problem` (TEXT) - Problema principal identificado (gerado por LLM)
    *   `solution_proposed` (TEXT) - Solução proposta (gerado por LLM)
    *   `metadata` (JSONB, default '{}')

4.  **`messages`**: Para armazenar mensagens individuais dentro de uma conversa.
    *   `id` (UUID, PK, default gen_random_uuid())
    *   `conversation_id` (UUID, FK para `conversations.id`, NOT NULL)
    *   `timestamp` (TIMESTAMP WITH TIME ZONE, NOT NULL, default now())
    *   `sender_type` (TEXT, NOT NULL) - 'user' ou 'agent'
    *   `content` (TEXT, NOT NULL)
    *   `message_type` (TEXT, default 'text') - e.g., 'text', 'image', 'audio'
    *   `metadata` (JSONB, default '{}')

Inclua também as chaves estrangeiras e índices necessários para otimização de consultas."```

#### Prompt 3.1.2: Criação de RLS (Row Level Security) para `conversations` e `messages`

```
"Crie políticas de Row Level Security (RLS) para as tabelas `conversations` e `messages` no Supabase. As políticas devem garantir que:

1.  Usuários autenticados possam `SELECT` em todas as conversas e mensagens.
2.  Usuários autenticados possam `INSERT` e `UPDATE` apenas em mensagens e conversas que eles criaram ou que estão associadas ao seu `agent_id` (se aplicável)."
```

### 3.2. Camada de Ingestão de Dados (n8n Workflows)

**Conceito:** Desenvolver workflows n8n para coletar dados de diversas fontes (Evolution API, Manus, OpenAI, sistemas de monitoramento) e inseri-los no Supabase.

**Prompts para Claude Code:**

#### Prompt 3.2.1: Workflow n8n para Ingestão de Mensagens do WhatsApp (Evolution API)

```
"Crie um workflow n8n que:

1.  Inicie com um nó `Webhook` para receber mensagens da Evolution API.
2.  Extraia `conversation_id`, `external_user_id`, `sender_type`, `content` e `timestamp` do payload do webhook.
3.  Verifique se a `conversation_id` já existe na tabela `conversations` do Supabase. Se não existir, crie uma nova entrada na tabela `conversations`.
4.  Insira a mensagem recebida na tabela `messages` do Supabase, associando-a à `conversation_id`.
5.  Utilize o nó `Supabase` para as operações de banco de dados.
6.  Retorne um status 200 para o webhook da Evolution API.

Forneça o JSON do workflow n8n."```

#### Prompt 3.2.2: Workflow n8n para Ingestão de Métricas de AIOps (Exemplo: Uso de CPU)

```
"Crie um workflow n8n que:

1.  Inicie com um nó `Cron` para ser executado a cada 5 minutos.
2.  Utilize um nó `HTTP Request` para fazer uma requisição GET a um endpoint fictício de monitoramento (e.g., `https://api.monitoramento.com/metrics/cpu`). Considere que o retorno é um JSON com `service_name`, `value` e `timestamp`.
3.  Transforme os dados para o formato da tabela `metrics` do Supabase, definindo `metric_name` como 'cpu_usage' e `unit` como '%'.
4.  Insira a métrica na tabela `metrics` do Supabase usando o nó `Supabase`.

Forneça o JSON do workflow n8n."```

### 3.3. Camada de Processamento e Análise (Supabase Edge Functions e n8n)

**Conceito:** Implementar lógica de negócio para detecção de anomalias e processamento de linguagem natural (NLP) usando Claude.

**Prompts para Claude Code:**

#### Prompt 3.3.1: Supabase Edge Function para Sumarização de Conversas com Claude

```
"Crie uma Supabase Edge Function (TypeScript) que:

1.  Receba um `conversation_id` via HTTP POST.
2.  Recupere todas as mensagens associadas a esse `conversation_id` da tabela `messages` do Supabase.
3.  Concatene as mensagens em um formato adequado para um prompt de LLM.
4.  Envie o texto concatenado para a API do Claude (Anthropic) com um prompt para sumarizar a conversa, identificar o problema principal, a solução proposta e o sentimento geral do cliente.
5.  Atualize a tabela `conversations` no Supabase com o `summary`, `sentiment`, `main_problem` e `solution_proposed` retornados pelo Claude.
6.  Retorne o resultado da sumarização.

Inclua a lógica para autenticação com a API do Claude usando uma chave de API (via variáveis de ambiente)."```

#### Prompt 3.3.2: Workflow n8n para Disparo da Sumarização de Conversas

```
"Crie um workflow n8n que:

1.  Inicie com um nó `Cron` para ser executado a cada 10 minutos (ou um nó `Webhook` que seja acionado por um evento de 'conversa finalizada').
2.  Consulte a tabela `conversations` do Supabase para encontrar conversas que estão 'OPEN' e que não foram sumarizadas recentemente (e.g., `summary` IS NULL ou `end_time` IS NOT NULL e `summary` IS NULL).
3.  Para cada conversa encontrada, chame a Supabase Edge Function de sumarização (criada no Prompt 3.3.1) passando o `conversation_id`.
4.  Utilize o nó `Supabase` para consultar e o nó `HTTP Request` para chamar a Edge Function.

Forneça o JSON do workflow n8n."```

### 3.4. Camada de Apresentação (Frontend - React/Next.js)

**Conceito:** Desenvolver a interface da dashboard para visualizar métricas, eventos e conversas, e interagir com os agentes.

**Prompts para Claude Code:**

#### Prompt 3.4.1: Componente React para Visualização de Métricas (Gráfico de Linhas)

```
"Crie um componente React (TypeScript) que:

1.  Receba como `props` um array de objetos de métricas (e.g., `[{ timestamp: '...', value: 10, unit: '%' }]`).
2.  Utilize uma biblioteca de gráficos (e.g., Chart.js ou Recharts) para renderizar um gráfico de linhas mostrando a evolução do `value` ao longo do `timestamp`.
3.  Exiba o `unit` no eixo Y.
4.  O componente deve ser responsivo.

Forneça o código React/TypeScript."```

#### Prompt 3.4.2: Página React para Listagem de Conversas com Sumário

```
"Crie uma página React (TypeScript) que:

1.  Faça uma requisição para um endpoint de API (e.g., `/api/conversations`) para obter uma lista de conversas, incluindo `id`, `start_time`, `external_user_id`, `status`, `summary`, `sentiment` e `main_problem`.
2.  Exiba as conversas em uma tabela paginada.
3.  Cada linha da tabela deve mostrar as informações principais da conversa.
4.  Ao clicar em uma conversa, um modal deve ser aberto exibindo o `summary`, `sentiment` e `main_problem` completos.
5.  Utilize `fetch` ou `axios` para a requisição API.

Forneça o código React/TypeScript."```

### 3.5. Camada de Backend (API Gateway - Node.js/FastAPI)

**Conceito:** Criar uma API para servir o frontend, intermediar requisições ao Supabase e, opcionalmente, a LLMs.

**Prompts para Claude Code:**

#### Prompt 3.5.1: Endpoint Node.js (Express) para Listar Conversas

```
"Crie um endpoint Node.js (Express, TypeScript) em `/api/conversations` que:

1.  Receba parâmetros de query para paginação (`limit`, `offset`).
2.  Utilize o SDK do Supabase para Node.js para consultar a tabela `conversations`, aplicando os limites e offsets.
3.  Retorne a lista de conversas e o total de registros.
4.  Inclua tratamento de erros.

Forneça o código Node.js/TypeScript."```

## 4. Próximos Passos e Considerações

*   **Autenticação:** Integrar o Supabase Auth no frontend e backend para gerenciar o acesso de usuários.
*   **Monitoramento:** Configurar ferramentas de monitoramento para a própria dashboard e seus serviços (n8n, Edge Functions).
*   **Testes:** Desenvolver testes unitários e de integração para todas as camadas.
*   **CI/CD:** Implementar um pipeline de CI/CD para automação de deploy.
*   **Dockerização:** Criar Dockerfiles para o backend e frontend para facilitar o deploy em ambientes de produção.

Este plano serve como um guia detalhado para a implementação, com prompts que podem ser diretamente utilizados com o Claude Code para acelerar o desenvolvimento de cada componente. A modularidade e a clareza dos prompts são cruciais para o sucesso da colaboração com o LLM."
