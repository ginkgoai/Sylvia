# Arquitetura para Dashboard de AIOps e Conversational AI

## 1. Conceito

A dashboard de AIOps e Conversational AI visa centralizar a monitorização, análise e interação com sistemas de automação e agentes de IA. Ela permitirá a visualização de métricas de desempenho, identificação de anomalias (AIOps) e a gestão de interações conversacionais (Conversational AI), utilizando Large Language Models (LLMs) para processamento e geração de insights. O foco é em escalabilidade, observabilidade e integração de APIs.

## 2. Arquitetura Recomendada

### 2.1. Camada de Ingestão de Dados (Data Ingestion Layer)

Esta camada é responsável por coletar dados de diversas fontes e prepará-los para armazenamento e processamento.

*   **Fontes de Dados:** Logs de sistemas, métricas de desempenho (CPU, memória, rede, etc.), eventos de APIs (n8n, Evolution API, Manus, OpenAI), transcrições de conversas (Telegram, WhatsApp), dados de uso de bots.
*   **Tecnologias:**
    *   **n8n:** Atuará como um orquestrador central para coletar dados de diversas APIs e sistemas. Pode ser configurado para: 
        *   Receber webhooks de eventos em tempo real (e.g., novas mensagens no WhatsApp via Evolution API, execuções de workflows no n8n).
        *   Realizar polling em APIs para coletar métricas e logs periodicamente.
        *   Transformar e normalizar os dados antes de enviá-los para a camada de armazenamento.
    *   **APIs Diretas:** Para integrações com sistemas de monitoramento existentes (e.g., Prometheus, Grafana, ELK Stack) ou para ingestão de dados de alta frequência que o n8n possa não ser o mais adequado.
    *   **Evolution API:** Para ingestão de dados de interações do WhatsApp (mensagens, status, eventos).
    *   **Manus:** Para ingestão de dados de tarefas, execuções e logs de agentes de IA.
    *   **OpenAI APIs:** Para coletar logs de uso e custos de chamadas a modelos de linguagem.

### 2.2. Camada de Armazenamento de Dados (Data Storage Layer)

Responsável por persistir os dados coletados de forma eficiente e acessível.

*   **Banco de Dados Principal:**
    *   **Supabase (PostgreSQL):** Escolha ideal para armazenar dados estruturados e semi-estruturados. Será utilizado para:
        *   **Métricas de AIOps:** Desempenho de sistemas, uso de recursos, latência de APIs, taxas de erro.
        *   **Logs de Eventos:** Eventos de sistema, execuções de workflows, interações de agentes.
        *   **Dados de Conversação:** Histórico de mensagens, transcrições, metadados de interação (canal, usuário, agente).
        *   **Perfis de Usuários/Clientes:** Informações relevantes para personalização de interações.
        *   **Configurações de Agentes:** Parâmetros, prompts, modelos utilizados.
        *   A funcionalidade de tempo real do Supabase (via WebSockets) pode ser explorada para atualizações dinâmicas na dashboard.
*   **Armazenamento de Documentos/Mídia:**
    *   **S3 (via Supabase Storage ou diretamente):** Para armazenar dados não estruturados, como transcrições de áudio de chamadas, imagens enviadas em conversas, documentos anexados e logs detalhados que não se encaixam bem em um banco de dados relacional.

### 2.3. Camada de Processamento e Análise (Processing & Analytics Layer)

Esta camada é o coração da inteligência da dashboard, onde os dados são transformados em insights.

*   **Processamento de Eventos/Stream:**
    *   **n8n:** Pode ser usado para processamento leve de eventos, como filtragem, agregação e enriquecimento de dados antes de serem enviados para o LLM ou para o banco de dados.
    *   **Funções Supabase (Edge Functions):** Para lógica de negócio serverless e processamento de dados em tempo real, como validação de dados ou pré-processamento antes de armazenar.
*   **Análise de AIOps:**
    *   **Modelos de Machine Learning (Python/Scikit-learn/TensorFlow/PyTorch):** Implementados como serviços Docker ou funções serverless (via Supabase Edge Functions ou n8n custom code) para:
        *   **Detecção de Anomalias:** Identificar padrões incomuns em métricas e logs (e.g., picos de erro, quedas de desempenho).
        *   **Previsão de Falhas:** Prever problemas futuros com base em tendências históricas.
        *   **Análise de Causa Raiz:** Correlacionar eventos para identificar a origem de problemas.
*   **Processamento de Linguagem Natural (NLP) e Geração de Insights (Conversational AI):**
    *   **Claude (via API):** O LLM principal para:
        *   **Sumarização de Conversas:** Gerar resumos concisos de interações longas.
        *   **Análise de Sentimento:** Avaliar o tom e a emoção nas conversas.
        *   **Extração de Entidades/Intenções:** Identificar informações chave e o propósito das mensagens.
        *   **Geração de Respostas/Sugestões:** Auxiliar agentes humanos ou automatizados com respostas contextuais.
        *   **Análise de Tendências Conversacionais:** Identificar tópicos recorrentes, problemas comuns ou oportunidades de melhoria.
    *   **OpenAI APIs (alternativa/complemento):** Para tarefas específicas de NLP ou para diversificar os modelos de LLM utilizados.

### 2.4. Camada de Orquestração de Agentes (Agent Orchestration Layer)

Gerencia a interação entre a dashboard, os LLMs e os agentes de automação.

*   **n8n:** Essencial para orquestrar fluxos de trabalho complexos:
    *   **Integração com LLMs:** Enviar prompts para Claude/OpenAI e processar as respostas.
    *   **Disparo de Ações:** Com base nos insights do LLM, disparar ações em outros sistemas (e.g., criar um ticket no ClickUp, enviar uma notificação via Telegram, iniciar um workflow de correção).
    *   **Gestão de Contexto:** Manter o contexto de conversas e interações para os LLMs.
