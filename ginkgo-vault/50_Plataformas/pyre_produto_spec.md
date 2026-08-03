# PYRE — spec de produto (conteúdo / criação · agente Nyra)

> Spec (não deck). Grounded nos frameworks extraídos dos decks (`10_Marca/sintese_decks_fonte.md`, Parte D), na fronteira confirmada pelo fundador (`wave_benchmark_mywiser.md`) e na doutrina do tronco (`arquitetura_yggdrasil_ginkgo.md`, `doutrina_separacao_ia_sistema.md`, `hierarquia_capacidades_hermes.md`, `modelo_provedores_e_tiers.md`, `arquitetura_agentes_e_tiers.md`). Honest-engineering: status real marcado (✅ existe · ⚠️ parcial · 🔜 próximo · ❌ white-space). **PYRE/WAVE são conceituais hoje** — este doc é o norte, não uma promessa de que já existe.

## Posição na suíte (a costura)
**PYRE cria → WAVE distribui/mede → LEAF converte.** PYRE é o **"o QUÊ"**: tudo que chega ao público visualmente — imagem, vídeo, carrossel, apresentação, edição, copy, hashtag, descrição. O ativo/landing que a Nyra produz é o **seam**: *output do PYRE* · superfície de distribuição do *WAVE* · porta de entrada do *LEAF*. PYRE **não decide onde/quando publicar nem mede** (isso é WAVE) e **não atende/fecha** (isso é a Callima no LEAF). PYRE entrega o ativo pronto e aprovado.

---

## Tese / doutrina
- **Nyra (a face) ≠ PYRE (o sistema).** Nyra é a face do **Hermes** no ramo de conteúdo — percebe, raciocina, **emite Task**. Nunca executa o efeito bruto (a geração/edição/publicação atravessa a Boundary), nunca escolhe modelo, nunca toca o segredo. Uma mente, três faces; Nyra é uma delas.
- **honest-data é estrutural, não feature.** O produto do PYRE é criação, então a honestidade tem **duas faces**: (1) **honest-provenance** — a Nyra não afirma que publicou / que um número foi atingido sem o efeito/ingest real (medição é do WAVE; a Nyra nunca inventa alcance/views); (2) **honest-status** — o painel mostra só o estado real do ativo (rascunho / aprovado / no ar via WAVE). Zero vaidade: nunca "seu post bombou" sem dado ingerido.
- **Aprovação é o eixo de governança do conteúdo.** Publicar em nome do cliente = agir no mundo com a marca dele. Modelo do Catálogo: **"aprova com 1 clique ou 100% automático"** — mas o *default seguro* é HITL na publicação; o modo autônomo é opt-in por tenant, dentro do teto de risco. Criar/editar rascunho = livre; **publicar = efeito governado**.
- **Separação de propósito (contra o bundle).** My Wiser funde criação + distribuição + métrica; nós **separamos de propósito** (single-responsibility). PYRE é só criação. O WAVE consome o ativo do PYRE — **PYRE não coloca no ar, não agenda, não mede**.

## Escopo (o que é vs o que não é)
**É:**
- Ideação de conteúdo guiada pelos **4 pilares** (temas centrais).
- **Calendário editorial de 30 dias** (ideação → criação → agendamento → análise).
- Criação: imagem, vídeo/Reel, carrossel, apresentação, copy, hashtag, descrição.
- Roteiro de vídeo curto: **Hook (3s) → Desenvolvimento → CTA**.
- **Banco de hooks** + templates de roteiro (reutilizáveis por tenant).
- Reaproveitamento **1 ativo → N formatos** (base → pílulas/carrossel/snippet/vídeo curto).
- Fila de aprovação (rascunho → aprovado) antes de entregar ao WAVE.

**NÃO é:**
- **Não distribui / não agenda / não impulsiona / não mede** — isso é WAVE. PYRE entrega o ativo; o WAVE coloca no ar.
- **Não atende / não qualifica / não fecha** — isso é LEAF (Callima).
- **Não afirma performance.** Views/alcance/conversão vêm do ingest do WAVE; a Nyra nunca inventa número.
- **Não publica sozinha por default.** Autônomo total é opt-in governado, não o padrão.
- **Não é banco de templates genérico** — o diferencial é *pilares + calendário + hook + reaproveitamento governados na engine*, não contagem de assets.

## Capacidades → Skills governadas
Toda capacidade da Nyra = **Skill governada pela Boundary** (efeito = Task + budget + evidência), organizada pelos frameworks dos decks. Regra de ouro (ADR 0002): **perceber (ler) é livre · agir (gerar/editar/publicar) atravessa a Boundary.** Geração multi-modal (imagem/vídeo/áudio) = efeito atrás do provedor no cofre (custo governado / cap por tenant).

