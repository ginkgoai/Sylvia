---
title: "Mercado de Direitos sobre Dados"
source: "https://chatgpt.com/c/6a684eab-a358-83e9-994f-d632c3bcf169"
author:
published:
created: 2026-07-28
description: "ChatGPT conversation with 2 messages"
tags:
  - "clippings"
---
**Você disse**

Dados são alugaveis e vendáveis? Recente vi a notícia de Peter chill comprador de todos os dados sobre medicina, onde é esse mercado de direitos sobre dados e como ele funciona

---

## Sim — dados podem gerar receita, mas normalmente não são “vendidos” como um imóvel

O mercado funciona mais como **licenciamento de petróleo digital**: o fornecedor mantém a base e concede ao comprador um direito limitado de acessar, consultar, cruzar ou produzir análises.

O que geralmente é comercializado não é a “propriedade absoluta” dos dados, mas:

- direito de uso por determinado período;
- acesso via API ou assinatura;
- licença para uma finalidade específica;
- resultados agregados e inteligência derivada;
- direito de treinar modelos, quando contratualmente e legalmente permitido;
- acesso controlado dentro de um *data clean room*;
- aquisição de uma empresa que controla a infraestrutura ou possui contratos de acesso aos dados.

## A notícia de Peter Thiel

Você provavelmente está se referindo à **Palantir**, empresa cofundada por Peter Thiel, e ao sistema público de saúde britânico, o NHS.

A Palantir ganhou um contrato de aproximadamente **£330 milhões** para fornecer a tecnologia da *Federated Data Platform* do NHS. Porém, juridicamente, isso não significa que Peter Thiel “comprou os dados médicos dos britânicos”. Os documentos oficiais dizem que o NHS continua sendo o **controlador** e que a Palantir atua como **operadora/processadora**, executando instruções do NHS. [^1]

A controvérsia é que quem controla a camada tecnológica ganha uma posição extremamente poderosa: integra sistemas, define arquitetura, processa informações e torna-se difícil de substituir. É como não possuir o petróleo, mas controlar os oleodutos, refinarias e painéis de comando.

Também existe outra notícia recente, de **27 de julho de 2026**, sobre a gestora norte-americana TPG adquirindo a Optum UK, que controla a EMIS, fornecedora de prontuários eletrônicos utilizada por mais da metade dos consultórios de atenção primária da Inglaterra. Esse caso não envolve Peter Thiel, mas pode ter sido misturado com a história da Palantir. [^2]

## Os quatro mercados de dados

### 1\. Dados não pessoais

São dados climáticos, geográficos, industriais, financeiros agregados, preços, tráfego, sensores, estoques e comportamento de máquinas.

Esses podem ser comercializados com relativamente menos restrições, desde que o vendedor tenha direito sobre a coleta, estruturação e distribuição.

Exemplos de produtos:

- preço médio de imóveis por região;
- fluxo de pessoas em determinados locais;
- produtividade de equipamentos industriais;
- dados de consumo energético;
- catálogos de produtos e preços;
- indicadores econômicos ou logísticos.

### 2\. Dados pessoais identificáveis

Nome, telefone, localização, histórico de compra, CPF, comportamento digital e outros dados relacionados a uma pessoa identificada ou identificável.

Eles não devem ser tratados como propriedade irrestrita da empresa. O controlador precisa de fundamento legal, informar finalidade, limitar o uso e permitir que o titular exerça seus direitos.

No Brasil, a LGPD declara que a pessoa natural é titular de seus dados e possui direitos de acesso, correção, eliminação, informação sobre compartilhamento e revogação de consentimento. [^3]

### 3\. Dados pessoais sensíveis

Incluem saúde, genética, biometria, origem racial, religião e outras categorias protegidas.

No caso brasileiro, dados de saúde recebem proteção especialmente rígida. A LGPD proíbe, como regra, o compartilhamento entre controladores de dados sensíveis de saúde com objetivo de obter vantagem econômica, salvo exceções relacionadas à prestação de serviços de saúde, assistência farmacêutica, portabilidade solicitada pelo titular e transações administrativas necessárias. [^3]

Portanto, uma clínica brasileira não poderia simplesmente anunciar:

