---
title: "Como Usar o Hermes, o Agente de IA Autônomo 100% DE GRAÇA #hermes #ia #gratis #openclaw #tutorial"
source: "https://www.youtube.com/watch?v=XK-zLxFaATo"
author:
  - "[[Kauã Miguel - Dev]]"
published: 2026-05-21
created: 2026-07-17
description: "Como instalar o Hermes no PC. Como usar o Hermes com NVIDIA. Agente de IA autônomo de graça. Hermes com Telegram. Como controlar o PC pelo Telegram com IA. Sucessor do OpenClaw. Hermes tutorial portug"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=XK-zLxFaATo)

Como instalar o Hermes no PC. Como usar o Hermes com NVIDIA. Agente de IA autônomo de graça. Hermes com Telegram. Como controlar o PC pelo Telegram com IA. Sucessor do OpenClaw. Hermes tutorial português. Como usar os melhores modelos de IA grátis. Hermes vs OpenClaw. Nesse vídeo eu mostro como instalar o Hermes — um agente de IA autônomo que controla o seu PC e faz tudo por você — e como conectar ele nos modelos mais poderosos do mundo (Nemotron, DeepSeek, GLM, Kimi, Qwen) de graça via NVIDIA, sem cartão e sem trial. No final, conecto ele no Telegram pra controlar o PC de qualquer lugar.  
  
⏱️ TIMESTAMPS  
0:00 - Intro  
0:13 - Acessando o site do Hermes  
0:51 - Instalando o Hermes  
1:31 - O que é o build.nvidia.com  
2:11 - Pegando a API Key da NVIDIA  
3:45 - Configurando o Hermes (setup)  
5:26 - Hermes configurado e funcionando  
7:33 - Demo: navegando na web sozinho  
8:43 - Conectando o Hermes no Telegram  
13:00 - Testando o bot no Telegram  
13:50 - Encerramento  
  
🔗 LINKS  
→ Hermes: https://hermes-agent.nousresearch.com  
→ Node.js: https://nodejs.org  
→ NVIDIA Build: https://build.nvidia.com  
→ Qual modelo seu PC roda? https://canirunai.kc1t.com  
→ Tutorial do OpenClaw + NVIDIA: https://www.youtube.com/watch?v=TffgvumBJMg  
  
💻 COMANDOS (na ordem do vídeo)  
  
\# Instalar o Hermes (Windows nativo)  
iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)  
  
\# Rodar o Hermes  
hermes  
  
\# Instalar pacote de mensageria (caso falte)  
pip install "hermes-agent\[messaging\]"  
  
\# Configurar o gateway (Telegram, Discord, etc)  
hermes gateway setup  
  
\# Parar e reiniciar o gateway  
hermes gateway stop  
hermes gateway start  
  
📱 ME SEGUE  
→ LinkedIn: https://linkedin.com/in/kaua-miguel  
→ GitHub: https://github.com/kc1t  
  
\---  
Se ajudou, deixa o like e se inscreve! 🚀  
  
#hermes #hermesagent #openclaw #ia #gratis #nvidia #claudecode #inteligenciaartificial #programacao #dev #desenvolvedor #tutorial #opensource #coding #developer #tech #ai #devbr #techbr #dicasdev #tecnologia #nemotron #deepseek #glm #kimi #qwen #iagratis #telegram #agentedeia #aiagent #tutorialdev #alternativaclaudecode #terminalai #devtools #vibecoding

## Transcript

### Intro

**0:00** · Nesse vídeo eu vou te ensinar a instalar o Werms, um agente de ar autônomo que controla o seu computador e faz tudo por você. Ele faz aplicativos, conecta com Discord, Telegram e muito mais. E o melhor, usando os melhores modelos de a do mercado, totalmente de graça. Então vamos lá. E para começar, a gente vai ter que vir até hermassagent.nesearch.com.

### Acessando o site do Hermes

