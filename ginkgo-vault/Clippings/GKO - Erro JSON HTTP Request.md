---
title: "GKO - Erro JSON HTTP Request"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/6923615c-b8e4-832a-93aa-9cadfc71aaa8"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
dom., 23 de nov. às 16:32

tool de audio fluxo prv. faça uma avaliação minuciosa do que esta dando errado.

Vamos direto:

Hoje o gargalo não é o ElevenLabs, é o envio do áudio para o Evolution.  
O `Bad request – please check your parameters` está vindo do **HTTP Request1** (sendMedia).

Vou dissecar ponto a ponto.

---

## 1\. Onde está o erro crítico

### 1.1. JSON do HTTP Request1 inválido

No último node:

```markdown
{
  "number": "5553921448730@s.whatsapp.net",
  "mediatype": "audio",
  "media": {{ 'data:audio/mpeg;base64,' + $binary.data.toString('base64') }}
}
```

Repara em duas coisas:

1. A expressão não está com `=`.
2. Ela não está entre aspas.

O preview embaixo mostra algo assim:

```markdown
{
  "number": "5553921448730@s.whatsapp.net",
  "mediatype": "audio",
  "media": data:audio/mpeg;base64,AAA...
}
```

Ou seja: o valor de `media` chega **sem aspas** → o body que o Evolution recebe não é JSON válido → 400 (Bad Request).

### Como corrigir

Troca o body para:

```markdown
{
  "number": "={{ $json.phone || $json.chatId || '5553921448730@s.whatsapp.net' }}",
  "mediatype": "audio",
  "media": "={{ 'data:audio/mpeg;base64,' + $binary.data.toString('base64') }}"
}
```

Regras:

- Sempre usar `="={{ ... }}"` quando for expressão dentro de JSON.
- Sempre manter o valor como **string JSON**.

Depois de salvar, executa só o `HTTP Request1` com um item de teste que já tenha o binário `data` e vê se o erro some.

---

## 2\. Problemas de dados antes do TTS (vão te morder depois)

### 2.1. mensagem\_audio não está chegando

No node `Entrada TTS`:

- Schema: `instance`, `phone`, `mensagem_audio`.
- No OUTPUT de teste aparecem só `instance` e `phone`.

Ou seja, no teste fixo você não está mandando `mensagem_audio`.  
No node `Set`:

```markdown
texto_limpo = {{ $json.mensagem_audio.replace(/\n/g, '').replace(/\r/g, '').replace(/_/g, '') }}
```

Como `mensagem_audio` está `undefined`, o resultado é:

- `texto_limpo: [null]`

Por isso, no HTTP para a ElevenLabs aparece:

```markdown
"text": "{{$json.texto_limpo}}"
```

Preview:

```markdown
"text": ""
```

Não quebra o fluxo, mas você está pedindo para a ElevenLabs gerar áudio de texto vazio.

### Como deixar robusto

No `Set` troca para:

```markdown
{{ 
  ($json.mensagem_audio || '')
    .replace(/\n/g, ' ')
    .replace(/\r/g, ' ')
    .replace(/_/g, ' ')
}}
```

Ou, se quiser mais explícito:

- Field: `texto_limpo`
- Value:
```markdown
{{ 
  $json.mensagem_audio 
    ? $json.mensagem_audio.replace(/\n/g, ' ').replace(/\r/g, ' ').replace(/_/g, ' ')
    : ''
}}
```

E garante no **Execute Workflow** do fluxo PRV que o input `mensagem_audio` está vindo de:

```markdown
mensagem_audio: {{ $json.output }}
```

(com o campo certo do node anterior).

---

## 3\. ElevenLabs – está quase certo, só depende do texto

O node `HTTP Request` (ElevenLabs) está ok:

- Method: `POST`
- Body:
```markdown
{
  "text": "{{$json.texto_limpo}}",
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.5,
    ...
  }
}
```
- Output: Binary `data.mpeg` → está chegando certinho.

Problema aqui não é parâmetro, é **conteúdo vazio** por causa do `texto_limpo` nulo.  
Arrumando o `Set`, esse trecho fica saudável.

---

## 4\. Envio para Evolution – alinhamento com a arquitetura

Na visão geral do fluxo BRANN / subfluxo ÁUDIO, a recomendação é usar o endpoint de **áudio com URL**:

```markdown
{
  "number": "={{$json.phone || $json.chatId}}",
  "mediaData": {
    "url": "={{$json.out.audioUrl}}",
    "ptt": true
  }
}
```

E o subfluxo de áudio recomendado no doc usa `/message/sendAudio` com URL pública do arquivo, não base64 direto.

Visao-geral-do-fluxo

Hoje você está fazendo:

- ElevenLabs → binário dentro do n8n.
- Depois `/message/sendMedia/PRV_Alimentos` com `media` base64 inline.

Funciona, mas é mais sensível a erro.

Se quiser ficar 100% alinhado com a arquitetura documentada, um caminho mais sólido:

