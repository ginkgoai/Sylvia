---
title: "Automatização Dropshipping Amazon"
source: "https://chatgpt.com/c/6a62b308-f508-83e9-8a9e-a5fc9e466389"
author:
published:
created: 2026-07-24
description: "ChatGPT conversation with 4 messages"
tags:
  - "clippings"
---
**Você disse**

Estava conversando com um Parceiro, ele precisa automatizar a operação dele utilizando apenas Claude: a operação dele se trata de um Dropshiping novo pela Amazon, onde encontra produtos iguais entre Amazon e Shopee que esteja mais barato já Shopee, ele pega de lá, com desconto e frete grátis cupons que ele tem, e anuncia na Amazon, depois que o Lead compra ainda tem uma ou outra coisinha para preencher de dados, ele também utiliza dolphin-anty para projetar várias contas Shopee, ainda a mais informações que devemos aprender com o parceiro: então planeje as perguntas principais, a operação dele já está validada e com faturamento de 10k mês, imagino que precisará de um Agente minerador pesquisando o produto perfeito, um agente redator escrevendo as informações de envio, um agente social interagindo com comentários, um agente avisando o Lead que foi postado o produto, um agente procurando fornecedor que precisa do produto. Tudo rodando no Claude, um disparo por email de vendas e uma planilha automatizada. Pesquise total tudo sobre a Amazon, e as burocracias envolvidas para automatizar isso.

---

Há uma oportunidade interessante aqui, mas existe um ponto crítico que precisa ser entendido antes da arquitetura.

O fluxo descrito (comprar em um varejista como Shopee somente após vender na Amazon e pedir que esse varejista envie diretamente ao cliente) entra em conflito com a política oficial de dropshipping da Amazon em muitos casos. A Amazon proíbe comprar de outro varejista e fazer com que ele envie diretamente ao cliente quando o pacote, nota, embalagem ou documentos identifiquem esse terceiro como vendedor. Violações podem levar à suspensão da conta. [^1]

Isso não impede automatizar a operação. Significa apenas que o desenho deve ser feito considerando conformidade, e primeiro precisamos entender exatamente como ele opera.

## Objetivo da descoberta

Antes de escrever uma linha de prompt no Claude, eu faria uma sessão de descoberta de aproximadamente 90 minutos.

As perguntas seriam divididas em blocos.

### 1\. Operação

- Quantos pedidos por dia?
- Quantos SKUs ativos?
- Quantos produtos novos entram diariamente?
- Quantos pedidos por conta Shopee?
- Qual ticket médio?
- Margem mínima?
- ROI esperado?
- Taxa de cancelamento?
- Tempo médio de envio?
- Quais categorias possuem maior conversão?

---

### 2\. Pesquisa de produtos

Como ele encontra produtos?

Manual?

Pesquisa na Shopee?

Pesquisa na Amazon?

Existe alguma regra como:

- lucro mínimo
- diferença percentual
- frete
- peso
- avaliações
- número de vendas
- prazo

Ele pesquisa:

- 100 produtos?
- 500?
- 5.000?

Quanto tempo leva?

---

### 3\. Publicação

Como anuncia?

Produto já existe?

Cria anúncio?

Usa IA?

Usa SP-API?

Usa Seller Central?

Copia descrição?

Reescreve?

Quem gera título?

Quem gera SEO?

Quem define preço?

---

### 4\. Após vender

Quando chega uma venda...

O que acontece exatamente?

Abrir Seller Central

↓

Copiar endereço

↓

Entrar Shopee

↓

Comprar

↓

Aplicar cupom

↓

Selecionar conta Dolphin

↓

Escolher frete

↓

Inserir endereço

↓

Pagar

↓

Esperar código

↓

Enviar código Amazon

↓

Enviar mensagem cliente

Precisamos saber literalmente clique por clique.

---

### 5\. Dolphin Anty

Quantos perfis?

Cada perfil representa:

- uma conta?
- um CPF?
- um IP?
- um navegador?

Como ele troca?

Manual?

Existe automação?

---

### 6\. Shopee

Como consegue cupons?

Como consegue frete grátis?

Existem limites?

Os cupons vencem?

São reutilizáveis?

Como decide qual conta usar?

---

### 7\. Amazon

Seller Individual?

Professional?

Brasil?

EUA?

MFN?

FBA?

SP-API habilitada?

Tem acesso API?

Recebe pedidos via e-mail?

Via Seller Central?

Via API?

---

### 8\. Atendimento

Quem responde?

Perguntas

Trocas

Reembolso

Avaliações

Mensagens

Tudo manual?

---

### 9\. Financeiro

Como controla?

Excel?

Google Sheets?

ERP?

Quanto lucrou?

Quanto gastou?

Quais cupons foram usados?

---

### 10\. Escala

Meta?

100 pedidos/dia?

500?

1000?

Isso muda completamente a arquitetura.

---

## Depois disso desenhamos os agentes.

## Agente 1 — Miner

Pesquisa produtos continuamente.

Entrada:

Amazon + Shopee

Saída:

Produtos aprovados.

Analisa:

- margem
- frete
- avaliações
- estoque
- risco
- concorrência

---

## Agente 2 — Pricing

Calcula

Preço Amazon

Taxas

Margem

Lucro

Preço ideal.

---

## Agente 3 — Publisher

Cria anúncios.

Escreve

Título

Bullet Points

Descrição

SEO

Palavras-chave

Categoria

---

## Agente 4 — Order Brain

Monitora novas vendas.

A Amazon oferece notificações e APIs oficiais para eventos de pedidos, reduzindo a necessidade de consultas constantes. [^2]

Quando chega pedido:

↓

cria workflow.

---

## Agente 5 — Fulfillment Assistant

Não compra automaticamente.

Preenche:

- endereço
- telefone
- CEP
- observações

Deixa tudo pronto para conferência humana quando necessário.

---

## Agente 6 — Customer Service

Responde perguntas.

Entrega.

Atrasos.

Garantia.

Trocas.

Tudo usando Claude.

---

## Agente 7 — Reviews

Monitora avaliações.

Detecta risco.

Sugere respostas.

---

## Agente 8 — Supplier Hunter

Pesquisa fornecedores melhores.

Compara:

Shopee

Distribuidores

Importadores

Fabricantes

Encontrando fontes mais estáveis e compatíveis com a política da Amazon.

---

## Agente 9 — Analytics

Dashboard.

KPIs.

Lucro.

ROI.

Margem.

Produtos campeões.

Categorias.

Tempo médio.

---

## Agente 10 — Auditor

Detecta:

produto sem estoque

queda de preço

concorrente

prazo aumentado

cupom expirado

risco de prejuízo

---

## Claude como "Sistema Operacional"

Em vez de dezenas de prompts independentes, faria um único projeto no Claude com:

- Memória da operação.
- Procedimentos operacionais.
- Políticas da Amazon.
- Estrutura de prompts.
- Planilhas.
- Histórico.
- Dashboards.
- Base de conhecimento.

Cada agente seria um subagente especializado.

---

## Integrações mínimas

- Claude (Projects + subagentes)
- Gmail (alertas)
- Google Sheets (controle financeiro)
- Amazon Seller Central / SP-API (quando disponível)
- Navegador automatizado apenas para tarefas que não possuam API oficial
- Dolphin Anty (apenas se o uso estiver em conformidade com os termos das plataformas)

---

## Minha sugestão

Não começaria automatizando os cliques.

Começaria automatizando o conhecimento da operação.

Fase 1:

- descoberta completa;
- documentação;
- prompts;
- planilhas.

Fase 2:

- mineração de produtos;
- cálculo de margem;
- geração de anúncios;
- atendimento.

Fase 3:

- integração oficial com Amazon (SP-API);
- notificações;
- relatórios.

Fase 4:

- apenas as etapas restantes que realmente exigem interação com interfaces web e não possuem APIs adequadas, sempre respeitando as políticas das plataformas.

Esse caminho tende a produzir uma automação mais robusta e reduz o risco operacional em comparação com uma solução baseada apenas em automação de navegador desde o início.

---

**Você disse**

Deixa as perguntas mais resumidas e essenciais, focada na operação inteira, para você ter acesso a todo entendimento do negócio completo, pense em um questionário que faria para o CEO e operador dessa operação agora

---

Eu faria uma entrevista de 20 a 30 minutos. O objetivo não é entender apenas o processo atual, mas capturar todo o "modelo mental" do operador para que depois possamos transformá-lo em agentes no Claude.

## Questionário de Descoberta – Operação Amazon × Shopee

## 1\. Visão Geral

1. Explique sua operação do início ao fim, como se estivesse treinando um novo funcionário.
2. Quais etapas hoje são totalmente manuais?
3. Quais etapas você considera mais demoradas ou repetitivas?

## 2\. Produtos

4. Como você encontra um produto vencedor?
5. Quais critérios um produto precisa atender para ser anunciado?
6. Como você decide o preço de venda?

## 3\. Publicação

7. Como um anúncio nasce? Quais informações você preenche e de onde elas vêm?
8. O que você altera em relação ao anúncio original da Shopee?

## 4\. Venda

9. O que acontece exatamente, passo a passo, quando entra uma venda na Amazon?
10. Em quais momentos você precisa tomar decisões?

## 5\. Compra na Shopee

11. Como escolhe qual conta Shopee utilizar?
12. Como decide qual cupom, frete ou promoção aplicar?
13. Existe algum limite ou regra para uso das contas?

## 6\. Envio

14. Como você envia o pedido ao cliente final?
15. Como informa o código de rastreio na Amazon?
16. Existem exceções frequentes (sem estoque, atraso, cancelamento)?

## 7\. Atendimento

17. Quais mensagens você mais responde aos clientes?
18. Como lida com devoluções, reclamações e avaliações negativas?

## 8\. Controle

19. Como acompanha lucro, pedidos, cupons e desempenho hoje?
20. Quais métricas você olha diariamente?

## 9\. Ferramentas

21. Quais sistemas você usa diariamente (Amazon, Shopee, Dolphin Anty, planilhas, e-mail etc.)?
22. Existe alguma API, integração ou exportação que você já utiliza?

## 10\. Escala

23. O que impediria você de dobrar o volume de pedidos amanhã?
24. Se tivesse uma equipe de IA trabalhando 24h por dia, quais tarefas você delegaria primeiro?
25. O que nunca pode ser automatizado e precisa continuar sob decisão humana?

---

## Última pergunta (a mais importante)

> **Se eu observasse sua tela durante um dia inteiro de trabalho, quais seriam todos os cliques, decisões e exceções que você faria, e por quê?**

Essa resposta normalmente revela 80% do conhecimento operacional que não aparece em um fluxograma.

Com essas respostas, é possível desenhar:

- o mapa completo da operação;
- os SOPs (Procedimentos Operacionais Padrão);
- os agentes especializados do Claude;
- os gatilhos entre agentes;
- os pontos de decisão humana;
- e a arquitetura completa da automação, priorizando primeiro as tarefas de maior impacto e menor risco.

[^1]: [sellercentral.amazon.com](https://sellercentral.amazon.com/seller-forums/discussions/t/eb0ed778-d33a-4ec2-831b-e5561e03f352?mons_sel_locale=pt_BR&pageName=US%3ASC%3ATrim-seller-forums%2Fdiscussions%2Ft%2Feb0ed778-d33a-4ec2-831b-e5561e03f352&utm_source=chatgpt.com)

[^2]: [developer-docs.amazon](https://developer-docs.amazon/sp-api/docs/tutorial-subscribe-to-order-change-notification?utm_source=chatgpt.com)