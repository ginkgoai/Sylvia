---
title: "Tutorial de Claude Code + AWS CLI | Criando infra de forma automática"
source: "https://www.youtube.com/watch?v=7SmqqalsLRY"
author:
  - "[[Fernanda Kipper | Dev]]"
published: 2026-07-20
created: 2026-07-21
description: "Nesse vídeo vamos aprender como utilizar o Claude Code em conjunto com a AWS CLI e o Terraform para automatizar o provisionamento de infraestrutura na nuvem. Na prática veremos como criar um fluxo de"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=7SmqqalsLRY)

Nesse vídeo vamos aprender como utilizar o Claude Code em conjunto com a AWS CLI e o Terraform para automatizar o provisionamento de infraestrutura na nuvem. Na prática veremos como criar um fluxo de trabalho (workflow) profissional que gera automaticamente um ambiente de preview completo (incluindo banco de dados RDS) para cada novo Pull Request aberto no GitHub.  
  
🧡 Portal de Carreiras Itaú  
https://carreiras.itau.com.br  
  
🔗 Portal de Cursos GRATUITOS + Curadoria  
https://fernandakipper.com/yt/descricao  
  
🔗 Nossa NEWSLETTER Gratuita de Tecnologia  
https://www.boratomarcafe.com  
  
⭐ Seja um membro do canal e tenha acesso às lives, vídeos e conteúdos exclusivos!  
https://www.youtube.com/channel/UCpKvMmsF6QrkVr\_zWaLGK-A/join  
  
👉 Me siga no Instagram!  
https://www.instagram.com/kipper.dev/  
  
  
00:00 - Intro  
01:08 - Entendendo e instalando a AWS CLI  
03:11 - Configurando a AWS CLI e permissões via IAM  
07:22 - Integrando o Claude Code com documentações via MCP (Context.py)  
09:30 - O que é Terraform (Infraestrutura como Código)  
11:11 - Exemplo prático de código Terraform para criar um bucket S3  
14:42 - Executando o Terraform: Comandos init, plan, apply e destroy  
20:01 - Projeto Prático: Criando um ambiente de preview para uma aplicação Next.js  
23:27 - Definindo a especificação (Spec) da pipeline de CI/CD  
28:00 - Usando o Claude Code para implementar a pipeline via GitHub Actions  
30:18 - Configurando o token do GitHub para integração com o AWS Amplify  
34:00 - Rodando o Terraform para provisionar o serviço AWS Amplify e RDS  
37:19 - Corrigindo problemas de permissões (IAM Roles) durante o deploy  
42:13 - Resultado final: Demonstração do ambiente de preview sendo criado automaticamente  
44:06 - Considerações finais e encerramento  
  
#aws #claudecode #tutorialaws #tutorialclaude

## Transcript

### Intro

**0:00** · Nesse tutorial vou te mostrar como é que você consegue utilizar o seu cloud code para provisionar serviços de infraestrutura de forma automática na sua AWS. E além disso, no final da aula, a gente vai construir também um próprio workflow, no caso uma pipeline de CD, utilizando o Cloud Code para provisionar ambientes pra nossa aplicação de forma automática e também seguindo boas práticas de maneira super profissional.

**0:24** · E a aula de hoje está sendo oferecida em parceria com o Itaú, que foi um lugar que eu trabalhei durante dois anos.

**0:29** · Tenho muito carinho pelo banco. E foi também o lugar onde eu mais aprendi sobre infraestrutura e também sobre os serviços da WS, porque eu utilizava muito no meu dia a dia. E é um prazer estar fornecendo essa aula hoje em parceria com o Itaú. Então agora, sem mais enrolações, bora começar.

**0:46** · Então vamos lá. Antes da gente criar o nosso workflow de provisionamento de ambientes de forma automática, a gente precisa entender duas dois conceitos aqui, na verdade, duas ferramentas que estão disponíveis pra gente, que vão ser as principais ferramentas que vão permitir que a gente crie esses workflows de maneira automática e utilizando o cloud code.

### Entendendo e instalando a AWS CLI

**1:08** · A primeira ferramenta é a WSCLI, que é a commandline interface da WS, pra gente conseguir gerenciar, né? e coordenar os serviços da WS através do nosso terminal, né, através da CLI. A CLI da WS permite que a gente interaja com diversos serviços da WS, que a gente configure a nossa conta, configure serviços, provisione, né, camadas de infraestrutura e por aí vai. E eles têm essa documentação aqui que é o doc.

**1:38** · /CLI/LATES, né? E aqui vai ter descrito certinho todos os serviços que estão disponíveis para serem gerenciados via Cali e também todos os comandos dentro de cada um desses serviços. Então, por exemplo, se eu procurar aqui pelo serviço do S3, né? Deixa eu dar uma scrollada aqui até chegar no S, ó, S3. A gente vai conseguir visualizar todos os comandos, né, que estão disponíveis para eu interagir com o S3 através da Seal e tudo que como que ele funciona e por aí vai.

**2:09** · Se a gente voltar lá pro índice, a gente vai ver que tem vários outros serviços, como Amazon, Bedrock, Amplify, MP, por aí vai, tá? Quase todos os serviços da WS estão aqui. E a primeira coisa que vocês precisam ter em mente é que vocês precisam ter o AWSCLI instalado na máquina de vocês, porque é através do AWSCLI que o nosso cloud Code vai conseguir interagir com a nossa conta da WS, tá? Porque o Cloud Code vai conseguir rodar comandos na nossa conta da WS utilizando o nosso WSCI.

**2:36** · Para fazer a instalação da WSCI é super simples, tá? É só procurar aqui, ó, WSCI install. Essa documentação vai tá aqui na descrição do vídeo também para facilitar, mas no macOS, por exemplo, que é o meu caso, a gente pode usar aqui os comandos direto que eles deixam disponíveis, né, através do Gin Staller e também do Command Line Staller, que é só fazer o o download aqui do installer da WS e instalar o package, certo? Não tem muito mistério.

**3:05** · E eles deixam aqui bem detalhadinho como instalar no Mac, no Windows e no Linux. Com a WSCI instalada na nossa máquina, a primeira coisa que a gente vai precisar fazer é a configuração da WSC, porque quando a gente instala C, tá só instalada a ferramenta, mas não tá conectado com a nossa conta. Para conectar com a nossa conta, a gente vai ter que fazer a WS configure, né? Na verdade, para ter certeza que tá instalado, a gente vai fazer a WS men version. E ele vai dizer para mim, ó, versão da WS AL que eu tenho instalado é a 2.34.38.

