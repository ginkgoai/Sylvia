# LEAF · Backlog de features (pós-MVP)

> O que sai do MVP enxuto e vira feature quando a receita/credibilidade justificar. Mantido pela Sexta-feira.

## Pagamentos nativos — Mercado Pago (âncora BR) + Stripe *(2026-07-01)*
- **Tese (doutrina IA↔sistema):** o PSP é **execução atrás da abstração `Offer`** — a Callima só relaya o link e **nunca finge "pago"** (o webhook do PSP confirma). Somar/trocar PSP é **invisível pra engine**.
- **Feature:** PSP **nativo por-tenant**, com **Mercado Pago** como âncora BR (Pix + cartão + boleto, melhor credibilidade/settlement que a Stripe no Brasil) **+ Stripe** (global/cartão) — "o melhor da Stripe + banco". Componentes: config de PSP por-tenant · webhook por PSP · **reconciliação pagamento→lead** (marca pago no CRM com Evidence).
- **Governança:** cada confirmação vem do webhook do PSP (nunca do LLM); credencial do PSP do tenant = R3 no cofre. Honest-data por construção.
- **MVP interino:** a venda usa o link que já existe (Stripe Payment Link — que faz Pix no BR — ou o `pix_link`), com honest-data ("te mandei o link; confirmo quando o pagamento cair").
- **Quando:** pós-MVP / fase-com-renda.

## Identidade do agente por-tenant — nome + avatar/mascote + tom *(2026-07-02)*
- **Tese:** a personalidade é **STATE do tenant**, não código (mesma engine). O cliente **batiza** o agente e escolhe **avatar** (não precisa ser pessoa: mascote, ícone, inicial) + **tom** — vira a identidade do negócio dele no WhatsApp.
- **Feature:** avatar do agente = **asset de imagem** (`AgentProfile.avatarAssetId`, blob) — **built-ins** (Callima fem/masc, corvo, silhueta-luz, monograma) **OU importar o próprio PNG**. `tone` também. Picker no dashboard + o Brann configura por conversa ("usa a Callima feminina, tom acolhedor" / "sobe esse PNG"). Honest-data intacto (identidade ≠ capacidade). **Não** é SVG gerado.
- **Arte canônica definida** (refs do fundador) → ver `brand/identidade_visual_agentes.md`. Brann = corvo + chapéu de palha + olho-anel ciano + berloque-**engrenagem** (doutrina visível); Callima = silhueta sem rosto feita de luz (interface, não pessoa falsa). Brann = identidade **fixa** da plataforma; o customizável é o **agente do cliente**.
- **Lapidação pós-core** (fatia de design), agora **com arte real** — o rascunho SVG foi descartado.
- **Quando:** fatia de lapidação do Fable, depois do core (áudio/RAG/handoff/pix).

## Conhecimento automatizado — upload de arquivos → Brann destila *(2026-07-02)*
- **Hoje (S4 pronto):** o Brann embeda **texto/URL** no workspace do tenant (`adicionar_conhecimento`). Funciona.
- **A visão:** o cliente sobe **arquivos** (PDF/docx) + um prompt → o Brann faz **parse → chunk → embed** e **destila** o conteúdo denso numa **persona/doutrina** flechada ao agente (nome/avatar dele). "Joga os documentos, eu viro a base + o jeito de falar."
- **Governança:** parse/embed atrás de Skill governada (R1), per-tenant (slug persistido), sem vazar cross-tenant; chaves no cofre.
- **Quando:** logo após o core — é o que faz o onboarding do conhecimento ser 100% self-serve.

## Outras (registradas)
- **Orb de presença + Biblioteca "cérebro vivo"** *(2026-07-03)* — orb minimizado = **presença do agente** (ouvindo/pensando/falando; protótipo neon feito). Expandido na **Biblioteca** (conhecimento/RAG) = **grafo estilo Obsidian** do que o agente sabe — "ver o cérebro vivo" (ref: sphere dourada Jarvis). **Honest-data visual:** o dono VÊ exatamente o que fundamenta a Callima (o RAG deixa de ser caixa-preta). Lapidação de design pós-core; construível com D3/force-graph/Three.js. Refs: `zoeyos_benchmark.md` · `familia_mascotes_e_conceito.md` (+ clipps novos a conferir no pass de design).
- **Tema dark** (variante + toggle) — #39.
- **RAG vetorial (pgvector)** — upgrade interno do RAG (hoje AnythingLLM workspace-por-tenant); absorve #13.
- **Multicanal** (Instagram/Messenger/e-mail/webchat) — além do WhatsApp. **Spec cravada:** `leaf_feature_multicanal.md` (ChannelPort + adapters Meta; também mitiga o risco Baileys).
- **Disparos/campanhas governados** (opt-in + rate-limit + templates aprovados).
