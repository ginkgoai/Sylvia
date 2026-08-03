---
title: "Animações SVG Podem Ficar Assim! (Sem biblioteca, sem GIF, só código)"
source: "https://www.youtube.com/watch?v=GG8tM9r5Wy4"
author:
  - "[[Gustavo Campelo - Desenvolvedor]]"
published: 2026-06-01
created: 2026-07-21
description: "⚡INSCREVA-SE PARA A NOVA ERA:https://gustavocampelo.com.br/a-nova-era-pagina/🚀 FORMAÇÕ DEV COMPLETA:https://webhubeducacao.com.br/comunidade-webhub/🔔 Inscreva-se no canal para mais dicas e rev"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=GG8tM9r5Wy4)

⚡INSCREVA-SE PARA A NOVA ERA:  
https://gustavocampelo.com.br/a-nova-era-pagina/  
  
🚀 FORMAÇÕ DEV COMPLETA:  
https://webhubeducacao.com.br/comunidade-webhub/  
  
🔔 Inscreva-se no canal para mais dicas e reviews!  
  
#programação #frontend #desenvolvimentoweb #html #css #javascript #desenvolvimento #design #webdesign #uidesign #uxdesign #uiux #layout #animation  
  
00:00 Introdução  
00:50 O que é um SVG?  
01:43 Criando um SVG  
03:47 Inserindo um SVG no código  
18:41 Conclusão

## Transcript

### Introdução

**0:00** · Você já viu sites com animações fluidas?

**0:02** · Às vezes um logotipo se preenchendo ou então alguns ícones animados sendo desenhados? Se sim, provavelmente você estava vendo o poder do SVG. E nesse vídeo aqui você vai aprender como criar SVGs e como animá-los, porque eles são extremamente leves, né? Eles não dependem de pixels, não são vídeos.

**0:21** · Basta a gente utilizar um pouquinho de código, vocês vão ver que é muito fácil.

**0:25** · Então eu peço para que você curta esse vídeo, se for útil para você, apoie o nosso canal, se inscreva, ative o sininho para que você não perca nenhum conteúdo, para que a gente possa continuar trazendo esse conteúdo gratuito de qualidade para você. A gente traz vídeos aqui quase todos os dias sobre design, programação, sobre inteligência artificial, mercado. Então não deixe de se inscrever e comentar também o que que você acha e pedir novos temas para que a gente esteja trazendo aqui, tá? Meu nome é Gustavo Campeiro e bora pro conteúdo, então. Então vamos lá. A gente pode começar falando o que é SVG de forma bem rápida. Mesmo se você já saiba, fique aqui. O SVG ele é uma conta matemática.

### O que é um SVG?

**0:58** · Ele é feito de código e não de pixels. Olha só, para que você entenda isso daqui, ó, vamos demonstrar.

**1:04** · Vamos lá para te mostrar isso aqui de forma fácil. Olha só, aqui na tela, do lado esquerdo, eu tenho um SVG, um arquivo vetorial, e do lado direito, eu tenho uma imagem normal composta por pixels. Qual que é a diferença? Quando a gente dá um zoom, a gente pode ver que ela é composta por pixels. Olha só. E se eu expandir muito essa imagem, ela vai ter distorção, certo? Diferentemente de um arquivo vetorial, como por exemplo um SVG, que quando a gente aproxima, você pode ver que não é determinado por pixels, mas sim é uma linha vetorial, realmente.

**1:34** · Então, o bom é que você pode aproximar o quanto você quiser, que ela nunca vai perder a qualidade. E ainda assim fica um elemento extremamente leve. Gustavo, mas como que eles podem ser criados? Bom, aí, ó, você pode vir em ferramentas de prototipação, como por exemplo o Figma, em ferramentas de ilustração, como Adobe Illustrator. E você pode pegar, por exemplo, a ferramenta caneta e aí você dá um clique em um lado. Você vem, por exemplo, vamos criar aqui juntos uma setinha. Olha só, para você ver como que é fácil. Dei um clique do outro lado, venho aqui, dou um clique.

### Criando um SVG

