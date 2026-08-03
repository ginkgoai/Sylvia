---
tipo: plano
agente: callima
status: ativo
atualizado: 2026-06-16
---

# Callima — Plano de Skills (features) + credenciais + guardrails

Regra: **ligar uma skill de ação sem testar é risco** no template-mestre. Por isso preparamos
cred/escopo agora e **ligamos+testamos cada uma quando o OpenRouter (modelo pago) entrar** — uma a
uma, isolada, com limite. (Hoje o LLM é Gemini free, em rate limit, então teste fica bloqueado.)

## Estado atual das skills do agente
- **Ativas:** RAG (`base_conhecimento_callima`), Áudio (`AUDIO FEM`), Think, Calculator, Stripe (ligado, com credencial).
- **Desativadas (a ligar):** Gmail (tem credencial), Google Calendar (sem credencial).
- **Removidas:** HubSpot (será substituído pelo CRM do LEAF) e **WhatsAuto** (redundante — Evolution já cobre o WhatsApp).

## As 4 features escolhidas
| Skill | Credencial | Guardrail | Status |
|---|---|---|---|
| **E-mail (Gmail)** | já existe no n8n | só envia quando o cliente pede; nunca em massa | pronta p/ ligar+testar |
| **Agendamento (Google Calendar)** | **Google OAuth (fundador gera)** | confirma antes de marcar; calendário específico | aguarda cred |
| **Pagamento (Stripe / OpenPix)** | Stripe já existe · **OpenPix App ID (fundador cria)** | só **gera link** (não cobra direto); valor da base; sem desconto; ideal confirmação humana | Stripe testável; Pix aguarda App ID |
| **Envio de mídia (catálogo/promo)** | hospedagem | só mídia da biblioteca do cliente | template: Evolution `sendMedia` por URL · definitivo: Supabase Storage por tenant (LEAF) |

## Credenciais que faltam (fundador fornece)
1. **Google OAuth** (Calendar) — Google Cloud Console → OAuth client → conectar conta no n8n.
2. **OpenPix App ID** — criar conta OpenPix/Woovi.
(Gmail e Stripe já têm credencial.)

## Sequência de ativação (quando o OpenRouter entrar) — menor risco → maior
1. **Gmail** (cred pronta) → 2. **Google Calendar** → 3. **Envio de mídia** → 4. **Pagamento** (com confirmação humana).
Cada uma: ligar o nó → testar isolada (caso feliz + erro) → só então a próxima.

## LLM
Trocar o nó `Gemini Brain` por **OpenRouter (modelo pago)** — o nó "OpenRouter Chat Model" já existe
no template (desativado). Resolve o rate limit que hoje gera o fallback "me perdi". Modelo sugerido:
`openai/gpt-4o-mini` ou `google/gemini-2.0-flash-001`.

## Multi-tenant (clone por cliente)
Cada skill usa a **credencial do próprio cliente** (e-mail dele, calendário dele, conta de pagamento dele).
No dogfood (usuário 1) são as do fundador; no LEAF SaaS vira config por tenant (`org_id`).