**Frameworks dos decks, mapeados em capacidades (Parte D do síntese):**

- **4 Pilares de Conteúdo (D1)** — **Inovação · Engajamento · Otimização · Autoridade.** Temas centrais que guiam toda a produção; ancoram a ideação e o calendário (por tenant, no RAG governado).
- **Ciclo do calendário — 30 dias (D1)** — **Ideação → Criação → Agendamento → Análise.** *A "Análise" e o "Agendamento" são superfície do WAVE (a Nyra prepara/propõe; o WAVE agenda e mede).* PYRE entrega o plano + os ativos.
- **Reaproveitamento 1→N (D1)** — **base (post/roteiro) → Social (pílulas/carrosséis) → snippet → vídeo curto**, adaptado por formato. Mensagem unificada liga PYRE↔WAVE.
- **Psicologia do Hook — 3s (D2)** — **Atenção Instantânea · Curiosidade Inadiável · Relevância Acelerada.** Abre o roteiro forte nos primeiros 3s.
- **Estrutura narrativa de Reel (D2)** — **Hook (3s) → Desenvolvimento (10–15s) → CTA (2–3s).** Espinha de todo vídeo curto.
- **Copy de conversão (D2)** — clareza/benefício + **gatilhos mentais** (escassez, urgência, prova social, autoridade) + CTA assertiva. *Honest-data: gatilho de "prova social" só com fato real — não fabricar número.*
- **Sistema automatizado — 4 blocos (D2, casa com PYRE)** — **Banco de Hooks · Templates de Roteiro · Automação de Edição · Análise de Performance** (loop). *A "Análise de Performance" fecha o loop via ingest do WAVE — a Nyra não mede sozinha.*
- **Elementos visuais de retenção (D2)** — cortes dinâmicos · animação de texto/legenda · cores/contraste · trilha · ângulos — parâmetros das skills de edição.

**Skills concretas (efeito = Boundary):** `ideiar_pauta` (usa pilares + RAG, read+propor) · `gerar_imagem` / `gerar_video` / `montar_carrossel` / `montar_apresentacao` (efeito → provedor no cofre) · `escrever_copy` / `gerar_hashtags` / `gerar_descricao` (efeito) · `montar_calendario_30d` (rascunho aprovável) · `banco_de_hooks` (registry por tenant, read/escrita governada) · `editar_video` (Automação de Edição) · `enviar_para_wave` (entrega o ativo aprovado ao WAVE — o WAVE distribui). *Publicação direta = HITL por default; discovery de skill por similaridade = 🔜.*

## Dados (multi-tenant · org do token)
- **Isolamento por org.** Contas sociais / material de marca / tom de voz / banco de hooks **por tenant**; nada cross-tenant. A org sempre sai do **JWT no painel**; nunca `id` no path (sem superfície cross-tenant; 404 cross-tenant).
- **Ativos como fonte da verdade no tronco.** Rascunho, versão, status de aprovação e o ativo final moram no `ginkgo-tree` (DB/Evidence), não na cabeça do modelo. O painel lê de lá. Quando entra em distribuição, o **ponteiro do ativo** é passado ao WAVE (o WAVE não recria — referencia).
- **Ingest/entrega por token de org.** Conector (n8n/API) detém **token de serviço por-org** e resolve a org pelo token — nunca JWT de usuário no executor cego (mesmo padrão do `POST /ingest/lead` do LEAF).
- **RAG per-tenant governado** (pgvector, P004): pilares, tom de voz, material de marca, banco de hooks via Skill de escrita `adicionar_conhecimento` — não similaridade crua. A Nyra "absorve o material + tom de voz" (onboarding do Catálogo) por essa via.
- **Provedores/tiers:** default **white-label compartilhado** (Ginkgo detém contas de LLM/imagem/vídeo/TTS; custo no plano) → **teto de uso por tenant** (metering/cap) obrigatório antes de escalar — geração multi-modal é o maior vetor de custo. **Enterprise BYO ("Odysseus"):** o tenant aponta **chaves próprias** (LLM X, imagem Y, vídeo Z) no cofre do tenant — mesmo código, STATE diferente.

