# LEAF — superfície de produto (visão recomendada)

> Opinião da Sexta-feira (2026-06-26), a pedido do fundador. Grounded no que já existe + na arquitetura Callima / Brann / Hermes. Honest-engineering: status real marcado (✅ real · ⚠️ parcial · 🔜 próximo · 🔴 risco/depois).

## A tese (a opinião que organiza tudo)
**LEAF não é "um CRM com IA colada". É uma secretária que se opera sozinha — e te dá um CRM como o rastro auditável do que ela fez + os controles pra afiná-la.**
Inverte o normal: a **conversa é o produto**; as telas são **lentes** sobre a mesma espinha. O dono **afina** (via Brann) e **supervisiona** (inbox + dados) — **não opera**. Essa tese diz o que construir (o loop apertado) e o que **não** construir (CRM genérico, disparo cedo).

## A espinha (toda tela é uma lente disto)
**Contato (lead) → Conversa (Callima) → Ação (agendar / checkout / disparo) → Resultado (dado).**

## As telas (recomendadas, com status)
- **Conversas (inbox multicanal)** — WhatsApp agora; o humano assume quando quiser (handoff honesto). É o coração. **✅ real.**
- **CRM / Pipeline (Kanban)** — o lead **se preenche sozinho** (Callima qualifica → bridge → CRM); o dono só move estágios. **✅ real (auto-fill provado).**
- **Agenda** — Callima agenda (`[[AGENDAR]]`) → cai aqui + no Google do dono. **🔜** (build COWORK em andamento + appointment-bridge CODE lançada).
- **Ofertas / Produtos + Checkout** — o dono **anexa a oferta** (preço, descrição, link) → alimenta o que a Callima vende **e** o **checkout** que ela manda. Checkout = **Stripe Payment Links** (já construído). **⚠️ checkout ✅ · "Ofertas" como tela/registry = 🔜.**
- **Dados (atendimentos × resultado)** — o funil: atendimentos → leads → agendamentos → checkouts → vendas. A "analista de operação" pro dono. **🔜.**
- **Brann (config + controle)** — o dono conversa pra configurar/monitorar a Callima (persona, voz, permissões, o que fala/faz). **⚠️ `hermes.chat` existe · escrever a config = 🔜.**
- **Disparos (campanhas promo · WhatsApp/email)** — **🔴 alto risco** (spam, compliance, **ban do número**). Fazer **por último e com trava** (opt-in, rate-limit, templates aprovados).

## Sequência recomendada (valor × risco × já-construído)
1. **Apertar o loop que já existe:** Conversas + CRM auto-fill + **Agenda** + **Ofertas→checkout**. (Low-risk, metade pronto.)
2. **Dados** (o funil) — mostra ROI, fecha o ciclo de confiança do dono.
3. **Brann config** — self-serve real (afinar a Callima por conversa).
4. **Disparos** — por último, com governança pesada.

## As regras (a cola)
- **Cada ação = capacidade governada sob o Hermes** (os 4 ramos): agendar/checkout/disparo = **portal determinístico** (n8n/Skill), disparado por intent, **honest-data**, dentro das permissões.
- **Honest-data em tudo:** a tela mostra só **estado real** (agendamento real, pagamento via webhook real, envio real). Zero vaidade.
- **Governança:** o que a Callima pode fazer = **concedido do catálogo**, dentro do teto de risco do tenant.

## O que eu NÃO faria ainda (opinião forte)
- **Disparo promo cedo** — é o jeito mais rápido de **queimar o WhatsApp do cliente**. Só com opt-in + rate-limit + template aprovado.
- **CRM genérico** — não competir em contagem de feature; o diferencial é *"se preenche e se opera sozinho"*.
- **Checkout custom** — usar os Payment Links que já existem; não reinventar pagamento.

_Mantido pela Sexta-feira. A conversa é o produto; as telas são o rastro + os controles._
