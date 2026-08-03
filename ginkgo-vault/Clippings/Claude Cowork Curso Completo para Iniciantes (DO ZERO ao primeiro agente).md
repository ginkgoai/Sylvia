---
title: "Claude Cowork: Curso Completo para Iniciantes (DO ZERO ao primeiro agente)"
source: "https://www.youtube.com/watch?v=pyb3G0z1m7c"
author:
  - "[[Rodrigo do Carmo]]"
published: 2026-06-02
created: 2026-07-17
description: "Aprenda a usar o Claude Cowork do zero ao avançado neste tutorial completo. Você vai entender o que é, como instalar, como funciona e como criar agentes, skills, plugins e conexões (MCPs) para colocar"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=pyb3G0z1m7c)

Aprenda a usar o Claude Cowork do zero ao avançado neste tutorial completo. Você vai entender o que é, como instalar, como funciona e como criar agentes, skills, plugins e conexões (MCPs) para colocar a IA da Anthropic para trabalhar por você, mesmo sem saber programar.  
  
➡️ Formulário da comunidade, responda 3 perguntas rápidas:  
https://forms.gle/BPAvnrVDaCL3zSEw7  
  
🔴 Vote em mim no iBest:  
https://premioibest.vote/610463084  
  
✅ INSCREVA-SE NO CANAL!  
https://www.youtube.com/@rodrigo-do-carmo?sub\_confirmation=1  
  
📩Assine a minha newsletter semanal:  
https://news.iastack.com  
  
✅ SIGA MINHAS REDES SOCIAIS!  
https://rodrigodocarmo.com/links  
  
⏱️ CAPÍTULOS  
00:00 Introdução  
00:43 O que é o Claude e a Anthropic  
01:53 Claude Code vs Cowork  
02:53 Chat vs Agente de IA  
04:41 Chat, Cowork ou Code?  
05:33 Como instalar o Cowork  
05:51 Planos Free, Pro e Max  
06:20 Criando seu primeiro projeto  
08:44 O arquivo CLAUDE.md  
10:28 Memórias e Markdown  
12:45 Exemplo: orçamento e e-mail  
13:16 Como funciona um agente  
16:00 Memórias vs Regras  
18:46 Opus, Sonnet e Haiku  
19:23 O que são tokens  
21:33 Gerenciando o contexto  
22:19 Quando usar cada modelo  
23:21 O que são Skills  
26:05 Criando sua primeira Skill  
29:37 Atualizando uma Skill  
31:51 O problema do contexto cheio  
32:36 O que são Subagentes  
38:11 O que é MCP  
42:13 Conectores: Gmail, Notion, Drive  
46:05 O que são Plugins  
47:11 Criando um Plugin do zero  
52:02 Instalando e testando o Plugin  
54:10 Tudo num repositório  
56:44 Boas práticas

## Transcript

### Introdução

**0:00** · Seja muito bem-vindo ao curso completo de cloud Cork. Aqui você vai aprender desde o básico para quem tá iniciando até o intermediário. Então, se você é um iniciante ou se você é uma pessoa que já tem experiência, tenho certeza que vai esclarecer muitas dúvidas que você tem sobre a ferramenta. A gente vai falar de skills, de MCPs, plugins, \[música\] subagentes, como você consegue criar tudo isso e também distribuir pras outras pessoas da sua equipe. Se você é novo por aqui, aproveite para se inscrever aqui no canal. Quero trazer bastante coisa gratuita, então com esse incentivo você me ajuda bastante. Então vamos começar falando do nosso projeto.

**0:32** · A ideia aqui é criar um projeto do início ao fim. No caso vai ser um processo de criação de conteúdo, que a ideia é a gente digitar, por exemplo, barra criar conteúdo e no final a gente tem um carrossel finalizado. Então falar um pouquinho sobre o que se trata o Cloud. Bom, o Cloud ele é uma ferramenta criada pela empresa Antropic. Antropic foi desenvolvida, foi fundada por Dario Amodei e Daniela Amodei, que são irmãos.

### O que é o Claude e a Anthropic

**0:59** · E o Dario Amodei, ele trabalhava na Open Ai, porém segundo ele, após perceber que a empresa tava indo para um caminho diferente, quando se tratava de segurança e responsabilidade, então ele decidiu sair da empresa e fundar a Antropic, que hoje é uma empresa que bate de frente aí com a Open AI, então uma das maiores do mundo quando se fala de inteligência artificial. Mas o que é o cloud? Se você abrir o cloud, você vai visualizar que a interface dele possui três abinhas aqui em cima. O chat ele funciona de forma similar ao chat EPT.

**1:31** · Então, se eu colocar aqui olá, tudo bem?

**1:33** · A função dele é me dar uma resposta.

**1:36** · Então, ele possui algumas ferramentas que a gente pode utilizar, por exemplo, buscar na web, eh, busque as notícias para ele pode nos ajudar a criar trabalhos, a escrever textos, fazer resumos, entre várias outras funções, incluindo criação de visualizações, que são os artefatos, entre outras. Agora, o que é o cloud code? O Cloud Code ele é uma IA agêntica, então ele é um agente de inteligência artificial que foi desenvolvido para desenvolvedores, para programadores. Então ele é feito para criar código originalmente.

### Claude Code vs Cowork

**2:06** · Depois de um certo tempo, a Antropic percebeu que profissionais que não eram da área da programação estava utilizando o cloud code por causa das suas funções agênticas, que ele consegue realizar tarefa do início ao fim, coisa que a gente não consegue fazer com o chat.

**2:24** · Percebendo isso, eles decidiram criar o Cloud Cowork. E o que é o Cloud Cowork?

**2:29** · Ele é basicamente o cloud code, porém voltado para profissionais de outras áreas. Então, se você é um advogado, se você é um profissional de marketing e etc, você pode utilizar o cowork sem ter a complexidade técnica do cloud code. O cowork ele tem várias funções de segurança, então ele é mais limitado do que o cloud code, porém ele consegue cumprir boa parte das tarefas aí que você precisa fazer se você não for um programador, tá? Mas então, qual a diferença de um chat para um agente de A? Isso muita gente acaba confundindo.

### Chat vs Agente de IA

**2:59** · Hoje nós temos os chats com ferramentas e nós também temos os agentes de IA. O chat com ferramenta ele consegue dar respostas, fazer pesquisas e realizar tarefas básicas. Alguns exemplos de tarefas básicas é resumos, trazer informações da internet, criar documentos. Esses são alguns exemplos de funções básicas.

**3:26** · Agora, os agentes de A, a função dele é realizar tarefas. Então ele tem uma autonomia muito maior do que um chat. Um exemplo que eu posso dar para vocês, se a gente vir no chat com ferramentas e falar para ele o seguinte: "Oganize minha pasta de downloads, ele vai pensar e vai me trazer um plano dizendo o seguinte: você precisa acessar sua pasta, fazer X, Y Z para você organizar ela." Agora, se eu vir no agente como cloud code e pedir para ele organizar a minha pasta de downloads, que que ele vai fazer?

**3:55** · Ele vai buscar onde tá a minha pasta, vai ver quais arquivos tem lá dentro, vai criar um plano e vai executar de fato. Então ele vai organizar a minha pasta porque ele já tem acesso ao meu computador e ele consegue executar funções lá dentro.

**4:08** · Diferente do chat que tá apenas na nuvem e ele não tem acesso às informações do meu computador. Ele responde dizendo que tem suas limitações e que ele não consegue acessar a nossa pasta de downloads. Diferente do cloud code. O Cloud Code tá contando os arquivos e ele vai de fato acessar a minha pasta e organizar ela para mim. E aqui ele já perguntou como que eu quero organizar a minha pasta, se eu quero por tipo, por tipo mais arquivos antigos, fazer uma triagem, enfim, ele já listou aqui quais são os meus arquivos, a quantidade, né, de arquivos, que inclusive tô precisando fazer uma limpa.

**4:37** · Mas você entendeu a diferença, ele realmente executa a tarefa. Então, como escolher entre essas três opções? Como eu disse, o chat ele é mais limitado e ele é bom para fazer tarefas básicas. Agora, o cowork ele é excelente para você conseguir realizar tarefas de forma autônoma, onde você cria ali um planejamento e ele executa essa tarefa dentro do seu computador, dentro de uma pasta ou em alguma ferramenta na web. Agora, o Cloud Code ele tem muito mais poder de acesso ao seu computador. O Cloud Cowork ele consegue operar dentro de pastas.

