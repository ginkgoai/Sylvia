# LEAF · Loop 2 — "Callima como deve ser" (spec / brief pro Fable)

> Criado 2026-07-01 (Sexta-feira). Fatia vertical: a Callima que **atende, entende e vende por TEXTO e ÁUDIO**, fundamentada em conhecimento real, com handoff que chega a algum lugar. Roda **na stack LOCAL**, governado (Laplace/Boundary), honest-data. Providers travados; tudo atrás do Provider Router (white-label).

## Barra do "pronto"
Um lead manda **áudio** no WhatsApp → a Callima **entende** (STT) → responde fundamentada na **base de conhecimento do tenant** (RAG) → por **texto ou voz** (TTS) → qualifica/agenda/**vende** com o link certo → quando precisa de gente, **passa pro dono e avisa** (handoff). Cada efeito é uma **Skill governada** (Task + orçamento GTK + Evidence); nada inventado.

## Providers (travados; chaves no **COFRE** via `secretScopes`/Boundary — **NUNCA `.env`**; o model-router só NOMEIA o provider)
> Correção pós-revisão (invariante #8): chave de provider é segredo governado — vai pro cofre (igual `openrouter_api_key` do M3-03), injetada por invocação, redigida/auditada/revogável. `.env` escaparia da redação do Boundary.
- **STT** = Groq `whisper-large-v3-turbo` (secret `groq_api_key`) — aceita ogg/opus (nativo do WhatsApp).
- **TTS** = ElevenLabs Flash (`ELEVENLABS_API_KEY`) — voz pt-BR; fallback OpenAI `gpt-4o-mini-tts`.
- **Embeddings** = OpenAI `text-embedding-3-small` (`OPENAI_API_KEY`) — pgvector.
- **Roles novos no model-router:** `callima.stt` · `callima.tts` · `rag.embed`.

## Invariantes (não-negociáveis)
honest-data (falha de STT/TTS/RAG NÃO fabrica conteúdo — degrada honesto) · #3 multi-tenant (credencial e conhecimento por-tenant; org_id do token) · #4 token-aware (áudio custa mais GTK: STT+LLM+TTS) · #6 Evidence por efeito · #8 credencial/segredo via Boundary (nunca no Core/LLM/.env em código) · n8n = executor cego (só o envio); leitura de mídia = read-through do worker.

---

## Sub-fatias (ordenadas; cada uma = 1 loop/PR verificável)

### S1 · STT — áudio de ENTRADA (a Callima entende voz)
- **Onde:** worker do tronco (NÃO novo fluxo n8n). Ao chegar `kind=AUDIO`, o worker faz *read-through* da mídia via Evolution (`getBase64FromMediaMessage`) com **lease da Boundary** (chave Evolution do tenant, efêmera) — igual já lê status/QR.
- **Cognição:** manda o áudio pro `callima.stt` (Groq) → transcrição.
- **Persistência:** grava a transcrição em `ChatMessage.text` (novo campo/uso) marcada como transcrita; o prompt da Callima passa a receber o TEXTO real (não mais `"[audio]"`).
- **honest-data:** se o STT falhar, NÃO inventa — a bolha mostra "áudio não transcrito" e a Callima pede pra repetir por texto. Sem transcrição-fantasma.
- **Governança:** Skill `leaf.stt.transcribe` (R1), Evidence `stt:transcribed:<hash>`, débito GTK.
- **Verificação:** teste unit (fixture de áudio → texto), teste de falha (provider 500 → degrada honesto), e2e local com um áudio real.

### S2 · TTS — áudio de SAÍDA (a Callima responde por voz)
- **Decisão de voz:** persona/política do tenant decide quando responder em áudio (ex.: cliente mandou áudio, ou config "responder por voz").
- **Fluxo:** `callima.tts` (ElevenLabs Flash) → **transcode mp3→ogg/opus** → **fluxo n8n cego novo** `channel.whatsapp.send-audio` (Evolution sendWhatsAppAudio/PTT) → **confirmer simétrico** (só o Boundary emite EXTERNAL_CONFIRMATION).
- **Custo:** débito GTK do áudio = STT(se houve) + LLM + TTS; pinar no pricing.
- **honest-data:** bolha de áudio só confirma após o confirmer (Task COMMITTED); TTS falho ⇒ cai pra texto, sem fingir envio.
- **Governança:** Skill `leaf.reply.whatsapp.audio` (R1), egress Evolution, Evidence `observed:`.
- **Verificação:** teste de envio (mock n8n), teste de fallback texto, e2e local (a Callima responde um áudio de verdade).

### S3 · RAG vetorial — a Callima ENTENDE (conhecimento do tenant)
- **Schema (Prisma + pgvector):** `Knowledge` (fonte por-tenant: texto/URL/FAQ) · `KnowledgeChunk` (chunk + `embedding vector` + metadata/tags hierárquicas) — absorve o **#13** (memória em camadas: bruto=fonte, refinado=chunk, RAG=embedding).
- **Ingestão:** fonte → chunk → embed (`rag.embed` OpenAI) → grava vetor. Ferramenta Brann **`adicionar_conhecimento`** (colar texto/URL pelo chat) + **tela de Conhecimento** (F4, review/CRUD).
- **Recuperação:** busca **híbrida** (keyword + vetor por `org_id`) → top-k injetado no prompt da Callima (substitui a string chapada de ofertas).
- **honest-data:** a Callima só afirma o que está no conhecimento recuperado; sem fonte ⇒ diz que não sabe (não alucina).
- **Governança:** por-tenant estrito (RLS/`org_id`), Skill de ingestão (R1), Evidence.
- **Verificação:** retrieval determinístico (fixture → chunks esperados), isolamento cross-tenant (tenant A não vê conhecimento de B), teste de "sem fonte ⇒ honesto".

### S4 · Handoff que chega a algum lugar (#15)
- **Gatilho:** a Callima detecta intenção de handoff (pedido de humano, fora do escopo, frustração) → emite intenção (não executa sozinha).
- **Efeito:** pausa a IA na conversa (`aiPausedReason='handoff'`) + marca a conversa "**precisa de você**" + **alerta ao dono** (WhatsApp/Discord/e-mail, o que o tenant configurar) → surface na inbox (filtro/badge).
- **honest-data:** só marca handoff real; o alerta só "enviado" após efeito real.
- **Governança:** Skill de alerta (R1) via Boundary; sem novo segredo além dos canais do tenant.
- **Verificação:** teste do gatilho→pausa→alerta; a inbox mostra o item; e2e local.

---

## Transversais
- **Model-router:** adicionar os 3 roles; STT/TTS/embeddings via chave direta (OpenRouter é só chat).
- **Migração n8n:** o `AUDIO FEM` interino vira o `channel.whatsapp.send-audio` cego; a cognição de áudio/RAG nasce no worker (não no n8n).
- **Ordem:** S1 → S2 → S3 → S4 (cada uma um loop/PR; gate `pnpm build && typecheck && test` verde + teste da fatia).

## O que precisa do fundador
- Chaves já no `.env`: Groq ✓ · ElevenLabs ✓ · OpenAI ✓ (rotacionadas).
- Rodar a stack local (infra + app) pra os e2e de áudio/RAG.
- Escolher o cliente-piloto (conhecimento + ofertas reais) pra alimentar o RAG.