**0:18** · O link tá na descrição do vídeo, você basta você clicar ali no step um que vai est o link, beleza? E aí você vai cair nesse site aqui. Ele já vai trazer pra gente um comando em específico, mas a gente não vai rodar ele, porque esse comando aqui ele existe que a gente tem a WSL2 no PC, tá? No caso no Windows.

**0:30** · Então o como que a gente vai fazer? A gente vai até aqui em cima em docs e vai apertar. Aí ele vai redirecionar pra documentação do Herms, que inclusive é bem interessante para poder ler e entender melhor sobre o ARMS. E aqui embaixo ele vai dar duas opções de comando, Inux MacOS ou WSL2, como eu falei para vocês, é com o curl, ou aqui embaixo com uma versão L beta pra Windows via PowerhShell. E aqui ele vai dar esse RM, que vai ser o caso que eu vou usar nesse vídeo. Então a gente vai copiar ele aqui. Com ele copiado, a gente vai dar Windows e vai pesquisar por terminal. Caso você não tenha terminal, você vai pesquisar por PowerShell, tá? E aqui eu vou abrir outro terminal.

### Instalando o Hermes

**1:00** · E aí, beleza, vamos colar o comando que a gente copiou, que pode ser botão direito mouse ou contrtrl V para colar. E eu vou dar um enter.

**1:07** · Resumidamente, o que que o esse comando vai fazer? Ele vai est instalando os pacotes que o Windows precisa para poder usar o Hermes aí, gente. Então, por exemplo, o Python, Git, Node, que são muito importantes, FMEG para poder ter áudio, sabe? poder automatizar as coisas no PC. Você consegue ver todos esses pacotes, todas as instalações que são feitas é pelo repositório deles aqui e nacentação deles também, tá? Mas aqui não vou explicar todas as coisas específicas, tá? Mas enquanto isso, vamos atrás da nossa AP de graça para poder usar. Por qu Armes por si, ele é um agente com várias instruções, mas ele precisa de um cérebro.

### O que é o build.nvidia.com

**1:35** · E aí você pode usar o cloud code, pode usar trop codex até inclusive, mas caso você não tenha esse nenhuma assinatura de a vamos ter que pegar uma pake de alguma coisa. E como que a gente vai fazer isso? A gente vai vir até build.nv. nvidia.com. E o que tem nesse site aqui, né? Esse site aqui é basicamente um site de infraestrutura de a da Nvidia. Não se preocupa, não precisa ter Nvidia, você pode ter AMD, pode ter Intel, pode ser o que que for, é até celular, você consegue vir aqui e logar de boa, tá?

**1:58** · Não tem nenhuma restrição. Eles vão ter várias modelos de A, né, vários modelos já prontos aqui para você poder utilizar. Então, por exemplo, de psique, né, Motron que é deles LM ou até o gema.

**2:07** · Então, são modelos muito fortes que você consegue usar totalmente graça via Nvidia. Então, como que a gente vai começar? A gente vai vir aqui em login aqui em cima e vai se logar, né? colocar o nosso e-mail aqui. No meu caso, eu tenho um pré-pronto para isso. Vou apertar em next. E aí você vai passar pelo processo de login, tá? Que nada demais, é só você logar e verificar seu e-mail. E após você logar, você vai vir até aqui em cima novamente e vai aqui no seu nome, né? E aqui ele vai ter esse your API hate limit up to 40 RPM. E o que que é esse hate limit, tá?

### Pegando a API Key da NVIDIA

**2:32** · Basicamente é o tanto de requisições que você pode fazer por minuto aqui dentro da Nvidia, tá? E 40 requisições por minuto é bastante coisa, principalmente tá usando para algum modelo de ar, tipo openlaw ou arms, por exemplo, né? Então, com isso aqui em mente, né? Normalmente não teve cartão de crédito, não teve Pix, não teve nada, foi totalmente graça, tá? Então não se preocupa em ter cobrança, não se assusta quando eh com o uso que apareceu no terminal caso apareça, beleza? Então a gente vai vir aqui em API Kiss e aqui em API Kiss vai aparecer aqui generate API aqui a gente vai nesse botão e com esse botão aqui a gente vai escrever o nome da nossa API.

