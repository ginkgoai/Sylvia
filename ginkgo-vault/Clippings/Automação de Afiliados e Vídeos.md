---
title: "Automação de Afiliados e Vídeos"
source: "https://chatgpt.com/c/6a62c982-400c-83e9-b32d-9617cb343720"
author:
published:
created: 2026-07-24
description: "ChatGPT conversation with 2 messages"
tags:
  - "clippings"
---
**Você disse**

https://www.youtube.com/shorts/iadFWjfTdyo?feature=share quero criar um grupão automatizado igual a este, plugando links de afiliado prontos de contas minhas e produtos em promoção, e ao mesmo tempo criar trailers cinematrograficos com ia e postar no youtube / tiktok

---

Sim. O projeto deve ser tratado como **dois motores conectados**:

1. **Deal Engine**: encontra, valida, transforma e distribui promoções.
2. **Trailer Engine**: converte as melhores ofertas em vídeos verticais cinematográficos para TikTok e YouTube Shorts.
```
Fontes de produtos
        ↓
Coleta e normalização
        ↓
Validação de preço, estoque e comissão
        ↓
Score econômico da oferta
        ↓
┌──────────────────────┬────────────────────────┐
│ Distribuição direta  │ Fábrica de conteúdo    │
│ WhatsApp / site      │ Shorts / TikTok        │
└──────────────────────┴────────────────────────┘
        ↓                         ↓
Cliques, vendas e comissão → motor de aprendizado
```

## Ponto crítico antes de construir

Pelos prints, os links parecem ser do Mercado Livre. Atualmente, o programa de afiliados do Mercado Livre informa que **links não podem ser divulgados em grupos fechados**; os canais precisam ser públicos, próprios e cadastrados no programa. Também não permite tráfego pago diretamente para links de afiliado. Portanto, copiar exatamente esse modelo para links do Mercado Livre pode gerar comissão invalidada ou suspensão. [^1]

A arquitetura segura seria:

- WhatsApp como canal de audiência e notificação, após validação das regras de cada programa.
- Página pública própria como hub das promoções.
- TikTok, YouTube e redes cadastradas no programa.
- Link rastreável da sua página redirecionando para o link de afiliado.
- Divulgação direta no grupo somente para programas que autorizem expressamente esse canal.

Para Amazon, Shopee e demais programas, cada política deve ser registrada no sistema como uma regra de distribuição. Nada de deixar o robô virar um estagiário cyberpunk disparando links proibidos.

---

## 1\. Motor de promoções

## Entrada dos produtos

O MVP não precisa começar raspando toda a internet. Comece com três entradas:

- Google Sheets com produtos selecionados.
- Links de afiliado já gerados.
- Feeds, APIs ou páginas autorizadas de promoções.

Estrutura mínima da oferta:

```json
{
  "marketplace": "mercado_livre",
  "product_name": "Estante Industrial 5 Andares",
  "original_price": 251.90,
  "current_price": 225.58,
  "coupon": null,
  "affiliate_url": "https://...",
  "image_url": "https://...",
  "commission_percentage": 8,
  "stock_status": "available",
  "expires_at": null
}
```

## Agentes do sistema

### Scout

Localiza ou recebe novas oportunidades.

Responsabilidades:

- coletar produtos;
- detectar redução de preço;
- identificar cupom;
- capturar imagem, título, avaliações e vendedor;
- impedir produtos duplicados.

### Validator

Confere a oferta antes de publicar:

- preço atual;
- estoque;
- frete;
- reputação;
- validade do cupom;
- funcionamento do link;
- política permitida para aquele canal.

O Validator deve executar novamente **imediatamente antes da publicação**. Promoção vencida é o equivalente comercial de um link para uma nave abandonada.

### Ranker

Calcula o potencial econômico:

```
offer_score =
  desconto × 0,25
+ comissão × 0,25
+ demanda estimada × 0,20
+ reputação × 0,15
+ conversão histórica × 0,15
```

Exemplo de classificação:

- 90–100: trailer cinematográfico + todos os canais.
- 75–89: vídeo simples + grupo/site.
- 60–74: card estático.
- abaixo de 60: arquivar ou aguardar.

### Copy Agent

Gera a mensagem padronizada:

```
🔥 ESTANTE INDUSTRIAL COM DESCONTO

De: R$ 251,90
Por: R$ 225,58

✅ 5 andares
✅ Estrutura metálica
✅ Oferta verificada às 19:41

🔗 Ver promoção:
[LINK]

*Link de afiliado. Podemos receber comissão pela compra.
Preço e estoque podem mudar.*
```

### Creative Agent

Produz automaticamente:

- card vertical;
- card quadrado;
- imagem para WhatsApp;
- thumbnail;
- capa de vídeo;
- variações A/B de headline.

