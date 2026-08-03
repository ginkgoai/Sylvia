# Portfólio Meta / WhatsApp Business Platform — o que precisamos (burocrático + técnico)

Objetivo: migrar a Ginkgo do WhatsApp não-oficial (Evolution/Baileys, risco de ban) para
o **WhatsApp Business Platform (Cloud API) oficial** — exigência pra escalar e ter confiança.
Contexto Ginkgo: SaaS multi-cliente (cada cliente = um número/WABA). Logo somos, na prática,
um **provedor** — vale decidir entre Cloud API direto vs entrar por um BSP.

## PARTE 1 — Burocrático (o que VOCÊ/empresa precisa providenciar)

### 1. Entidade legal + documentos (Business Verification)
A Meta exige 2 provas que precisam BATER entre si e com o site:
- **Prova de entidade legal:** CNPJ ativo (cartão CNPJ / contrato social). Razão social tem
  que ser idêntica em todo lugar.
- **Prova de endereço/telefone:** conta de utilidade, extrato bancário ou doc oficial com
  nome da empresa + endereço (emitido < 90 dias), OU telefone comercial verificável.
- **Regra de ouro:** Meta Business Info = Documento de registro = Site = Comprovante de
  endereço = Admin autorizado — TUDO com a mesma razão social/endereço. Divergência = reprova.

### 2. Conta Meta Business (Business Manager / Portfólio)
- Criar/usar o **Meta Business Portfolio** (business.facebook.com) da Ginkgo AI Systems.
- Concluir a **Verificação de Negócio** (Security Center → Business Verification).
  Prazo típico: 1–3 dias úteis.

### 3. Identidade do WhatsApp (por número de cliente)
- **Número de telefone dedicado** que NÃO esteja ativo num app WhatsApp/WhatsApp Business
  (precisa receber SMS/voz pra verificar). Pode ser fixo ou celular.
- **Display name** (nome de exibição) seguindo as regras da Meta (sem termos proibidos) —
  passa por aprovação.
- Perfil: categoria, descrição, logo, site.

### 4. Site institucional coerente
- Domínio próprio (ginkgo...), com a razão social, endereço e contato visíveis (rodapé) —
  é o que o revisor cruza. (Mais um motivo pro site institucional que estamos desenhando.)

### 5. Decisão de modelo (impacta prazo e custo)
- **Via BSP** (provedor oficial: ex. 360dialog, Twilio, Gupshup, Zenvia): setup 24–48h,
  eles cuidam de hosting/infra e templates; você paga markup por conversa. Mais rápido.
- **Cloud API direto** (Meta hospeda grátis; você integra): 2–6 semanas de engenharia,
  sem markup de BSP. Mais barato no volume, mais trabalho nosso.
  → Recomendação: começar **Cloud API direto** (já que temos engenharia) e manter BSP como
    plano B se a verificação travar.

## PARTE 2 — Técnico (o que EU/Claude Code implementamos)

### Ativos no painel Meta (App + WhatsApp product)
- **Meta App** (developers.facebook.com) tipo Business, com o produto **WhatsApp** adicionado.
- **WABA** (WhatsApp Business Account) dentro do portfólio.
- **System User** (admin) + **token de acesso permanente** (System User token) — NÃO usar
  token temporário em produção.
- **App Secret**, **WABA ID**, **Phone Number ID**, **Business Portfolio ID**.

### Webhooks
- Endpoint HTTPS público (verify token + assinatura `X-Hub-Signature-256`) assinando os
  campos `messages` (entrada) e `message_template_status_update`, `account_update`, etc.
- Trocar o ingest atual (Evolution) pelo webhook da Cloud API no `apps/api/webhooks`.

### Envio de mensagens
- **Janela de 24h (sessão):** fora dela, só **templates** pré-aprovados (HSM). Dentro da
  janela (cliente respondeu < 24h): texto livre/mídia.
- Implementar **gestão de templates** (criar/submeter/àprovar) — espelha o que a Callima já
  faz, mas via Graph API oficial (`/{waba-id}/message_templates`).
- Categorias de conversa cobradas: marketing / utility / authentication / service.

### Limites de envio (tiers) — planejar no produto
- Sem verificação: **250** conversas/24h. Verificado → **Tier 1: 1.000/dia**.
- Sobe pra 10k → 100k → ilimitado conforme **qualidade do número** + uso (usar ≥50% do
  limite em 7 dias). Meta reavalia a cada 6h.
- **Desde out/2025 o limite é por PORTFÓLIO, não por número** — números novos herdam o maior
  tier do portfólio na hora. (Bom pra nós: 1 cliente novo já entra no tier alto.)
- Implicação de produto: monitorar **quality rating** por número (green/yellow/red) e expor
  no dashboard; pausar disparos se cair pra red.

### Mudanças no LEAF
- `whatsapp_instances`: hoje modela instância Evolution. Adaptar p/ Cloud API
  (phone_number_id, waba_id, quality_rating, tier, token ref). Manter Evolution como
  fallback/legado durante a transição.
- Onboarding do cliente: fluxo de **Embedded Signup** da Meta (cliente conecta o próprio
  WABA via popup OAuth) — é o padrão dos BSPs e o melhor UX pra multi-tenant.

## Resumo do caminho crítico
1. CNPJ + comprovantes coerentes → 2. Verificar Business Portfolio → 3. Site coerente no ar →
4. Criar App+WABA+System User token → 5. (eu) webhooks + templates + Embedded Signup no LEAF →
6. Verificar 1º número + aprovar display name + 1º template → produção.
Itens 1–4 são SEUS (burocráticos); 5 é meu; 6 é conjunto.