**2:04** · Agora, se eu quiser formar a outra perninha da seta, eu posso apertar ES, ó, para que ele deixe de fazer aqui o próximo ponto. Eu clico nesse pontinho aqui e ligo aqui embaixo. Ó lá, nós temos uma seta. Essa aqui não é uma aula de Figma, né? Mas a gente tem muito conteúdo sobre Figma no canal aqui se você quiser assistir também. Mas olha só, aqui, ó, nós temos um arquivo vetorial, tá vendo? É uma setinha. Então ele pode ser criado por caneta, por lápis, por formas geométricas também.

**2:29** · Você pode criar aqui, ó, um retângulo.

**2:32** · Você pode dar um stroke, tirar o plano de fundo e você cria qualquer elemento, qualquer ícone, qualquer logotipo que você quiser. E você pode animar partes independentes dele. Isso que é muito interessante. Outra forma também é você pesquisar em bibliotecas. A gente tem milhares delas, como por exemplo é o Flaticon. Então aqui, ó, nós temos ícones de interface. Todos esses ícones aqui você pode baixá-los SVG. Então, se você clicar aqui, ó, ó lá, tem o arquivo vetorial SVG.

**2:57** · Inclusive, né, se você vier aqui, ó, na parte da edição do ícone, clicar com o botão direito, vier em inspecionar, você pode ver todo o código da página. Se você vier aqui, ó, inspecionar esse elemento, você pode ver que ele é um arquivo vetorial, um SVG.

**3:11** · Olha só, VG. Arquivos SVG, eles são visíveis dessa forma. Você pode até clicar com o botão direito, vira aqui em copy copy element. Você cola no seu Figma e na sua ferramenta vetorial. E lá nós temos o nosso ícone. Olha só, você pode ver que ele é composto por um círculo aqui na parte superior. Olha só, você pode, ó, movê-lo como você quiser.

**3:31** · E você pode movê-lo como você quiser, tanto nessa parte aqui do Figma, na ferramenta vetorial, como também no código, porque no código você pode movimentar essas linhas do desenho desse vetor. Então ele pode sofrer qualquer transformação animada. Por isso que é muito bacana. Para que a gente possa ver isso na prática, bora inserir um SVG no código agora para que vocês possam ver.

### Inserindo um SVG no código

**3:52** · Bom, em vez de uma setinha, um quadrado, o que que a gente pode fazer? A gente pode fazer um carrinho bem charmoso, como esse daqui. Não fui eu que criei do zero, tá? Eu peguei de uma biblioteca e além de inserir ele um projeto para que vocês vejam na prática, eu também vou animá-lo. Então, a gente vai animar as rodas. Esse carro vai ficar girando.

**4:07** · Vocês vão ver como é algo muito fluido, né? É como se fosse um vídeo, né? Eu também vou fazer essa animação aqui. Eu tenho um texto, tá vendo? um texto qualquer. Eu vou exportar esse texto porque esse texto também é, ó, vetorial.

**4:19** · Eu vou inserir ele no nosso projeto como SVG e vou fazer uma animação bem bacaninha, como a gente tem aqui na Web Hubão, na página da comunidade Webub.

**4:27** · Olha só que página bonitinha. Quando a gente clica no menu, olha só, nós temos o nosso olá aqui, que é um texto também sendo desenhado. Vocês vão entender como fazer isso. Agora, então, como é que funciona? Vamos pegar aqui, ó, esse nosso grupamento. Tá vendo, ó? Ele é feito de vários vetorezinhos, ó. Aqui, ó, nós temos um retângulo, aqui nós temos um círculo. Então, eu vou pegar esse grupamento maior, que é a junção de todos esses nossos elementos. Eu posso vir aqui no Figma, ó, export e exportar como SVG. Ou eu posso até clicar com o botão direito, vir aqui copiar como SVG, tá?

**4:58** · Vamos copiar como SVG. eu vou inserir no nosso projeto, um projetinho HTML, mesmo que você não saiba muito, HTML, mas você pode inserir no seu projeto, sei lá, WordPress, Webflow, Framer, qualquer ferramenta aí. Aqui, ó, tô nesse projetinho aqui só de exemplo para nós. E aqui dentro da nossa div, né, de um bar e HTML, então dentro da estrutura da nossa página, como a gente já copiou esse SVG aqui, como vocês viram, agora eu vou colá-lo. Olha só, colei, ficou meio que uma zona. E lá nós já temos o nosso carrinho dentro aqui da página. Eu vou só organizar isso daqui, ó. Tá vendo?