### Configurando a AWS CLI e permissões via IAM

**3:37** · E aí, se eu venho aqui e faço a WS configure, ele vai então me pedir o meu Access Key ID, que no meu caso já tá configurado na minha máquina, e vai me pedir o meu AWS Secret Access Key. Esses dois já estão configurados aqui na minha máquina porque eu já ã loguei na WS antes aqui, né, no meu terminal, porque eu já utilizo a ferramenta. No caso de vocês, vocês estão fornecendo esses dados pela primeira vez, então ele não vai vir nenhum dado pré-preenchido aqui. A mesma coisa pro default region, né?

**4:04** · O meu Default region tá East 2, porque os nossos serviços aqui da empresa estão rodando no US East 2. Então eu já deixo por padrão US East 2, porque todo o comando que eu for rodar na WS aqui pela minha Cai já vai rodar nessa região da WS, tá? Mas isso aqui vocês poderiam colocar tranquilamente East One ou colocar pra região de São Paulo, se é que a empresa de vocês utiliza, defult output format e etc. Vocês vão mudando aqui a medida que precisem. F. Onde é que eu encontro meu AWS Access ID? e o secret, né?

**4:36** · Então, tem duas formas que a gente pode fazer isso. Vocês podem utilizar o secretória conta de vocês, tá? O Access Ced e o secret da própria conta. E aí isso significa que tudo que vocês fizerem pela CLI vai ter o mesmo nível de permissão que a conta de vocês tem, né? Então, a conta que vocês logam aqui no AWS Console tem nível de permissão de leitura, de escrita para cada serviço, vai ser o mesmo ali pro terminal.

**5:01** · Ou vocês podem utilizar aqui o IAM, né, da WS, o serviço de de gerenciamento de perfis, gerenciamento de contas, e criar um novo usuário que vai ser só a WSCLI de vocês. Ó, no caso aqui eu criei, ó, WSCLI, que é o meu, tá vendo? Foi a última atividade 12 minutos atrás e aí eu gerei AWS Access Key ID e um AWS Secret somente para eu utilizar a minha Celai.

**5:28** · No meu caso, eu dei a permissão de de administrador, né? Porque eu sou, digamos assim, a a que mais tem poderes aqui na empresa para rodar as coisas na WS. Mas o correto seria dar somente as premissões que eu acho seguro eu ter via e também tendo em consideração, né?

**5:45** · Lembrando que se eu vou deixar o cloud utilizar minha WSI, tudo que tá disponível aqui o cloud vai poder fazer, né? Então, a gente pode adicionar ou remover permissões. Aí eu posso botar permissão só para mexer na minha lambdada, né? É que já a gente já tem um grupo aqui da lâmbda criado. Eu posso anexar as políticas diretamente, posso procurar aqui o serviço que eu quero ã somente da permissão e ir ã formatando isso aqui da maneira que eu preferi. E no final ele vai gerar para mim a chave de acesso, né, o Access e o Secret eu vou copiar e colar lá no meu terminal.

**6:17** · Beleza? Quando a WSI configurado, o que que eu vou conseguir fazer aqui pelo meu terminal? Eu consigo interagir com o serviço da WS. Então, por exemplo, eu vou interagir com o serviço do Amplify.

**6:25** · Eu vou chamar a WS Amplify List Apps, que é um comando que eu sei que existe porque eu uso bastante. Esse List apps vai listar todos os meus apps que tem dentro do serviço do Amplify. O Amplify é um serviço para hospedagem de front end, digamos assim, tá? E ele traz aqui para mim, ó, todos os serviços, né?

**6:45** · Hã, aqui em formato de lista, como o terminal tá minimizado, fica ruim de ler a lista, mas é uma lista com todos os meus serviços configurados lá no meu amplify. Eu posso também, por exemplo, rodar o comando AWS S3 help para ver o que que eu tenho disponível aqui para usar no S3. E ele vai me explicar um pouco, ó, no S3 eu posso fazer isso, serve para aquilo, etc. Ele vai me explicando cada um dos comandos.

**7:08** · Vocês vão vir lá na documentação do AWSE lá e vão descobrindo, né, o os comandos que vocês precisam e as coisas que servem para vocês. E claro, toda essa documentação, já que ela tá pública, já que ela existe, a gente também consegue fornecer pro nosso cloud, né? E lembrando aqui que a gente pode utilizar, deixa eu abrir meu cloud aqui, ó, a gente pode utilizar o MCP do Context 7. Deixa eu ver até se o meu tá configurado aqui nesse PC.

### Integrando o Claude Code com documentações via MCP (Context.py)

**7:37** · Acho que nem está nem está configurado o MCP do Context 7, mas a gente pode usar o MCP Context 7 para que o cloud tenha acesso atualizado a todas as documentações que estão listadas lá no artifact, né? E aqui lembrando que esse MCP é um MCP público da comunidade que existe pra gente acessar para pras LMS acessarem as documentações atualizadas. E se a gente der uma olhada aqui no context 7, era para tá aqui a documentação da WS. Tenho quase certeza que tá aqui, ó, a WS aline, tá vendo?

**8:08** · Então, se o cloud de vocês tá com o context 7 configurado, isso aqui e ele já vai dar acesso a à documentação da WS Al atualizada para ele. Eu vou inclusive a instalar o context Steva aqui nessa minha máquina que eu tinha na outra. \[música\] Essa aqui eu não tenho mais. Deixa eu sair aqui, tirar um ESC.

**8:29** · Ã, deixa eu dar um comandinho para instalar, né, o Context 7 setup. E aí, dessa maneira, o meu cloud já vai ter acesso atualizadas todas as documentações que estão listadas aqui no artifact do do context se, beleza? Então, com isso, a gente já tem a ferramenta necessária pro cloud interagir com a nossa WS, né?

**8:54** · Interagir com a nossa conta, mexer com serviços, etc. Agora, como é que o cloud pode fazer para provisionar serviços de infraestrutura, né? Porque tem alguns serviços aqui da WS que exigiam um pouco mais de configuração, não é simplesmente rodar um AWS Amplify create, né? Às vezes a gente tem que configurar variável de ambiente, a gente tem que configurar rede, né? Tem que configurar as portas, tem que configurar contêiner, tem que configurar VPC, um monte de coisa, né?

