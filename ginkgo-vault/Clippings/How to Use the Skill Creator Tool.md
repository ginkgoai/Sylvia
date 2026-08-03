---
title: "How to Use the Skill Creator Tool?"
source: "https://manus.im/app/S6LW0kPSh5LQoxBrzWaiCn"
author:
published:
created: 2026-07-19
description: "Manus é o motor de ação que vai além de respostas para executar tarefas, automatizar fluxos de trabalho e expandir seu alcance humano."
tags:
  - "clippings"
---
/

Manus 1.6 Lite

PRECISO DE ALGO SIMPLES E FUNCIONAL, O N8N VIA AGENT VAI PERGUNTAR ALGO PARA A MANUS E A MANUS VAI TRAZER A RESPOSTA BASEADA NOS DADOS QUE ELA TEM SOBRE O ASSUNTO E A SUPABASE, VAI RETORNAR A RESPOSTA PRO AGENT N8N E ELE VAI SEGUIR O FLUXO APARTIR DAI.

Perfeito! Entendi completamente. Você quer algo **simples e direto**:

1. **Agent n8n** faz uma pergunta para a **Manus**
2. **Manus** busca a resposta (usando seus dados + Supabase)
3. **Manus** retorna a resposta
4. **Agent n8n** continua o fluxo com essa resposta

Isso é um **padrão síncrono simples**. Vou criar:

✅ **Um nó HTTP Request único** (POST) que faz tudo isso  
✅ **Configuração pronta para copiar/colar**  
✅ **Exemplo de como integrar com o agente**  
✅ **Sem loops, sem complexidade**

Deixa eu criar isso agora! 🚀

Entregar solução final

Criar nó HTTP Request simples e funcional

## ⚡ Solução Simples e Funcional: Manus + n8n

Criei exatamente o que você pediu - **simples e direto**:

### 📦 Arquivo: Manus\_Simples\_Funcional.json

Um **único nó HTTP Request** que:

- ✅ Recebe a pergunta do agent
- ✅ Envia para a Manus
- ✅ Manus busca nos dados + Supabase
- ✅ Retorna a resposta
- ✅ Agent continua o fluxo

**Sem loops, sem complexidade, sem timeouts.**

### 🚀 Setup em 3 Passos

**Passo 1:** Importe `Manus_Simples_Funcional.json` no n8n  
**Passo 2:** Configure a credencial com sua API Key  
**Passo 3:** Conecte como ferramenta do agente Callima

### 📝 Fluxo

```
Agent n8n
    ↓
[Pergunta] "Qual é o preço?"
    ↓
[Nó HTTP POST] → Manus
    ↓
[Manus] (busca dados + Supabase)
    ↓
[Resposta] "Preço: R$ 79,90"
    ↓
[Agent] continua com a resposta
```

### 📊 Entrada e Saída

**Entrada:**

```
{
  "pergunta": "Qual é o preço da camisa branca?",
  "user_id": "5521987654321",
  "user_name": "João Silva"
}
```

**Saída:**

```
{
  "answer": "Sim! Temos a camisa branca tamanho P. Preço: R$ 79,90.",
  "confidence": 0.95,
  "request_id": "req_abc123"
}
```

### ✅ Checklist Rápido

- Arquivo importado
- Credencial configurada
- Nó conectado como ferramenta
- Teste realizado
- Workflow ativado

**Tudo pronto para usar!** 🎉

Tarefa concluída

Como foi este resultado?

Entregar solução final

Manus is an AI Agent and can make mistakes. Please double-check before use.