### Chat, Cowork ou Code?

**5:07** · Agora o Cloud Code ele consegue mexer na sua máquina inteira, inclusive pode apagar seus arquivos. Se você quiser que ele suba informações na internet, ele pode fazer isso também. Obviamente, se você der essas permissões. Então eu diria para você testar o chat. Se o chat não atender, testa o cowork. Se você achar que cork também não atende, aí vai pro code. Só que aí a complexidade aumenta um pouquinho mais. Mas futuramente eu vou fazer um vídeo desses aqui também cobrindo o cloud code, tá? Mas como você instala o cloud Cork no seu computador?

### Como instalar o Cowork

**5:37** · Basta você acessar cloud.aiaiai, clicar aqui nesse botão, ele vai fazer o download. Eh, vou até parar o download aqui, mas basta você abrir o aplicativo e seguir as instruções. É bem simples a instalação. Depois você precisa acessar com a sua conta. O cloud possui três planos, o plano Free, o Pro e o Max. O que vai variar é as ferramentas que você tem acesso. O Cowork tá disponível apenas a partir do plano Pro, que ele custa aproximadamente 17 por mês.

### Planos Free, Pro e Max

**6:02** · E o plano Max, que você vai ter um contexto muito maior, então você vai poder utilizar a ferramenta de forma mais livre, né? O Pro el é um pouco mais limitado, porém o Max já custa $100, que é um valor absurdo paraa maioria das pessoas. Então, assim que você logar com a sua conta, você vai ver algo parecido com isso aqui. Então, como funciona o Cloud Cowork de fato? Vamos começar criando um projeto aqui, exemplo, para mostrar para vocês. Então, a primeira coisa que eu quero fazer é, eu vou mandar algumas instruções, tá?

### Criando seu primeiro projeto

**6:29** · Eu criei um exemplo aqui de uma agência de marketing que a gente vai fazer é vir aqui em nova tarefa, depois é só clicar aqui na pastinha e clicar em criar novo projeto. A partir daqui você decide se quer começar do zero ou se quer usar uma pasta existente. A gente vai começar do zero mesmo. O nome vai ser claus content. E aqui dentro a gente pode colocar algumas instruções. Por exemplo, sempre responder em português. Basta eu selecionar essa pasta. Se eu tiver algum arquivo ou alguma coisa que eu queira enviar, eu também consigo enviar por aqui.

**6:59** · Quero que você crie um repositório para minha agência. Aqui dentro vamos gerenciar memórias, regras, ferramentas e outros detalhes. Quero que você crie a estrutura de pastas de forma simplificada e gerencie as memórias de forma local. Por que gerenciar as memórias de forma local? Por padrão, quando você dá um feedback para ele ou fala alguma coisa, ele vai salvar uma memória. Então, digamos que ele escreveu ali um texto com travessão e você não quer que ele use travessão.

**7:31** · Se você der um feedback, ele vai salvar essa memória, porém ele vai salvar dentro do usuário. Então, essa memória vai ficar salva só no seu computador. E se a gente quiser compartilhar essa pasta com alguém, essa memória não vai est lá.

**7:44** · Então, eu quero que ele gerencie as memórias de forma local. Por isso que eu disse para ele criar uma pasta memórias, porque assim eu consigo compartilhar essas memórias também. Se você não quiser compartilhar, você pode pedir para ele salvar no usuário, mas aqui nesse exemplo, eh, eu quero que as memórias também sejam compartilhadas. Aí aqui embaixo eu posso dar mais detalhes, né? Minha agência é, eu posso pegar as informações que eu deixei aqui no nosso mapa mental, que tem uma descrição resumida aqui sobre nossa agência. Aqui embaixo eu posso selecionar se eu quero que ele pergunte antes de executar ou se eu quero que ele execute antes de perguntar.

**8:14** · No caso, a gente mantém como perguntar porque daí ajuda a gente a fazer um planejamento. Então aqui ele já criou toda a estrutura do projeto para mim. Como eu já tinha uma pasta criada, ele criou uma pasta nova, né, chamada Close Content. No caso nem precisava, né, mas enfim, daria pra gente deixar direto no desktop. E aqui dentro você viu que ele criou a estrutura de pastas e também de gestão de memória. Mas como você percebeu, o texto tá todo em inglês. Então, digamos que eu quero que ele mude para português. Quero que você use português em toda a estrutura.

### O arquivo CLAUDE.md

**8:45** · Enquanto ele vai renomeando tudo, vou te mostrar aqui também esse arquivo chamado cloud.m.

**8:50** · Esse arquivo ele carrega em todas as conversas. Então aqui dentro que a gente coloca as instruções que precisam ser carregados assim que a gente inicia uma nova tarefa. Um exemplo é tom de escrita, qual o idioma que você quer que ele responda, como que você quer que ele responda. Então eu posso colocar aqui, por exemplo, sempre responda em português e vou salvar o arquivo. Assim ele vai criar um arquivo para mim chamado cloud.md. E a partir do momento que eu iniciar uma nova conversa, eu posso fazer com que ele puxe memórias e regras que a gente tinha especificado antes.

**9:21** · Então eu posso até dizer aqui para ele, quero que você inclua informações sobre o nosso projeto dentro das instruções. E se você quiser ser ainda mais claro, coloca cloud.m.

**9:37** · Assim, ele vai atualizar as nossas instruções e vai colocar os detalhes do projeto. A partir daí, ele vai saber onde estão as memórias, onde estão as regras, qual que é a estrutura, do que se trata a empresa, que que ele deve carregar primeiro e etc. Então aqui ele já atualizou o meu cloud.md com informações da minha agência. E aqui você vê que tem memória, qual que é a pasta de memórias, quais são as regras, né? Informações sobre isso. Então, se eu iniciar uma nova tarefa aqui com o meu projeto selecionado, eu posso perguntar aqui para ele do que se trata a minha agência.

**10:07** · Ele já vai saber do que se trata. Tá vendo que ele já carregou as instruções? Então, aqui do lado é o que ele tá trazendo para dentro do contexto dele. E ele já sabe o que que é. É uma agência de marketing fundada em 2022, etc., né? Informações fictícias. Mas você percebe que ele não precisou carregar outras informações, porque o que a gente precisava já tava aqui dentro de instruções. Agora eu quero que ele memorize os nossos serviços. Então aqui eu tenho uma imagem contendo a tabela de serviços e eu quero que ele memorize isso. Memorize nossos serviços.

### Memórias e Markdown

**10:39** · Posso enviar essa imagem para ele e ele vai pegar isso e jogar dentro de um arquivo ali também no formato markdown.

**10:46** · E o que se trata esse formato markdown?

**10:48** · Markdown é basicamente um arquivo de texto, é como se fosse um txt, porém ele possui algumas regras de formatação. Por exemplo, se eu abrir isso aqui no meu editor de texto comum, você vai ver que ele é um arquivo de texto, mas aqui ele tem essas hashtags aqui que é para definir se ele é um título de nível um, de nível dois. Quando tem é esses asteriscos aqui, é para definir se é se é em ou não. Aqui é uma lista.

**11:13** · Enfim, é bem simples. É basicamente um arquivo de texto com formatação. E os modelos de inteligência artificial, eles conseguem lidar muito bem com esse tipo de arquivo. Não é como se fosse um doc X, um PDF, onde ele precisa de todo um processo ali para conseguir ler o arquivo. Esses arquivos Markdown, eles funcionam de forma nativa, então é muito mais fácil do modelo lidar com ele, gastando muito menos tempo e também menos recursos. Aqui, como você pode ver, ele já pegou minha tabela de serviços e ele jogou dentro de memória/serviços.

**11:42** · Então, se a gente abrir aqui a nossa pasta memória e abrir o nosso arquivo serviço no bloco de notas, você vai ver que aqui já tem os detalhes sobre nosso serviço. Então agora, por exemplo, se eu iniciar uma nova conversa e perguntar quais são os meus serviços, ele já consegue me dar uma resposta, porque ele vai ler as instruções, ele vai verificar onde estão as memórias e a partir disso ele vai saber que ele precisa buscar informações sobre o nosso serviço. É que ele trouxe os nossos serviços.

