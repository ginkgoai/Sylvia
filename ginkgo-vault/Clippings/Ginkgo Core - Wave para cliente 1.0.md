---
title: "Ginkgo Core - Wave para cliente 1.0"
source: "https://chatgpt.com/g/g-p-68e0a0b393cc8191a0f44ad743e1117d/c/69224052-27e4-8328-8bf9-67a1db147e0a"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sáb., 22 de nov. às 19:59

Se eu precisasse deixar uma versão do Wave totalmente pronta pra 1 usuário, um cliente, com essas funções. Apenas usando a Manus ou outra ferramenta ou serviço que precisar.

Beleza, vamos pensar no Wave como um “copiloto de tráfego plugado no ClickUp” só para o Lucas, rodando em cima da Manus.

Vou montar como se fosse um checklist de entrega v1-fechada para 1 cliente.

---

## 1\. Objetivo do Wave v1 para o Lucas

Resolver exatamente isso que ele falou no áudio:

1. Ele configura a campanha no ClickUp (ideia, objetivo, orçamento, público).
2. A IA (Alfred/Wave) pega esses dados, monta a campanha e sobe nos gestores de tráfego (Meta / Google).
3. Depois a IA monitora, otimiza com regras simples e manda relatório, reduzindo custo de pessoal.

Nada de plataforma gigantesca: é “ClickUp + Manus + contas de Ads”.

---

## 2\. Stack mínima

- **ClickUp**: painel onde ele “clica e resolve”.
- **Manus**: cérebro orquestrando:
	- LLM para interpretar briefing.
		- Agentes/ferramentas para chamar APIs.
- **APIs**:
	- Meta Ads (Facebook/Instagram).
		- Google Ads (se ele usar).
- **Canal de aviso**: WhatsApp (Evolution/Twilio) ou e-mail/Telegram.

---

## 3\. Estrutura no ClickUp (lado do cliente)

Criar uma lista exclusiva, ex.: `WAVE – Campanhas`.

Campos principais (custom fields):

- `Plataforma`: Meta / Google / Ambas.
- `Objetivo`: Leads / Vendas / Alcance / Tráfego / etc.
- `Link de destino`.
- `Orçamento diário`.
- `Limite de orçamento total`.
- `Data início` / `Data fim`.
- `Público / Interesses` (texto livre).
- `Localização`.
- `Criativos`:
	- link para pasta com imagens/vídeos **ou**
		- checkbox `Gerar criativos via IA`.
- `Status Wave`: Rascunho / Pronto para subir / Subido / Em otimização / Pausado.
- `Risco máx.`: quanto ele aceita mexer em orçamento (%).

Essas tasks serão o “formulário” que dispara tudo.

---

## 4\. Fluxos na Manus

Pensa em 3 fluxos:

1. **Fluxo 1 – Subir campanha** (Evento → criar campanha).
2. **Fluxo 2 – Otimizar diariamente** (Cron → ler dados → ajustar orçamento/pausar).
3. **Fluxo 3 – Relatórios** (diário/semana → mandar resumo pro Lucas).

### 4.1 Fluxo 1 – Subir campanha a partir do ClickUp

**Trigger:**

- Webhook do ClickUp quando:
	- lista = `WAVE – Campanhas`
		- `Status Wave` muda para `Pronto para subir`.

**Passos no Manus:**

1. **Buscar dados da task**
	- Node “HTTP / ClickUp – Get Task”.
		- Puxa todos os custom fields.
2. **Normalizar para JSON de campanha**
	- LLM na Manus com prompt algo como:
		> “Você é um media buyer sênior. Recebe um briefing de campanha com: objetivo, orçamento diário, datas, público, localização, link, plataforma.  
		> Devolva um JSON exatamente no formato abaixo, SEM comentários:
		> 
		> ```markdown
		> {
		>   "plataforma": "meta|google|ambas",
		>   "objetivo_marketing": "...",
		>   "orcamento_diario": 50,
		>   "limite_total": 500,
		>   "data_inicio": "YYYY-MM-DD",
		>   "data_fim": "YYYY-MM-DD",
		>   "publicos": [ "..." ],
		>   "localizacao": "Brasil, RS, ...",
		>   "conjuntos": [
		>      {
		>        "nome": "Topo - Interesse X",
		>        "tipo_otimizacao": "conversions|traffic|leads",
		>        "criativos": [
		>          {
		>            "tipo": "image|video",
		>            "headline": "...",
		>            "texto_principal": "...",
		>            "descricao": "...",
		>            "cta": "Saiba mais|Enviar mensagem"
		>          }
		>        ]
		>      }
		>   ]
		> }
		> ```
3. **(Opcional) Gerar criativos**
	- Se `Gerar criativos via IA = true`:
		- Node LLM para gerar textos de anúncio (headline, primário, descrição).
				- Se quiser ir mais longe: integração com ferramenta de criativo (NanoBanana, Midjourney, etc.) e gravar URL da imagem.
