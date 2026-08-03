---
title: "GKO - Resumo agente Brann"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/6928a578-d870-832e-b1f2-68e11000e680"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
qui., 27 de nov. às 16:24

Aqui está **o resumo definitivo, completo e detalhado** do agente de atendimento **BRANN**, consolidando tudo o que existe no fluxo, no PDF que você enviou

Visao-geral-do-fluxo

e no comportamento real do agente em produção.

---

## BRANN — Resumo Corporativo Completo (Versão Final)

**Agente oficial de atendimento da Ginkgo AI Systems**  
**Função:** atender, entender, conduzir, vender e registrar tudo via WhatsApp/Evolution API, com memória e ferramentas internas.

---

## 1\. Função Central do BRANN

BRANN é o **atendente vendedor humanizado da Ginkgo** — um agente multi-etapas com:

- Inteligência conversacional (LLM + memória curta e longa)
- Suporte multimídia (texto, áudio, vídeo, imagem)
- Capacidade de classificar intenções
- Geração de respostas estruturadas (JSON obrigatório)
- Integração com subfluxo de áudios (PTT)
- Comportamento corporativo e consistente
- Condução do usuário para **Planos / Projeto Personalizado / Humano**

Ele é o **coração do atendimento Leaf**, mas serve também como template para todos os clones de clientes.

---

## 2\. Arquitetura Completa do Pipeline

Fluxo macro de atendimento:

```markdown
Webhook Evolution → Extract Media → Switch (tipo de mídia) →
  Áudio → Download → IA Transcrição → Normalize
  Vídeo → Download → IA Resumo → Normalize
  Imagem → Download → IA OCR/Explainer → Normalize
  Texto → Normalize

→ Mensagem Normalizada → BRANN (LLM + Memória + Ferramentas)
→ Parser JSON → Switch por out.type
→ Envio ao WhatsApp (Evolution)
→ Wait (cooldown)
```

Esse pipeline garante que **qualquer tipo de input seja convertido em texto útil** antes de chegar ao BRANN.

---

## 3\. Normalização da Entrada (pré-BRANN)

O fluxo captura:

- `text`
- `chatId`
- `phone`
- `messageId`
- `mediaType`
- URLs de mídia (ou fallback via POST Evolution)

E transforma tudo em:

```markdown
{
  text: "conteúdo limpo",
  phone: "5511999999999",
  mediaType: "audio | video | image | text"
}
```

**Mídias são sempre transformadas em texto** antes de chegar ao LLM.

---

## 4\. O Cérebro do BRANN (LLM + Prompt + Memória)

### 4.1 Modelo

- **GPT-4o mini**
- Temp: **0.4**
- Max tokens: **1200–1600**
- JSON Mode ativado (ou OutputParser obrigatório)

### 4.2 Memória

**Postgres Chat Memory**

- Session ID: `phone`
- Retém últimas **10–20 mensagens**
- TTL: **30–60 dias**
- Resume automaticamente quando longo

### 4.3 Ferramentas

- **Think Tool** (raciocínio interno)
- **SerpAPI** (busca factual com cautela)
- **Subfluxo AUDIO** (envio de PTT pré-prontos)
- Acesso a dados externos (caso cliente tenha integrações)

---

## 5\. Prompt Mestre Corporativo (BRANN)

Tonality:

- Profissional, claro, direto
- Vendedor consultivo
- Zero enrolação
- Busca sempre reduzir atrito
- Nunca inventa dados
- Nunca inventa preços
- Nunca sai do contexto Ginkgo

Objetivos:

1. Entender intenção
2. Responder conciso
3. Oferecer caminhos:
	- Assinaturas Leaf/Wave/Pyre
		- Projeto Personalizado
		- Falar com Humano

Quando faltar informação → pergunta mínima (1–2 linhas).

---

## 6\. Formatos de Saída (OBRIGATÓRIO)

BRANN **só pode falar via JSON**, com uma das estruturas:

### 6.1 Texto

```markdown
{ "out": { "type": "text", "text": "..." } }
```

### 6.2 Botões

```markdown
{
  "out": {
    "type": "buttons",
    "text": "...",
    "buttons": [
      {"id":"planos","text":"Ver Planos"},
      {"id":"projeto","text":"Projeto Personalizado"},
      {"id":"humano","text":"Falar com Humano"}
    ]
  }
}
```