## Governança (Boundary · cofre · money/credencial = HITL)
- **Chokepoint único:** todo efeito — de qualquer camada — atravessa a **Security Boundary = Laplace** (Task + orçamento + evidência + segredo do cofre + HITL se R3). O Hermes/Nyra pensa; o Laplace é o portão. Kill-switch pronto; guardrails ativos.
- **Escala de blast-radius** (`hierarquia_capacidades_hermes.md`): social/geração é **camada 3–4 (Integrações + Serviços)** — read = livre · **publicar/trigger = Skill (R2)**; **credencial/gasto = R3/HITL**. A Nyra do cliente nunca sobe além da camada 1 (sandbox per-tenant); **nunca toca o host.**
- **Credencial no cofre.** Chaves de rede social / provedor de geração **injetadas pelo Boundary no runtime**, redijidas no log — nunca no `.env` (lição do quase-furo da `GROQ_API_KEY`).
- **Publicação em nome do cliente = efeito governado.** Default HITL (aprova antes de ir ao ar); modo 100% autônomo = opt-in por tenant, dentro do teto de risco. Nada de a Nyra publicar sem estar dentro das permissões concedidas.
- **Money = R3 → HITL** se a skill gastar (ex.: geração premium acima do cap, provedor pago sob demanda) — o PSP/provedor confirma; honest-data nunca finge o efeito.
- **Maturity ladder** (`simulation → shadow → production`): skill nova nasce em simulação/shadow, promovida só com evidência.

## Sequência de fatias (P0 → Pn · buildável · uma fatia vertical por vez)
> Regra: cada fatia é **vertical e provável** (entrega valor sozinha, sem inchar). Ordem = valor × risco × já-construído. **Rascunho antes de publicar; publicação (efeito com a marca do cliente) por último e com trava** (mesma disciplina do LEAF).

- **P0 · Roteiro Hook→Dev→CTA + banco de hooks (o "aha", zero efeito externo).** `banco_de_hooks` por tenant + `ideiar_pauta` (pilares) → `escrever_copy` no formato **Hook (3s) → Desenvolvimento → CTA** → tela de rascunho aprovável (`GET /pyre/drafts`, tenant-scoped, org do token). **Nada publicado, nada medido.** Prova a espinha: texto real, status honesto (rascunho/aprovado). ← **primeira**
- **P1 · Geração de imagem/carrossel (efeito governado, cap por tenant).** `gerar_imagem` / `montar_carrossel` via provedor no cofre, com **metering/cap**. Primeiro efeito que consome provedor pago — governado por custo. Fila de aprovação antes de sair do PYRE.
- **P2 · Calendário 30 dias + reaproveitamento 1→N.** `montar_calendario_30d` (pilares → pautas) + reaproveitamento (base → pílulas/carrossel/snippet). Entrega o *plano* + ativos; a Nyra propõe, o dono aprova.
- **P3 · Vídeo/Reel + Automação de Edição.** `gerar_video` / `editar_video` (cortes, legenda, trilha) — maior custo/complexidade, por isso depois do estático. Segue Hook→Dev→CTA.
- **P4 · Entrega ao WAVE (o seam).** `enviar_para_wave`: ativo aprovado → ponteiro passado ao WAVE (que distribui/mede). PYRE **não** publica direto aqui — costura a suíte. Loop de performance fecha via ingest do WAVE (a Nyra lê, não inventa).
- **P5 · Publicação orgânica direta (opt-in, HITL por default).** Só se o tenant optar por PYRE publicar sem passar pelo WAVE (orgânico simples). Default = aprovação; autônomo total = opt-in governado. Por último, com trava (risco de marca).
- **Pn · Enterprise BYO** (chaves próprias de LLM/imagem/vídeo) + discovery vetorizado de skills + skills de edição agent-authored.

## Não-metas
- **Não distribuir/medir** (é WAVE) nem **atender/fechar** (é LEAF). PYRE entrega o ativo aprovado e para aí.
- **Não afirmar performance.** Views/alcance/conversão só via ingest do WAVE — a Nyra nunca inventa número (honest-provenance).
- **Não publicar sozinha por default.** Autônomo total é opt-in governado, não o padrão.
- **Não banco de templates genérico** — o diferencial é pilares + calendário + hook + reaproveitamento governados, não contagem de assets.
- **Não geração sem cap.** Multi-modal é o maior vetor de custo — sempre com metering/cap por tenant.
- **Não vaidade.** Painel mostra estado real do ativo (rascunho/aprovado/no ar), nunca "bombou" sem dado.

_Mantido pela Sexta-feira. Nyra cria; o Laplace é o portão de todo efeito; o ativo real ancora o status. **PYRE cria** → WAVE distribui/mede → LEAF converte._
