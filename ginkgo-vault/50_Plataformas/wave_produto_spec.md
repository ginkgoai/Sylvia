# WAVE — spec de produto (tráfego / distribuição · agente Alfred)

> Spec (não deck). Grounded nos frameworks extraídos dos decks (`10_Marca/sintese_decks_fonte.md`, Parte C), na fronteira confirmada pelo fundador (`wave_benchmark_mywiser.md`) e na doutrina do tronco (`arquitetura_yggdrasil_ginkgo.md`, `doutrina_separacao_ia_sistema.md`, `hierarquia_capacidades_hermes.md`, `modelo_provedores_e_tiers.md`, `arquitetura_agentes_e_tiers.md`). Honest-engineering: status real marcado (✅ existe · ⚠️ parcial · 🔜 próximo · ❌ white-space). **PYRE/WAVE são conceituais hoje** — este doc é o norte, não uma promessa de que já existe.

## Posição na suíte (a costura)
**PYRE cria → WAVE distribui/mede → LEAF converte.** WAVE é a metade **"distribuição + performance"**: pega o ativo (criativo/landing) que é *output do PYRE*, o coloca no ar (pago **e** orgânico), rastreia honesto e devolve o lead pra **porta de entrada do LEAF** (a Callima fecha no WhatsApp). A landing/ativo é o **seam**: output do PYRE · superfície de distribuição do WAVE · porta do LEAF. WAVE **não gera criativo** — ele coloca, agenda, mede e propõe otimização.

---

## Tese / doutrina
- **Alfred (a face) ≠ WAVE (o sistema).** Alfred é a face do **Hermes** no ramo de tráfego — percebe, raciocina, **emite Task**. Nunca executa o efeito (não cria a campanha, não mexe na verba, não toca o segredo). Quem executa é a **Boundary/Laplace** (Task + orçamento + evidência + segredo do cofre + HITL). Uma mente, três faces; Alfred é uma delas.
- **honest-data é estrutural, não feature.** O calcanhar de "IA que faz ads" é **alucinar número**. WAVE separa **IA (propõe** criativo/página/lance/público) de **sistema (ingest REAL** do Google Ads / Meta / GA). O Alfred só afirma métrica que o **sistema provou** — nunca "a campanha deu certo" / "escalei" / "gastei" sem evidência ingerida. Sem dado real, o painel mostra vazio honesto, não estimativa.
- **Dinheiro é o eixo de governança.** Mídia paga = mover dinheiro de terceiro. Todo efeito que gasta (criar campanha, subir lance, ampliar verba, cobrar o cliente) = **R3 → HITL**; o PSP/plataforma confirma; só então o efeito é real. Previsibilidade > inteligência onde há verba em jogo.
- **Separação de propósito (contra o bundle).** My Wiser é um bundle vertical (cria + distribui + mede num fluxo só). Nós **separamos de propósito** (single-responsibility + honest-data): WAVE é só distribuição+métrica; criação é do PYRE, conversão é do LEAF. O diferencial não é fazer tudo — é **governança + honestidade + funil de suíte**.

## Escopo (o que é vs o que não é)
**É:**
- Análise de canal/audiência (lê performance real por canal/público).
- Agendamento e publicação **pago + orgânico** (calendário de distribuição por canal).
- Operação de campanha paga: estrutura de funil, segmentação, lances/orçamento — **todo movimento de verba atrás de HITL**.
- Tracking honesto: pixel / UTM / GA / Ads / plataformas orgânicas — ingest do dado **real**.
- Analytics + relatório em tempo real (o que rendeu, o que não).
- Sugestão de otimização (o Alfred **propõe**; humano **aprova** o que gasta).
- **Sub-agente financeiro** (verba de ads + cobranças) — ver seção própria.

**NÃO é:**
- **Não gera criativo nem landing** — isso é PYRE. WAVE **consome** o ativo do PYRE.
- **Não fecha venda / não atende** — isso é LEAF (a Callima). WAVE entrega o lead na porta.
- **Não executa gasto sozinho.** Nunca cria campanha / mexe em verba sem aprovação humana. (É o oposto do "autopilot que queima verba".)
- **Não inventa métrica.** Sem ingest real, não afirma resultado.
- **Não é gestor de mídia genérico** — não compete em contagem de feature; compete em *governança de verba + honest-data + suíte*.

## Capacidades → Skills governadas
Toda capacidade do Alfred = **Skill governada pela Boundary** (efeito = Task + budget + evidência), organizada pelos frameworks dos decks. Regra de ouro (ADR 0002): **perceber (ler) é livre · agir (efeito) atravessa a Boundary.**

**Frameworks dos decks, mapeados em capacidades (Parte C do síntese):**

