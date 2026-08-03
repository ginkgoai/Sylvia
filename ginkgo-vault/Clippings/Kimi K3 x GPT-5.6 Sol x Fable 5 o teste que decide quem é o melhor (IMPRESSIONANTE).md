---
title: "Kimi K3 x GPT-5.6 Sol x Fable 5: o teste que decide quem é o melhor (IMPRESSIONANTE)"
source: "https://www.youtube.com/watch?v=AWKCVvT9hpM"
author:
  - "[[Matheus Battisti - Hora de Codar]]"
published: 2026-07-18
created: 2026-07-18
description: "Kimi K3 vs GPT 5.6 Sol vs Fable 5, quem vence? Coloquei os 3 modelos para brigar em um projeto absurdo de e-commerce, o resultado surpreendeu...🔴 Formação Vibe Coding (Antigravity, Claude Code e +)"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=AWKCVvT9hpM)

Kimi K3 vs GPT 5.6 Sol vs Fable 5, quem vence? Coloquei os 3 modelos para brigar em um projeto absurdo de e-commerce, o resultado surpreendeu...  
  
🔴 Formação Vibe Coding (Antigravity, Claude Code e +): https://app.horadecodar.com.br/lp/formacao-vibe-coding?utm\_source=yt\_k3solfable  
  
🟪 Hospedagem que eu indico: https://www.hostinger.com/matheushoradecodar (use o cupom HORADECODAR para ter +10% de desconto)  
  
💳 Sistema de pagamentos que eu indico: https://appmax.com.br/desenvolvedores/?utm\_source=hora-de-codar&utm\_medium=social&utm\_campaign=influencer-tech (Pix com taxa zero via API)  
  
📘 Guia Engenharia de Prompt: https://app.horadecodar.com.br/ebookpages/guia-engenharia-de-prompt  
  
Entre no nosso servidor de Discord e me siga nas redes:  
  
🟣 Discord Hora de Codar: https://discord.gg/Veq4mvsWwk  
🔴 Instagram: https://www.instagram.com/horadecodar/  
  
🎁 PROMOÇÕES DA KIMI API (as duas acumulam!)  
  
▸ Bônus de recarga nos créditos do K3 (válido até 12/08):  
http://kimi.com/code?utm\_campaign=TR\_smf0JcBp&utm\_content=&utm\_medium=Youtube&utm\_source=CH\_kEMBez3l&utm\_term=  
  
▸ +10% de bônus na primeira compra pra contas novas (válido até 30/09):  
https://platform.kimi.ai?track\_id=track-b65bd32c3e20444fa986c8e28ef428e1  
  
TIMESTAMPS  
  
00:00 Qual modelo é melhor? Kimi K3, Fable 5 ou GPT 5.6 Sol?  
00:40 Critérios de avaliações dos modelos (versões e effort)  
06:45 Comparativo de Recursos de cada modelo (Kimi K3, GPT 5.6 Sol e Fable)  
18:28 Primeiro prompt para criação do e-commerce (análise de design)  
26:55 Verificando como ficou a home page de cada projeto  
30:10 Segundo prompt para fluxo de compra do usuário (carrinho, checkout e sucesso)  
34:20 Testando fluxo de compra no Kimi K3, Fable 5 e GPT 5.6 Sol  
40:06 Terceiro prompt para visão administrativa (pedidos, dashboard)  
42:25 Testando área admin e dashboard  
47:25 Testando o jogo criado pelas IAs Kimi K3, Fable 5 e GPT 5.6 Sol  
52:55 Considerações finais sobre os três modelos

## Transcript

### Qual modelo é melhor? Kimi K3, Fable 5 ou GPT 5.6 Sol?

**0:00** · Química 3 versus GPT 5.6 Sol versus Fable 5. Hoje é dia de guerra. Rinha de LLMs modelos Frontier. A gente vai criar dois projetos e ver qual modelo se sai melhor. Sem passar pano. Aqui não tem fanby. A gente só quer os nossos projetos feitos da maneira certa, gastando o menos possível. Bora lá.

**0:24** · Te convido a ficar até o fim desse vídeo que vai ter muita coisa bacana, muita surpresa e briga, guerra de ar de verdade. Chega aí, sem enrolação. Bora definir os critérios. Bom, galera, primeiramente deixa eu explicar para vocês como é que vai funcionar. Química 3 no high, tá? Todos os modelos vão estar no high, né?

### Critérios de avaliações dos modelos (versões e effort)

**0:46** · Então, química 3 no high, Fable 5 no high também, né? de effort e o nosso o GPT 5.6 Sol no effort high também todos no modo iolo, né, com acesso completo e ignorar ignorar permissões, né? Então eles não vão perguntar nada, eles só vão receber o prompt e vão criar os sistemas. Primeiro sistema que a gente vai criar aqui vai ser o e-commerce. Desafio bem interessante. Vou trabalhar vários critérios. Primeiro, design.

**1:16** · Então a gente vai ver qual que vai criar a melhor homepage e o scaffolding também.

**1:22** · Vamos comparar um pouco o tempo de que leva para cada um criar. Depois fluxo de compra, home, página de produto, carrinho, checkout, parte de obrigados, né? O fluxo comum de projeto de e-commerce. Vamos ver qual que cria esse fluxo de uma maneira mais detalhista, de uma maneira mais envolvente pro usuário.

**1:42** · Vamos ver se o layout também fica padrão, se fica claro pro usuário fazer essa compra, se ele consegue fazer.

**1:49** · Terceiro, uma área admin, ou seja, para quem comanda o e-commerce, vê ali como é que estão os pedidos, essas coisas e criar produtos, categorias, essas três etapas, cada uma num prompt só, tá? E nosso segundo projeto, que eu vou começar primeiro porque vai demorar mais aqui o prompt, né, mas eu vou analisar ele depois, já que ele vai ser entregue depois, provavelmente também. É um jogo estilo Headad Redemption, tá?

**2:14** · Então a ideia é criar um jogo 3D ali com o próprio one shot e ver quem sai melhor e entrega com melhor qualidade esse jogo. Beleza? Então, preparei também uma análise comparativa que eu vou fazer antes com vocês para que a gente possa ver o que cada modelo tem a oferecer. E aí ao longo do vídeo a gente vai criando os projetos, vendo o jogo no final. E é isso, vai ser longo. Tô começando de dia e talvez vou terminar à noite aqui.

**2:38** · E galera, claro, antes de começar, de fato, esse vídeo é um oferecimento da formação Vibe Coding, o meu treinamento mais completo aí quando se trata de programação com IA. Como a gente tá falando de vários modelos, lá tu vai encontrar também várias ferramentas de código diferente. O link vai tá aqui no comentário fixado para tu conhecer. É acesso vitalístico, galera. tá com um preço muito interessante pelo conteúdo e o valor que vai agregar para vocês. Tem de tudo mesmo, Antigraphic, Cloud Code, tem Codex e outras tecnologias aqui.

