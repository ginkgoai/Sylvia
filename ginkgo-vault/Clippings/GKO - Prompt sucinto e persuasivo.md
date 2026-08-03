---
title: "GKO - Prompt sucinto e persuasivo"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/690641cc-57dc-8328-8ddf-cc0b16e81d8b"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 1 de nov. às 14:22

Use este prompt ajustado para o agente do WhatsApp (Brann ou G-Tech) responder de forma curta, convincente e com links diretos para cada plano:

---

**Prompt corporativo (versão curta e persuasiva):**

Você é o assistente de vendas da **Ginkgo AI Systems**, especializado em automação inteligente para empresas.

Fale sempre de forma **objetiva, clara e persuasiva**, mantendo tom profissional e amigável.  
Seu objetivo é **explicar rapidamente o valor da automação** e direcionar o cliente para o plano ideal com o **link direto de contratação**.

### Estrutura de resposta:

1. **Explique o que é automação** em **1 parágrafo curto** (foco em benefício, não definição técnica).
2. Se o cliente pedir opções ou preços, **apresente os 3 planos com links diretos**:
```markdown
Automatizar tarefas reduz custos e tempo, enquanto melhora a experiência do cliente.  
Conheça nossos planos:

1. **Plano Básico** – Atendimento automatizado via WhatsApp.  
👉 [Assinar por R$ 449/mês](https://ginkgoai.systems/planos/basico)

2. **Plano Avançado** – Inclui automação de marketing e comunicação.  
👉 [Assinar por R$ 749/mês](https://ginkgoai.systems/planos/avancado)

3. **Plano Futurista** – Gestão empresarial inteligente completa.  
👉 [Assinar por R$ 1.199/mês](https://ginkgoai.systems/planos/futurista)

Precisa de ajuda para escolher? Posso recomendar o melhor para seu caso.
```
3. **Se o cliente quiser detalhes específicos**, aprofunde com frases curtas e foco em resultado (“reduz tempo”, “aumenta lucro”, “melhora atendimento”).
4. Nunca repita textos longos nem defina novamente o termo automação.

---

Quer que eu gere o JSON pronto para importar no **n8n (node BRANN)** já com esse novo comportamento?

Segue o desenho prático. Curto, direto e “copy/cola”.

## Visão rápida

- BRANN decide a resposta e **pede ferramentas por intenção**.
- Saída sempre em **JSON `out.*`** para o roteador (text | buttons | list | image | audio | audio\_key).
- Memória guarda **últimas 10–20 msg** por `sessionId = phone`.
- Subworkflow **AUDIO\_PTT** envia PTTs prontos por chave.

---

## Tools do Agent

## 1) OpenAI – Main (Chat Model BRANN)

**Uso:** resposta principal, sumarização curta, geração de call-to-action.  
**Quando:** sempre.  
**Input:** `text` limpo do usuário + contexto curto.  
**Output:** JSON obrigatório:

```markdown
{ "out": { "type": "text", "text": "..." } }
```

ou:

```markdown
{ "out": { "type": "buttons", "text": "...", "buttons": [
  {"id":"plano_basico","text":"Assinar Básico"},
  {"id":"plano_avancado","text":"Assinar Avançado"},
  {"id":"plano_futurista","text":"Assinar Futurista"}
]}}
```

**Config n8n (resumo):**

- Model: `gpt-4o-mini`
- Temperature: `0.4`
- Max tokens: `1200`
- JSON mode: `on`
- Stop: vazio

**System (cole):**

```markdown
Você é o assistente de vendas da Ginkgo AI Systems. Fale curto, claro e persuasivo.
Quando perguntarem por planos, retorne BOTÕES com os 3 planos e links diretos:
- Básico: https://ginkgoai.systems/planos/basico
- Avançado: https://ginkgoai.systems/planos/avancado
- Futurista: https://ginkgoai.systems/planos/futurista
Formato OBRIGATÓRIO: JSON em { "out": ... } sem texto fora do JSON.
```

## 2) Memory (Postgres/Redis Chat Memory)

**Uso:** histórico mínimo e contexto do perfil.  
**Quando:** sempre antes do model.  
**Chave:** `{{$json.phone || $json.chatId}}`  
**Janela:** 10–20 mensagens; **TTL:** 30 dias.  
**Boas práticas:** sumarizar quando >15 msgs.

## 3) Think (Rascunho interno)

**Uso:** planejar resposta em tópicos sem vazar ao usuário.  
**Quando:** decisão de plano, objeções, “qual plano ideal?”.  
**Input:** intenção + 3 bullets do caso.  
**Output:** somente texto interno → injetado no `system` do Model.  
**Guard rail:** nunca encaminhar saída do Think ao usuário.

## 4) Calculator

**Uso:** contas simples de ROI, % de redução de tempo, projeções.  
**Quando:** usuário pergunta “quanto economizo”, “em quantos dias paga”.  
**Output:** número ou string curta → Model compõe a resposta.

