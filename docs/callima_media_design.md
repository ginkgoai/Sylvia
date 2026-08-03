# Callima — Mídia (entrada + saída)

Spec do template Callima para **entender** qualquer mensagem recebida e
**enviar** mídia (catálogo etc.). Aplicar junto com a virada para OpenRouter.

## ENTRADA — "Entender Mídia" (refactor)
Hoje: uma branch por tipo (áudio→OpenAI, imagem→OpenAI, vídeo→Gemini,
documento→Anthropic). Funciona, mas usa 3–4 provedores = 3 credenciais,
3 faturas, 3 rate-limits e muitos nós por clone.

**Alvo:** colapsar em **1 etapa multimodal**.
- Imagem / vídeo / documento(PDF) / sticker → **1 modelo multimodal**
  (Gemini 2.x flash via OpenRouter) com prompt
  "descreva/extraia o que importa desta mídia para a secretária responder".
- Áudio → **Whisper** (transcrição literal, barata) — ou o mesmo multimodal.
- Saída sempre vira **texto** → `Text Final` → agente (igual hoje).

**Governança/custo (mídia é cara):** medir, cap de tamanho, flag por plano
("entende mídia" como feature paga), vídeo limitado (clipe curto / só áudio),
sticker → normalmente só mapear "[figurinha]" sem gastar IA.

## SAÍDA — sub-workflow "Enviar Mídia" (catálogo etc.)
Espelha o padrão do `AUDIO FEM`.
- **Input:** org/instância + contato (remoteJid) + rótulo/id da mídia.
- **Faz:** busca em `media_assets` da org (biblioteca criada pelo LEAF) →
  pega URL no Supabase Storage → **Evolution `sendMedia`** para o contato.
- **Exposto como TOOL** da Callima → ela envia em tempo real quando o
  cliente pede ("manda o catálogo").

### Dois caminhos, uma biblioteca
- **Callima (ao vivo):** envia mídia **já aprovada** na `media_assets`,
  sem HITL — é atendimento normal.
- **Brann (blast):** promo/catálogo para um segmento via
  `brann_actions` (`send_media`) **com HITL** → consumer envia.
- Ambos usam a **mesma `media_assets`**.

## Tools da Callima — revisão
- Manter: RAG (`base_conhecimento`), Postgres Memory, Think, Calculator,
  Calendar (agendar), Stripe (link de pagamento, **com HITL/guardrail**).
- Gmail: opcional (canal da secretária é WhatsApp).
- Remover `AUDIO` como tool (o bloco `[[AUDIO]]` + a saída já cuidam).
- **Adicionar:** tool "Enviar Mídia" (acima).

## Status
- ENTRADA refactor: **desenhado**, aplicar com OpenRouter.
- SAÍDA "Enviar Mídia": **desenhado**, construir com OpenRouter
  (precisa de instância Evolution real por org para testar `sendMedia`).

## SAÍDA — IMPLEMENTADO + VALIDADO (2026-06-17)
Workflow **ENVIAR MIDIA** (id `oeAXd3LE30lzOIor`) reescrito (TTS removido):
- `Start` (executeWorkflowTrigger; inputs: instance, phone, media, caption) — p/ uso como tool.
- `Test Webhook` (POST /webhook/enviar-midia-test) — só p/ validação.
- `Prep` (Set) — normaliza body/json → instance/phone/media/caption.
- `Evolution Send Image` (evolutionApi, op `send-image`, cred Evolution `tWl4eIzULkFUsVvg`).
- Conexões: Start→Prep, Test Webhook→Prep, Prep→Evolution.

**Teste real:** POST no webhook com imagem pública → Evolution `success:true`,
`imageMessage` enviada à instância **CALLIMA** (open) p/ `555391338911`. ✅

### Próximas extensões (sem urgência)
- `send-document` / `send-video` (irmãos do `send-image`) p/ PDF/vídeo.
- Resolver **rótulo→URL** via `media_assets` (Supabase) ANTES do envio (camada por org).
- Remover o `Test Webhook` antes de clonar p/ produção (deixar só o `Start`).