**3:10** · Tu vai conseguir aprender e criar vários projetos. Tem mais de 20 projetos do zero, do planejamento até o deploy. Tu vai entender como é que eu penso, como é que eu crio e desenvolvo nessas ferramentas, né? Independente se tu usa uma ou outra, é interessante aprender como eu crio os meus projetos, né? Não só falando da ferramenta em si. E tu ainda vai prender outras ferramentas no processo, né?

**3:33** · Não tô falando só das ferramentas de a, mas tudo que leva a gente a criar uma aplicação que vai estar no ar, que vai receber usuários, que vai monetizar em cima. Então cara, confere aí que isso aqui é o ouro do ouro. Então, acabando a área dos patrocinadores, vamos voltar aqui ao prompt inicial. Vou começar com o Kim aqui, tá? Vou colocar o mesmo prompt nos três. Esse aqui é o do jogo. Já vou explicar como ele funciona, né?

**4:02** · Como esse prompt aqui foi construído, ó, os três estão com o mesmo prompt.

**4:15** · Vamos ver se já tá rodando.

**4:17** · Já começou aqui, tá?

**4:21** · Vou ver o sol já começou também.

**4:26** · E o Fable. Então vou ler aqui o prompt, tá? Então olha só. Cria um jogo 3D completo, mundo aberto no estilo velho oeste em terceira pessoa jogável no navegador usando a biblioteca 3D consolidada. Provavelmente vai usar 3DS, uma biblioteca bem interessante. Cria o projeto do zero em uma pasta nova chamada Poeira Alta, né, o nome do jogo, totalmente separado de qualquer outro projeto. Todos os personagens, nomes, lugares, elementos visuais devem ser 100% originais. Nenhuma referência a jogos, marcas ou personagens existentes.

**4:55** · Isso é um one shot. Leia tudo antes de começar. Caprich em cada detalhe e não deixe nenhum item de fora porque não haverá segunda chance de ajustar. Ó, então o jogo poeira alta, né? Aí eu botei com o personagem principal o Jonas Prata, um pistoleiro que chega na cidadezinha de Vila Seca para acertar as contas com o bando do coronel Barbosa e dormir na região. Aí vai ter uma tela inicial. Escrevi como é que ela vai funcionar no jogo continuar. Minuto de pausa, tela de morte, salvamento automático.

**5:24** · Falei um pouco do mundo, aberto, compacto, denso, cercado por canons que delimitam o mapa naturalmente.

**5:32** · Expliquei um pouco da vila seca, como é que funciona ao redor, as trilhas de terra, o ciclo de dia, poeira levantando ao galopar, NPCs da cidade com rotina simples. Então, a promessa é grande.

**5:46** · Vamos ver se vai cumprir, né?

**5:48** · O personagem terceira pessoa porque orbital, né? Pode girar ela, andar, correr, pular, esquivar. O cavalo, sobe ar para chamar o cavalo, montar e desmontar, trote, galope, o combate, revólver com seis balas, tambor aí, mira ao segurar o botão direito, tiro na cabeça causa dano crítico. Expliquei como é que funciona o combate aqui, né?

**6:08** · Dei algumas missões, tá? Expliquei um pouco de economia e itens, dinheiro ganho por missão, loja geral vendendo balas. expliquei um pouco da interface, tá? Áudio, desempenho, né, para rodar o a 60 fps. Então, olha só, o projeto ambicioso one shot. Vamos ver até onde é que cada uma delas vai, tá? Tá todo mundo começando aqui o poeira alta.

**6:34** · E agora quero convidar vocês, antes de a gente começar o e-commerce, que vai provavelmente desenvolver bem mais rápido, a ver o que cada um dos modelos tem ali no seu core, né, dentro deles mesmo.

### Comparativo de Recursos de cada modelo (Kimi K3, GPT 5.6 Sol e Fable)

**6:47** · Para isso, galera, eu fiz o meu slide bonitão aqui. Eh, muita gente gostou ali de como ele tá sendo feito. É uma skill, né, que tá rodando no cloud. Se vocês tiverem interesse, comentem aí que eu posso pensar em fazer uma aula sobre isso, tá? Não serve só para slide, serve para outras coisas também. Então vou ter aqui, né, os três comparativos, o preço ali do valor da PI. Então a gente já viu uma discrepância muito grande aqui que o Kim, né, ele ganha nisso, né, ele é mais barato.

**7:15** · Então eu comentei até no vídeo de lançamento do Kim que eu fiz na quinta-feira, que quem sabe um modelo que entrega um pouco menos, mas é muito mais barato, é melhor do que um modelo muito mais caro que entrega legal, né? Então vamos lá. Os três competidores, três lançamentos em cinco semanas. O topo da tabela nunca girou tão rápido, né? Então, a gente teve aqui uma coisa bem legal que lá no LM Arena tinha gente testando o modelo do Kim sem saber que era o Kim, né, o K3, comparando com GPT 5.6, Sol e Fable 5.

**7:49** · Por isso que eu trouxe essa comparação, tá? Porque eu acredito que esteja perto, tá? Como eu falei no vídeo lá do Kim, não acho que tá igual, mas cara, tá chegando. Isso é muito bom porque é um modelo de código aberto, barato. Então fiquem atentos. Bom, o lançamento foi dia 16, quando eu lancei o vídeo, né? O desafiante é aberto, né? Então ele tem openweights.

**8:10** · Eh, ele tem 2.5 trilhões de parâmetros, foi o que reportaram lá. Eh, o Openweight multimodal, aceita vários tipos de arquivos, né? Já o sol, ele foi lançado dia 9 de julho. Ele é o topo da família de modelos dessa versão, né, que foi lançado Sol, Terra e Luna. E o foco declarado em coding multietapas. O Kim da Moon Shot também foi declarado como coding, tá?

**8:33** · Então a gente tem muito essas empresas focando em programação, galera, o que é bem legal porque avança as entregas que eles têm para com a gente, né? Então aqui, ó, Cloud Fable 5 foi lançado dia 9 de junho, né? Então pouquinho antes de todos, teve todo aquele negócio, né? O o Sol também teve de ser proibido ali pelo governo dos Estados Unidos e depois solto, né?

**9:00** · novamente, como o Sol também, né? E ele representa class mitos que tem o foco em cybersegurança, né? Porque eles descreveram, mas é um modelo acima do Opus, né? Uma classe acima do Opus e consequentemente também entrega coding, né? Programação melhor. Aqui uma breve ficha técnica, o lançamento dos modelos eh em cinco semanas, como eu falei, né?

**9:22** · Um mês praticamente ali. O contexto 1 milhão de tokens, todo muito parecido.