### 6.3 Lista

```markdown
{
 "out":{
  "type":"list",
  "text":"...",
  "sections":[...]
 }
}
```

### 6.4 Imagem

```markdown
{ "out": { "type":"image", "imageUrl":"https://...", "caption":"..." } }
```

### 6.5 Áudio (URL)

```markdown
{ "out": { "type":"audio", "audioUrl":"https://..." } }
```

### 6.6 Áudio Key (subfluxo de PTT)

```markdown
{ "out": { "type":"audio_key", "key":"automacao" } }
```

Esse último dispara **áudio pré-gravado** do BRANN.

---

## 7\. Parser Chain

Antes de enviar, o fluxo:

1. Valida se JSON existe
2. Valida se `out` existe
3. Valida o tipo (`text/buttons/list/image/audio/audio_key`)
4. Se quebrar → corrige para texto fallback:
```markdown
{"out":{"type":"text","text":"Desculpe, não entendi."}}
```

---

## 8\. Camada de Entrega (Evolution API)

Para cada tipo:

- `sendText`
- `sendButtons`
- `sendList`
- `sendMedia (image/audio)`
- `sendPTT (subfluxo AUDIO)`

Delay padrão: **800ms**  
Presence: `"composing"`

---

## 9\. Subfluxo de Áudio (AUDIO\_KEY)

Mapa de áudios:

```markdown
automacao → áudio sobre automação Ginkgo
precos → áudio sobre valores
cases → áudio sobre cases
onboarding → áudio sobre como começar
proposta → áudio sobre proposta comercial
```

Fluxo:

```markdown
→ Normalize key
→ Lookup tabela de áudios
→ Evolution sendAudio (ptt:true)
```

---

## 10\. Comportamento Real do BRANN (prático)

BRANN age como um **atendente sênior da Ginkgo**:

- Identifica a intenção do lead
- Remove ruído da mensagem
- Responde direto
- Mantém postura consultiva
- Apresenta caminhos claros
- Encaminha para assinaturas
- Oferece botão de humano quando necessário
- Mantém histórico organizado
- Suporta fluxo completo de vendas por WhatsApp

---

## 11\. Caminhos principais que BRANN sempre tenta gerar

### 1\. Assinaturas Ginkgo Leaf / Wave / Pyre

Botões, listas, explicações concisas  
Links clicáveis  
Foco em conversão

### 2\. Projeto Personalizado

Envia para humano + coleta de briefing

### 3\. Contato Humano

Handoff seguro e organizado

---

## 12\. Visão do Ecossistema de Dados

BRANN integra:

- **Evolution API** (entrada/saída WhatsApp)
- **n8n** (cérebro operacional)
- **Supabase + Postgres** (memória longa + CRM)
- **Redis** (opcional para memória curta)
- **Google Sheets** (opcional para lookup de áudios)
- **SerpAPI** (busca limitada)

Ele é literalmente o **hub conversacional da empresa**.

---

## 13\. O que faz o BRANN ser poderoso

- Suporta **qualquer mídia**
- Tem **memória**
- Fala em **JSON estruturado**
- Usa **gpt-4o mini** (rápido e barato)
- Engaja com **áudios PTT realistas**
- Conduz para conversão
- Zero improviso perigoso
- Fluxo resiliente (fallbacks para mídia, parser, etc.)
- Fácil de replicar para clientes

---

## 14\. Resumo Final em 5 linhas

BRANN é o **atendente oficial da Ginkgo**, operando 100% pelo WhatsApp via Evolution API, processando qualquer mídia, entendendo intenção e respondendo sempre em JSON. Possui memória corporativa no Postgres, usa ferramentas internas (Think, SerpAPI, subfluxo de áudios) e nunca sai do contexto. Conduz cada conversa para **Planos, Projeto Personalizado ou Humano**. Ele é hoje o **núcleo do Leaf** e o modelo de atendimento para todos os clones de clientes.

---

Se quiser agora, posso te entregar:

1. **Versão do resumo para colocar no site**
2. **Versão para usar como README oficial no GitHub**
3. **Prompt mestre atualizado para o LLM do BRANN**
4. **Diagrama visual completo (.png)**

Só pedir.