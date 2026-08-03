# LEAF · 2 Pilotos + Roteiro de Demo (setup)

> 2026-07-01. Dois tenants pra validar ponta-a-ponta (secretária Callima + assistente Brann + dashboard) e gravar a demo. **Provisionamento é host-side** (scripts do tronco); o sandbox da Sexta-feira não toca a stack.

## Os 2 pilotos

### Piloto 1 — Ginkgo (a própria) · Callima
- **org:** "Ginkgo" · **agentName:** "Callima" · **businessName:** "Ginkgo AI Systems".
- **número:** +55 53 9133-8911 — ⚠️ ver *Caveat do número* abaixo.
- **persona:** secretária da Ginkgo — qualifica interessados no LEAF/Callima, tira dúvidas, agenda demo, manda o link do plano. Tom caloroso, técnico-claro, direto. honest-data.
- **ofertas:** planos LEAF ($79/$199/$499) com link Stripe.
- **conhecimento (RAG):** FAQ Ginkgo/LEAF (o que é, o que a Callima faz, preços, como conectar o WhatsApp).

### Piloto 2 — [PROPOSTA: Belle Estética] · *(swappable)*
Vertical DIFERENTE de propósito (prova o multi-tenant na demo).
- **org:** "Belle Estética" · **agentName:** "Sofia" · **businessName:** "Belle Estética".
- **número:** um número de TESTE dedicado (não o +5553).
- **persona:** recepção — agenda procedimentos, responde preço/horário, confirma. Calorosa, objetiva.
- **ofertas:** procedimentos (ex.: Limpeza de Pele R$180) com link.
- **conhecimento:** serviços, horários, endereço, políticas.
> **Troca livre:** se você tem um cliente REAL pro 2º piloto, me passa negócio + ofertas + conhecimento que eu troco o conteúdo.

## Sequência de provisionamento (host-side, por tenant)
Pré: stack local no ar (`bash scripts/start-dev.sh`); `.env` com `ENCRYPTION_KEY` + as 4 chaves de provider.
1. **Criar org+user:** signup em `/signup` (ou `POST /auth/signup {orgName,email,password}`) → anota o `ORG_ID`.
2. **Config da Callima:**
   `DATABASE_URL=... ORG_ID=<id> AGENT_NAME=Callima BUSINESS_NAME="Ginkgo AI Systems" EXTRA_INSTRUCTIONS="<persona>" ENABLED=true node --import tsx scripts/seed-agent-profile.ts`
3. **Cofre (×4 — valor vem de env var, NUNCA de argv):** repetir o comando trocando `SECRET_KEY`/`SECRET_VALUE_ENV`:
   `DATABASE_URL=... ENCRYPTION_KEY=... ORG_ID=<id> SECRET_KEY=evolution_api_key SECRET_VALUE_ENV=EVOLUTION_API_KEY node --import tsx scripts/put-secret.ts`
   → repetir p/ `openrouter_api_key`, `groq_api_key`, `elevenlabs_api_key` (SECRET_VALUE_ENV apontando pra cada var do `.env`).
4. **Ingest token (bridge lead/agenda):** `... ORG_ID=<id> node --import tsx scripts/put-ingest-token.ts` → te dá o token.
5. **Conectar WhatsApp:** dashboard → LEAF → Conectar WhatsApp → Aprovar (ATTESTATION) → escanear o QR com o número do tenant.
6. **Ofertas:** painel (LEAF → Ofertas) ou conversando com o Brann (`cadastrar_oferta`).
7. **Conhecimento:** conversando com o Brann (`adicionar_conhecimento`) — quando o S3 (RAG) fechar.

## ⚠️ Caveat do número +55 53 9133-8911
Está HOJE na Callima da **ai-stack** (:8080, produção viva). Um número WhatsApp pareia com **UMA** instância Evolution por vez → parear no **trunk** (:8081) **desliga** a Callima interina desse número. Recomendo:
- **Agora (trunk ainda incompleto):** pilotar o trunk com um número de **teste**; manter o +5553 na ai-stack (produção não cai).
- **Quando o trunk chegar em paridade** (S2 TTS + S3 RAG + S4 handoff): **cutover** do +5553 ai-stack → trunk (aposenta o interino do Ginkgo). Decisão sua.

## Checklist de teste ponta-a-ponta (por piloto)
**Secretária (WhatsApp):** texto ✓ · áudio-in (STT ✓) · áudio-out (TTS, S2) · entende fundamentada (RAG, S3) · qualifica → lead no CRM · agenda → evento + tela Agenda · vende → link certo (Stripe/Pix) · handoff → alerta o dono + inbox (S4). honest-data em tudo.
**Dashboard:** inbox (conversa espelhada, áudio tocável) · CRM (mover lead) · Ofertas · Agenda · balão do Brann.
**Assistente (Brann):** configurar por conversa (persona/oferta/conhecimento/ligar) · operador (conectar/ligar).

## Roteiro do vídeo-demo (ordem de gravação)
1. **Onboarding:** dono conversa com o Brann → configura a Callima (persona + oferta + conhecimento) + liga.
2. **Texto:** cliente manda texto no WhatsApp → Callima entende, responde, oferece.
3. **Áudio:** cliente manda áudio → Callima transcreve (S1) e responde por voz (S2).
4. **Handoff:** cliente pede algo fora do escopo → handoff → dono recebe alerta → assume no inbox (S4).
5. **Painel:** lead novo no CRM, agendamento na Agenda, conversa no inbox — dados vivos honestos.
6. **Multi-tenant:** mostrar o 2º piloto (outra Callima, outra persona/ofertas) — **mesma engine**.

## Gates (o que falta pra rodar tudo ao vivo)
S2 (TTS) em curso · S3 (RAG) + S4 (handoff) a seguir · 4 chaves no cofre por org · números pareados · stack no ar. Antes disso, tudo roda honesto/fail-closed (a demo completa espera o loop de áudio+RAG+handoff fechar).