**5:31** · Você pode ver, então, que o nosso SVG ele é o seguinte, ele é envolvido pela tag SVG, certo? E aqui a gente tem um widf e um height padrão, que é o mesmo, ele segue a mesma largura e altura que a gente copiou esse nosso SVG. Só que você pode setar essas configurações aqui mexendo no CSS, né?

**5:51** · Você pode setar um novo WIDF, um novo height no CSS para esse SVG, sem problema. E aí dentro desse SVG a gente tem o PEF. Que que seria o PEF? O PEF é como se fosse o desenho. Então o SVG é como se fosse a nossa folha e o PEF a gente vai desenhando um retângulo. A gente vai pegando igualzinho a caneta a gente fez criando a nossa setinha. E cada ponto desse daqui é como se fosse uma coordenada. Então é como se a gente pegasse o nosso lápis e movesse ele para essa posição, depois para essa posição até formar esse carro.

**6:22** · Então é um conjunto de vários PFs, né, de vários desenhos aqui. E aí, Gustavo, como é que funciona? Bom, se eu quiser animar somente essa roda, é só eu pegar o PEF que corresponde a esse desenho geométrico aqui da roda. Como que eu vou saber qual é o PEF, né? Aí que a gente se perde um pouquinho, mas bem tranquilo. Olha só, se você clicar com o botão direito na sua página, como a gente já falou, tem um inspecionar. E aí, ó, nesse Dev Tools aqui, né, utilizando o Google Chrome, eu vou até aumentar a tela para que vocês vejam melhor. Aqui, ó, eu posso clicar aqui e a gente vai selecionar lá. a roda.

**6:51** · Você pode ver que a gente consegue selecionar os elementos de forma independente, porque são independentes. Á, são vários PEFs. Então, se eu vier aqui, ó, e selecionar a rodinha, você pode ver, ó, que tem cada tracinho dessa roda. Tá vendo, ó? Cada tracinho preto. Que que eu vou fazer? Eu queria animar todos esses tracinhos pretos para que eles gerassem. Eu posso envolvê-los em um grupamento e aí eu animo esse grupamento para que eu não precise animá-los de forma independente. Cada tracinho vai ficar meio ruim. Então, como fazer isso?

**7:21** · Deixa eu dividir tela aqui. Eu vou pegar aqui, ó, esse tracinho, ó lá, esse PEF aqui, ó. Eu vou copiar esse M só para que eu encontre esse M aqui dentro, tá?

**7:30** · Então aí no seu código, vamos dar um contrtrl F. Eu vou colar. Ó lá, ó, esse M371, tá vendo? Que é esse nosso PEF aqui, ó. Ó lá, já encontrei. Então esse daqui é o PEF. Esse é o desenho do nosso traço. Você pode ver, ó, que ele tem um stroke, um stroke wiedh, ou seja, uma largura de stroke, né? como se eu tivesse vindo aqui, ó, e feito realmente várias retas, pegado a minha caneta, viesse aqui, ó, e fizesse uma reta dessa daqui, tá vendo, ó? E desse um stroke aqui de dois, ó lá. É exatamente isso.

**7:57** · E aqui, ó, nós temos esse tracinho, nós temos esse outro, esse outro, esse outro. Então, todos esses stroke do aqui, eu posso agrupá-los porque são os risquinhos da roda. Como que a gente cria um grupamento no SVG? Muito importante, você pode criar aqui, ó, com a tag G, tá? Então, se você, ó, abrir aqui a tag G e fechar, ele já vai fazer aqui pra gente. Essa tag G representa um grupamento do SVG. E agora eu posso pegar esses pefs aqui, ó, que simbolizam os risquinhos e eu colo div, desse grupamento G aqui.

**8:29** · Eu posso dar uma classe para ele, para que eu possa chamá-lo no CSS. Então, vou chamar de, por exemplo, roda. Vou até fechar aqui, ó, para que a gente possa ver o nosso carro maiorzinho. E agora no style CSS basta eu personalizar essa roda. Então, eu posso ver aqui, eu posso criar um animation para ele, uma animação, né?