**12:09** · Se eu perguntar para ele quanto cobr serviço, agora sim ele vai acessar as memórias e vai buscar aquele arquivo de serviços para mim e vai trazer que como você pode ver ele leu a memória. Ele já sabe que aqui dentro dessa memória tem um arquivo de serviços. Então, ó, serviços e preços tem a tabela oficial ali dentro. Então, ele já vai trazer a tabela aqui para mim.

**12:30** · E como você pode perceber, isso aqui tem um poder gigantesco, porque se a gente cria um repositório da nossa empresa e compartilha com a nossa equipe, eles conseguem ter acesso a diversas informações, eh, para que eles consiga utilizar ali no dia a dia deles.

### Exemplo: orçamento e e-mail

**12:45** · Por exemplo, com uma tabela dessa eu posso fazer um orçamento. Então, se eu pedisse aqui, ó, faça um orçamento eh de quatro posts no feed, um carrossel, roteiro para TikTok, ele vai fazer o orçamento para mim. me entregar o orçamento pronto. E eu posso pedir, por exemplo, escreva o orçamento em formato de e-mail. Então, ele vai \[roncando\] pegar aquela tabela e transformar em um e-mail. E por aí vai.

**13:11** · É só um exemplo rápido aqui para vocês entenderem do potencial que tem essa ferramenta, né? Aqui ele já virou modelo de e-mail. Vamos voltar aqui pro meu mapa mental que eu vou explicar para vocês o funcionamento do agente. E é muito importante que vocês entendam isso porque vai dar uma clareza muito maior para vocês. No caso do chat, quando eu peço para ele eh faça um repositório para minha empresa, como que o chat vai interpretar isso? Ele vai buscar contexto e fazer um planejamento e vai me responder, né? Então ele vai pegar o que tem dentro da conversa dele, que a gente já conversou anteriormente.

### Como funciona um agente

**13:43** · Com base naquilo, ele vai fazer um planejamento. Então ele vai ver se a gente já falou sobre a empresa. Ele vai listar ali um planejamento eh do que a gente pode fazer para criar esse repositório. Ele vai me dar uma resposta, certo? Qual que é a diferença ali do agente? Como que ele vai funcionar? O agente ele vai fazer um processo parecido, mas ele vai buscar o contexto, ele vai fazer um planejamento e ele vai agir.

**14:06** · Esse aqui é o principal. E depois ele vai me dar uma resposta. E ele pode voltar aqui novamente se a resposta não for ideal. Então, digamos que assim, ele buscou o contexto, fez um planejamento, agiu, só que ele viu que a estrutura não ficou ideal da forma como a gente queria, porque no processo de revisão ele viu que faltou alguns arquivos.

**14:23** · Então, o que acontece? Ele pode buscar o contexto novamente, fazer um planejamento novo e agir até ele ter a resposta ideal para eles nos dizer que tá tudo certo. Só que aqui faltou um detalhe que é verificar o resultado.

**14:36** · Então, antes de ele dar resposta, ele precisa verificar se o resultado foi ideal. Então, se ele vê que o resultado não foi ideal, que que ele vai fazer?

**14:44** · Ele vai voltar a buscar contexto novamente. Por exemplo, digamos que na hora dele criar uma pasta deu um problema de permissão, ele não conseguiu criar a pasta. Então, no momento que ele vai verificar o resultado, ele consegue identificar esses problemas e agir novamente. Mas em vez dele buscar o contexto e agir eh diante da tarefa principal, que é fazer um repositório, ele vai agir diante da tarefa que impactou o resultado. Digamos que na hora de verificar o resultado, ele viu que um arquivo não foi criado. Ele vai ver qual arquivo não foi criado. Aqui no contexto. Ele vai fazer um planejamento, porque aqui ele já vai ter a resposta.

**15:18** · Arquivo memória. MD não foi criado e vai verificar novamente. Deu certo? Deu.

**15:23** · Então ele dá resposta. Seu repositório foi criado com sucesso. Então você vê a diferença aqui. Ele tem um fluxo maior, é, e dinâmico. Então assim, com base nesse fluxo, a gente consegue ter resultados muito melhores. Por quê?

**15:38** · Primeiro que a gente tem gestão de memória, então ele sabe qual que é o nosso estilo, o que que a gente quer ali de resultado. Ele consegue revisar o que foi feito anteriormente e ele também consegue agir com base nisso, só para depois nos dar uma resposta. Muito diferente do chat que ele foi feito para responder. Então ele não consegue dar um resultado tão interessante como um agente que ele vai gerenciando essas tarefas de forma dinâmica, tá? Então qual as diferenças de memórias e regras?

### Memórias vs Regras

**16:03** · Isso aqui eu tô usando um conceito do cloud code, mas no cloud cowork por padrão, ele não tem esse conceito de regras, por exemplo. Então o que eu posso fazer é o seguinte, é quando eu tiver uma regra que precisa ser carregada em todas eh as sessões, quero que você adicione em regras e certifique-se de que isso está definido nas instruções do cloud.m. MD.

**16:31** · Aqui eu tô sendo específico, pessoal, porque é para vocês conseguirem entender realmente como que isso funciona. O que seria uma regra?

**16:39** · Uma regra ela pode ser um tom de resposta. Então, a ideia aqui é realmente quando eu criar uma nova sessão, a partir do momento que eu enviei uma mensagem, eu quero que essa regra esteja especificada ali dentro.

**16:50** · Então, isso é aplicado em só alguns casos. A gente não quer esses arquivos carregados o tempo todo. Por quê?

**16:56** · Dependendo da situação, isso vai consumir muitos tokens. E a gente não quer consumir tokens porque aumenta o nosso custo e acaba limitando a o nosso uso na ferramenta. Então, regras elas podem ser utilizadas só em casos muito específicos que eles precisam ser adicionados em todas as conversas. E outro detalhe é que dentro das instruções não é interessante que ela passe de 200 a 500 linhas. Então, a partir de certo momento, essas instruções elas vão ficar grandes demais para est aqui dentro. Então, o que que a gente pode fazer? Em vez de deixá-las aqui, a gente pode mover para uma regra.

**17:29** · Então, por exemplo, digamos que eu quero que ele carregue essas regras de comportamento dentro da nossa pasta regras. Eu posso colocar assim, regras/comortamentoesperado.md e pedir para ele criar um arquivo sobre isso, tá? Mas isso tudo pode ser feito no chat, tá bom, pessoal? Eu posso falar aqui, ah, minhas instruções estão muito longas, quero que você e quebre elas em arquivos diferentes dentro das regras e por aí vai.

**17:57** · Agora, diferente das regras, as memórias elas são carregadas assim quando são necessárias. Então, por exemplo, quando eu pedir o orçamento, ele só vai carregar a memória de serviços quando for preciso. Além disso, ele não precisa ter memória de serviço ali dentro. Mesma coisa se eu quiser escrever um postedin.

**18:18** · Digamos que eu tenho um arquivo chamado LinkedIn. MD. Esse arquivo, ele só precisa ser carregado quando eu for escrever um post sobre o LinkedIn. Então ele pode ser uma memória. Assim eu não fico ocupando o contexto de arquivos desnecessários, porque isso deixa a ferramenta mais lenta, mais gastona e também mais burrinha, porque ela vai dar resultados piores. Aqui embaixo, como eu falei, tem diferentes modos. Você pode selecionar o modo de perguntar antes de agir, mas também tem o modo agir sem perguntar, onde você dá autonomia dele executar ali tarefas dentro da sua pasta. Além disso, nós temos diferentes modelos.

### Opus, Sonnet e Haiku

**18:49** · Quando você inicia uma tarefa nova, você pode selecionar o modelo que você quer. Tem o Opus, que é o modelo com maior capacidade deles, o Sonet e o Haiko, tá? Aqui tá do maior pro menor. E é o seguinte, o Opus ele possui duas versões diferentes. Ele possui a versão 1 milhão de tokens e a versão de 200.000 tokens. No Cloud Code você pode selecionar qual que você quer. Agora no Cloud Cowork acredito que seja é gerenciado automaticamente.

**19:16** · O Sonet ele suporta até 200.000 1000 tokens e o também até 200.000 tokens. E o que seriam esses tokens? Tá pessoal, vamos mostrar aqui para vocês um exemplo. Se a gente acessar esse sitezinho aqui, acho bem legal que a gente consegue visualizar melhor. Eu posso escrever um texto aqui, assim como eu enviei lá pro nosso cloud. Então, deixa eu copiar esse texto aqui. Vamos jogar lá dentro para vocês entenderem de fato o que é um token. Aqui, como você pode ver, cada token tá marcado por uma cor diferente.

