---
title: "Lab - Estrutura Site Haven"
source: "https://chatgpt.com/g/g-p-6920bddfbb548191ac06d937cdb0b5c0/c/69517fbd-7d7c-8325-89fc-d9a39252fa66"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
seg., 29 de dez. às 0:21

seg., 29 de dez. às 3:26

![d395ccf6-4fe7-4acc-a277-e0f3798cbfd6.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000a1d871f59f65285fe763d6ee&ts=495691&p=fs&cid=1&sig=c1ff38a22c35c3dd9642c13ba8c27151755c21f61753b4f418a4a93cf3446bda&v=0)

Funciona — e **faz muito sentido**, desde que usado **do jeito certo**.

Vou ser direto e estratégico.

---

## Resposta curta

**Sim, usar o DeepSeek como backend é uma excelente escolha para a Haven**, especialmente se você quer:

- Alta capacidade de raciocínio
- Bom custo-benefício
- Ótimo desempenho em extração, lógica e decisões
- Menos dor de cabeça que LLM local no início

Mas **não como “chat simples”**.  
Ele precisa entrar como **motor cognitivo dentro de um backend orquestrado**.

---

## Por que DeepSeek combina com a Haven

A Haven não é:

> “responder perguntas sobre imóveis”

Ela é:

> **entender intenção + traduzir desejo + decidir próximo passo**

O DeepSeek é muito forte em:

- Raciocínio multi-etapas
- Síntese de contexto
- Extração estruturada (JSON)
- Lógica de decisão (if / else implícito)
- Menos “poesia vazia”, mais **pensamento**

Isso casa bem com:

- Investimento imobiliário
- Decisão de vida
- Conversas longas
- Conversão consultiva

---

## DeepSeek vs Ollama (decisão honesta)

### DeepSeek (API / hosted)

**Vantagens**

- Qualidade consistente
- Ótimo para produção
- Menos manutenção
- Melhor para lógica e estrutura
- Mais confiável para não “viajar”

**Desvantagens**

- Custo por token (mas ainda competitivo)
- Dependência externa

### Ollama + Qwen (local)

**Vantagens**

- Custo quase zero
- Total controle
- Privacidade máxima

**Desvantagens**

- Manutenção pesada
- Qualidade varia
- Alucina mais fácil se prompt falhar
- Tool-calling mais instável

👉 **Minha recomendação realista para a Haven:**

- **DeepSeek agora (produto real)**
- **Ollama depois (otimização / fallback / escala)**

---

## Arquitetura ideal usando DeepSeek

### 1️⃣ Frontend (Lovable)

- Apenas UI
- Campo de conversa
- Nada de lógica pesada
- Envia tudo para `/api/chat`

---

### 2️⃣ Backend (seu cérebro Haven)

Um serviço (FastAPI ou Node) com:

**Camadas claras:**

```markdown
[ Lovable ]
     ↓
[ API Haven ]
     ↓
[ Orquestrador ]
     ↓
[ DeepSeek ]
     ↓
[ Ferramentas ]
```

O DeepSeek **não decide tudo**.  
Ele **opina dentro de limites**.

---

### 3️⃣ Orquestrador (o segredo do produto)

Aqui está o diferencial que te separa de 99%:

O backend controla:

- Em que etapa o usuário está
- O que pode ou não ser perguntado
- Quando sugerir
- Quando calar
- Quando chamar humano

Exemplo de estados:

```markdown
INIT
→ INTENCAO
→ LOCAL
→ ORCAMENTO
→ OBJETIVO
→ CRITERIOS
→ BUSCA
→ VALIDACAO
→ HANDOFF
```

O DeepSeek recebe:

- Contexto atual
- Dados já confirmados
- Instruções duras (guardrails)

---

### 4️⃣ Uso correto do DeepSeek

#### System Prompt (fixo)

- Personalidade da Haven
- Regras legais
- Bloqueios (não inventar bairro, não prometer)
- Estilo de fala

