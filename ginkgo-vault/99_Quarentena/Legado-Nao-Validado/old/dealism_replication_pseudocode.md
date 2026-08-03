# Exemplos Técnicos e Pseudocódigo para Replicação da Dealism

Este documento complementa a arquitetura proposta, fornecendo exemplos técnicos e pseudocódigo para a implementação dos principais componentes.

---

## 1. Workflow n8n para Processamento de DM do Instagram

Este pseudocódigo descreve um workflow simplificado no n8n que recebe uma mensagem do Instagram, processa-a com RAG e LLM, e envia uma resposta.

```pseudocode
// Workflow n8n: Processar Instagram DM

// 1. Trigger: Webhook (Instagram DM)
NODE: Instagram_DM_Webhook
  TYPE: Webhook
  CONFIG:
    Method: POST
    Path: /instagram-dm-inbound
  OUTPUT:
    message_text = $json.body.entry[0].changes[0].value.messages[0].text
    sender_id = $json.body.entry[0].changes[0].value.messages[0].from.id
    thread_id = $json.body.entry[0].changes[0].value.messages[0].id

// 2. Função: Preparar para RAG e LLM
NODE: Prepare_RAG_LLM_Input
  TYPE: Function
  INPUT:
    message_text,
    sender_id,
    thread_id
  CODE:
    // 2.1. Recuperar histórico de conversa do Supabase
    // SELECT * FROM conversations WHERE sender_id = sender_id ORDER BY timestamp DESC LIMIT 5
    conversation_history = SUPABASE.query('conversations', { sender_id: sender_id }, { order: 'timestamp.desc', limit: 5 })

    // 2.2. Gerar embedding para a mensagem atual
    current_message_embedding = COHERE_API.embed(message_text)

    // 2.3. Buscar documentos relevantes na base de conhecimento (Supabase RAG)
    // SELECT * FROM documents ORDER BY embedding <-> current_message_embedding LIMIT 3
    rag_context = SUPABASE.query('documents', { embedding_similarity: current_message_embedding }, { limit: 3 })

    // 2.4. Formatar input para o LLM
    system_prompt = "Você é um agente de vendas de IA para a Ginkgo AI Systems. Seu objetivo é engajar leads, responder perguntas e fechar vendas no Instagram. Mantenha um tom profissional e amigável, alinhado com a 'vibe' da marca. Use as informações fornecidas para responder."
    
    formatted_history = conversation_history.map(msg => `User: ${msg.user_message}\nAgent: ${msg.agent_response}`).join('\n')
    formatted_rag = rag_context.map(doc => `Documento: ${doc.content}`).join('\n')

    llm_input = `
      ${system_prompt}

      Contexto da Base de Conhecimento:
      ${formatted_rag}

      Histórico da Conversa:
      ${formatted_history}

      Mensagem do Usuário: ${message_text}
      Agente:
    `
  OUTPUT:
    llm_input,
    sender_id,
    thread_id,
    message_text

// 3. LLM: Gerar Resposta
NODE: Generate_LLM_Response
  TYPE: HTTP Request (ou nó de LLM específico, se disponível)
  CONFIG:
    Method: POST
    URL: https://api.openai.com/v1/chat/completions (ou Grok/Cohere endpoint)
    Headers:
      Authorization: Bearer {{OPENAI_API_KEY}}
      Content-Type: application/json
    Body:
      model: gpt-4.1-mini (ou outro modelo)
      messages: [
        { role: "user", content: $json.llm_input }
      ]
      temperature: 0.7
      max_tokens: 200
  OUTPUT:
    agent_response = $json.choices[0].message.content

// 4. Função: Salvar Histórico e Atualizar CRM (Supabase)
NODE: Save_Conversation_CRM
  TYPE: Function
  INPUT:
    sender_id,
    thread_id,
    message_text,
    agent_response
  CODE:
    // 4.1. Salvar nova interação no histórico de conversas
    SUPABASE.insert('conversations', {
      sender_id: sender_id,
      thread_id: thread_id,
      user_message: message_text,
      agent_response: agent_response,
      timestamp: NOW()
    })

    // 4.2. Lógica para atualização de CRM (ex: qualificação de lead)
    // IF agent_response CONTAINS "link de pagamento" THEN
    //   SUPABASE.update('customer_profiles', { sender_id: sender_id }, { status: 'Lead Qualificado', last_interaction: NOW() })
    // END IF
  OUTPUT:
    agent_response,
    sender_id

// 5. HTTP Request: Enviar Resposta para Instagram
NODE: Send_Instagram_DM
  TYPE: HTTP Request
  CONFIG:
    Method: POST
    URL: https://graph.facebook.com/v19.0/{{INSTAGRAM_PAGE_ID}}/messages
    Headers:
      Authorization: Bearer {{INSTAGRAM_ACCESS_TOKEN}}
      Content-Type: application/json
    Body:
      recipient: { id: $json.sender_id }
      message: { text: $json.agent_response }
  OUTPUT:
    status = $json.success

```

---

## 2. Pseudocódigo para Configuração da Base de Conhecimento (Supabase)

Este exemplo mostra como adicionar documentos e gerar embeddings no Supabase.