**9:27** · GPT Sol ganha, né? um pouco mais de tokens no contexto, né? Isso é quanto a IA consegue absorver para lidar com aquele conteúdo e aí eh formar uma resposta com base em todo esse contexto que ela agregou nesses tokens, tá?

**9:43** · Preço, como eu comentei no começo, o Kim ele ganha, tá? O Kim ele é nativo multimoldal, então aceita texto, imagem, arquivos, ele vai conseguir interpretar isso. O GPT 5.6 Sol texto e imagem e o Fable texto, imagem e arquivos também, tá? Esses arquivos que eu coloco aqui, não que o Sol não entenda arquivos, né?

**10:06** · Você pode colocar um PDF lá, ele vai ler. São outros tipos de arquivos mais variados assim que o modelo absorve além de texto, arquivos de texto, né, e imagens, tá? Pesos abertos, então os outros são fechados, né, de empresas que eh tão desenvolvendo o produto de forma isolada, sem trabalhar com a comunidade, diferente do Kim, né? Todo seu tem seu agente de coding. Eu tô usando os três inclusive ali para desenvolver cada um dos projetos, pra gente não ter problema de hardness.

**10:38** · Kim com Kim Code, GPT com Codex e Cloud Antropic com Cloud Code, tá? Contexto, como eu falei ali, a gente tem o GPT só ganhando, mas não é aquela diferença toda, né? Então a gente pode esperar ali que os três aceitem muito contexto e saibam lidar com isso. Que que é contexto? Uma code base inteira, né? Um projeto todo ali num prompt. Ele pode ler isso. Não que vai ser bom, né, galera?

**11:08** · Já expliquei que isso pode eh gerar muitos custos se for usado da maneira errada, né? Então não necessariamente é legal fazer isso. Ou um edital de 150 páginas num promp só.

**11:19** · Pegadinha do sol, né? Então, olha só, acima desses tokens de contexto, a requisição inteira é cobrada de duas vezes a 1 e meia na saída. Então, já temos aqui um aumento de custo, né, natural cobrado pela empresa porque tá usando mais tokens. Valor, isso aqui importa muito, né, galera?

**11:39** · Como eu venho sempre comentando, se um modelo entrega, sei lá, nota 8 de 10 e ele é metade do preço de um que entrega 9 de 10 ou 10 de 10, talvez o que custe metade seja mais interessante para muita gente, né? Então eu boto aqui o K3 custa 1/3 do Fable 5 e 60% do Sol no nos tokens de entrada, né?

**12:05** · A gente vê aqui o comparativo e vê que realmente o Feber é bem puxado. E se os três entregassem igual, obviamente a gente iria pelo Kim, né? Mas vamos dizer assim que o Kim não tá nem na jogada, né? A gente fez o teste ali, não dá nem para considerar, cara. Então o Sol pode se tornar uma opção viável. A gente já fez a comparação aqui do Sol e do Fable. O sol saiu melhor, né? Então Fable não tá muito bem na fita.

**12:33** · Lembrando, galera, todos esses dados aqui são dados públicos, né, que eu fui encontrando ali no launch, né, do no paper, vamos dizer assim, de cada uma da dos modelos que lançaram, né, e trouxe aqui condensado para vocês, tá? Eu botei aqui um cenário real, que é algo legal de analisar. Por exemplo, se a gente mandasse um documento gigante com 500.000 tokens de entrada e 20.000 tokens de saída, né? A resposta de outputs, essa análise em cada um desses modelos aqui sairia esse valor.

**13:00** · Então a gente vê que o kim realmente seria muito menos e o sol quase empata com o Fable porque passou daquela barreira ali que aumenta o preço, né? Então a gente tem que tomar cuidado com isso também. Aí na parte de código, né? Como eu falei, todos eles têm uma tendência forte a isso, né? Eu acho que é pelo vibe, é pelo hype \[roncando\] do Vibe Code, né? Então todos se declaram o melhor em codic, né? Lan aqueles benchmarks lá que sempre estão na frente e tal. Na verdade, o time não é tanto assim, né?

**13:29** · Mas ele fala que tá focando nisso, ele tem recursos que trabalham com isso, né? Então ele tende a ter especialidades que os outros não têm. Mas é interessante esse foco na parte de programação. Então o Kim ele aposta em navegação de repositório grande, debug com logs e testes, long horizon, né? Tarefas longas.

**13:52** · Ele eles acreditam, né, que o modelo vai melhor. Já o Sol posicionamento oficial é forte em code multietapas e tarefas de linha de comando. É o motor do Codex e herda o ecossistema de turing mais adotado do mercado. Fable 5 antrópico, coloca como estado da arte, engenharia de software na programação, feito para tarefas longas e autônomas, onde outros modelos precisam de checking constante.

**14:14** · Então, vejam aqui todos eles indo para esse lado. Multimodalidade, né, galera?

**14:21** · a gente já falou, né, a habilidade do modelo de aceitar diferentes tipos de arquivos. E uma coisa interessante que eles citam aqui é que o modelo do Kim ele foi treinado nativo com imagem.

**14:32** · Então, desde o começo já tinha ali que eles queriam desenvolver a imagem no treinamento da IA. Já os outros, se vocês acham acompanharam na evolução do GPT e do Cláudio, eles não aceitavam logo de cara ali, eh, imagens, por exemplo, eles não sabiam ler. Isso tende a parecer que é algo acoplado ao modelo, né? Não foi algo natural que surgiu, algo natural. Então, teoricamente, o que me sairia na frente nesse quesito, né, de multimodalidade, aceitar tipos diferentes de arquivos. E o GPT 5.6 e o Febes não falam muito disso, né?

**15:03** · Apesar de citarem, né? Já o Kim ele trabalha com essa com esse argumento, né? Falando disso e ainda tem essa questão de geração de 3D que a gente comentou lá no lançamento, que ficou bem legal, pelo menos os exemplos que eles mostraram, né? ecossistema agênico, o me também traz muito forte isso. Tem a parte ali do do client de code, né, que é o Kim Code, tipo um e um cloud code, tipo um open code, agent, que quando lançou deu muito burburinho, né?

**15:31** · Vários agentes trabalhando de forma paralela num projeto só, Kimclaw, tipo Open Cloud.

**15:37** · Então, claro, eles aproveitaram coisas que deram certo de outras empresas e colocaram aqui. Então, a gente vê também que eles estão evoluindo não só a IA, mas vários produtos juntos. Já o GPT tem o Codex, o response API e também várias outras questões menores, né, que se tornaram padrão de mercado, né, que a gente não vê tanto, por isso que eu falo menor, mas, por exemplo, padrão de API de integração, né?

**16:03** · Antigamente a gente via muito eles usando os pacotes base da Open AI para conectar na API e só mudando ali o modelo, né? Então o motor era da Open AI e modelo era de outra empresa. Isso porque eles fizeram bem feito essa parte de integração a sistemas de a, né, com um pacote aberto que pode ser reutilizado para outras empresas.

