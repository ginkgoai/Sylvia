# App WAVE — Tráfego / Atribuição (agente Alfred)

Acento azul. Rotas sob `/(dashboard)/wave/...`. Base: `wave_funcionalidades_utmify.md`.
Diferencial: atribuição nativa anúncio→WhatsApp→CRM→pagamento (dono do loop).

## Seções (sidebar do app Wave)
1. **Visão geral** — gasto, receita atribuída, ROAS, ROI, CPA, lucro (período). Por conta de anúncio.
2. **Campanhas** — lista de campanhas/conjuntos/anúncios com métricas + venda atribuída por
   criativo. Filtros por rede/período. Drill no criativo.
3. **Atribuição (Track)** — visão do funil: clique (UTM) → lead → conversa → card → pagamento.
   Mostra origem de cada venda. (UTM gravado no lead via `custom_fields`.)
4. **Otimização (Alfred)** — recomendações da IA (pausar perdedor, escalar vencedor, realocar
   verba) com **HITL** (aprovar/recusar). Ações registradas em governança.
5. **CAPI** — config de eventos server-side de conversão pro Meta/Google/TikTok.
6. **Conexões** — conectar contas de anúncio: **Meta Marketing API** (1º), depois Google/TikTok.

## Dados
- Gasto/métricas: APIs de anúncio (Meta Marketing API primeiro). Receita: `payments` + leads
  "won" casados com a campanha de origem. Cálculo ROAS/ROI/CPA no `apps/api`.

## GTK
- Tracking/atribuição = **feature do plano** (infra, não metered). GTK só em IA: Optimize
  (análise/recomendação), copy/criativo de anúncio (~10), relatórios narrados.

## Dependências
- Acesso às APIs de anúncio (casa com o portfólio Meta — `meta_portfolio_requisitos.md`).
- Implementar após P0 do LEAF. MVP: Track/UTM → Visão geral(ROAS) → CAPI → Otimização.

## Aceite
- Conectar conta Meta; ver ROAS/CPA reais por campanha; atribuição mostra origem da venda;
  Optimize sugere e aplica com HITL; estados completos; identidade azul; lint/build OK.
