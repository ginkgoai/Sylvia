# WAVE — benchmark My Wiser + hipótese de produto (PARKED, pós-LEAF)

> 2026-07-03. Clip do fundador: https://app.mywiser.com.br/lp — engenharia reversa + ângulo de produto pra WAVE. **Parked** por North Star §7 (nada de 2ª frente antes do LEAF margear). Teardown de 1ª passada (a LP é SPA client-rendered; teardown profundo via Chrome quando abrir a frente).

## O que é My Wiser
- Categoria: **execução de Google Ads com IA** — "Você clica, a My Wiser cria" / "Sistema de Execução VPC para Google Ads".
- **4 pilares:** (1) análise de produtos, (2) criação de anúncios/criativos, (3) gerador de páginas (LP), (4) análise de métricas.
- Posicionamento: autopilot de performance (e-commerce/afiliado) — do produto ao criativo à página à métrica num fluxo só.
- Tell técnico: `storage.googleapis.com/gpt-engineer-file-uploads` → SPA gerada no Lovable/gpt-engineer; provável thin-layer sobre API de Ads + LLM. (= o "protótipo shippado" que nossa doutrina de design critica.)

## Fronteira de produto (confirmada pelo fundador — 2026-07-03)
- **PYRE = criação (o QUÊ):** imagem, vídeo, carrossel, apresentação, edição, copy, hashtag, descrição — tudo que chega ao público visualmente.
- **WAVE = distribuição + performance (ONDE/COMO/QUANDO + medição):** mídia **paga E orgânica**, agendamento, canais, tracking, analytics, gestão de verba.
- **LEAF = conversão/atendimento:** fecha no WhatsApp.
- **Fluxo:** PYRE cria o ativo → WAVE distribui/impulsiona/mede → LEAF converte. **Seam:** a landing/ativo é *output do PYRE*, *superfície de distribuição do WAVE* e *porta de entrada do LEAF*.
- My Wiser é um **bundle vertical** (cria + distribui + mede) que nós **separamos de propósito** — single-responsibility + honest-data. O benchmark do WAVE é só a metade "distribuição + métrica" dele.

## Onde a doutrina ganha (diferencial vs My Wiser)
- **Honest-data:** o calcanhar de "IA cria ads" é **alucinar número**. WAVE separa IA (propõe criativo/página/lance) de sistema (**ingest REAL do Google Ads/GA**); só afirma métrica provada. Nunca "deu certo" sem evidência.
- **Gasto governado (money = R3 → HITL):** criar campanha / mexer em verba = execução atrás de `Offer`/Boundary, com **aprovação humana do gasto**. My Wiser provavelmente executa direto → risco de queimar verba. Nós = governança de orçamento.
- **Multi-tenant + BYO:** conta de Ads/pixel por tenant; enterprise BYO (chaves próprias de Ads/LLM) — já temos o modelo.
- **Sinergia de suíte:** PYRE gera a landing/criativo → WAVE distribui e mede → o lead cai no **WhatsApp da LEAF** (a Callima fecha). Wiser é ilha; a suíte é funil.
- **Reuso da engine:** WAVE **consome o ativo do PYRE** (não gera criativo — ele coloca, agenda e mede). Tudo skills governadas na mesma engine.

## Pilares da WAVE (distribuição + performance)
análise de canal/audiência → agendamento/publicação (**pago + orgânico**) → tracking honesto (pixel/UTM/GA/Ads) → analytics → sugestão de otimização (**HITL no gasto**). *Criativo e landing vêm do PYRE.*

## Próximo passo
Confirmar o que é o WAVE. Teardown profundo (Chrome: features, pricing, fluxo, stack) **quando o LEAF margear**.
