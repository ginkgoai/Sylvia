---
title: "GKO - Criar LLM no VS Code"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68f6ffe2-8ca4-8330-9c38-9d9ce98c3f01"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
Bora montar teu “atendente-LLM” dentro do VS Code, já plugado no WhatsApp via Evolution API e com voz humana via KOKORO? Vou te dar o mapa completo: arquitetura, pastas, variáveis, e um “starter kit” em TypeScript que você só cola, instala e roda. Zero firula, foco em conversa que vende e manda áudio bonito.

---

## Visão de arquitetura (🤝 WhatsApp + 🧠 LLM + 🗣️ KOKORO)

```markdown
[Cliente no WhatsApp]
        │  (Webhook do Evolution API)
        ▼
[Seu servidor Node/TS no VS Code]
  ├─ Ingestão (valida evento, deduplica, extrai texto/áudio)
  ├─ Orquestrador de diálogo (policy, contexto do negócio)
  ├─ LLM (OpenAI/Ollama/etc) + Ferramentas (ex.: CRM, FAQ, RAG)
  ├─ TTS KOKORO (gera voz humana a partir da resposta)
  └─ Entrega via Evolution API (texto + áudio)
        ▲
        └── Logs, métricas, memória curta/longa (SQLite/Redis)
```

Princípio zen: 1) recebe → 2) decide → 3) responde → 4) fala.

---

## Stack sugerida

- **Node + TypeScript** (rápido de iterar no VS Code).
- **Express** para webhook.
- **LLM provider** a sua escolha (OpenAI, local **Ollama**, etc.) — o código já vem desacoplado.
- **KOKORO** para TTS (endpoint HTTP).
- **Evolution API** para WhatsApp (webhook + envio).
- **SQLite (Prisma)** para memória curta (historinha recente) e logs. Depois você pluga um RAG.

---

## Estrutura de pastas (cola no terminal)

```markdown
mkdir -p ginkgo-whats-llm/{src/{adapters,core,providers,utils},logs} && \
cd ginkgo-whats-llm && \
npm init -y && npm i express axios dotenv zod && \
npm i -D typescript ts-node-dev @types/node @types/express
npx tsc --init
```

Pastas:

- `src/adapters/` integrações (evolution, kokoro, llm).
- `src/core/` orquestração de diálogo, memória e políticas.
- `src/providers/` wrappers por provedor (ex.: `openai.ts`, `ollama.ts`).
- `src/utils/` helpers (validadores, logger simples).

---

## .env modelo (cola e preenche)

```markdown
PORT=3000
PUBLIC_URL=http://localhost:3000   # se usar ngrok, troque aqui

# Evolution API
EVOLUTION_API_BASE=https://SEU_HOST_DA_EVOLUTION/api
EVOLUTION_API_INSTANCE=inst_XXXX
EVOLUTION_API_TOKEN=EVO_TOKEN

# KOKORO TTS
KOKORO_BASE_URL=https://SEU_HOST_DO_KOKORO/tts
KOKORO_API_KEY=KOKORO_KEY
KOKORO_VOICE=br_female_01      # exemplo; troque pelo voice id disponível
KOKORO_FORMAT=mp3              # mp3/wav

# LLM (exemplos; use só um)
OPENAI_API_KEY=sk-xxxx
LLM_MODEL=gpt-4o-mini          # ou o que preferir
# Para Ollama local:
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1:8b
```

---

## package.json – scripts úteis

```markdown
{
  "scripts": {
    "dev": "ts-node-dev --respawn --transpile-only src/index.ts",
    "start": "node dist/index.js",
    "build": "tsc"
  }
}
```

---

## Código base (copy-paste)

## src/index.ts

