---
title: "Engenharia Reversa MayaHub"
source: "https://chatgpt.com/c/6a6cf752-d934-83e9-98c0-c80e2790ca98"
author:
published:
created: 2026-08-02
description: "ChatGPT conversation with 6 messages"
tags:
  - "clippings"
---
**Você disse**

O número 6 acho parecido

[![](https://chatgpt.com/images/ecosystem/apps/github/icon.png)](https://chatgpt.com/plugins/plugin_connector_1p_1a69035c238881919c4190932b2df699?plugin_detail_origin=inline_selection_pill)

[GitHub](https://chatgpt.com/plugins/plugin_connector_1p_1a69035c238881919c4190932b2df699?plugin_detail_origin=inline_selection_pill) Leaf e workforce. https://mayahub.ai/ faça uma engenharia reversa aqui (penso como feature importantíssima atendimento de ligações e follow up e avisos por ligação)

---

A atualização mais parecida foi o **Grok Voice Agent Builder**, lançado em beta em **1º de julho de 2026**. Ele permite criar agentes telefônicos por descrição em linguagem natural e reúne telefonia, conhecimento, ferramentas, guardrails, MCPs e observabilidade em uma única interface. Também aceita números existentes via SIP, APIs próprias, servidores MCP e clientes WebSocket. [^1]

Ele é a camada no-code construída sobre uma sequência de lançamentos:

1. **Grok Voice Agent API — dezembro de 2025:** runtime de conversação em voz com tool calling.
2. **Grok Voice Think Fast 1.0 — abril de 2026:** modelo especializado em ligações complexas, vendas, suporte e agendamento.
3. **Custom Voices — abril de 2026:** clonagem autorizada da voz da empresa.
4. **Voice Agent Builder — julho de 2026:** painel no-code completo.
5. **21 novas vozes — julho de 2026:** catálogo multilíngue voltado a suporte, publicidade, educação e personagens. [^2]

## O que a xAI construiu de verdade

A maioria das plataformas de voz monta um Frankenstein:

```
Ligação
  ↓
Speech-to-Text
  ↓
LLM
  ↓
Text-to-Speech
  ↓
Ligação
```

A xAI oferece um caminho **speech-to-speech integrado**. Isso elimina parte das viagens entre provedores, reduzindo latência, custo intermediário e pontos de falha. O agente recebe áudio, raciocina, usa ferramentas e produz áudio dentro do mesmo runtime. [^1]

O Grok Voice permite configurar por sessão:

- Prompt e comportamento.
- Voz padrão ou voz clonada.
- Raciocínio ativado ou desativado.
- Detecção de fala e silêncio.
- Velocidade de voz.
- Termos específicos para melhorar reconhecimento.
- Idioma, incluindo `pt-BR`.
- RAG e busca em arquivos.
- Funções próprias.
- Web search, X search e MCPs.
- Retomada de sessão após desconexão. [^3]

A xAI diz que o modelo foi treinado para telefonia degradada, ruídos, sotaques, interrupções e fluxos com várias ferramentas. A empresa também o posiciona para suporte, vendas telefônicas, reservas e agendamento. Esses benchmarks são publicados pela própria xAI, portanto devem ser validados por nós em testes brasileiros antes de virarem argumento comercial. [^4]

---

## Como a telefonia funciona

## Entrada da chamada

```
Cliente liga
   ↓
Operadora / número SIP
   ↓
xAI SIP Gateway
   ↓
Webhook assinado para Workforce
   ↓
Workforce identifica organização e agente
   ↓
Workforce abre WebSocket usando call_id
   ↓
Callima atende
```

A xAI permite registrar um número trazido pelo cliente, direcioná-lo para `sip.voice.x.ai` e receber um webhook assinado `realtime.call.incoming`. O Workforce então abre uma sessão WebSocket usando o `call_id` e envia a configuração da Callima para aquela ligação. [^5]

Durante a chamada, a API suporta:

- Transferência para número humano por SIP.
- Encerramento programático.
- Teclas telefônicas DTMF.
- Codecs próprios de telefonia.
- Integração com Twilio, Telnyx, Plivo ou outro provedor SIP. [^5]

## Limitação importante

A documentação pública atual detalha muito bem **chamadas inbound**, controle da chamada e conexão SIP, mas não apresenta uma API nativa clara para criar campanhas outbound em massa.

Portanto:

> **xAI deve ser o cérebro e o motor de áudio. O discador outbound deve continuar sob responsabilidade do carrier.**

Para outbound:

```
Workforce Scheduler
   ↓
Twilio / Telnyx / operadora SIP inicia a chamada
   ↓
Ao atender, carrier conecta com xAI SIP
   ↓
Grok Voice conduz a conversa
```

Isso também facilita trocar a xAI por outro runtime sem reconstruir toda a telefonia.

---

## xAI versus MayaHub versus Workforce

| Camada | MayaHub | Grok Voice Builder | Ginkgo Workforce |
| --- | --- | --- | --- |
| Telefonia | Agregada/white-label | SIP e números xAI | Abstração multi-provider |
| Modelo de voz | Terceiros | Speech-to-speech Grok | Grok inicialmente |
| CRM | Básico ou integração | Integrações | LEAF como fonte da verdade |
| Ferramentas | Automação própria | Functions e MCP | Skill Engine governado |
| Follow-up | Campanhas | Configuração de agente | Motor de jornadas |
| Governança | Configuração da plataforma | Guardrails xAI | Policies, aprovação, orçamento |
| Multiagente | Limitado | Agentes isolados | Callima, Eliza e futuros workers |
| Diferencial | Revenda operacional | Infraestrutura vertical | Força de trabalho digital completa |

A arquitetura certa é:

> **Grok Voice = sistema nervoso da voz.  
> Workforce = cérebro operacional e sistema de controle.  
> LEAF = memória, CRM e interface.**

O Workforce já foi definido como o monorepo da força de trabalho digital: Callima atende, Eliza coordena, Connections conecta sistemas e o Skill Engine governa permissões, risco e consumo.

O LEAF permanece como CRM WhatsApp-first, API, dashboard e fonte canônica dos dados comerciais.

---

## PRD técnico — Workforce Voice

**Nome interno:** Workforce Voice Runtime  
**Feature comercial:** Leaf Voice  
**Repositório proprietário:** `ginkgoai/ginkgo-workforce`  
**Versão:** PRD 1.0  
**Status:** proposta para implementação  
**Documento sugerido:** `docs/PRD_WORKFORCE_VOICE.md`

---

## 1\. Visão do produto

Criar uma infraestrutura multi-tenant para que os agentes do Ginkgo Workforce possam:

- Atender chamadas recebidas.
- Realizar chamadas de follow-up.
- Confirmar e remarcar compromissos.
- Qualificar leads.
- Recuperar oportunidades.
- Consultar sistemas durante a ligação.
- Transferir chamadas para humanos.
- Registrar resultados estruturados.
- Coordenar ações posteriores em WhatsApp, e-mail e CRM.

A feature não será apenas uma “IA que fala”. Será um **canal de execução do Workforce**.

---

## 2\. Problema

O LEAF atualmente opera principalmente por canais assíncronos, especialmente WhatsApp. Entretanto:

- Muitos clientes não respondem mensagens.
- Confirmações urgentes exigem contato imediato.
- Ligações recebidas são perdidas fora do expediente.
- Agendamentos demandam idas e voltas.
- Equipes deixam leads sem acompanhamento.
- Informações das ligações ficam fora do CRM.
- Ferramentas de voz existentes são sistemas isolados.

O Workforce Voice deve transformar qualquer evento comercial relevante em uma possível ação telefônica governada.

---

## 3\. Objetivos

### Objetivos funcionais

1. Atender ligações 24/7.
2. Identificar o contato pelo número.
3. Carregar contexto da organização e do LEAF.
4. Executar ferramentas durante a conversa.
5. Transferir para humano quando necessário.
6. Criar follow-ups automáticos.
7. Armazenar transcrição, resumo e resultado.
8. Acionar o próximo canal automaticamente.
9. Controlar custos e limites por organização.
10. Permitir substituição de provider.

### Não objetivos do MVP

- Construir infraestrutura SIP própria.
- Desenvolver modelo STT/TTS proprietário.
- Oferecer call center humano completo.
- Criar discador preditivo.
- Fazer campanhas frias em massa.
- Colocar ferramentas financeiras críticas diretamente nas mãos do modelo.
- Criar uma nova interface de CRM dentro do Workforce.

---

## 4\. Princípio arquitetural

### Workforce é o plano de controle

O Workforce decide:

- Quem pode ligar.
- Para quem pode ligar.
- Quando pode ligar.
- Qual agente será usado.
- Quais ferramentas estarão disponíveis.
- Quanto pode ser gasto.
- Quando exigir aprovação.
- Qual ação acontece depois da chamada.

### Provider é o plano de mídia

A xAI ou outro provider executa:

- Entrada e saída de áudio.
- Detecção de fala.
- Raciocínio conversacional em tempo real.
- Síntese da voz.
- Emissão de tool calls.
- Ponte de áudio com SIP.

Nunca deixar regras comerciais críticas somente no prompt. Prompt não é firewall; é um post-it muito eloquente.

---

## 5\. Arquitetura proposta

```
┌───────────────────────────────────────────────────────┐
│                         LEAF                          │
│ CRM · Contatos · Agenda · Pipeline · Timeline · UI   │
└──────────────────────────┬────────────────────────────┘
                           │ REST / Events
                           ▼
┌───────────────────────────────────────────────────────┐
│                  GINKGO WORKFORCE                     │
│                                                       │
│  Voice API       Follow-up Engine     Campaign Engine │
│  Session Runtime Skill Engine         Tool Gateway    │
│  Policy Engine   Provider Router      Event Bus       │
│  Audit Log       Cost Engine          Scheduler       │
└─────────────┬──────────────────────────┬───────────────┘
              │                          │
              ▼                          ▼
┌─────────────────────────┐   ┌─────────────────────────┐
│ xAI Speech-to-Speech    │   │ Connections             │
│ WebSocket · SIP · Voice │   │ Calendar · CRM · ERP    │
└─────────────┬───────────┘   │ Payments · WhatsApp     │
              │               └─────────────────────────┘
              ▼
┌─────────────────────────┐
│ Twilio / Telnyx / SIP   │
│ PSTN · Número · Discador│
└─────────────────────────┘
```

---

## 6\. Componentes

### 6.1 Voice API

API pública interna usada pelo LEAF e pelos agentes.

Responsabilidades:

- Criar chamadas.
- Consultar chamadas.
- Cancelar chamadas.
- Testar agentes.
- Registrar números.
- Gerenciar configurações.
- Receber webhooks.
- Expor transcrições e resultados.

### 6.2 Voice Session Runtime

Processo responsável por uma chamada ativa.

Responsabilidades:

- Resolver `org_id`.
- Resolver número e agente.
- Buscar configurações.
- Criar prompt contextual.
- Montar ferramentas permitidas.
- Abrir e manter WebSocket.
- Processar eventos do provider.
- Persistir transcrição incremental.
- Aplicar timeouts.
- Recuperar sessões.
- Encerrar e consolidar resultado.

Cada ligação é uma unidade isolada:

```
VoiceSession
├── organization
├── agent
├── contact
├── call policy
├── provider session
├── tool allowlist
├── transcript buffer
├── usage meter
└── outcome collector
```

### 6.3 Provider Router

Interface desacoplada do fornecedor:

```typescript
export interface VoiceProvider {
  registerNumber(input: RegisterNumberInput): Promise<RegisteredNumber>;

  createInboundSession(
    input: InboundSessionInput
  ): Promise<ProviderSession>;

  startOutboundCall(
    input: OutboundCallInput
  ): Promise<ProviderCall>;

  transferCall(
    providerCallId: string,
    destination: string
  ): Promise<void>;

  hangupCall(providerCallId: string): Promise<void>;

  parseWebhook(
    headers: Record<string, string>,
    body: unknown
  ): Promise<VoiceProviderEvent>;

  getUsage(providerCallId: string): Promise<ProviderUsage>;
}
```

Implementações:

```
XaiVoiceProvider       MVP
TwilioVoiceProvider    telefonia e discagem
TelnyxVoiceProvider    alternativa SIP
RetellVoiceProvider    futuro
VapiVoiceProvider      futuro
```

### 6.4 Skill Engine Integration

O modelo não recebe acesso irrestrito aos sistemas.

Fluxo:

```
Grok solicita ferramenta
        ↓
Voice Runtime envia ao Tool Gateway
        ↓
Skill Engine valida:
- organização
- agente
- permissão
- risco
- orçamento
- parâmetros
- necessidade de aprovação
        ↓
Connections executa
        ↓
Resultado sanitizado retorna ao modelo
```

Ferramentas iniciais:

```
identify_contact
get_contact_context
get_available_slots
book_appointment
reschedule_appointment
cancel_appointment
get_order_status
create_follow_up
update_lead_stage
send_whatsapp_confirmation
transfer_to_human
request_human_assistance
register_do_not_call
```

Ferramentas de alto risco ficam fora do MVP:

```
issue_refund
charge_payment
cancel_contract
change_bank_data
bulk_contact
```

### 6.5 Follow-up Engine

Transforma eventos em ações futuras.

Exemplo:

```yaml
trigger: appointment.created
conditions:
  appointment_status: scheduled
sequence:
  - delay: 48h_before
    channel: whatsapp
  - condition: no_response
    delay: 24h_before
    channel: voice
  - condition: no_answer
    delay: 4h
    channel: voice
    max_attempts: 2
  - condition: confirmed
    action: close_sequence
```

### 6.6 Outbound Dialer

Responsável por:

- Filas.
- Priorização.
- Concorrência.
- Retentativas.
- Horários permitidos.
- Identificação de chamadas.
- Integração com carrier.
- Controle de campanhas.

O carrier inicia a chamada; o Grok assume quando o contato atende.

### 6.7 Outcome Engine

Não confiar apenas em resumos livres do modelo.

Ao final, produzir saída estruturada:

```json
{
  "technical_status": "completed",
  "business_outcome": "appointment_confirmed",
  "intent_completed": true,
  "contact_verified": true,
  "sentiment": "neutral",
  "human_handoff": false,
  "next_action": {
    "type": "send_whatsapp_confirmation",
    "execute_at": "now"
  },
  "captured_fields": {
    "appointment_id": "apt_123",
    "confirmed_date": "2026-08-03T14:00:00-03:00"
  }
}
```

---

## 7\. Fluxos principais

### 7.1 Ligação inbound

```
1. Cliente liga.
2. Carrier direciona para xAI SIP.
3. xAI envia webhook assinado ao Workforce.
4. Workforce valida assinatura e resolve o número.
5. Número determina org_id e agent_id.
6. Workforce procura contato pelo telefone.
7. Skill Engine gera permissões daquela sessão.
8. Voice Runtime abre WebSocket.
9. Callima recebe contexto mínimo necessário.
10. Conversa e ferramentas são executadas.
11. Se necessário, a chamada é transferida.
12. Outcome Engine consolida o resultado.
13. LEAF recebe evento e atualiza timeline.
14. Follow-up Engine agenda a próxima ação.
```

### 7.2 Follow-up outbound

```
1. Evento do LEAF gera follow-up.
2. Scheduler verifica horário, consentimento e orçamento.
3. Job entra na fila BullMQ.
4. Carrier disca.
5. Quando atendida, chamada é conectada ao runtime de voz.
6. Callima apresenta contexto e finalidade.
7. Resultado é estruturado.
8. LEAF e agenda são atualizados.
9. WhatsApp de confirmação pode ser enviado.
```

### 7.3 Transferência humana

```
1. Callima detecta necessidade de humano.
2. Consulta rota de escalonamento.
3. Verifica horário e disponibilidade.
4. Resume o contexto.
5. Realiza SIP REFER.
6. Envia resumo ao atendente.
7. Registra handoff no LEAF.
```

### 7.4 Aviso por ligação ao proprietário

Eliza pode ligar ao proprietário somente em eventos de alta prioridade:

- Lead VIP esperando resposta.
- Falha operacional crítica.
- Pagamento relevante vencido.
- Agenda com conflito grave.
- Cliente solicitando escalonamento urgente.

Regra:

```
evento comum → dashboard/WhatsApp
evento importante → WhatsApp
evento crítico e não reconhecido → ligação da Eliza
```

---

## 8\. Modelo de dados

### voice\_providers

```sql
id
name
provider_type
status
config_encrypted
created_at
updated_at
```

### voice\_numbers

```sql
id
org_id
provider_id
external_id
phone_number
sip_uri
country_code
inbound_enabled
outbound_enabled
agent_id
webhook_secret_ref
status
created_at
```

### voice\_agent\_configs

```sql
id
org_id
agent_id
provider
provider_model
voice_id
language
instructions_template
greeting_template
reasoning_effort
vad_threshold
silence_duration_ms
idle_timeout_ms
max_duration_seconds
tool_policy_id
transfer_policy_id
recording_enabled
transcription_enabled
status
version
```

### voice\_calls

```sql
id
org_id
contact_id
agent_id
number_id
provider
provider_call_id
direction
purpose
technical_status
business_outcome
started_at
answered_at
ended_at
duration_seconds
audio_seconds
cost_provider
cost_carrier
cost_total
recording_uri
transcript_uri
summary
structured_outcome_json
campaign_id
follow_up_id
correlation_id
```

### voice\_call\_events

```sql
id
org_id
call_id
sequence
event_type
provider_event_id
payload_json
occurred_at
```

### voice\_tool\_executions

```sql
id
org_id
call_id
skill_id
tool_name
risk_level
input_json
output_json
approval_status
latency_ms
status
created_at
```

### follow\_up\_sequences

```sql
id
org_id
name
trigger_type
conditions_json
steps_json
status
```

### follow\_up\_jobs

```sql
id
org_id
sequence_id
contact_id
related_entity_type
related_entity_id
channel
scheduled_at
attempt
max_attempts
status
outcome
```

### communication\_preferences

```sql
id
org_id
contact_id
voice_allowed
whatsapp_allowed
email_allowed
allowed_hours_json
timezone
do_not_call
consent_source
consent_at
revoked_at
```

### voice\_usage\_ledger

```sql
id
org_id
call_id
provider
audio_seconds
carrier_seconds
provider_cost
carrier_cost
billed_amount
created_at
```

---

## 9\. Estados

### Estado técnico

```
created
queued
dialing
ringing
answered
active
transferring
completed
no_answer
busy
voicemail
rejected
cancelled
failed
```

### Resultado comercial

```
qualified
appointment_booked
appointment_confirmed
appointment_rescheduled
support_resolved
callback_requested
payment_promised
not_interested
wrong_number
do_not_call
human_required
unknown
```

Separar os dois é obrigatório. `completed` significa apenas que a tecnologia funcionou, não que o objetivo comercial foi atingido.

---

## 10\. APIs

### Números

```
POST   /v1/voice/numbers
GET    /v1/voice/numbers
GET    /v1/voice/numbers/:id
PATCH  /v1/voice/numbers/:id
DELETE /v1/voice/numbers/:id
```

### Agentes

```
POST  /v1/voice/agents/:agentId/config
GET   /v1/voice/agents/:agentId/config
PATCH /v1/voice/agents/:agentId/config
POST  /v1/voice/agents/:agentId/test
```

### Chamadas

```
POST /v1/voice/calls
GET  /v1/voice/calls
GET  /v1/voice/calls/:id
POST /v1/voice/calls/:id/cancel
POST /v1/voice/calls/:id/transfer
POST /v1/voice/calls/:id/hangup
GET  /v1/voice/calls/:id/transcript
GET  /v1/voice/calls/:id/events
```

### Follow-up

```
POST  /v1/follow-ups/sequences
GET   /v1/follow-ups/sequences
PATCH /v1/follow-ups/sequences/:id
POST  /v1/follow-ups/evaluate
POST  /v1/follow-ups/jobs/:id/execute
POST  /v1/follow-ups/jobs/:id/cancel
```

### Webhooks

```
POST /v1/webhooks/voice/xai
POST /v1/webhooks/voice/twilio
POST /v1/webhooks/voice/telnyx
POST /v1/webhooks/leaf/events
```

---

## 11\. Eventos internos

```
voice.call.requested
voice.call.queued
voice.call.ringing
voice.call.answered
voice.call.started
voice.call.tool_requested
voice.call.tool_completed
voice.call.transferred
voice.call.completed
voice.call.failed
voice.call.outcome_ready
follow_up.created
follow_up.due
follow_up.executed
follow_up.completed
contact.do_not_call_registered
usage.voice_recorded
budget.voice_threshold_reached
```

Payload padrão:

```json
{
  "event_id": "evt_uuid",
  "event_type": "voice.call.completed",
  "org_id": "org_uuid",
  "correlation_id": "corr_uuid",
  "entity_id": "call_uuid",
  "occurred_at": "2026-07-31T19:30:00Z",
  "data": {}
}
```

---

## 12\. Estrutura do monorepo

```
ginkgo-workforce/
├── apps/
│   ├── api/
│   ├── voice-runtime/
│   ├── scheduler/
│   └── worker/
│
├── packages/
│   ├── voice-core/
│   ├── provider-xai/
│   ├── provider-twilio/
│   ├── provider-telnyx/
│   ├── skill-engine/
│   ├── policy-engine/
│   ├── connections-sdk/
│   ├── event-bus/
│   ├── observability/
│   └── contracts/
│
├── agents/
│   ├── callima/
│   │   ├── voice/
│   │   └── policies/
│   └── eliza/
│       ├── voice/
│       └── policies/
│
├── db/
│   ├── schema/
│   └── migrations/
│
├── docs/
│   ├── PRD_WORKFORCE_VOICE.md
│   ├── VOICE_ARCHITECTURE.md
│   └── PROVIDER_XAI.md
│
└── tests/
    ├── contract/
    ├── integration/
    ├── simulations/
    └── load/
```

---

## 13\. Segurança e governança

### Regras obrigatórias

- Validar assinatura dos webhooks.
- Isolar todas as chamadas por `org_id`.
- Não enviar credenciais ao modelo.
- Criptografar configuração SIP.
- Usar allowlist de ferramentas por sessão.
- Sanitizar retorno das ferramentas.
- Bloquear prompt injection por conteúdo recuperado.
- Registrar toda execução.
- Limitar custo por chamada.
- Limitar duração.
- Aplicar rate limit por organização.
- Manter kill-switch global e por tenant.
- Armazenar gravações em bucket privado.
- Aplicar retenção configurável.
- Registrar consentimento e opt-out.

Para voz personalizada, a xAI exige verificação de presença e consentimento do dono da voz; o Workforce deve persistir o comprovante e o identificador da autorização. [^6]

### Níveis de risco

| Nível | Exemplo | Política |
| --- | --- | --- |
| 0 | Consultar FAQ | Automático |
| 1 | Consultar agenda | Automático |
| 2 | Criar agendamento | Automático com confirmação verbal |
| 3 | Alterar registro sensível | Confirmação reforçada |
| 4 | Pagamento, reembolso, contrato | Aprovação humana |
| 5 | Ação proibida | Bloqueada |

---

## 14\. Observabilidade

Métricas técnicas:

- Latência até primeira resposta.
- Latência média por turno.
- Taxa de interrupção correta.
- Taxa de tool call bem-sucedida.
- Quedas de WebSocket.
- Falhas de SIP.
- Duração média.
- Custo por minuto.
- Concorrência ativa.
- Transferências concluídas.

Métricas comerciais:

- Taxa de atendimento.
- Confirmações por ligação.
- Agendamentos realizados.
- Leads qualificados.
- Recuperação de leads.
- Conversão após follow-up.
- Taxa de opt-out.
- Custo por resultado.
- Receita influenciada por chamada.
- Redução de no-show.

A documentação atual da xAI informa preço inicial de **US$ 0,05 por minuto de áudio**, limite público padrão de **10 sessões simultâneas por equipe** e sessão máxima de 120 minutos. O Voice Agent Builder acrescenta US$ 0,01 por minuto ao usar o número provisionado pela própria xAI. Esses valores devem entrar no Cost Engine como configuração, nunca hardcoded. [^7]

---

## 15\. Critérios de aceite do MVP

O MVP estará concluído quando:

1. Uma organização puder registrar um número SIP.
2. Uma chamada inbound criar uma sessão isolada.
3. Callima identificar um contato existente.
4. Callima consultar dados do LEAF.
5. Callima consultar horários.
6. Callima criar ou remarcar um agendamento.
7. Callima transferir para humano.
8. A chamada gerar transcrição.
9. O resultado comercial for estruturado.
10. A timeline do LEAF for atualizada.
11. Um follow-up outbound puder ser agendado.
12. Custos forem registrados no ledger.
13. Opt-out bloquear chamadas futuras.
14. Kill-switch interromper novas chamadas.
15. Testes provarem ausência de vazamento entre tenants.

---

## Épicos de implementação

## Épico 0 — Fundação

- Monorepo.
- PostgreSQL.
- Redis/BullMQ.
- Contratos de eventos.
- Multi-tenancy.
- Configuração e secrets.
- Observabilidade básica.

## Épico 1 — Provider xAI

- Webhook assinado.
- Registro BYO SIP.
- WebSocket runtime.
- Eventos de áudio e transcrição.
- Transferência.
- Encerramento.
- DTMF.
- Metering.

## Épico 2 — Callima Voice

- Prompt builder.
- Identificação de contato.
- Context loader.
- Ferramentas iniciais.
- Saída estruturada.
- Sandbox web para testes.

## Épico 3 — Integração LEAF

- Eventos LEAF → Workforce.
- Workforce → timeline LEAF.
- Agenda.
- Contatos.
- Pipeline.
- Histórico omnichannel.

## Épico 4 — Follow-up Engine

- Regras.
- Sequências.
- Scheduler.
- Retentativas.
- Fallback WhatsApp.
- Opt-out.
- Controle de horário.

## Épico 5 — Outbound Carrier

- Twilio ou Telnyx.
- Discagem individual.
- Filas.
- Concorrência.
- Callbacks.
- Custos combinados carrier + xAI.

## Épico 6 — Governança

- Skill Engine.
- Aprovações.
- Limites financeiros.
- Auditoria.
- Retenção.
- Policies por tenant.

## Épico 7 — Eliza Voice

- Alertas críticos.
- Resumo executivo.
- Confirmação de ações.
- Escalonamento multicanal.

---

## Decisão final de stack

Para a primeira versão:

```
Runtime de voz:       xAI Speech-to-Speech
Telefonia inbound:    SIP direto
Carrier Brasil:       validar Telnyx, Twilio e operadora SIP local
Discagem outbound:    carrier
Orquestração crítica: código TypeScript
Filas e scheduler:    Redis + BullMQ
Automação periférica: n8n
Banco Workforce:      PostgreSQL
CRM/fonte comercial:  LEAF
Ferramentas:           Workforce Skill Engine
Integrações:           Connections / MCP / APIs
Observabilidade:       OpenTelemetry + logs estruturados
```

Não usaria o **Voice Agent Builder** como núcleo do produto. Ele serve para criar protótipos e comparar vozes rapidamente. Em produção, usaria a API direta, porque o Builder concorreria com o próprio painel e a própria governança do Workforce.

O desenho estratégico é simples:

> **Não construir outro MayaHub.  
> Construir o sistema operacional que pode usar Grok Voice, trocar Grok Voice e coordenar uma empresa inteira por voz.**

---

**Você disse**

Neste caso elevenlabs não supre?

---

Sim. **Para o Workforce Voice, a ElevenLabs supre praticamente toda a camada de voz e telefonia inteligente — e hoje parece uma escolha mais completa para o MVP do que usar a xAI diretamente.**

Ela não supre o **Workforce inteiro**, mas elimina boa parte do reator de áudio que teríamos de construir.

## O que a ElevenLabs já entrega

| Necessidade | ElevenLabs |
| --- | --- |
| Conversação de voz em tempo real | Sim |
| Voz natural em português | Sim |
| Clonagem de voz | Sim |
| Ligações recebidas | Sim |
| Ligações realizadas | Sim |
| Twilio nativo | Sim |
| SIP trunk próprio | Sim |
| Campanhas em lote | Sim |
| Controle de concorrência | Sim |
| Transferência para humano | Sim |
| Transferência entre agentes | Sim |
| Tools por API/webhook | Sim |
| MCP | Sim |
| RAG/base de conhecimento | Sim |
| Contexto dinâmico por chamada | Sim |
| Gravação e transcrição | Sim |
| Análise e resultado estruturado | Sim |
| Webhook pós-ligação | Sim |

A ElevenLabs oferece telefonia inbound e outbound tanto pela integração nativa com Twilio quanto por SIP trunking. Ela também possui endpoint específico para iniciar ligações outbound e um módulo de chamadas em lote com listas, variáveis personalizadas, agendamento e limite de concorrência. [^8]

Durante a conversa, os agentes podem executar webhook tools, acessar MCPs, consultar bases RAG e transferir a ligação para outro agente ou para um número humano. [^9]

Depois da ligação, a plataforma pode enviar ao Workforce transcrição completa, áudio, resumo, avaliação de sucesso, sentimento e campos estruturados extraídos da conversa. Os webhooks possuem assinatura HMAC para validação. [^10]

## Então por que ainda precisamos do Workforce?

Porque a ElevenLabs é o **sistema vocal**, não o sistema operacional da empresa.

Ela consegue dizer:

> “O cliente pediu para remarcar para sexta-feira.”

O Workforce precisa decidir:

- Esse cliente realmente existe no LEAF?
- Ele pode remarcar?
- Quais horários estão disponíveis?
- Essa ferramenta está autorizada?
- Precisa de confirmação adicional?
- O cliente consentiu em receber ligações?
- Quantas tentativas já foram feitas?
- Quanto essa organização pode gastar?
- Qual próximo canal deve ser acionado?
- O resultado deve alterar qual etapa do funil?

A separação correta fica:

```
ElevenLabs
├── telefonia
├── voz
├── conversa em tempo real
├── interrupções e silêncio
├── transferência
├── campanhas
├── transcrição
└── análise inicial

Workforce
├── identidade da organização
├── políticas
├── permissões
├── consentimento
├── agenda e follow-up
├── ferramentas governadas
├── orçamento
├── auditoria
├── memória operacional
└── coordenação multicanal

LEAF
├── CRM
├── contatos
├── agenda
├── pipeline
├── timeline
├── configurações
└── interface do cliente
```

## Arquitetura recomendada

```
┌──────────────────────────────────────────────┐
│                    LEAF                      │
│ CRM · Agenda · Leads · Timeline · Dashboard │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│              GINKGO WORKFORCE                │
│                                              │
│ Follow-up Engine · Policy Engine · Skills    │
│ Scheduler · Consent · Billing · Audit        │
│ Provider Router · Connections · Event Bus    │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│              ELEVENLABS AGENTS               │
│                                              │
│ Voice · Conversation · Tools · Analysis      │
│ Transfer · Batch Calls · SIP · Twilio        │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
             Twilio / Telnyx / SIP
```

## O que muda no PRD anterior

A mudança é importante: **não precisamos construir um runtime de áudio WebSocket próprio no MVP**.

Em vez de:

```
apps/voice-runtime
provider-xai
audio streaming
turn detection
transcript buffer
session recovery
```

Usamos:

```
packages/provider-elevenlabs
apps/voice-orchestrator
apps/tool-gateway
apps/webhook-ingress
apps/follow-up-worker
```

O `voice-orchestrator` não transporta áudio. Ele provisiona, configura, inicia e acompanha as ligações.

## Estrutura revisada

```
ginkgo-workforce/
├── apps/
│   ├── api/
│   ├── voice-orchestrator/
│   ├── webhook-ingress/
│   ├── tool-gateway/
│   ├── scheduler/
│   └── worker/
│
├── packages/
│   ├── provider-elevenlabs/
│   ├── provider-contracts/
│   ├── skill-engine/
│   ├── policy-engine/
│   ├── follow-up-engine/
│   ├── connections-sdk/
│   ├── event-bus/
│   ├── billing-engine/
│   └── observability/
│
├── agents/
│   ├── callima/
│   │   ├── voice-template/
│   │   ├── tools/
│   │   └── policies/
│   └── eliza/
│       ├── voice-template/
│       └── alert-policies/
│
└── docs/
    ├── PRD_WORKFORCE_VOICE.md
    ├── PROVIDER_ELEVENLABS.md
    └── VOICE_COMPLIANCE.md
```

## Fluxo inbound com ElevenLabs

```
1. Cliente liga para o número.
2. Twilio/SIP envia a chamada à ElevenLabs.
3. ElevenLabs consulta o pre-call webhook do Workforce.
4. Workforce identifica:
   - organização;
   - contato;
   - agente;
   - idioma;
   - finalidade;
   - contexto autorizado.
5. Workforce retorna variáveis e overrides.
6. Callima inicia a conversa.
7. Tools são chamadas no Tool Gateway.
8. Skill Engine autoriza ou bloqueia cada ação.
9. Ligação termina.
10. ElevenLabs envia o post-call webhook.
11. Workforce valida a assinatura.
12. Salva resultado e consumo.
13. Atualiza o LEAF.
14. Follow-up Engine decide a próxima ação.
```

A ElevenLabs permite personalizar a chamada antes de começar usando dados como número do chamador, agente, número chamado e identificador da ligação. O webhook pode retornar variáveis dinâmicas e sobrescrever configurações da conversa, como prompt, primeira mensagem, idioma ou voz. [^11]

## Fluxo outbound

```
Evento no LEAF
    ↓
Follow-up Engine
    ↓
Policy Engine
    ├── consentimento?
    ├── horário permitido?
    ├── limite de tentativas?
    ├── orçamento disponível?
    └── contato bloqueado?
    ↓
Fila BullMQ
    ↓
ElevenLabs outbound API
    ↓
Twilio ou SIP
    ↓
Callima conversa
    ↓
Webhook pós-ligação
    ↓
LEAF atualizado
```

Para campanhas:

```
Campanha criada no LEAF
    ↓
Workforce seleciona contatos elegíveis
    ↓
Remove opt-outs e duplicados
    ↓
Envia lote para ElevenLabs
    ↓
ElevenLabs controla a concorrência
    ↓
Workforce recebe cada resultado
```

A ElevenLabs já suporta chamadas em lote com CSV/XLS, variáveis por destinatário, horário programado e limite explícito de chamadas simultâneas. [^8]

## Como integrar as tools

A ElevenLabs não deve chamar diretamente Supabase, Google Calendar, Stripe ou sistemas do cliente.

Ela deve enxergar apenas uma porta:

```
https://workforce.ginkgosystems.tech/v1/voice/tools/:tool
```

Exemplo:

```json
{
  "organization_id": "{{org_id}}",
  "conversation_id": "{{system__conversation_id}}",
  "contact_id": "{{contact_id}}",
  "tool": "get_available_slots",
  "arguments": {
    "service_id": "consulta_inicial",
    "preferred_date": "2026-08-05"
  }
}
```

O Tool Gateway executa:

```
Receber chamada
    ↓
Autenticar origem ElevenLabs
    ↓
Resolver tenant
    ↓
Validar schema
    ↓
Consultar Skill Engine
    ↓
Verificar risco
    ↓
Executar Connection
    ↓
Sanitizar resultado
    ↓
Registrar auditoria
    ↓
Responder à Callima
```

Isso impede que a ElevenLabs vire proprietária da lógica do produto.

## Dois modelos possíveis

## Modelo A — ElevenLabs completa

A própria ElevenLabs controla:

- Voz.
- STT/TTS.
- LLM.
- Turn-taking.
- Tools.
- RAG.
- Telefonia.
- Análise.

### Vantagem

MVP muito rápido.

### Desvantagem

Maior dependência da plataforma.

## Modelo B — ElevenLabs como voz, Workforce como cérebro

A ElevenLabs controla:

- Áudio.
- Voz.
- Interrupção.
- Telefonia.

O Workforce fornece o LLM por um endpoint compatível.

A ElevenLabs permite integrar um servidor LLM próprio usando formatos compatíveis com Chat Completions ou Responses API. As system tools continuam disponíveis para transferência e encerramento da chamada. [^12]

### Vantagem

- Mantemos Hermes, Grok, Claude ou outro modelo atrás do gateway.
- Memória e governança ficam centralizadas.
- Podemos trocar o modelo sem trocar a voz.
- Menor lock-in cognitivo.

### Desvantagem

- Mais latência.
- Mais engenharia.
- Mais pontos de falha.

## Minha recomendação

## MVP

```
ElevenLabs Agents completo
+
Twilio ou SIP
+
Workforce Tool Gateway
+
Workforce Policy Engine
+
LEAF
```

Usaria o LLM nativo ou integrado da ElevenLabs inicialmente. Não colocaria Hermes no caminho crítico da voz até validar latência.

## Versão 2

```
ElevenLabs = camada de voz
Workforce AI Gateway = cognição
Hermes/Grok/Claude = modelos intercambiáveis
```

## Versão 3

Provider Router:

```
VoiceProvider
├── ElevenLabsProvider  ← principal
├── XaiProvider         ← experimental
├── RetellProvider
├── VapiProvider
└── CustomRealtimeProvider
```

## Onde Grok ainda pode entrar

Grok não precisa ser o motor telefônico.

Ele pode ser um dos cérebros disponíveis:

```
Callima Voice
    ↓
ElevenLabs áudio e telefonia
    ↓
Workforce AI Gateway
    ├── Grok para raciocínio rápido
    ├── Claude para casos complexos
    ├── Gemini para custo baixo
    └── modelo local para tarefas simples
```

Assim, não escolhemos entre ElevenLabs e Grok. Colocamos cada um no andar em que trabalha melhor.

## Veredito

**Sim, ElevenLabs supre. E supre melhor o MVP específico de atendimento, follow-up e avisos por ligação.**

A decisão ajustada seria:

> **ElevenLabs como provider oficial inicial do Workforce Voice.  
> Workforce como controle, ferramentas, governança e jornadas.  
> LEAF como CRM e interface.  
> Grok como modelo opcional, não como dependência estrutural.**

Atualmente, a ElevenLabs também está mais pronta para outbound operacional porque já possui API de ligações, campanhas em lote, Twilio, SIP, transferências e análise pós-chamada em um único produto. O preço público adicional dos ElevenAgents está listado em torno de **US$ 0,08 por minuto**, com limites de concorrência variando por plano; telefonia e eventuais custos de LLM devem ser considerados separadamente na margem do LEAF. [^13]

---

**Você disse**

Projete um PRD técnico desta feature com elevenlabs e documente em ginkgo-workforce

---

## PRD documentado no ginkgo-workforce

Criei o documento:

**`docs/PRD_WORKFORCE_VOICE_ELEVENLABS.md`**

Também adicionei o acesso direto na seção **Documentação** do `README.md`.

### O PRD define

- ElevenLabs como **plano de mídia e conversação**.
- Workforce como **plano de controle, governança e execução**.
- LEAF como **CRM, agenda, pipeline e interface**.
- Chamadas inbound e outbound.
- Callima Reception, Callima Follow-up e Eliza Critical Alert.
- Integração via Twilio inicialmente, com SIP preparado para produção.
- Provider Adapter para evitar lock-in.
- Voice Orchestrator, Webhook Ingress, Tool Gateway e Follow-up Engine.
- Skill Engine com níveis de risco e aprovação.
- APIs, eventos, estados e modelo completo de dados.
- Usage ledger, orçamento, concorrência e limites.
- Opt-out, retenção, auditoria e isolamento multi-tenant.
- Testes unitários, de contrato, integração, segurança, conversação e carga.
- SLOs, rollout e 12 épicos de implementação.
- 18 critérios objetivos de aceite do MVP.

A base técnica foi validada na documentação atual da ElevenLabs: há suporte oficial a telefonia inbound e outbound por Twilio e SIP, chamadas em lote, variáveis dinâmicas, webhook/system tools, webhooks pós-chamada e integração futura com LLM próprio. [^14]

A decisão central registrada ficou:

> **ElevenLabs fala. Workforce governa e executa. LEAF lembra, organiza e vende.**

[^1]: [x.ai](https://x.ai/news/grok-voice-agent-builder)

[^2]: [x.ai](https://x.ai/news/grok-voice-agent-api?trk=article-ssr-frontend-pulse_little-text-block&utm_source=chatgpt.com)

[^3]: [docs.x.ai](https://docs.x.ai/developers/model-capabilities/audio/voice-agent)

[^4]: [x.ai](https://x.ai/news/grok-voice-think-fast-1)

[^5]: [docs.x.ai](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech/sip)

[^6]: [x.ai](https://x.ai/news/grok-custom-voices)

[^7]: [docs.x.ai](https://docs.x.ai/developers/models/voice-agent-api)

[^8]: [elevenlabs.io](https://elevenlabs.io/docs/eleven-agents/phone-numbers/batch-calls?utm_source=chatgpt.com)

[^9]: [elevenlabs.io](https://elevenlabs.io/docs/eleven-agents/customization/tools/mcp?utm_source=chatgpt.com)

[^10]: [elevenlabs.io](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks?utm_source=chatgpt.com)

[^11]: [elevenlabs.io](https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables?utm_source=chatgpt.com)

[^12]: [elevenlabs.io](https://elevenlabs.io/docs/eleven-agents/customization/llm/custom-llm?utm_source=chatgpt.com)

[^13]: [elevenlabs.io](https://elevenlabs.io/pt/pricing/agents?utm_source=chatgpt.com)

[^14]: [elevenlabs.io](https://elevenlabs.io/docs/eleven-agents/phone-numbers/sip-trunking)