**9:20** · Então ão uma série de de configurações às vezes que a gente precisa fazer para criar uma infraestrutura realmente parruda, uma infraestrutura realmente profissional ali na WS. E aí que vem o segundo carinha que vocês precisam conhecer, que é o Terraform, tá? O que que é o Terraform? O Terraform é basicamente eu chamo de linguagem de infraestrutura, mas a verdade é que ele é uma ferramenta de infraestrutura, né? De infra code.

### O que é Terraform (Infraestrutura como Código)

**9:45** · Infraestrutura como código, né?

**9:48** · Inclusive tem vídeo de terraform já aqui no canal, vídeo de Infres Code, vai tá aparecendo aqui na tela. Então, o Terraform é uma linguagem, digamos assim, que permita que a gente define, defina, né, o formato da da nossa estrutura em formato de código, né? A gente vai transformar o que seria uma série de configurações lá na WS em código. E aí, dessa maneira, eu tenho uma infraestrutura replicável, porque isso tá salvo em um código, como se fosse um script que cria a infraestrutura para mim. E eu trouxe um exemplo aqui para mostrar para vocês como é que é um código terraform, tá?

**10:21** · Então, deixa eu abrir aqui minha ideia.

**10:24** · Olha só, um código terraform eh tem essa carinha aqui, tá? É um, é quase uma, parece uma linguagem de marcação, né?

**10:34** · Onde na verdade a gente tá só fazendo as especificações do serviço de infraestrutura ali que a gente tá provisionando, que a gente tá configurando, tá? Então, todo arquivo Terraform essa extensão. PTF, tá? E aí aqui ele vai me dizer para qual provider ele se aplica, porque de novo, Terraform para WS, né? Eu posso usar o Terraform para especificar infraestrutura em diversos cloud providers. Posso usar para pra Eure, para GCP também da Google, se eu não me engano, e para vários outros, tá?

**11:02** · O Terraform é uma ferramenta mais agnóstica, digamos assim. E eu posso usar Terraform, por exemplo, para serviços da EO. No meu caso aqui, eu tô usando para a WS, tá?

### Exemplo prático de código Terraform para criar um bucket S3

**11:15** · Aí aqui no próprio site do Terraform eles explicam como usar o provider de cada de cada cloud provider ali. Beleza?

**11:21** · Então tô usando para WS e eu tô colocando aqui que o required provider para rodar esse código Terraform é o Hashcorp/ws. Rashcorp é a empresa que tá pro T do Terraform. Aí eu vou especificar o provider, vou especificar a minha WS region na qual eu vou rodar aquilo. Então eu vou especificar qual resource. Resource é o recurso mesmo, né? o serviço de AW, o serviço de nuvem ali no qual estou manipulando, no qual estou criando, modificando, excluindo, etc.

**11:46** · E aqui eu estou criando simplesmente um AWSS3 bucket com o nome Hello Word, ã, que eu tô nomeando aqui de Hello Word, né? E mas o nome do bucket de fato vai ser ã importado lá da minha variável bucket name prefix e gerando um random ID aqui para cada um, para caso eu gere mais de um bucket, eles não tem um nome igual, né? A cada a cada execução vai gerando um ID ã randômico ali para cada para cada bucket. Esse var. Bucketname ele puxa aqui do meus verbales.

**12:17** · Isso aqui é tudo padrão do terraform, tá? Forma de escrever Terraform. Não, não desrespeito esse vídeo. E lembrando, todo esse código aqui a gente consegue escrever com o cloud code, tá? Então se você não domina Terraform, não conhece muito bem, não tem problema. Dá uma olhada na documentação, saiba o básico e aí vai instruindo o cloud para ele escrever o código Terraform para você, tá?

**12:39** · Inclusive esse código aqui de exemplo vai tá na descrição aqui do vídeo.

**12:43** · Então, com o nosso código Terraform criado, eu vou estar especificando exatamente qual infraestrutura eu quero criar. Nesse exemplo aqui que eu tô mostrando para vocês, é somente um bucket do S3, tá? Um bucket público com o nome BTC Terraform Hello World. Por que BTC? É bora tomar café, tá? Então, bora tomar café. Terraform Hello World.

**13:02** · Eu posso inclusive trocar esse nome para ser BTC Terraform S3 test, por exemplo.

**13:08** · E aí, o que que vai acontecer? Como é que eu posso executar isso aqui? Eu vou primeiro mostrar para vocês como vocês executariam manualmente, né, no terminal. Só que lembrando que tudo que a gente consegue fazer no terminal, o cloud consegue fazer pra gente, tá?

**13:21** · Então, eu até trouxe um readmzinho aqui para nos guiar. Então, a primeira coisa que a gente pode fazer que ele tá instalando o context 7. Vou deixar em outra \[música\] em outro terminal aqui. Deixa eu dar um command mais e beleza. Comand T para criar uma nova abinha no terminal. E vamos começar, tá? Primeira coisa que a gente precisa ter instalado na nossa máquina para poder rodar o código Terraform é o Terraform. No caso do meu computador aqui, como é um Mac, eu utilizo o BRW, né, como meu instalador. E a gente vai ter que fazer o BRW tap ã HCP tap, né?

**13:56** · BRW tap HCP/ Tab para trazer ali o os packets do Hashcorp. Hashcorp de novo é a empresa que tá por trás do Terraform.

**14:05** · Então eu vou ter que fazer brew install HCORP Tap/terraform.

**14:09** · No meu caso, eu já tenho o Terraform instalado, então já posso fazer aqui, ó, Terraform.

**14:14** · Para quem tem Mac, tá? Tomem muito cuidado para não rodar aquele comando brew install terraform, porque o HCorp tirou o o pacote Terraform do do Brewill Core ali, né? E eles ã disponibilizaram agora tudo via dentro do do módulo Hashcorp deles, tá? Então tem que instalar assim, primeiro fazendo o Tap no Terreform, no Hashcorp, depois puxando o Terraform. E aí ele já trouxe a minha versão do Terraform. Eu tô na versão 1.15.7 e o que que eu vou fazer, tá?

### Executando o Terraform: Comandos init, plan, apply e destroy

**14:42** · Eu tenho primeiro que estar dentro da pasta na qual o arquivo main.tf, né, o meu arquivo main. Form existe. Então eu vou ter que entrar dentro dessa pasta que é a minha pasta infra example.