#### User Prompt

- Mensagem do usuário

#### Tool / Schema Prompt

- Extração estruturada:
```markdown
{
  "intencao": "",
  "estado": "",
  "cidade": "",
  "faixa_valor": "",
  "objetivo": "",
  "status": ""
}
```

O backend valida.  
Se algo estiver vazio → **a IA não avança**.

---

## Busca de imóveis (ponto crítico)

DeepSeek **não deve “buscar na internet sozinho”**.

O correto:

1. IA define critérios
2. Backend chama:
	- Base própria
		- Parceiros
		- Portais (via scraping/API)
3. Backend retorna resultados
4. IA **explica e contextualiza**, não inventa

Isso evita:

- Alucinação
- Dados desatualizados
- Promessas falsas

---

## Conversão e ponte humana

Quando critérios fecham:

- Backend gera **Resumo do Perfil**
- Dispara handoff:
	- WhatsApp
		- CRM
		- Corretor parceiro

O corretor recebe:

- Quem é o lead
- O que ele quer
- Por que quer
- Orçamento real
- Grau de prontidão

Isso **aumenta conversão absurda**.

---

## Caminho recomendado (passo a passo)

1️⃣ DeepSeek como LLM principal  
2️⃣ Backend simples (FastAPI ou Node)  
3️⃣ Orquestrador com estados  
4️⃣ Extração estruturada obrigatória  
5️⃣ Lovable só como UI  
6️⃣ WhatsApp para handoff  
7️⃣ Depois: Ollama como fallback/escala

---

## Veredito final

> **DeepSeek é uma escolha madura para a Haven.**  
> Mais cérebro, menos firula.  
> Menos “chatbot”, mais **consultor invisível**.

Se quiser, no próximo passo eu:

- escrevo o **System Prompt definitivo da Haven para DeepSeek**
- desenho o **schema exato do backend**
- ou monto o **fluxo n8n / API / Lovable pronto pra rodar**

Escolha o próximo comando.

bora, me guie na construção exata e me ajude a vizualizar a forma final, haven deve ser capaz de ser a imobiliaria do povo, do pobre e do alto padrao, tem que entender pela conversa, sempre conversando como um psicologo particular, por audio ou texto, entender qual o imovel ideal que aquela pessoa procura e qual a realidade dela como ela poderia comprar tal imovel, entao buscar na internet uma opçao que se enquadre para ela e segura, fazer o contato e a verificação com a imobiliaria e finalmente fechar a transação conectando os dois e a haven ficando com uma porcentagem da venda

## Forma final da Haven (visão “produto pronto”)

Pense na Haven como um **piloto automático imobiliário** com 3 camadas:

**Camada 1 — Psicóloga (conversa):** entende pessoa, fase de vida, dor, sonho, limite real.  
**Camada 2 — Engenheira (tradução):** transforma desejo em critérios e viabilidade (financiamento, entrada, renda, risco).  
**Camada 3 — Detetive + Corretora (execução):** busca opções, valida, contata imobiliária/proprietário, organiza visita, e faz o handoff para fechamento com CRECI.

O site é o cockpit: o usuário só conversa. Por trás, o backend faz todo o trabalho pesado.

---

## Grafo mental do sistema (pipeline real)

```markdown
[Texto/Áudio]
   ↓
[Transcrição + Normalização]
   ↓
[Perfil Psicográfico + Intenção]
   ↓
[Viabilidade Financeira]
   ↓
[Critérios do Imóvel]
   ↓
[Busca (parceiros + internet)]
   ↓
[Triagem + Risco/Confiabilidade]
   ↓
[Validação humana (corretor)]
   ↓
[Contato com imobiliária/proprietário]
   ↓
[Visita + Documentos + Negociação]
   ↓
[Fechamento]
   ↓
[Fee Haven (%)]
```

---

## Regras de ouro do comportamento (pra não virar “chat bonito”)

