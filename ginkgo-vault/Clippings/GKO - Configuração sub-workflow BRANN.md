---
title: "GKO - Configuração sub-workflow BRANN"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69291b4c-2b6c-8329-be9a-ffb2fc898a2e"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 28 de nov. às 0:47

Perfeito. Vamos configurar esse **sub-workflow do BRANN** com precisão cirúrgica. Vou agir como *Arquiteto de Dados e Fluxos*, usar o PDF que você enviou como referência direta, e transformar isso no roteiro definitivo para deixar esse subfluxo **100% operacional, escalável e limpo**.

Abaixo: **diagnóstico do subworkflow**, **melhorias**, **checklist de configuração nó-a-nó**, **ordem recomendada**, **SQL e integrações**, tudo pronto para copy/cola.

---

## 1) VISÃO ESTRATÉGICA — COMO ESTE SUBFLUXO DEVE OPERAR PARA O BRANN

O sub-workflow da imagem é o **núcleo multimídia** do BRANN: ele pega o texto do usuário (captado no fluxo principal), gera **slides, apresentações, imagens, vídeos**, consulta Google Sheets e retorna **mídia final** para o cliente via WhatsApp.

Pense nisso como o “ **departamento de criação autônomo** ” do BRANN:  
gpt → prompt → Gamma → NanoBanana → VEED 3 → enviar mídia.

### Meta:

O subfluxo deve ser chamado **somente quando o out.type do BRANN for**:

- `"image"`
- `"video"`
- `"slides"`
- `"gamma"`
- `"creative_asset"`

Ou quando o BRANN emitir:

```markdown
{ "out": { "type": "creative", "mode": "slides|image|video", "prompt": "..."} }
```

Isso mantém o ciclo limpo, modular e sem risco de loops.

---

## 2) DIAGNÓSTICO DO WORKFLOW DA IMAGEM

Com base na imagem:

