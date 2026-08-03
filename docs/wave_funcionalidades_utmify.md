# Wave — Funcionalidades (referência: Utmify)

Utmify = ferramenta #1 de **tracking/atribuição de vendas para tráfego pago** (Meta/Google/
TikTok Ads). Mapeio o que aplicar ao **Wave** (agente de tráfego/ADS da Ginkgo).

## O que a Utmify faz
- **Atribuição de vendas por campanha/anúncio/criativo** via parâmetros UTM + pixel próprio.
- **Trackeamento server-side** (estilo Conversions API) → dados precisos mesmo com perda de
  cookie/iOS; alimenta a otimização das campanhas.
- **Dashboard de KPIs** de campanha (gasto, vendas, CPA, ROAS, ROI, lucro). Múltiplos dashboards.
- **Gestão de tráfego "automática"**: ver vendas por campanha e otimizar **pelo próprio
  relatório, sem abrir o Facebook**.
- **App mobile**. Suporte/consultoria.
- **Integrações**: redes de anúncio (Meta, Google, TikTok) + checkouts/pagamentos
  (Hotmart, Kiwify, Shopify, Stripe, PerfectPay, Eduzz, Cartpanda, Ticto, Braip, etc.).
- **Preço por volume de vendas** (limite = vendas aprovadas; recusada/reembolso/chargeback
  não conta).

## Como aplicar ao Wave
Wave deixa de ser só "agente de ADS" e vira **inteligência de tráfego + atribuição + otimização**:
- **Wave Track** — atribuição server-side: liga gasto de anúncio → clique (UTM) → **lead no
  WhatsApp → card no CRM → pagamento**. (Ver diferencial abaixo.)
- **Wave Dashboard** — KPIs por campanha/anúncio/criativo: gasto (puxado das APIs de ads) +
  receita (da nossa tabela `payments`) → CPA, ROAS, ROI, lucro. Múltiplos dashboards.
- **Wave Optimize** — o agente recomenda/age: pausar perdedores, escalar vencedores,
  realocar verba — com **HITL** (aprovação). É a "gestão automática" com governança.
- **Wave CAPI** — envia eventos de conversão (lead/venda) de volta pro Meta/Google/TikTok
  (server-side) pra alimentar o algoritmo deles — precisão sem depender de cookie.

## Diferencial Ginkgo (por que o Wave SUPERA a Utmify)
A Utmify só sabe a receita se você integrar o **checkout** — ela vê venda de infoproduto/
e-commerce. A Ginkgo **é dona da conversa (Leaf/Callima) + CRM + pagamento**. Então o Wave
atribui até **vendas de alto ticket fechadas no WhatsApp** (sem checkout), não só compras em
página. O loop fica nativo: anúncio → wa.me com UTM → lead → conversa → card ganho → pagamento,
tudo no mesmo banco. Isso é atribuição que a Utmify não consegue fazer.

## Mapeamento técnico
- **Captura de UTM**: link de entrada (wa.me / landing) carrega utm_source/medium/campaign/
  content/term → grava no lead (usar `leads.source` + novos campos utm em `custom_fields`).
- **Ingestão de gasto**: Meta Marketing API, Google Ads API, TikTok Marketing API (ler
  campanhas, gasto, métricas). Depende de acesso de anúncio (liga com o portfólio Meta).
- **Receita**: já temos `payments` + leads "won" → casar com a campanha de origem.
- **Server-side / CAPI**: Meta Conversions API (e equivalentes) enviando eventos de conversão.
- **Cálculo**: ROAS = receita atribuída / gasto; ROI; CPA = gasto / leads; por campanha/criativo.
- UI no /dashboard (nova área "Wave" / tráfego). Mobile depois.

## Custo GTK
- Tracking/atribuição = **infra** (não é LLM pesado) → entra como **feature do plano**, não
  metered por GTK. O que consome GTK no Wave: **análise/recomendações da IA** (Wave Optimize),
  geração de copy/criativo de anúncio (~10 GTK), relatórios narrados. Plano Wave Base $99 (6k
  GTK) / Pro $249 (20k GTK) — já definido.

## MVP do Wave (ordem) — depois do P0 do LEAF
1. **Captura UTM + atribuição básica** (anúncio→lead→venda no nosso banco) — fundamento, baixo custo.
2. **Wave Dashboard** (ROAS/ROI/CPA por campanha) — puxa gasto via Meta Marketing API.
3. **Wave CAPI** (eventos server-side de volta pro Meta) — precisão.
4. **Wave Optimize** (recomendações/ações da IA com HITL) — o "uau".
+ Google/TikTok ads depois do Meta.

## Pendências / dependências
- **Acesso às APIs de anúncio** (Meta Marketing API primeiro — casa com o portfólio Meta que
  já está no caminho crítico; depois Google/TikTok).
- Confirmar com founder se Wave entra após P0 do LEAF (provável) ou em paralelo.
- Preço: mantemos GTK + plano (Wave $99/$249). Modelo "por volume de vendas" da Utmify fica
  como métrica de referência, não copiamos.


---
## Agente: ALFRED (persona do Wave)
Alfred opera o tráfego: Track (atribuição), Dashboard (ROAS/ROI/CPA), CAPI, Optimize (HITL).