### O que são tokens

**19:43** · E o token ele pode ser uma palavra como quando, ou ele pode ser eh parte de uma palavra, como aqui adicione. A regras é uma palavra, mas certifique-se tem dois tokens diferentes. E essa aqui é a forma como o modelo de linguagem trabalha. Diferente e da gente que conversa através de palavras e textos, o modelo ele entende números porque ele faz cálculos estatísticos para conseguir prever qual é a próxima palavra na sequência.

**20:09** · Então, quando a gente envia uma mensagem aqui pro cloud, como essa daqui, todas as mensagens anteriores elas também são carregadas. E o que ele faz é prever basicamente a próxima palavra. Então, quando eu pergunto para ele, "Olá, tudo bem?" Ele vai pegar olá, tudo bem? E vai ver qual palavra faz mais sentido vir depois dessa interrogação. Ele pode falar tudo bem, que são duas palavras e depois dessas aqui ele vai jogar novamente e vai prever a vírgula.

**20:37** · Depois ele vai jogar novamente e vai prever essas três outros, esses três outros tokens aqui dentro. Então tudo isso aqui, cada vez que a gente manda uma mensagem para ele, isso permanece no contexto. Então para ele conseguir prever uma interrogação, ele tem que injetar todo esse texto aqui anteriormente. Isso faz com que eh o poder computacional seja muito alto, né?

**21:04** · O custo computacional. Por isso que essas ferramentas são extremamente caras e e e absurdo assim que o pessoal tá fazendo para conseguir manter elas. E se você olhar esses numerinhos aqui em cima, ó, é isso que a IA enxerga quando você envia uma mensagem. Por isso é tão difícil ela conseguir contar a quantidade de caracteres de uma palavra, porque ela não enxerga da mesma forma que a gente. Esses tokens vão ocupando o contexto. Então, se a gente tiver 200.000 tokens desse aqui na nossa conversa, vai chegar um momento que o modelo não vai mais aguentar.

**21:31** · Então, ele vai fazer o quê? ele vai comprimir a conversa ou você deve iniciar um chat novo. O que eu recomendo, toda vez que você tiver com contexto quase cheio, né, você tiver conversado muito com o modelo ou você quiser realizar uma tarefa nova, recomendo você é começar aqui de novo, porque isso vai limpar o seu contexto e a partir do momento que você mandar uma mensagem, ele vai carregar apenas o arquivo necessário, né, que é o arquivo de instruções. Só aí que ele vai carregar o arquivo de serviços e vai ocupar mais um pedaço ali do nosso contexto, tudo bem?

### Gerenciando o contexto

**22:02** · Então é sempre importante você saber gerenciar esse contexto, porque é isso que vai definir o quanto você tá pagando ali de mensalidade e o quanto que vai custar para você isso no final. Então, se você tem um plano pro, por exemplo, é interessante você saber gerenciar isso para não ter que interromper o uso da ferramenta no meio da tarefa. E quando usar cada um desses modelos que a gente conversou aqui, o Opus ele é mais recomendado para tarefas complexas.

### Quando usar cada modelo

**22:25** · Então, raciocínio complexo, design, código difícil, análise profunda, é, agentes que são muito longos ou que precisam de muito contexto, é bom você utilizar o Opus, mas é o ponto negativo é que ele é pesado e gasta muito, então tem que usar com sabedoria. O Sonet ele é mais flexível, né? Então, para você usar com código do dia a dia, escrita, análise média, automação, até algumas tarefas complexas de nível médio, eh, você consegue repassar para ele. Ele também consegue lidar bem com o código.

**22:55** · O Sonet, ele gasta menos da sua limitação ali de tokens do plano. Agora, o Riku ele é o menor de todos e ele é interessante usar pra tarefa rápida de classificação, extrair informações, respostas curtas, fazer resumos simples, responder e-mail e ou tarefas que você precisa de um volume grande, mas não precisa de um raciocínio super específico, você pode usar o Haikel.

**23:17** · Então, é, use esses modelos com sabedoria, dependendo do tipo de tarefa.

### O que são Skills

**23:22** · Então agora vamos falar das skills. Eu sei que tem muita gente que provavelmente abriu esse vídeo pensando já nas skills, que é uma das ferramentas mais poderosas do cloud cowork, do cloud code chat e por aí vai. Então, vou mostrar para vocês como elas funcionam e como você pode criar suas próprias skills. As skills, como o próprio nome já diz, são habilidades. É um conjunto de passos que você consegue realizar de forma automática ali para automatizar um processo. Aqui eu coloquei alguns exemplos, né, do nosso caso. A gente tem criar notícia, criar proposta, revisar contratos e gerar dashboard.

**23:53** · Convenhamos que isso aqui é um negócio muito genérico. O que que é criar notícia?

**23:59** · Pode ser buscar informações na web.

**24:03** · Que mais que pode ter dentro de criar notícias? Pode ter escrever um resumo, verificar se as informações são verídicas, porque não basta a gente criar, né? Vai que é uma fake news e a gente tá escrevendo uma notícia falsa.

**24:18** · Pode ter criar o design do carrossel ou pode ter fazer um post do LinkedIn, enfim, uma sequência de tarefas diferentes que a gente consegue englobar dentro de uma única habilidade. Então, a habilidade criar notícia, ela pode fazer tudo isso aqui ao mesmo tempo. Então, a gente pode pegar tudo isso, englobar aqui dentro. Eu quero que ele faça o design do carrossel, faça um posto LinkedIn e eu quero que ele salve as imagens na pasta é da notícia. Só um exemplo, tá, pessoal, para para vocês entenderem melhor.

**24:49** · Mesma coisa, criar proposta. Que que criar proposta pode ter? Ver e-mail de contato, eh, listar serviços, fazer orçamento dos serviços, escrever e-mail de resposta. Então, eu poderia, por exemplo, no meu chat digitar criar proposta para o Google. Que que ele ia fazer? ele ia acessar o Gmail, o e-mail de contato através do Gmail, ele ia listar os serviços que estão inclusos dentro desse e-mail, né?

**25:20** · Que que ele tá solicitando? Ele quer que a gente faça um post, ele quer que a gente faça eh um vídeo pra internet, enfim, ele vai fazer orçamento desse serviço, vai escrever o e-mail e a partir desse e-mail ele vai lá e dentro do Gmail vai criar um rascunho pra gente. Então a gente distitou barra criar proposta e ele já fez tudo isso automaticamente, tá? Essa é a ideia das skills. É, esse é o poder das skills.

**25:44** · E hoje existem skills prontas que você pode baixar, por exemplo, skill própria para criar site, para facilitar ali o design, para não ficar com aquela cara de inteligência artificial, para gerar imagens, enfim.

**25:57** · Hoje você acha skill para tudo, para você enriquecer leads e por aí vai. Eu deixei essas pastas aqui, mas na verdade isso aqui é do cloud coding. Então as nossas skills pessoais no cloud cowork elas são gerenciadas da seguinte forma.

### Criando sua primeira Skill

**26:11** · Se eu acessar o cloud Cork aqui e eu vir em customize aqui ou customizar, personalizar, eu acho que tá em português, e eu vim aqui em habilidades, aqui dentro eu tenho as minhas skills.

**26:22** · Então aqui tem habilidades pessoais e habilidades integradas. Aqui eu também tenho plugins. E dentro dos plugins eu posso ter habilidades, conectores, entre várias outras coisas. A gente já vai entrar em mais detalhes sobre os plugins. Digamos que eu quero criar uma habilidade sobre escrever notícia, escrever resumo de uma notícia. Se eu clicar aqui em criar com o Cloud, ele vai abrir o chat para mim e conversando com ele, ele pode criar essa skill. Mas o que que eu quero fazer? Eu já quero fazer direto na nossa conversa, porque aqui ele já tem o contexto do que se trata nossa agência.

**26:52** · Eu não quero fazer lá dentro do chat. Então eu vou falar o seguinte para ele: "Quero que você crie uma skill para escrever notícias".

**27:02** · Escrever resumo de notícias. Você vai buscar, vai buscar as principais notícias no Google feed e vai me retornar cinco opções.