**14:54** · Entrei dentro de infra example. Vou fazer um ls aqui para mostrar para vocês que eu tenho o meu arquivo main.tf, outputs.tf e variables. Aí agora eu vou rodar o seguinte comandinho. Primeiro eu vou rodar Terraform init. Esse Terraformit vai instalar todos os providers e as bibliotecas, digamos assim, do Terraform que eu tô usando.

**15:15** · Não é bem biblioteca, é provider mesmo o nome. No caso, é ali o meu, os plugins, né, que eu tô usando, que são os plugins da WS. Então, pr para eu conseguir utilizar o Terraform para cada serviço tem um plugin diferente de Terraform. No caso da WS, vai ter o plugin da WS e o plugin do S3, \[música\] né, para eu poder mexer ali com esse recurso. Então, depois que eu faço isso, vocês vão ver até que alguns arquivos foram criados aqui. Foi criado o meu terraform.lck e essa pasta aqui, ó, Terraform/provarders e tal, que é como se fosse meu meu Node Modules, tá?

**15:46** · do Terraform aqui, que é onde tem o o source code do dos plugins que eu tô usando. Depois disso, a gente vai fazer aqui o Terraform Plan, que ele esse Terraform Plan é o comando que nos mostra o que que vai ser aplicado caso eu rode esse Terraform. Ele me mostra exatamente o que seria criado, né?

**16:06** · \[música\] E lembrando que tudo isso daqui, toda essa execução do Terraform, vai usar a minha conta da WS que tá configurada no meu WS AL por padrão. Se eu quiser modificar e rodar numa outra conta da WS, eu teria que especificar isso no meu código Terraform. No caso aqui eu tô usando o padrão e aí por padrão ele vai rodar na conta da WS configurada na minha \[música\] Cali. Então ele me mostra aqui, ó, se eu rodar esse terraform, ó, tá vendo? Esse Terraform vai performar a seguinte operação, ó, a seguinte ação.

**16:34** · Ele vai eh criar um novo recurso chamado de AWS3 Bucket, né, que esse é o nome do serviço. Ã, e ele vai criar o accelerator status bucket RN, né, né, né, vai botar um nome, vai usar um random ID como sufix para para preencher o nome, etc. Ele me mostra que tudo que vai ser feito, né? E aí se eu rodo aí, deixa eu até mostrar para vocês, ó.

**16:55** · Se eu abro lá minha WS agora nos meus serviços do S3, aqui vocês vão ver que não tem nenhum bucket com aquele nome que a gente estabeleceu de BT BTC Terraform test S3. Depois que eu rodar aqui o Terraform apply, tá vendo?

**17:14** · Terraform apply, ele vai aplicar aquele script Terraform. Então isso vai provisionar a infraestrutura para mim. Então eu tenho que digetar aqui y que eu confirmo a criação e ele vai fazer isso para mim.

**17:26** · Então vamos esperar rodar. Ele tá fazendo creating aqui. Perfeito, criado.

**17:31** · Deixa eu dar um reload e perfeito. Ó, terraform btc terraform s3 teste. E aí um random ID. Se eu rodar de novo, ele era para criar de novo, né? Vai rodar.

**17:43** · Criou um novo random ID como sufix.

**17:48** · Beleza. Vamos ver.

**17:52** · Ele não criou um novo porque no caso, né, ele mantém um estado ali, tinha me esquecido disso, ele manteve um status, ó, que o Terraform foi comparado com a minha infraestrutura real e não foi achado diferenças, então ele não aplicou nenhuma mudança, tá? Terraform também mantém esse estado, tinha me esquecido disso de explicar para vocês, que fica aqui nesse terraform state, né, que ele mostra ali o estado, a última vez que aquilo ali foi aplicado, ele compara com a infraestrutura real lá na WS, vê que não tem nenhuma diferença, então não tem nenhuma mudança para ser aplicada. É

**18:23** · literalmente a mesma coisa que migrations no banco de dados, né? Quando a gente cria uma nova migration, a migration executa, altera o esquema do banco de dados. Se o esquema tá em dia com as migrations, se todas as migrations já for aplicadas, não tem nada para ser modificado. É como se fosse isso. E toda vez que eu altero meu terraform, daí isso vai causar uma nova mudança lá na minha na minha infraestrutura. E se eu quiser fazer o drop dessa infraestrutura, derrubar isso que eu criei, né, desprovisionar, digamos assim, eu posso fazer terraform destroy, que ele vai destruir essa infraestrutura ou essas modificações que foram realizadas, tá?

**18:55** · E aí ele vai me pedir aqui a confirmação se eu realmente quero destruir. Ó, ele tá explicando, ó.

**19:01** · Vou destruir isso, vou destruir isso.

**19:03** · Tudo que vai ser destruído, eu vou botar aqui. Yes. F. Isso aqui vai destruir todos os meus S3, não vai destruir só o que ele criou. Lembrando que ele mantém esse estado aqui para ã manter o track do que que foi feito. E agora meu TF state tá vazio. Tá vendo? Antes tava cheio, agora tá vazio, porque aquela essa infraestrutura não tá mais aplicada, não tem mais nada para eu manter de estado contra ela. Se eu vier aqui dar um reload, esse BTC Terraform era para sumir. Então vou dar um reload, sumiu, foi destruído, tá? Então por que que eu quis passar por isso? Porque isso aqui é importante vocês entenderem, tá?

**19:34** · Esses dois conceitos do Terraform, do WSI, para vocês verem que já é possível a gente provisionar a infraestrutura através de código, né? E também usando o nosso terminal. Agora, com essas duas ferramentas em mãos, a gente vai de fato botar o cloud para provisionar a infraestrutura de forma automática pra gente e para criar os nossos workflows.

**19:52** · Então agora vamos pra segunda etapa, que é a etapa prática, onde a gente vai criar um workflow próprio usando o cloud code.

### Projeto Prático: Criando um ambiente de preview para uma aplicação Next.js

**20:01** · Então vamos lá. A aplicação que a gente vai usar como exemplo aqui para esse vídeo é a nossa aplicação da newsletter aqui do canal que é a newsletter do Bora tomar café. Essa aplicação é uma aplicação NextJS, tá? Então é um uma aplicação aqui frontend que consome ali o back end para enviar as as newsletters semanais pros usuários e etc.