**8:46** · Essa propriedade aqui serve para isso.

**8:48** · Eu posso colocar o nome que eu quiser para essa animação, como por exemplo, girar, né? Porque é isso que a roda faz, mas você pode colocar qualquer nome. Eu vou dar um tempo para ela acontecer, por exemplo, um segundo. Eu vou falar que vai ser um movimento linear, tá? Você pode escolher esse tipo de movimento.

**9:02** · Pode ser que ele vá começando, acelerando e depois freie, ou pode ser que ele seja linear, né? A mesma velocidade em todo movimento. Vou manter dessa forma. A partir do momento que a gente cria uma animação, a gente precisa criar os keyframes, que são as etapas dessa animação. Que que vai acontecer?

**9:17** · Se é uma animação, precisa acontecer alguma coisa. Então, como que a gente faz isso? Nós temos os keyframes aqui.

**9:24** · Aí eu vou pegar girar. Basicamente a animação funciona, ela vai de um ponto até outro ponto, então seria 0% até 100%, ou então é from, né? Então vem de um ponto e vai para outro ponto. Mesma coisa. Como o nosso ponto inicial é esse daqui mesmo, então eu nem preciso setar o 0%, porque o 0% já seria esse estado padrão aqui. Eu vou setar então só o final. Então posso colocar aqui, ó, o 100% ou então o to, né, ó. Se eu colocar 100% ou true aqui vai dar na mesma. Qual vai ser o 100%?

**9:56** · Bom, eu vou pegar aqui, ó, o nosso roda. Eu vou pegar aqui, ó, a propriedade de transform, que essa propriedade aqui a gente consegue fazer qualquer transformação, seja de movimentação de posição na horizontal, na vertical, ou seja, de rotação. Então eu vou dar aqui um rotate, ó, um rotate de 360º.

**10:20** · Opa, escrever errado aqui. Lá, ó. Você pode ver que você pode ver que ele deu um giro, ficou meio estranho. Vamos colocar isso daqui pr acontecer em loop.

**10:27** · Então a gente pode setar aqui o infinite. Vamos ver o que que vai acontecer. Ó lá, ó. Ele tá girando, só que ele não tá girando no seu próprio eixo. Então aqui a gente vai mais um aprendizado aí de como funciona o SVG.

**10:37** · Ele vai pegar o eixo padrão de todo o SVG, ou seja, o ponto central do carro.

**10:42** · E essa roda ela tá girando em volta desse eixo central do carro. Se eu quiser que ela entenda que o limite dessa nossa animação, a referência vai ser o próprio corpo dessa roda, né, e não o corpo total do SVG, a gente precisa, ó, setar aqui a propriedade transform transform box e a gente vai colocar fi box. Ou seja, agora, ó lá, ele vai entender que a referência é realmente a roda, só que ele tá colocando o ponto de origem na parte superior esquerda. Esse é o padrão. Não quero.

**11:14** · Eu quero que a origem seja no centro dessa roda. Então aí é só a gente mexer no transform Origin.

**11:21** · Transform Orange. E aí eu seto center.

**11:24** · Vamos ver o que que vai acontecer. Lá nó já temos a nossa rodinha gerando. Tá vendo como que é muito fácil? Você poderia aumentar o tamanho dessa roda utilizando o scale. Você poderia diminuir, você poderia mexer, como a gente já falou, ó, para que ela mudasse de posição dessa forma. Uma hora ela fica assim, depois ela cresce, depois ela faz assim. Você pode mexer no que você quiser. Inclusive, você pode vincular isso daqui à rolagem da página.

**11:46** · Conforme você rola a página, ela vai girando. Aí você pode fazer isso utilizando JavaScript. Se vocês quiserem que eu traga mais vídeos, às vezes alguma coisa específica, comentem aí. E agora, Gustavo, como que a gente faz isso na outra roda? Bom, agora é só a gente replicar, né? Clicaria com o botão direito, veria, ó, qual que é esse PEF aqui, ó. Vou copiar, vou encontrar aqui, ó. Tá vendo? Stroke 2, tal. Isso daqui se refere à outra roda. Vou criar mais um grupamento. E agora vou colar esses pefs aqui nesse grupamento. E vou dar classe dele também de roda. Vamos ver se vai funcionar.