Pode usar um template HTML/CSS renderizado como PNG ou uma integração com Canva. HTML é mais barato, previsível e escalável; IA generativa entra apenas quando realmente melhora o criativo.

---

## 2\. Automação do WhatsApp

A Meta agora possui uma **Groups API oficial**, capaz de criar, administrar e enviar mensagens para grupos por meio da Cloud API. Porém, a empresa precisa possuir uma **Official Business Account — OBA**, e o recurso não é disponibilizado para números comuns do aplicativo WhatsApp Business. Os grupos são baseados em convite e a API também oferece gerenciamento de links e participantes. [^2]

Isso permite replicar tecnicamente o padrão mostrado:

```
Grupão #1 lotado
      ↓
Sistema cria Grupão #2
      ↓
Gera link de convite
      ↓
Atualiza página de entrada
      ↓
Publica ofertas nos grupos ativos
      ↓
Registra entrega e falhas
```

## Duas rotas possíveis

### Rota oficial e escalável

- Meta Cloud API.
- WhatsApp Groups API.
- Conta OBA.
- Webhooks oficiais.
- n8n para orquestração.
- PostgreSQL para grupos, produtos e mensagens.

É a rota recomendada para construir um ativo durável.

### Rota provisória

- Telegram Channel totalmente automatizado.
- Página pública de ofertas.
- WhatsApp usado para opt-in, relacionamento e notificações permitidas.

Eu não colocaria Evolution API ou automação baseada em sessão de WhatsApp Web como núcleo de uma operação que pretende escalar. Pode servir para protótipo controlado, mas cria dependência operacional e risco de indisponibilidade.

---

## 3\. Fábrica de trailers cinematográficos

Não faz sentido produzir um filme da Marvel para cada boné de R$21. A fábrica precisa ter níveis.

## Tier 1 — Oferta rápida

Para a maioria das promoções:

- duração: 8–12 segundos;
- animação de produto;
- preço anterior versus preço atual;
- trilha;
- CTA;
- render automático via FFmpeg.

Custo e tempo baixos.

## Tier 2 — Trailer de produto

Para produtos com score alto:

- duração: 15–25 segundos;
- 3 a 5 cenas;
- produto inserido em cenários;
- narração curta;
- sound design;
- transições cinematográficas;
- CTA final.

Exemplo para uma estante:

```
Cena 1 — Um quarto caótico, iluminação dramática.
Cena 2 — A estante surge sendo montada em cortes rápidos.
Cena 3 — Livros e objetos se organizam automaticamente.
Cena 4 — Close cinematográfico na estrutura.
Cena 5 — “De R$251 por R$225 — enquanto durar.”
```

## Tier 3 — Hero Trailer

Uma ou duas vezes por semana:

- 30–45 segundos;
- storytelling;
- qualidade superior;
- produto campeão de comissão;
- vídeo usado em Shorts, TikTok, Reels e anúncios institucionais do canal.

## Pipeline técnico

```
Produto aprovado
    ↓
Claude cria hook e roteiro
    ↓
Claude cria storyboard e prompts
    ↓
Geração das cenas
    ↓
Narração por TTS
    ↓
Trilha licenciada ou gerada
    ↓
FFmpeg monta cenas, legendas e CTA
    ↓
QC automático
    ↓
Aprovação ou publicação
```

O QC deve verificar:

- duração;
- resolução 9:16;
- áreas seguras;
- erros no preço;
- produto deformado;
- texto cortado;
- áudio alto demais;
- presença da divulgação de afiliado;
- identificação de conteúdo gerado por IA quando necessária.

---

## 4\. Publicação automática

## YouTube Shorts

O upload pode ser feito oficialmente pela YouTube Data API usando OAuth 2.0. O método de upload aceita o vídeo e seus metadados, como título, descrição, tags e privacidade. [^3]

Fluxo:

```
Render final
 → gerar título e descrição
 → upload pelo videos.insert
 → definir thumbnail
 → salvar video_id
 → registrar publicação
 → coletar métricas
```

## TikTok

O TikTok oferece Content Posting API para upload e publicação. Para publicação pública automática, o aplicativo precisa passar pela auditoria do TikTok; clientes ainda não auditados ficam limitados a conteúdo privado. A API também possui campos específicos para marcar conteúdo promocional e conteúdo gerado por IA. [^4]

Fluxo:

```
Consultar configurações do criador
 → obter consentimento
 → iniciar publicação
 → transferir vídeo
 → consultar status
 → registrar post_id
```

Para o MVP, o TikTok pode começar em modo semiautomático:

1. sistema gera vídeo, legenda e capa;
2. envia como rascunho;
3. operador revisa e publica;
4. após validação, solicita auditoria para Direct Post público.

