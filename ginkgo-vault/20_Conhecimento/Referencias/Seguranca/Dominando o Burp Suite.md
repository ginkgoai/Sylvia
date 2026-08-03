---
title: "Dominando o Burp Suite"
source: "https://www.youtube.com/watch?v=qOJmTB_9-3g"
author:
  - "[[Solyd Offensive Security]]"
published: 2024-07-03
created: 2026-07-15
description: "Bem-vindo ao nosso guia definitivo sobre o Burp Suite! Neste vídeo, você aprenderá tudo o que precisa saber para dominar essa poderosa ferramenta de teste de pentest em aplicativos web. Vamos explorar"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=qOJmTB_9-3g)

Bem-vindo ao nosso guia definitivo sobre o Burp Suite! Neste vídeo, você aprenderá tudo o que precisa saber para dominar essa poderosa ferramenta de teste de pentest em aplicativos web. Vamos explorar desde a instalação e configuração básica até as funcionalidades avançadas, como Spidering, Scanning, Intruder, e Repeater.  
  
Aprenda gratuitamente sobre Hacking e ainda ganhe certificado e suporte gratuitos.  
https://solyd.com.br/treinamentos/introducao-ao-hacking-e-pentest-2/  
  
Se torne um pentester profissional com o curso Solyd Pentest do Zero ao Profissional.  
https://solyd.com.br/treinamentos/pentest-profissional  
  
Proteja sua empresa contra hackers. Contrate um Pentest.  
https://guardsi.com.br  
  
As principais notícias de cybersecurity para serem lidas em menos de 3 minutos, todo dia em seu e-mail.  
https://caveiratech.com  
  
Nos siga em nossas redes  
Instagram: https://www.instagram.com/solyd.offsec  
LinkedIn: https://www.linkedin.com/company/solyd-offensive-security  
TikTok: https://www.tiktok.com/@solyd.offsec  
Facebook: https://www.facebook.com/solyd.offsec  
Blog: https://blog.solyd.com.br  
  
AVISO  
Esta é uma vídeo-aula ministrada a profissionais de segurança da informação e possui conteúdo estritamente educacional. Este vídeo não contém nenhum conteúdo ilegal ou que fere as normas e termos do YouTube e Google. O curso é ministrado em ambiente controlado respeita todas as leis e diretivas morais e éticas. Qualquer uso das tecnologias usadas neste vídeo fora de ambiente controlado e sem permissão pode ferir leis em diversos países.  
WARNING  
This is a video lesson given to information security professionals and has strictly educational content. This video does not contain any illegal content or hurts the standards and terms of YouTube and Google. The course is taught in a controlled environment complies with all laws, moral and ethical directives. Any use of the technologies used in this video outside of a controlled environment and without permission can hurt laws in several countries.

## Transcript

**0:00** · Neste vídeo eu vou elevar suas habilidades hacker você vai aprender a utilizar de uma vez por todas uma ferramenta que não pode faltar no seu Arsenal Então seja bem-vindo ao guia prático e definitivo do burp suite o burp Suit permite interceptar analisar e modificar todo o tráfego http que ocorre entre o seu navegador e aplicação web e não é só isso ele já vem equipado com diversas subfer ramentas que facilitam não só a descoberta mas também a exploração de vulnerabilidades Então vamos parar de conversa e vamos partir pra prática para instalar o suite você

**0:30** · pode vir aqui no site do part sger clicar em projects você vai selecionar community Edition que é a versão totalmente gratuita e clicar em download colocando aqui o seu e-mail logo em seguida você vai selecionar o sistema operacional que você utiliza então no meu caso é o Mac Mas você pode fazer o download ali Windows enfim e seguir ali com o processo de instalação da mesma forma como você instalaria qualquer outro software só que no meu caso aqui o meu Mac é o app silicon então vou clicar

**1:01** · para fazer o download ele já vai baixar ali o instalador beleza download concluído aqui só vou clicar aqui no dmg no meu caso no seu caso se você utiliz Windows só seguir com processo normal ali de instalação aqui eu só arrasto para applications e beleza bu sut já tá

