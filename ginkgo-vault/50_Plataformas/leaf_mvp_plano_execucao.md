# LEAF — Plano de Execução do MVP (re-baseline · 2026-07-01)

> Reinício do loop. Foco único: **LEAF enxuto**, a primeira plataforma a abrigar usuários reais.
> Tronco canônico = `C:\dev\ginkgo-tree`. Cofre = `C:\sexta-feira\ginkgo-vault`.
> **honest-data é lei** em tudo: a UI e a Callima nunca afirmam o que o sistema não provou.

---

## 1. A barra do "pronto" (o que o MVP precisa fazer)

Um cliente assina o LEAF e consegue:

1. **Entrar** → criar conta, conectar o WhatsApp dele (QR).
2. **Configurar a Callima falando com o Brann** — persona, ofertas, conhecimento, ligar. (a conversa é o produto; as telas são a lente)
3. A **Callima atende no WhatsApp por TEXTO e ÁUDIO**: entende (fundamentada em conhecimento real), qualifica, agenda, e **vende** mandando o link de pagamento certo — sempre honest-data.
4. O dono **vê tudo** no CRM (funil) + Caixa de entrada, **assume** quando quiser (handoff), e vê **métricas reais** básicas.
5. **Paga** — assinatura do Leaf + recarga de GTK (Stripe).

Tudo além disso é *feature* (Wave/Pyre, multi-agente, automações visuais custom, RAG vetorial completo, white-label, app mobile, multicanal Instagram/e-mail).

---

## 2. Onde a plataforma está HOJE (real, provado no tronco)

**Sólido / PRODUCTION:**
- **Governança (Laplace):** Kernel (Task lineage completo), Security Boundary (assinatura de executor, injeção de segredo por lease + auditoria, evidence-binding anti-forja, confirmer independente), ledger de tokens HOLD/SETTLEMENT, HITL em R3. Espinha robusta.
- **CRM:** Pipeline/Stage/Lead + Kanban (drag-drop, tags, etapas, temperatura Quente/Morno/Frio) ligado à API real.
- **Caixa de entrada:** 3 painéis WhatsApp (lista/thread/composer/lead-panel), IA liga/desliga + "assumir/devolver", resolver/reabrir, envio humano governado. **Só texto.**
- **Callima (motor de resposta):** texto-in/texto-out via OpenRouter → n8n → Evolution. Debounce + anti-runaway (loop, tetos, saldo). Honest-data (disclosure de IA, nunca "pago confirmado").
- **Brann (assistente web):** chat governado (Task R1, custo visível) ligado ao balão; **ferramentas de função** `configurar_callima` + `cadastrar_oferta` (o "inteira" — persona + oferta + ligar num papo só, escrita real + prova ancorada). ✅ recém-entregue e testado (9/9).
- **Ofertas:** CRUD completo + feed legível pra Callima vender com o link certo.
- **Billing:** planos, checkout, Payment Links, webhook de assinatura/fatura (Stripe).
- **Auth/tenancy:** e-mail+senha, Google OAuth, JWT, cookie httpOnly, escopo por org.
- **Conectar WhatsApp (QR):** governado R3 + HITL, QR ao vivo. Agenda (Google Calendar) via bridge n8n.

**Provisionado mas dormente:** pgvector + AnythingLLM (RAG) — infra pronta, **zero** código de aplicação usando.

---

## 3. Os GAPS do MVP (o que falta pra barra do item 1)

