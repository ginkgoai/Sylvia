---
title: "Organização de Contas Ginkgo"
source: "https://chatgpt.com/c/6a6d619a-13f8-83e9-98ad-6aac3a043483"
author:
published:
created: 2026-08-02
description: "ChatGPT conversation with 2 messages"
tags:
  - "clippings"
---
**Você disse**

me ajude a organizar o meta da ginkgo, contas como facebook, instagram, tudo que tiver vinculado. quero tirar o vinculo com minhas contas pessoais, e adicionar colaboradores. exemplo a pagina do facebook só posso entrar com o meu perfil pessoal. whatsaap busines, etc. vamos organizar tudo como deve ser, adicione tambem uma camada só como mapa mental, outras redes. x, linkedin, youtube, tiktok, github. automatizaremos postagem e conteudo diario de cada / colocaremos um colaborador administrativo. de inicio, será um colaborador: Tiffany Ribeiro, apenas para gestorar as contas, as automações e postagens serão criadas e disparadas por mim, via n8n ou outras tecnicas, ela ficara encarregada de anuncios, stories e dms.

---

## Objetivo correto

Não tente “desconectar tudo do perfil pessoal” de uma vez. Isso pode deixar a empresa trancada do lado de fora da própria nave.

O modelo profissional é:

- **Perfil pessoal ou conta individual:** identidade de autenticação.
- **Business Portfolio / Business Center / Organização:** proprietário dos ativos.
- **Tiffany:** acesso individual e limitado às tarefas dela.
- **n8n:** acesso técnico por API, OAuth ou usuário de sistema.
- **Senhas:** nunca compartilhadas.

No Facebook, o perfil pessoal funciona como um crachá para acessar a Página. A Página e os demais ativos devem ficar dentro do **Business Portfolio da Ginkgo**. A Meta também oferece contas corporativas gerenciadas, chamadas *managed Meta accounts*, mas isso pode ser implantado numa segunda etapa. [^1]

---

## Arquitetura de acesso da Ginkgo

| Camada | Responsável | Poder |
| --- | --- | --- |
| Proprietário institucional | Gabriel | Controle total, segurança, cobrança, APIs e usuários |
| Operação social | Tiffany Ribeiro | Anúncios, stories, DMs, comentários, leads e relatórios |
| Automação | n8n / Ginkgo Apps | Publicação, coleta de métricas e distribuição |
| Recuperação | Segundo proprietário futuro | Apenas contingência |
| Cofre | Password manager | Senhas, recovery codes, chaves e tokens |

**Tiffany não deve receber controle total do Business Portfolio.** Na Meta, pessoas com controle total podem alterar acessos, configurações e até excluir ativos; o acesso por tarefas permite operar conteúdo, mensagens e anúncios pelo Business Suite sem entregar as chaves do castelo. [^2]

---

## 1\. Organização da Meta Ginkgo

Pelo seu print, já existe um ambiente “Ginkgo AI Syste…” no Meta Business Suite e existe uma campanha de leads ativa. Portanto, não remova nenhum acesso ou ativo antes do inventário.

## Estrutura final desejada

```
Meta Business Portfolio — Ginkgo AI Systems
│
├── Pessoas
│   ├── Gabriel — Controle total
│   └── Tiffany Ribeiro — Acesso parcial
│
├── Contas
│   ├── Página Facebook Ginkgo AI Systems
│   ├── Instagram profissional Ginkgo
│   ├── Conta de anúncios Ginkgo
│   └── Conta do WhatsApp Business
│
├── Fontes de dados
│   ├── Pixel / Dataset
│   ├── Conversões
│   ├── Públicos
│   └── Catálogos
│
├── Tecnologia
│   ├── Meta App Ginkgo
│   ├── Usuário de sistema n8n
│   └── Tokens da Graph API
│
└── Segurança
    ├── 2FA obrigatório
    ├── Domínio verificado
    ├── Empresa verificada
    └── Métodos de pagamento corporativos
```

Um Business Portfolio existe justamente para reunir Página, Instagram, anúncios, WhatsApp e demais ativos empresariais em uma única estrutura de propriedade e permissões. [^3]

---

## Ordem exata dentro do Meta Business Suite

### Etapa A — Inventário

No menu inferior esquerdo do seu print, abra **Configurações**.

Registre:

1. Nome e ID do Business Portfolio.
2. Pessoas com acesso.
3. Página vinculada.
4. Instagram vinculado.
5. Conta de anúncios e proprietário.
6. Método de pagamento.
7. Pixel ou Dataset.
8. Catálogos.
9. Conta do WhatsApp.
10. Apps, parceiros e usuários de sistema.

Não exclua duplicidades ainda. Primeiro identificamos quem é realmente proprietário e quem apenas tem acesso compartilhado.

### Etapa B — Segurança

Em **Central de Segurança**:

- Exija autenticação em dois fatores para todas as pessoas.
- Use aplicativo autenticador, não apenas SMS.
- Salve os códigos de recuperação no cofre.
- Verifique o domínio `ginkgosystems.tech`.
- Use e-mails corporativos individuais.

A Meta permite exigir 2FA para integrantes do Business Portfolio e recomenda aplicativo autenticador para reduzir problemas de acesso. [^4]

E-mails recomendados:

```
gabriel@ginkgosystems.tech
tiffany@ginkgosystems.tech
social@ginkgosystems.tech
ads@ginkgosystems.tech
automacoes@ginkgosystems.tech
financeiro@ginkgosystems.tech
```

`social@`, `ads@` e `automacoes@` devem ser caixas funcionais ou aliases. Cada pessoa continua usando sua própria identidade para acessar as plataformas.

---

## Etapa C — Adicionar Tiffany

Caminho aproximado:

```
Configurações
→ Usuários
→ Pessoas
→ Convidar pessoas
```

A Meta permite convidar uma pessoa e depois atribuir somente os ativos e permissões necessários. [^5]

Use o e-mail corporativo da Tiffany e configure:

### Business Portfolio

- **Acesso parcial:** sim.
- **Controle total:** não.
- Gerenciar pessoas: não.
- Gerenciar parceiros: não.
- Gerenciar apps: não.
- Gerenciar usuários de sistema: não.
- Gerenciar cobrança: não.

### Página do Facebook

Conceder:

- Criar e gerenciar conteúdo.
- Stories e reels.
- Mensagens.
- Comentários e atividade da comunidade.
- Visualizar insights.
- Criar e gerenciar anúncios.
- Acessar leads.

Não conceder:

- Controle total da Página.
- Gerenciamento de acessos.
- Exclusão ou alteração estrutural da Página.

### Instagram

Conceder:

- Conteúdo.
- Stories e reels.
- Mensagens.
- Comentários.
- Insights.
- Anúncios.

### Conta de anúncios

Conceder:

- Visualizar campanhas.
- Criar e editar campanhas.
- Gerenciar anúncios.
- Visualizar resultados e leads.

Não conceder:

- Administrar conta de anúncios.
- Alterar métodos de pagamento.
- Alterar limites de gastos.
- Adicionar pessoas ou parceiros.
- Encerrar a conta.

### Pixel, Dataset e públicos

- Leitura e uso em campanhas.
- Sem administração ou exclusão.
- Sem compartilhamento com terceiros.

---

## Etapa D — Corrigir a Página do Facebook

Existem duas camadas que devem ser verificadas:

1. **A Página dentro do Business Portfolio.**
2. **Os acessos diretos configurados na própria Página.**

Verifique:

```
Página do Facebook
→ Configurações
→ Configuração da Página
→ Acesso à Página
```

Você provavelmente aparecerá em “Pessoas com acesso do Facebook”. Isso é normal. O importante é a Página também constar como ativo pertencente ao Business Portfolio correto.

Somente depois disso:

- Remova acessos antigos.
- Remova agências ou parceiros desconhecidos.
- Elimine perfis duplicados.
- Mantenha Gabriel com controle total.
- Mantenha Tiffany por tarefas.

O acesso direto com controle total permite administrar acessos e configurações; o acesso por tarefas é operado por ferramentas como Business Suite e Ads Manager. [^2]

---

## 2\. Instagram

A conta deve estar configurada como **Instagram profissional — Empresa** e vinculada simultaneamente a:

```
Página Facebook Ginkgo
+
Business Portfolio Ginkgo
+
Conta de anúncios Ginkgo
```

Evite:

- Instagram conectado somente pelo seu Accounts Center pessoal.
- Senha compartilhada com Tiffany.
- n8n autenticado usando sua sessão pessoal.
- Várias ferramentas publicadoras disputando o mesmo token.