**1:20** · instalado então vou abrir aqui a ferramenta perfeito Então esse aqui é o burp sut bom a primeira AB aqui é o dashboard que vai mostrar mostrar pra gente uma visão geral dos Testes que a gente tá realizando e aqui a gente consegue também criar novas tasks por padrão o burp já vem com uma Task ali de Crawling passivo ou seja ele vai todo momento que você tá acessando o site ele vai tentar buscar por links domínios hosts dentro daquele código e e colocar

**1:47** · tudo isso aqui na aba target onde vai ficar toda a estrutura dos Sites ali dos domínios que a gente tá testando n e aqui no dashboard você consegue também iniciar novas tasks que inclusive na versão paga na versão pro você consegue criar ali uma tesque de Scan né o burp

**2:04** · consegue fazer um Scan de vulnerabilidades que é até bem efetivo na versão community a gente não consegue fazer esse Scan mas mesmo assim o burp já vai fazer ali um Crawling já vai ajudar bastante Enfim então vamos lá agora pra aba proxy onde a gente vai conseguir interceptar e modificar as requisições gtp que ocorrem do nosso navegador pra aplicação web então e você

**2:25** · pode configurar um navegador externo ali na porta 80 80 que é a porta padrão onde o burp escuta né ou você pode simplesmente clicar em Open browser que o burp já vai abrir o navegador já configurado com proxy para interceptar as requisições do tráfego que ocorre por esse navegador então por exemplo se eu colocar aqui intercept Ison e acessar

**2:49** · aqui um site online Então nesse caso aqui teste phpv web.com Olha só o burp já interceptou essa requisição e ele me mostra aqui o cabeçalho com o corpo dessa request e eu posso modificar dando um Ford ele vai pra frente e segue com essa requisição lá pro pra aplicação web né dando um drop eu quebro né essa esse envio então

**3:17** · se eu der um Ford aqui a requisição vai pra frente ou se eu desligar o modo de interceptação ele segue ali com todas as requisições mas ele loga aqui no histórico do Bup no http his você vai ter uma lista de todas as requisições que o navegador tá fazendo e o burp tá interceptando Então olha só acessamos aqui o site e aqui no http History existe a requisição e a resposta http

**3:44** · que com todo o código HTML daquela página e o Bup também vai logar aqui o tráfego de websockets enfim agora indo pra ferramenta Intruder do burp e bom o Intruder é uma ferramenta utilizada para automatizar ataques fazer força bruta fuzzing Então vamos configurar aqui na prática um ataque de força bruta para descobrir uma credencial uma senha numa aplicação we só que para isso a gente precisa primeiro capturar a requisição que a gente vai utilizar para fazer esse ataque então aqui no

**4:15** · proxy eu vou selecionar aqui no meu navegador a requisição de login Ele já fala aqui que username teste a senha teste mas como simulação vou colocar uma uma senha incorreta aqui vou fazer o login aqui no

**4:33** · http History ele já logou aqui a requisição de login nesse caso aqui é requisição get então a debaixo ali para user info é o post que ele envia de fato as credenciais então vou clicar aqui com o segundo botão do mouse e enviar pro Intruder enviando pro Intruder a gente já consegue né manipular aqui qual o valor dessa requisição a gente vai utilizar para fazer o funing para fazer um ataque ali de força bruta nesse caso a gente vai fazer o fuz em cima de peça então a gente seleciona aqui o valor

**5:06** · clica em add para ele adicionar aquilo ali como ponto de ataque então ele vai tentar a partir de uma lista de uma Word list ele vai enviar várias requisições ali passando por cada item dessa Word list aqui em cima existem diversos tipos de ataque o ataque padrão é o Sniper que vai fazer justamente isso então é só você pegar uma lista eu já separei uma aqui e clicar aqui em paste copiando dando paste ele já vai colar essa lista aqui você pode enviar uma Word list completa para ele fazer o ataque né aqui