**20:20** · O que a gente vai tá fazendo aqui é o seguinte, a gente vai replicar aquele funcionamento que os projetos da Versel já t, que é sempre quando uma nova PR é aberta, né, um novo P request aberto paraa branchmin, é criado um ambiente de preview, né, no qual é feito o deploy dessa aplicação no ambiente preview para que o usuário ali, o desenvolvedor consiga testar ou até o próprio team, tá? Só que a gente vai replicar esse mesmo funcionamento só que usando os serviços da WS.

**20:50** · Por que que a gente vai fazer isso, tá? Porque esse tipo de de de cenário, né, de case é muito comum para empresas do porte do Itaú, por exemplo, né? Então, lá no Itaú não tem como a gente ã não testar o as alterações em um ambiente pré-produção, né? Não tem como eu só testar local e aí depois enviar pra produção. São aplicações muito críticas, né? Então é importante a gente entender como é que a gente pode criar essas cópias do ambiente de produção para utilizar pros nossos testes.

**21:20** · No nosso caso, é só uma aplicação frontend simples de exemplo, mas eu quero que você sempre tentem imaginar sendo aplicado, né, para grandes empresas ou para cenários mais críticos, porque é de fato onde esse tipo de conhecimento e esse tipo de infraestrutura faz diferença, né? Aqui no nosso caso do Bora tomar café não faz tanta diferença. Uma newsletter pequena, tem poucos usuários. Eu até poderia só testar local e depois já mandar pra produção, mas a gente tem que fazer o exercício de imaginação, de imaginar em cenários críticos, como o caso do Itaú.

**21:52** · E é por isso que é relevante vocês terem esse tipo de conhecimento, porque quando vocês passarem por um cenário desse na empresa de vocês, no local onde vocês trabalham, vocês já vão saber aplicar, já vão saber resolver. E aí, claro, né, de novo, porque que eu não usaria Versel, porque esse tipo de de aplicação tá rodando em infraestruturas mais robustas, né?

**22:07** · Então, um servidor ali do Itaú, um frontend, mesmo que seja, provavelmente tá rodando numa num serviço da WS, porque aí você tem mais controle, tem mais acesso aos logs, ã, até apresenta mais segurança porque consegue colocar nas regiões aqui de São Paulo, né, eh, reduz a latência, etc.

**22:28** · Então, acaba tendo muito mais controle em cima da da infraestrutura e por isso acabam optando por seguir com esses serviços de de cloud providers. Então o que a gente vai fazer é toda vez que uma nova PR for aberta, essa PR tem que disparar o deploy de um novo ambiente lá no nosso AWS Amplify. Então a gente vai est usando esse serviço aqui da WS, que é o AWS Amplify para fazer o deploy da nossa aplicação, né? AWSF ele já é bem conhecido para fazer o web hosting.

**22:55** · E aí cada novo cada novo deploy vai ter uma URL personalizada para acessar aquele ambiente. Então o essa URL vai ser comentada na PR, né? Então ali na PR o botezinho vai fazer um comentário com a URL pro usuário conseguir testar a aplicação dele no ambiente que foi provisionado só para aquilo. E aí dessa maneira o usuário consegue identificar problemas e e bugs, né, antes daquilo ir pra produção. Então vamos lá.

**23:26** · Eu já criei aqui pra gente começar uma documentaçãozinha, né, usando o superpers, a skill do superpers. Criei aqui uma spec pra gente, que é spec de como é que a gente vai fazer essa pipeline. Então, como é que ela vai funcionar? Quando o usuário abrir uma nova PR, vai ser gerado, vai ser trigado um deploy no Amplify e também vai ser trigada uma GitHub action. A GitHub action aqui vai ser a nossa pipeline CD.

### Definindo a especificação (Spec) da pipeline de CI/CD

**23:55** · O próprio Amplify, que é o serviço da WS, ele já identifica modificações automáticas no no GitHub, já tem essa integração automática, mas mesmo assim eu vou criar uma action do GitHub para que essa action ela consiga provisionar uma nova ã cópia do banco de dados para mim também é um um banco de dados que eu vou criar específico para esse ambiente para conseguir separar as coisas também porque caso essa aplicação esteja

**24:20** · rodando alguma migration no banco de dados ou caso vai ter que encher encher com um monte de dado de teste, eu não fique tendo o meu banco de dados, por exemplo, de homologação sendo poluído.

**24:31** · Eu consigo criar um ambiente ã novo para cada PR ali. E eu vou fazer isso provisionando um uma nova instância no AWS RDS, né? O RDS é o serviço da WS para hospedagem de bancos. a gente vai criar ali um banco postis, vai gerar então uma nova connection string específica para aquilo, ã, específica para aquele banco, né? Porque vai ter um novo host, uma nova senha. E aí, antes de eu disponibilizar a aplicação, eu vou rodar também um DBID, né?

**25:01** · Eu vou rodar um um naquele banco de dados para já popular o banco com algumas informações, pro banco não vir zerado, né? meu banco não vir resetado. E aí então depois eu vou lá, atualizo o as credenciais no meu AWS Amplify, faço o comentário na PR com a URL de preview e aí quando a PR for fechada, né, quando o usuário fizer o merge da PR ou cancelar ela por algum motivo, o GitHubs vai ser acionado para fazer o tiar down, né, excluindo aquela aquele banco de

**25:34** · dados que foi criado só para aquela branch, né, para não ficar com um monte de infraixo, porque depois iso que pode ser custo. Então, a medida que eu provisiono para cada ambiente, eu também tenho que matar quando eu não tiver mais usando, né? Então, quando a PR for fechada, eu excluo o banco de dados que eu criei só para aquilo e excluo também a branch lá no AWS Amplify, tá? E tudo isso a gente vai provisionar com Terraform. Eu não vou vir aqui na WS e configurar tudo na mão, eu não vou vir aqui e fazer as configurações. Quem vai fazer para mim vai ser o Cloud e a gente só vai testar se tá funcionando, tá?

**26:06** · Então, com a minha spec bem definida, a gente consegue delegar isso aqui pro cloud. Para quem não entendeu como vai ser, eu fiz até um desenhozinho aqui no paper, só para resumir. Então, o que que vai acontecer aqui? Eu botei o exemplo de agente de A, mas pode ser um dev também, né? Então, toda vez que um dev ou um agente de a, o próprio cloud, fizer um push para pro meu repositório remoto e abrir uma nova branch e abrir uma nova PR, essa PR vai trigar o meu amplify hosting, que vai fazer o build e o deploy de uma nova instância da minha aplicação, tá?

