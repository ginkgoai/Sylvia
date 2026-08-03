---
title: "GKO - Respostas curtas e áudio"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69a83713-a660-8330-a583-be80b4765781"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
qua., 4 de mar. às 10:43

![95412df3-1fa1-43d4-a8d3-c3afb0496162.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000003d9471f5a3b52f5ddc95abca&ts=495692&p=fs&cid=1&sig=6f88c365022e9890654ae8b1192e6e1153ebc8d1c7c2a7c9768f381f6c8f1aa8&v=0)

Brann (21).json

Arquivo

como podemos deixar as respostas mais curtas e humanas, e quando for resposta longa ser audio e naturalmente sem ter q pedir audio

O que está acontecendo na sua conversa é um **problema clássico de UX de agente conversacional**:  
o modelo responde como “chat de texto padrão”, não como **assistente humano no WhatsApp**.

Você precisa ajustar **3 camadas do fluxo**:

1. **Prompt / estilo de resposta**
2. **Lógica de tamanho da resposta**
3. **Fallback automático para áudio**

Vou te mostrar a arquitetura usada em bots de vendas bons.

---

## 1️⃣ Primeiro: limitar o tamanho das respostas (prompt)

No prompt do **Brann**, adicione uma regra clara:

```markdown
REGRAS DE RESPOSTA

1. Sempre responda de forma curta e natural.
2. Use no máximo 2 frases quando responder por texto.
3. Evite listas longas ou explicações extensas.
4. Fale como um humano no WhatsApp.
5. Se a resposta exigir explicação maior que 2 frases, responda com áudio.
```

E um exemplo dentro do prompt:

```markdown
EXEMPLO

Pergunta: Como funciona automação para vendas?

Resposta curta:
"A automação cuida da prospecção e do atendimento inicial automaticamente. Assim você recebe leads mais qualificados e foca só na venda."

Resposta longa → usar áudio.
```

---

## 2️⃣ Criar uma regra automática para áudio

No **n8n** você consegue detectar quando a resposta é grande.

### Node: Function

```markdown
const text = $json.response;

if (text.length > 280) {
  return [{audio: true, text}];
}

return [{audio: false, text}];
```

Regra simples:

| Tamanho | Ação |
| --- | --- |
| < 280 caracteres | texto |

> 280 caracteres | áudio |

---

## 3️⃣ Gerar áudio automaticamente

Fluxo:

```markdown
LLM
 ↓
Function (verifica tamanho)
 ↓
IF
 ├ texto → WhatsApp
 └ áudio → ElevenLabs → WhatsApp
```

---

## 4️⃣ Node ElevenLabs (TTS)

Request:

```markdown
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}
```

Body:

```markdown
{
 "text": "{{ $json.text }}",
 "model_id": "eleven_multilingual_v2"
}
```

Depois envia o **MP3 para WhatsApp**.

---

## 5️⃣ Resultado final da experiência

Cliente pergunta algo.

### Pergunta simples

Cliente:

> "Vocês fazem automação para consórcio?"

Resposta:

> "Sim! Automatizamos a prospecção de leads e o atendimento inicial no WhatsApp."

---

### Pergunta mais complexa

Cliente:

> "Como funciona a captação e qualificação dos leads?"

Resposta:

🎤 **áudio automático**

Sem pedir.

---

## 6️⃣ Truque que deixa MUITO mais humano

Antes do áudio, enviar uma frase curta:

```markdown
Boa pergunta — vou te explicar rapidinho em áudio 👇
```

Depois envia o áudio.

Parece **100% humano**.

---

## 7️⃣ Outra melhoria importante

Seu Brann está **explicando demais**.

No WhatsApp venda funciona assim:

```markdown
Confirmação
↓
Resposta curta
↓
Pergunta de continuidade
```

Exemplo:

```markdown
Boa pergunta.

Automação consegue captar leads e responder eles instantaneamente no WhatsApp.

Hoje você já roda tráfego ou ainda está só no orgânico?
```

Sempre puxa conversa.

---

## 8️⃣ Prompt ideal do Brann (versão melhor)

Adicione isso:

```markdown
FORMATO DAS RESPOSTAS

Sempre responder em 3 etapas:

1. Confirmação curta
2. Explicação simples (1 ou 2 frases)
3. Pergunta que mantém a conversa

Se precisar explicar algo mais longo, responda em áudio automaticamente.
```

---

## 9️⃣ Resultado esperado

Antes:

❌ texto gigante  
❌ robótico  
❌ cara de IA

Depois:

✔ curto  
✔ natural  
✔ áudio quando precisa  
✔ parece humano

---

## 🔥 Se quiser, posso te passar também

- **Fluxo n8n completo do Brann (versão PRO)**
- **Sistema de decisão texto vs áudio**
- **Áudio com voz realista**
- **Typing delay humano**
- **Mensagens quebradas estilo humano**

Isso deixa o bot **10x mais natural no WhatsApp.**