**3:01** · Então, no meu caso vai ser Herms test e aqui embaixo você definir a inspiração do seu token. Então, por exemplo, ah, eu queria um token de uma semana. Quando der uma semana a partir de hoje esse token vai sumir e não vai poder mais ser usado. Então, é importante que esse token seja seguro, tá? Que você use ele com segurança e não deixe vazar. Aqui, no caso do vídeo, eu tô colocando só por um dia, se não caso 24 horas, mas não se preocupa, você pode colocar 12 meses à vontade, tá?

**3:22** · Não, não se assusta com isso, não tem problema. ou um custom time, por exemplo, never expire, se quiser, né, que ele nunca vai inspirar, você nunca vai precisar voltar aqui, por exemplo, mas para mim, para alguém pegar minha chave de API, eu vou estar usando 24 horas, beleza? E eu vou est generate aqui. E aí, beleza, ele vai gerar aqui a sua chave de API, beleza? E aí você vai copiar essa chave, inclusive tem aqui a data de expperação dela, dia 22/05/05 de 2026. Eu vou copiar a chave de API. Com a chave de API pronta, a gente vai voltar no nosso terminal para poder aplicar ela em si, tá? Então, vou dar um out tab aqui e vou voltar pro terminal.

### Configurando o Hermes (setup)

**3:50** · E pronto, ele já instalou aqui o Airms.

**3:52** · A gente vai tá fazendo já o Airms setup, tá? E o que ele fez por trás, né?

**3:55** · Basicamente ele baixou todas as dependências que o ARMs precisa para poder configurar no seu PC. E agora ele vai te perguntar como você quer configurar ele. E ele dá duas opções, a opção quick setup ou a opção full setup.

**4:06** · Nesse caso, eu vou com quick setup, vou apertar um, vou dar enter e após isso, ele vai dar uma série de opções aqui. E o que são essas opções, tá? Essas opções são basicamente os provedores de que você consegue usar. Lembra que eu te falei sobre codex, por exemplo? Dá para você usar a viaentão deles ou usar tropicio open router, tá? Tem várias maneiras de você tá usando isso aqui.

**4:23** · Inclusive eu tenho outro vídeo no canal falando sobre como instalar o open claw que eu ensino você a usar de outra forma. E nesse caso, nós vamos estar usando uma outra coisa, já tá usando o quê? O Nvidia N, que é esse aqui, ó, Nem for models build.Nnvvidia or local name, né? Então o número dele é número 11. Eu vou apertar aqui número 11. E aqui ele vai perguntar sobre a chave de API.

**4:40** · Lembra que a gente gerou uma chave de API aqui atrás? A gente vai copiar essa chave de API e vai colar aqui com você direito mouse? Não vai aparecer na tela, tá? É normal. E aí você dá um enter e vai aparecer aqui API Key savet, tá?

**4:49** · Normalmente não aparece as informações por questão de segurança da própria do próprio Hermes, né? Eles fazem isso para te percutar e tal, se fosse uma senha, por exemplo. Aqui ele vai dar o base BRL, eu vou com essa aqui mesmo, vou dar um enter agora. E aqui ele vai dar as opções, né, que a Nvidia fornece de a para você integrar aqui no Herm Agent ou em qualquer outro lugar. A Nvidia funciona em quase qualquer provedor.

**5:06** · Então Cloud Code, Open Code, Codex, por exemplo, tem como você usar os modelos da Nvidia, tá? Então vamos subir um pouco aqui e eu vou est usando o modelo emotron deles, inclusive, tá? Eles têm aqui o OMI 30, é o Nemotron 3B. E eu vou est usando esse modelo Nvidia Nemotron 3 Super 120 limite B, tá? Então o código dele é o código 13. Aqui é só você pegar o código que você quer e ver qual modelo que você prefere. Nesse caso eu vou est com código 13. Aí você vai vir aqui, digitar 13 e dá um enter. Agora ele vai perguntar qual que vai ser o nosso back end, né? Como que ele vai ser executado na sua máquina.