4. **Criar campanha na Meta Ads API**
	- Node HTTP chamando Facebook Marketing API com o JSON.
		- Criar:
		- Campaign
				- Ad Sets
				- Ads
		- Salvar os IDs retornados: `campaign_id`, `adset_ids`, `ad_ids`.
5. **Criar campanha no Google Ads** (se `plataforma` incluir google)
	- Mesma lógica, outro node HTTP.
6. **Atualizar ClickUp**
	- `Status Wave` → `Subido`.
		- Adicionar custom fields com:
		- `Meta Campaign ID`
				- `Google Campaign ID`
		- Adicionar comentário na task:  
		“Wave subiu sua campanha nas plataformas X. IDs: …”
7. **Notificar o Lucas**
	- Enviar WhatsApp/Telegram:
		- “Campanha X foi criada e ativada. Orçamento diário R$Y, objetivo Z. Se quiser pausar, mude o Status Wave no ClickUp para ‘Pausado’.”

---

### 4.2 Fluxo 2 – Otimizador diário

**Trigger:**

- Cron diário, ex.: 08:00 e 18:00, na Manus.

**Passos:**

1. **Listar campanhas ativas do Lucas**
	- Chamar Meta Ads / Google Ads filtrando por label/campo `Wave` ou por `campaign_id` salvo em base (ou direto vindo dos custom fields do ClickUp).
2. **Puxar métricas-chave por campanha/adset/ad**
	- CPC, CPM, CTR, CPA, ROAS (se tiver conversões), gastos do dia e total.
3. **Passar para LLM “Media Buyer”**
	- Prompt com regras claras:
		- Se CPA > limite ou campanha sem conversão após X cliques → sugerir:
			- Pausar anúncio ruim
						- Diminuir orçamento em Y%
				- Se campanha com CPA abaixo da meta e ROAS bom → sugerir:
			- Aumentar orçamento em Z% (respeitando `Risco máx.` do custom field).
				- Sempre devolver um JSON de ação:
			```markdown
			{
			  "acoes": [
			    {
			      "tipo": "aumentar_orcamento",
			      "plataforma": "meta",
			      "nivel": "adset",
			      "id": "XXX",
			      "percentual": 20
			    },
			    {
			      "tipo": "pausar",
			      "plataforma": "meta",
			      "nivel": "ad",
			      "id": "YYY"
			    }
			  ],
			  "sumario": "Texto curto explicando as decisões."
			}
			```
4. **Aplicar ações via API**
	- Loop nas ações:
		- Chamar Meta/Google Ads para:
			- Atualizar budget.
						- Pausar / reativar ads/adsets/campaigns.
5. **Registrar no ClickUp**
	- Para cada campanha:
		- Adicionar comentário: resumo das mudanças do dia.
				- Gravar em um campo histórico tipo `Última otimização Wave`.
6. **Notificar o Lucas (opcional)**
	- Se houve mudança grande (> X% orçamento ou campanha pausada):
		- Mensagem no WhatsApp:
			- “Wave ajustou a campanha Y: +20% de orçamento no conjunto Z, pausou anúncio W por CPA alto. Resumo no ClickUp.”

---

### 4.3 Fluxo 3 – Relatório simples

**Trigger:**

- Cron semanal, ex.: segunda 09:00.

**Passos:**

1. Puxar resultados da semana por campanha:
	- Gastos, leads/vendas, CPA, ROAS.
2. LLM formata isso em texto direto:
	- “Campanha X: investido R$…, gerou … leads, CPA R$…, recomendação: manter/escala/pausar.”
3. Enviar:
	- 1 comentário em uma task “Relatórios Wave – Semana”.
		- 1 mensagem WhatsApp com resumo curto + link da task.

---

## 5\. Onboarding técnico desse único cliente

Checklist:

1. Criar projeto `Wave – Lucas` na Manus.
2. Conectar:
	- OAuth ou tokens da conta de **Meta Ads** do Lucas.
		- OAuth/tokens de **Google Ads** (se usar).
		- API Token do **ClickUp** + configurar webhooks.
		- Canal de notificação (WhatsApp/e-mail).
3. Configurar:
	- Campos custom no ClickUp (lista de Campanhas).
		- Webhook: evento “Task Updated” + filtro por `Status Wave`.
4. Definir limites de segurança:
	- Orçamento máximo por campanha.
		- % máxima de mudança de budget por dia.
		- Lista de ações que a IA pode fazer sozinha vs que só recomenda.

---

## 6\. Resultado prático para o Lucas

A experiência dele fica assim:

1. Ele entra no ClickUp → cria task “Campanha Black Friday Loja X”.
2. Preenche os campos (orçamento, público, datas, etc.) e marca `Status Wave = Pronto para subir`.
3. Em alguns minutos:
	- Wave sobe tudo nas contas de Ads.
		- Ele recebe mensagem: “Campanha pronta e ativa”.
4. Todo dia:
	- Wave olha as métricas.
		- Ajusta orçamento e pausa o que estiver ruim dentro dos limites.
		- Deixa tudo registrado no ClickUp e manda resumo.

Isso já é uma versão “Wave para 1 usuário” totalmente funcional, 100% construída com:

- ClickUp (painel do cliente).
- Manus (orquestração + IA).
- APIs dos gestores de anúncios.
- Opcional: ferramenta de criativo.

Se quiser, no próximo passo eu desenho isso em formato de diagrama (tipo mermaid) para ficar visual e pronto para você replicar depois em escala para outros clientes.

e isso lincamos no github? upamos em dominio hostinger? banco de dados? todas integrações que devem ser conectadas me fake

Boa, agora vamos fechar a “foto completa” de infra do Wave v1 pro Lucas.

Pensa em 2 camadas:

- **Camada de operação**: Manus + ClickUp + contas de Ads + WhatsApp → onde a mágica acontece.
- **Camada de marca/produto**: GitHub + Hostinger + domínio + (opcional) banco de dados → onde tu versiona, documenta e dá cara de SaaS.

---

## 1\. GitHub – o que vai lá

Mesmo usando Manus (que já roda na nuvem deles), vale ter um repo do Wave, nem que seja “leve”.

Sugestão de estrutura:

```markdown
wave-lucas/
  README.md
  docs/
    arquitetura-wave-v1.md
    fluxos-manus-explicacao.md
  manus-flows/
    fluxo-1-subir-campanha.json
    fluxo-2-otimizacao-diaria.json
    fluxo-3-relatorio-semanal.json
  backend/          # opcional (webhook/proxy)
    src/
      index.ts
    package.json
    .env.example
  landing/          # site do Wave
    index.html
    assets/
    package.json    # se usar React/Vite etc.
```
- **`manus-flows`**: exports em JSON dos fluxos, pra ter histórico/versionamento.
- **`backend` (opcional)**: caso tu queira um micro back-end pra:
	- receber webhooks do ClickUp,
		- fazer outras integrações que não queira deixar só dentro da Manus,
		- logar ações em banco próprio.
- **`landing`**: a página que vai para o domínio na Hostinger.

Repo fica no GitHub, Hostinger puxa desse repo para deploy (ou tu builda local e sobe).

---

## 2\. Hostinger + domínio

O Wave pra 1 usuário não precisa ser um monolito gigante. Pensa assim:

- **Domínio**: `wave.seudominio.com`
- Na Hostinger tu hospeda só:
	1. **Landing** (pasta `landing/`):
		- Explica o que é o Wave,
				- botão “Acessar painel” → link direto pro espaço dele no ClickUp ou para uma página interna com o link.
		2. **Backend opcional** (pasta `backend/`, via Node/Docker se quiser):
		- endpoint `/webhook/clickup` (se preferir passar por ti antes de mandar pra Manus),
				- endpoint `/health` só pra monitorar.

Se quiser 100% lean:

- Deixa **só a landing** na Hostinger.
- Webhook do ClickUp aponta direto pra URL da Manus, sem backend próprio.

---

## 3\. Banco de dados – precisa mesmo?

Para **v1 só pro Lucas**, você consegue sobreviver com:

- ClickUp como “banco” de campanhas,
- logs dentro da Manus,
- APIs de Ads guardando o resto.

Mas se quiser já pensar em escala (outros clientes depois), vale um DB simples, tipo **Supabase/Postgres**:

Tabelas mínimas:

- `clients`
	- `id`, `name`, `clickup_space_id`, `meta_ad_account_id`, `google_customer_id`
- `campaigns_mirror`
	- `id`, `client_id`, `clickup_task_id`,
		- `meta_campaign_id`, `google_campaign_id`,
		- `status`, `created_at`
- `actions_log`
	- `id`, `campaign_id`, `platform`,
		- `action_type` (aumentar\_orcamento, pausar\_ad, etc.),
		- `payload_json`, `created_at`

O backend (ou a própria Manus via HTTP node) grava nisso.

Se quiser **zero back-end próprio agora**, pula banco nessa fase e deixa pra “Wave multi-cliente”.

---

## 4\. Todas as integrações necessárias (fake)

Lista completa do que precisa conectar para o Lucas ter o Wave rodando:

### 4.1. ClickUp

- API Key do teu usuário admin:
	- `CLICKUP_API_KEY="pk_xxxxxxxxxxxxxxxxxxxxx"`