```markdown
import "dotenv/config";
import express from "express";
import { json } from "express";
import { z } from "zod";
import { handleIncomingMessage } from "./core/router";

const app = express();
app.use(json({ limit: "10mb" }));

// Evol webhook: ajuste o path conforme sua config
app.post("/webhook/evolution", async (req, res) => {
  try {
    // A Evolution geralmente manda um payload com infos da mensagem.
    // Como formatos variam, tratamos genericamente:
    const body = req.body ?? {};
    // Exemplo de normalização mínima:
    const schema = z.object({
      event: z.string().optional(),
      message: z.object({
        from: z.string(),
        chatId: z.string().optional(),
        text: z.string().optional(),
        type: z.string().optional(),   // "chat" | "ptt" | ...
        id: z.string().optional()
      }).passthrough().optional()
    }).passthrough();

    const parsed = schema.safeParse(body);
    if (!parsed.success) {
      console.error("Webhook inválido:", parsed.error);
      return res.status(400).send("bad payload");
    }

    const msg = parsed.data.message;
    if (!msg) return res.status(200).send("no message");

    // Extrai o texto (se voz, você pode transcrever numa etapa futura)
    const text = msg.text ?? "";
    const from = msg.chatId ?? msg.from;

    // Orquestra a conversa
    await handleIncomingMessage({ from, text, raw: body });

    res.status(200).send("ok");
  } catch (err) {
    console.error(err);
    res.status(500).send("error");
  }
});

const port = Number(process.env.PORT || 3000);
app.listen(port, () => {
  console.log(\`Server on http://localhost:${port}\`);
});
```

## src/core/router.ts

```markdown
import { llmGenerate } from "../providers/llm";
import { sendText, sendAudioFromBuffer } from "../adapters/evolution";
import { synthesize } from "../adapters/kokoro";

type InMsg = {
  from: string;
  text: string;
  raw: any;
};

const BUSINESS_SYSTEM_PROMPT = \`
Você é o BRANN, atendente de vendas carismático da Ginkgo. 
Objetivo: entender o pedido, qualificar, oferecer ajuda com clareza e CTA. 
Estilo: sábio, consultivo, simpático, direto, sem rodeios, PT-PT com "ora pois" quando convier.
Responda curto, mas completo, e proponha um próximo passo prático.
\`;

export async function handleIncomingMessage(msg: InMsg) {
  const userText = (msg.text || "").trim();

  // Regras simples (ex.: saudações/FAQ curto)
  if (!userText) {
    await sendText(msg.from, "Manda a tua dúvida ✍️");
    return;
  }

  // Contexto mínimo do negócio (placeholder; substitua por empresa/planos reais)
  const businessContext = \`
Empresa: Ginkgo AI Systems.
Produto: Automação com IA (Brann, Nyra, Alphie).
Canais: WhatsApp, Instagram, Site.
Planos: Básico, Avançado, Futurista (valores sob consulta).
\`;

  const prompt = [
    { role: "system", content: BUSINESS_SYSTEM_PROMPT },
    { role: "user", content: \`Contexto de negócio:\n${businessContext}\n---\nMensagem do cliente: "${userText}"\` }
  ];

  // Gera resposta textual
  const reply = await llmGenerate(prompt);

  // Manda texto
  await sendText(msg.from, reply);

  // Gera áudio com KOKORO
  try {
    const audio = await synthesize(reply);
    await sendAudioFromBuffer(msg.from, audio, {
      filename: "resposta.mp3",
      mime: "audio/mpeg"
    });
  } catch (e) {
    // fallback silencioso se TTS falhar
    console.warn("Falha no TTS:", e);
  }
}
```

## src/providers/llm.ts

```markdown
import axios from "axios";

type Msg = { role: "system"|"user"|"assistant"; content: string };

const useOpenAI = !!process.env.OPENAI_API_KEY;

export async function llmGenerate(messages: Msg[]): Promise<string> {
  if (useOpenAI) return openai(messages);
  return ollama(messages);
}

async function openai(messages: Msg[]): Promise<string> {
  const apiKey = process.env.OPENAI_API_KEY!;
  const model = process.env.LLM_MODEL || "gpt-4o-mini";
  const res = await axios.post(
    "https://api.openai.com/v1/chat/completions",
    { model, messages, temperature: 0.4 },
    { headers: { Authorization: \`Bearer ${apiKey}\` } }
  );
  return res.data.choices?.[0]?.message?.content?.trim() || "Deu branco por aqui 😅";
}

async function ollama(messages: Msg[]): Promise<string> {
  const base = process.env.OLLAMA_BASE_URL || "http://localhost:11434";
  const model = process.env.OLLAMA_MODEL || "llama3.1";
  const prompt = messages.map(m => \`${m.role.toUpperCase()}: ${m.content}\`).join("\n\n");
  const res = await axios.post(\`${base}/api/generate\`, { model, prompt, stream: false });
  return (res.data?.response || "").trim() || "Deu branco por aqui 😅";
}
```