Para automação, utilize a Instagram Graph API. A API oficial permite publicar conteúdo em contas profissionais e possui limites de publicação que devem ser respeitados. [^6]

---

## 3\. WhatsApp Business

Aqui existem dois possíveis cenários.

## Cenário profissional recomendado

```
Número corporativo Ginkgo
→ WhatsApp Business Account — WABA
→ Meta Business Portfolio
→ WhatsApp Cloud API ou BSP
→ Chatwoot
→ n8n
→ Leaf / agentes
```

Tiffany trabalha pela:

- Caixa de Entrada do Meta Business Suite; ou
- Chatwoot.

Ela não precisa da senha, chip, QR code permanente nem acesso administrativo ao número.

A Meta permite adicionar pessoas à conta do WhatsApp Business e definir níveis de permissão. [^7]

### Permissões da Tiffany no WhatsApp

Conceder:

- Ler e responder conversas.
- Classificar e encaminhar contatos.
- Acompanhar leads.
- Consultar métricas operacionais.

Não conceder:

- Remover o número.
- Alterar PIN ou configurações de segurança.
- Administrar templates técnicos.
- Administrar aplicativos e tokens.
- Alterar cobrança.
- Migrar a conta para outro parceiro.

Se o número atual estiver conectado por sessão QR/Evolution API, não faça migração impulsiva. Primeiro documente:

```
Número
Proprietário do chip
PIN de verificação
E-mail de recuperação
Histórico necessário
Integrações n8n
Webhooks
Chatwoot
Agentes ativos
```

Depois decidimos entre manter a sessão atual temporariamente ou migrar para a Cloud API.

---

## 4\. Automação Meta via n8n

Não utilize o token pessoal de Gabriel como motor permanente.

Crie:

```
Meta App — Ginkgo Social Publisher
+
System User — ginkgo-n8n-production
+
Permissões mínimas por ativo
+
Token guardado no n8n Credentials
```

Usuários de sistema da Meta existem especificamente para representar servidores ou softwares que realizam chamadas de API sobre ativos empresariais. [^8]

Separação recomendada:

```
ginkgo-n8n-social
ginkgo-n8n-ads
ginkgo-whatsapp-production
```

Assim, se um token de publicação falhar, ele não derruba anúncios, WhatsApp e CRM junto. Monólitos de credencial são o equivalente digital de ligar toda a Estrela da Morte numa única extensão.

---

## 5\. Matriz de acessos da Tiffany

| Plataforma | Papel recomendado | Não conceder |
| --- | --- | --- |
| Meta Business Portfolio | Acesso parcial | Controle total |
| Facebook | Conteúdo, comunidade, mensagens e anúncios | Gerenciar acessos e excluir Página |
| Instagram | Conteúdo, stories, DMs, comentários e anúncios | Senha e propriedade |
| Meta Ads | Gerenciar campanhas | Financeiro e administração |
| WhatsApp | Atendimento pela Inbox ou Chatwoot | Número, PIN, tokens e migração |
| LinkedIn | Content Admin + Campaign Manager | Super Admin |
| X | Contributor | Admin ou senha |
| YouTube | Editor limitado | Owner ou Manager |
| TikTok | Standard Member com ativos atribuídos | Business Center Admin |
| GitHub | Nenhum inicialmente | Owner ou acesso aos repositórios |
| n8n | Nenhum inicialmente | Credenciais, produção e tokens |

---

## 6\. Outras redes

## LinkedIn

No LinkedIn, a Página também é administrada por perfis pessoais individuais. Não existe uma senha separada da Página. Os papéis principais são Super Admin, Content Admin e Analyst. O Content Admin pode publicar, responder, gerenciar conteúdo e mensagens de Páginas elegíveis; anúncios exigem permissões adicionais no Campaign Manager. [^9]

Configuração:

```
Gabriel
├── Super Admin da Página
├── Account Manager da conta de anúncios
└── Billing Admin

Tiffany
├── Content Admin
├── Campaign Manager
└── Lead Gen Forms Manager, quando necessário
```

---

## X

Crie ou mantenha a conta institucional da Ginkgo e utilize **X Delegate**.

```
Gabriel — Owner
Tiffany — Contributor
```