> “Temos 100 mil pacientes com diabetes. Vendemos a lista para laboratórios.”

Isso seria uma sirene jurídica tocando em volume máximo.

### 4\. Dados anonimizados, agregados ou sintéticos

Esse é o terreno comercial mais interessante.

A empresa remove ou transforma identificadores para que uma pessoa não possa ser razoavelmente reidentificada. Pela LGPD, dados efetivamente anonimizados deixam de ser considerados dados pessoais, desde que a anonimização não possa ser revertida com esforços razoáveis. [^3]

Nos Estados Unidos, a HIPAA também admite dois métodos principais de desidentificação: remoção padronizada de identificadores, chamada *Safe Harbor*, ou avaliação estatística por especialista, chamada *Expert Determination*. Dados corretamente desidentificados deixam de estar sujeitos às principais restrições da HIPAA, embora outras leis e contratos ainda possam se aplicar. [^4]

**Pseudonimização não é a mesma coisa que anonimização.** Substituir o nome por um código não resolve necessariamente, porque alguém que possua a chave ou outras bases pode reconstruir a identidade. [^5]

## Onde esse mercado acontece

Não existe uma “B3 dos dados” centralizada. O mercado é fragmentado em cinco arenas.

### Marketplaces de dados

Plataformas como AWS Data Exchange e Snowflake Marketplace permitem que empresas publiquem produtos de dados e que compradores assinem licenças com preço, duração, finalidade e condições de utilização. [^6]

### Negociações privadas B2B

As transações mais valiosas normalmente não aparecem publicamente.

Uma farmacêutica pode contratar:

- acesso a dados longitudinais de tratamentos;
- índices agregados de adesão a medicamentos;
- resultados clínicos anonimizados;
- dados de prescrições e exames;
- coortes específicas para estudos;
- comparação entre terapias;
- acompanhamento de efeitos no mundo real.

Esses contratos são conhecidos no setor como **Real-World Data — RWD** e podem gerar **Real-World Evidence — RWE**.

Empresas como a IQVIA mantêm catálogos comerciais de ativos de dados de saúde e bases longitudinais não identificadas. [^7]

### Plataformas de conexão de dados

Empresas como a Datavant não precisam entregar uma planilha com pacientes. Elas usam tokenização e mecanismos de correspondência para conectar registros de hospitais, farmácias, laboratórios, seguradoras e pesquisas sem revelar diretamente a identidade ao comprador. [^8]

### Aquisição de empresas

Um investidor pode comprar:

- um sistema de prontuário;
- uma rede de clínicas;
- uma plataforma de exames;
- uma empresa de seguros;
- um aplicativo de saúde;
- um laboratório genético;
- uma empresa de pesquisas clínicas.

Ele não está necessariamente comprando a propriedade irrestrita dos dados. Está adquirindo a empresa, seus contratos, tecnologia, relacionamento com usuários e posição de controladora ou operadora, sujeita às leis aplicáveis.

Esse é o movimento mais poderoso: **comprar o porto, não cada contêiner**.

### Dados públicos e de pesquisa

Governos, universidades, biobancos e instituições de pesquisa disponibilizam bases abertas ou ambientes controlados. No Brasil, existem o Portal Brasileiro de Dados Abertos e bases do DATASUS, geralmente com dados agregados ou mecanismos de proteção. [^9]

Para estudos de saúde pública, a LGPD determina ambiente controlado e seguro, finalidade restrita, anonimização ou pseudonimização quando possível e proibição de revelar indivíduos nos resultados. [^3]

## Como uma transação de dados é estruturada

O processo profissional costuma seguir esta cadeia:

**Origem → direitos → tratamento → produto → licença → fiscalização**

1. **Origem:** quem coletou e em quais condições.
2. **Proveniência:** como os dados foram produzidos e se são confiáveis.
3. **Base legal:** consentimento, obrigação legal, pesquisa, execução contratual ou outra hipótese válida.
4. **Classificação:** pessoal, sensível, anonimizado, agregado ou não pessoal.
5. **Transformação:** limpeza, padronização, anonimização, enriquecimento e criação de metadados.
6. **Contrato:** finalidade, prazo, território, usuários permitidos e proibições.
7. **Entrega:** arquivo, API, consulta SQL, dashboard ou ambiente seguro.
8. **Auditoria:** logs, limites de consulta, prevenção de exportação e verificação de exclusão.