## src/adapters/kokoro.ts

```markdown
import axios from "axios";

export async function synthesize(text: string): Promise<Buffer> {
  const base = process.env.KOKORO_BASE_URL!;
  const apiKey = process.env.KOKORO_API_KEY!;
  const voice = process.env.KOKORO_VOICE || "br_female_01";
  const format = process.env.KOKORO_FORMAT || "mp3";

  const res = await axios.post(
    \`${base}\`,
    { text, voice, format },
    { headers: { Authorization: \`Bearer ${apiKey}\` }, responseType: "arraybuffer" }
  );
  return Buffer.from(res.data);
}
```

## src/adapters/evolution.ts

```markdown
import axios from "axios";
import FormData from "form-data";

const base = process.env.EVOLUTION_API_BASE!;
const instance = process.env.EVOLUTION_API_INSTANCE!;
const token = process.env.EVOLUTION_API_TOKEN!;

function authHeaders() {
  return { Authorization: \`Bearer ${token}\` };
}

export async function sendText(chatId: string, text: string) {
  // Ajuste o endpoint/conteúdo conforme sua versão da Evolution API
  await axios.post(
    \`${base}/message/sendText/${instance}\`,
    { chatId, text },
    { headers: authHeaders() }
  );
}

export async function sendAudioFromBuffer(chatId: string, audio: Buffer, opts: { filename: string; mime: string }) {
  // Algumas versões precisam de upload + referência; outras aceitam multipart direto.
  // Exemplo genérico com multipart:
  const form = new FormData();
  form.append("chatId", chatId);
  form.append("audio", audio, { filename: opts.filename, contentType: opts.mime });

  await axios.post(
    \`${base}/message/sendAudio/${instance}\`,
    form,
    { headers: { ...authHeaders(), ...form.getHeaders() } }
  );
}
```

> **Atenção**: Endpoints/nome de campos da Evolution podem variar por versão. O código acima é um **esqueleto genérico**: se teu endpoint for diferente (ex.: `send-voice`, `sendFile`, `phone` em vez de `chatId`), só ajusta a função `sendText/sendAudioFromBuffer` mantendo a interface do resto intacta.

---

## Como rodar local

1. **Instalação**
```markdown
npm install
npm run dev
```
2. **Expor webhook** (para a Evolution chamar seu servidor local)
- Usa `ngrok`:
	```markdown
	ngrok http 3000
	```
- Copia a URL pública e coloca em `PUBLIC_URL` e na config da Evolution no endpoint de webhook:  
	`POST {PUBLIC_URL}/webhook/evolution`
3. **Testar manualmente** (simular mensagem):
```markdown
curl -X POST http://localhost:3000/webhook/evolution \
  -H "Content-Type: application/json" \
  -d '{
    "message": { "from":"5544999999999@c.us", "chatId":"5544999999999@c.us", "text":"Olá, o que vocês fazem?" }
  }'
```

Se tudo ok:

- Você verá log no terminal,
- A API vai tentar responder no chatId via Evolution (se o token/instância estiverem válidos),
- E vai tentar mandar o **áudio** gerado pelo KOKORO.

---

## Boas práticas de conversa (para deixar “com cara de gente”)

- **Typing indicator & delay humano**: simule leve atraso antes do áudio.
- **Memória curta** (últimas 10-20 mensagens por chatId) — guarde em SQLite com `chatId`, `role`, `content`, `timestamp`.
- **Políticas claras**: defina “o que pode” (preços, prazos, agendamento) e “o que escala” (passa pro humano).
- **Fallbacks**: se TTS cair, manda só texto; se LLM cair, template de emergência (“Tive um soluço técnico, posso te ligar?”).