**26:35** · E também vai trigar a execução de uma GitHub actions, de uma action lá no GitHub, que vai então criar um novo banco de dados usando a WSRDS, provisionar um novo e vai ser uma instância micro, tá? que não tem custo, que fica ali no free tier, vai fazer um seed nesse banco de dados para já popular com algumas informações. Então, vai esperar o build da Amplify terminar e e vai até rodar alguns testes com Playwrite, né? O Playwrite ali é uma ferramenta de testes ã de integração.

**27:02** · E então vai fazer o comentário na PR com o link do ambiente de preview, tá? Tudo isso aqui vai ser feito por uma GitHub action.

**27:13** · E aí no final eu vou ter uma deployed preview com uma ORL nesse formatinho aqui que é o próprio Amplify Serviço da WS já fornece ã essa esse esses domínios pra gente, tá? E aí quando a PR for fechada, quando ela for encerrada, eu vou ter um tear down ali que vai derrubar toda essa infra que foi criada, tá? É mais ou menos isso aqui que vai que vai acontecer. E agora a gente vai delegar pro cloud code, criar as coisas pra gente, tá? E até uma coisa importante aqui, um comentário legal, tá?

**27:44** · Por que que eu resolvi utilizar GitHubs e não usei um Jenkins ou algo assim? Eu acho que o GitHubs ele oferece boas ferramentas, tá? Ele permite a gente fazer um monte de coisa e de forma super simplificada, sem eu ficar, sem eu precisar ficar subindo um novo contêiner, uma nova instância, só para rodar um Jenkins, tá? Então, continuando, o que nós vamos fazer agora é pedir pro cloud implementar essa nossa spec que define exatamente como que vai ser o fluxo aqui, o nosso workflow para gerar um ambiente novo para cada deploy.

### Usando o Claude Code para implementar a pipeline via GitHub Actions

**28:13** · Então vou abrir aqui um novo terminal, eu vou voltar pra pasta root aqui, né, da minha aplicação que é o newsletter bora tomar café. Vou acionar o cloud e vou pedir para ele start the implementation implementation of the spec. Eu vou copiar aqui o nome da spec.

**28:34** · Copy relative path. Perfeito. Vou colar aqui.

**28:40** · Andegate to sub agents the tasks that can be parallel, né? Para ele delegar para suagentes as tarefas que podem ser paralelizadas. Como já tá tudo definido na spec, eu já tomei todas as decisões antes, agora é só eu ir revisando o que o cloud for fazendo e, claro, testando a medida que ele ã vá terminando cada etapa, né?

**29:05** · Mas o mais importante aqui de fato é a gente tomar essa decisão inicial de como que vai ser a arquitetura, como que vai funcionar esse workflow. Então, depois disso é deixar o cloud agir, né? deixa ele escrever os terraformas pra gente, sempre revisando, claro, mas o mais importante, as decisões já foram tomadas antes. E aí, enquanto isso, é só a gente esperar. A primeira coisa aqui que o meu agente vai fazer, provavelmente, vai ser quebrar essa spec em um plano de implementação e algumas tesques, né? Até porque esse é o padrão do superpers.

**29:34** · O Superpers é uma um conjunto de skills bem comum aqui do cloud que organiza bastante essa parte de escrever spec, de fazer brainstorming e de escrever os planos. Então, no padrão do superpers é isso, né? A gente começa fazendo a spec que eu já tinha feito. Depois a gente vai pra parte de plano, que é de fato o plano de implementação baseado na spec. Aí a gente quebra mais em tarefas e exatamente onde a gente vai modificar. E aí, por fim, a gente passa pra parte da implementação. E aí eu vou esperar que o agente agir.

**30:03** · Se surgir alguma coisa nesse meio tempo, alguma, algum tópico importante que é relevante eu mostrar para vocês, eu mostro. Senão eu vou voltar já com a pipeline pronta e a gente vai revisar só o terraform gerado e o resultado final do nosso workflow.

### Configurando o token do GitHub para integração com o AWS Amplify

**30:18** · Pronto. Ã, o cloud aqui terminou de executar, ele levou um tempão, tá? Ele foi fazendo algumas perguntas no meio da execução, algumas perguntas sobre como ele deveria implementar e etc. Apesar disso já estar bem especificado na spec, eu fui só guiando ele, mas demorou muito. Demorou tipo uns 20 minutos aqui a sessão, mas eu também tava no high effort, então normal ele levar mais tempo.

**30:40** · E agora ele chegou no final da implementação e ele tá me pedindo para gerar um token do GitHub, certo? porque ele vai precisar desse token do GitHub para configurar lá no Amplify, né, para fazer com que o Amplify consiga monitorar as atualizações, os pushes, etc., pro nosso repo. O Amplify, lembrando que é o serviço da WS que nós estamos utilizando para fazer o hosting da nossa aplicação web. Então, ele tá me pedindo esse token do GitHub para ele colocar lá nas variáveis de ambiente do meu Amplify, pro Amplify conseguir ficar fazendo esse esse monitoramento, tá?

**31:13** · Então, o que eu vou fazer é seguir só o passo a passo que ele me botou aqui. Vou entrar no meu gitubar um novo token aqui para ele, certo?

**31:22** · Então, generate new token, um token classic, que foi o que ele me pediu ali, ó. Se a gente perceber, ele pediu um token classic.

**31:30** · Vou colocar aqui minha senha, né? fazer o login.

**31:37** · Pronto. Eu vou chamar esse token de amplify.

**31:41** · Eh, amplify, só o WS Amplify.

**31:51** · Aqui eu vou colocar a inspiração de no expiration, né? A ideia é que não espire, vai ficar rodando lá ã no meu amplify. Aí qualquer coisa eu só faço o revoke do token, caso eu precise.

**32:03** · E aqui eu vou selecionar os as premissões somente que ele precisa.

**32:08** · Eu preciso do escopo de repo, certo?

**32:10** · Então vou vir aqui escopo de repo, vou marcar todos eles. Os demais escopos eu não preciso marcar porque ele nem vai utilizar, certo? Então, escopo de recupo, generate token. Vou copiar o meu token aqui. Se você tá assistindo esse vídeo, claramente eu já excluí esse token depois, então fiquem tranquilos, o token não vazou. Ã, aí eu vou botar aqui, ó, já gerei o token. Gere e copio o token. Beleza, já gerei o token. Vou esperar ele rodar agora o Terraform Apply, onde ele vai criar o meu serviço lá na WS, né? vai criar o meu amplify.