- **AI Hub / loop (C1)** — arquitetura-mãe do WAVE em 4 blocos: **Data Sources → AI Hub (Alfred orquestra) → Execution Platforms → Analytics** (loop). O AI Hub é o Alfred sob o Hermes; as Execution Platforms são Skills governadas.
  - Ciclo de campanha (4 etapas): **Geração de Insights → Criação de Conteúdo Dinâmico → Segmentação & Ativação → Otimização Contínua.** *(A "criação de conteúdo" aqui = pedir ao PYRE / colocar variações do ativo — WAVE não desenha o criativo.)*
- **Arquitetura de funil (C2)** — **Awareness → Consideration → Conversion**, cada estágio com métrica própria (perceber = livre; a leitura ancora a proposta).
- **Segmentação progressiva (C2, 4 passos)** — **Inicialização (públicos amplos) → Refinamento (IA lê engajamento) → Expansão (lookalikes) → Adaptação contínua.** Cada mudança de público que ativa verba = Skill R3/HITL.
- **A/B estruturado (C2)** — testar **Títulos · Imagens/Vídeos · Landing Pages · Segmentações**. O Alfred propõe o experimento; **subir o teste (gasto) = HITL**; o resultado só conta com ingest real.
- **Loop de otimização (C2)** — **Monitoramento → Análise IA → Ajuste (lances/orçamento) → Escala.** O "Ajuste Autônomo" do deck vira **Ajuste proposto + aprovado** (money = R3). "Escala o que vende, corta o que não rende" — mas *com evidência e aprovação*. Metáfora do deck: *"o criativo é o motor; o tráfego é o combustível"* — o motor vem do PYRE.
- **Insights / análise preditiva** — prever desempenho **antes** de lançar (perceber/propor = livre; **lançar = HITL**). Nunca vira "vai converter X%" afirmado como fato.

**Skills concretas (efeito = Boundary):** `conectar_conta_ads` (credencial → cofre, R3/HITL) · `ingerir_metricas` (read, livre) · `propor_campanha` (rascunho, sem gasto) · `criar_campanha` / `ajustar_verba` / `ajustar_lance` (R3 → HITL) · `agendar_publicacao_organica` (R2) · `rastrear` (pixel/UTM/GA, read) · `relatorio` (read). *Discovery de skill por similaridade = 🔜 (herda do Skill Registry do tronco).*

### Sub-agente financeiro (sob o Alfred) — verba de ads + cobranças
Delegação hierárquica **main (Alfred) → sub (financeiro)**; o sub **herda a governança inteira** (mesmo Boundary/cofre/honest-data/HITL; teto = `min(face, tenant)`).
- **Benchmark: Pierre.finance (CloudWalk)** — IA que **lê** extratos (Open Finance, 100+ bancos, Bacen), categoriza, alerta cobrança estranha/duplicada, prevê parcelas/assinaturas, define metas. **Padrão de ouro: SÓ LEITURA, zero transação** ("nunca mexe no seu dinheiro"; a senha fica com o usuário).
- **No nosso caso — a linha que não se cruza:**
  - **Read é livre** (à la Pierre): lê gasto de ads, extrato de verba, categoriza, alerta anomalia/duplicidade, projeta burn de campanha, sugere realocação. Perceber não atravessa HITL.
  - **Movimento de dinheiro = R3 → HITL/PSP.** Executar cobrança do cliente / mover verba **só pela camada de dinheiro governada**: o PSP/webhook confirma; o Alfred **nunca finge** "gastei" nem "cobrado". Read livre · **movimento aprovado**.
- Ex.: o financeiro pode dizer "esta campanha vai estourar a verba em 3 dias" (read) e **propor** cortar; **executar o corte de orçamento (gasto) = aprovação humana**.

## Dados (multi-tenant · org do token)
- **Isolamento por org.** Conta de Ads / pixel / GA **por tenant**; nada cross-tenant. A org sempre sai do **JWT no painel**; nunca `id` no path (sem superfície cross-tenant; 404 cross-tenant).
- **Ingest por token de org.** O conector de métricas (n8n/API) detém **token de serviço por-org** e resolve a org pelo token — nunca JWT de usuário no executor cego (mesmo padrão do `POST /ingest/lead` do LEAF).
- **Fonte da verdade = tronco.** As métricas ingeridas moram no `ginkgo-tree` (Evidence/DB), não na cabeça do modelo nem só no painel da plataforma externa. O painel lê de lá. Estado durável mora no sistema (P004).
- **RAG per-tenant governado** (pgvector, P004): repertório de campanha/público por org via Skill de escrita — não similaridade crua.
- **Provedores/tiers:** default **white-label compartilhado** (Ginkgo detém contas de Ads/LLM; custo no plano) → **teto de uso por tenant** (metering/cap) obrigatório antes de escalar. **Enterprise BYO ("Odysseus"):** o tenant aponta **chaves próprias** de Ads/LLM (cofre do tenant) — mesmo código, STATE diferente.