---

## Como evoluir (sem trocadilhos com Evolution 😅)

- **RAG leve**: pastas de PDFs/políticas → índice local (ex.: LiteLLM + Chroma) e um tool de “buscar resposta”.
- **Ferramentas (tools)**: CRM (consultar lead), Agenda (propor horário), Geração de proposta (PDF) — expõe tudo como funções chamadas pelo LLM.
- **Transcrição**: quando receber áudio do cliente, transcreve (pode ser Whisper local/serviço) e segue o mesmo fluxo.
- **Analytics**: loga intenção, etapa do funil, taxa de áudio vs texto, tempo de resposta.
- **Multicanal**: mesma engine atende Instagram/Website mudando só o adaptador.

---

## Segurança & confiabilidade

- **Verificação de assinatura** do webhook (se disponível) + **idempotência** por `message.id` (não responda duas vezes).
- **Rate limit** por `chatId`.
- **Sanitização** de saída (nada de links maliciosos) e **mascaramento** de dados sensíveis nos logs.
- **Observabilidade**: request IDs, logs estruturados, alertas se TTS/LLM falhar.

---

## TL;DR do passo a passo

1. Cria projeto Node/TS no VS Code e sobe o Express.
2. Configura webhook da Evolution para bater em `/webhook/evolution`.
3. Orquestra mensagem → LLM → texto.
4. Passa texto no KOKORO → recebe `mp3`.
5. Envia texto + áudio de volta via Evolution.
6. Adiciona memória curta, RAG, e tools de negócio.
7. Upa logs/métricas e coloca em produção (Docker + reverse proxy + HTTPS).

Se quiser, na sequência a gente pluga **memória com SQLite/Prisma** e um **tool de “agendar no Trello/Google Calendar”**, deixando o Brann pronto para vender e confirmar horários no automático.

Certo, qual a diferença de ser feito assim e pelo n8n?

Boa! Dá pra pensar assim: **VS Code (Node/TS)** é “forjar a espada sob medida”; **n8n** é “montar Lego turbo”. Os dois fazem um bot vender e falar no WhatsApp, mas com **trade-offs** bem diferentes.

## Comparativo direto

## 1) Velocidade de construir

- **n8n:** prototipa em minutos. No-code/low-code, nós prontos (HTTP, Webhook, Trello, GSheets…). Perfeito pra provar valor logo.
- **VS Code (Node/TS):** leva mais tempo no começo, mas você molda tudo do seu jeito (rotas, middlewares, testes). Bom pra produto sério/long-lasting.

## 2) Flexibilidade e controle

- **n8n:** excelente pra orquestração de passos e integrações simples. Lógica complexa fica “esticada” no canvas, difícil de versionar diffs.
- **VS Code:** você manda em tudo (estado, fila, cache, patterns, libs). Ideal pra **policy de diálogo**, **ferramentas do LLM**, **memória** e **RAG** mais elaborados.

## 3) Latência e performance

- **n8n:** cada nó = overhead; pouca granularidade de otimização. Em áudio TTS + chamadas LLM + upload, pode dar **lag** perceptível.
- **VS Code:** dá pra usar streaming, conexões keep-alive, filas (BullMQ), cache, e otimizar timeout/retentativa por chamada. **Resposta mais “snappy”**.

## 4) Observabilidade e testes

- **n8n:** logs por execução são ok, mas debug fino e **testes automatizados** são limitados.
- **VS Code:** testes unitários/e2e, tracing (OpenTelemetry), logs estruturados, feature flags, etc. Vida feliz pra CI/CD.

## 5) Versionamento e time

- **n8n:** versões de workflow, mas comparar mudanças visuais é sofrido. Merge em equipe é chato.
- **VS Code:** Git flui. Code review, branches, PRs, linters, tudo redondinho.

## 6) Segurança e compliance

- **n8n:** credenciais guardadas na plataforma; RBAC depende da tua instalação. Difícil aplicar políticas finas de dados sensíveis.
- **VS Code:** controle total: criptografia, mascaramento de logs, assinatura de webhooks, validações por schema, etc.