**16:27** · Já o Cloud, né, tem o Cloud Core que virou referência em agente de código terminal, né? Acredito que a maioria, pelo menos no ambiente corporativo, prefere o cloud code, né? Usa mais até pelo ter o dinheiro para pagar, né? Aí tem o cork, o GPT criou recentemente também o cowork deles, né? E a gente tem, né, essa ação dessas empresas por esse lado, eu vou dizer mais tímido assim, porque a gente não conhece muito o Kim, né?

**16:54** · Não sei se vocês acompanham, mas se tu olha ali para o sistema deles, tu vê algo bem amplo lá também acontecendo. E galera, letras miúdas, né, coisas pra gente ficar atento.

**17:04** · Química 3, self host, né, a gente pode ter acesso ao modelo para rodar na nossa máquina, mas no lançamento ainda sem model card oficial e sem licença confirmada. Isso pode ser o problema para quem usar o modelo pra sua empresa, por exemplo, eles vão lá e colocam uma licença meio esquisita, né? GPT tem aquele negócio ali de aumentar os tokens no contexto e tu pagar uma grana muito a mais e ficar sem saber o que aconteceu.

**17:27** · E o Fable 5, a questão de retenção obrigatória de dados por 30 dias, que para alguns setores, para algumas empresas, é critério eliminatório, né?

**17:36** · Nem vai deixar entrar o modelo por ter esse probleminha, tá? Aqui eu trouxe um diagrama, né, todos esquisitos, mostrando o que cada um tem de melhor.

**17:46** · Então, se a gente falasse de ecossistema, provavelmente o GPT é mais evoluído. Se a gente falasse de código, provavelmente o cloud Code é mais evoluído. Questão de custo benefício, Kim tá ganhando ali, pelo menos no preço, né? Se a gente ver a qualidade de fato dos projetos gerados, ele tá ganhando sim. Abertura nenhum deles é aberto, né? Então a gente tem o Kim também despontando e com texto na prática, pelo que foi liberado, o Kim trabalha melhor, tá? Mas isso a gente vai ver logo logo nos projetos também, porque o resultado vai aparecer.

**18:15** · Dito isso, galera, feita essa introdução longa aí, mas que é importante pra gente tomar a decisão porque tá envolvendo o nosso dinheiro, né? Bora lá pra prática, vamos ver o que cada um dos modelos tem a entregar. Bom, aqui, galera, só para dar um feedback do modelo, de cada modelo para vocês sobre o poeira alta, né? Os três já começaram aqui a criação, já tem pastinha, já tem arquivo aqui no Kim, né? Já tem o jogo completo aqui no Codex, né? No GPT 5.6, tá?

### Primeiro prompt para criação do e-commerce (análise de design)

**18:47** · Eu não vou abrir agora, vou deixar para depois, né? Mas já tem. E aqui ele colocou, né? Limitações e fidelidade.

**18:53** · Montar de montar transições, scuteras de POS. Vamos ver.

**18:57** · Os diálogos aparecem em panel estilizado, não corado espinicamente. Aí a usa decisões individuais de cobertura de avanço, tá? Algumas coisas que não são tão importantes, mas estão aqui, né?

**19:07** · Vamos ver o que acontece depois na prática. E o Fable segue trabalhando ainda, né? Lembrando, o GPT ele terminou o jogo em 10 minutos, galera. Febo tá trabalhando a 20, tá? E o Kim não tem como controlar ali porque eles não tem o timerinho, mas eu vou falando para vocês como vai ali indo cada um dos projetos.

**19:26** · Agora vamos lá pro e-commerce, né? Vou ter que abrir aqui os novas avas pra gente poder trabalhar nesse outro projeto em paralelo enquanto desenvolve esse aqui. Bom, só para vocês revisarem, então, Kim K3 no high. Só vou botar o iolo aqui rapidão.

**19:43** · Vou colocar o prompt GPT Sol também no high. Acesso completo, já tá tudo certo. Colocar o prompt e fable 5 também no high. Colocar o prompt. Então vou ler aqui o prompt do e-commerce. Então vou ter crie um sistema web completo de e-commerce usando next com temp. Mas te domina, galera. Então é interessante começar por isso porque a gente já vai ter erros minimizados e provavelmente você vai escolher uma stack comum, né, para não ter muitos problemas.

**20:14** · Aqui o projeto do zero, uma pasta nova chamada loja pisada. totalmente separado de qualquer outro projeto. Esse é o início de um produto real que vai crescer nas próximas etapas, né? Porque eu vou fazer os outros prompts, fluxo de compra completo e painel administrativo. Então, estruture como um sistema de verdade desde o começo, não como uma página vulsa. A marca pisada é uma loja brasileira de tênis streetware, público 18 a 30 anos, urbano, ligado à cultura de rua, música e moda.

**20:38** · Então, expliquei como é que é a marca para poder dar a cara do design, porque esse meu primeiro critério aqui é o quê? a gente trabalhar no scaffolding, que é a criação de pastas e arquivos ali iniciais de projeto e também o design da homepage e do restante da loja, né? Mas ele vai dar o início aqui. Base produtos, pelo menos 16 produtos fictícios distribuíd entre as categorias, tênis, camisetas e acessórios. Cada produto tem nome próprio. Eh, cada produto tem nome próprio com personalidades.

**21:07** · Lug, descrição a duas e três frases, preço, preço promocional em pelo menos cinco desses. As imagens do produtos devem ser geradas dentro do próprio projeto.

**21:17** · Então aqui, galera, alguns modelos não geram imagens. Aliás, alguns modelos não, né? O cloud em si não gera, os outros deve deveriam gerar. Então, a gente pode ter aqui um ganho dos outros nesta parte. E dá a diferença, tá? Lá no vídeo que eu fiz do Fable versus GPT 5.6, a imagem deu a cara do projeto.

**21:39** · Inclusive, dá uma olhada no vídeo lá depois, hein? Homepage, explicar como é que ela deve ser. Barra de anúncio no topo, header fixo com logo um hero, né, que é um banner, faixa de benefícios, vitrin de lançamentos, sessão de categorias, vitrine de mais vendidos, né? Então, algumas sessões que um e-commerce tem, banner promocional, sessão de prova social, captura de e-mail, footer completo e pronto. Aí eu expliquei como o card do produto, né, que isso é bem legal, é o próximo passo, depois a gente entrar na página de produto e fazer o fluxo de compra, qualidade, tudo responses.

**22:12** · Estado de carregamento, né, o loading, o skeleton, acessibilidade básica, títulos e descrição de página pensados para SEO.

