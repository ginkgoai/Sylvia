# Brief Claude Design — telas Outbound + CRM (LEAF) — 2026-07-06

> Pronto pra colar. **Registro WARM do produto** (verde #12874A + creme #F4F0E6 + tinta escura, iOS-soft, cantos macios) — NÃO o neon da marca. honest-data é conteúdo. Callima como chip de mascote. **O kanban-pipeline é o herói.** Rouba o UX do Mailerfind (ver `50_Plataformas/benchmark_mailerfind.md`) mas com o nosso modelo governado. Refs de código: editor = Maily.to; tour = Driver.js/Onborda (ver `20_Conhecimento/pesquisa_gits_uteis.md`). Anexar mascotes transparentes de `brand/refs/transparent/`.

## Estilo (trava)
Dark-suave iOS, verde-sinal como accent único; **1 toque violeta** só no CTA cross-agente ("dar tarefa a outro agente"). Voz **1ª pessoa da Callima**. Badges de confiança: **"governado · auditável · honest-data · opt-out respeitado"**. Cards de dado vivo flutuando. Nada de banner de contagem-regressiva (fere honest-data).

## Tela 1 — Lead Finder (Fontes)
Escolher a fonte da cartela, com honestidade de consentimento:
- Cards de fonte: **Importar CSV/colar** (MVP, marca opt-in por lead) · **Google Maps** (empresa local por categoria+local) · **Instagram** (com selo ⚠️ "requer opt-in / respeita ToS").
- **Job de coleta com progresso REAL:** barra "592 de 88.662 · RODANDO 1%" (honest-data, igual Mailerfind).
- **Card de resultado:** "Encontrei **73 e-mails, 62 telefones** — **41 com opt-in**." (números provados; o resto fica inelegível pra abordagem, com badge).

## Tela 2 — Kanban CRM (HERÓI)
Pipeline como jornada, não tabela:
- Colunas: **Não abordado → Conversando → Frio → Convertido** (+ Perdido). Colunas configuráveis (StageManager).
- Card = lead (nome · empresa · need) + **badge de temperatura** (Quente/Morno/Frio, derivado do `intentScore` REAL — separado do estágio) + **chip da Callima** quando ela está atuando naquele lead.
- **honest-data:** o card **só anda sozinho com Event provado** (abordado→enviado; conversando→resposta real; convertido→pagamento). Arrastar manual é permitido (ação do dono).
- CTA no topo: **"Iniciar prospecção"** (abre o wizard de campanha) + contador "eu abordo 1 a 1, no seu ritmo".

## Tela 3 — Campanha (wizard + editor) — roubar o Mailerfind
Fluxo curto, done-for-you:
1. **Origem:** Análise (um Lead Finder) **| Lista** (CSV).
2. **Modelos IA:** 3 variantes geradas + **"Gerar novos"** (a Nyra escreve; variáveis `{{primeiro_nome}}`).
3. **Editor** (estilo Maily): Assunto + Corpo rich-text + **Variáveis** + **Email AI** (gera/reescreve) + **Pré-visualização/HTML**.
4. **Definições:** **Canal = E-mail (cold) | WhatsApp (só warm/opt-in)** · **Cadência** ("~25/dia, horário comercial, warmup") · remetente.
5. **Tela "Excelente!"** — checklist honest-data com números provados: "✓ 41 leads elegíveis ✓ modelo pronto ✓ canal conectado".
6. **Botão "Aprovar campanha"** = o **HITL** (a aprovação é a attestation; aí a engine dispara sequencial sozinha).

## Tela 4 — Inbox unificada
As respostas caem aqui e **a Callima assume** (1ª pessoa). Bolhas **honest-data** (só "enviada" após confirmação do sistema). Handoff pro humano a 1 clique. Cada conversa mostra de qual campanha/lead veio.

## Cross-cutting — Onboarding guiado
Tour passo-a-passo estilo **Driver.js/Onborda** (overlay escurece a tela + **spotlight** no elemento + tooltip "X de N"), ensinando cada área na 1ª vez (conectar canal → importar cartela → aprovar campanha → ver o kanban andar). No registro WARM.

## O diferencial a mostrar na tela
"O Mailerfind te dá a lista e envia. **Eu abordo, converso, agendo e vendo — e mostro a prova de cada passo no seu kanban.**" (Callima, 1ª pessoa.)
