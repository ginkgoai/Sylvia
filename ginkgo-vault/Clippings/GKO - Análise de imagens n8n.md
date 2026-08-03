---
title: "GKO - Análise de imagens n8n"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68f7b7dd-ee14-832a-872c-1e70d4dae684"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
ter., 21 de out. às 13:42

Sim. Adicione um para corretores de imóveis e imobiliárias também. Vamos usar nosso template do Brann e apenas diversificar para esses setores e mudar prompt envs e o que for necessário.

Perfeito, Gabriel — isso é o caminho certo: **usar o mesmo “esqueleto inteligente” do Brann** e apenas adaptar identidade, prompts, e variáveis de ambiente para diferentes segmentos. Assim tu consegues **multiplicar agentes verticais** mantendo uma base técnica unificada.

Vamos desenhar a estrutura base e depois eu te mostro como clonar cada agente e adaptar rapidamente no n8n.

---

## 🌿 MAPA DE AGENTES GINKGO (base Brann)

Cada um desses usa o mesmo modelo estrutural de fluxo:

> **Entrada (WhatsApp / Áudio / Documento)** → **Transcrição** → **Compreensão via LLM** → **Ação específica** → **Resposta humanizada (texto ou voz)**

---

### 1\. 🧠 BRANN — Vendedor & Atendente Comercial

**Público:** empresas e autônomos  
**Função principal:** captação e qualificação de leads, atendimento e fechamento de vendas.

**Prompt base:** personalidade carismática, empática e consultiva.  
**Ações principais:**

- Captação de leads (formulário conversacional)
- Atendimento de dúvidas
- Catálogo de produtos / serviços
- Agendamento de reuniões
- Envio de propostas automáticas
- Follow-up de clientes

---

### 2\. ⚖️ GINKGO LAW — Assistente Jurídica (versão “Júlia”)

**Público:** advogados e escritórios jurídicos  
**Base:** Brann + funções jurídicas

**Extras no fluxo:**

- Upload de documentos (PDFs, DOCX)
- Análise de petições / contratos
- Geração de minutas e notificações
- Agenda de prazos processuais (Google Calendar)
- Resumo e classificação de áudios de clientes
- Chat jurídico com contexto legal
- Banco de templates legais

**Env vars adicionais:**

```markdown
LAW_DOCS_FOLDER=
GOOGLE_CALENDAR_API_KEY=
JURIDICO_PROMPT_SYSTEM=
```

---

### 3\. 🧱 GINKGO BUILD — Agente para Engenheiros / Obras

**Público:** engenheiros civis, arquitetos, construtoras  
**Base:** Brann + automação financeira e de obras

**Extras no fluxo:**

- Recebe áudios, notas ou fotos de comprovantes
- Extrai dados com OCR + LLM
- Atualiza planilhas de orçamento automaticamente (Google Sheets)
- Gera relatórios de custos e produtividade
- Envia lembretes de etapas da obra e pagamentos

**Env vars adicionais:**

```markdown
SHEET_ENGINEER_BUDGET_ID=
OCR_API_KEY=
ENGINEER_PROMPT_SYSTEM=
```

---

### 4\. 🏠 GINKGO REALTY — Assistente para Corretores e Imobiliárias

**Público:** corretores autônomos e imobiliárias  
**Base:** Brann + integração imobiliária

**Extras no fluxo:**

- Recebe mensagens e filtra tipo de imóvel (venda/aluguel)
- Consulta banco de imóveis (Supabase)
- Envia opções filtradas com fotos e descrição
- Agendamento automático de visitas (Google Calendar)
- Geração de contratos e recibos
- Envio automático de follow-ups
- Notificações de vistoria e vencimento de aluguel

**Env vars adicionais:**

```markdown
SUPABASE_URL=
SUPABASE_KEY=
IMOVEIS_TABLE=
CORRETOR_PROMPT_SYSTEM=
GOOGLE_CALENDAR_API_KEY=
```

---

### 5\. 💸 GINKGO PAY — Agente Financeiro / Autônomos

**Público:** prestadores de serviço, pequenos empreendedores  
**Base:** Brann + controle financeiro pessoal

**Extras no fluxo:**

- Recebe comprovantes de pagamento ou nota via WhatsApp
- Extrai e categoriza despesas/receitas
- Atualiza planilha financeira automaticamente
- Gera relatórios diários ou semanais
- Envia lembretes de cobrança e vencimentos

**Env vars adicionais:**

```markdown
SHEET_FINANCAS_ID=
PAY_PROMPT_SYSTEM=
OCR_API_KEY=
```

---

## ⚙️ PRINCÍPIO TÉCNICO

Todos herdam a mesma arquitetura:

```markdown
WhatsApp → Transcrição (Kokoro STT) → Análise (LLM via Flowise / n8n) → 
Ação específica (Google Sheets / Docs / Supabase / etc.) → 
Resposta humanizada (texto + Kokoro TTS)
```

O que muda:

- O **prompt do agente** (personalidade + especialidade)
- As **variáveis de ambiente** (chaves e tabelas específicas)
- Alguns **nós condicionais** (ex.: contrato jurídico vs imóvel vs orçamento)

---

Se quiser, posso te gerar agora o **modelo JSON do fluxo base Brann adaptável** (com variáveis genéricas e placeholders) — assim tu só duplica, altera os envs e o prompt do agente pra cada setor.  
Quer que eu gere esse modelo pronto pra importar no n8n?

Agora quero tirar dúvidas sobre o BACK END, qual estrutura de back end ideal para o Brann? O que deve ser montado? Todo o necessário vscode, pois vejo na imagem dele q ele o usa, pq e para que, no n8n ficará os templates e funções tudo, no vs code oq? É um modelo híbrido se sim me ajude a construir o do Brann da mesma forma para amplificar as capacidade e funcionalidades.

Bora deixar o Brann “bi-turbo”: n8n cuidando da orquestra e um back end leve (VS Code) para tudo que exige código de verdade, performance, versionamento e testes. É um **modelo híbrido**. A regra é simples:

- **No n8n:** entrada/saída do WhatsApp, roteamento por mídia, memória curta, prompts, templates, gatilhos e integrações prontas.
- **No back end (API + worker):** tarefas pesadas, longas, reutilizáveis ou que dependem de libs (OCR, TTS/STT alternativos, RAG, geração de PDFs/contratos, scraping, filas, assinaturas HMAC, cache, rate-limit, logs, testes).

Abaixo está o blueprint “copy/cola” para levantar o **Back End do Brann**.

---

## 1) Estrutura recomendada (monorepo simples)

```markdown
brann/
├─ api/                      # FastAPI (endpoints síncronos)
│  ├─ main.py
│  ├─ deps.py                # auth, rate limit, CORS
│  ├─ routers/
│  │  ├─ health.py
│  │  ├─ media.py            # /transcribe, /ocr, /image-caption
│  │  ├─ tts.py              # /tts-kokoro, /tts-cache
│  │  ├─ docs.py             # /contract, /pdf-fill
│  │  ├─ rag.py              # /rag/search, /rag/upsert
│  │  └─ wa.py               # /wa/send-audio, util p/ Evolution
│  ├─ services/
│  │  ├─ stt.py              # Whisper/OpenAI/Deepgram wrapper
│  │  ├─ ocr.py              # Tesseract/PaddleOCR
│  │  ├─ kokoro.py           # cliente HTTP pro Kokoro
│  │  ├─ supabase.py         # client + queries
│  │  ├─ pdf.py              # pydantic+docxtpl+pdfkit
│  │  └─ rag.py              # vetoriza, busca, rerank
│  └─ models/                # pydantic (request/response)
│
├─ worker/                   # tarefas assíncronas
│  ├─ tasks.py               # RQ/Celery jobs (ex.: transcrever grande, OCR pesado)
│  └─ queue.py
│
├─ shared/
│  ├─ config.py              # lê .env, valida
│  └─ utils.py               # HMAC, uuid, s3 helpers, tracing
│
├─ prompts/                  # YAMLs versionados (por “agente”)
│  ├─ brann.system.yaml
│  └─ brann.tools.yaml
│
├─ tests/                    # pytest
├─ docker-compose.yml
├─ Dockerfile
├─ requirements.txt (ou pyproject.toml)
└─ .env.example
```

**Por que FastAPI + worker (RQ/Celery)?**  
Porque o n8n não é bom para: PDFs grandes, OCR pesado, scraping com retries, TTS em lote, pipeline de RAG, assinatura de webhooks e fila de reprocessamento. No back end tu resolves isso com **filas + cache + reuso de libs**.

---

## 2) Variáveis de ambiente (.env.example)

```markdown
# Core
ENV=prod
APP_PORT=8080
API_BASE_URL=http://api:8080
ALLOWED_ORIGINS=*

# Auth entre n8n e API
INTERNAL_TOKEN=supersecreto
HMAC_SECRET=troque_isto

# Evolution API (WhatsApp)
EVOLUTION_BASE_URL=https://SEU-HOST:PORTA
EVOLUTION_TOKEN=XXX
EVOLUTION_INSTANCE=BRANN

# Supabase (memória longa, imóveis, etc.)
SUPABASE_URL=https://xyz.supabase.co
SUPABASE_KEY=sbp_...
SUPABASE_JWT=service_role_ou_anon
SUPABASE_BUCKET=brann-media
SUPABASE_TABLE_MEMORY=memory
SUPABASE_TABLE_IMOVEIS=imoveis

# Redis / Fila
REDIS_URL=redis://redis:6379/0

# Kokoro (TTS)
KOKORO_URL=http://kokoro:9000/synthesize
KOKORO_VOICE=pt_br_female_01

# STT / LLM
OPENAI_API_KEY=sk-...
OPENAI_MODEL_4O_MINI=gpt-4o-mini-transcribe

# S3/MinIO (opcional)
S3_ENDPOINT=http://minio:9000
S3_ACCESS_KEY=admin
S3_SECRET_KEY=admin123
S3_BUCKET=brann
```

