# Ginkgo — Índice de Specs e Roadmap (mapa mestre)

Visão geral de tudo que está specado, status e ordem. Atualizar a cada entrega.
Convenção de status: ✅ feito · 🔧 em build (Claude Code) · 📋 specado (na fila) · ⛔ bloqueado (founder).

## Arquitetura
- Suíte (1 login → apps Leaf/Wave/Pyre, carteira GTK única, governança Laplace) → `suite_arquitetura_spec.md`
- Roster de agentes: Leaf=Brann · Pyre=Nyra · Wave=Alfred · Callima=secretária do cliente → `roster_agentes_ginkgo.md`
- Visão/loop do ecossistema → `ecossistema_ginkgo_visao.md`

## Ordem de build (uma spec por vez pro Code)
| # | Item | Spec | Status |
|---|------|------|--------|
| 1 | Suite Shell + App Switcher | suite_arquitetura_spec.md | 📋 |
| 2 | Leaf · Inbox | inbox_spec_claudecode.md | 🔧 feat/inbox-v1 |
| 3 | Leaf · Funil/Kanban | crm_funil_spec_claudecode.md | 📋 |
| 4 | Leaf · demais seções (Callima/KB/Mídia/Canais) | app_leaf_spec.md | 📋 |
| 5 | Planos tokenizados + /pricing (GTK) | pricing_impl_claudecode.md | 📋 |
| 6 | Wave MVP (tráfego/atribuição) | app_wave_spec.md | 📋 ⛔ APIs ads |
| 7 | Pyre MVP (estúdio) | app_pyre_spec.md | 📋 ⛔ Postiz/HeyGen |
| 8 | Site institucional (repo separado) | site_institucional_spec_claudecode.md | 📋 (paralelo) |

## Dependências do founder (destravam itens)
- WhatsApp Cloud API / portfólio Meta (CNPJ+verificação) → Canais oficiais + Wave (APIs de ads).
  Detalhe: `meta_portfolio_requisitos.md`.
- Stripe USD/global → billing dos planos.
- Fix Postiz (Elasticsearch) → Pyre Content Engine.
- Créditos OpenRouter/ElevenLabs → calibrar tabela GTK→custo (margem).

## Modelo de preço (CONFIRMADO)
Leaf $79/$199/$499 · Wave $99/$249 · Pyre $99/$249 · Full $599 · top-ups GTK · anual −17% · USD.
Detalhe: `pricing_tokenizado_ginkgo.md`.

## Ritmo de trabalho
Founder envia 1 spec pro Claude Code → manda print da resposta → Sexta-feira(eu) revisa e
prepara o próximo prompt. Uma de cada vez, PRs limpos, branch local até decidir publicar.