## 7) Confiabilidade e recuperação

- **n8n:** tem retries, mas filas/Dead-letter são mais limitadas.
- **VS Code:** você escolhe a stack (Redis + BullMQ, SQS, Kafka…), **idempotência** por message.id, e playbook de reprocessamento.

## 8) Custos

- **n8n:** barato pra começar; escala pode encarecer pelo overhead e “sprawl” de workflows.
- **VS Code:** investimento maior inicial, porém **custo unitário menor** e previsível a longo prazo.

---

## O que fica melhor em cada um?

**Brilha no n8n**

- Webhooks simples da Evolution API → repassar evento.
- ETL leve (capturar dados, jogar no Notion/Trello/GSheets/CRM).
- Rotinas de backoffice (reengajar lead D+1, cobrar assinatura, gerar lembretes).
- “Puxar/empurrar” arquivos (PDF, imagem, nota fiscal) sem lógica pesada.

**Brilha no VS Code**

- **Cérebro conversacional**: policy do Brann, ferramentas do LLM (buscar no CRM, consultar estoque, criar proposta), **memória curta/longa**, **RAG** com embeddings.
- **Áudio**: pipeline de TTS (KOKORO), transcrição, normalização, stream/concatenação.
- **Baixa latência**, controle de erros, timeouts, batching, streaming de resposta.
- **Integrações críticas** com controle fino (assinatura de webhook, autenticação forte).

---

## Modelo híbrido (o “melhor dos dois mundos”)

**Fluxo recomendado pra tua stack (Evolution API + KOKORO):**

1. **Evolution API Webhook** → chega no **VS Code**
	- Valida, deduplica `message.id`, grava no log/SQLite, detecta tipo (texto/áudio/documento).
2. **Orquestrador (VS Code)**
	- Aplica **policy** e chama o **LLM** (com ferramentas e RAG).
		- Se a resposta exigir tarefas de negócio (criar lead no Pipedrive, abrir card no Trello, mandar e-mail),  
		publica um evento numa **fila** (ex.: Redis/BullMQ) com `type: "CRM_CREATE_LEAD"`.
3. **n8n como “músculo operacional”**
	- Escuta a fila/webhook de eventos internos (ou endpoint privado).
		- Executa as automações: Trello, Notion, Planilha, ERP, assinatura/Pagamento, etc.
		- Retorna um “ACK”/status que o VS Code pode consultar (ou o n8n notifica de volta).
4. **Resposta ao usuário (VS Code)**
	- Envia **texto** via Evolution.
		- Gera **áudio** no KOKORO → envia `mp3` via Evolution.
		- Se falhar TTS, fallback pra texto.

**Divisão mental:**

- **VS Code = cérebro em tempo real** (diálogo, TTS, RAG, segurança, performance).
- **n8n = esteira de tarefas** (integrações, ETL, rotina, pós-atendimento, relatórios).

---

## Quando escolher 100% n8n?

- **MVP ultra-rápido**, sem “cérebro” complexo; responder prompts fixos, FAQs, puxar dados básicos e mandar áudio pronto.
- Time sem dev dedicado e com urgência de botar no ar **hoje**.

## Quando escolher 100% VS Code?

- Você quer **produto**: baixo tempo de resposta, experiências de voz “premium”, ferramentas de LLM, testes, escalabilidade e roadmap longo (apps, site, Insta, multitenant, billing, etc.).

---

## Checklists práticos

**Se for híbrido agora:**

- Webhook Evolution apontando pro VS Code (`/webhook/evolution`).
- VS Code com: validação Zod, idempotência, memória curta SQLite, providers (LLM/KOKORO/Evolution).
- Fila (Redis) + conector HTTP no n8n para consumir eventos internos (ou n8n com Webhook privado autenticado).
- Nós do n8n para: Trello/Notion/CRM/GSheets + retries + alertas no Telegram/Slack.
- Observabilidade: logs estruturados + dashboard mínimo (falhas LLM/TTS, tempo médio de resposta).

**Se for full n8n (temporário):**

