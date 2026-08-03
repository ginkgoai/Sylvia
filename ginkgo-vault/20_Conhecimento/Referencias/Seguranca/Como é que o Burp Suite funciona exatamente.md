---
title: "Como é que o Burp Suite funciona exatamente?"
source: "https://www.reddit.com/r/cybersecurity/comments/11gdc9y/how_burp_suite_works_exactly/?tl=pt-pt"
author:
  - "[[[apagado]]]"
published: 2023-03-02
created: 2026-07-15
description: "Olá a todos! Comecei a usar o Burp Suite na minha jornada de aprendizagem em cibersegurança e estou mesmo fascinado. Desde que comecei a usá"
tags:
  - "clippings"
---
Olá a todos! Comecei a usar o Burp Suite na minha jornada de aprendizagem em cibersegurança e estou mesmo fascinado. Desde que comecei a usá-lo, tenho uma pergunta que não me sai da cabeça: como é que o Burp Suite funciona exatamente? Como é que consegue intercetar um pedido, congelá-lo e depois encaminhá-lo assim que o utilizador termina o seu trabalho?

---

## Comments

> **Astralnugget** · [2023-03-02](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jao6a2k/?tl=pt-pt) · 87 points
> 
> Também sou muito novo nisto, por isso, ALGUÉM, POR FAVOR, me corrija se estiver errado, para que eu possa aprender.
> 
> Num nível super básico, não estás a ligar-te diretamente ao servidor do site, estás a ligar-te ao servidor proxy do Burp, que depois se liga ao site. O que significa que todos os teus pedidos têm mesmo de passar pelo Burp, e ele diz "olha, é isto que estou a enviar para o site, dá uma olhada" e depois, quando interceptas e modificas um pedido, estás basicamente a dizer "ah, não, aquela coisa devia ser esta coisa" e modificas o pedido. Depois, o Burp diz "ok, a enviar isso para o site então". E o site só recebe esse pedido modificado do Burp em teu nome e o site não tem como saber que alguma vez foi diferente.
> 
> > **pyker42** · [2023-03-02](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaopxtc/?tl=pt-pt) · 13 points
> > 
> > Concordo com o outro comentário, nunca diria que és novo/a na cibersegurança. Essa é a melhor explicação de como o Burp funciona que já vi.
> > 
> > **w00liest** · [2023-03-02](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaoeh4l/?tl=pt-pt) · 19 points
> > 
> > Excelente resposta e explicaste maravilhosamente. Nunca diria que és muito novo :)
> > 
> > **mannyspade** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jap95mn/?tl=pt-pt) · 5 points
> > 
> > Yup. A única coisa que gostava de acrescentar é que o servidor proxy Burp é mesmo a própria app na tua máquina (se definires o proxy como loopback). O que também significa que podes configurar outra máquina (LAN ou remota) com o Burp Suite instalado, e essa máquina pode funcionar como o servidor proxy.
> > 
> > > **sappydowner** · [2023-10-07](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/k3u3vux/?tl=pt-pt) · 1 points
> > > 
> > > Queres dizer que usar essa máquina com tipo RDP para mais segurança? Estou a perceber bem?
> > > 
> > > > **mannyspade** · [2023-10-07](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/k3vmkq7/?tl=pt-pt) · 1 points
> > > > 
> > > > Já não me lembro bem o que queria dizer. Acho que estava a tentar explicar que podes passar os teus pedidos web por outro servidor quando o configuras no browser, mas não tenho a certeza onde é que o Burp Suite seria instalado nesse caso. Ainda não experimentei; tou só a falar por alto.
> 
> > **peesoutside** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jar026t/?tl=pt-pt) · 3 points
> > 
> > Diria que a chave de tudo isto é que o utilizador tem de confiar no certificado do BURP (assumindo que estás a intercetar tráfego HTTPS). Se o certificado do BURP não for confiável, não vai desencriptar o tráfego e, por isso, o utilizador não consegue mexer nos pedidos e nas respostas.
> > 
> > **\[apagado\]** · [2023-03-02](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaob5xh/?tl=pt-pt) · \-19 points
> > 
> > Olá, sim, eu sei como funciona a um nível muito, muito básico, queria saber mais alguns detalhes a nível de rede, por exemplo, para poder tentar estudar isso.
> > 
> > > **littlemissfuzzy** · [2023-03-02](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaolqdd/?tl=pt-pt) · 9 points
> > > 
> > > Não há muito mais a dizer, o [u/Astralnugget](https://www.reddit.com/user/Astralnugget/) explicou bem.
> > > 
> > > O browser está programado para perceber o que é um servidor proxy, como falar com ele e quando. Se estiver configurado para isso, vai fazê-lo. Pronto.
> > > 
> > > Umas palavras-chave que te podem interessar: SOCKS, proxy HTTP, proxy transparente.
> > > 
> > > Se quiseres saber mais sobre a parte da rede: ficheiros PAC e... ui, qual era mesmo? Há um registo DNS que podes fazer para também informar os endpoints do servidor proxy.
> > > 
> > > > **\[apagado\]** · [2023-03-02](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaongy2/?tl=pt-pt) · \-17 points
> > > > 
> > > > Foi bem explicado, sim, mas como disse, estava interessado em como essa funcionalidade foi realmente implementada. Vou ver as coisas que disseste, obrigado.
> > > > 
> > > > > **noob2code** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jar3j71/?tl=pt-pt) · 2 points
> > > > > 
> > > > > Eles explicaram, tipo, a maior parte de como a cena funciona. É tipo, configuras um proxy através do Burp. O utilizador faz um pedido -> O Burp intercepta via proxy -> O gajo vê/modifica/envia o pedido -> O site alvo recebe a cena interceptada -> O site responde -> O Burp vê a resposta & o utilizador vê a resposta.
> > > > > 
> > > > > O que é que estás a pedir "tecnicamente" mais? Assumo que seja como é que o proxy funciona, mas não vou tirar conclusões precipitadas.
> > > > > 
> > > > > > **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jarnu1n/?tl=pt-pt) · 1 points
> > > > > > 
> > > > > > Já tentei explicar isto várias vezes, mas acho que não consigo explicar-me melhor do que isto. Desculpa.
> > > > > > 
> > > > > > > **noob2code** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jarrqu3/?tl=pt-pt) · 1 points
> > > > > > > 
> > > > > > > Está tudo bem, só queria tentar dar-te uma ajudinha. Recomendo que leias sobre como as redes funcionam em geral, e também como funciona um proxy. Acho que com uma boa compreensão de ambos, vais conseguir responder às perguntas que possas ter.
> > > > > > > 
> > > > > > > > **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jas0hjv/?tl=pt-pt) · 1 points
> > > > > > > > 
> > > > > > > > Vou com certeza, obrigado/a. Se calhar posso seguir os vídeos do Professor Messer para o Network+.
> > > > > > > > 
> > > > > > > > > **noob2code** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jas5pqq/?tl=pt-pt) · 1 points
> > > > > > > > > 
> > > > > > > > > Esses são mesmo muito úteis e informativos, se ainda não viste, recomendo vivamente. Se tiveres recursos, também diria Total Seminar ou James Dion como alternativas, muito informativos.
> > > > > > > > > 
> > > > > > > > > > **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jat6p1l/?tl=pt-pt) · 1 points
> > > > > > > > > > 
> > > > > > > > > > Procurei por Total Seminar mas não encontrei nenhuma playlist de Network+ no YouTube. O mesmo para o James Dion, tens aí algum link?
> > 
> > > **dangerseeker69** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaqk7ay/?tl=pt-pt) · 2 points
> > > 
> > > Então parece que a tua questão é mais sobre networking em geral e não sobre o Burp 😅
> > > 
> > > **Astralnugget** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jarhuf6/?tl=pt-pt) · 2 points
> > > 
> > > Tenho a sensação de que talvez o inglês não seja a tua primeira língua, por isso estás com dificuldades em articular a pergunta, então vou tentar ajudar e ver se consigo entender um pouco melhor o que estás a perguntar.
> > > 
> > > O que queres dizer é mais ou menos, a nível do código-fonte, como é que a arquitetura do Burp se parece, e que tipos de comandos e código está a usar para interceptar e exibir o tráfego?
> > > 
> > > > **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jarnmq6/?tl=pt-pt) · 1 points
> > > > 
> > > > sim, é isso que quero dizer. desculpa se não me consigo explicar bem.
> > > > 
> > > > > **Astralnugget** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jarqx6b/?tl=pt-pt) · 2 points
> > > > > 
> > > > > Está tudo bem, o teu inglês é muito bom, eu só falo 1 língua, por isso estás a safar-te melhor do que eu.
> > > > > 
> > > > > A razão pela qual as pessoas parecem confusas é só porque os falantes nativos de inglês estão habituados a ouvir certas palavras em certos contextos, é só uma coisa que se aprende a usar a língua muito.
> > > > > 
> > > > > Tipo, neste caso, se perguntas como é que algo, ou qualquer coisa funciona, a maioria das pessoas vai assumir que estás a perguntar como é que funciona a um nível superficial e vais receber respostas como as que toda a gente aqui te deu.
> > > > > 
> > > > > Como é que algo "funciona" é geralmente uma pergunta muito ampla e vais receber respostas muito amplas. Se queres saber mais especificamente sobre um certo aspeto, podes tentar reformular a pergunta como eu fiz para ti no comentário acima.
> > > > > 
> > > > > Espero que isto não tenha soado condescendente, estou só a tentar ajudar-te para que possas aprender de forma mais eficaz no futuro.
> > > > > 
> > > > > > **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jas0w3k/?tl=pt-pt) · 1 points
> > > > > > 
> > > > > > Agradeço mesmo, obrigado/a. De qualquer forma, quero melhorar o meu inglês, por isso qualquer correção é bem-vinda :)
> > > > 
> > > > > **Astralnugget** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jarrc3x/?tl=pt-pt) · 1 points
> > > > > 
> > > > > Se precisares de ajuda para garantir que consegues dizer o que queres no futuro, podes mandar-me uma mensagem privada e eu tento ajudar para que seja bem traduzido.
> > > > > 
> > > > > > **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jas0lm6/?tl=pt-pt) · 1 points
> > > > > > 
> > > > > > Muito obrigado/a, és mesmo fixe!
> > > > > > 
> > > > > > **AutoModerator** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jarrc76/?tl=pt-pt) · 0 points
> > > > > > 
> > > > > > Olá. Parece que estás a pedir para te enviarem uma DM, ou a perguntar se podes enviar uma DM a alguém. Por favor, considera fazer/responder a perguntas no fórum público para que outras pessoas possam encontrar a informação se alguma vez pesquisarem e encontrarem este tópico.
> > > > > > 
> > > > > > *Sou um bot, e esta ação foi realizada automaticamente. Por favor, contacta os moderadores deste subreddit\](/message/compose/?to=*[r/cybersecurity](https://www.reddit.com/r/cybersecurity/)*) se tiveres alguma questão ou preocupação.*
> > 
> > > **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jarjbt1/?tl=pt-pt) · 1 points
> > > 
> > > Não percebo porque é que levaram todos esses downvotes, mas ok.

> **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/japgttq/?tl=pt-pt) · 6 points
> 
> É só um proxy. Pensa nisso como o teu router. Todos os pedidos passam pelo teu router. Se o teu router só guardasse um pacote até lhe dizerem para o enviar, ele ficaria ali no router físico. O dispositivo que está à espera da resposta continuaria à espera.