**27:16** · Depois que eu selecionar as opções, você deve escrever resumo da cinco e me retornar. Então é isso, ele vai buscar as notícias pra gente. Eu não especifico o tópico, pode ser que ele pergunte do que se trata as notícias. Ele vai buscar pra gente, vai trazer, eu vou escolher quais notícias eu quero que ele resuma e ele vai nos entregar o resumo pronto.

**27:39** · Mas ele já começou a executar a tarefa aqui para mim. Então ele associou aqui quatro agentes para pesquisar na internet para nos trazer essas notícias.

**27:46** · Então aqui, pessoal, o que que ele fez?

**27:48** · Mesmo sem eu pedir, ele criou um arquivo HTML para mim para que eu consiga visualizar quais fluxos ficaram mais interessante, né? Então ele tem a saída aqui com com as notícias, eh, e desde do das instruções até os resultados aqui, que é como as notícias apareceram depois. Então, posso revisar essas opções aqui e falar que tá tudo certo, ou eu posso simplesmente dar um feedback falando que eu quero que ele escolha a melhor opção. Pode escolher a opção mais eficiente. Então aqui ele já começou a criação da skill para mim automaticamente, sem eu precisar acessar ali a a aba de skills.

**28:20** · Então aqui ele já trouxe a skill empacotada pra gente conseguir instalar aqui dentro do nosso cloud cowork. Diferente do Cloud Code, onde a gente consegue colocar as habilidades dentro de uma pasta, no Cloud Cowork, a gente precisa instalar ele aqui na nossa aplicação web. Então, aqui tem os detalhes da nossa habilidade. A gente pode pedir para ele alterar se a gente quiser, mas aqui eu vou só clicar em salvar a habilidade e automaticamente ele já vai instalar ela pra gente.

**28:46** · Então agora da próxima vez que eu digitar barra resumo notícias, ele já vai executar todo esse fluxo para mim. Vamos fazer esse teste abrindo aqui uma nova tarefa. E tem que se certificar de que o nosso projeto está selecionado aqui. Mas eu coloco aqui, por exemplo, resumo notícias e ele já vai executar para mim. Então, todo aquele processo que a gente empacotou ali de buscar as notícias, ver quais são as notícias principais, escrever o resumo pra gente, isso já vai ser feito automaticamente aqui pra gente.

**29:15** · Outro detalhe, a gente consegue visualizar quais tarefas ele tá realizando nesse momento. Então, você vê que a primeira tarefa vai ser buscar as notícias do dia. Depois ele vai nos apresentar cinco opções onde a gente vai escolher. Depois que a gente escolher, ele vai escrever pra gente. E aqui ele já tá escrevendo os nossos resumos em paralelo, ó. Tá vendo? são daquelas notícias que eu pedi para ele resumir.

### Atualizando uma Skill

**29:37** · Uma coisa que chama muita atenção, que entrega um pouco, que é inteligência artificial, é o uso de travessões.

**29:42** · Digamos que eu não quero que ele escreva travessão, eu posso só falar aqui no chat, quero que você escrever com travessão. Atualize a skill para especificar isso e use também nossa memória melhorar o resultado. Então agora além dele atualizar a skill, né, para não incluir o travessão, ele também vai puxar a nossa memória ali automaticamente. Toda vez que a gente chamar resumo notícias, ele vai puxar também eh a nossa memória ali de tom de escrita.

**30:13** · Não sei se é esse exatamente o nome do arquivo, mas vamos só verificar aqui dentro. Na verdade, a gente nem tem o arquivo criado ainda, então vamos ver como que ele vai se virar ali.

**30:22** · Provavelmente ele vai criar um arquivo pra gente nas memórias com essas regras.

**30:26** · Olha aqui, como ele é muito espertinho, ele já achou onde tem aquela informação que é dentro das nossas regras de diretrizes editoriais. Então agora dentro da skill ele também vai englobar essas questões. E ele consolidou tudo isso dentro da memória. E aqui dentro do arquivo de memória, você viu que ele já especificou que não pode ter travessão, né? Que isso tá dentro das diretrizes e com o tempo isso vai aumentando, né? Vai se construindo.

**30:48** · Então é interessante a gente tá sempre pedindo para ele reorganizar essas memórias porque isso aqui no caso ele vai reforçar, né? que não precisa, não pode ter travessão, mas é interessante que isso esteja dentro de um arquivo separado e não necessariamente aqui no arquivo principal de memórias, tá? A ideia do arquivo principal de memórias é que ele seja um índice para outras memórias, né?

**31:10** · Para não ocupar muito espaço dentro do nosso contexto. Agora a gente pede para ele escrever novamente, mas vamos começar uma nova sessão, uma nova tarefa para ele não entender exatamente do que se trata. Então vamos ver se ele tá realmente é entendendo como que precisa fazer a nossa tarefa. Então aqui ele já tá escrevendo novamente as nossas notícias, porém sem ter o travessão, né?

**31:32** · mesmo eu tendo iniciado a partir de uma nova conversa que não falava nada ali sobre o travessão. Então ele de forma inteligente ele leu as instruções, ele puxou essa nossa skill e aqui dentro tinha informações, né, sobre não inserir o travessão. Então aqui ele já escreveu as notícias para mim, mas tem um grande problema nesse fluxo todo. E qual que é?

### O problema do contexto cheio

**31:52** · Se você vir aqui em web search, esse aqui são todos os sites que ele acessou.

**31:57** · Então, todas as informações de cada um desses sites foram inseridas dentro do nosso contexto. Então, para prever uma palavrinha aqui embaixo, ele precisou repassar, remandar esses, todas essas informações pro modelo. Então, para ele conseguir prever um tokenzinho aqui embaixo, ele precisou ler as informações de todos esses sites. Isso, como você deve imaginar, não é nada eficiente, porque acaba gastando muito token e também deixando a inteligência artificial mais lenta. modelo em si, ele fica mais lento para conseguir prever as próximas palavras.

**32:28** · Se eu mandar um oi aqui para ele, vai ser um oi carregado de todo esse contexto que tem aqui em cima, de todos esses sites aqui. Então, que que a gente faz para melhorar esse processo? É aí que moram os suagentes.

### O que são Subagentes

**32:43** · Se você vir aqui em customiz em habilidades, você vai ver que nossa habilidade já tá aqui dentro, tá? Ela foi instalada a nível de usuário, mas a gente consegue criar plugins e dentro dos plugins a gente consegue inserir habilidades, conectores, agentes e comandos. Beleza? Então vou mostrar tudo isso aqui para vocês. Então, como que funcionou esse nosso processo agora de buscar de resumo notícias? É isso, né?

**33:13** · Resumo notícias. Como que isso tudo funcionou? Primeiro buscou é buscar informações na web. O segundo passo dele, buscar principais notícias do dia, né? Vamos usar a mesma palavra aqui para facilitar.

**33:30** · Depois, que que ele fez? Apresentou as cinco notícias pra gente selecionar e depois ele escreveu o resumo dessas notícias selecionadas.

**33:42** · Então aqui, resumo, notícias. E aqui dentro ele escreveu a notícia um, notícia do notícia 3, notícia 4, notícia 5. Para ele escrever a notícia dois, ele ainda tinha notícia um dentro do contexto dele. Então assim, ele executou as tarefas dessa forma aqui. Primeiro, ele escreveu a primeira, depois a segunda, depois a terceira, depois a quarta, depois a quinta. tudo isso dentro do contexto dele.

**34:12** · Só que assim, a gente não precisa necessariamente da notícia dois para conseguir escrever a notícia quatro, porque é um assunto totalmente diferente. Então, assim, quando ele tá escrevendo a notícia três, pouco importa as informações da notícia dois ou notícia um. Ele não precisa ter isso dentro do contexto dele. E aí que moram os subagentes.

**34:33** · Os subagentes conseguem executar tudo isso aqui de forma paralela. Então, em vez do agente principal escrever primeiro a notícia um, depois a notícia dois, depois a três, depois a quatro, com todo aquele mundarel de site em cima, a gente pode delegar essa tarefa para um agente. Como isso funciona? A gente pode criar um agente, agente jornalista, por exemplo, pode ser um agente escritor de notícias, um agente criador de resumos e por aí vai.