## Governança (Boundary · cofre · money/credencial = HITL)
- **Chokepoint único:** todo efeito — de qualquer camada — atravessa a **Security Boundary = Laplace** (Task + orçamento + evidência + segredo do cofre + HITL se R3). O Hermes/Alfred pensa; o Laplace é o portão.
- **Escala de blast-radius** (`hierarquia_capacidades_hermes.md`): Ads é **camada 3 (Integrações)** — **efeito = Skill (R2); dinheiro/credencial = R3/HITL.** O Alfred do cliente nunca sobe além da camada 1 (Python sandbox per-tenant); **nunca toca o host.**
- **Credencial no cofre.** Chave de Ads / token de plataforma **injetados pelo Boundary no runtime**, redijidos no log — nunca no `.env`, nunca na cabeça do modelo (lição do quase-furo da `GROQ_API_KEY`).
- **Money = R3 → HITL/PSP** em tudo que gasta: criar campanha, subir lance/verba, cobrar cliente. O PSP/plataforma confirma → só então honest-data afirma.
- **Maturity ladder** (`simulation → shadow → production`): skill nova de gasto nasce em simulação/shadow, promovida só com evidência + HITL. Kill-switch pronto; guardrails ativos.

## Sequência de fatias (P0 → Pn · buildável · uma fatia vertical por vez)
> Regra: cada fatia é **vertical e provável** (entrega valor sozinha, sem inchar). Ordem = valor × risco × já-construído. **Read antes de write; dinheiro por último e com trava** (mesma disciplina do LEAF: disparo/gasto governado por fim).

- **P0 · Ingest de métricas + painel read-only (o "aha" honesto).** `conectar_conta_ads` (credencial → cofre) → `ingerir_metricas` de 1 plataforma (Meta **ou** Google) → `GET /wave/metrics` (tenant-scoped, org do token) → tela de performance real. **Zero gasto, zero criação.** Prova a espinha honest-data: o painel mostra só o que foi ingerido. ← **primeira**
- **P1 · Analytics de funil + relatório.** Awareness→Consideration→Conversion com métrica por estágio; relatório "o que rendeu / o que não" (read). Fecha o ciclo de confiança (ROI visível) antes de qualquer efeito.
- **P2 · Proposta de campanha (rascunho, sem gasto).** `propor_campanha` + segmentação progressiva (passos 1–2) como **rascunho aprovável**. O Alfred desenha; nada vai ao ar sem humano. Consome o ativo do PYRE (seam).
- **P3 · Execução governada de campanha (money = HITL).** `criar_campanha` / `ajustar_verba` / `ajustar_lance` atrás de `Offer`/Boundary com **aprovação humana do gasto**; PSP/plataforma confirma. A/B estruturado e loop de otimização entram aqui — **sempre proposto + aprovado**. ← primeiro efeito que gasta.
- **P4 · Distribuição orgânica + agendamento.** `agendar_publicacao_organica` (calendário pago+orgânico), risco menor que verba. Costura com o calendário do PYRE.
- **P5 · Sub-agente financeiro (read).** Leitura de gasto/verba à la Pierre: categorização, alerta de anomalia, projeção de burn. **Só read.**
- **P6 · Sub-agente financeiro (cobranças, money=HITL).** Movimento de dinheiro pela camada governada (PSP confirma). Por último, com trava máxima.
- **Pn · Enterprise BYO** (chaves próprias de Ads/LLM) + discovery vetorizado de skills.

## Não-metas
- **Não ser autopilot que gasta sozinho.** Nunca criar/ampliar campanha sem HITL — evitar "queimar verba" é feature, não limitação.
- **Não gerar criativo/landing** (é PYRE) nem **atender/fechar** (é LEAF). WAVE fica na sua faixa.
- **Não afirmar resultado sem ingest real.** Sem dado provado, vazio honesto — nunca estimativa vestida de fato.
- **Não CRM de mídia genérico** — não competir em contagem de feature.
- **Não custom de pagamento** — cobrança pela camada de dinheiro governada (PSP), não reinventar.
- **Não "IA que decide o gasto".** A IA propõe; o humano aprova; o sistema registra.

_Mantido pela Sexta-feira. Alfred propõe; o Laplace é o portão de todo efeito; o dado real ancora a fala. PYRE cria → **WAVE distribui/mede** → LEAF converte._