### Hermes configurado e funcionando

**5:38** · Aqui vai dar várias opções, como por exemplo, local, docker, modal, SSH, deitona, né? Isso é algo que fica na cloud deles, por exemplo. E aqui, eh, para ser mais simples, eu vou est indo com o default deles, que é o local, tá? Que como eles baixou o Node, baixou o Python, um monte de coisa, é o recomendado você fazer. Mas caso você tenha Docker, é, recomendo que você use o Docker porque fica mais leve. Então, vou dar só um enter. E agora ele vai perguntar uma coisa importante aqui sobre a mensageria, tá? É importante que você entenda que esses plataformas como Airms ou OpenCla, Miniw, o objetivo deles é que você controle seu PC à distância, né?

**6:07** · Então você pode fazer de várias maneiras, por exemplo, WhatsApp, Telegram e Discord. Nesse caso aqui, pra gente não f perder muito tempo aqui, eu não vou fazer agora, tá? Eu só vou pular o eh a mensageria, mas depois a gente vai voltar aqui, tá? Então não se preocupa, quando eu setar o Nvidídeo aqui e terminar, a gente vai voltar para poder colocar o Telegram aqui no Hermes.

**6:25** · Beleza? Vou dar um dois e a gente tá ready to go. Inclusive ele deu os comandos aqui, né? O configur settings, que é setup, que basicamente acabou de fazer ele, e logo abaixo o ARMS gateway para poder configurar que o Telegram, Discord, o que foi, para poder bater no nosso computador. E aí, beleza? Aqui ele vai at comentar: "Restart seu terminal para poder aplicar as alterações de PEF, né? Eh, vou fazer isso para poder não dar nenhum problema, mas aqui ele dá os comandos principais. Então, herm setup, config, config edit, gateway e update."

**6:51** · Para começar o é basicamente você só rodarms, tá? Mas aqui eu vou fechar o terminal, eu vou procurar por terminal novamente e vou abrir aqui e eu vou dar um herms. Talvez demore um pouco a primeira vez, mas não se preocupa, ele é um processo, por assim dizer, pesado com muita coisa. Mas finalmente estamos aqui com o Hermes agent totalmente configurado na nossa máquina. Inclusive ele tem algumas configurações aqui que ele já fala, tá? As coisas de de browser inclusive. E vamos descer aqui embaixo, né? Ó, ele falou aqui, ó, o nosso modelo Nemotron 3 Super 120B e ele tá aqui com as questões dele. Vamos dar um oi.

**7:21** · E pronto, estamos com o Herms configurado no nosso computador. Então você viu como foi simples, foi questão de cli para poder configurar o Herms e ter uma PIDA de graça integrando nele, tá? E agora, antes de colocar o Telegram, vamos fazer um teste mais forte. Eu vou rodar aqui para ele acesseg.com/trending e diga os três primeiros. Por padrão, o Airms Agent já veio com algumas coisas instaladas.

### Demo: navegando na web sozinho

**7:47** · Então, por exemplo, ele vem com eh browser automation, vem com algumas skills de inteligência, geração de áudio, geração de voz, tá? Então ele tem várias skills que tornam ele um agente automatizado muito maneiro.

**7:59** · Inclusive ele tá aqui já, né, preparando o browser navegate e e navegando até gitub.com. E pronto, ele foi até o site gitub.teng e trouxe pra gente aqui os três principais repositórios que estão em tendência. E cara, tem uma variedade impressionante de técnicas aqui e skills que o Herms tem que você pode usar no seu dia a dia. Então, cara, é realmente um agente totalmente autônomo no seu PC.

**8:20** · Inclusive, eu tenho aqui até uma máquina virtual onde eu uso isso para ter várias eh rotinas diárias. Então, por exemplo, você pode colocar: "Ah, eu quero que todo dia 5 da manhã você faça X YZ.