**34:59** · E esse agente, ele vai ser especialista em criar notícias, criar resumos de notícias. Então o que que o agente principal vai passar para ele? Ele vai delegar uma tarefa. E qual seria essa tarefa? Resuma a notícia eh da guerra.

**35:18** · Um exemplo bem genérico aqui, pessoal, só para facilitar. Então, esse agente aqui com as informações daquela notícia ali, que é a notícia um, né? Notícia da guerra. Então, o que ele pode fazer?

**35:28** · buscar sites sobre a notícia da guerra, que é a um, né, por exemplo, resumir a notícia, só isso que ele precisa fazer.

**35:40** · Então, todas essas informações dos sites que ele acessou e tudo mais, vai ficar só dentro do contexto do nosso agente.

**35:46** · Os outros agentes que estão aqui, eles podem executar essas tarefas em paralelo, porque cada um vai ter uma tarefa diferente. Um vai ser resumir a notícia dois, o outro vai ser resumir a notícia três. Então, cada um desses aqui, ele vai ter um, eles vão ter um contexto próprio. Ele vai acessar os sites que precisam ser acessados, buscar as informações, fazer o resumo e só o resumo retorna pro agente principal.

**36:11** · Então a resposta que esse carinha dá aqui é o resumo da notícia. Então aqui seria resumo da notícia 5. Aqui resumo da notícia 4, resumo da notícia 3, 2, 1, etc. Então esse fluxo aqui é muito mais eficiente. Por quê? Eu vou dar o comando resumo notícias. Ele vai buscar as notícias. Eu seleciono as cinco que eu quero escrever e ele vai despachar uma notícia para cada agente. Então ele vai apresentar as notícias.

**36:37** · Eu selecionei, confirmei to, soltou cinco agentes e eles vão trabalhando em paralelo, muito mais rápido. E depois eles me retornam todo o resultado. Diferente dessa aqui que eu vou buscar eh informações de um monte de site, vou injetar no contexto, vou escrever primeiro da notícia um, depois que terminar da notícia um, agora eu tenho que escrever da da dois, da três, da quatro e da cinco. É sendo um trabalho muito mais custoso e demorado.

**37:03** · Isso aqui também fica muito claro. É, digamos que eu tenho uma skill chamada enriquecer leads, que é buscar informações de clientes no LinkedIn.

**37:13** · Digamos que eu tenho 500 leads. Imagina só o modelo dentro do contexto dele, buscando lead 1, lead 4, até no 500.

**37:22** · Imagina o tamanho do contexto que isso ia virar. O resultado ia ficar ruim, ia consumir muito contexto, muito token. É, não ia ser nada bacana. Agora, em vez disso, se ele lançasse bets, sequências de agentes de cinco em cinco agentes, esses agentes poderiam trabalhar em paralelo e o processo seria muito mais rápido, mais eficiente e consumir é menos contexto. Beleza? Então, esse é um exemplo aqui dos suagentes. Já já eu vou mostrar para vocês como criar esses suagentes também, mas antes eu vou mostrar sobre os MCPs.

**37:53** · Tô aqui finalizando a edição do vídeo, mas eu vim aqui para comunicar que eu tô concorrendo ao prêmio IBEST como autoridade em A. Então, se você aprendeu alguma coisa até aqui ou se você gosta do meu conteúdo, eu vou deixar o link aqui na descrição para que você possa votar em mim. Então, muito obrigado pela sua ajuda e vamos voltar lá pro vídeo.

### O que é MCP

**38:11** · MCP, pessoal, é bem simples de entender, tá? MCP significa model context protocol. É o protocolo de contexto do modelo de modelo, né? Acho que melhor.

**38:26** · Basicamente é para você conectar com ferramentas externas. Antigamente como que funcionava? Para você conseguir fazer uma IA, comunicar com Gmail, você precisava executar um código que conversava com a API do Gmail, tá? Eu sei que esse é um papo meio técnico e chato, mas basicamente você precisava criar um código que conversava com a API do Gmail. Se você quisesse conversar com Google Drive, você precisava criar um outro código que conversa com o Google Drive. Isso.

**38:57** · Se o Google Drive fizesse uma alteração na PI deles, como que eu vou fazer o upload de arquivo? Sendo que a API do Google Drive atualizou, agora ela funciona de forma diferente, o nosso sistema não faz ideia de como que ela tá funcionando agora? Então isso aqui acarretava uma série de problemas, porque quando você criava um conector utilizando o código, além de ser o processo muito mais dificultoso, ele não tinha um padrão. O que aconteceu?

**39:22** · A Antropic, de forma muito inteligente criou o MCP, que é um protocolo, é um padrão de utilização de contexto pros modelos. Então, em vez da gente conectar com a API do Gmail, agora o o Gmail ele consegue ter um servidor MCP. E o que que esse servidor MCP tem? Tem as ferramentas, tem exemplos de prompts e tem outros recursos que a gente consegue informar o nosso agente.

**39:50** · Então aqui a gente tem o nosso cloud, digamos assim, cloud cork. Quando a gente conecta o cloud cowork com o nosso Gmail, o Gmail consegue passar para ele todas as informações que ele tem. Então a gente já sabe quais as ferramentas que o Gmail possui. Por exemplo, escrever rascunho, eh, ler e-mail e listar e-mails, alguns exemplos, né? Então, quando a gente tiver conversando com o nosso cloud cowork, ele já vai carregar as informações de conectores que a gente tem.

**40:21** · Então, ele vai saber o seguinte, que a gente vai ter lá uma sessão serve para enviar, ler. Então, assim, quando a gente manda uma mensagem, ele já sabe quais conectores ele possui. Então, se a gente mandar uma outra mensagem falando o seguinte: "Screva um rascunho". Ele sabe que ele possui conexão com o Gmail.

**40:42** · Então, como ele possui uma ferramenta disponível para ele utilizar, ele vai chamar essa ferramenta. Então, ele pode chamar o Gmail e a tarefa escrever rascunho pro José. E aqui pode ter, por exemplo, o conteúdo do rascunho. Olá, José. Com o MCP é tudo padronizado, então basta a gente plugar a ferramenta com o nosso cloud ou com alguma outra ferramenta de a que ela vai entender como a ferramenta funciona. A gente não tinha a possibilidade de mandar e-mail antes, antes dessa conexão aqui com os Gmail.

**41:12** · Se eu pedisse para ele mandar o e-mail, que ele não tem ferramenta para escrever rascunho pra gente, mas como a gente conectou esse Gmail, agora ele tem uma ferramenta. Então ele sabe que a gente tem essa ferramenta de escrever rascunha. Mesma coisa, se a gente pedir para ele ler o e-mail, ele vai falar que e-mail? Ele não sabe que ele tem uma ferramenta ali, mas a partir do momento que a gente conectou, ele sabe o que ele precisa fazer. Mesma coisa com o Google Drive. Então, digamos que a gente tem o MCP do Google Drive e aqui no MCP tem as tem o a descrição dele. Então, esse MCP consegue fazer o upload de arquivos.

**41:44** · Aí aqui dentro vão ter as funções, né?

**41:49** · Quais funções? Beleza? Deletarquo e upload de arquivo. Se eu não conectar o MCP do Google Drive e eu pedir pro meu cloud fazer o upload de um arquivo no Drive, deu um arquivo no drive, ele não sabe o que fazer porque ele não tá conectado. Agora, a partir do momento que eu conectei os dois, tá? Então agora eu tenho uma conexão com o meu drive, agora ele sabe exatamente que ele precisa executar. Eu posso fazer o seguinte, se eu vir aqui na opção customize, aqui dentro nós temos conectores. E aqui você pode adicionar quais conectores você quer.

### Conectores: Gmail, Notion, Drive

**42:20** · Um deles que tá disponível aqui nativamente é o Gmail. Então basta você clicar aqui nesse botão navegar conectores e aqui você consegue selecionar os conectores que você quer, no caso Gmail, Notion, Google Drive, entre vários outros. Se você clicar no maisinho, ele vai pedir com que você acesse a sua conta para dar permissão para ele. E a partir desse momento, você vai ter conectado a sua ferramenta com o cloud e ele já vai saber quais as funções que estão disponíveis lá dentro.

**42:50** · E aqui a gente consegue ver inclusive as ferramentas que eu falei para você. Ele consegue buscar ler um e-mail, né, especificamente ele consegue listar os rótulos que a gente tem. Ele consegue buscar por e-mails. E tem outras ferramentas aqui, ó, né? criar um rótulo, deletar o rótulo eh adicionar rótulos a mensagens, enfim, outras entre várias outras funções que ele consegue executar, incluindo criar um rascunho de e-mail.