Contributor pode publicar, agendar, responder e operar DMs, mas não administra os demais delegados. Não compartilhe a senha. [^10]

Para automações, evite DMs, menções ou respostas automatizadas em massa. O X permite publicações automatizadas, mas proíbe abordagens não solicitadas e comportamento duplicado ou semelhante a spam. [^11]

---

## YouTube

Use **Channel Permissions** no YouTube Studio:

```
Gabriel — Owner
Tiffany — Editor (Limited)
```

Editor limitado pode publicar, editar, comentar e gerenciar lives, mas não acessa dados de receita nem gerencia permissões. Isso é mais seguro do que compartilhar a conta Google. [^12]

Para automação, utilize YouTube Data API com OAuth da Ginkgo. A API suporta upload, metadados e gerenciamento de vídeos. [^13]

---

## TikTok

Crie um **TikTok Business Center — Ginkgo AI Systems**.

```
Gabriel — Business Center Admin
Tiffany — Standard Member
```

Atribua especificamente:

- Conta TikTok Ginkgo.
- Conta de anúncios.
- Leads.
- Pixels.
- Catálogos, quando houver.

O TikTok Business Center permite conceder permissões por conta e por ativo, sem transformar todo colaborador em administrador. [^14]

Para publicação automatizada, utilize a Content Posting API. Aplicações não verificadas podem ter restrições de visibilidade, portanto o caminho de produção inclui registro do app e revisão adequada. [^15]

---

## GitHub

Estruture todos os projetos em uma organização:

```
GitHub Organization — ginkgo-ai-systems
│
├── leaf
├── ginkgo-connect
├── ginkgo-workforce
├── ginkgo-amazon-ops
├── automations-n8n
├── infrastructure
└── brand-assets
```

Tiffany não precisa entrar no GitHub neste momento. Caso precise baixar arquivos de marca, entregue via Drive ou conceda somente leitura a um repositório específico.

O GitHub diferencia Owner, Member, equipes, papéis por repositório e colaboradores externos. A própria documentação recomenda mais de um proprietário para continuidade, mas o segundo proprietário deve ser alguém técnico e altamente confiável. [^16]

Automações devem utilizar GitHub Apps ou GitHub Actions, não o token pessoal de Gabriel. [^17]

---

## 7\. Mapa mental geral

```
GINKGO DIGITAL HQ
│
├── IDENTIDADE E PROPRIEDADE
│   ├── Domínio ginkgosystems.tech
│   ├── E-mails corporativos
│   ├── Password manager
│   ├── 2FA
│   └── Recovery codes
│
├── META ECOSYSTEM
│   ├── Facebook
│   ├── Instagram
│   ├── Threads
│   ├── WhatsApp
│   ├── Ads Manager
│   ├── Pixel / Dataset
│   └── Catálogos
│
├── SOCIAL DISTRIBUTION
│   ├── LinkedIn
│   ├── X
│   ├── YouTube
│   ├── TikTok
│   └── Google Business Profile
│
├── COMUNIDADE
│   ├── Discord
│   ├── WhatsApp Community
│   ├── Newsletter
│   └── Telegram
│
├── TECNOLOGIA
│   ├── GitHub Organization
│   ├── n8n
│   ├── Postgres
│   ├── Redis
│   ├── Media Factory / Pyre
│   └── APIs oficiais
│
├── OPERAÇÃO HUMANA
│   ├── Gabriel
│   │   ├── Estratégia
│   │   ├── Aprovação
│   │   ├── Automação
│   │   └── Segurança
│   │
│   └── Tiffany
│       ├── Anúncios
│       ├── Stories
│       ├── DMs
│       ├── Comentários
│       ├── Leads
│       └── Relatório semanal
│
└── AUTOMAÇÃO
    ├── Pesquisa
    ├── Roteiro
    ├── Geração de criativo
    ├── Aprovação Gabriel
    ├── Publicação
    ├── Coleta de métricas
    └── Otimização
```

---

## 8\. Pipeline diário de conteúdo

```
Banco editorial
→ Pesquisa de tendências
→ IA gera roteiro e copy
→ Geração de imagem ou vídeo
→ Validação automática
→ Aprovação de Gabriel
→ Adaptação por plataforma
→ Publicação via API
→ Tiffany acompanha DMs e comentários
→ Métricas retornam ao Postgres
→ Relatório e novas hipóteses
```