**8:28** · Quero que todo dia você abra meu Discord e faça uma coisa no servidor, quero que você faça uma análise de gráficos, quero que você faça uma análise de dados, por exemplo, então cara, isso aqui é limitado somente à sua criatividade como pessoa usando a IA Autônoma". E agora, se eu quiser configurar o Telegram para poder mandar mensagem pro meu PC remotamente, né? Como que eu vou fazer isso? A gente vai primeiramente cancelar aqui o terminal, né? Eu vou dar um contrtrol C, vou dar aqui um clear só para limpar o terminal e eu vou colar o comando aqui gateway setup, tá?

### Conectando o Hermes no Telegram

**8:54** · Aqui vai dar uma série de opções pra gente, né, de conectores, por exemplo, como kckbot, e-mail, discord, telegram. E aqui eu vou est fazendo com o Telegram. Então vou apertar o número um, vou dar um enter e aqui ele vai pedir o token de bot. E para isso vamos ter que ir lá no Telegram. Como que a gente pega esse token de bot? A gente vai voltar aqui pro nosso Chrome. E aqui no Chrome a gente vai pesquisar por bot father.

**9:16** · automaticamente se pesquisar @botifad ele já vai aparecer aqui pra gente no Instagram. Então eu vou apertar aqui nesse launch @botfad ele vai pedir aqui para poder abrir via desktop, mas nesse caso eu não vou, vou apertar cancelar e eu vou abrir em web. E beleza, chegando aqui no botfader, a gente vai rodar o seguinte comando. A gente vai rodar barra newbot. A gente vai pedir o nome do nosso bot, nesse caso, pro teste do Herms E aqui vai pedir o nosso username pro bot, tá? Que é basicamente tem que ter bot no final com camel case ou com case, tá? Então aqui eu vou dar um herm underline bot e pronto, já criou aqui o nosso bot.

**9:49** · Aí ele vai fornecer pra gente aqui esse token de API, né? A gente copia ali com o botão esquerdo do mouse e vai aparecer aqui code copy clipboard. Nisso a gente vai voltar pro nosso terminal e vai colar aqui esse token novamente. Caso não apareça na tela, não se preocupa, é normal, ele tá ocultando por questão de segurança. Eu colei aqui já com o botão do mouse e eu vou dar um enter. E pronto, Telegram token Saved. E agora ele vai pedir aqui o nosso token de usuário, nosso ID de usuário, né? Ele até fala como fazer isso. A gente vai dar uma mensagem para user infobot no Telegram e ele vai responder com o nosso ID numérico, tá? Para isso eu vou fazer a mesma coisa, o mesmo processo.

**10:20** · Eu vou dar aqui em user infobot Telegram e vai aparecer aqui em cima. Eu vou fazer o mesmo processo. Eu vou aqui n em open em web e vou dar um start aqui. E pronto.

**10:31** · Aí passa aqui as infos do meu perfil, tá? Não se preocupe, isso aqui não é perigoso, todo mundo consegue. Se eu vi aqui e tacar outro usuário, vai aparecer também. Eu vou copiar esse ID aqui em cima. E aqui eu vou copiar esse ID. Como que eu vou fazer isso? Eu só vou apertar com o botão escrito do mouse no ID e pronto, tá copiado. Aí eu vou voltar pro terminal e eu vou colar com o botão direito do mouse. E aqui ele aparece porque não é um dado sensível, tá?

**10:50** · Inclusive, se você quiser passar mais de um usuário, você consegue fazer isso passando vírgula e o outro ID, tá? É tudo colado. Mas nesse caso aqui eu só vou passar o meu usuário. Então só cola ele aqui e dá enter. E aqui ele vai perguntar se é o nosso home channel.

**11:01** · Então, por exemplo, lembra que eu falei que ele pode rodar coisas diariamente?