**22:20** · Então, cara, estamos criando um bom projeto aqui. Inicialmente tá começando aqui também no nosso GPT Sol. E aqui o Kim também já começou a loja. O Kim ele costuma dar todo list, tá? Então aqui provavelmente já vai mostrar. O GPT já me deu os passos, né, que é tudo list. Então a gente tem aqui esses quatro passos para ficar pronto. E aqui o Cloud não me passou nada.

**22:50** · E ele tende ser assim, tá? Então vamos dar uma olhada no desenvolvimento de cada um deles e também acompanhar o jogo ali quando terminar, né, para ver o tempo de cada um. Bom, galera, já tinha comentado isso no vídeo lá do lançamento do Kim, né? A resposta do sistema, ela aparenta ser rápida, mas eu sinto que demora um pouco mais do que os demais, tá? Aí eu não sei se é por causa do lançamento, ainda a gente tá nessa fase muito inicial, depois vai dar para ver isso melhor, mas aqui tá a tudo deles, né? Vamos ver se realmente vai continuar demorando. O jogo segue aqui, tá?

**23:20** · E os outros também estão entregando conforme a gente pediu, tá? Então basta aguardar agora enquanto os projetos são concluídos.

**23:35** · Bom, galera, aqui no cloud o jogo terminou, tá? E aqui o GPT ele também já entregou a parte inicial.

**23:48** · da loja, tá? Que a gente pediu para desenvolver e a gente já pode testar, só que eu vou esperar os outros, é claro, né?

**23:58** · Então, o Cloud tá trabalhando 16 minutos. O jogo também terminou, como eu falei, né? Foi cerca de 30 minutos, eu acho.

**24:08** · Ele tirou aqui, mas ali quando deu status eu vi que deu 30 minutos de sessão, tá? Então deve ser, foi em torno disso, né?

**24:19** · E o Kim aqui ainda está fazendo a loja, né? Ele já tá bem adiantado, fazendo a home já, que é praticamente a última parte, né?

**24:28** · Aí vamos ver o que ele nos entrega. A gente testa os três juntos para poder ver essa primeira parte. O jogo do Kim tá aqui andando ainda também. Deixa eu ver aqui, ó.

**24:45** · Se a gente for ver em questão de tarefas, né, são 12, aí falta três para terminar.

**24:52** · Então aqui também não tá muito longe do Fable, né, que vocês viram ali. Vamos ver se vai rodar muito tempo, né, que lá no na comparação que eu fiz com que lá no lançamento, né, que eu fiz o vídeo de lançamento, ele demorou muito para fazer os testes. Aí quando eu cancelei, fui rodar o jogo, tava meio bugado ainda, mas entregou legal.

**25:11** · Vamos ver aqui então, acompanhar a loja que é o nosso foco inicial para depois cereja do bolo, seu jogo.

**25:19** · Ó, então aqui, galera, o Cloud ele também terminou a loja, tá?

**25:24** · Eh, demorou um pouco mais ali que o GPT.

**25:27** · Eu vou pedir para ele iniciar o projeto ali no GPT também.

**25:35** · Tá na porta aleatória, porque daí não bate uma com a outra, né? Tento iniciar geralmente na 3.000.

**25:42** · Pedi aqui também. E fico no aguardo do Kim, né?

**25:47** · Agora o Kim tá quase no fim, né? Não vai ficar tanta diferente diferença pro Fable assim, imagino eu. E a gente inicia também, teste essa primeira etapa.

**25:57** · Ó, pessoal, o Kim também terminou, tá? Vou pedir a mesma coisa para iniciar na porta aleatória. Então agora a gente vai poder testar os três ao mesmo tempo. Vamos ver como é que foi a escolha de cores, né, o design de cada aplicação. Assim a gente vai entender melhor como é que cada modelo funciona nesse quesito, né?

**26:18** · Iniciar projeto e design. Como eu falei para vocês, o Fable entregou ali por volta também de uns 30 minutos o e-commerce. O jogo também foi o mesmo tempo, basicamente, e o químico, eu falei que demorava, levou ao mesmo tempo. Então, talvez a percepção minha ontem no lançamento, né, quando eu gravei foi enganosa, né, porque eu tava rodando o modelo em si, mas ele levou um tempo bem parecido do Fable aqui nesse exemplo.

**26:47** · O jogo também já terminou, cara. Que doideira. Mas vamos agordar. É a cereja do bolo. Vou abrir os três.

### Verificando como ficou a home page de cada projeto

**26:55** · Vamos lá, então, galera. Os três estão na ordem. Kim, GPT e o Fabor 5, rapaziada. Então, esse aqui foi o Kim.

**27:04** · Cara, eu curti, curti a pegada, achei legal, né? Ou a pisada, ó. Tá interessante. Ele desenvolveu os produtos SBG. Ficou legal, né? Não gerou imagens. Beleza. Tá, ó, tem um highlightzinho cada produto, né? Teve um trabalhinho, categorias, né? Todas as sessões estão comprometido. Aqui, ó.

**27:25** · Faltou um gradient, né? Esse aqui é um erro de acessibilidade.

**27:29** · Google reclama, tá? Então temos um ponto ruim aqui. Claro, um prodzinho resolve, né? Mas temos que ficar atento pras entregas.

**27:40** · Aí, ó, ele entregou aqui a parte de produto que eu não tinha solicitado, ele foi além, né? E a gente tinha especificado ali no prompt, talvez por isso até que ele demorou um pouco mais, mas tá tudo certo. GPT, caraca, sinistro, né? A gente teve um resultado bem interessante também eh no GPT quando eu fiz o teste do 5.6 contra o Fable. Foi bem legal. Como eu falei, olhem lá, o vídeo tá bem massa.

**28:04** · Então, cara, achei o visual bem interessante, pegadaça, muito fora de slop, né, que a animação não ficou tão boa, né? Ele deu uma cortada ali na imagem, ó.

**28:18** · Todos esses tá de produto, né? Já.

**28:21** · Então aqui tá cara a COP, né? Vocês estão percebendo os textos também? Você é bem olhar. Tipo, o Kim ele entregou textos padrão de e-commerce, né? Nada contra. Beleza, texto a gente melhora depois. Mas a cópia do GPT já tá COP de loja mesmo, cara. De pegada assim que tem a aquela cara, né? Ele já fez tudo junto. Isso é legal. Mais vendidos, ó.

**28:47** · Sessão de promoção, contraste legal, reviews, faquzinho, \[ \_\_ \] É, rapaziada, e agora clot, ó, Facebook fez assim, tá? Desafi é sua também.

**29:06** · Copzinha já.

**29:09** · Legal.

**29:12** · É, eu achei os outros dois, tipo assim, os contrastes de sessões assim melhor, né? Principalmente GPT, tipo Fable.

**29:25** · Tá bacana, tá legal.

**29:28** · Vou dizer para vocês, acho que até prefiro Kim. E olha só, temos scroll lateral, mano. \[ \_\_ \] isso aqui inadmissível para mim. Inadmissível, tá?