- Webhook Evolution → Nó “IF” por tipo de mensagem.
- Nó HTTP p/ provedor LLM + manipulação de strings.
- KOKORO via HTTP Request → upload do `mp3` de volta pela Evolution.
- Rotinas de follow-up (Wait → Send) + erro → enviar alerta.

---

## Resumo honesto

- **n8n** é imbatível pra **colar integrações** e automatizar backoffice.
- **VS Code** é imbatível pra **conversa inteligente em tempo real** com voz e memória, mantendo **qualidade, testes e escalabilidade**.
- O **híbrido** te dá entrega rápida agora e base sólida pro crescimento.

Curto transformar isso em blueprint de deploy (Docker + EasyPanel) com Redis/BullMQ, um worker no n8n e o app Node orquestrando a conversa em milissegundos. Quer que eu te entregue o `docker-compose.yml` e os nós-base do n8n já prontos pra colar?

Perfeito. Vamos de **“n8n-first”** e deixar o **VS Code** só com o mínimo vital pra controle/backup. Abaixo vai um blueprint copiável: fluxo no n8n (nós, payloads, credenciais), mais um microserviço levinho em Node/TS só pra **log/backup** (e futuro controle).

---

## Arquitetura enxuta (n8n no volante)

**Entrada** (Evolution → Webhook n8n)  
**Roteiro** (n8n decide se é texto/áudio, chama LLM e TTS)  
**Resposta** (n8n → Evolution: texto + voz KOKORO)  
**Backup/controle** (n8n → microserviço VS Code: guarda tudo)

```markdown
Evolution Webhook
      │
      ▼
   n8n (Webhook)
      ├─ Normalizar evento + deduplicar (Data Store)
      ├─ Se texto:
      │    ├─ LLM (HTTP → OpenAI/Ollama/etc.)
      │    ├─ TTS (HTTP → KOKORO)
      │    └─ Enviar texto + áudio (HTTP → Evolution)
      ├─ Se áudio:
      │    ├─ Baixar mídia
      │    ├─ Transcrever (HTTP → Whisper/OpenAI)
      │    └─ Mesma trilha de cima (LLM → TTS → enviar)
      └─ Log/backup (HTTP → microserviço VS Code /ingest)
```

---

## Variáveis/credenciais (centralize no n8n)

Crie **Credenciais HTTP** no n8n para:

- **Evolution API**
	- Base URL: `https://SEU_HOST_DA_EVOLUTION/api`
		- Headers: `Authorization: Bearer <EVO_TOKEN>`
		- Param fixo (se precisar): `instance = inst_XXXX`
- **OpenAI (ou outro LLM)**
	- Base URL: `https://api.openai.com/v1`
		- Header: `Authorization: Bearer {{ $env.OPENAI_API_KEY }}`
- **KOKORO**
	- Base URL: `https://SEU_HOST_DO_KOKORO`
		- Header: `Authorization: Bearer {{ $env.KOKORO_API_KEY }}`
- **Microserviço de backup (VS Code)**
	- Base URL: `http://log-sink:3001` (ou `http://localhost:3001` em dev)

No n8n, vá em **Settings → Environment variables** e adicione:

```markdown
OPENAI_API_KEY=sk-xxxx
LLM_MODEL=gpt-4o-mini
KOKORO_VOICE=br_female_01
KOKORO_FORMAT=mp3
```

---

## Workflow principal no n8n (nós essenciais)

### 1) Webhook (Trigger)

- **Method**: POST
- **Path**: `/evolution/inbound`
- **Response**: 200 com `{ ok: true }` depois que a execução enfileirar.

> Dica: copie o **Production URL** do n8n e cole na Evolution como webhook.

### 2) Function (Normalizar + extrair campos)

Código (cole no **Function**):

```markdown
const body = $json;
const message = body.message || body.data || body; // acomodar variações
const from = message.chatId || message.from || message.phone || "";
const text = message.text || message.body || "";
const type = message.type || (message.audio ? "ptt" : "chat");
const id = message.id || message.key?.id || \`${from}-${Date.now()}\`;

return [
  {
    json: {
      raw: body,
      id,
      from,
      type,
      text,
      mediaUrl: message.mediaUrl || message.audio?.url || null
    }
  }
];
```

