# Ginkgo — Arquitetura da Tokenização (GTK) + Anúncios

## 1. Computação/Geração → GTK (sua intuição está CORRETA)
O usuário só vê o OUTPUT; provedor e custo ficam atrás das câmeras. Implementação:
- **Provider Router** (já temos `services/llm/aiGateway.ts` + `tokenRouter`): camada única na
  frente de TODOS os provedores — LLM (OpenRouter), TTS (ElevenLabs), imagem (Flux/fal.ai/MJ),
  vídeo (Seedance/HeyGen), MCP (Meta/TikTok), etc.
- Cada capacidade é uma **ação normalizada** (reply, tts, generate_image, generate_video,
  avatar_video, ad_copy...). O router escolhe o provedor por custo/qualidade/disponibilidade,
  com **failover**, executa e devolve só o resultado.
- A ação debita **GTK = custo_USD ÷ preço_do_GTK (arredondado pra cima)**, com a margem já
  embutida no preço do GTK. Usuário nunca vê provedor nem USD bruto.
- Ganhos além de esconder: trocar provedor sem mexer em UX/preço, otimizar custo, resiliência.
✅ É exatamente assim que se faz. A tabela `gtk_costs` é a expressão disso.

## 2. Anúncios → ATENÇÃO: separar "trabalho de IA" de "dinheiro de mídia"
Aqui mora a distinção crítica. Existem DUAS coisas no Wave/Alfred:
- **(a) Trabalho de IA** (estratégia, copy, criativo, otimização, atribuição) = COMPUTAÇÃO →
  **GTK**, igual ao resto. ✅
- **(b) Verba de mídia** (o dinheiro que vira impressão/clique no Meta/TikTok) = NÃO é custo de
  compute. É o dinheiro de anúncio do cliente. Converter "GTK → dinheiro de mídia" transforma a
  Ginkgo em **intermediário financeiro** (guarda e gasta dinheiro alheio) — outro regime:
  contabilidade (pass-through, não receita; markup é que é receita), compliance/financeiro
  (managed-spend/revenda pode tocar regras de meios de pagamento), titularidade do billing no
  Meta, reembolso, fraude/chargeback.
- **Regra de ouro:** NÃO misturar a carteira GTK (compute) com a verba de mídia. São saldos
  separados, mesmo que a UX abstraia.

## 3. Dois modelos pra verba de mídia
### Modelo A — Conta de anúncio do PRÓPRIO cliente (recomendado pro launch)
- Cliente conecta a própria conta Meta/TikTok + método de pagamento dele. Alfred opera via API.
- A mídia é paga **pelo cliente direto ao Meta**. A Ginkgo cobra só o **trabalho de IA em GTK**.
- Zero intermediação financeira, zero FX sobre mídia, contabilidade limpa, mais rápido de subir.
- UX: continua "deposita GTK + pede campanha"; a verba de mídia é do cliente, definida por campanha.

### Modelo B — "Créditos de mídia gerenciados" (v2, decisão deliberada)
- Cliente deposita uma **carteira de mídia (USD)** que a Ginkgo gasta por ele, com **taxa de
  gestão/markup transparente** (ex.: 10–15%, padrão de agência).
- É o "deposita dinheiro e a gente roda" que você descreveu — válido, mas exige: billing no Meta
  sob System User com fonte de pagamento central, contabilidade de pass-through, controle de
  fraude/reembolso, e provavelmente CNPJ + estrutura financeira pronta.
- Carteira de mídia SEPARADA da carteira GTK (saldo e ledger próprios).

## 4. Recomendação
- **v1 (agora):** Modelo A. GTK cobre 100% do compute (incl. trabalho de Alfred). Mídia = conta
  do cliente. Não bloqueia o pricing #5 (que é só GTK/compute).
- **v2 (depois):** oferecer Modelo B como upgrade "gestão completa", quando a estrutura
  financeira existir. Aí entra uma `media_wallets` separada.

## 5. Resumo (respondendo "está correto?")
- Compute/geração (ElevenLabs, fal, flux, MJ, seedance, HeyGen, MCP, APIs) via GTK com rotação
  de provedor no back-end, usuário vendo só o output: **CORRETO**. ✅
- Anúncio "deposita token → vira dinheiro no Meta no back-end": correto **em espírito**, mas
  a verba de mídia tem que ser **carteira separada** e é uma **decisão de modelo (A vs B)** com
  peso financeiro/legal — não é a mesma coisa que o GTK de compute.