**29:38** · sua lateral, algum bug de CSS, provavelmente, tá? E na admissível, para mim isso aqui é um erro que no modelo que tu paga tanto não devia ter, tá? Então eu requeria GPT, Kim, Fable, tá?

**29:56** · Provavelmente alguns de vocês vão preferir o Fable, mas eu senti uma uma pegadinha ali no Kim também, tá?

**30:03** · Gostei da ideia. Segundo prompt agora é o fluxo de compra. Vamos ver então.

### Segundo prompt para fluxo de compra do usuário (carrinho, checkout e sucesso)

**30:10** · Vou mandar aqui no Kim, vou mandar no GPT, vou mandar no Fable.

**30:19** · Olha só. Vamos lá. Continue o mesmo projeto Pisada dentro da pasta loja Pisada, né? Agora ele vai implementar o fluxo de home, página de produto, carrinho, checkout, página de obrigado.

**30:29** · Então, como eu tinha falado, eu não pedi para ele desenvolver parte de produto antes, né? Tinha lá no prompt aqui.

**30:34** · Então, eu tô pedindo para desenvolver, né? Então o que eu quero da parte de produto, eles vão melhorar provavelmente não vão reiniciar do zero, mas ali pedir galeria com imagem principal, seleção de corre tamanho com variações esgotadas, guia de medidas eh preço, passamento e cálculo de frete por CP, botão de adicionar o carrinho, sessão de avaliações, vitrine produtos. Aí vai ter o carrinho que é a próxima etapa quando o cara adiciona mini carrinho deslizante no header. Então vai ter um carrinho eh sem página, vamos dizer assim, vai ter vai ser a síncrona, né?

**31:04** · O cara vai est acompanhando o pedido dele em qualquer página. Aí vai ter a página de carrinho completa que aí sim o cara vai pro checkout, né? Barra de progresso pro frete grátis, cupons de desconto. Vai ter bem-vindo 10 com 10%, dá para testar. Resumo detalhado, carrinho persistente, estado vazio, bem desenhado com CTA de volta para as vitrines, se o cara não tiver nada. Aí o checkout em etapas, identificação, entrega, pagamento e revisão, tá? Então o cara vai passando pelas etapas e compra.

**31:35** · Depois ele fecha o pedido, a gente vai salvar no banco Esquelate para não complicar ali a questão de banco de estrutura. Se até vocês quiserem acompanhar, ele vai criar arquivo, né?

**31:42** · Então pedi aqui para ele fazer a finalização com uma página de obrigado.

**31:48** · Pedi para ele tratar os casos de borda, tá? Que seriam os problemas possíveis que aconteceria no sistema real.

**31:55** · Quantidade marca estoque, cupom fora da regra, CP inexistente, cartão reprovado, Pixirado e tentativa de finalizar com o carrinho esvaziado em outra, né? Então o cara esvazou o carrinho e tava com o carrinho aberto, tenta finalizar, mas não rola, né? Então vamos dar uma olhada aqui como é que eles desenvolvem isso. Todos os três rodando, né?

**32:21** · com Kim aqui, Codex e o Cloud. Vamos ver que que entrega melhor essa segunda etapa.

**32:31** · Bom, galera, rodou, está rodando, né, cerca de 10 minutos aqui, né, e os três estão trabalhando, né, que foi muito rápido, nas outras, tá aqui na primeira etapa ainda. Cloud tá aqui, né, acho que não tinha banco de dados antes.

**32:51** · E agora ele tá estruturando um e o Kim está aqui também. Então a gente tem uma paridade pelo menos nesse início de tarefa, vamos dizer assim, né? Vamos ver que que vai acontecer no decorrer.

**33:08** · Mesma situação, tá? O Codex terminou, o cloud terminou um pouco depois, tá?

**33:18** · Então a gente teve uma entrega mais lenta novamente aqui no cloud code e o Kim segue trabalhando e aqui não tá tão perto do final, então talvez nessa etapa aqui ele demore um pouco mais, né? Mas vamos dar uma acompanhada aqui ver o que acontece.

**33:37** · Bom, galera, então o Kim terminou também demorou um pouquinho mais, tá? eram mais etapas, como lá no jogo que eu testei quando lançou, ele ficou um pouquinho mais também aqui nos testes. Eu não sei se é algo configurado do modelo, né, que ele testa mais para entregar, mas tá aqui, tá?

**33:55** · Então tem roteiros de teste e tudo mais, mas vamos tentar fazer sem, né? Vamos ver se a gente consegue ir até o fim da compra sem seguir roteiros. GPT e Cloud, né? Todos com mensagem finalizados.

**34:08** · Vamos abrir aqui, ó. Todos os projetos continuam de pé.

**34:13** · Então, ó, Cláud caiu, parece. Não cai não. Então, é isso. Agora vamos testar primeiro pelo Kim, né? Repetir o processo aqui para que a gente possa ter ã uma avaliação mais justa, né? E ver se nos três a gente chega até o final.

### Testando fluxo de compra no Kimi K3, Fable 5 e GPT 5.6 Sol

**34:29** · Vamos lá. Então, galera, a ideia é a gente conseguir comprar aqui. Vou escolher um produto.

**34:36** · Esse aqui é o Kim.

**34:39** · da cor aqui.

**34:41** · Um CEP, ó. Achou aqui, não tá recarregando no outro CP, né?

**35:07** · C não existe nossa base, tá?

**35:11** · É, deixa eu ver aqui.

**35:21** · Tem umas validações aqui. Teria que testar mais, né? Ó, o carrinho flutuante finaliza aí. Já foi pro checkout, né? Beleza. A ideia é sempre pelo carrinho, né?

**35:34** · Ó, o carrinho já botou o compom ali, né?

**35:37** · Não é a melhor coisa do mundo. Deu desconto. Beleza. Recarrega. Persiste.

**35:48** · Tá o CEP aqui.

**35:55** · O número traga Express normal para Pix.

**36:05** · E aqui, ó, ele confirmou, né? Geralmente com ambiente de teste, a gente faz isso, né?

**36:14** · A gente faz o Pix se confirmar depois de um tempo, né? Então, beleza, pedido feito, pedido fechado.

**36:26** · E aqui não fiz autenticação, né?

**36:32** · Mas eu posso ver ali o meu pedido, se eu consegui entrar naquela tela ali, né, do obrigado.

**36:38** · Eu posso mandar o o PIS e ele me mostra.

**36:48** · Tá, funcionou, funcionou. Tá, galera, tá legal, tá bem polido. É isso aí, né?

**36:53** · Talvez alguma coisa a gente tivesse que mudar, beleza, melhorar, polir mais alguma coisa, mas deu boa. Vamos ver o GPT aqui. Escolher um produto, ó. Esse aqui tá segund os tamanhos, né?

