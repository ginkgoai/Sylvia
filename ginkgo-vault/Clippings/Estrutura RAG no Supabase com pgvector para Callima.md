---
title: "Estrutura RAG no Supabase com pgvector para Callima"
source: "https://manus.im/app/5vVe41nqKYtSIq41n2fua6"
author:
published:
created: 2026-07-19
description: "Manus é o motor de ação que vai além de respostas para executar tarefas, automatizar fluxos de trabalho e expandir seu alcance humano."
tags:
  - "clippings"
---
/

Manus 1.6 Lite

pronto

Perfeito! Agora vou inserir os 30 registros automaticamente. Aguarde...

Executar criação da tabela e inserção no Supabase

⚠️ Inseridos 20 de 30 registros. Os últimos 10 falharam por duplicação (já existiam). Vou limpar a tabela e reinserir todos os 30 registros corretamente.

Executar criação da tabela e inserção no Supabase

Identifiquei o problema! Há **registros duplicados do catálogo** (doc\_id `catalog_varejo_2025` aparece múltiplas vezes). Vou corrigir o arquivo JSON removendo duplicatas e inserir corretamente.

Executar criação da tabela e inserção no Supabase

🎉 **Perfeito! Todos os 30 registros foram inseridos com sucesso!**

Agora vou avançar para documentar a estrutura e criar o guia de uso.

Documentar estrutura e uso da nova tabela

Entregar resultado ao usuário

## 🎉 Tabela prv\_policies Criada e Populada com Sucesso!

## ✅ Resumo da Entrega

Criei e populei a tabela **`prv_policies`** no Supabase com **30 registros** de políticas, regras e catálogo da PRV Alimentos.

## 📊 Estatísticas Finais

| Métrica | Valor |
| --- | --- |
| **Total de registros** | 30 |
| **Políticas (policy)** | 20 |
| **Catálogo (catalog)** | 10 |
| **Prioridade 5 (crítica)** | 11 |
| **Prioridade 4 (alta)** | 11 |
| **Prioridade 3 (média)** | 6 |

## 🎯 Políticas Críticas (Prioridade 5)

As 11 políticas de maior prioridade incluem:

1. **Regra absoluta sobre preços** — Callima nunca inventa valores
2. **Como consultar preços na base oficial** — Procedimento obrigatório
3. **O que a PRV não faz** — Limites e guardrails
4. **Farinhas e produtos do catálogo** — Informações de produtos

## 📦 Arquivos Entregues

### 1\. DOCUMENTACAO\_PRV\_POLICIES.md

Guia completo com:

- Schema da tabela
- Funções RPC disponíveis
- Exemplos de uso no n8n
- Estratégias de integração

### 2\. prv\_policies\_FINAL.zip

Contém:

- SQL de setup completo
- SQL de inserção
- Documentação

## 🚀 Como Usar no n8n

### Opção 1: Busca por Texto (Full-Text Search)

Use a função `search_prv_policies` para buscar no título e conteúdo:

```
SELECT title, content, relevance
FROM search_prv_policies(
    '{{ $json.userQuery }}',
    'prv',
    5
);
```

### Opção 2: Busca por Prioridade

Carregue apenas as regras críticas (prioridade >= 4):

```
SELECT title, content, priority
FROM get_prv_policies_by_type(
    'policy',
    'prv',
    4
);
```

### Opção 3: Consulta Direta

Busque por `doc_id` específico:

```
SELECT content
FROM prv_policies
WHERE doc_id = 'policy_regra_precos';
```

## 🎯 Integração com RAG

### Estratégia Recomendada:

1. **Primeiro:** Busque na tabela `prv_policies` para regras de negócio
2. **Depois:** Use RAG (`rag_callima_chunks`) para conhecimento geral
3. **Combine:** Ambos os resultados no contexto do LLM

Isso garante que regras críticas sempre sejam consideradas, enquanto o RAG fornece contexto adicional.

## ✅ Próximos Passos

1. **Teste as funções** no Supabase SQL Editor
2. **Integre no n8n** usando os exemplos fornecidos
3. **Ajuste o prompt** da Callima para priorizar políticas de alta prioridade
4. **Monitore** a qualidade das respostas

**🎉 Sua base de conhecimento está pronta para uso!**

Tarefa concluída

Como foi este resultado?

Entregar resultado ao usuário

Manus is an AI Agent and can make mistakes. Please double-check before use.