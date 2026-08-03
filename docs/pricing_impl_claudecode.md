# LEAF — Spec: Planos tokenizados + /pricing (Claude Code)

Implementar DEPOIS do Inbox e do Kanban (evita conflito de branch). Valores em
`C:\sexta-feira\docs\pricing_tokenizado_ginkgo.md` (CONFIRMADO). Cobrança USD via Stripe.

## 1. Seed `plans` (migration nova; substitui basic/pro/enterprise)
Criar: leaf-starter, leaf-pro, leaf-scale, wave-base, wave-pro, pyre-base, pyre-pro, full.
- `price_monthly` em USD: 79,199,499 / 99,249 / 99,249 / 599.
- `limits` jsonb: { product:'leaf'|'wave'|'pyre'|'full', tier, token_monthly (=GTK),
  whatsapp_instances, agents, leads, team_members, knowledge_files, channels, features:[] }.
  Leaf: 8000/25000/70000 GTK; números 1/1/3; agentes 1/3/-1; leads 1000/10000/-1;
  users 1/5/15; KB 5/50/200. Wave 6000/20000. Pyre 8000/25000. Full 70000 (pool).
- Manter compat: organizations.plan referencia plans.name (já é FK).

## 2. Config de custo GTK por ação (parametrizável sem deploy)
- Nova tabela `gtk_costs` (action text pk, gtk numeric, notes) OU jsonb em settings global.
- Seed inicial (calibrar depois): text_reply 1, media_transcribe 3, tts_reply 8,
  content_post 10, content_image 25, content_motion 80, ad_copy 10.
- `tokenRouter` debita GTK por ação consultando essa config (não hardcode).

## 3. Top-ups + carteira
- Pacotes: 5000/$25, 15000/$60, 50000/$175 (Stripe one-time). Credita em token_wallets
  com flag de origem ('plan'|'topup') e validade (ativo enquanto subscription ativa).
- Travas: alerta 80%, **pausa de ações de IA em 100%** (retorna estado p/ UI), auto-recharge
  opcional (flag por org). Nunca debitar além do saldo (sem prejuízo).

## 4. /pricing (apps/web/app/pricing)
- 4 cards: Leaf (3 tiers toggle), Wave (2), Pyre (2), Full (bundle, destaque "mais popular").
- Mostrar GTK/mês, principais limites, e bloco de top-ups. Toggle mensal/anual (−17%).
- Identidade dark navy via tokens; CTA "Começar teste" → checkout Stripe (USD).
- /planos do site institucional reusa os mesmos dados.

## Aceite
- Seed aplica; /pricing mostra os 8 planos reais com GTK e preços USD; toggle anual; lint/build OK.
- tokenRouter lê gtk_costs; saldo pausa em 100%; top-up credita. Sem regressão no billing atual.