**37:12** · Deixa eu ver aqui.

**37:15** · Será que não encontrado, ó? Entrega normal. Beleza.

**37:23** · Adicionar sacola, ver carrinho ou pro checkout.

**37:26** · Carrinho.

**37:29** · Tá. Cupons bem-vindo. 10.

**37:35** · Deu certo.

**37:38** · Checkout.

**37:39** · Passo a passo destinatário.

**37:50** · Tá mudando, Pix.

**37:59** · Pixulado. Então vocês tão vendo que tá muito legal, né? A entrega do GPT.

**38:07** · confirmar pedido. Valeu, sua pisada já começou, cara. Tá bem bem interessante, né?

**38:15** · E que tá o acompanhamento pedido.

**38:18** · As duas entregaram muito parecido, né?

**38:21** · Então eu ainda fico pelo layout e cop o GPT, né? Achei bem único assim, bem legal.

**38:30** · pro cloud escolher o produto.

**38:35** · Tamanho tá o CP tá caiu no carrinho. Ó o carrinho dele meio bugado, cara. Olha só essas coisas, cara. Não dá para entender, velho. Isso é \[ \_\_ \] cara. Vamos ver o carrinho.

**38:55** · Taliste já pedido.

**39:10** · T Express, mano. Completo cartão Pix. Ó, tem uns cuidadinhos que do GPT e do Kim ficaram melhor, né? Tipo, a gente via ali as marcações de Pix cartão aques botão os emojis, né? Ó, tá quebrado, cara. Tá com scroll, cara. Fable, quem diria, né?

**39:40** · Aprovou, caiu aqui. Para mim, o mais simples de todos, tá? Claudim tá perdendo até do Kim nesse no quesito do projeto. Tá bom.

**39:52** · Testes feitos. Ainda fica o GPT, mas o Kim tá logo ali, né? Agora eu quero passar o último prompt, que seria a área admin, né? pra gente poder ver a visão de quem dá manutenção pra loja. Então, vou colocar o prompt no Kim, o prompt no GPT, o prompt no cloud.

### Terceiro prompt para visão administrativa (pedidos, dashboard)

**40:17** · Mostrar o promp para vocês. Continuar com projeto Pisada. Autenticação do admin, login com e-mail e senha senha armazenada com rest seguro. Sessão segura. Inspiração por inatividade, logout. Proteção de todas as rotas administrativas.

**40:31** · limite tentativas erradas na primeira execução criu admin inicial. Então uma prática comum, né, para sistemas assim.

**40:38** · Gestão de pedidos, lista paginada com busca, detalhe do pedido, mudança de status, cancelamento, né? Eu posso dar um reboço pra pessoa, regras de transição, pedido entregue não pode voltar para em separação, cancelada é terminal, né? Então não, ele não revive mais esse produto, vamos dizer assim, gestão de produtos para poder eh adicionar e tal, né?

**40:59** · Dashb da loja, indicadores, gráfico de faturamento, distribuição de pedidos por status, top cinco produtos vendidos, receita por categoria, alerta de produtos com estoque baixo e regist auditoria. Aqui toda a ação do admin, né, para ele poder testar e ver se todos os fluxos funcionam.

**41:21** · Vamos então fazer o teste, os três rodando.

**41:26** · E aí a gente vai definir qual que foi o melhor e testar a cereja do bolo, né, galera, que é o nosso grande jogo poeira alta.

**41:38** · Bom, daí a gente começa a ver a repetição de padrões, né? Lista de to no Kim, no GPT aqui também os passos no cloud nada, né? Então vamos acompanhando e vendo quanto tempo também eles vão terminar as ações e tal pra gente poder ter esse nível de comparação também. Então é isso, galera. Temos aqui no Kim, ó, ele me entregou como testar barra de mim, tá?

**42:08** · Aqui no Codex.

**42:12** · Codex deu uma desistida aqui, fechou.

**42:15** · Esse projeto tá no ar ainda e o nosso cloud barra admin também. Vamos ver então.

### Testando área admin e dashboard

**42:26** · Já tá aqui. Codex também tá on. Tudo on.

**42:30** · Beleza. Então vou testar primeiro no Kim barra admin.

**42:36** · Tá aqui admin.

**42:45** · Ó, aqui, deixa eu ver se ele me deu alguma instrução.

**42:52** · Tem uma senha aqui, ó.

**42:57** · Então, eu tenho a dashboard, seguindo a ideia da loja, né?

**43:02** · Hoje, últimos 7 dias, pedidos por status, alerta de estoque baixo, mais vendidos, não linca pro produto, né? Podia ter linkado para ajudar.

**43:18** · Tá de pedidos.

**43:22** · Ó, o pedido aqui.

**43:24** · Produtos.

**43:26** · Posso editar.

**43:29** · Vamos mudar o estoque.

**43:32** · Salvou auditoria, ó, o o log de tudo, né? Então, bem legal, funcional. E cara, é isso, né? Que que eu vou falar?

**43:48** · Admin, ó. Então aqui eu vou ter que ver que ele me deu destrução.

**43:55** · Tava no projeto errado. Ele abri outra conversa quando ele caiu.

**44:00** · Deixa eu ver se ele vai me dizer como testar. Não falo nada, né?

**44:13** · Tem a as tentativas do login.

**44:22** · Vou pedir aqui o usuário para testar o admin deve ter feito, né? Mas ele não passou aqui.

**44:29** · Tá aqui, ó. Admin@pisada.com.br.

**44:32** · BR, ó, entrou. Então, ele manteve a mesma estética. Temos a dashboard, estoque baixo, top cinco produtos, pedidos. Posso ver detalhe do pedido?

**44:53** · Bem legal. Eu gosto de dashboard às vezes com design diferente, né, galera?

**45:00** · Acho que eu errei nisso porque muito parecido assim, fica muito carregado.

**45:05** · Deixa eu botar aqui salvar.

**45:09** · É o admino, acho que preferia até do admin no geral, acho que eu preferiria até do do Kim, cara.

**45:18** · Sei se porque o design tá menos carregado do projeto em si, né? Ficou mais legal. Aqui tem vários logs porque ele testou também, né? Então legal, né?

**45:30** · Tudo entregue. Vamos ver o cloud.

**45:34** · Pedi usuário para testar aqui também.

**45:36** · Ah, ele deu aqui já. Tinha visto.

**45:38** · Admin@pisada.com.br.

**45:42** · Senha, ó. Tá aqui. Então, o dashboard dele, por o design de ser menos carregado, tá mais interessante de visualizar, né?

**45:53** · Eu posso em pedidos.

**45:57** · ver o detalhe do pedido, tá legal, né?

**46:02** · Posso ver o produto? Alterar um estoque.

**46:08** · Beleza.