*   **Manus:** Para a gestão e execução de agentes autônomos, permitindo que a dashboard monitore seu status e resultados.

### 2.5. Camada de Apresentação (Presentation Layer - Dashboard)

A interface do usuário para visualizar os dados e interagir com o sistema.

*   **Frontend:**
    *   **Tecnologias:** React/Next.js (TypeScript) para uma interface dinâmica e responsiva.
    *   **Visualização de Dados:** Bibliotecas como Chart.js, Recharts ou D3.js para gráficos e dashboards interativos.
    *   **Componentes:** Tabela de logs, gráficos de métricas, histórico de conversas, resumos gerados por IA, alertas de anomalias, interface para interação com agentes.
*   **Backend (API Gateway):**
    *   **Node.js (Express/Fastify) ou Python (FastAPI/Flask):** Para expor endpoints RESTful que o frontend consumirá.
    *   **Autenticação/Autorização:** Integrar com Supabase Auth para gerenciar acesso de usuários.
    *   **Proxy para LLMs:** Encaminhar requisições do frontend para Claude/OpenAI, adicionando lógica de segurança, rate limiting e logging.

## 3. Estrutura do Projeto (Exemplo)

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

## 4. Integrações Chave

| Componente | Integração com | Método | Observações |
| :--------- | :------------- | :----- | :---------- |
| **n8n** | Supabase | HTTP API, PostgreSQL Node | Ingestão de dados, atualização de métricas, logs. |
| | Claude/OpenAI | HTTP API | Envio de prompts, processamento de respostas. |
| | Evolution API | Webhook, HTTP API | Coleta de mensagens e eventos do WhatsApp. |
| | Manus | HTTP API | Monitoramento de agentes, disparo de tarefas. |
| | Telegram/WhatsApp | HTTP API (via Evolution API) | Envio de notificações, interação com usuários. |
| **Backend API** | Supabase | SDK (PostgREST) | Leitura/escrita de dados, autenticação. |
| | Claude/OpenAI | SDK/HTTP API | Proxy para o frontend, lógica de negócio com LLM. |
| **Frontend** | Backend API | HTTP/REST | Consumo de dados, envio de comandos. |
| | Supabase (Realtime) | SDK | Atualizações em tempo real para métricas e conversas. |
| **Supabase** | n8n, Backend API, Edge Functions | PostgREST, Realtime, Auth | Armazenamento centralizado, autenticação, lógica serverless. |

## 5. Fluxos de Automação Exemplares

### 5.1. Detecção de Anomalias e Alerta (AIOps)

1.  **Ingestão:** n8n coleta métricas de desempenho (CPU, memória) de servidores a cada 5 minutos via API de monitoramento.
2.  **Processamento:** n8n envia as métricas para uma Edge Function do Supabase.
3.  **Análise:** A Edge Function executa um modelo de ML (leve) para detectar anomalias. Se uma anomalia for detectada (e.g., uso de CPU > 90% por 3 leituras consecutivas).
4.  **Alerta:** A Edge Function dispara um webhook para um workflow n8n.
5.  **Orquestração:** O workflow n8n:
    *   Registra o alerta no Supabase.
    *   Envia uma notificação para um canal do Telegram/WhatsApp via Evolution API.
    *   Cria um ticket no ClickUp para a equipe de operações.
    *   Opcionalmente, envia um prompt para Claude para gerar uma análise inicial da causa provável e sugestões de mitigação, anexando-as ao ticket.

### 5.2. Sumarização de Conversas e Geração de Insights (Conversational AI)

1.  **Ingestão:** Evolution API envia um webhook para n8n a cada nova mensagem de WhatsApp.
2.  **Armazenamento:** n8n armazena a mensagem no Supabase, associada a um `conversation_id`.
3.  **Processamento (Assíncrono):** Após 10 minutos de inatividade na conversa (ou ao final da conversa), um workflow n8n é acionado (via agendamento ou evento).
4.  **LLM:** O workflow n8n recupera todo o histórico da conversa do Supabase e envia para Claude (via API) com um prompt como: `"Sumarize a seguinte conversa de atendimento ao cliente, identifique o problema principal, a solução proposta e o sentimento geral do cliente: [histórico da conversa]"`.
5.  **Insights:** Claude retorna o resumo, problema, solução e sentimento.
6.  **Atualização:** n8n atualiza o registro da conversa no Supabase com os insights gerados.
7.  **Dashboard:** A dashboard exibe o resumo e os insights, permitindo que os gerentes de atendimento monitorem a qualidade e identifiquem tendências.

## 6. Considerações de Escalabilidade

*   **Supabase:** Gerencia automaticamente a escalabilidade do PostgreSQL e oferece Edge Functions para lógica serverless.
*   **n8n:** Pode ser escalado horizontalmente com múltiplas instâncias e workers para lidar com alto volume de eventos.
*   **Docker:** Permite empacotar e escalar serviços de análise de ML e backend de forma independente.
*   **APIs de LLM:** Claude e OpenAI são serviços gerenciados e escalam automaticamente com a demanda.

## 7. Próximos Passos

1.  **Modelagem de Dados:** Detalhar o esquema do banco de dados no Supabase para logs, métricas e conversas.
2.  **Desenvolvimento de Workflows n8n:** Criar os workflows para ingestão, processamento e orquestração.
3.  **Implementação do Backend:** Desenvolver a API para servir o frontend e interagir com Supabase e LLMs.
4.  **Desenvolvimento do Frontend:** Construir a interface da dashboard com as visualizações e interações necessárias.
5.  **Configuração de Agentes Manus:** Integrar os agentes existentes e futuros para monitoramento e gestão.