---

## 3) Docker Compose (subir tudo de uma vez)

```markdown
version: "3.9"
services:
  api:
    build: .
    container_name: brann-api
    env_file: .env
    ports: ["8080:8080"]
    depends_on: [redis]
  worker:
    build: .
    container_name: brann-worker
    env_file: .env
    command: ["python", "-m", "worker.queue"]   # RQ worker
    depends_on: [redis]
  redis:
    image: redis:7-alpine
    container_name: brann-redis
    ports: ["6379:6379"]
  # opcional: MinIO para media
  minio:
    image: minio/minio
    environment:
      MINIO_ROOT_USER: admin
      MINIO_ROOT_PASSWORD: admin123
    command: server /data --console-address ":9001"
    ports: ["9000:9000","9001:9001"]
```

**Dockerfile (Python 3.11):**

```markdown
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["uvicorn","api.main:app","--host","0.0.0.0","--port","8080"]
```

**requirements.txt (mínimo):**

```markdown
fastapi==0.114.2
uvicorn[standard]==0.30.6
python-dotenv==1.0.1
pydantic==2.9.2
requests==2.32.3
redis==5.0.8
rq==1.16.2
supabase==2.6.0
docxtpl==0.16.7
pdfkit==1.0.0
pypdf==4.3.1
pillow==10.4.0
```

---

## 4) API base (FastAPI) — endpoints que o n8n vai chamar

`api/main.py`

```markdown
from fastapi import FastAPI, Header, HTTPException, Depends
from shared.config import settings
from api.deps import verify_internal_token
from api.routers import health, media, tts, docs, rag, wa

app = FastAPI(title="Brann API")

@app.middleware("http")
async def token_guard(request, call_next):
    if request.url.path.startswith("/health"):
        return await call_next(request)
    # token simples (ou substitua por HMAC em deps.py)
    token = request.headers.get("x-internal-token")
    if token != settings.INTERNAL_TOKEN:
        raise HTTPException(status_code=401, detail="unauthorized")
    return await call_next(request)

app.include_router(health.router, prefix="/health")
app.include_router(media.router, prefix="/media")
app.include_router(tts.router,   prefix="/tts")
app.include_router(docs.router,  prefix="/docs")
app.include_router(rag.router,   prefix="/rag")
app.include_router(wa.router,    prefix="/wa")
```

`api/routers/media.py` (ex.: transcrever áudio pesado via fila):

```markdown
from fastapi import APIRouter, UploadFile, File, HTTPException
from worker.tasks import transcribe_task
from rq import Queue
from shared.config import settings
from redis import Redis

router = APIRouter()
redis = Redis.from_url(settings.REDIS_URL)
q = Queue("brann", connection=redis)

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    job = q.enqueue(transcribe_task, await file.read(), file.filename, ttl=3600)
    return {"job_id": job.id}

@router.get("/transcribe/{job_id}")
def transcribe_result(job_id: str):
    job = q.fetch_job(job_id)
    if not job: raise HTTPException(404, "job not found")
    if job.is_finished: return {"status":"done", "text": job.result}
    if job.is_failed:   return {"status":"failed"}
    return {"status":"queued"}
```

`worker/tasks.py` (ex.: STT com OpenAI/Whisper):

```markdown
import base64, io
from shared.config import settings
import requests

def transcribe_task(raw_bytes: bytes, filename: str) -> str:
    # exemplo com OpenAI "audio.transcriptions"
    from openai import OpenAI
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    audio_b64 = base64.b64encode(raw_bytes).decode()
    resp = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe",
        file={"filename": filename, "content": audio_b64}
    )
    return resp.text.strip()
```

`api/routers/tts.py` (Kokoro wrapper + cache S3 opcional):

```markdown
from fastapi import APIRouter
from shared.config import settings
import requests, uuid

router = APIRouter()

@router.post("/kokoro")
def kokoro_tts(payload: dict):
    text = payload.get("text","").strip()
    voice = payload.get("voice", settings.KOKORO_VOICE)
    r = requests.post(settings.KOKORO_URL, json={"text": text, "voice": voice})
    r.raise_for_status()
    # r.content deve ser WAV/OGG/MP3; devolve URL ou bytes
    audio_bytes = r.content
    # …(opcional) subir no MinIO/S3 e retornar URL público
    return {"bytes_b64": audio_bytes.hex()}  # ou {"url": "https://..."}
```