![https://www.hostinger.com/tutorials/wp-content/uploads/sites/2/2025/03/format_social_media_metrics-1024x497.png](https://www.hostinger.com/tutorials/wp-content/uploads/sites/2/2025/03/format_social_media_metrics-1024x497.png) ![https://n8n-automation.com/wp-content/uploads/2024/06/head-image.jpeg?w=1024](https://n8n-automation.com/wp-content/uploads/2024/06/head-image.jpeg?w=1024)

**Elementos identificados:**

1. **Entrada Executado por outro Workflow** ✔  
	— Correto: chamado pelo fluxo principal do BRANN.
2. **Tratamento de dados**  
	— Precisamos padronizar o input: `prompt`, `mode`, `phone`, `referenceImageUrl`.
3. **Visão (analisar imagem)**  
	— Serve para gerar prompt de referência.
4. **Google Sheets Read + Update**  
	— Está coletando parâmetros de vídeo e configurando geração de conteúdo.
5. **AI Agent (Master Prompt)**  
	— Gera o prompt final estruturado (slides, vídeo, imagem).
6. **Ramos paralelos:**
	- Rota 1 → Gamma → Slides → Enviar apresentação
		- Rota 2 → NanoBanana → Editar → Download → Enviar imagem
		- Rota 3 → VEED3 → Render → Download → Enviar vídeo

**Estado atual:**  
A arquitetura está **correta**.  
O que falta é **padronização**, **integração com o fluxo principal**, e **limpeza das entradas/saídas**.

---

## 3) COMO CONFIGURAR O SUBFLUXO — PASSO A PASSO CIRÚRGICO

## PASSO 0 — DEFINIR FORMATO DE ENTRADA

O seu subfluxo deve aceitar exatamente este JSON como entrada:

```markdown
{
  "mode": "slides|image|video",
  "prompt": "Texto-base do cliente",
  "phone": "5511XXXXXXXXX",
  "referenceImageUrl": null
}
```

No início do workflow → adicione um **Set** chamado **Normalize Input**:

```markdown
= $json.mode
= $json.prompt
= $json.phone
= $json.referenceImageUrl
```

---

## PASSO 1 — TRATAMENTO DE DADOS

Nó “Tratamento de Dados” deve virar:

```markdown
return [{
  json: {
    mode: $json.mode ?? "slides",
    prompt: $json.prompt ?? "",
    phone: $json.phone ?? "",
    referenceImageUrl: $json.referenceImageUrl ?? ""
  }
}];
```

---

## PASSO 2 — RAMIFICAÇÃO INTELIGENTE POR MODE

Logo após esse Set → coloque um **Switch**:

**Expression**:

```markdown
{{$json.mode}}
```

**Cases:**

- slides
- image
- video

Saídas:  
0 = slides  
1 = image  
2 = video

---

## 4) CONFIGURAÇÃO DE CADA RAMO

---

## RAMO 1 — SLIDES (Gamma)

## Node: “Generate Slides Prompt”

Use **GPT-4o mini**:

**System:**

```markdown
Você é um gerador de apresentações Gamma.  
Crie um prompt estruturado e persuasivo, em PT-BR, com tópicos claros e storyboard.
Retorne apenas o texto final.  
Nada fora disso.
```

**User:**

```markdown
{{$json.prompt}}
```

## Node: Gamma API

POST: `https://api.gamma.app/v1/...`  
Headers:

- Authorization: Bearer {{env.GAMMA\_KEY}}

Body:

```markdown
{
  "prompt": "={{$json['Generate Slides Prompt'].text}}"
}
```

## Node: Enviar apresentação

Use Evolution API:

POST → `/message/sendFile`

Body:

```markdown
{
  "number": "={{$json.phone}}",
  "mediaData": { "url": "={{$json.gammaFileUrl}}" },
  "caption": "Aqui está sua apresentação!"
}
```

---

## RAMO 2 — IMAGEM (NanoBanana)

## Node: “Generate Image Prompt”

Use GPT-4o mini:

```markdown
{
 "role": "system",
 "content": "Crie um prompt hiper descritivo, cinematográfico, para gerar uma imagem de alta qualidade."
}
```

User:

```markdown
{{$json.prompt}}
```

## Node: NanoBanana Create

POST:

```markdown
https://api.nanobanana.com/v1/image
```

Body:

```markdown
{
 "prompt": "={{$json['Generate Image Prompt'].text}}",
 "size": "1080x1920"
}
```

## Node: Wait

3–5 segundos.

## Node: Download Edited Image

GET para a URL retornada.

## Node: Enviar Imagem

Evolution API:

```markdown
{
  "number": "={{$json.phone}}",
  "mediaData": {
    "url": "={{$json.imageUrl}}",
    "caption": "Sua imagem está pronta!"
  }
}
```

---

## RAMO 3 — VÍDEO (VEED 3)

## Node: “AI Agent Generate Video Prompt”

System:

```markdown
Crie um prompt completo para um vídeo curto vertical (15–30s), com estética futurista Ginkgo.
Inclua:
- tema
- narrador
- transições
- plano a plano
Retorne apenas o texto final.
```

User:

```markdown
{{$json.prompt}}
```

## Node: Format Prompt

Formate assim:

```markdown
return [{
  json: {
    script: $json.text,
    style: "futuristic blue / neon / cyberpunk light",
    length: "15-30 seconds"
  }
}];
```

## Node: Generate Video with VEED3

POST:

```markdown
https://api.veo3.ai/video/create
```

## Node: Wait

Até 20–40s dependendo do tamanho.

## Node: Download Video

GET → URL do render final.

## Node: Enviar Vídeo

```markdown
{
  "number": "={{$json.phone}}",
  "mediaData": {
    "url": "={{$json.videoUrl}}"
  }
}
```

---

## 5) SAÍDA PARA O WORKFLOW PRINCIPAL

No final de cada ramo, insira um **Set**:

Slides:

```markdown
{ "ok": true, "type": "slides" }
```

Imagem:

```markdown
{ "ok": true, "type": "image" }
```

Vídeo:

```markdown
{ "ok": true, "type": "video" }
```

---

## 6) COMO O BRANN CHAMA ESSE SUBFLUXO

No Parser final do BRANN:

Se ele retornar:

```markdown
{ "out": { "type": "creative", "mode": "slides", "prompt": "..." } }
```

Você aciona:

**Execute Workflow → Subfluxo Brann Creative**

Params:

- mode = `{{$json.out.mode}}`
- prompt = `{{$json.out.prompt}}`
- phone = `{{$json.phone}}`
- referenceImageUrl (opcional)

---

## 7) CHECKLIST FINAL (copy/cola)

### Geral

- Entradas normalizadas com Set.
- Switch por mode: slides / image / video.
- Todos os ramos enviam a mídia direto via Evolution.
- Usar apenas GPT-4o mini (barato e eficaz).
- Todos os serviços externos com keys via ENV.
- Nenhum texto é enviado sem JSON ao fluxo principal.

### Slides

- Prompt estruturado.
- Gamma API configurada.
- Envio via Evolution.

### Imagem

- NanoBanana integrado.
- Download + envio funcionando.

### Vídeo

- Prompt cinematográfico.
- VEED3 configurado.
- Wait configurado corretamente.

### Segurança

- Sem dados sensíveis nos logs.
- Env vars ativadas: GAMMA\_KEY, NANOBANANA\_KEY, VEO3\_KEY.

---

Se quiser, eu também monto **o JSON completo de importação** desse subfluxo já padronizado, com todos os nós nomeados e funcionais.

Só pedir: **“mande o JSON de importação do subfluxo creative do BRANN”**.