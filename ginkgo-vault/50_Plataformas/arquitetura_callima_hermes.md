# Arquitetura Callima + Hermes — conversa vs. execução

> Criado 2026-06-26 pela Sexta-feira, após a prova de que o modelo barato aluciná ação.
> Decisão: **separar a conversa (Callima) da execução (Hermes).** Honest-data deixa de depender do modelo e vira **garantia estrutural**.

## Por quê (a prova)
`gpt-4.1-mini` é excelente na **conversa** (vender, responder, RAG, link, áudio) e **não confiável** em chamar tool de ação inline: na execução 132 ele disse "já agendei" sem criar o evento (`gcal=0`). Prompt não corrige isso (a regra honest-data foi ignorada). Logo, ação não pode depender do tool-calling do modelo fraco — tem que sair pra uma camada determinística.

## Modelo de produto LEAF — o usuário configura a Callima conversando com o Brann
O loop do produto (a tela que o cliente Leaf usa):
> **Usuário Leaf → (web chat) Brann → configura + monitora → Callima (n8n, por-usuário) → atende os clientes DO usuário no WhatsApp.**

- **Callima = modelo "Secretária WhatsApp", instanciado por-usuário.** Roda no topo de fluxos n8n. É a **única face que o cliente final vê**.
- **Brann = o plano de controle do dono.** O usuário Leaf **conversa com o Brann no dashboard** (`hermes.chat`) para **configurar e monitorar** sua Callima — em linguagem natural, sem tocar em n8n.
- **O que o usuário edita via Brann:** persona, nome, voz, **permissões**, o que ela deve falar/fazer — **dentro da gama de ferramentas que a Ginkgo dá** (os 4 ramos) e **dos tetos de governança** (`max_risk` da face × do tenant; Boundary). Configurar = escrever a **config por-tenant** da Callima (Persona/Face Registry).
- **Brann monitora:** vê conversas, leads, agenda, o que a Callima fez — a "analista de operação" (observability).
- **Diversificação:** o mesmo modelo abre outras skills e usos; nas outras plataformas, as faces **Alfred (Wave) / Nyra (Pyre)**.

**Reconciliação de nomes (cânone do tronco):** **Hermes = a mente única**; **Brann = a face do Hermes no LEAF** (o orquestrador que dirige a Callima e fala com o dono). "Brann executa" lê-se *"roteia pra um executor cego (n8n/Boundary) que executa"* — honest-data por construção. (Antes este doc usava "Hermes" pro papel do LEAF; o nome certo é **Brann**.)

## As duas peças

### Callima — a conversa (por-tenant; o ÚNICO que o usuário Leaf vê)
- **Papel:** transcrição (STT/TTS), contato (o canal WhatsApp), conversa (vender, qualificar, responder com a KB do tenant).
- **Limites (explícitos):** NUNCA executa efeito colateral; NUNCA confirma uma ação sem o resultado real do Hermes.
- **Memória:** janela de conversa controlada + RAG do tenant.
- **Quando precisa agir:** não chama tool — **emite uma intent estruturada**.
- **Objetivo mensurável:** conversão, captura limpa de intent, satisfação.

### Hermes — a orquestração ("Brann + analista de operação")
- **Papel:** recebe a intent, valida, **roteia**, executa, captura o **resultado real**, libera a confirmação honesta, loga, monitora, alimenta a dashboard.
- **"Brann" (cérebro operacional do Leaf):** playbook do tenant, regras de negócio e de escalonamento.
- **"Analista de operação":** observabilidade (sucesso/erro, intents presas, latência, custo), detecção de anomalia, audit log, alerta ao humano.
- **Roteia pra:**
  - **(a) Fluxo determinístico** — os ~90% bem-definidos (agendar, e-mail, follow-up, CRM).
  - **(b) MCP / API** — capacidade externa registrada.
  - **(c) LLM mais capaz** — os ~10% abertos/ambíguos que exigem raciocínio.
  - **(d) Handoff humano** — baixa confiança / fora do escopo permitido. Nunca chuta.