**5:37** · embaixo tem outras opções de processamento de payload enfim a gente não precisa disso clicando em start Attack ele já vai começar o Scan ele avisa ali que o Comin Edition tem uma limitação né no pro ele faz esse ataque de forma bem mais rápida você consegue configurar trads e tal mas aqui né a gente consegue já eh identificar a senha

**6:00** · da de login ali daquela aplicação que no caso é teste a gente já viu Ali pela pela página porém ele fez aqui todos os testes com cada item da lista então admin password olha só aqui embaixo ele vai alterando quando ele chegou no teste aqui né ele retornou um status code

**6:19** · diferente indicando que a gente de fato acertou a senha dessa conta muito legal né então agora indo para uma outra funcionalidade aqui do burp suite vou descartar o Intruder e vou pro Repeater o Repeater permite a gente reenviar requisições http então uma forma da gente manualmente ali né Enviar suas

**6:38** · requisições e analisar o comportamento daquela aplicação as respostas então uma ferramenta primordial no momento que a gente tá tentando identificar ou até explorando alguma vulnerabilidade o Repeater funciona da mesma forma eu preciso selecionar a requisição no caso vou selecionar novamente aqui user info na requisição de login e ele abre aqui o painel para modificar e reenviar essa requisição então eu posso clicar aqui em send ele vai enviar e vai mostrar aqui para mim essa resposta Olha só e o must login se eu alterar o parâmetro aqui

**7:11** · pass para test olha só ele já retorna uma outra resposta então eu consigo ir alterando a requisição aqui para entender como a aplicação eh se comporta a partir dessas alterações inclusive testar né diversas vulnerabilidades então por exemplo testar um SC injection colocar um uma simples aqui olha só

**7:32** · ocorreu um erro ali no navegador então isso aqui já é um indicador de vulnerabilidade J scaling Action tá Então olha só com poucos minutos aqui a gente já conseguiu identificar uma vulnerabilidade inclusive se você quer aprender a explorar essa vulnerabilidade e várias outras se você quer aprender a criar automações como Intruder ali criar

**7:50** · suas próprias ferramentas Eu recomendo que você faça o curso Pain test do zero profissional da Solid lá você vai ter toda a base necessária para se tornar um Pain tester de excelência disso vai ter diversos Laboratórios práticos para você invadir durante o seu estudo e até uma competição hacker valendo premum em Bitcoin Mas o melhor de tudo mesmo é que no final do treinamento você passa pela certificação SY CP Então você vai de

**8:11** · fato sair desse treinamento um Pain tester profissional pronto para atuar no mercado de segurança ofensiva o link do treinamento vai est aí na descrição e no comentário fixado bom Bora voltar pro vídeo na próxima aba A gente tem o colaborator que é uma ferramenta que não tá disponível na versão community do burp Switch Porém uma ferramenta simples que basicamente levanta um link ali um servidor que fica escutando por requisições isso é utilizado para eh

**8:35** · identificar a vulnerabilidade D ssrf enfim qualquer falha onde o servidor a aplicação vai fazer alguma requisição para Ah um host seu e você precisa logar Isso você precisa receber essa informação agora indo pra próxima

**8:51** · ferramenta a gente chega no sequencer que é uma ferramenta bem legal para analisar a aleatoriedade de tokens a entropia de Tok to então token de sessão como que ele é criado enfim você consegue utilizar isso aqui para identificar se né a partir das alterações das requisições isso Muda alguma coisa nesse token e com

**9:11** · base nisso analisar se esse token é previsível se a gente consegue forjar um token Enfim então da mesma forma a gente pode vir aqui no proxy selecionar a requisição e enviar pro sequencer ele já vai aqui e analisar né o a a requisição e a

**9:30** · resposta nesse caso aqui como a resposta não seta um Cook ele não mostra nada pede pra gente configurar uma localização customizada Mas se a gente for aqui no Repeater vou enviar essa requisição de login olha só ele dá um