**43:13** · Então, se eu vir aqui agora no meu cloud, que tá conectado com o meu Gmail, eu posso falar para ele fazer o seguinte: crie um rascunho de e-mail fazendo um orçamento para pedro@email.com, contendo o os valores totais e também uma tabela de valores para os itens, posto feed, roteiro de TikTok e outro roteiro de Instagram.

**43:43** · Tá, eu enviei isso aqui para ele. Então, como ele tá conectado com o nosso Gmail, ele vai lá, vai fazer esse orçamento com base no nosso arquivo de serviço. Vamos ver se ele vai carregar isso no nosso contexto aqui. Se ele não carregar, então aconteceu alguma coisa muito errada aqui que a gente cometeu. Mas vamos dar uma olhada aqui. Ele já carregou as ferramentas, então ele sabe que ele tem conexão com o Gmail. Ele já buscou o nosso arquivo, ó, nosso arquivo de serviços. Então ele vai escrever o nosso e-mail automaticamente já com o nosso orçamento e vai nos entregar um rascunho.

**44:15** · Aqui ele já tá criando, ó, o nosso rascunho. Eu devo ver um rascunho lá dentro criado. Aqui ele pediu permissão para executar a ação. Aqui a gente consegue visualizar, né? Ó, segue o orçamento referente aos itens. Aqui tem uma tabela de itens, valor total e com prazo de entrega. Aqui ele colocou abraço, né, close content, mas a gente pode especificar que a gente quer que ele responda de certa forma eh como uma pessoa. A gente pode falar que que a gente tem uma assinatura de e-mail específica por aí vai. Permitindo que ele executou a tarefa.

**44:45** · Acessando aqui meu Gmail, eu posso ver que ele já criou o rascunho aqui para mim. Então, ó, já tenho o olá, tenho segue o orçamento.

**44:54** · Aqui ele já colocou a tabelinha, né, com serviços fictícios. prazo de entrega de pagamento pode ser combinado. Pá, pá, pá. Mas se tivessem outras regras, né?

**45:03** · Digamos que eu tinha uma memória lá para dizer que eu só aceito o pagamento via PayPal, né? E por aí vai, que a minha assinatura, na verdade, tem que assinar como Rodrigo do Carmo. São só alguns exemplos para você ver o nível de poder que essa ferramenta tem. Isso aqui pode se estender para muitas outras tarefas, né? É algo que a gente criou rapidinho aqui, porém isso poderia ser feito para vários outros casos de uso que tem um poder absurdo.

**45:26** · Então, esses são os MCPs, são conexões que a gente consegue criar com ferramentas externas. É como se fosse uma tomada que a partir do momento que você conecta, o nosso agente passa a entender como aquela ferramenta funciona e ele consegue utilizar ferramentas dentro dela. Obviamente as ferramentas que essa outra plataforma dá acesso. No caso do Gmail, por exemplo, a gente não consegue enviar o e-mail com ele, mas a gente consegue escrever um rascunho. Mas tem outras ferramentas que dão diversas outras permissões.

**45:55** · Então isso aqui cobriu o mais pesado, digamos assim, do cloud cork, que é essa parte realmente de skills, agentes e conectores. O restante é bem tranquilo, tá pessoal?

### O que são Plugins

**46:05** · Então agora vamos falar sobre os plugins. Plugins nada mais são do que um conjunto de habilidades. Então eles conseguem possuir habilidades, né, as skills, comandos, agentes, conectores.

**46:19** · Os plugins servem para facilitar a transferência de conhecimento. Então assim, digamos que você tem uma agência de marketing e você quer transferir todas essas skills, esses agentes, esses conectores paraos seus funcionários.

**46:34** · Você pode ter um arquivo skill.plugin, então poderia ser agência e dentro desse agência.plugin você teria todos esses arquivos aqui. Então digamos que você criou 10 habilidades, digamos que você tem conect conexão com o Gmail, com o Google Drive. Sem essas conexões, as suas habilidades não funcionam. Então, se você tiver uma habilidade chamada criar orçamento ou fazer orçamento, essa habilidade precisa ter o conector do Gmail, senão ela não vai funcionar.

**47:03** · Você meio que empacota todas as funções necessárias para que a pessoa consiga utilizar e é muito simples dela instalar lá também. Então, vou te mostrar como criar esse plugin. E assim como eu mostrei para vocês que a criação das habilidades pode ser feita diretamente pelo chat, inclusive você consegue transformar o chat aqui em habilidade, mas eu não gosto muito de fazer isso.

### Criando um Plugin do zero

**47:24** · Você pode vir aqui no chat e falar o seguinte: "Eu quero criar um plugin chamado agência. Dentro dele, quero que contenha uma skill de criar notícias que basicamente vai fazer uma busca e após aprovadas vai escrever resumo. Também quero outra skill chamada design carrossel, que vai pegar esse resumo, buscar uma imagem livre de direitos autorais e fazer o design de um carrossel em HTML.

**47:58** · Precisamos também criar o template do meu carrossel. Quero também criar um comando. E o que seria o comando, pessoal? O comando ele é diferente da skill. Eu posso digitar barra e colocar resumo notícias. Isso aqui é uma skill, mas é também um comando. Então é um comando que chama uma skill, mas uma skill não necessariamente precisa ter um comando. Existem skills que são chamadas automaticamente pelos agentes ou pelo modelo.

**48:27** · Então você não precisa necessariamente ter um comando para skill para chamar ela automaticamente.

**48:33** · Então essa skill aqui, por exemplo, de resumo notícia, eu não precisaria necessariamente ter ela um comando para ela, porque ela poderia ser chamada automaticamente por um agente. Aqui, no caso, eu queria ter porque para mostrar como exemplo para vocês. A ideia é criar um comando central que quando eu chamar criar conteúdo, ele já chame a skill de criar notícias e a outra skill de design de carrossel. Então o comando ele consegue executar várias skills.

**48:59** · Então quando eu der barra criar conteúdo, ele já vai criar para mim fazer essa busca de notícias, chamar os agentes para escrever a notícia, né? Inclusive é interessante eu especificar isso aqui.

**49:13** · Eh, nosso plugin também terá agentes que vão escrever as notícias em paralelo e outros agentes que farão o HTML do carrossel. Então assim, a ideia é a gente despachar vários agentes, eles vão fazer o resumo. A partir do momento que eles tm um resumo, a gente vai despachar vários agentes novamente para criar os carrosséis. Tudo isso em paralelo. Então nós teremos cinco resumos esses cinco carrosséis sendo feitos em paralelo.

**49:42** · Outra skill, né? Coloquei scrill que vai chamar as duas skills automaticamente e vai passar as tarefas de uma para outra. Por exemplo, após finalizar os resumos, faça o HTML das cinco notícias.

**50:03** · Então, aqui, pessoal, eu não tô colocando o MCP específico, né, um conector dentro desse nosso plugin, mas eu quero que ele faça todas essas funções aqui pra gente. Então, vamos ver que que ele vai retornar. Então, aqui ele fez uma pergunta, né, sobre qual nicho de notícias que a gente quer buscar. Aqui eu vou colocar tecnologia e educação pros carrosséis, cinco slides do tamanho do Instagram. Eh, da onde ele quer ele busca as imagens, né? Vamos falar para ele buscar eh busca genérica mesmo da internet, só pra gente testar.

**50:34** · E ele perguntou onde ele deve criar o plugin. Eu vou falar o seguinte: quero que você me retorne o plugin pronto para que eu possa instalar. Então aqui ele vai me retornar o arquivo em vez de já adicionar diretamente lá na pasta, tá pessoal? Então aqui ele me retornou o template que ele criou, né, que é meio tenebroso assim, mas para intuito aqui da nossa explicação é bom o suficiente.

**50:56** · E um caso de uso real, a gente pode refinando esse tema até ficar bom o suficiente. Pode falar para alterar as cores, alterar o tamanho da fonte, enfim, dá pra gente customizar praticamente tudo até ficar alinhado com nossa marca. É isso que eu fiz, no caso, é, pros meus próprios post, eu fui alinhando até ele ficar bem parecido com a minha marca. Hoje ainda tem um processo muito grande de feedback, parte de direção criativa mesmo. Então não é aquele trabalho que eu faço automatizado, né? Tem uma toda uma curadoria que eu preciso fazer para conseguir um resultado interessante.