1. Depois do ElevenLabs, salva o binário num storage acessível (S3/minio/drive com link público).
2. Gera um `audioUrl`.
3. No `HTTP Request1` chama `/message/sendAudio` ou `/message/sendMedia` com:
	```markdown
	{
	  "number": "={{ $json.phone || $json.chatId }}",
	  "mediaData": {
	    "url": "={{ $json.audioUrl }}",
	    "ptt": true
	  }
	}
	```

Mas isso é um “upgrade”. O mínimo para parar de quebrar é corrigir o JSON e alimentar direito o `mensagem_audio`.

---

## 5\. Checklist rápido para você validar

1. `Entrada TTS`
	- `mensagem_audio` chega com texto quando chamado pelo fluxo PRV.
		- Remove/ajusta o “Pinned data” de teste para incluir `mensagem_audio` ou desfixa.
2. `Set (texto_limpo)`
	- Usa fallback para `''` se `mensagem_audio` vier vazio.
		- No preview, `texto_limpo` mostra uma string real.
3. `HTTP Request (ElevenLabs)`
	- `text` no preview está com a frase esperada.
		- Output Binary → `data.mpeg` presente.
4. `HTTP Request1 (Evolution)`
	- Body JSON em n8n:
		```markdown
		{
		  "number": "={{ $json.phone || $json.chatId }}",
		  "mediatype": "audio",
		  "media": "={{ 'data:audio/mpeg;base64,' + $binary.data.toString('base64') }}"
		}
		```
		- Preview mostra `"media": "data:audio/mpeg;base64,AAAA..."` **com aspas**.
		- Executando apenas esse node com um item de teste, o WhatsApp recebe o áudio.

Se seguir esses 4 blocos, o “tool de áudio” entra nos trilhos e o PRV passa a mandar PTT redondo a partir do texto da IA.

dom., 23 de nov. às 23:53

Sim — agora **estamos MUITO mais perto do correto**, mas ainda tem **dois ajustes críticos** que precisam ser feitos para o fluxo finalmente rodar **100% zero erro**.

Vou te guiar ponto a ponto.

---

## ✔️ 1. A mudança que você fez MELHOROU muito

Você corrigiu o problema principal:

- Trocou o envio via **HTTP Request manual** para o **node Evolution oficial**
- Botou o campo `audio` usando:  
	`{{ $binary.data.toString('base64') }}`
- Acertou a instância, número, etc.

Isso é **correto** e é exatamente o uso recomendado.

Porém…

---

## 🚨 2. Problema atual: sua entrada está vazia

Veja seu print do node **Entrada TTS**:

```markdown
instance: null
phone: null
mensagem_audio: null
```

Se isso estiver **nulo**, nada no fluxo vai funcionar.

Isso significa:

## 🔥 O PRV não está enviando corretamente os parâmetros ao chamar este workflow.

Você PRECISA que o fluxo PRV envie algo assim no Execute Workflow:

```markdown
{
 "instance": "PRV_Alimentos",
 "phone": "55392xxxxx@s.whatsapp.net",
 "mensagem_audio": "Olá, tudo bem? Aqui está sua resposta em áudio!"
}
```

Hoje ele está chamando assim:

**instance → vazio  
phone → vazio  
mensagem\_audio → vazio**

Por isso, no node ElevenLabs:

```markdown
Text: {{ $json.mensagem_audio }}
```

→ sai `null`  
→ não gera áudio  
→ Evolution não recebe nada  
→ nada é enviado

---

## ✔️ Como corrigir AGORA

## 1\. Vá ao fluxo PRV

Vá até o node **Execute Workflow** onde você chama a sua “Voz Feminina”.

**Troque seus inputs para:**

```markdown
instance: {{ $json.INSTANCIA }}     → ou o campo real do seu fluxo PRV
phone: {{ $json.NUMERO_LEAD }}      → idem
mensagem_audio: {{ $json.MENSAGEM }}  → o texto que você quer falar
```

Pelo seu print do PRV, o correto é:

```markdown
instance: {{ $(Tratamento de Dados).item.json.INSTANCIA }}
phone: {{ $(Tratamento de Dados).item.json.NUMERO_LEAD }}
mensagem_audio: {{ $json.output }}     ← ESTE campo vem antes da TTS
```

**Verifique se o nome está certo**  
No PRV, muitas vezes você usa:

- `mensagem_brann`
- `mensagem_limpa`
- `resposta_llm`
- `text_final`

CONFIRA o nome exato do campo onde sai o texto final de resposta.

Se mandar errado, sempre vai chegar `null` no TTS.

---

## ✔️ 2. No node ElevenLabs (novo)

Seu print mostra:

```markdown
Text: {{ $json.mensagem_audio }}
```

Se esse campo chegar vazio, você vai ver:

```markdown
null
```

Faz essa correção preventiva:

```markdown
{{ $json.mensagem_audio || "..." }}
```

Exemplo:

```markdown
{{ $json.mensagem_audio || "Não recebi texto para gerar áudio." }}
```

---

## ✔️ 3. No node Evolution (Enviar Áudio)

O seu está assim:

```markdown
Áudio: {{ $binary.data.toString('base64') }}
```

Isso está **corretíssimo**.

Mas a Evolution API exige o BODY assim:

```markdown
"audio": "BASE64-AQUI"
```

Use:

- **Sem `data:audio/mpeg;base64,`**
- Apenas o base64 puro (Evolution monta tudo)

Ou seja, está **perfeito do jeito que fez**.

---

## 🧩 Checklist final — execute e veja

### No node “Entrada TTS” você deve ver:

```markdown
instance: PRV_Alimentos
phone: 55XXXXXXXX@s.whatsapp.net
mensagem_audio: "oi, tudo bem? Aqui vai sua resposta!"
```

Se isso não aparecer, **o erro está no PRV**, não no TTS.

### No node ElevenLabs você deve ver no output:

```markdown
Binary:
  data.mpeg (xx kb)
```

### No node Evolution:

```markdown
No error → áudio toca no WhatsApp
```

---

## 🧠 Diagnóstico preciso

**Se o TTS não recebe nada, o áudio nunca vai existir.  
Se o áudio não existe, o Evolution falha.**

Hoje:

- **Seu fluxo TTS está certo**
- **Seu ElevenLabs está certo**
- **Seu Evolution está certo**
- **O PRV está enviando os inputs ERRADOS ou vazios**

A correção é **na chamada do Execute Workflow no PRV**.

---

## Quer que eu analise o print exato do PRV para corrigir os campos?

Me mande o print do node **Execute Workflow** dentro do fluxo PRV que chama “VOZ FEMININA”.

Eu te digo exatamente o que trocar.

seg., 24 de nov. às 3:07

Perfeito, esse print entrega exatamente o problema.

No node **Generate speech from text (ElevenLabs)** aparece em vermelho:

> `Your request is invalid or could not be processed by the service (422)`

E logo acima do campo **Text**:

> `{{ $json.mensagem_audio }}`  
> `undefined`

Ou seja: você está mandando para a ElevenLabs:

```markdown
{
  "text": null
}
```

A API aceita só **string não vazia**, então responde 422.

---

## 1\. O que está errado exatamente

1. O node **Entrada TTS** na execução que você printou está assim:
	- `instance: PRV_Alimentos`
		- `phone: 5539...@s.whatsapp.net`
		- `mensagem_audio: [não aparece / null]`
2. O node **Generate speech from text** usa:
	```markdown
	Text: {{ $json.mensagem_audio }}
	```
3. Como `mensagem_audio` não existe nessa execução, o valor vira `undefined` e a ElevenLabs devolve 422.

Então:  
**O subworkflow está certo, quem está falhando é a chamada que não envia `mensagem_audio`.**

---

## 2\. Correção mínima pra ElevenLabs não quebrar

No node **Generate speech from text**, troca o campo **Text** para:

```markdown
{{ $json.mensagem_audio || "Teste de voz PRV – se você está ouvindo isso, o texto veio vazio." }}
```

Isso faz duas coisas:

- Se `mensagem_audio` vier preenchido → usa o texto real.
- Se vier vazio → manda uma string padrão (não dá 422).

Isso tira o erro imediato, mas ainda não resolve a causa raiz: o PRV precisa mandar o texto certo.

---

## 3\. Onde está a causa raiz: chamada do PRV → VOZ FEMININA

Vai no fluxo **PRV** no node **Execute Workflow** que chama “VOZ FEMININA”.

Na parte **Workflow Inputs**, você deve ter algo assim:

- `instance` → ok
- `phone` → ok
- `mensagem_audio` → provavelmente vazio ou nem está mapeado

Você precisa setar assim (ajusta os campos para os nomes reais do teu fluxo):

```markdown
instance:        {{ $('Tratamento de Dados').item.json.INSTANCIA }}
phone:           {{ $('Tratamento de Dados').item.json.NUMERO_LEAD }}
mensagem_audio:  {{ $('Text Final').item.json.text_final }}   // exemplo
```

O importante é:

- O terceiro campo **mensagem\_audio** precisa apontar para o **texto final da resposta do Brann/LLM**.
- No editor do n8n, clica no campo → ícone de expressão → navega no painel esquerdo até o node que contém o texto (ex: `Text Final`) e escolhe o campo certo.

Quando você fizer isso, na próxima execução do subworkflow, o node **Entrada TTS** deve mostrar:

```markdown
instance: PRV_Alimentos
phone: 5539...@s.whatsapp.net
mensagem_audio: "Aqui vai o texto que será falado em áudio..."
```

Se isso aparecer, a ElevenLabs vai gerar o áudio normalmente.

---

## 4\. Checklist rápido para você validar

1. No **PRV → Execute Workflow (VOZ FEMININA)**:
	- `mensagem_audio` está preenchido com o texto final (campo vindo do node certo).
2. No subworkflow **VOZ FEMININA**:
	- Em uma execução real, na aba **Schema** do node **Entrada TTS**, aparece `mensagem_audio` com texto.
		- No node ElevenLabs, o campo **Text** está:  
		`{{ $json.mensagem_audio || "Teste de voz PRV..." }}`  
		e no preview não aparece mais “undefined”.
3. Node **Evolution2**:
	- Continua com  
		`Audio: {{ $binary.data.toString('base64') }}`  
		(isso está correto).

Feito isso, o áudio deve começar a chegar no WhatsApp.