- **Credenciais por-tenant:** resolve via Vault/Boundary → usa o Google/e-mail/WhatsApp **do cliente**, não o do fundador.

## Os contratos (a cola entre as peças)
- **Intent** (Callima → Hermes): `{ tenant, contato, intent, payload, conversation_id, confidence }`
- **Result** (Hermes → Callima + dashboard): `{ intent_id, status: success|failed|pending, real_ref, message_to_client }`
- **Regra honest-data (estrutural):** a Callima só fala `message_to_client` quando `status=success`. Enquanto isso ela diz futuro ("deixa eu confirmar isso"). Ela **não tem como** mentir porque **não executa**.

## A pilha (camadas)
1. **Canal** — WhatsApp via Evolution (instância por-tenant). _Futuro: API oficial pra robustez (o Baileys dessincroniza — vide o incidente de hoje)._
2. **Callima** — conversa (barata, confiável no que faz bem).
3. **Hermes** — orquestração + observabilidade.
4. **Capacidades** — fluxos n8n determinísticos, MCPs, APIs, eventos de sistema. Cada uma com **contrato**. Um **registry**: adicionar skill = registrar uma capacidade, **não inchar a Callima**. (Reduz entropia: uma indireção limpa em vez de N tools no modelo fraco.)
5. **Dados/Governança (tronco ginkgo-tree)** — tenants, Vault (creds por-tenant), Boundary, dashboard (honest-data), audit log.

## Controle · monitoramento · desligamento (não-negociável)
- **Lista explícita de intents permitidas.** Desconhecida / baixa confiança → handoff humano.
- **Kill-switch** por-tenant e global → desliga execução autônoma (cai pra "só notificar/humano").
- **Todo intent logado** (auditável — quem pediu, o que decidiu, o que executou, o resultado).
- **Observabilidade:** sucesso/erro/latência/custo por intent — o painel do "analista de operação".

## Onde roda (bootstrap → produção)
- **Agora (n8n):** Callima (workflow) + **Hermes v0** (workflow roteador + branches determinísticos). Clone por-tenant interino.
- **Alvo (tronco):** Callima + Hermes migram pro **runtime governado** (Kernel/Boundary) — creds por-tenant nativas, dashboard nativa, auditoria first-class. **n8n é o bootstrap; o tronco é a casa de produção.**

## Sequência de construção
1. **[COWORK] Hermes v0 — primeira capacidade: `[[AGENDAR]]`.** Callima emite a intent → Hermes (branch determinístico) cria o evento de verdade (nó Calendar real) → confirma só no sucesso. **Prova o padrão e mata a alucinação de hoje.**
2. **[COWORK] Estende capacidades:** `[[EMAIL]]`, `[[FOLLOWUP]]`, `[[CRM]]` — cada uma um branch com contrato.
3. **[COWORK] Emagrece a Callima:** remove as tools de ação dela; deixa só conversa + emissão de intent + a regra "nunca confirme, o Hermes confirma".
4. **[CODE] Hermes governado no tronco:** contrato de intent como endpoint, Boundary resolve creds por-tenant, audit log, kill-switch, observabilidade. A Callima (n8n) chama o Hermes do tronco.
5. **[CODE] Dashboard consome os results** (agenda, e-mails, follow-ups) — honest-data ponta-a-ponta.

## Honest-data
- Callima nunca confirma o que não aconteceu (estrutural — ela não executa).
- Dashboard mostra só estado real (vindo dos `result` do Hermes).
- _Stopgap de prompt foi deprioritizado: sem clientes reais ainda (dogfood na conta do fundador), o fix certo é o Hermes/`[[AGENDAR]]`, não band-aid de prompt._

_Mantido pela Sexta-feira. Esta é a espinha da plataforma — atualizar a cada capacidade nova._
