# Piloto 1 — Ginkgo · Callima · Kit de onboarding (self-serve, pronto pra colar)

> 2026-07-01. Conteúdo pronto pra rodar o onboarding do jeito real (como um usuário faria): signup → conectar WhatsApp → configurar a Callima conversando com o Brann → ligar. Behind-the-curtain (white-label, o usuário não vê): 4 chaves de provider no cofre (put-secret).

## 1. Signup (web)
- **Org:** `Ginkgo AI Systems` · e-mail/senha (você define). → anota o `ORG_ID`.

## 2. Persona da Callima *(colar no Brann: "Configure a Callima com esta persona: …")*
> Você é a Callima, a secretária virtual da Ginkgo AI Systems no WhatsApp. Atende quem chega interessado no LEAF (a secretária de IA que atende, entende e vende no WhatsApp do cliente). Seu trabalho: acolher, entender a necessidade, explicar o LEAF de forma simples, qualificar (que negócio a pessoa tem, qual dor de atendimento), **agendar uma demonstração** quando houver interesse, e **mandar o link do plano certo** quando a pessoa quiser assinar. Tom caloroso, claro e direto, sem juridiquês nem promessa exagerada. Fale em pt-BR. **Nunca afirme o que não aconteceu** (não diga "agendei" sem o evento criado, nem "pagamento confirmado" — a confirmação vem pelo sistema). Se não souber algo, diga que vai verificar. Se a pessoa pedir um humano ou fugir do escopo, passe para a equipe.

## 3. Ofertas — planos reais *(Brann: `cadastrar_oferta`, ou painel LEAF → Ofertas)*
> Links + valores REAIS (BRL, 14 dias grátis), fonte `apps/api/src/billing/catalog.ts` — são os que a Callima já usa hoje.

| Nome | Preço/mês | Link (real) | Descrição (o que a Callima fala) |
|---|---|---|---|
| **Leaf** | R$ 449 | https://buy.stripe.com/6oUcN74Mtcgbamfghqgbm03 | Atendimento + CRM · Callima no WhatsApp (texto+áudio) · funil de leads. |
| **Pyre** | R$ 899 | https://buy.stripe.com/fZu9AV4Mtfsn65Zd5egbm0a | Social Media (Nyra) · conteúdo diário, roteiros, calendário · 14d grátis |
| **Wave** | R$ 1.199 | https://buy.stripe.com/eVq9AV92Jfsn0LFfdmgbm09 | Tráfego pago (Alfred) · testa/otimiza campanhas 24/7 · 14d grátis |

*(Suite: Pyre R$899 `…/fZu9AV4Mtfsn65Zd5egbm0a` · Wave R$1.199 `…/eVq9AV92Jfsn0LFfdmgbm09` · Sinal R$100 avulso `…/4gM9AVgvbfsngKD6GQgbm05`. Pro demo do Ginkgo, Leaf é a oferta-âncora.)*

## 4. Conhecimento (RAG) *(Brann: `adicionar_conhecimento` — colar cada bloco; entra quando o S3 fechar)*
- **O que é o LEAF:** o LEAF é uma secretária de IA (a Callima) que atende no WhatsApp do cliente — entende texto e áudio, responde, qualifica, agenda e vende, com um painel (inbox + CRM) onde o dono vê tudo e configura conversando com o Brann.
- **O que a Callima faz:** responde 24/7 por texto e voz; entende áudio; agenda no Google Calendar; manda o link de pagamento certo; passa pro humano quando precisa — sempre honesto (nunca inventa status).
- **Como o cliente começa:** assina um plano → conecta o WhatsApp dele (QR) → configura a Callima falando com o Brann (nome, jeito de falar, ofertas, conhecimento) → liga. Sozinho, pelo painel.
- **Preços:** à la carte Leaf R$449 · Pyre R$899 · Wave R$1.199 (mês, 14d grátis, **sem Full**) · Sinal R$100 avulso; top-ups de GTK (USD).
- **Diferencial:** governança e honest-data — a Callima nunca afirma o que não aconteceu; tudo é auditável no painel. Multi-tenant: cada cliente tem a própria Callima, isolada.
- **Agendamento:** a Callima marca a demo/atendimento e o evento cai no Google Calendar; a agenda aparece no painel.
- **Áudio:** o cliente pode mandar áudio; a Callima entende e pode responder por voz.

## 5. Ligar + conectar WhatsApp
- No painel: LEAF → **Conectar WhatsApp** → Aprovar (ATTESTATION) → escanear o QR.
- **Ligar a Callima:** pelo Brann ("pode ligar") — ato isolado, honest-data.

## 6. Número (decisão)
- O +55 53 9133-8911 está na Callima da **ai-stack** (produção). Ver `leaf_pilotos_setup_demo.md` → *Caveat do número*: pra o trunk, ou um **número de teste** agora (mantém a produção) **ou cutover** do +5553 (interino cai). Recomendo teste até o trunk fechar S2+S3+S4; cutover depois.

## Pré-provisionamento behind-the-curtain (platform-side, 1x)
4 chaves no cofre por org (`put-secret`): `evolution_api_key` · `openrouter_api_key` · `groq_api_key` · `elevenlabs_api_key`. + `AgentProfile.voiceEnabled=true` (pro TTS) + `put-ingest-token`.

## O que preciso de você pra fechar o kit do Ginkgo
1. ~~Payment Links~~ ✅ resolvido (catalog.ts, BRL, links reais).
2. **Número:** teste agora; cutover das instâncias pro trunk depois, passo a passo (decidido).
3. (quando o S3 RAG fechar) rodar o `adicionar_conhecimento` com os blocos acima.
