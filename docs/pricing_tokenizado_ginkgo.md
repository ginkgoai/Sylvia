# Ginkgo — Modelo de Pricing Tokenizado (USD) · proposta

Decisão founder (2026-06): cada produto tem um **plano-base acessível** que supre as
necessidades daquele corpo; **tudo tokenizado/parametrizado** para nunca dar prejuízo no
uso de APIs; allowance de tokens/mês explícita; **compra de tokens adicionais** (estilo Manus).
Âncora Leaf confirmada: **$79 / $199 / $499**. Wave/Pyre/Full: anchors PROPOSTOS (confirmar).

## Como o Manus faz (referência)
- Crédito por ação (chat simples 5–15; tarefa pesada 500–900).
- Plano-base com allowance mensal + **300 créditos/dia de refresh** (piso de uso).
- **Top-up packs** que ACUMULAM enquanto a assinatura está ativa (somem se cair p/ free).
- Tiers: Free 300/dia · $20/4k · $40/8k · $200/40k. Anual −17%.

## GTK — Ginkgo Token (unidade de cobrança)
- 1 GTK = unidade interna que abstrai custo de API/LLM/voz/imagem. O cliente vê "GTK", não
  tokens de LLM. Cada ação consome GTK por uma **tabela de custo** (parametrizável):
  - resposta de texto (atendimento): ~1 GTK
  - transcrição de áudio/imagem (multimodal): ~3 GTK
  - resposta em áudio (TTS ElevenLabs): ~8 GTK
  - geração de post/legenda (Pyre): ~10 GTK · imagem: ~25 GTK · motion/vídeo: ~80 GTK
  - copy/otimização de anúncio (Wave): ~10 GTK
  (valores RELATIVOS — calibrar antes do launch contra preço real OpenRouter/ElevenLabs.)
- **Regra de margem (trava):** preço de venda do GTK ≥ 3–4× o custo bruto de API por GTK.
  Allowance de cada plano dimensionada p/ o preço cobrir o custo no uso típico + sobra.

## Travas anti-prejuízo (parametrizadas)
- Alerta em 80% do allowance; em 100% **pausa novas ações de IA** e oferece top-up
  (nunca consome silenciosamente / nunca dá prejuízo).
- Auto-recharge opcional (cliente liga). Hard-cap por org configurável.
- Piso de preço por plano > custo fixo do tenant (número WABA + storage + infra).

## Planos (USD/mês · anual −17%) — proposta p/ o seed `plans`

### LEAF — Atendimento + CRM (Callima) — âncora confirmada
| Plano | Preço | GTK/mês | Nº WhatsApp | Agentes | Leads | Usuários | Arq. KB | Extra |
|------|------|--------|------|------|------|------|------|------|
| Leaf Starter | $79  | 8.000  | 1 | 1 | 1.000 | 1 | 5 | base |
| Leaf Pro     | $199 | 25.000 | 1 | 3 | 10.000 | 5 | 50 | filas/times |
| Leaf Scale   | $499 | 70.000 | 3 | ilimitado | ilimitado | 15 | 200 | prioridade |

### WAVE — Tráfego/ADS (anchors a confirmar)
| Plano | Preço | GTK/mês | Contas de anúncio | Usuários |
|------|------|--------|------|------|
| Wave Base | $99  | 6.000  | 1 | 2 |
| Wave Pro  | $249 | 20.000 | 3 | 5 |

### PYRE — Conteúdo (anchors a confirmar)
| Plano | Preço | GTK/mês | Canais sociais | Posts/mês* |
|------|------|--------|------|------|
| Pyre Base | $99  | 8.000  | 2 | ~30 |
| Pyre Pro  | $249 | 25.000 | 5 | ~100 |
*posts dependem do mix texto/imagem/motion (consome GTK pela tabela).

### FULL — Ecossistema (bundle Leaf+Wave+Pyre, nível Pro)
- Soma dos Pro ≈ $697/mês. **Full = $599/mês (−14%)** com **pool de GTK compartilhado
  ~70.000/mês** entre os três + prioridade + onboarding assistido.

## Top-up de GTK (acumula enquanto assinatura ativa — modelo Manus)
- +5.000 GTK = $25 · +15.000 GTK = $60 · +50.000 GTK = $175 (preço/GTK cai com volume,
  sempre acima do custo → margem). Só usável com assinatura paga ativa.

## Mapeamento no banco (`plans` + config)
- `plans`: criar Leaf Starter/Pro/Scale, Wave Base/Pro, Pyre Base/Pro, Full. Campos:
  `price_monthly` (USD), `limits` jsonb { token_monthly(=GTK), whatsapp_instances, agents,
  leads, team_members, knowledge_files, channels, features:[...] }.
- Nova config de **tabela de custo GTK por ação** (jsonb em settings ou tabela própria) —
  parametrizável sem deploy.
- `token_wallets`/`token_ledger` já existem → vira o saldo/extrato de GTK. tokenRouter
  debita por GTK conforme a tabela. Top-up credita no wallet (com flag de validade).

## Próximos passos
1. Founder confirma anchors Wave/Pyre/Full (Leaf já ok).
2. Calibrar a tabela GTK→custo real (OpenRouter/ElevenLabs) garantindo margem ≥ alvo.
3. Eu atualizo o seed `plans` + escrevo a /pricing (cards Leaf/Wave/Pyre/Full) e a /planos do site.


---
## ✅ CONFIRMADO (founder, 2026-06)
- Leaf $79/$199/$499 · Wave $99/$249 · Pyre $99/$249 · Full $599 (pool 70k GTK).
- Top-ups: +5k $25 · +15k $60 · +50k $175. Anual −17%. Cobrança USD (Stripe).
- Pendente só técnico: calibrar tabela GTK→custo real quando tiver chaves OpenRouter/ElevenLabs.
