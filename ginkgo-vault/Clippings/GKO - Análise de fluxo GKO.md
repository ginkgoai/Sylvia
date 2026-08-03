---
title: "GKO - Análise de fluxo GKO"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68c4d903-0750-832d-96a9-9ac9bdcc50dd"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 12 de set. às 23:37

![a54ccbbb-067b-4bbb-85b9-c0293d1937c2.png](https://chatgpt.com/backend-api/estuary/content?id=file-BQSMTk63jXFkKkXqNDrxF2&ts=495692&p=fs&cid=1&sig=d290d6e02e591fca2ebdbfb97ab79c8daedfd1e1dda42d94969eb6fd6c83f1f6&v=0)

GKO ATENDIMENTO.json

Arquivo

Perfeito, Gabriel. Analisei teu fluxo **GKO ATENDIMENTO.json** junto com o print do n8n. Aqui vai o raio-X do que você montou:

### 📌 Estrutura geral

- O workflow está dividido em **duas grandes etapas**:
	1. **Evolution API + Buffer + Tratamento da Mensagem** (azul).
		- Captura mensagens vindas do WhatsApp (Webhook → Variáveis → Switch).
				- Diferencia **texto, áudio, imagem, documento ou interativo**.
				- Converte mídias (base64 → arquivo).
				- Transcreve áudios (OpenAI).
				- Extrai conteúdo de PDFs.
				- Analisa imagens com GPT-4o.
				- Faz **push no Redis** para acumular histórico por sessão.
				- Depois junta o histórico e limpa a fila.
				- Passa um **payload normalizado** para o agente.
		2. **Classific Router + Agent** (vermelho).
		- Usa o **BRANN (Agente Supervisor)**.
				- BRANN recebe memória (Postgres), ferramentas (`Think_tool`), e os modelos OpenAI.
				- Regras de roteamento já embutidas:
			- Nova conversa → agente\_geral.
						- Continuidade → mantém mesmo agente.
						- Palavras-chave → loteamentos / construtora.
						- Fallback → agente\_geral.
				- Saída passa pelo **Parser Chain** que quebra em mensagens naturais para WhatsApp (negrito, tachado, itálico, links formatados).
				- Segmenta e envia de volta via Evolution API.

### 🔧 O que está certo

- **Normalização completa**: independentemente se o usuário manda áudio, imagem ou documento, o fluxo sempre cria um campo de texto coerente (`chatInput`).
- **Memória de conversa**: Redis (curto prazo) + Postgres (longo prazo).
- **Buffer inteligente**: garante que o agente sempre receba contexto acumulado, sem repetir mensagens antigas.
- **Classificação clara**: Switch inicial + BRANN com regras no `systemMessage`.
- **Output tratado**: Parser Chain força a resposta a respeitar Markdown do WhatsApp, evitando respostas “quebradas”.

### ⚠️ Pontos de atenção

1. **Dois Redis em paralelo** – o push e depois o delete estão certos, mas se o fluxo cair no `No Operation` (caso do Switch para tipos desconhecidos), pode ficar lixo na memória.
2. **Delay fixo** (`Wait 10s` e `1,2s`) pode gerar travas ou respostas demoradas em fila se o volume subir. Ideal seria condicional ou “debounce”.
3. **Fallback de mídia** – imagens/documentos hoje são processados mas não há branch claro se a análise falhar (ex.: PDF corrompido). BRANN vai receber só `''` no lugar.
4. **Classificação do Code1** está simplista (busca por “loteamento” ou “construção”). Pode ser expandida para intents mais ricas (ex: “orçamento”, “financiamento”, “arquitetura”).
5. **Agente único** – BRANN supervisiona tudo. Se você quiser escalabilidade, pode deixar BRANN apenas roteando e delegar mesmo a outros agentes n8n (um para cada área), não só “internamente” como agora.

### 🎯 Sugestão de próximos passos

- Revisar o `No Operation` → talvez transformar em log ou fallback, para não perder contexto.
- Adicionar um **If** logo após cada tratamento de mídia → se falhar, cair em “mensagem de erro amigável” antes de ir para BRANN.
- Expandir intents no `Code1` com regex ou até um modelo leve (GPT-4o-mini só para classificação).
- Ajustar os **Wait** para “apenas se múltiplas mensagens em lote” em vez de sempre.

Esse fluxo já está bem maduro, Gabriel — está praticamente no ponto de ser **um hub de atendimento comercial pronto para rodar produção**.

Quer que eu faça um **fluxo simplificado em diagrama textual** (mostrando o caminho exato que cada tipo de mensagem percorre, como um “mapa mental”)? Isso ajuda a visualizar antes de adicionar refinamentos.