## 5) SerpAPI

**Uso:** fato externo sensível a tempo (horário, preço de terceiros, estatística recente).  
**Quando:** Model solicitar explicitamente.  
**Throttle:** baixo.  
**Output:** resumo objetivo de 1–2 linhas para o Model.

## 6) TTS AUDIO (desativado por padrão)

**Uso:** transformar texto de proposta em áudio.  
**Ative** quando quiser leitura automática.  
**Output:** URL de áudio → `out.type="audio"`.

## 7) MCP Tools (desativado por padrão)

**Uso:** ações operacionais: criar cliente, registrar lead, iniciar ingestão RAG.  
**Ative** quando o fluxo comercial estiver fechado.  
**Retornos padrão:**

```markdown
{ "ok": true, "id": "cli_123", "note": "lead criado" }
```

---

## Subworkflow: AUDIO\_PTT

**Objetivo:** enviar **áudios prontos** por chave sem usar TTS.  
**Entrada esperada:**

```markdown
{ "phone": "55XXXXXXXXXXX", "key": "automacao|proposta|cases|onboarding|precos", "text": "opcional" }
```

## Passos

1. **Normalize (Function)**
```markdown
const key = (item.json.key||"").toLowerCase();
const map = {
  automacao: "https://cdn.seu-dominio/ptt/automacao.ogg",
  proposta:  "https://cdn.seu-dominio/ptt/proposta.ogg",
  cases:     "https://cdn.seu-dominio/ptt/cases.ogg",
  onboarding:"https://cdn.seu-dominio/ptt/onboarding.ogg",
  precos:    "https://cdn.seu-dominio/ptt/precos.ogg"
};
item.json.audioUrl = map[key] || map["automacao"];
return item;
```
2. **Send PTT (HTTP Request → Evolution)**
- Method: `POST`
- URL: `={{$env.EVOLUTION_BASE_URL}}/message/sendAudio/{{$env.EVOLUTION_INSTANCE}}`
- Headers:
	- `Authorization: ={{'Bearer ' + $env.EVOLUTION_TOKEN}}`
		- `Content-Type: application/json`
- Body (RAW JSON):
```markdown
{
  "number": "={{$json.phone}}",
  "mediaData": {
    "url": "={{$json.audioUrl}}",
    "ptt": true
  }
}
```
- Response: JSON
3. **Return (Set)**
```markdown
item.json.out = { type: "audio", audioUrl: item.json.audioUrl };
return item;
```

**Integração com o Agent:**  
Quando o BRANN quiser um PTT, ele devolve:

```markdown
{ "out": { "type": "audio_key", "key": "automacao" } }
```

O Switch envia para **AUDIO\_PTT** e retorna o envio.

---

## Env e rotas Evolution (mínimo)

```markdown
EVOLUTION_BASE_URL=https://SEU-HOST:SEU-PORT
EVOLUTION_TOKEN=SEU_TOKEN
EVOLUTION_INSTANCE=BRANN
```

**Enviar texto**

```markdown
POST /message/sendText/{INSTANCE}
{ "number": "55XXXXXXXXXXX",
  "options": { "delay": 800, "presence": "composing" },
  "textMessage": { "text": "={{$json.out.text}}" } }
```

**Enviar botões**

```markdown
POST /message/sendButtons/{INSTANCE}
{ "number": "={{$json.phone}}",
  "buttonMessage": { "text": "={{$json.out.text}}", "buttons": "={{$json.out.buttons}}" } }
```

**Enviar lista**

```markdown
POST /message/sendList/{INSTANCE}
{ "number": "={{$json.phone}}",
  "listMessage": { "title":"Ginkgo AI Systems","text":"={{$json.out.text}}","buttonText":"Abrir opções","sections":"={{$json.out.sections}}" } }
```

---

## Prompt de vendas embutido (sucinto, com links)

Cole no **System** do BRANN:

```markdown
Fale curto, claro e persuasivo. Foque em benefício e próximo passo.
Quando pedirem planos ou preço, retorne BOTÕES com os 3 planos e links:
- Básico: https://ginkgoai.systems/planos/basico
- Avançado: https://ginkgoai.systems/planos/avancado
- Futurista: https://ginkgoai.systems/planos/futurista
Formato de saída: somente JSON em { "out": ... }.
Nunca explique o que é automação por mais de 1 parágrafo.
```

---

## Teste rápido

1. Usuário: “Quero saber preços” → **buttons** com 3 planos + links.
2. Usuário: “Pode mandar áudio explicando onboarding” → **audio\_key:onboarding** → PTT.
3. Usuário: “Quanto economizo?” → Calculator → resposta em 1 linha + CTA.

Se quiser, envio o **JSON de import do subworkflow AUDIO\_PTT** e o **roteador out.type** prontos.

2/3