> **gccalvin** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jap1ls4/?tl=pt-pt) · 6 points
> 
> O Burp Suite (e o OWASP ZAP) é um software para testes de segurança de aplicações. No nível mais básico, podes abrir um browser "Burp" e todos os pedidos/respostas serão "proxied" através da aplicação Burp. Permite-te modificar facilmente os pedidos e ver como o servidor responde. Para o Burp, isto é normalmente feito através do separador Repeater.
> 
> O Burp também vem com outras ferramentas para testar sites, como uma análise DAST (Dynamic Application Security Test) que testará vulnerabilidades Web como XSS e injeções SQL. No entanto, isto requer uma subscrição pro. Também podes pegar num pedido, usar o Intruder para percorrer uma lista de palavras ou alterar o teu pedido incrementalmente.
> 
> A principal conclusão é ser capaz de ver um pedido e resposta HTTP, e modificar os pedidos para ver como o servidor responde. Esta ferramenta é comum entre as equipas vermelhas para invadir sites, e as equipas azuis para analisar sites.
> 
> Recomendo que dês uma vista de olhos à Web Security Academy da PortSwigger para um pouco de prática.
> 
> > **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jarctc3/?tl=pt-pt) · 1 points
> > 
> > Obrigado, o PortSwigger parece mesmo porreiro e também tem percursos de aprendizagem. Fixe!
> > 
> > **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/japszuk/?tl=pt-pt) · 1 points
> > 
> > Aqui, aqui