1. **Nunca sugerir bairro/cidade antes de confirmar local.**
2. **Nunca prometer “imóvel seguro” sem checagem e fonte.**
3. **Sempre resumir o que entendeu** (estilo psicólogo) antes de avançar.
4. **Separar “conversa” de “ação”**: ação só com ferramentas/logs.
5. **Handoff para humano** quando: valores altos, documentação, urgência, ou qualquer incoerência.

---

## A “psicóloga imobiliária” (como a Haven conversa)

A Haven precisa operar com um loop fixo:

**(1) Acolhe → (2) Reflete → (3) Pergunta 1 coisa → (4) Confirma → (5) Avança**

Exemplo curto:

- “Entendi. Você quer X porque Y, e seu limite é Z. Faz sentido?”
- “Antes de eu buscar, me diz só uma coisa: sua cidade no Paraná é Curitiba ou outra?”

Ela não é vendedora. Ela é **clareza**.

---

## Escopo do produto: popular, médio e alto padrão

A diferença não é “tom”, é **estratégia e restrições**:

### Popular (povo)

- foco: financiamento/Minha Casa Minha Vida (se aplicável), entrada mínima, custo total, risco de golpe
- prioridade: documentação, bairro seguro, prestação que cabe no mês

### Médio

- foco: equilíbrio, liquidez, condomínio, localização, revenda

### Alto padrão

- foco: discrição, curadoria, visita qualificada, validação pesada, negociação e timing

A mesma IA faz todos. O que muda é o “modo” decidido pelo backend a partir do perfil/viabilidade.

---

## Construção exata (arquitetura recomendada)

### 1) Frontend (Lovable)

- UI de chat (texto + botão de áudio)
- envia para seu backend: `POST /api/chat`
- renderiza:
	- mensagens
		- “cards” de imóveis
		- CTA: “Agendar visita” / “Falar com corretor”

Nada de lógica no front.

---

### 2) Backend “Haven Core” (onde o produto vive)

Sugestão: **FastAPI (Python)** ou **Node**. Componentes:

1. **Session Service**: estado da conversa (etapa do funil)
2. **Profile Service**: perfil psicográfico + preferências
3. **Finance Service**: viabilidade (renda, entrada, prazo, parcela alvo)
4. **Search Service**: busca em fontes (parceiros + web)
5. **Risk/Trust Service**: score de confiabilidade (fonte, sinais de golpe, inconsistências)
6. **Handoff Service**: envia para corretor/CRM/WhatsApp (Chatwoot/Evolution)

E um **LLM Orchestrator** usando DeepSeek:

- “chat” para conversa
- “extract” para extrair JSON estruturado
- “policy” para checar regras (ex.: não inventar cidade)

---

### 3) Dados (Supabase/Postgres)

Tabelas mínimas:

- `leads` (id, nome, contato, estágio, cidade, faixa\_valor, objetivo)
- `messages` (lead\_id, role, content, timestamp)
- `preferences` (lead\_id, quartos, tipo, região, prioridades)
- `finance_profile` (lead\_id, renda, entrada, score\_aprox, parcela\_alvo)
- `property_candidates` (lead\_id, url, fonte, preço, cidade, atributos, trust\_score)
- `handoffs` (lead\_id, corretor\_id, status, resumo\_enviado)

---

## Áudio e texto (como fica robusto)

1. Usuário envia áudio no site
2. Backend chama **STT** (transcrição)
3. Salva transcrição + áudio (opcional)
4. Passa pro mesmo pipeline do chat

Importante: a Haven responde em **texto** e, se você quiser, também em **áudio TTS** (isso aumenta sensação “psicóloga”).

---

## Busca na internet (sem virar risco jurídico/qualidade)

A Haven não “navega como humano” sem controle. Você cria conectores:

### Fontes:

- **Parceiros (imobiliárias)**: o ideal (feed, planilha, API, ou scraping permitido)
- **Portais**: usar busca programática com normalização e cache
- **Classificados**: só com checagem forte