---

## 5\. Workflows n8n

## Workflow 01 — Ingestão

```
Schedule Trigger
→ Google Sheets / API
→ Normalize Product
→ Validate URL
→ Check Duplicate
→ Save PostgreSQL
```

## Workflow 02 — Validação e ranking

```
New Product
→ Check Price
→ Check Stock
→ Check Channel Policy
→ Calculate Offer Score
→ IF Score >= 60
→ Add to Publication Queue
```

## Workflow 03 — Card e mensagem

```
Approved Offer
→ Claude Copy
→ Render HTML Card
→ Upload Storage
→ Generate Tracking URL
→ Schedule Publication
```

## Workflow 04 — WhatsApp

```
Scheduled Offer
→ Revalidate Price
→ Select Eligible Groups
→ Send Group Message
→ Record Message ID
→ Retry Failed Groups
```

## Workflow 05 — Trailer Factory

```
Offer Score >= 75
→ Generate Script
→ Generate Storyboard
→ Generate Scenes
→ Generate Voice
→ FFmpeg Composition
→ Automated QC
→ Approval Queue
```

## Workflow 06 — Social publishing

```
Approved Video
├→ YouTube Upload
├→ TikTok Upload/Draft
└→ Store Publication IDs
```

## Workflow 07 — Aprendizado

```
Clicks + Sales + Commission
→ Attribution
→ Update Product Performance
→ Update Category Performance
→ Adjust Ranking Weights
```

---

## 6\. Dashboard necessária

A interface deve conter somente o essencial:

### Ofertas

- produto;
- preço;
- desconto;
- comissão;
- score;
- estoque;
- canais permitidos;
- status.

### Fila editorial

- aguardando validação;
- card pronto;
- vídeo em produção;
- aprovado;
- agendado;
- publicado;
- expirado.

### Grupos e canais

- nome;
- número de participantes;
- capacidade;
- link ativo;
- status;
- última publicação.

### Analytics

- cliques;
- CTR;
- pedidos;
- comissão;
- receita por produto;
- receita por categoria;
- receita por grupo;
- receita por vídeo;
- custo de geração;
- lucro líquido.

### Configurações

- contas de afiliado;
- etiquetas/subIDs;
- templates;
- frequência máxima;
- horários;
- categorias bloqueadas;
- margem mínima;
- desconto mínimo.

---

## 7\. Banco de dados mínimo

```
affiliate_accounts
products
offers
affiliate_links
channels
groups
group_membership_stats
creative_assets
videos
publication_queue
publications
click_events
conversion_events
commissions
policy_rules
workflow_logs
```

Cada link deve receber um identificador:

```
/source/whatsapp/group-03/product-847
/source/tiktok/video-221/product-847
/source/youtube/short-331/product-847
```

Assim o sistema descobre não apenas o que vendeu, mas **qual criativo, canal, horário e grupo geraram a venda**.

---

## MVP recomendado

## Etapa 1 — Máquina de ofertas

- Google Sheets como entrada.
- PostgreSQL.
- validador;
- score;
- card automático;
- página pública;
- Telegram ou canal permitido;
- dashboard simples.

## Etapa 2 — WhatsApp oficial

- Business Manager;
- OBA;
- Cloud API;
- Groups API;
- criação e rotação de grupos;
- webhooks;
- opt-in e links de convite.

## Etapa 3 — Vídeo vertical

- três templates de vídeo;
- Claude para roteiro;
- geração de cenas;
- ElevenLabs ou TTS equivalente;
- FFmpeg;
- publicação no YouTube;
- TikTok inicialmente como rascunho.

## Etapa 4 — Autopilot econômico

- importar conversões;
- recalibrar score;
- priorizar categorias;
- cortar formatos com ROI ruim;
- aumentar produção dos vencedores.

A primeira versão não deve tentar minerar milhões de produtos nem produzir 100 trailers cinematográficos por dia. O MVP correto é:

> **20–40 ofertas validadas por dia, cards automáticos, 3–5 vídeos rápidos e 1 trailer premium diário, com rastreamento completo de comissão.**

Isso já cria uma operação funcional, mensurável e preparada para multiplicar grupos e contas sem transformar o backend numa feira intergaláctica.

[^1]: [mercadolivre.com.br](https://www.mercadolivre.com.br/l/afiliados-compartilhamento-de-publicacao?utm_source=chatgpt.com)

[^2]: [developers.facebook.com](https://developers.facebook.com/documentation/business-messaging/whatsapp/groups?utm_source=chatgpt.com)

[^3]: [developers.google.com](https://developers.google.com/youtube/v3/guides/uploading_a_video)

[^4]: [developers.tiktok.com](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post)