**12:17** · Lá, nós já temos as duas rodas gerando. Vamos animar agora o nosso texto como se ele fosse desenhado.

**12:23** · Mas antes, meu nobre, olha só. Você tá vendo esse projeto do Thor aqui, esse projeto bonitinho, cara? Você quer aprender a criar projetos como esse daqui, utilizando inteligência artificial de forma realmente profissional, né? unindo ela o processo criativo, ao design, ao desenvolvimento.

**12:36** · Olha só, criando essas animações aqui, ó, com a rolagem da página, com esse elemento 3D interativo.

**12:44** · Se você quiser criar esse projeto do zero aqui junto comigo, nós temos o nosso novo treinamento que é o projeto Tor à Nova Era. A gente vai criar juntos do zero esse projeto aqui. Você vai entender como usar IA de ponta a ponta do design à programação. E você vai entender também sobre design e programação, animações, não só para que você crie esse projeto, mas qualquer outro também projetos de alto nível. E também a gente fala sobre o mercado ainda para que você consiga os seus primeiros clientes e seja bem remunerado na área, tá?

**13:12** · Então, se você quiser, mesmo que você ainda não tenha nenhum conhecimento técnico, a gente ensina tudo do básico. O link vai tá aqui na descrição do vídeo para que você faça a sua inscrição, tá? É, a gente não sabe até quando a gente vai ter esse treinamento aqui. Às vezes a gente muda as coisas na empresa, abre um outro treinamento, a gente para algum projeto.

**13:33** · Então, participe, aproveite isso daí, tá? Não procrashine, porque como eu falei, a gente não sabe até quando ele vai est disponível aí, tá? E é um preço também super bacana. Qualquer dúvida você pode chamar a gente no WhatsApp também. Projetinho aqui ficou top e responsivo. Voltando aqui, então vamos agora pegar o nosso texto. Você poderia criar qualquer texto aí. E agora se a gente clicar aqui da mesma forma que a gente tinha feito no carro, clica com o botão direito, vem aqui em copiar.

**14:00** · Copiar como SVG. Agora a gente vai colar aqui no nosso projeto. Eu posso até, ó, fechar esse SVG aqui do carro. Eu vou colar em cima. Ó lá. O texto vai ser a mesma coisa. Ele tem a tag SVG na parte superior, um wef e um height padrão. E tem também o PEF. A diferença é que ele tem um PEF único, que é essa movimentação aqui, ó, essas coordenadas para formar esse texto bonitinho. Como que funciona? Olha só, agora vai um novo ensinamento aí para vocês. Então, eu posso vir aqui nesse SVG, ó, e dar uma classe de texto, só para que a gente pega essa referência aqui lá no CSS.

**14:33** · Agora aqui no CSS, vamos lá. Vou mexer agora com o nosso texto. Uma propriedade legal do SVG também é o fio, porque com o fio você pode mudar a cor. Não é porque você insere um texto ou um carro vermelho que ele precisa se manter vermelho. Você pode mudar a cor de cada elemento desse SVG. Por exemplo, se você mexer aqui no fio, aqui eu tô mexendo no nosso SVG de forma geral. Eu vou colocar, por exemplo, vermelho também para combinar com o carro. Não mudou nada, Gustavo. É porque aqui eu tô chamando o SVG, né? Eu tenho sempre chamar o PEF. Ó lá, chamei o PEF, você pode ver que já funcionou.

**15:05** · Uma outra coisa bacana, olha só que vai ficando mais interessante. Se eu deixar isso aqui, ó, transparente levemente, que que vai acontecer? Ó lá, levemente transparente. A gente tem um outro camarada que é o stroke. Eu posso, por exemplo, dar um stroke aqui de vermelho.

**15:20** · Vamos ver isso aqui. Lá já deu um stroke vermelho. Você pode controlar a largura desse stroke, né? peso. Se você quiser aqui com stroke widif, se você colocar quatro pixels, vai ficar um stroke muito grossão. Eu vou manter esse padrão aqui.

