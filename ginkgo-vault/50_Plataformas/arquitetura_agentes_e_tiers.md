# Arquitetura de agentes + tiers (decisões do fundador — 2026-07-04)

> Hierarquia **main → sub-agentes delegados**, roster, histórico de nomes (renomeações), e o tier **IMAGINE**. Governança herdada (honest-data, money/credencial = HITL). Reconcilia os decks antigos (`10_Marca/sintese_decks_fonte.md`) com a doutrina atual.

## Camadas
- **Brann — Assistente / copiloto** (camada de operação): você **conversa com ele** pra configurar e operar; **orquestra** os agentes-trabalhadores. Superior a eles. É a cara da plataforma (olho-anel ciano).
- **Agentes-trabalhadores (um por produto):**
  - **Callima — Secretária (LEAF):** atende · entende (áudio) · fala (voz) · agenda · vende no WhatsApp. Qualificação por **SPIN** (dos decks).
  - **Nyra — Criação (PYRE):** imagem/vídeo/carrossel/copy.
  - **Alfred — Tráfego (WAVE):** distribuição · anúncios (pago+orgânico) · métricas.
- **Sub-agentes delegados:** um agente-main delega tarefas especializadas a um sub-agente **governado** (mesmo Boundary/cofre/honest-data/HITL).

## Sub-agentes (roadmap)
- **Financeiro — sob Alfred (WAVE):** gestão de **verba de anúncios** + **cobranças**.
  - **Benchmark: Pierre.finance** (CloudWalk) — IA que lê extratos (Open Finance, 100+ bancos, Bacen), categoriza, alerta cobrança estranha/duplicada, prevê parcelas/assinaturas, metas. **Padrão de ouro de segurança: SÓ LEITURA, zero transações** ("nunca mexe no seu dinheiro"; senha fica com o usuário). Usa sub-agentes nomeados (Marie/Einstein/Galileu).
  - **Nosso:** analisa gasto de ads (read, à la Pierre) + **executa cobranças SÓ pela camada de dinheiro governada** — money = R3 → **HITL**; o PSP/webhook confirma; honest-data (nunca finge "gasto" nem "cobrado"). Read é livre; **movimento de dinheiro é aprovado**.
- **Lexra — jurídica (futura):** especialista — análise, escrita, **criação de contratos, integração DocuSign**. Governança: **assinar/enviar = HITL**; honest-data (só afirma o que o DocuSign confirmou). Era uma das **demos reais** citadas no Briefing (Lead Finder · Lexra · Live Agent).
- **Padrão:** delegação hierárquica main → sub; o sub herda a governança inteira.

## Histórico de nomes (renomeações — NÃO são agentes reservados)
- **Alphie → Alfred** e **Shion → Sexta-feira**: nomes antigos que o fundador foi trocando na idealização. São a **mesma entidade renomeada**, não nomes reservados nem agentes futuros. O conceito de **orquestrador sempre existiu** (linhagem Sexta-feira/Alfred/Brann); a ideia dos agentes virarem **avatares/mascotes veio depois**. Concepts antigos (tarô "Alphie – O Gerente", etc.) = design **alpha/beta**, arquivados em `brand/_alpha_beta/`.

## Tier IMAGINE (institucional)
- **Acima das 3 assinaturas.** Pra quem quer **contratar a Ginkgo como empresa** — build custom, sob medida: **"você imagina, a gente constrói".** Encaixa com **Enterprise BYO ("Odysseus")** + serviço de agência. Topo do funil de valor (linguagem do Briefing: Básico → Futurista → Imagine).

## Pricing (modelo v2 — 04/07, fechado)
- **À la carte:** assina **LEAF R$449 · PYRE R$899 · WAVE R$1.199** de forma **independente** (um, dois ou os três). **Sem "Full"** — o antigo R$2.497 era desconto-fake de R$50 (soma=2.547) → fere honest-data. Bundle só volta se for **desconto REAL** (ex.: −15% nos três); senão, dropado.
- **Teste grátis** (7–14 dias, cheio) como porta de entrada. Tier grátis limitado (X conversas/mês · texto · 1 agente) = **depois** do metering (#9), pra não sangrar com abuso.
- **IMAGINE / enterprise:** **tokens por uso (GTK, estilo Manus) + BYO** (traz sua própria inferência). O **GTK já existe no app** (carteira). Regra: SMB = assinatura flat (previsível); enterprise = uso.
- **Ajuste no código (fatia Fable):** `apps/api/src/billing/catalog.ts` — assinatura independente por produto + trial; rever/remover o Full.
- Decks antigos arquivados: WAVE 749 · PYRE↔WAVE invertidos · LEAF-guarda-chuva (Core/Infinity/Prime).

## Papéis (trava de nomenclatura)
Callima = **Secretária** · Brann = **Assistente** (copiloto) · Nyra = criação · Alfred = tráfego. As grafias antigas dos decks ("Alphie"→Alfred, "Brann-secretária") = **corrigidas**; os footers HTML já usam Callima.