```sql
-- Tabela para armazenar documentos da base de conhecimento
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  content TEXT NOT NULL,
  embedding VECTOR(768) -- Usando o padrão de 768 dimensões (Ollama)
);

-- Função para gerar embedding e inserir documento
CREATE OR REPLACE FUNCTION embed_and_insert_document(content TEXT) RETURNS VOID AS $$
DECLARE
  new_embedding VECTOR(768);
BEGIN
  -- Chamar serviço de embedding (ex: função Supabase Edge Function que chama Cohere/Ollama)
  SELECT embedding_service_call(content) INTO new_embedding;
  
  INSERT INTO documents (content, embedding)
  VALUES (content, new_embedding);
END;
$$ LANGUAGE plpgsql;

-- Exemplo de uso:
SELECT embed_and_insert_document('Perguntas frequentes sobre o produto X: O produto X é um software de automação...');

-- Tabela para perfis de clientes (CRM simplificado)
CREATE TABLE customer_profiles (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  instagram_id TEXT UNIQUE NOT NULL,
  name TEXT,
  email TEXT,
  status TEXT, -- Ex: 'Lead', 'Qualificado', 'Cliente'
  last_interaction TIMESTAMP WITH TIME ZONE
);

-- Tabela para histórico de conversas
CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  sender_id TEXT NOT NULL REFERENCES customer_profiles(instagram_id),
  thread_id TEXT NOT NULL,
  user_message TEXT NOT NULL,
  agent_response TEXT NOT NULL,
  timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tabela para diretrizes de 
vibe_guidelines (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  brand_name TEXT NOT NULL,
  tone_of_voice TEXT, -- Ex: 'Formal', 'Amigável', 'Jovial'
  persona_description TEXT, -- Ex: 'Agente de vendas experiente e prestativo'
  example_conversations TEXT -- Exemplos de como o agente deve se comunicar
);

-- Exemplo de inserção de diretrizes de vibe
INSERT INTO vibe_guidelines (brand_name, tone_of_voice, persona_description, example_conversations)
VALUES (
  'Ginkgo AI Systems',
  'Profissional e Inovador',
  'Um especialista em automação de IA, focado em soluções escaláveis e eficientes.',
  'User: Olá, como posso automatizar meu Instagram?
  Agent: Olá! Para automatizar seu Instagram, podemos integrar nossa plataforma com a API oficial da Meta, permitindo gerenciar DMs, comentários e muito mais. Qual o seu principal objetivo com a automação?'
);
```

---

## 3. Exemplo de Prompt para LLM (com RAG e Histórico)

Este é um exemplo de como o `llm_input` seria construído no n8n para ser enviado ao LLM.

```text
Você é um agente de vendas de IA para a Ginkgo AI Systems. Seu objetivo é engajar leads, responder perguntas e fechar vendas no Instagram. Mantenha um tom profissional e inovador, alinhado com a 'vibe' da marca. Use as informações fornecidas para responder de forma concisa e útil. Se a pergunta for sobre preços, consulte a base de conhecimento e forneça a informação de forma clara.

Contexto da Base de Conhecimento:
Documento: Perguntas frequentes sobre o produto X: O produto X é um software de automação de marketing que integra-se com diversas plataformas de redes sociais, incluindo Instagram e WhatsApp. Preço: R$99/mês para 1000 conversas.
Documento: Diretrizes de Vibe: Tom de voz: Profissional e Inovador. Persona: Especialista em automação de IA.

Histórico da Conversa:
User: Olá, estou interessado em automação para Instagram.
Agent: Olá! Que ótimo! Para começarmos, qual o seu principal objetivo com a automação no Instagram? Você busca otimizar o atendimento, gerar leads ou algo mais específico?

Mensagem do Usuário: Qual o preço do produto X?
Agente:
```

---

## 4. Integração com a API do Instagram (via n8n)

Para enviar mensagens de volta ao Instagram, você precisará usar a API oficial da Meta. O n8n fará uma requisição HTTP POST para o endpoint de mensagens.

```json
// Exemplo de corpo da requisição HTTP POST para a API do Instagram
{
  "recipient": {
    "id": "{{sender_id_do_usuario}}"
  },
  "message": {
    "text": "{{resposta_gerada_pelo_llm}}"
  }
}
```

**Headers da Requisição:**
*   `Authorization: Bearer {{INSTAGRAM_ACCESS_TOKEN}}`
*   `Content-Type: application/json`

**Endpoint:**
`https://graph.facebook.com/v19.0/{{INSTAGRAM_PAGE_ID}}/messages`

---

## 5. Considerações Finais para Implementação

*   **Segurança:** Garanta que todas as chaves de API (OpenAI, Cohere, Instagram, Supabase) sejam armazenadas de forma segura (ex: variáveis de ambiente no n8n).
*   **Monitoramento e Logs:** Implemente um sistema robusto de logs no n8n e no Supabase para depuração e auditoria das conversas.
*   **Testes:** Realize testes extensivos com diferentes cenários de conversação para refinar o prompt do LLM e a base de conhecimento RAG.
*   **Feedback Loop:** Crie um mecanismo para coletar feedback humano sobre as respostas do agente, permitindo melhorias contínuas no treinamento e na lógica.

Esta abordagem modular e baseada em componentes permite que a Ginkgo AI Systems construa uma solução de automação de DM no Instagram altamente personalizada, escalável e com a inteligência de "Vibe Selling" que a Dealism oferece, mas com total controle e adaptabilidade à sua infraestrutura existente.