**15:33** · E tem uma brincadeirinha legal que é o quê? Você pode segmentar esse stroke, esse traçado, como se fosse uma linha tracejada. Como que você faz isso? Com stroke dash array, né? Então vai ser um array, né? Um grupamento de traçados, né? Porque a gente vai segmentar esse traçado. Olha só, se você colocar, sei lá, três, ó. Lá, ó. Tá vendo que ficou tracejadinho? Ou seja, você criou strokes de três pixels. Por isso que são vários strokes de três pixels.

**16:03** · E se você for aumentando isso daqui, por exemplo, colocando 100, você vai criar um strokes de 100 pixel. Se você movimentar isso até que pegue o tamanho completo do seu elemento, vamos ver quanto que seria isso. Se eu colocar 200, ó lá, ó, você pode ver que ele já vai preenchendo mais. 400. 400 já ficou completo. E agora tem um outro camaradinha que você pode mexer aqui, ó, que é o stroke dash offset, que é como se fosse você empurrar esse tracejado mais pra frente. Então você tem o seu traço aqui. Então vamos supor, você tem aí a sua linha dessa forma aqui, ó.

**16:33** · E aí você pode vir aqui até no Figma, você consegue fazer isso. Em vez de sólido, você coloca dash tá vendo? Esse offset seria mais ou menos esse gap aqui, ó, onde você pode movimentar o seu stroke, tá vendo? Ó lá. Aqui, ó, o dash seria o tamanho desse traçado. Ó lá, se você colocar um pixel, vai ficar dessa forma.

**16:54** · Só que também você pode movimentar.

**16:56** · Então aqui, ó, você pode ver que começando no meio pixel, mas se você movimentasse e aqui no Figma, eu acho que a gente não tem essa opção. Aqui seria o gap, né? Só esse espaçamento entre cada traçado. O offset seria realmente você movimentar esse traçado ou mais pra frente ou mais para trás.

**17:12** · Então, se eu vi aqui, por exemplo, e setar 100, eu vou jogar 100 pixels paraa frente. Esse nosso traçado, você pode ver aqui em algumas partes, ele até já tá sem o traçado. Se você movimentar 400, o que que vai acontecer? Antes você tinha um traçado que pegava o nosso elemento completo e agora você jogou ele completamente para fora. Então, ficou tudo sem. E agora a mágica é o quê? Você pode criar mais uma animação que vai voltar a esse traçado. Então esse traçado vai vir como se fosse desenhando o seu formato geométrico. Quer ver? Eu vou dar aqui, ó, mais uma vez um animation, por exemplo, desenhar.

**17:43** · Vou dar um tempo também de 2 segundos linear. Agora aqui vamos definir os keyframes dessa animação desenhar. Vamos lá. Não preciso definir o 0%. Basta eu definir o 100% que vai ser o quê? A gente vai pegar o stroke dash offset e eu vou colocar ele agora zero. Então o que que vai fazer aqui, ó? Não, não tinha ido, mas eu atualizei a página que ele foi. Olha só, tá vendo que ele está sendo desenhado, só que depois ele volta pro seu estado padrão. Se você quiser que alguma animação aconteça, essa não é uma aula sobre keyframes, né?

**18:15** · Se vocês quiserem, a gente pode trazer. Mas se você quiser que alguma animação aconteça e ela permaneça no seu estado final, você coloca aqui o forwards dessa forma.

**18:25** · Ó lá, ele, ó, será animado, ele se manterá dessa forma. E você personaliza isso daqui como você quiser. Se você quiser também, você pode, ó, dar um preenchimento final também de red.

**18:37** · Então, além de ir sendo desenhado, ele também vai sendo preenchido. E aí, o que que você achou? Você gostou? Pô, se sim, eu peço, por favor, curta o vídeo, comenta o que que você acha. Não deixe de se inscrever no canal para que você não perca nenhum conteúdo de qualidade e gratuito. Participe também do projeto Tor junto conosco aí para que você se torne um desenvolvedor de sucesso nessa nova era do mercado aí com a inteligência artificial. Muito obrigado por você ter assistido e até a próxima.

### Conclusão

**19:02** · Yeah.