`api/routers/docs.py` (gerar contrato/recibo em DOCX/PDF):

```markdown
from fastapi import APIRouter
from docxtpl import DocxTemplate
import pdfkit, tempfile, os

router = APIRouter()

@router.post("/contract")
def generate_contract(data: dict):
    tpl = DocxTemplate("templates/contrato_base.docx")
    tpl.render(data)
    tmp_docx = tempfile.mkstemp(suffix=".docx")[1]
    tpl.save(tmp_docx)
    tmp_pdf = tmp_docx.replace(".docx",".pdf")
    pdfkit.from_file(tmp_docx, tmp_pdf)
    # subir para S3 ou devolver como bytes
    with open(tmp_pdf,"rb") as f:
        pdf = f.read()
    os.remove(tmp_docx); os.remove(tmp_pdf)
    return {"pdf_b64": pdf.hex()}
```

`api/routers/wa.py` (disparar PTT via Evolution):

```markdown
from fastapi import APIRouter
from shared.config import settings
import requests

router = APIRouter()

@router.post("/send-audio")
def send_audio(payload: dict):
    number = payload["number"]
    url = payload["audio_url"]  # gerado por /tts/kokoro ou S3
    r = requests.post(
        f"{settings.EVOLUTION_BASE_URL}/message/sendAudio/{settings.EVOLUTION_INSTANCE}",
        headers={"Authorization": f"Bearer {settings.EVOLUTION_TOKEN}"},
        json={"number": number, "mediaData": {"url": url}, "ptt": True},
        timeout=30
    )
    r.raise_for_status()
    return r.json()
```

---

## 5) Como o n8n conversa com a API (padrão copy/cola)

**HTTP Request (n8n) → header fixo**

```markdown
x-internal-token: {{$env.INTERNAL_TOKEN}}
```

**Ex.: enviar áudio para transcrição (quando for grande/pesado)**

1. `HTTP Request` (POST, binary file → `file`) para `http://api:8080/media/transcribe`
2. `Wait` e `HTTP Request` (GET) em `/media/transcribe/{{$json.job_id}}` até `status="done"`
3. `Set`: `text = {{$json.text}}` → segue para o nó BRANN.

**Ex.: gerar PTT**

1. `HTTP Request` (POST) `http://api:8080/tts/kokoro` com `{ "text":"={{$json.out.text}}", "voice":"pt_br_female_01" }`
2. Recebe `audio_url` (se usar S3)
3. `HTTP Request` (POST) `http://api:8080/wa/send-audio` com `{ "number":"={{$json.phone}}", "audio_url":"={{$json.audio_url}}" }`

---

## 6) O que fica no back end vs no n8n

**Back end (código):**

- STT/TTS alternativos ou lotes grandes
- OCR/visão, PDF parsing, contratos DOCX → PDF
- RAG: ingestão de documentos, embeddings, busca (Supabase pgvector)
- Filas (RQ/Celery) para jobs longos, retries e timeouts
- Assinatura HMAC de webhooks e rate-limit
- Cache (Redis) de chamadas caras e de TTS
- Biblioteca de “ferramentas” para o Brann (web-scrape, extratores)

**n8n (fluxo):**

- Webhook do WhatsApp, roteamento por mídia
- Memória curta, estado de conversa, prompts/templates
- Regras de negócio, botões, listas, agendamentos
- Chamar o back end quando precisar de “músculo”

---

## 7) Segurança & observabilidade (essencial)

- **Auth interno:** header `x-internal-token` + **HMAC** opcional (assina body com `HMAC_SECRET` e o back end valida).
- **Rate limit/circuit-breaker:** limite por IP/rota; retries exponenciais no worker.
- **Logs estruturados:** traceId no início do fluxo; loga latência e mídia processada.
- **Erros gritantes:** sempre um fallback seguro no n8n (“não consegui processar a mídia; posso seguir por texto?”).
- **Backups:** bucket de mídia + Supabase (memória) com retenção.
- **Versionamento:** prompts YAML e templates em repositório Git; tags por cliente.

---

## 8) Passo a passo agora

1. Criar pasta `brann/` com a árvore acima.
2. Copiar `.env.example` → `.env` e preencher.
3. `docker compose up -d` (api, worker, redis, minio opcional).
4. No n8n, criar **credencial HTTP** com `x-internal-token`.
5. Substituir nós de transcrição/TTS pesados para chamar a API.
6. Teste E2E: texto → áudio → imagem → contrato → PTT.

---

Quer que eu gere os **arquivos base** (main.py, tasks.py, requirements.txt, Dockerfile e docker-compose.yml) prontos num pacote `.zip` com os YAMLs de prompt do Brann para tu abrir no VS Code e subir direto?