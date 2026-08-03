# Ginkgo — Arquitetura de Apresentação (3 formatos)

> 2026-07-04. Idealização pra **Claude Design** (exploração/marketing; produção = Fable). Material 100% real do vault. **Dois registros visuais:** warm/honest-data (produto) + neon-cósmico (marca/hero) — não misturar no app.

## Por que temos material de sobra (e por que impacta)
A maioria dos decks de IA é vaporware. A Ginkgo tem **engine governada VIVA** + **mundo de marca coeso** (honest-data + mito Yggdrasil + família de mascotes). O "mostramos o trabalho" vira o próprio pitch: produto real, arquitetura real, mascotes reais.
**Baldes prontos:** marca (Ginkgo/Yggdrasil/Hiroshima) · doutrina (IA↔sistema, honest-data, governança) · 3 produtos + preços reais · mascotes (Brann/Callima/Alfred/Nyra) · arquitetura (engine multi-tenant, Boundary, cofre, skills, white-label/BYO) · tração (Callima provada + 348 testes) · refs (orb, mãos IA×robô, iridescente, logo árvore-circuito em `brand/refs/`).

---

## FORMATO 1 — Didático para leads
**Público:** PMEs curiosas. **Objetivo:** entender + querer. **Registro:** warm + toques neon; mascotes. **Template Claude Design:** Protótipo (landing) ou Slides.
**Prompt (colar no Claude Design):**
> Crie uma landing/apresentação didática e chamativa da **Ginkgo AI Systems** para leads (PMEs). Tom caloroso, claro, impactante. Narrativa: (1) **Quem é** — Ginkgo, a árvore de 200 milhões de anos que sobreviveu até Hiroshima; "Raízes antigas · agentes novos". (2) **O problema** — IA "mágica" que inventa e quebra. (3) **A virada** — "Agentes de IA que mostram o trabalho": cada ação vira tarefa auditável, com prova (honest-data). (4) **Os 3 mundos, uma conta** — LEAF (Callima, secretária no WhatsApp que atende, entende áudio, fala por voz, agenda e vende — R$449), PYRE (Nyra, criação de conteúdo — R$899), WAVE (Alfred, tráfego e métricas honestas — R$1.199). (5) **Como funciona** — você configura conversando com o Brann, o copiloto corvo; sem código. (6) **Gap pra imaginação** — "Você imagina, a gente constrói": descreva seu negócio e veja seu agente nascer. Visual: paleta warm (verde/creme) com toques neon; mascotes (corvo Brann de chapéu e olho-anel ciano, Callima de luz, polvo Alfred, criatura Nyra); logo árvore-circuito. Seções com respiro, CTA "Conectar meu WhatsApp".

---

## FORMATO 2 — Institucional para parceiros
**Público:** parceiros / enterprise / investidores. **Objetivo:** confiança + credibilidade técnica. **Registro:** dark elegante, arquitetura > mascote. **Template:** Documento ou Slides executivos.
**Prompt (colar no Claude Design):**
> Crie uma apresentação institucional sóbria e técnica da **Ginkgo AI Systems** para parceiros e enterprise. Tom sólido, credível, arquitetural. Conteúdo: (1) **Tese** — IA como infraestrutura crítica, não feature mágica. (2) **Doutrina/diferencial** — separação IA↔sistema (a IA interpreta e emite intenção; o sistema executa governado e prova) → honest-data por construção; dinheiro/credencial exigem aprovação humana (HITL); Evidence append-only; 9 invariantes. (3) **Arquitetura** — engine governada multi-tenant, Boundary (executor + cofre AES-256-GCM), skills plugáveis (transcrição, voz, RAG, agenda), WhatsApp via Evolution. (4) **Implementação** — self-serve (signup → conecta canal → configura com o Brann → opera); white-label compartilhado (zero atrito) OU Enterprise BYO "modo Odysseus" (chaves próprias, LLM local, provedores e skills trocáveis). (5) **Valores** — confiável (resiliência do ginkgo), honesto (honest-data), governado (auditável). (6) **Tração** — Callima provada vendendo, engine governada de pé, 348 testes verdes. (7) **Tempo/formato** — implantação em dias, sem lock-in. Visual: dark elegante; hero = mão humana tocando mão-robô (a separação IA↔sistema); diagramas limpos da engine.

---

## FORMATO 3 — Motion / vídeo
**Público:** social / impacto. **Objetivo:** wow + demo. **Registro:** neon-cósmico total (orb, mascotes animados, cenas do produto). **Template:** Animação.
**Prompt (colar no Claude Design):**
> Crie uma peça de motion cinematográfica da **Ginkgo** — neon-cósmica, impactante. Cenas: (1) um **orb de luz** acende no escuro (ciano/azul/violeta) = a presença da IA. (2) O corvo **Brann** (chapéu, olho-anel ciano, berloque-engrenagem) surge = o copiloto. (3) Split: **mão humana × mão-robô** se tocam = IA↔sistema. (4) **Demo real** — a Callima atendendo no WhatsApp (texto → áudio → voz → agenda → venda), com "cada resposta vira uma tarefa auditável". (5) Os **3 mundos** giram — LEAF/PYRE/WAVE (Callima/Nyra/Alfred). (6) Tagline: **"Ginkgo — agentes de IA que mostram o trabalho."** Estilo: preto + neon líquido, iridescência, glow, transições suaves; deixar espaço pra encaixar cenas/testes/demos reais depois.

---

## Como construir no Claude Design
- Marketing = **Claude Design** (exploração). Começa de um template (Protótipo/Slides/Documento/Animação) e **cola o prompt** do formato + **anexa refs** de `brand/refs/` (logo, mascotes, mãos-IA, orb).
- "Criar usando o código Claude (React)" dá **mais fidelidade** se você quiser puxar nossos tokens/DS — bom pro Formato 2. Pros Formatos 1/3, template + prompt + refs já bastam.
- **Regra dos 2 registros:** o neon-cósmico é da MARCA (hero/motion); **não deixa vazar** pro dashboard warm do produto.