**46:10** · Auditoria aqui também. Então, a parte do adminal no cloud, né? Preferi por causa do design. Na verdade, foi um erro meu, né? Ter colocado o mesmo design para todos os admins, né? Ela deveria ter colocado um layout diferente, né, mais tranquilo assim, tipo esse aqui, né, que f um layout mais padrãozinho por causa da loja em si, né, talvez transferisse para um admin layout mais padronizado, fosse mais interessante para fazer um teste, né?

**46:39** · Mas bom, tudo funcionou perfeitamente, né, nada a reclamar do admin, né?

**46:48** · Então, galera, seguindo aqui os meus critérios, eu acredito que eu preferi não gerar o do GPT, mas logo em seguida o do Kim, tá?

**46:59** · E por último, o do Claud, eu acho que errou em alguns algumas questões, principalmente essa barra lateral, carrinho aqui, muito esquisito, né?

**47:10** · Então, não tem como esse projeto aqui, tá?

**47:13** · Não é uma qualidade Fable, né? Não espera o Fable entregar isso aqui.

**47:18** · Tudo o mesmo prompt, né? Agora quero saber de vocês também. Vamos pro jogo, então. Vamos ver o que que nos reservou o jogo.

### Testando o jogo criado pelas IAs Kimi K3, Fable 5 e GPT 5.6 Sol

**47:26** · Tá aqui. Inicie o jogo e me passe endereço de teste.

**47:33** · Dis pros três, né? Ó, pedir pro cloud também. Vamos guardar aqui.

**47:41** · Ele nos dá como testar o jogo. Ó, o do Kim abriu é esse aqui.

**47:48** · Vamos ver os outros.

**47:50** · Abri o do Cloud também.

**47:52** · Então vamos lá, galera. Só para recapitular. 8419 é o do Kim, tá bom?

**47:59** · GPT ficou na 5568, que é essa daqui, e o Cloud 3196, né, à portas. Então, esses são os três jogos. Vamos testar o do Kim primeiro, ó. Então, ele tá tirando aqui, ó. Tem que falar com tio Rubens, ó. Tem, tá 3D, né? Não tá muito bem trabalhado os modelos, mas acredito que o estábulo.

**48:31** · Minimapa tá ao contrário.

**48:39** · Entrou no está tio Rubens.

**48:45** · Tem um dialogozinho.

**48:50** · Será que passa?

**48:54** · Recarregando.

**49:01** · \[risadas\] Matou o cara mesmo, velho.

**49:04** · Loucura. Vamos ver lá.

**49:09** · Ó, tem alguém me atirando em mim.

**49:13** · Os cara policial. Ah, mas tá ruim de atirar.

**49:31** · Tem tem um sonzinho, né?

**49:51** · Ó, agora vocês estão vendo o som?

**49:55** · Agora acabou as balas aqui.

**49:59** · Ah, tem mira, ó. Que o boneco tá na frente.

**50:08** · Tá, ficou legalzinha. Não ficou tão ruim.

**50:11** · Sonzinho da arma. Tá beleza. Então, Kim e desenvolveu alguma coisa. Não para dizer que não. Vamos ver aqui, ó, o do GPT.

**50:23** · Caraca, mano.

**50:25** · Não tem som.

**50:30** · Como é que põe a arma?

**50:36** · Conversa ficou meio bugado.

**50:38** · A mira.

**50:42** · Não tá tirando as pessoas.

**50:50** · É, o jogo parece a qualidade tá um pouquinho melhor, né? Mas não tá tirando ninguém.

**50:55** · Ó o cach cavalo, cara. Para tu ver do que me tá respondendo melhor, né?

**51:07** · Ah, tem som sim. Não tem música do Kim tinha música, velho.

**51:18** · Cara, assim, ó, de acabamento, né? O do Kim ficou melhor, né? Iniciou a missão e tal. Aqui eu não sei nem o que eu tenho que fazer, né?

**51:27** · Conversa com os moradores.

**51:32** · Não tá pulando. Que isso?

**51:38** · Ah, beleza.

**51:40** · Então, tá, é isso aí. GPT também não foi muito bem, mas o Kimi saiu melhor aqui.

**51:46** · E por último, Clod, né? Vamos ver se agora no jogo ele se restabelece.

**51:53** · Ó, matou o cara.

**51:58** · Policial não tá lá com o policial.

**52:06** · Pula. Tá pulando.

**52:09** · Mata o policial do que me ganhou nisso também.

**52:15** · Ó, subiu, cara. O que me deu matar o policial pelo menos.

**52:24** · Bom, nenhum dos dois ficou tão excelente assim, mas deu para brincar um pouco, né? Aí cara, curti mais do Kim, até a tela inicial aqui, ó, mais trabalhadinha, né? Mostrando a cidade e tal, cara. Entra aqui, pá, tem que ir ali pro estáblo, facultens.

**52:47** · E aí, tem que comentar vocês aí agora, né? Quero saber o que vocês acham.

**52:52** · Bom, galera, essa daqui foi a comparação, né, entre os três. Espero que vocês tenham curtido.

### Considerações finais sobre os três modelos

**53:00** · Quero saber o que vocês acharam de todos os nossos testes aqui. Acho que deu para ver bastante, né, que nem sempre a gente vai ter melhores resultados com modelos melhores, né, teoricamente melhores, né?

**53:12** · A gente pode ter bons resultados com modelos mais baratos, com modelos intermediários, né?

**53:17** · Dá pra gente testar bastante, por isso que eu sempre incentivo o teste. Não esqueçam, dê uma olhada aqui na formação Vibe Coding, o link vai est no comentário fixado. Galera, eu também vou descolar para vocês uns cupons de desconto do Kim, esqueci de avisar. Vou deixar na descrição aqui se eu conseguir, tá? Pessoal troca uma ideia comigo de vez em quando, então eles me dão acesso antecipado, né, para poder testar o modelo e às vezes eles me dão o cupom vai tá aqui na descrição desse vídeo, beleza? Também, claro, né?

**53:46** · formação VB coding. Se tu quer aprender mais sobre ferramentas que a gente usou aqui, Codex, cloud code, Open Code, é o treinamento certo, tá? Vitalício, tem comunidade de alunos, quase 40 horas de treinamento, vários e vários projetos para tu praticar e colocar eles no ar e aumentar teu portfólio, aprender a criar coisas diferentes, né? Entender como é que funcionam os prompsar os projetos de forma correta. Acho que vale muito a pena, tá? Eu ficando por aqui, não esqueça de deixar aquele like também se inscrevam, isso ajuda a gente bastante, tá? Fortalece muito o meu trabalho.

**54:21** · Quero muito ouvir a opinião de vocês, ler aqui nos comentários o que vocês acharam de cada um deles, qual que vocês estão testando e qual que vocês pretendem utilizar. Galera, vou ficando por aqui, muito obrigado. Vejam os vídeos que eu recomendei e até mais.

**54:34** · Valeu,