Distribuição por canal:

| Canal | Função |
| --- | --- |
| Instagram | Branding, reels, carrosséis e prova social |
| Facebook | PME, grupos, anúncios e geração de leads |
| LinkedIn | Autoridade institucional, cases e B2B |
| TikTok | Alcance, demonstrações e conteúdo viral |
| YouTube | Educação, demos, shorts e conteúdo duradouro |
| X | Notícias, opiniões rápidas e construção pública |
| GitHub | Prova técnica, documentação e open source |
| WhatsApp | Conversão, atendimento e retenção |

---

## 9\. Divisão operacional final

## Gabriel

- Proprietário de todas as organizações.
- Estratégia e calendário editorial.
- Desenvolvimento dos workflows n8n.
- Gestão das APIs e credenciais.
- Aprovação de conteúdo.
- Produtos, integrações e infraestrutura.
- Aprovação final de orçamento publicitário.

## Tiffany

- Criar e otimizar campanhas.
- Publicar stories manuais e conteúdos emergenciais.
- Responder DMs e comentários.
- Qualificar e encaminhar leads.
- Organizar respostas salvas.
- Acompanhar alertas das plataformas.
- Relatório semanal de anúncios e atendimento.
- Sinalizar conteúdos que precisam de intervenção humana.

## n8n

- Criar e distribuir conteúdo aprovado.
- Publicar em horários definidos.
- Adaptar textos e formatos.
- Registrar IDs das publicações.
- Coletar métricas.
- Alertar falhas.
- Alimentar dashboards.
- Nunca responder automaticamente situações sensíveis ou reclamações críticas.

---

## Sequência de execução

1. Criar os e-mails corporativos.
2. Implantar password manager e 2FA.
3. Inventariar todos os ativos da Meta.
4. Confirmar o proprietário de cada ativo.
5. Adicionar Tiffany com acesso parcial.
6. Testar Página, Instagram, anúncios e Inbox.
7. Organizar o WhatsApp.
8. Criar organizações nas demais plataformas.
9. Migrar automações para credenciais de serviço.
10. Só então remover acessos pessoais redundantes.

**Próximo passo:** abra no Meta Business Suite **Configurações → Pessoas** e envie um print dessa tela, seguido de **Contas → Páginas**. A partir dessas duas telas será possível definir exatamente o que manter, transferir, remover e atribuir à Tiffany.

[^1]: [facebook.com](https://www.facebook.com/business/help/1710077379203657?utm_source=chatgpt.com)

[^2]: [facebook.com](https://www.facebook.com/help/289207354498410?utm_source=chatgpt.com)

[^3]: [facebook.com](https://www.facebook.com/business/help/442345745885606?utm_source=chatgpt.com)

[^4]: [facebook.com](https://www.facebook.com/business/help/280940009201586?utm_source=chatgpt.com)

[^5]: [facebook.com](https://www.facebook.com/business/help/2169003770027706?utm_source=chatgpt.com)

[^6]: [developers.facebook.com](https://developers.facebook.com/documentation/instagram-platform/content-publishing?utm_source=chatgpt.com)

[^7]: [facebook.com](https://www.facebook.com/business/help/2087193751603668?utm_source=chatgpt.com)

[^8]: [developers.facebook.com](https://developers.facebook.com/docs/business-management-apis/system-users/?utm_source=chatgpt.com)

[^9]: [linkedin.com](https://www.linkedin.com/help/linkedin/answer/a546865?utm_source=chatgpt.com)

[^10]: [help.x.com](https://help.x.com/en/managing-your-account/how-to-use-the-delegate-feature)

[^11]: [help.x.com](https://help.x.com/en/rules-and-policies/x-automation?utm_source=chatgpt.com)

[^12]: [support.google.com](https://support.google.com/youtube/answer/9481328?co=GENIE.Platform%3DAndroid&hl=en)

[^13]: [developers.google.com](https://developers.google.com/youtube/v3?utm_source=chatgpt.com)

[^14]: [ads.tiktok.com](https://ads.tiktok.com/help/article/how-to-assign-asset-level-permissions)

[^15]: [developers.tiktok.com](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post?enter_method=left_navigation&utm_source=chatgpt.com)

[^16]: [docs.github.com](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)

[^17]: [docs.github.com](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps?utm_source=chatgpt.com)