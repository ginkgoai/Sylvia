# Gap Analysis — Helena CRM × LEAF CRM (2026-06)

Cruzamento do produto Helena (concorrente BR de CRM-WhatsApp) com o LEAF real
(schema.sql + 13 módulos da API + 9 telas do dashboard). Foco: o que **falta** e o
que **ajustar** no LEAF — priorizado pro modelo de negócio Ginkgo (vende agentes de
IA direto pra PME; White Label é jogada futura, não core).

## O que o LEAF JÁ tem (e onde lidera)
- Multi-tenant real (organizations/memberships/roles owner→viewer, tenantContext, RLS).
- Inbox no banco: conversations + messages (status bot/human/resolved/waiting, assigned_to, unread).
- CRM-IA: leads (status, intent_score, ai_summary, tags, custom_fields, source), interactions.
- Agentes: agents (+versions) + workspace_assistants (secretária por tenant, kill-switch,
  handoff_config, scheduling/payment/followup/filter/response configs).
- IA: RAG (knowledge_files + ragEngine), aiGateway/gemma/replyGenerator, **tokenRouter +
  token_wallets/token_ledger** (cobrança por uso — moat que a Helena NÃO tem).
- HITL/governança (hitlManager, brann actions) — o "Assumir" do Laplace, já no backend.
- Pagamentos: payment_links + payments (Stripe + Stripe Connect por org).
- Agendamento: appointments + googleCalendarManager. Mídia: media_assets (catálogo).
- Billing/planos (basic/pro/enterprise), onboarding, webhooks, n8n.
- Telas: dashboard, admin, assistant, automations, billing, crm, inbox, media, studio.

Resumo: o LEAF é **AI-native** e em vários pontos mais sofisticado que a Helena
(tokenomics, kill-switch, souls/agentes versionados). O que falta é "músculo de CRM
operacional" (fila/times, funil flexível) e canais oficiais.

## GAPS priorizados

### P0 — Table-stakes (sem isto não compete / não é usável)
1. **Inbox UI 3-pane** (em construção pelo Claude Code). Backend já existe.
2. **WhatsApp Oficial (Meta Cloud API / BSP).** Hoje = Evolution/Baileys (não-oficial,
   risco de ban). Helena é Meta BSP. → migrar p/ API oficial (founder já no portfólio Meta BR).
3. **Funil de CRM flexível.** Hoje leads.status é enum FIXO (1 funil implícito). Falta:
   tabelas `pipelines` + `pipeline_stages` (múltiplos funis, etapas customizadas) e Kanban
   na tela /crm. Helena tem múltiplos funis + etapas livres.
4. ~~Pix + boleto~~ → **Reclassificado (decisão founder 2026-06): comercialização GLOBAL,
   cobrança em USD.** Logo **Stripe (USD, cartão global, multi-moeda) é o CORE correto** — já
   está no LEAF. Pix/boleto viram **add-on regional BR (P1/opcional)**, não bloqueiam o produto.
   Ação: garantir Stripe em modo USD/multi-currency + checkout internacional; Pix depois.
5. **Filas + distribuição automática + transbordo + Times/Setores.** Hoje só `assigned_to`.
   Falta: tabela `teams`/`queues`, round-robin, transferência por timeout, visibilidade por
   equipe. Essencial p/ contas com vários atendentes (plano Pro+).

### P1 — Diferencia e escala
6. **Respostas rápidas/templates** (canned) + **notas internas por conversa**.
7. **Campanhas/disparos em massa** (outbound segmentado por tag/campo + agendado) +
   relatório de campanha. Hoje: inexistente.
8. **Relatórios/Analytics**: tempo de atendimento, produtividade por atendente, conversão
   do funil, exportação. Hoje: dashboard básico só.
9. **Orquestração multi-agente + Agente Supervisor** (roteia intenção entre agentes numa
   conversa) — casa com a visão Laplace/Hermes. + expandir skills do agente (criar card,
   etiquetar, chamar API/MCP).
10. **Importação de contatos (CSV)** + rastreio de origem/visita do site.

### P2 — Estratégico / futuro
11. **Canais Instagram + Messenger** (omnichannel de verdade).
12. **Builder de chatbot/automação no-code dentro do produto** (hoje depende de n8n —
    ok pra nós, ruim pra cliente final).
13. **White Label / revenda** (marca, domínio, app próprio, gerenciador de contas) —
    linha de receita futura, NÃO core agora.
14. **App mobile nativo.** 15. **API pública/parceiro + servidor MCP** documentados.

## Ordem recomendada (encaixando no que já roda)
1. Inbox UI (já solto). 2. Funil flexível (pipelines/stages + Kanban) — emenda direto na
   tela /crm. 3. WhatsApp Oficial + Pix/boleto (dependem de você: Meta BR + OpenPix).
4. Filas/Times. 5. Campanhas + Relatórios. 6. Supervisor multi-agente.

## Ajustes pontuais (rápidos)
- `/dashboard/settings` 404 → criar Configurações (workspace_assistants + perfil + plano).
- /pricing: planos reais Leaf/Wave/Pyre/Full (hoje basic/pro/enterprise genéricos).
- leads.channel já prevê instagram/telegram/web mas só WhatsApp está ligado — sinalizar "em breve".