**51:26** · Mas se você não liga pr pra qualidade assim, você pode pedir para ele fazer automaticamente e ele vai te entregar um resultado. Então aqui ele já finalizou a criação do plugin. Você pode clicar aqui em mostrar na pasta. E a partir desse momento é só você vir aqui em customizar plugins pessoais, clicar nesse maisinho aqui e fazer o p de plugin. Aqui, como você pode ver, você também pode criar conversando com ele ou adicionar o marketplace, né?

**51:52** · Aqui você arrasta o arquivo zip, você faz o upload e ele vai instalar automaticamente todas essas funções pra gente. Então aqui, por exemplo, já tem os agentes, né? O agente designer de carrossel, o escritor de notícias. Aqui tem as instruções que eles devem fazer, né, tanto para ele conseguir criar os templates e com designer ou também para escrever as notícias. E aqui tem as habilidades que a gente conversou. Primeiro, criar notícia, também tem design de carrossel e tem o criar conteúdo, né, que ele vai chamar as outras duas skills ali.

### Instalando e testando o Plugin

**52:23** · Aqui ele tá dentro de habilidades mesmo, tá, pessoal? Mas eh ele é um comando basicamente que vai chamar essas outras habilidades. Vamos começar uma nova conversa, né, para ter certeza que tá tudo certo e colocar criar conteúdo. Eu não vou precisar fazer mais nada. Então agora vamos ver qual vai ser o passo a passo. A ideia é que ele me traga as notícias, tá? Então tem que vir aqui nas tarefas. Aqui ele já chamou a habilidade, né, que é o que a gente pediu aqui em cima. As instruções também estão carregadas e ele já tá definindo a lista de tarefas.

**52:54** · Definido a lista de tarefas, agora ele vai agir. Então ele vai buscar aqui agora as notícias pra gente. Detalhe que ele tá usando o modelo Opus, mas não precisava necessariamente ser esse modelo. Agora que ele trouxe as notícias, eu vou aprovar todas aqui mesmo pra gente ver os agentes trabalhando em paralelo. Aqui ele já tá executando os agentes e você vê que ele chama ele por bets, né, por sequências de agentes. Então cada vez vem aqui estão vindo de dois em dois, né? Mas, ó, ele já executou o terceiro, então vai precisar de mais dois agentes para finalizar as notícias.

**53:24** · Aqui ele já tá escrevendo os resumos e tá salvando na pasta. A gente poderia especificar para ele se a gente não quisesse que ele salvasse na pasta, mas podemos manter assim mesmo. Deixa ele salvar lá os conteúdos. Pelo menos a gente tem um histórico. Já escreveu sobre três notícias e agora ele tá terminando de pesquisar duas aqui. Tudo isso realizado em paralelo pelos nossos agentes. A gente pode visualizar aqui os resumos que eles fizeram, ó. E o detalhe interessante é que a gente pode pedir para ele alterar o fluxo, pedir qualquer coisa e falar para ele criar um zip, né, do nosso plugin.

**53:57** · Com esse zip basta a gente enviar paraos nossos colegas de trabalho, eh, para amigos, etc., para que eles possam instalar lá na na ferramenta deles e utilizar também esse mesmo fluxo que a gente. E qual o benefício de usar uma ferramenta dessa dentro de um repositório? Bom, primeiro que você tem acesso a todas as ferramentas que você usa no dia a dia, todo o conhecimento ele fica guardado com você. Então você pode pegar esses arquivos e colocar no Google Drive. Se você decidir mudar de ferramenta, digamos que amanhã o Codex tá muito melhor que o Cloud Code.

### Tudo num repositório

**54:27** · Você quer migrar de ferramenta, basta você apontar o Codex para essa pastinha que você criou, que ele vai entender o que tá acontecendo ali dentro. Ele vai ter acesso a suas memórias, a seus arquivos, suas habilidades e por aí vai. Então, com o tempo, você vai aumentando essas capacidades e assim que tiverem interfaces diferentes, como por exemplo esse óculos da meta, né, você pode mandar um comando pelo óculos para ele executar no seu computador. Hoje em dia essas ferramentas ainda estão mais limitadas, né?

**54:56** · O meta, você precisa fazer algumas gambiarras para que você consiga mandar comandos. Porém, com o tempo, eles vão criar interfaces, aquele spin mesmo que a gente consegue conversar, ferramentas para celular, entre várias outras coisas que a gente vai conseguir mandar comandos através dessas interfaces para que elas realizem tarefas automaticamente pra gente.

**55:17** · Então, com o meu óculos, eu poderia dizer: "Faz um orçamento pro Pedro". E ele vai ler o e-mail automaticamente, vai ver qual o valor dos serviços, vai fazer o orçamento, vai enviar o e-mail.

**55:27** · Então você você consegue ter uma dimensão da quantidade de passos que a gente consegue automatizar com essas ferramentas e a gente consegue ficar somente com a parte criativa, né, que é isso que essas ferramentas é ainda pecam bastante. Ela consegue realizar muito bem tarefas quadradinhas como essa que tem um passo a passo, que tem um processo bem definido, mas elas têm muita dificuldade de realizar tarefas de design ou que envolve algo um pouco mais orgânico. Então tudo que é quadrado você terceiriza para ela e o restante você faz por conta, né, onde envolve mais inteligência humana.

**55:57** · E aqui ele já criou todos os nossos carrosséis com imagem de fundo, uma imagem eh que ele buscou na web. Já tem o texto aqui, as informações. E o próximo passo seria fazer uma revisão, né? Ver se esse conteúdo tá certo mesmo, ajustar o design, ajustar esse template. Mas você viu que com comando simples a gente conseguiu realizar esse monte de tarefas. Então, imagina só a quantidade de coisas que você não consegue facilitar aí no seu trabalho.

**56:21** · Por exemplo, hoje em dia eu uso até para fazer mercado, pedir marmita, essas coisas que são bem chatinhas mesmo, porque ele consegue inclusive mexer no seu navegador. Você instala o plugin do navegador, ele vai habilitar ali um MCP que ele vai entender como usar o navegador e a partir daí você consegue é pedir com que ele navegue no site. Então ele consegue usar o site para você também com o MCP do Google Chrome. E tem algumas boas práticas que eu recomendo também para vocês antes da gente finalizar, que é o seguinte, a gente não quer que apareça essa mensagem aqui, tá pessoal?

### Boas práticas

**56:53** · Isso aqui é uma situação bem trágica, é um uma limitação da ferramenta, tá? Um dos maiores pontos negativos aí do Cloud é que o plano Pro deles é muito limitado. Com o plano Max você consegue fazer bastante coisa, mas o plano Pro é lamentável assim em relação à quantidade de tokens, né, que a gente pode utilizar. A gente quer evitar isso. E como a gente evita isso?

**57:14** · sempre inicia uma nova tarefa e ele só traz o que é necessário. Eh, vê o que tá sendo carregado, que são os arquivos aqui na lateral. O interessante aqui do do cloud Cowork que ele mostra os arquivos para você, manter apenas o que for necessário e você usar um modelo correto para cada tarefa, que é o que eu falei, né? Tem três modelos diferentes.

**57:32** · Espero que vocês tenham gostado do vídeo, ficou muito longo, mas a gente conseguiu falar bastante coisa do Cloud.

**57:37** · Se você gostou do conteúdo, não esquece de deixar o like aqui, porque deu muito trabalho para criar. Também penso em criar uma comunidade. Se você tem interesse na comunidade, eu vou deixar a lista de espera aqui embaixo para você acessar para eu saber se vale a pena ou não eu criar essa comunidade. Mas lá eu queria abordar casos de uso mais específicos, por exemplo, para advogados, médicos, criadores de conteúdo, eh coisas que você pode usar no seu dia a dia, oferecer skills gratuitas, recursos, enfim. Essa comunidade faz muito tempo que eu quero criar ela, só que eu ainda não tive a disponibilidade.

**58:08** · Então, se você tem interesse, se inscreve na lista aqui embaixo, porque vai sinalizar para mim que vale a pena eu criar isso. Muito obrigado se você assistiu até aqui e a gente se vê no próximo vídeo. Valeu,