| # | Gap | Estado hoje | Impacto |
|---|-----|-------------|---------|
| G1 | **Áudio de entrada (STT)** | mensagem de voz vira só o rótulo `"[audio]"` pro modelo — não transcreve | **crítico** — "atende por áudio" não existe |
| G2 | **Áudio de saída (TTS)** | inexistente; n8n só manda `sendText` | alto (o vault cita ElevenLabs) |
| G3 | **Conhecimento (RAG-lite)** | não há tabela Knowledge; "conhecimento" = `Offer.description` + janela de 20 msgs | alto — o "entende" é raso |
| G4 | **Handoff pra humano que chega a algum lugar** | Callima não sinaliza "preciso de você"; hoje o handoff "vai pra lugar nenhum" | médio-alto (#15) |
| G5 | **Tela de config da Callima + Conhecimento** | nav marca "em breve"; config só via chat do Brann | médio |
| G6 | **Player de áudio/mídia na Caixa** | mostra "Mensagem de voz" sem player; mic desabilitado | médio |
| G7 | **Métricas reais no dashboard** | KPIs do LeafOverview são placeholders honestos-vazios | médio (demo/venda) |
| G8 | **Criar/importar lead manual no CRM** | leads só via WhatsApp/ingest | baixo-médio |
| G9 | **Prod (hospedar usuários)** | só local; túnel/env/compose prod pendentes | gate de negócio (#23-25) |

*(Automações "custom" e RAG vetorial completo ficam FORA do MVP por decisão do cofre; as "automações" do MVP são o próprio loop da Callima: atende/qualifica/agenda/vende.)*

---

## 4. Tasks — **FABLE** (código pesado, no tronco `ginkgo-tree`)

- **F1 · Áudio de entrada (STT).** Buscar a mídia (Evolution `getBase64FromMediaMessage`) → transcrever via provider → gravar transcrição na `ChatMessage` → alimentar o prompt da Callima com o texto real. Governado como skill, honest-data (se a transcrição falhar, não inventa conteúdo). *Depende de: brief C-spec + provider (você).*
- **F2 · Áudio de saída (TTS) — MVP (D1).** Callima responde por áudio quando fizer sentido (política/persona) → TTS → nó n8n `sendWhatsAppAudio` → confirmer simétrico (igual ao texto).
- **F3 · Conhecimento — RAG VETORIAL (D2, absorve #13). MAIOR fatia.** Tabelas Knowledge/Chunk/Embedding + pgvector por-tenant (P004); pipeline ingestão→chunk→embed; busca híbrida (keyword+vetor) injetada no prompt da Callima; ferramenta Brann `adicionar_conhecimento`. Desenho de arquitetura ANTES de codar (C1/C2). Precisa provider de embeddings (Y8).
- **F4 · Tela Callima + Conhecimento (web).** Tela mínima: preview da persona, toggle ligado, ofertas, editor de conhecimento. Reaproveitar o LeadPanel/padrões.
- **F5 · Handoff que chega a algum lugar (#15).** Callima emite intenção de handoff → pausa a IA + marca a conversa "precisa de você" + filtro/aviso na Caixa.
- **F6 · Player de áudio na Caixa + gravar áudio (G6).** Renderizar/tocar voz; habilitar o mic do composer.
- **F7 · Métricas reais no dashboard (G7).** Ligar os KPIs do LeafOverview a dados que já existem (conversas, leads por etapa, respostas 24h, agendamentos). Honest-data, nada de número fake.
- **F8 · Criar/importar lead no CRM (G8).** Botão "novo lead" + import CSV simples.
- **F9 · Prod hardening (#23-25) — adiado (D4=local).** compose prod + túnel Cloudflare + smoke test, quando o caixa justificar.
- **F10 · Tema dark (#39).** *(opcional)* variante + toggle.
- **F11 · Lapidação web + avatar do Brann (Duolingo). ← PRIMEIRO LOOP (zero credenciais).** Responsividade (375/768/1280 sem overflow/sobreposição), polish visual anti AI-slop no tema warm, motion/efeitos coesos, avatar-mascote animado do Brann (idle/pensando/falando/sucesso/erro) no AgentBubble, varredura hardcodes→tokens. Verificado por gate + Playwright. *Roda enquanto você libera as chaves de áudio/embeddings.*
- **F12 · Autenticação & Conta (padrão SaaS) + endurecimento de segurança (defensivo).** Login Google/Apple/e-mail, esqueci-senha, verificação de e-mail, aceite de termos versionado, sessão/cookies seguros, rate-limit/anti-brute-force, LGPD (excluir dados) + Security Review com testes que PROVAM cada proteção. Credencial-gated: Apple + provider de e-mail transacional (Y9/Y10).

## 5. Tasks — **COWORK (eu)** — spec, QA, glue, docs

- **C1 · Briefs de tarefa do Fable.** Escrever os specs enxutos de F1/F2/F3/F5 (contrato honest-data, governança, evidence, pontos de falha) pra o Fable receber tarefa apertada.
- **C2 · Provider STT/TTS + model-router.** Pesquisar custo/qualidade (candidatos: STT = Groq Whisper / OpenAI / Deepgram; TTS = ElevenLabs / OpenAI) e desenhar o *role* no model-router mantendo margem/white-label. Recomendação + fatia de código.
- **C3 · QA-gate de cada fatia.** Typecheck + testes + revisão honest-data conforme o Fable entrega (como fiz nas ofertas). Sou o portão.
- **C4 · Reconciliar specs/memória com o tronco (#7/#9).** Marcar o `00_INDEX_specs.md` como stale, atualizar `MEMORIA.md`/`CONTEXT_LOG.md` pro estado real, alinhar o `memory_system_sextafeira.md`.
- **C5 · Verificar assinatura Payment Links ponta a ponta (#19).** Webhook → plano → e-mail → tenant → ativa. Apontar gaps pro Fable.
- **C6 · Trilha de demo afiada (#21).** Seed, tema warm, fluxo Brann "inteira" — pronto pra mostrar/vender.

## 6. Tasks — **VOCÊ** — acessos, rotas, envs, apis, decisões

- **Y1 · Provider de áudio.** Decidir + liberar chave/crédito do STT e do TTS (OpenRouter já existe pra LLM; áudio precisa de conta/API própria — ex.: Groq/OpenAI/ElevenLabs). Confirmar orçamento de tokens de áudio.
- **Y2 · Parear WhatsApp** do cliente-piloto (QR + login Google são atos seus — credenciais só você toca).
- **Y3 · Stripe.** Confirmar que os Payment Links do plano Leaf e das ofertas-piloto estão vivos/corretos.
- **Y4 · Rotas & envs.** Confirmar base URL da API, webhooks do n8n, config da instância Evolution, e que os `.env` estão preenchidos (eu reuso via script sem exibir segredo).
- **Y5 · Cliente-piloto.** Escolher o negócio real pra primeiro onboard (ex.: Belle Estética) com ofertas + conhecimento reais.
- **Y6 · Decisão de hospedagem (#23-25).** Local (demo/primeiros clientes na mão) **ou** subir prod agora (túnel Cloudflare `TUNNEL_TOKEN` + `.env` de prod + domínio). Se prod: me liberar o token + preencher o env.
- **Y8 · Provider de embeddings** (RAG vetorial): decidir/liberar chave/crédito (ex.: OpenAI text-embedding-3-small, ou modelo aberto via provider). — *Y7 (decisões de escopo) ✅ resolvido em 01/07.*

---

## 7. Decisões TRAVADAS (2026-07-01)

- **D1 · Áudio = STT + TTS juntos no MVP.** A Callima entende E responde por voz desde o lançamento. → F1 e F2 ambos MVP; precisa provider de STT **e** de TTS (Y1).
- **D2 · Conhecimento = RAG VETORIAL completo agora.** pgvector + embeddings + busca híbrida (absorve o #13, memória em camadas). É a **MAIOR fatia** do Fable; precisa provider de embeddings (Y8). → F3 sobe de "lite" pra vetorial.
- **D3 · Config da Callima = chat do Brann + tela mínima de review.** Configurar por conversa (já funciona) + tela só de preview/toggle/ofertas/conhecimento. → F4 = tela de review.
- **D4 · Hospedagem = local por enquanto.** Prod (F9/Y6) fica pra quando o caixa justificar. Não bloqueia o loop.

---

## 8. Ordem sugerida do loop

1. **Você:** D1–D4 + Y1 (provider de áudio) + Y5 (cliente-piloto).
2. **Eu (Cowork):** C1 (briefs) + C2 (provider/router) — em paralelo com sua liberação.
3. **Fable:** F1 (STT) → F3 (conhecimento) → F5 (handoff) → F6/F4 (áudio na UI + tela Callima) → F7 (métricas) → F2 (TTS, se D1=MVP).
4. **Eu:** C3 (QA) a cada fatia; C4/C5/C6 em paralelo.
5. **Você:** Y6 quando o loop fechar local → F9 (prod) quando o caixa justificar.

> Mapa das tasks antigas: #7/#9→C4 · #13→F3 (RAG-lite; vetorial pós-MVP) · #15→F5 · #19→C5 · #21→C6 · #23-25→Y6/F9 · #30→pós-MVP (VPS) · #39→F10.
