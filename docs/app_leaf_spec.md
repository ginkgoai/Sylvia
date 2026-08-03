# App LEAF — Atendimento + CRM (agente Brann · secretária Callima)

Acento verde. Rotas sob `/(dashboard)/leaf/...`. Lê schema existente (conversations, messages,
leads, whatsapp_instances, workspace_assistants, knowledge_files, media_assets, appointments).

## Seções (sidebar do app Leaf)
1. **Visão geral** — KPIs de atendimento: conversas abertas, tempo de resposta, % IA vs humano,
   leads novos, conversões, próximos agendamentos. Estados loading/empty/error.
2. **Inbox** (Central de Atendimento) — 3-pane. Spec: `inbox_spec_claudecode.md`. (em build)
3. **Funil / CRM** — Kanban multi-funil. Spec: `crm_funil_spec_claudecode.md`. (em build)
4. **Callima** (secretária) — config do `workspace_assistants`: persona, nicho, skills
   (schedule/payment/qualification/followup), voz (ElevenLabs), handoff, horário, filtros,
   kill-switch (pausar). É a "sua secretária de IA" que o cliente personaliza.
5. **Base de conhecimento** — upload/gestão de `knowledge_files` (RAG da Callima): PDF/txt/
   url/faq, status de processamento.
6. **Mídia** — catálogo `media_assets` que a Callima envia (recebe peças do Pyre também).
7. **Agendamentos** — `appointments` (Google Calendar): lista/calendário, status.
8. **Canais** — conectar WhatsApp: hoje Evolution (QR), futuro **WhatsApp Cloud API oficial**
   (Embedded Signup) — ver `meta_portfolio_requisitos.md`. Status/quality rating/tier.

## Cruzamentos
- Wave cria lead/conversa (UTM) que aparece aqui. Pyre abastece a Mídia. Leaf marca venda
  (lead won + payment) que o Wave atribui. Brann opera; Callima fala com o cliente final.

## GTK
- Resposta de texto ~1, transcrição ~3, áudio TTS ~8 (tabela `gtk_costs`). Debita o saldo único.

## Aceite
- Cada seção com dados reais, estados completos, responsivo, identidade verde, lint/build OK.
- Inbox e Kanban conforme suas specs; Callima salva config e kill-switch funciona.