**32:40** · E aí eu mesma manualmente já vou ã colar aqui para ele o token, né? Então aqui token, só para ele conseguir rodar o apply lá na WS, certo? porque ele vai pegar esse token e vai criar uma variável de ambiente lá com esse valor.

**32:58** · O ideal aqui, na verdade, na verdade mesmo, é que a gente pegasse esse token, nós mesmos, fôssemos lá na WS depois que ele rodasse o apply e cadastrássemos a variável de ambiente nós mesmos, né?

**33:09** · Para evitar colar token aqui no chat com a gente, evitar colar pro cloud, porque mesmo eles dizendo que não usam os as sessões para treinamento, que isso que não fica salvo depois, é mais seguro, né? Já que é um token que vai dar acesso aos nossos repositórios, é mais seguro somente nós termos acesso ali. A gente faz a configuração manual e tá tudo certo. Mas aqui a título de simplicidade, até para facilitar, eu pedi para ele já botar os tokens mesmo no Terraform, rodar o Terraform apply e depois eu só excluo esse terraform aqui, não deixo o token salvo lá, tá? Não tem problema nenhum, é só eu excluir isso aqui depois.

**33:40** · Ah, mas de novo, se fosse realmente um token produtivo, se fosse uma aplicação crítica, eu prefiro que vocês apliquem o Terraform, deixem a variável de ambiente lá pendente e vocês mesmos vão lá e preenchem ela na no console da WS, tá? Então vamos esperar aqui ele finalizar o a execução. Ele já rodou o Terraform plan. Tá aqui o output.

### Rodando o Terraform para provisionar o serviço AWS Amplify e RDS

**34:02** · Beleza, o approach foi bloqueado porque tá com crential exposure, né, que foi exatamente isso que eu falei. Não era pra gente estar passando token direto por aqui, mas ele vai tentar um approach mais seguro aqui, ã, ignorando alguns alguns pré-requisitos de segurança. Vamos esperar ele terminar de executar. Então, pronto, ele terminou de rodar aqui o plan do Terraform, né, e ele me trouxe um resumo das alterações que vão ser aplicadas.

**34:29** · Eu já li aqui, já revisei e ele trouxe também um resuminho para mim de do que que de fato vai ser criado na WS e o custo disso, né? Ele tá me avisando que isso aqui de fato é um billable, né? É algo cobrável lá da WS que a gente vai est usando aqui uma estância de TG4 micro do RDS que apesar de ser uma super pequena, super barata, se eu não tiver créditos ali da WS vai consumir um pouquinho, né? É um valor pequeno, mas tem que ter isso em mente também. o valor da do amplify que é used based, né?

**35:00** · Porque é um serviço mais serveless ali da WS. E aí o tempo de provcionamento vai demorar entre 5 a 10 minutos para ele terminar, porque criação do RDS demora um pouco mais.

**35:10** · Então sim, aplicar agora. E aí de novo, vou esperar ele terminar de aplicar. E agora eu só vou voltar quando já tiver tudo aplicado e a nossa pipeline já rodando em produção. Lembrando que essa aula que você tá assistindo agora foi desenvolvida em parceria com o Itaú, que é o local que eu trabalhei durante dois anos, aprendi muitos conceitos de infraestrutura e de AWS por lá. Foi um grande desenvolvimento de carreira para mim.

**35:34** · E se você também quer ter oportunidade de trabalhar no maior banco da América Latina com tecnologias de ponta como a WS e várias outras, o link pro Banco de Talentos do Itaú tá aqui na descrição desse vídeo e fixado nos nossos comentários também. Se inscreve lá, manda seu currículo e fica de olho nas oportunidades, porque eu tenho certeza que vai ser um ótimo lugar para você se desenvolver como profissional e aprender demais. E agora vamos continuar no nosso tutorial.

**35:59** · Bom, galera, e depois que o cloud finalizou aqui a execução, a última coisa que eu tive que fazer foi configurar as variáveis que vão ser usada pela minha GitHubs aqui dentro do GitHub, né? Então eu tive que vir no meu repositório em settings, vir aqui em actions e cadastrar todas as variáveis de ambiente que a Action vai utilizar e também a secreta vai utilizar para estabelecer ali a conexão, né, a sessão.

**36:26** · E essas variáveis de ambiente são basicamente o AWS region, o RDSDB user, o DB host, o DB secret, que na verdade tudo isso aqui eu poderia cadastrar como uma secret mesmo, né? Porque quando eu cadastro como verbal, o valor fica exposto. Quando eu cadastro como secreto.

**36:44** · Aqui eu não consigo consultar, eu só consigo alterar esse valor. Então, o correto mesmo seria ter cadastrado tudo isso aqui como secret, porque é melhor, né? Melhor ter mais ã segurança. E aí com essas variáveis configuradas, aquela aquele token do GitHub que eu tinha criado, eu já posso excluir, né? Já posso revogar ele, porque o cloud já usou ali para executar a o temaform na WS, já configurou o meu Amplify. O Amplify já tá configurado, já tá conectado com o meu repositório aqui do GitHub. Então ele não precisa mais daquele token funcionando.

**37:15** · Então eu já poderia revogar aquele token lá também.

### Corrigindo problemas de permissões (IAM Roles) durante o deploy

**37:19** · Galera, antes de eu mostrar aqui o resultado, aconteceu uma um outro problema quando eu estava implementando aqui o nosso a geração dos ambientes de forma automática. eu resolvi gravar pra gente já corrigir aqui no vídeo também.

**37:33** · Então, o que que começou a acontecer? Eu fui criar aqui uma perre de teste, né, para ver se se ele iria executar os testes corretamente nessa perra e se ele iria criar o ambiente. Os testes executaram perfeitamente aqui com a GitHub action, né, rodaram certinho e ele fez o comentário com o covered report.

**37:52** · E lembrando que toda essa action aqui foi trigada através desse arquivo que nós criamos, que é o arquivo de, deixa eu encontrar aqui, ó, pgithub/worflows, né, que tá dentro dessa pasta. E aqui o arquivo de c.