### 3) Data Store (Deduplicar por id)

- Crie um **Data Store** chamado `processed_messages` com campo `id` (string).
- Nó **Data Store → Get Many** buscando `id`.
- **IF**: se já existe, **encerrar** (evita responder duas vezes).

### 4) Roteamento por tipo (IF)

- IF `{{$json["type"]}} equals "chat"` → fluxo TEXTO
- ELSE IF `{{$json["type"]}} equals "ptt"` → fluxo ÁUDIO
- ELSE: opcional mandar “tipo não suportado”.

---

## Fluxo TEXTO

### 5) Prepare Prompt (Function)

```markdown
const BUSINESS_SYSTEM = \`
Você é o BRANN, vendedor consultivo da Ginkgo.
Fale curto e assertivo, PT-PT quando convier ("ora pois").
1) confirmar entendimento
2) 2–3 bullets práticos
3) CTA único
\`;

const context = \`
Empresa: Ginkgo AI Systems
Produto: automações com IA (Brann, Nyra, Alphie)
Planos: Básico, Avançado, Futurista
\`;

return [{
  json: {
    messages: [
      { role: "system", content: BUSINESS_SYSTEM },
      { role: "user", content: \`Contexto:\n${context}\n---\nCliente: ${$json.text}\` }
    ]
  }
}];
```

### 6) LLM (HTTP Request → OpenAI Chat Completions)

- **Method**: POST
- **URL**: `=/chat/completions` (usando credencial base `https://api.openai.com/v1`)
- **Body (JSON)**:
```markdown
{
  "model": "={{$env.LLM_MODEL}}",
  "temperature": 0.4,
  "messages": "={{$json.messages}}"
}
```
- **Response**: `{{$json["choices"][0]["message"]["content"]}}` → guarde em `replyText`.

### 7) TTS (HTTP Request → KOKORO)

- **Method**: POST
- **URL**: `/tts` (base do KOKORO)
- **Body (JSON)**:
```markdown
{
  "text": "={{$json.replyText || $items('LLM')[0].json.choices[0].message.content}}",
  "voice": "={{$env.KOKORO_VOICE}}",
  "format": "={{$env.KOKORO_FORMAT}}"
}
```
- **Response**: Binário (`Response Format: File`) → **Binary Property**: `audio`.

### 8) Enviar TEXTO (HTTP → Evolution)

- **Method**: POST
- **URL**: `/message/sendText/{{inst}}` (ajuste conforme sua Evolution)
- **Body**:
```markdown
{
  "chatId": "={{$items(0).json.from}}",
  "text": "={{$json.replyText || $items('LLM')[0].json.choices[0].message.content}}"
}
```

### 9) Enviar ÁUDIO (HTTP → Evolution, multipart)

- **Method**: POST
- **URL**: `/message/sendAudio/{{inst}}`
- **Send Binary**: ✅
- **Binary Property**: `audio`
- **Additional Fields**: `chatId = {{$items(0).json.from}}`

> Importante: alguns builds da Evolution preferem `sendVoice` / `sendFile` ou param `phone` em vez de `chatId`. Ajuste o endpoint/campos mantendo a mesma lógica.

---

## Fluxo ÁUDIO

### 5A) Baixar mídia (HTTP)

- **URL**: `={{$json.mediaUrl}}`
- **Download**: ✅ → binary `audioIn`

### 6A) Transcrever (HTTP → OpenAI Whisper)

- **Method**: POST
- **URL**: `https://api.openai.com/v1/audio/transcriptions`
- **Auth**: Bearer `OPENAI_API_KEY`
- **Multipart**:
	- `file`: `audioIn`
		- `model`: `whisper-1`
- **Result**: texto em `{{$json.text}}` → salve como `transcript`.

### 7A) Reaproveitar “Prepare Prompt”, “LLM”, “TTS” e “Enviar”

- Substitua a **mensagem do cliente** por `transcript`.

---

## Log/Backup (nó final em ambos fluxos)

**HTTP → microserviço VS Code**