### Processo seguro:

- coletar candidatos
- extrair dados padronizados
- calcular trust\_score
- mandar para validação humana quando necessário

---

## Verificação (o “anti-golpe” obrigatório)

Haven precisa de um checklist automático + humano:

**Checklist básico**

- CNPJ / CRECI / endereço / telefone oficial
- consistência de preço vs região (outlier = alerta)
- imagens repetidas / suspeitas
- domínio/contato (se é empresa real)
- pedir documentação padrão antes de qualquer sinal verde

A IA pode orientar, mas **a validação final** precisa ser humana e registrada.

---

## Fechamento e % da venda (modelo prático)

Você pode operar de 3 formas:

1. **Parceria com imobiliárias** (recomendado)
- contrato: “leads + intermediação”
- % combinada por venda
- reduz risco e aumenta escala
2. **CRECI próprio + operação interna**
- Haven vira operação completa
- mais margem, mais responsabilidade
3. **Híbrido**
- popular/médio via parceiros
- alto padrão com operação interna

---

## O “cérebro” da Haven (prompt e controle)

A parte crítica não é “um prompt bonito”. É **dois prompts**:

1. **Prompt de conversa (psicóloga)**
2. **Prompt de extração (JSON rígido)**

E o backend decide: se `cidade` não confirmada → IA só pode perguntar cidade.  
Se `objetivo` não confirmado → IA só pode perguntar objetivo.  
Isso elimina 80% das alucinações.

---

## Caminho de execução (sem improviso)

### Etapa A — MVP conversacional confiável (2–5 dias de build)

- `/api/chat` com estado (INIT → LOCAL → FINANCE → CRITERIA)
- extração JSON
- salvar tudo no Supabase
- handoff para WhatsApp/Chatwoot com resumo

**Saída:** Haven já qualifica lead como “gente grande”.

### Etapa B — MVP de busca (5–10 dias)

- Search Service com 1–2 fontes (começa por parceiros)
- cards de imóveis no chat
- trust\_score simples

### Etapa C — Verificação + fechamento (contínuo)

- pipeline de validação humana
- modelos de mensagem para contatar imobiliárias
- CRM e acompanhamento de visita/documento

---

## Para visualizar a “tela final”

O site final tem 3 telas (só isso):

1. **Portal (chat)**
2. **Sugestões (cards)**
3. **Linha do tempo (status do caso)**
	- “Entendimento concluído”
		- “Busca em andamento”
		- “Verificação”
		- “Visita”
		- “Documentos”
		- “Fechamento”

Isso dá sensação de produto “sério”, não “chat”.

---

## Próximo passo (agora, sem enrolar)

Escolha o stack para eu te guiar com especificação exata (endpoints + schemas + prompts):

1. **FastAPI + Supabase + DeepSeek + Evolution/Chatwoot** (recomendado)  
	ou
2. **Node + Supabase + DeepSeek**

Se você disser **1 ou 2**, eu já te devolvo:

- lista exata de endpoints
- JSON schema de extração (perfil, finanças, critérios)
- state machine completa (com regras)
- prompt system da Haven “psicóloga” pronto pra produção

seg., 29 de dez. às 20:32

quais webhooks a haven precisaria para funcionar na pratica como https://www.chavesnamao.com.br/ funcionar como uma imobiliaria de verdade mas conversacional e que busca oq nao tem no catalogo

A Haven, na prática, vira uma “imobiliária de verdade” quando você trata tudo como **eventos + webhooks** (igual um sistema operacional): cada ação dispara um evento, registra no CRM e aciona o próximo módulo. O site conversacional é só a interface.

Abaixo está a lista dos **webhooks essenciais** (MVP → produção), no formato que você realmente vai implementar.

---

## 1) Webhooks de Conversa (entrada do produto)

### 1.1 POST /webhook/chat.message

