# Arquitetura Recomendada para Replicação da Dealism (Instagram DM Automation)

Para replicar as capacidades de automação de DM do Instagram da Dealism, focando no "Vibe Selling" e na conversação dinâmica, propomos uma arquitetura baseada em **LLMs com RAG (Retrieval-Augmented Generation)**, orquestração via **n8n** e persistência de dados no **Supabase**.

---

## 1. Visão Geral da Arquitetura

A arquitetura proposta visa criar um sistema modular e escalável, onde cada componente tem uma função clara, permitindo flexibilidade e manutenção. O fluxo principal envolve a ingestão de mensagens do Instagram, processamento por um LLM enriquecido com RAG, e a geração de respostas inteligentes e contextuais.

```mermaid
graph TD
    A[Instagram DM Webhook] --> B(n8n Workflow)
    B --> C{Processar Mensagem}
    C --> D[LLM (OpenAI/Grok/Cohere)]
    C --> E[RAG System (Supabase + Embeddings)]
    D -- Consulta Contexto --> E
    E -- Contexto Relevante --> D
    D -- Resposta Gerada --> B
    B --> F[Atualizar Supabase (Histórico/CRM)]
    B --> G[Enviar Resposta Instagram API]
    F -- Dados de Conversa/Lead --> H[CRM (UI)]
    G -- Mensagem de Volta --> A
```

---

## 2. Componentes da Arquitetura

### 2.1. Gateway de Mensagens (Instagram DM API)

*   **Função:** Receber e enviar mensagens do Instagram. A Meta oferece uma API oficial para parceiros, que é a forma mais segura e escalável de interagir com DMs do Instagram. Isso evita banimentos e garante conformidade.
*   **Integração:** Configurar um Webhook na plataforma de desenvolvedores da Meta para encaminhar novas mensagens de DM para o n8n.

### 2.2. Orquestrador de Workflows (n8n)

O n8n atuará como o cérebro da automação, gerenciando o fluxo de dados e a lógica de negócios.

*   **Gatilho (Webhook):** Recebe as mensagens do Instagram.
*   **Pré-processamento:** Normaliza o texto da mensagem, extrai metadados do remetente (ID do usuário, histórico de conversas).
*   **Roteamento Inteligente:** Decide se a mensagem precisa de uma resposta imediata (ex: FAQ simples), se deve consultar o LLM, ou se requer intervenção humana.
*   **Pós-processamento:** Formata a resposta do LLM, atualiza o histórico no Supabase e envia a resposta de volta para o Instagram.
*   **Integrações:** Conecta-se ao Supabase (para RAG e CRM), ao LLM e à API do Instagram.

### 2.3. Sistema de Geração Aumentada por Recuperação (RAG)

O RAG é fundamental para o "Vibe Selling" e para garantir que o LLM tenha acesso a informações específicas e atualizadas da sua empresa ou do seu cliente.

*   **Base de Conhecimento (Supabase):**
    *   **Tabela `documents`:** Armazena o conteúdo textual (FAQs, manuais, descrições de produtos, políticas, histórico de vendas bem-sucedidas) em formato de texto e seus respectivos embeddings vetoriais.
    *   **Tabela `customer_profiles`:** Armazena dados de clientes, histórico de interações, preferências e informações de CRM.
    *   **Tabela `brand_vibe_guidelines`:** Armazena diretrizes de tom de voz, persona da marca e exemplos de conversas para o "Vibe Selling".
*   **Geração de Embeddings:** Utilizar um modelo de embedding (ex: Cohere Embed v3, ou Ollama com 768 dimensões conforme sua preferência) para converter o texto da base de conhecimento em vetores numéricos.
*   **Busca de Similaridade:** Quando uma nova mensagem chega, o n8n envia a mensagem para o gerador de embeddings, que cria um vetor para a consulta. Este vetor é usado para buscar documentos semanticamente similares na tabela `documents` do Supabase.

### 2.4. Large Language Model (LLM)

O LLM é o coração da inteligência conversacional.

