# LEAF · Feature: Multicanal — Callima onde o cliente está

> Status: **spec** (build pós-core, mas o seam vale antecipar — ver sequência). Callima no **Messenger, Instagram DM** [+ webchat, e-mail depois] além do WhatsApp. Benchmark: ManyChat. Mantido pela Sexta-feira.

## Tese (por que é barato — doutrina IA↔sistema)
- A separação já torna a Callima **channel-agnostic**: ela interpreta e **emite intenção**; QUEM entrega é execução. O canal é **transporte trocável atrás de uma porta** (`ChannelPort`) — exatamente o roadmap #3 que a auditoria apontou como pulado.
- Logo multicanal **≠ reescrever a Callima**. É **um adapter por canal** + fluxo de conexão. Todas as skills (STT, TTS, RAG, agenda, ofertas, handoff, inbox) **reusam sem tocar**.
- **Bônus estratégico:** o `ChannelPort` também **mitiga o risco existencial do Baileys** (auditoria: "1 onda de ban derruba a base inteira"). Com N canais, um ban não mata o tenant. **Multicanal = crescimento + resiliência.**

## Arquitetura — ChannelPort
- **Inbound normalizado** (o que todo canal vira): `{ channel, orgId, externalThreadId, sender{externalId,name}, kind: text|audio|image|file, payload, receivedAt, raw }`.
- **Outbound normalizado** (o que a Callima emite): `{ channel, orgId, recipientExternalId, kind, text|mediaRef|buttons, replyToThread }`.
- **`ChannelPort`** = `inboundAdapter` (webhook do canal → normalizado) + `outboundAdapter` (normalizado → API do canal). A cognição **só conhece o normalizado**.
- Adapter atual: WhatsApp (Evolution) → **refatorar pra trás da porta sem mudar comportamento** (gate = paridade). Novos: Messenger, Instagram (mesma infra Meta).

## Adapters Meta (Messenger + Instagram DM)
- **Uma plataforma** (Meta Messenger Platform) cobre os dois: webhook de mensagens + Send API; o campo `channel` distingue.
- **Inbound:** webhook do app Meta → **verificar `X-Hub-Signature-256` (HMAC-SHA256 com o app secret)** — conserta a classe de bug que a auditoria achou no n8n (HMAC enviado mas nunca verificado) → normalizar → **rotear por page-id / ig-id → org**.
- **Outbound:** Send API (`POST /{page-id}/messages` com page access token). Áudio recebido = baixa o attachment via Meta → **mesma skill STT**. Mídia de saída = mesma pipeline TTS/mídia.
- **Setup/permissões (VERIFICAR na doc Meta vigente no build — nomes/versão mudam):** app Meta Business; permissões da família `pages_messaging`, `instagram_manage_messages`, `pages_manage_metadata`, `instagram_basic`; **App Review obrigatório p/ produção**; IG precisa ser conta **Professional** ligada a uma Página FB; a Página/objeto IG assinada ao webhook.

## Multi-tenant (conexão self-serve)
- Cada tenant conecta a **própria Página FB / conta IG** via **Meta Login (OAuth)** no dashboard → guardamos **page access token (long-lived) + page-id/ig-id no cofre (R3)** da org. Inbound roteado por page-id/ig-id → org (invariante #3; cross-tenant ⇒ 404).
- **White-label:** 1 app Meta da plataforma p/ todos (menor atrito; blast-radius mitigado por #9). **Enterprise BYO:** app Meta próprio do tenant (isolamento) — encaixa no tier BYO (`modelo_provedores_e_tiers.md`).

## Honest-data & governança de canal (o pulo do gato)
- Mesmas leis: `reply` só conta como **enviado após sucesso real na Send API** (Evidence). Sem fala-fantasma.
- **Janela de 24h da Meta:** freeform só ≤24h da última msg do usuário; fora disso só **message tag / template aprovado**. O sistema **conhece a janela** e **não finge** um envio que a Meta vai rejeitar — surface honesto ("fora da janela, preciso de template"). Honest-data **no transporte**.
- **Handoff × `human_agent` tag:** o handoff (S5) casa com a tag de atendimento humano do Messenger/IG (janela estendida) — pausa a IA e o humano responde dentro da janela permitida.
- HMAC verificado; segredos no cofre/redigidos (secretScopes); rate-limit + retry (reliability); egress allowlist dos domínios Meta.

## Modelo de dados (deltas)
- `Channel` enum: `whatsapp | messenger | instagram | webchat | email`.
- `ChannelAccount` (orgId, channel, externalId=page/ig, tokenRef→cofre, status, connectedAt).
- `Conversation.channel` + `externalThreadId`; `Message.channel`.
- **Identidade:** v1 = thread **por-canal**; **unificar contato** (mesma pessoa no zap + IG) = enhancement posterior (link por org + heurística), não bloqueia a feature.

## Inbox
- Conceitualmente já é channel-agnostic; add **badge de canal** + filtro. Assumir/devolver, handoff, "precisa de você" reusam.

## Sequência (fatias governadas · honest-data · testes — padrão PROCESSO auditoria·loop·tasks·coesão)
- **M-CH0 · ChannelPort seam:** extrair a porta; mover WhatsApp/Evolution pra trás dela **sem mudar comportamento** (gate = paridade). *Vale antecipar assim que o core fechar* — é a mitigação anti-Baileys e a fundação de tudo.
- **M-CH1 · Messenger:** webhook (verify HMAC) + normalizar + Send API + OAuth de conexão + cofre + badge na inbox. Texto primeiro; áudio/mídia reusa skills.
- **M-CH2 · Instagram DM:** mesma infra, conta IG Professional.
- **M-CH3 · Governança de janela:** conhecer 24h + tags/template + surface honesto; casar handoff com `human_agent` tag.
- **M-CH4 · Identidade unificada** (opcional): linkar contato cross-canal.
- *Futuro:* webchat widget, e-mail — mesmos moldes.

## O que o fundador provê
- **App Meta (Business) + App Review** das permissões — **é o gargalo de prazo** (Meta leva dias/semanas); decisão white-label (app da plataforma) vs BYO (app do tenant); **domínio HTTPS público** pro webhook (depende do deploy VPS #8, `ginkgosystems.tech`).

## Marco Meta — App Review ≠ Meta Partner (sequência, 2026-07-03)
- **Destrava técnico = App Review (Advanced Access).** `pages_messaging`/`instagram_manage_messages` num app Business aprovado. **Não exige Partner** — dá pra shippar pros pilotos só com App Review.
- **Meta Business Partner / Tech Provider = credencial EARNED operando** (produto vivo + clientes +, nas trilhas de ads, verba gerida). Vem **depois** e **amplifica** (limites, selo/diretório, confiança, co-venda) — não é pré-requisito.
- **Sequência:** core LEAF → App Review + multicanal (+ WAVE gerindo ads) → track record → **aplicar Meta Partner**. A feature multicanal + o WAVE **constroem o caso** pro Partner — relação de plataforma que serve LEAF **e** WAVE. (Especificidades do programa Partner: verificar na Meta vigente quando chegar a fase.)

## Não-metas (MVP da feature)
- Sem broadcast/campanha (isso é **disparo governado**, outra feature). Sem comentário→DM automation (fase 2). Sem unificação de contato no v1.

## Checklist de reuso (por que é barato)
STT ✓ · TTS ✓ · RAG ✓ · agenda ✓ · ofertas ✓ · handoff ✓ · inbox ✓ · cofre ✓ — **só entra transporte.**