- **POST** `/ingest`
- **Body**:
```markdown
{
  "id": "={{$items(0).json.id}}",
  "from": "={{$items(0).json.from}}",
  "type": "={{$items(0).json.type}}",
  "input": "={{$items(0).json.text || $json.transcript}}",
  "reply": "={{$json.replyText || $items('LLM')[0].json.choices[0].message.content}}",
  "tts": "={{$env.KOKORO_VOICE}}",
  "ts": "={{$now}}"
}
```

E grave o `id` no **Data Store → Upsert** para deduplicação.

---

## VS Code (apenas o essencial): microserviço de backup

Serve pra **guardar histórico** e abrir espaço para métricas/controles futuros. Mantemos mínimo, sem dependências malucas.

## package.json

```markdown
{
  "name": "log-sink",
  "type": "module",
  "scripts": {
    "dev": "node index.js"
  },
  "dependencies": {
    "better-sqlite3": "^9.4.0",
    "express": "^4.19.2"
  }
}
```

## index.js (simples e direto)

```markdown
import express from "express";
import Database from "better-sqlite3";

const db = new Database("./sink.db");
db.exec(\`
CREATE TABLE IF NOT EXISTS messages (
  id TEXT PRIMARY KEY,
  ts TEXT,
  chat_from TEXT,
  type TEXT,
  input TEXT,
  reply TEXT,
  tts TEXT
);
\`);

const app = express();
app.use(express.json({ limit: "5mb" }));

app.post("/ingest", (req, res) => {
  const { id, ts, from, type, input, reply, tts } = req.body || {};
  if (!id) return res.status(400).json({ error: "missing id" });
  const stmt = db.prepare(\`
    INSERT OR REPLACE INTO messages (id, ts, chat_from, type, input, reply, tts)
    VALUES (@id, @ts, @from, @type, @input, @reply, @tts)
  \`);
  stmt.run({ id, ts, from, type, input, reply, tts });
  return res.json({ ok: true });
});

app.get("/health", (_req, res) => res.json({ ok: true }));

app.listen(3001, () => console.log("log-sink on :3001"));
```

> Isso é **só backup**. Depois ampliamos com métricas, buscas, export.csv, etc.

---

## Docker Compose (opcional, tudo junto)

```markdown
services:
  n8n:
    image: n8nio/n8n:latest
    ports: [ "5678:5678" ]
    environment:
      - N8N_HOST=n8n.local
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - TZ=America/Sao_Paulo
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - LLM_MODEL=gpt-4o-mini
      - KOKORO_VOICE=br_female_01
      - KOKORO_FORMAT=mp3
    volumes:
      - ./n8n_data:/home/node/.n8n

  log-sink:
    build: ./log-sink
    ports: [ "3001:3001" ]
    volumes:
      - ./log-sink:/app
    working_dir: /app
    command: ["node","index.js"]
```

> Crie a pasta `log-sink` com os arquivos acima. Suba com `docker compose up -d`.

---

## Check rápido de ponta a ponta

1. Configure **Webhook URL** da Evolution → `https://SEU_N8N/webhook/evolution/inbound`.
2. Dispare um “Oi!” do seu número.
3. Veja a execução no n8n: deve cair no fluxo TEXTO → LLM → TTS → Evolution envia texto+áudio.
4. Verifique backup em `GET http://localhost:3001/health` e confira o arquivo `sink.db` criado.

---

## Onde o n8n brilha nessa fase

- Iterar fluxos de negócio (Trello, Notion, Planilha, CRM) sem programar.
- Agendar follow-ups (“em 1h”, “amanhã 09h”).
- Encadear multi-passo (qualificar lead → abrir card → notificar).

## Onde o VS Code entra só o essencial

- Guardar **histórico** (auditoria), sem travar o desenvolvimento.
- Ter um lugar pra **métricas** e futuras políticas de segurança/assinatura de webhooks.

---

Quer que eu te entregue **o JSON do workflow n8n** já com esses nós prontos (Webhook → IF → LLM → KOKORO → Evolution → Backup), pra importar direto e só trocar as credenciais?