**38:10** · IML, né, que aqui é o nosso Yamel, contendo todo o detalhamento da execução dessa dessa action. Aí as variáveis de ambiente, o agente colocou aqui umas variáveis fakes, tá? E aí as variáveis de ambiente, o agente colocou aqui umas variáveis fakes, tá? Porque são variáveis de ambiente que ele vai injetar ali no na aplicação para quando ele fosse executar os testes. Então tá OK manter essas variáveis aqui porque são variáveis de teste mesmo, não tem problema.

**38:40** · Agora, se fossem variáveis de um ambiente eh deploiado de fato, né, mesmo que fosse um ambiente de testes nosso, mas se realmente fosse um banco de dados real, alguma coisa assim, a o ideal seria colocar essas variáveis de ambiente aqui em secrets nossas actions e não deixá-las expostas aqui direto no email. Mas aqui é como que vai ser usado só pro teste unitário, não tem problema algum, tá? só para ele não dar eu quando ele faz o build e a inicialização ali da aplicação. Então essa parte dos testes tá funcionando, ele tá executando os testes e tá comentando aqui pra gente o coverage report.

**39:14** · Só que a parte de integração com a WS não tá funcionando aí. Então se eu entro aqui no meu painel da WS, eu consigo ver que aqui na no meu amplify tá falhando, né, o deploy de todo de todo novo de todo o novo ambiente, né? Ele tá dando erro, não tá conseguindo fazer o deploy. Aqui, por exemplo, ó, do meu update home text. Tá vendo? Ele criou um ambiente específico para aquela minha branchi, que é a branch de update home text.

**39:43** · Isso aqui tá funcionando corretamente, mas o deploy está falhando. Ele não tá conseguindo criar um ambiente exclusivo para essa branch aqui. Por que que esse deploy tá falhando? Tá, o deploy tá falhando. Eu até tava investigando aqui com o cloud porque a gente não deu a Roll, né, IAM RLE específica pro nosso amplifier para ele conseguir se conectar com os meus outros serviços aqui da ã da WS, inclusive o RDS, né?

**40:15** · Então, quando eu faço deploy aqui desse meu ambiente do amplify, ele é uma aplicação Next que tem uma Next API ali por trás que tá utilizando o Prisma e o Prisma precisa se conectar com o banco de dados. Esse meu banco de dados tá rodando no RDS, né? Todo banco de teste aqui, não é o de produção. Beleza? Só que o meu amplify não tem a role necessária para se conectar com o RDS, né?

**40:40** · Na WS tudo é escopado por permissão, mesmo que seja na mesma conta, para que um serviço consiga acessar outro serviço, eles têm que ter aí a MRO correta, que dá essa permissão, né, que seria o privilégio ali. E isso não tá acontecendo. E aí tá falhando o build, né?

**40:59** · Ele tá dizendo, ó, accessite, o user aqui a WS, STS, assumid RLE, né, não tem, né, permissão para ã mexer no Secrets Manager, que é para cadastrar as Secrets, né, as variáveis de ambiente e também não tem permissão para se conectar com o nosso RDS, tá? Então eu preciso fazer essa atualização, essa correção, eh, pra gente dar a RLE necessária pro meu serviço do Amplify, a gente pode fazer via a Terraform também.

**41:29** · Mas a gente vai ter que criar aqui um novo script do Terraform para dar a permissão necessária para esse meu serviço do do Amplify, tá? Então eu vou dizer aqui pro cloud que ele pode continuar. Então pode continuar a correção para dar as roles necessárias para o amplify.

**41:50** · E aí a gente vai ter que rodar o Terraform apply novamente, né? Porque vão ter novas modificações ali de infraestrutura que a gente vai ter que fazer. e o nosso arquivo de de terraform vai ser alterado, né? Então é como se a gente tivesse fazendo uma uma modificação nessa nossa infraestrutura.

**42:08** · Então vamos aguardar aqui o cloud terminar. Vou esperar ele fazer alteração e aí eu volto quando a gente for fazer o apply. E agora as as implantações já estão acontecendo com sucesso, né? E sempre quando eu faço um novo push pra minha branch, né? sempre quando eu faço um novo commit, ele já tga a execução do deploy do ambiente separado para essa branch. Ó, percebam que aqui eu tenho mais de um ambiente.

### Resultado final: Demonstração do ambiente de preview sendo criado automaticamente

**42:32** · Eu tenho o ambiente da minha main, que ainda tá com falha porque eu ainda não mergiei essas alterações da correção, e o ambiente específico pra minha branch da Update Home Text. E aí já tá rodando aqui inclusive nos nas actions do GitHub o preview do End to end, né, do test end to end, que aí pega ali a nossa URL do amplify e então realiza também um teste do Playwrght em cima dessa URL, certo? Os testes do Playwright não estão funcionando, né?

**43:00** · Porque eu não parei ainda para configurar essa parte, mas já mostrando para vocês que é possível também, né? A gente pode ter uma action, ó, ela falhou aqui, mas a gente pode ter uma action que vai esperar esse deploy finalizar, vai fazer o comentário da preview RL aqui na nossa na nossa PR e vai também rodar os testes usando o playr ali em cima daquele ambiente que a gente acabou de deploiar, certo? Tudo integrado aqui, tudo de forma automática, sendo trigado pelos pushs do agente. Então, já tá tudo funcionando aqui no nosso repositório.

**43:31** · E o resultado final do nosso repositório, que gera um ambiente novo para cada PR aberta, tá aparecendo agora aqui na tela. Bonitinho, né? Eu fiz um vídeo bonitinho para demonstrar para vocês.

**43:44** · Vocês conseguem ver que eu abro a pro request, a action começa a executar, ele provisiona o ambiente no amplifire para mim e depois faz o comentário ali com o link do ambiente para eu entrar então ã ali no no ambiente provisionado, né, fazer os meus próprios testes. Ele também acaba executando \[música\] os testes end to end ali com o playgrid.

**44:04** · Beleza? Então, tá tudo prontinho.

### Considerações finais e encerramento

**44:06** · Relembrando, tá, que todos os materiais que eu usei aqui de terraform, de promptes, etc., vão tá aqui na descrição do vídeo para para quem quiser usar como base para construir seu próprio workflow e aí vai poder derivar ali pro teu caso de uso específico, né? Ah, preciso mexer com S2, preciso mexer com S3.

**44:23** · Aí é só ir mudando o que tu vai pedir pro cloud code e também o Terraform que vai ser gerado no final. \[música\] \[música\] \[música\]