> **VicTortaZ** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/japhy7n/?tl=pt-pt) · 3 points
> 
> Diverte-te a brincar ou lê sobre as ferramentas de programador do browser, especialmente o separador da rede. Vai ajudar-te na tua jornada com o Burp Suite.

> **jeffo95** · [2023-03-02](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaoizh2/?tl=pt-pt) · 4 points
> 
> Funciona como um proxy que recebe pedidos de protocolos como http/https mesmo antes de chegar ao servidor para analisar.
> 
> > **\[apagado\]** · [2023-03-02](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaonk3e/?tl=pt-pt) · 1 points
> > 
> > Sim, mas como é que o proxy consegue receber esse pedido?
> > 
> > > **ConfidentlyLearning** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaoygck/?tl=pt-pt) · 2 points
> > > 
> > > Vais ver que o Burp (tenta) configurar as definições de proxy do teu browser(s) e/ou do sistema, de forma que o programa Burp a correr no teu sistema seja o proxy de "next-hop" para o tráfego web de saída. O Burp liga-se a uma porta TCP alta (8080 por defeito) e fica à escuta nessa porta por CONNECTs do teu browser(s). O tráfego do teu browser é, idealmente, direcionado para o Burp no teu próprio sistema, onde podes mexer nele antes de o reencaminhar.
> > > 
> > > Podes ter problemas se, por exemplo, as definições de proxy do teu sistema estiverem definidas para exigir direitos de administrador e o Burp não conseguir alterá-las.
> > > 
> > > **0xTib3rius** · [2023-03-02](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaooizv/?tl=pt-pt) · 1 points
> > > 
> > > Provavelmente vais encontrar mais informação técnica aqui: [https://en.m.wikipedia.org/wiki/Proxy\_server#Web\_proxy\_servers](https://en.m.wikipedia.org/wiki/Proxy_server#Web_proxy_servers)
> > > 
> > > Também há links para o método CONNECT lá, e a especificação HTTP que fala sobre proxies.
> > > 
> > > > **\[apagado\]** · [2023-03-02](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaopzdj/?tl=pt-pt) · 0 points
> > > > 
> > > > Fixe, obrigado/a.

> **fhammerl** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jaqkue8/?tl=pt-pt) · 2 points
> 
> O Burp Suite é uma ferramenta para testar aplicações HTTP e HTTPS quanto a vulnerabilidades de segurança através da inspeção e manipulação dos seus pedidos. HTTP é um protocolo relativamente simples e sem estado, por isso presta-se bem a ter pedidos manipulados e reproduzidos.
> 
> O Burp Suite executa um proxy HTTP, através do qual todas as tuas ligações são tuneladas. No caminho através do proxy, o Burp pode reter um pedido até que queiras enviá-lo, mas também podes reescrever completamente um pedido, reproduzi-lo, alterar parâmetros, etc.
> 
> O Burp Suite *também* executa um servidor TLS para interceptar ligações HTTP seguras por TLS, ou seja, HTTPS. Por esta razão, tens de adicionar o certificado aos certificados TLS confiáveis do teu sistema operativo ou browser. Este certificado é gerado na tua máquina e é único, mas não é assinado por uma CA, pois o certificado é válido para todas as ligações e domínios – nenhum certificado desse tipo existe na natureza.
> 
> > **\[apagado\]** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jarjnza/?tl=pt-pt) · 1 points
> > 
> > A cena dos certificados é mesmo fixe. Onde é que posso ler sobre isso?
> > 
> > > **fhammerl** · [2023-03-03](https://reddit.com/r/cybersecurity/comments/11gdc9y/comment/jat3z15/?tl=pt-pt) · 1 points
> > > 
> > > Diria que qualquer curso de fundamentos de cibersegurança te vai ensinar isso, mas, caso contrário, ia ao Google e pesquisava "O que é um Certificado Raiz?" e começava por aí.