**Origem:** Site (Lovable), App, Widget  
**Dispara quando:** usuário envia texto

**Payload mínimo:**

- `session_id`
- `lead_id` (se já existir)
- `channel` (`web`)
- `message.text`
- `meta` (ip, userAgent, page)

---

### 1.2 POST /webhook/chat.audio

**Origem:** Site/App  
**Dispara quando:** usuário envia áudio

**Payload:**

- `session_id`
- `audio.url` (ou base64)
- `audio.duration`
- `language` (opcional)

**Ações internas:**

- STT (transcrever) → vira um `chat.message` normal
- salva áudio e transcrição

---

### 1.3 POST /webhook/chat.handoff.requested

**Origem:** Orquestrador Haven  
**Dispara quando:** o fluxo decide “chamar humano” (CRECI)

**Payload:**

- `lead_id`
- `summary` (perfil + critérios + próximos passos)
- `priority` (`low|medium|high`)
- `reason` (ex.: “documentação”, “alto padrão”, “inconsistência”)

---

## 2) Webhooks de Qualificação (o “psicólogo” virando dados)

### 2.1 POST /webhook/lead.upsert

**Dispara quando:** a IA extrai dados novos e válidos do usuário

**Payload:**

- `lead_id`
- `name`
- `phone/email`
- `city/state`
- `intent` (`comprar|alugar|investir|vender`)
- `budget`
- `timeline`
- `family_context` (opcional)

---

### 2.2 POST /webhook/lead.profile.updated

**Dispara quando:** perfil psicográfico e preferências mudam

**Payload:**

- `lead_id`
- `preferences` (quartos, tipo, bairro, prioridades)
- `psychographic_tags` (ex.: “cauteloso”, “urgente”, “primeira compra”)
- `deal_stage`

---

### 2.3 POST /webhook/finance.prequal.updated

**Dispara quando:** Haven estima viabilidade financeira

**Payload:**

- `lead_id`
- `income_range`
- `down_payment_range`
- `installment_target`
- `financing_possible` (bool)
- `notes` (ex.: “precisa reduzir parcela”)

---

## 3) Webhooks de Catálogo (para funcionar como Chaves na Mão)

Aqui você precisa de duas fontes: **catálogo interno** + **busca externa**.

### 3.1 POST /webhook/properties.ingest

**Origem:** parceiros (imobiliárias), planilhas, APIs, feed  
**Dispara quando:** novos imóveis entram no seu catálogo

**Payload:**

- `source_id` (imobiliária X)
- `property_id_external`
- `address_region` (sem expor dados sensíveis no público)
- `price`
- `attributes` (quartos, vagas, m², tipo)
- `media` (fotos)
- `url`
- `availability_status`

> Isso é o que transforma a Haven em “portal” com base própria.

---

### 3.2 POST /webhook/properties.updated

**Dispara quando:** preço muda / status muda / vendido / alugado

**Payload:**

- `property_id`
- `changes`
- `timestamp`

---

## 4) Webhooks de Busca Externa (o diferencial “procura o que não tem”)

Isso aqui é o coração da promessa.

### 4.1 POST /webhook/search.requested

**Origem:** Orquestrador Haven  
**Dispara quando:** usuário definiu critérios suficientes e a Haven vai buscar

**Payload:**

- `lead_id`
- `search_criteria` (cidade, bairros, faixa, tipo, etc.)
- `search_mode` (`internal_only|partners|web`)
- `urgency`

---

### 4.2 POST /webhook/search.results

**Origem:** módulo de busca (crawler/API/parceiros)  
**Dispara quando:** resultados chegam

**Payload:**

- `lead_id`
- `results[]`:
	- `title`
		- `price`
		- `region`
		- `url`
		- `source`
		- `raw_data` (opcional)
- `retrieved_at`

---

### 4.3 POST /webhook/search.no\_results

**Dispara quando:** nada bom encontrado (e aí a Haven reage como consultora)