- IDs:
	- `CLICKUP_TEAM_ID="12345678"`
		- `CLICKUP_SPACE_ID_WAVE="87654321"`
		- `CLICKUP_LIST_ID_CAMPANHAS="11223344"`

No ClickUp:

- Criar a lista `WAVE – Campanhas`.
- Criar os custom fields (Objetivo, Orçamento, Data Início, etc.).
- Configurar **Webhook**:
	- Evento: `taskUpdated`
		- Filtro: lista = `WAVE – Campanhas`
		- URL do webhook:
		- ou `https://hooks.manus.ai/wave-lucas/...`
				- ou `https://api.wave.seudominio.com/webhook/clickup` (teu backend, se usar).

### 4.2. Manus

- Projeto `Wave – Lucas`.
- Integrar:
	- **Credenciais da Meta Ads**:
		- `META_ADS_ACCESS_TOKEN="EAABxxx..."`
				- `META_ADS_ACCOUNT_ID="act_1234567890"`
				- `META_ADS_APP_ID="123456789012345"`
				- `META_ADS_APP_SECRET="xxxxxxxx"`
		- **Credenciais Google Ads** (se ele usar):
		- `GOOGLE_ADS_CLIENT_ID="000-xxx.apps.googleusercontent.com"`
				- `GOOGLE_ADS_CLIENT_SECRET="xxxxxx"`
				- `GOOGLE_ADS_REFRESH_TOKEN="1//0xxxx"`
				- `GOOGLE_ADS_DEVELOPER_TOKEN="xxxx-xxxx-xxxx"`
				- `GOOGLE_ADS_LOGIN_CUSTOMER_ID="1234567890"`
		- **Canal de notificação (WhatsApp, por ex.)**:
		- `WHATSAPP_API_URL="https://evolution.ginkgo.com.br"`
				- `WHATSAPP_API_KEY="evo_xxxxxxxxxxxxx"`
				- `WHATSAPP_NUMBER_ID="+55xxxxxxxxx"`
		- (Opcional) **Supabase**:
		- `SUPABASE_URL="https://xxxx.supabase.co"`
				- `SUPABASE_SERVICE_ROLE_KEY="supabase_sr_xxxx"`

No painel da Manus:

- Definir variáveis de ambiente com esses valores.
- Conectar cada credencial nos nodes HTTP ou integrações nativas.

### 4.3. Backend (se você quiser um)

Arquivo `.env.example` dentro de `backend/`:

```markdown
PORT=3000
NODE_ENV=production

# ClickUp
CLICKUP_API_KEY=pk_xxxxxxxxx
CLICKUP_TEAM_ID=12345678
CLICKUP_SPACE_ID_WAVE=87654321
CLICKUP_LIST_ID_CAMPANHAS=11223344

# Manus
MANUS_WEBHOOK_URL=https://hooks.manus.ai/wave-lucas/entrada
MANUS_API_KEY=manus_xxxxxxxxx

# Meta Ads
META_ADS_ACCESS_TOKEN=EAABxxxxxx
META_ADS_ACCOUNT_ID=act_1234567890

# Google Ads
GOOGLE_ADS_CLIENT_ID=000-xxx.apps.googleusercontent.com
GOOGLE_ADS_CLIENT_SECRET=xxxxxx
GOOGLE_ADS_REFRESH_TOKEN=1//0xxxx
GOOGLE_ADS_DEVELOPER_TOKEN=xxxx-xxxx-xxxx
GOOGLE_ADS_LOGIN_CUSTOMER_ID=1234567890

# Notificações
WHATSAPP_API_URL=https://evolution.ginkgo.com.br
WHATSAPP_API_KEY=evo_xxxxxxxxx
WHATSAPP_NUMBER_ID=+55xxxxxxxx

# Banco (opcional)
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_SERVICE_ROLE_KEY=supabase_sr_xxxx

# Wave
WAVE_CLIENT_LUCAS_ID=lucas-001
WAVE_ENV=production
```

O backend só faria:

- Receber o webhook do ClickUp;
- Validar / logar;
- Chamar a URL de entrada da Manus (`MANUS_WEBHOOK_URL`) com o payload.

---

## 5\. Em resumo (modo prático)

Se quiser **mais simples possível agora**:

1. **GitHub**: um repo com `docs/`, `manus-flows/` e `landing/`.
2. **Hostinger**: só a landing em um domínio tipo `wave.seudominio.com`.
3. **Sem backend e sem banco**:
	- ClickUp → Webhook → Manus
		- Manus → APIs de Ads + WhatsApp
		- ClickUp vira “banco + painel”.

Quando for virar **Wave multi-cliente**, tu adiciona:

- Backend próprio,
- Banco (Supabase),
- multi-tenancy no ClickUp ou outra base.

Se quiser, no próximo passo posso desenhar a versão “lean” e a versão “com backend + banco” em 2 diagramas separados, pra tu seguir como blueprint.