*   **Modelos Sugeridos:** OpenAI GPT-4, Grok, ou Cohere Command R+.
*   **Função:** Recebe a mensagem do usuário, o contexto recuperado pelo RAG e o histórico da conversa. Gera uma resposta natural, contextualizada e alinhada com a "vibe" da marca.
*   **Prompt Engineering:** Crucial para guiar o LLM a atuar como um agente de vendas, seguir as diretrizes de "Vibe Selling" e utilizar as informações do RAG de forma eficaz.

### 2.5. Banco de Dados (Supabase)

O Supabase servirá como o backend de dados para todo o sistema.

*   **Histórico de Conversas:** Armazena todas as interações para permitir que o LLM mantenha o contexto e para futuras análises.
*   **Perfis de Clientes (CRM):** Integração com a tabela `customer_profiles` para enriquecer as conversas com dados do cliente.
*   **Base de Conhecimento RAG:** Conforme detalhado acima.
*   **Monitoramento:** Armazena logs de desempenho do agente, métricas de conversão e feedback para otimização contínua.

---

## 3. Fluxo de Operação Detalhado

1.  **Mensagem Recebida:** Um usuário envia um DM no Instagram.
2.  **Webhook n8n:** O Webhook configurado na Meta API recebe a mensagem e a envia para um endpoint no n8n.
3.  **Pré-processamento n8n:** O workflow do n8n extrai o texto da mensagem, o ID do usuário e o timestamp.
4.  **Recuperação de Contexto (RAG):**
    *   O n8n envia a mensagem do usuário para um serviço de embedding (ex: Cohere API ou um serviço local Ollama).
    *   O embedding gerado é usado para consultar a tabela `documents` no Supabase, buscando os `k` documentos mais relevantes (usando busca de similaridade vetorial).
    *   O n8n também consulta o histórico de conversas do usuário no Supabase e o perfil do cliente na tabela `customer_profiles`.
5.  **Geração de Resposta (LLM):**
    *   O n8n constrói um prompt para o LLM, incluindo:
        *   **System Prompt:** Define a persona do agente (ex: "Você é um agente de vendas de IA para a marca X, com um tom de voz Y. Seu objetivo é qualificar leads e fechar vendas.").
        *   **Contexto RAG:** Os documentos mais relevantes recuperados do Supabase.
        *   **Histórico da Conversa:** As últimas `N` mensagens trocadas com o usuário.
        *   **Mensagem Atual do Usuário:** A pergunta ou declaração do cliente.
        *   **Diretrizes de Vibe Selling:** Instruções específicas sobre como negociar, lidar com objeções e fechar vendas.
    *   O n8n envia este prompt para o LLM.
6.  **Pós-processamento n8n:**
    *   O LLM retorna a resposta gerada.
    *   O n8n pode aplicar regras adicionais (ex: censura, formatação) ou detectar intenções para acionar outras ações (ex: "agendar reunião" -> chamar uma ferramenta de agendamento).
    *   A resposta é salva no histórico de conversas do Supabase.
7.  **Envio da Resposta:** O n8n envia a resposta final de volta para o usuário via API do Instagram.

---

## 4. Considerações de Escalabilidade e Otimização

*   **Gerenciamento de Tokens:** Monitorar e otimizar o uso de tokens do LLM é crucial para o custo. O RAG ajuda a manter o contexto relevante sem sobrecarregar o LLM com informações desnecessárias.
*   **Cache:** Implementar cache para embeddings e respostas comuns pode reduzir latência e custos.
*   **Monitoramento:** Dashboards no Supabase ou ferramentas externas para monitorar o desempenho do agente, taxas de conversão e feedback do usuário.
*   **Retreinamento Contínuo:** Aprimorar a base de conhecimento e os prompts do LLM com base nas interações reais para melhorar continuamente a qualidade das conversas.
*   **Handoff Humano:** Desenvolver um mecanismo robusto para que o agente possa escalar para um humano quando necessário, talvez com um alerta no CRM ou em uma ferramenta de atendimento.

---

Esta arquitetura fornece uma base sólida para replicar e até mesmo superar as capacidades da Dealism, oferecendo controle total sobre os dados, a lógica e a personalização para seus clientes SaaS.