**Payload:**

- `lead_id`
- `criteria`
- `recommendation` (ex.: “ajustar bairro”, “aumentar faixa”, “esperar 2 semanas”)

> Observação crítica: “buscar na internet” tem implicações legais/ToS. O ideal é: **parcerias + feeds + APIs**. Crawler entra como camada adicional com cuidado.

---

## 5) Webhooks de Verificação e Anti-golpe (imobiliária séria)

### 5.1 POST /webhook/verification.requested

**Dispara quando:** a Haven precisa validar um imóvel/anúncio externo

**Payload:**

- `lead_id`
- `property_url`
- `source`
- `checks_required[]` (CNPJ, CRECI, endereço, etc.)

---

### 5.2 POST /webhook/verification.completed

**Dispara quando:** verificação conclui

**Payload:**

- `property_url`
- `trust_score` (0–100)
- `flags[]` (ex.: “preço fora do padrão”, “contato suspeito”)
- `verdict` (`approved|needs_human|rejected`)
- `evidence` (links/prints/infos)

---

## 6) Webhooks de Operação (agenda, visita, negociação)

### 6.1 POST /webhook/visit.requested

**Dispara quando:** usuário quer visitar

Payload:

- `lead_id`
- `property_id/url`
- `preferred_times[]`
- `contact`

### 6.2 POST /webhook/visit.scheduled

**Origem:** corretor/CRM/calendário  
**Dispara quando:** visita confirmada

---

### 6.3 POST /webhook/negotiation.updated

**Dispara quando:** proposta / contraproposta muda

Payload:

- `lead_id`
- `property_id`
- `offer_value`
- `status`

---

## 7) Webhooks de Documentos e Fechamento (onde nasce o %)

### 7.1 POST /webhook/docs.requested

**Dispara quando:** precisa gerar/solicitar docs

Payload:

- `lead_id`
- `doc_type` (proposta, contrato, etc.)
- `parties` (comprador, vendedor, imobiliária)

### 7.2 POST /webhook/docs.signed

**Origem:** DocuSign/assinatura digital  
**Dispara quando:** assinado

---

### 7.3 POST /webhook/deal.closed

**Dispara quando:** venda fechada

Payload:

- `lead_id`
- `property_id`
- `sale_value`
- `commission_total`
- `haven_fee_value`
- `payer` (imobiliária/parceiro)

> Esse webhook é literalmente o “som de caixa registradora”.

---

## 8) Webhooks de Pagamento (para receber sua porcentagem)

### 8.1 POST /webhook/payment.invoice.created

### 8.2 POST /webhook/payment.paid

**Origem:** Stripe/Asaas/etc.  
**Dispara quando:** fee da Haven pago

---

## 9) Webhooks de Notificação (multi-canal)

### 9.1 POST /webhook/notify.whatsapp

### 9.2 POST /webhook/notify.email

### 9.3 POST /webhook/notify.push

Confirmações, follow-ups, lembretes, status.

---

## O “mínimo que funciona” (MVP real)

Se você quiser rodar a Haven na prática com qualidade, o MVP precisa só destes 8:

1. `chat.message`
2. `chat.audio`
3. `lead.upsert`
4. `lead.profile.updated`
5. `search.requested`
6. `search.results`
7. `verification.completed`
8. `deal.closed`

O resto é escala e refinamento.

---

## Próximo passo: visualização final do fluxo (operacional)

Eu monto pra você, em seguida, um diagrama “lado a lado”:

**Usuário (site)** → **Haven Core (DeepSeek)** → **Busca (parceiros/web)** → **Verificação** → **Corretor/CRM** → **Docs** → **Fechamento** → **% Haven**

Só preciso que você responda 2 coisas (curto, sem burocracia):

1. Vai usar **Chatwoot** como caixa de entrada do corretor ou outro CRM?
2. WhatsApp via **Evolution API** ou Meta Cloud API?