**11:04** · Então, quando ele terminar a ação X, ele vai mandar mensagem aonde? E aqui vai perguntar: "Quesse user ID aqui?" Eu vou falar que sim, quero que seja. E aí, pronto, configuramos o Telegram no nosso usuário. E para terminar isso, é só você dar 22, que ele vai dar um don, e você dá um enter. E perguntar: "Você quer iniciar o gateway agora?" Sim ou não?

**11:20** · Nesse caso, vou falar que sim, com o yes, né? Com y. E aqui vai perguntar se a gente quer iniciar automaticamente o gateway, né? Essa porta de conexão com o Telegram, sempre que eu iniciar o computador. Vou falar que não nesse caso, mas caso você esteja fazendo realmente uma automação, coloque sim. E aqui vai perguntar se a gente quer iniciar o gateway logo depois de instalar ele. Vou falar que sim também com Y. Aqui a mesma coisa, né? Você quer iniciar automaticamente, eu vou lá que não. E agora em background vai começar a rodar o nosso gateway, tá? Que o gateway é muito importante porque ele é uma po conexão entre é um processor externo, né?

**11:49** · Como que o o Teams vai falar com você, como que o Google chat vai falar com você? Ele vai bater uma porta no seu PC, né? Que é basicamente isso que o Gateway faz para poder conversar com você, tá? E aqui ele já automaticamente iniciou isso pra gente, né? O Gateway Started via Dark Spaw e Gateway Running com esse PID aqui. Agora que já configurou o Telegram, a gente tem que mandar a mensagem pro nosso bot. Mas antes eu percebi um problema enquanto tava gravando o vídeo que era nesse pacote de instalação, às vezes ele não baixa alguns pacotes. E um pacote muito importante que ele não baixou dessa vez é um pacote de mensageria do Telegram.

**12:17** · Então vamos volar aqui no terminal rapidinho e a gente vai dar um clear só para limpar o terminal. Vamos rodar o seguinte comando. Pip install agent messaging. Tá também na descrição do vídeo, tá? Esse comando. Você pode só copiar colar ele. Beleza? E você vai rodar esse comando. Ele basicamente vai baixar aqui o pacote de mensageria do Herms para poder conectar o nosso gatway com o Telegram. Então vamos dar um clear aqui novamente, só para limpar o chat e vamos dar um herm gateway stop só pra gente terminar ele. E um gateway start, só pra gente ser rápido, tá? Para garantir que vai funcionar aqui o gateway é corretamente, certo?

**12:47** · E agora a gente vai voltar no Telegram, vamos voltar lá no nosso bot father e vai pesquisar pelo nome do nosso bot. Você pode copiar aqui, ir no search e colar o nome do bot e vai aparecer aqui esses chats. A primeira opção que aparecer, provavelmente já vai ser o seu bot. Você aperta nela e pronto, estamos no nosso bot. Para começar, vamos fazer aqui um teste simples. Vamos dar só um oi e pronto, ele respondeu aqui, né, até muito rápido, de como que ele pode me ajudar no dia de hoje. Então, rapaziada, terminamos aqui a integração do Telegram com o nosso Herment e uma PI totalmente de graça da Nvidia de IA, tá?

### Testando o bot no Telegram

**13:17** · Peço desculpas novamente pelo esse imprevisto que apareceu agora no meio do vídeo pra instalação de um pacote, tá? Mas ele é importante, como eu disse, eh, aqui no Armizagent documentation, ele tá ainda em early beta, então alguns problemas podem acontecer, tá? Caso aconteça algum outro problema, manda mensagem. Eu testei o ARM só com Discord, com Telegram até agora. Caso vocês outra coisa e não funcione, pode mandar mensagem, eu vou tentar responder ao longo da semana. Todos os passos estão na descrição desse vídeo documentados.

**13:42** · Você pode só copiar e colar e seguir, certo? Qualquer dúvida, qualquer problema, manda um comentário aqui no vídeo que eu vou tentar responder o mais breve possível. E basicamente esse foi o vídeo.