O comprador normalmente recebe uma licença parecida com:

> Acesso por 12 meses, exclusivamente para pesquisa epidemiológica, sem publicidade, sem tentativa de reidentificação, sem transferência a terceiros e com exclusão após o encerramento.

## O que determina o valor de uma base

Uma base vale mais quando possui:

- exclusividade;
- grande cobertura populacional;
- histórico longitudinal;
- atualizações frequentes;
- resultados clínicos confirmados;
- possibilidade de conectar diferentes fontes;
- documentação de origem;
- alta qualidade e baixa quantidade de registros incompletos;
- conformidade jurídica demonstrável;
- dados raros, como doenças pouco frequentes;
- capacidade de responder perguntas que outras bases não respondem.

**Quantidade sozinha não basta.** Dez milhões de linhas bagunçadas podem valer menos que cinquenta mil registros extremamente bem documentados.

## A oportunidade empresarial real

Para a Ginkgo, o caminho inteligente não seria criar um “camelô de banco de dados pessoais”. Seria construir a **infraestrutura de confiança que permite monetizar dados legalmente**.

Uma possível frente seria o **Ginkgo Data Trust**:

- catálogo de produtos de dados;
- rastreamento de origem e consentimentos;
- classificação automática pela LGPD;
- anonimização e avaliação de risco;
- tokenização;
- contratos de licenciamento;
- controle de finalidade;
- API com limites de utilização;
- logs imutáveis de acesso;
- *data clean rooms*;
- geração de dados sintéticos;
- cobrança por assinatura, consulta ou volume;
- agentes de IA que analisam a base sem exportá-la.

A empresa não venderia necessariamente o dado bruto. Venderia **respostas, modelos e acesso governado**.

Exemplo:

Uma rede de oficinas não vende a placa e o endereço dos clientes. Ela oferece um produto agregado mostrando falhas mais comuns por modelo, região, quilometragem e período. Fabricantes, seguradoras e fornecedores de peças pagariam pela inteligência — não pela identidade do motorista.

Essa mesma arquitetura pode funcionar em:

- energia;
- agronegócio;
- logística;
- manutenção industrial;
- varejo;
- construção civil;
- mercado imobiliário;
- telecomunicações.

Na saúde, a oportunidade é maior, mas o campo regulatório é um corredor cheio de lasers. Seria necessário trabalhar com hospitais, pesquisadores, especialistas em privacidade, comitês de ética e assessoria jurídica especializada.

Em termos estratégicos: **dados brutos são minério; dados legalizados, organizados e atualizados são urânio enriquecido.**

*Esta é uma visão geral de mercado e regulação, não um parecer jurídico.*

Posso monitorar esse mercado e entregar um radar periódico de aquisições, contratos e novas empresas de monetização de dados.

[^1]: [england.nhs.uk](https://www.england.nhs.uk/digitaltechnology/nhs-federated-data-platform/fdp-faqs/?utm_source=chatgpt.com)

[^2]: [theguardian.com](https://www.theguardian.com/society/2026/jul/27/nhs-patients-records-us-private-equity-firm-optum-uk-tpg?utm_source=chatgpt.com)

[^3]: [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm)

[^4]: [hhs.gov](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html?utm_source=chatgpt.com)

[^5]: [ico.org.uk](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/introduction-to-anonymisation/?utm_source=chatgpt.com)

[^6]: [docs.aws.amazon.com](https://docs.aws.amazon.com/pt_br/data-exchange/latest/userguide/product-subscriptions.html?utm_source=chatgpt.com)

[^7]: [iqvia.com](https://www.iqvia.com/pt-br/solutions/real-world-evidence/real-world-data-and-insights?utm_source=chatgpt.com)

[^8]: [datavant.com](https://www.datavant.com/press-release/thermo-fisher-scientific-expands-real-world-data-interoperability-and-linkage-through-strategic-collaboration-with-datavant?utm_source=chatgpt.com)

[^9]: [dados.gov.br](https://dados.gov.br/?utm_source=chatgpt.com)