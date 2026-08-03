---
name: sexta-rag
description: >-
  Memória longa / base de conhecimento via RAG (AnythingLLM). Use quando o
  fundador perguntar algo que dependa de conhecimento acumulado, documentos,
  histórico, "o que sabemos sobre", contexto de vendas da Callima, materiais
  internos, ou pedir uma resposta fundamentada na base. Sempre cite a fonte.
---

# Skill: sexta-rag (AnythingLLM, somente consulta)

Consulte a base de conhecimento via AnythingLLM. **Somente leitura** (mode=query).
Rode com o Python do Hermes:

```
& "C:\Users\User\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe" "C:\sexta-feira\bridges\rag\anythingllm_client.py" <workspace> "<pergunta>"
```

## Workspaces
- `sexta-feira` → conhecimento próprio da orquestradora (padrão).
- `callima` → conhecimento de vendas/atendimento da Callima (LEITURA apenas;
  você observa, não personifica a Callima).

## Quando usar
- "O que a gente sabe sobre X?", "qual nosso material sobre Y?" → `sexta-feira`.
- Perguntas sobre o playbook/vendas da Callima → `callima`.
- Dúvidas factuais que devem vir da base interna, não da sua memória geral.

## Como responder
- Resuma a `answer` em linguagem natural e **cite as fontes** (campo `sources`)
  ao final. Não despeje o JSON cru.
- Se `sources` vier vazio, diga que não encontrou base e que está respondendo
  sem fonte interna (não invente fonte).
- Se `"ok": false` com erro de API key, avise que `bridges/rag/.env` precisa da
  API key do AnythingLLM.

## Regras
- Só consulta (query). Nunca tente treinar/escrever/embeddar documentos aqui.
- Não misture conhecimento da Callima como se fosse seu — atribua à fonte.