**9:46** · set no Cook login Test Test eu vou enviar isso aqui pro sequencer e ele automaticamente já pega o Cook ali e eu consigo iniciar um Live capture ele já vai enviar divas requisições e quando eu clicar aqui em analy Now ele já vai analisar a entropia ali daquele token nesse caso não é um token né e ele tá

**10:09** · literalmente passando ali o próprio nome de usuário então isso já é um problema de segurança porém se fosse um token ali gerado né um identificador do usuário eh o sequênc iria tentar identificar o nível de entropia desse token de randomização A Próxima ferramenta Como o próprio nome já diz é um decoder ou seja ela vai justamente permitir com que a gente consiga fazer um encode e Decode de Strings em diversos e tipos de cifras então e por exemplo se eu colocar um texto aqui Hello eu consigo encodar por

**10:42** · exemplo em base 64 né logo abaixo posso encodar novamente URL fazer o Decode de URL então e essa ferramenta aqui ajuda a gente bastante quando a gente tá mexendo ali com token jwt Você precisa fazer o Decode ali analisar o conteúdo enfim eh

**11:00** · ajuda bastante outra ferramenta também ajuda bastante é o comparer aqui do burp Suit que permite a gente analisar a diferença entre por exemplo Duas respostas http Então posso vir aqui no proxy e enviar isso aqui pro comparer então ele pergunta ali se eu quero enviar a resposta ou a requisição posso virar aqui a resposta a resposta de um posso pegar essa outra resposta aqui enviar pro comparer então aqui eu vou fazer a

**11:29** · verificação do item dois com item três posso comparar por palavras ou por bytes no caso aqui vou Comparar as palavras e olha só consegue ver tudo que é diferente em cada uma das requisições então isso aqui ajuda bastante quando a gente tá por exemplo fazendo testes ali é para burlar um filtro uma validação da aplicação você precisa entender de fato o que que tá mudando ali na resposta o que que tá e alterando ali em cada

**11:55** · requisição que você faz isso aqui realmente ajuda bastante as próximas sub ferramentas aqui do Bup é o logger e o organizer o logger ele vai basicamente fazer o login ali de tudo né que tá acontecendo do seu Bup todas as requisições ali que ele interceptou todas as operações que ocorreram eh pelas ferramentas também então no caso do sequencer aqui ele vai listando todas as requisições que o sequência realizou ou Intruder Enfim então é uma forma da

**12:23** · gente eh analisar posteriormente ali o comportamento da aplicação de acordo com eh essa ess as requisições esses Scans um fuz enfim né o organizer também e vai nos ajudar a organizar né E por categorias esses logs então aqui eh você

**12:41** · consegue organizar essa essa lista ali de de histórico de requisições enfim e agora a gente entra no extensions e o extensions aqui do burp é realmente um negócio muito legal e que muita gente não utiliza entrando aqui no extensions você consegue eh instalar né diversas é

**12:59** · sub ferramentas externas que vão deixar o seu burp absurdamente mais robusto que vai implementar diversas outras funcionalidades de segurança de hacking no seu burp então clicando aqui em B App Store por exemplo você já tem como se fosse uma lojinha aqui para você instalar essas ferramentas algumas requerem que você tenha o bub Suit pro mas várias outras que vão te ajudar

**13:22** · muito durante o Pain test durante sua procura por bugs em programas de bug boun você consegue instalar de forma totalmente gratuita no seu Bup sut community somente clicando aqui instalando então por exemplo posso clicar aqui Auto analyzer ele vai analisar autenticação clicando ali Descendo um pouquinho clica em install ele automaticamente vai instalar a extensão e ela já vai ficar disponível para mim aqui no burp Olha só apareceu aqui o al analyzer então e isso é realmente um

**13:51** · ponto muito interessante do burp su que muita gente não utiliza e que isso aqui que torna realmente o burp uma ferramenta extremamente poderosa para um hacker por um Pain test Beleza então é isso pessoal o vídeo vai ficando por aqui até a próxima falou