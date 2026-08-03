---
title: "Por que tantos projetos de IA estão sendo cancelados?"
source: "https://www.youtube.com/watch?v=FABST5o9s8k"
author:
  - "[[gotoCobol]]"
published: 2026-06-23
created: 2026-07-02
description: "Muitas empresas investiram milhões em projetos de Inteligência Artificial esperando substituir sistemas e processos corporativos inteiros.Mas algo inesperado aconteceu, e vários desses projetos estã"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=FABST5o9s8k)

Muitas empresas investiram milhões em projetos de Inteligência Artificial esperando substituir sistemas e processos corporativos inteiros.  
  
Mas algo inesperado aconteceu, e vários desses projetos estão sendo cancelados ou reduzidos.  
  
Será que a IA foi superestimada?  
  
Nesse vídeo eu compartilho minha visão sobre esse assunto, baseada em algo que vivi na prática ao tentar criar um validador inteligente para as tarefas executadas pelos alunos no curso de COBOL.  
  
Se você trabalha com tecnologia, desenvolvimento de sistemas ou está buscando uma área mais estável na TI, esse vídeo pode mudar a sua forma de enxergar a IA.  
  
Para saber mais sobre o curso, dá uma olhada no link abaixo:  
  
https://gotocobol.com.br/cursos/gtc1-b2c/

## Transcript

**0:00** · Você deve ter visto essa notícia nos últimos dias. Um monte de empresa grande, as maiores do mundo, estão reduzindo ou cancelando o projeto de inteligência artificial. E isso é estranho, né? Porque ao mesmo tempo a mesma imprensa fala em revolução da IA, super inteligência, agentes inteligentes, substituição de emprego.

**0:22** · Então, como que essas duas coisas se encaixam? como que uma tecnologia que parece ser tão impressionante tá decepcionando algumas empresas. E a resposta para isso, eu acho que pode tá acontecendo por uma confusão em alguns desses projetos. A gente tá tentando usar a IA para fazer o trabalho que era de software tradicional.

**0:44** · Eu vou começar com um caso real. Outro dia eu acordei com uma ideia sensacional que eu achei que era sensacional, né? Eu ia substituir os scripts de validação de tarefa do curso por validadores inteligentes. Eu só tinha que juntar a especificação da tarefa o programa que o aluno construiu ou alterou, juntava isso com as evidências de teste, fazia um prompt para amarrar isso tudo e chamava a API da IA e ela me dava um feedback e

**1:11** · esse feedback ia ser melhor do que os scripts que eu tinha, porque além de verificar se as tarefas foram cumpridas, se os pré-requisitos foram cumpridos, a IA ia poder também sugerir eh melhoria de código, sugerir padronização, padrão de nomenclatura, poderia dar uma resposta muito mais completa e melhorar muito a experiência do aluno, né? Ou seja, a ideia parecia perfeita e funcionou até que começou a parar de funcionar.

**1:40** · Depois de três semanas batendo cabeça com chat GPT, Clou e Gemini, eu fui percebendo que alguns programas que estavam certos a a Iar reclamava de alguma coisa. Programas que estavam incompletos, claramente incompletos, a IA dava como como aceitável. Por exemplo, tinha caso em que a variável nem tinha sido definida no working storage, mas a IA considerava que tava tudo certo.

**2:06** · E aí depois de muita dificuldade, assim, alguns casos que funcionavam e outros não, eu comecei a conversar com a própria para tentar entender porque que ela não tava conseguindo fazer uma coisa que parecia ser a área de especialidade dela, né?

**2:23** · analisar contexto, analisar conteúdo de analisar código, por exemplo, e me dar um feedback. E aí a resposta eu achei interessantíssima, tanto dos três, das três reais que eu tava usando. O que eles disseram é: "Você tá tentando usar uma ferramenta de análise semântica para fazer análise determinística". A IA é boa para analisar contexto e fazer resumo, mas ela é péssima para reproduzir resultados sempre da mesma maneira.

**2:51** · Então, por exemplo, para você ter uma ideia, os agentes não conseguiam identificar nem se o programa tinha sido codificado em free format ou fixed format. Por quando ele pega um programa fonte, ele não lê o programa linha a linha como a gente faz. Ele transforma aquilo tudo em token, vai criando contextos para aquele negócio e gera a resposta a partir de probabilidade que ele que ele conhece. E nem sempre essa resposta vai est 100% certa. Problema não era falta de conhecimento de cobol.

**3:22** · Cobol, os três agentes, conhecem como ninguém. O problema era outro. Eu tava tentando usar uma ferramenta probabilística para executar uma tarefa que precisava de um resultado determinístico. Agora pense em um banco, pensa num sistema que calcula juros, calcula imposto, calcula salário. Quando esse sistema recebe um input, ele precisa gerar um output completamente previsível, 100% previsível. Isso tem que acontecer hoje, amanhã, daqui a 5 anos. Para determinadas atividades, não tem espaço para criatividade.

**3:52** · Acho que esse é que é o ponto. Não existe espaço para interpretação, não existe espaço pro quase certo. E é exatamente por isso que sistemas corporativos são construídos com regras rígidas e comportamento previsível. E aqui que tá o ponto que eu acho que muitas empresas descobriram ou tão descobrindo quando investem pesado em IA. modelos de a são excelentes para interpretar, reconhecer contexto, são excelentes para resumir documento.

**4:21** · Você pode resumir, gerar uma ata de reunião a partir da transcrição, do que foi falado de 10 maneiras diferentes se você pedir 10 vezes para isso é aceitável nesse tipo de tarefa.

**4:36** · Mas interpretar não é a mesma coisa que executar um processo de negócio. Se uma empresa tenta substituir um sistema inteiro por IA, achando que ele vai conseguir repetir aquilo com muito mais facilidade, ele vai conseguir ser criativo, ser interpretativo, mas ele não vai resolver os problemas que o software tradicional resolve. A empresa descobre que tá usando a IA por uma tarefa que ela não foi projetada para executar, como usar um carro de corrida para arar um campo, usar uma chave de fenda para pregar um prego na parede.

**5:07** · O problema não é a chave de fenda, o problema é a tarefa que você tá esperando executar com ela, né? Depois dessa experiência, eu fiquei com a impressão de que o modelo vai caminhar para uma outra direção. A Iá vai interpretar coisas, mas quem vai tomar decisões é o software, é o sistema do jeito que a gente conhece. A Iá entende o que o cliente quer. O software é que vai gerar a transação. A Iar resume um contrato, mas quem registra o processo é o sistema tradicional.

**5:39** · Quando a gente lê na imprensa sobre os projetos que tão sendo que tão avançando mais, que estão sendo mais bem-sucedidos, pode reparar que todos eles tem essa característica e a para em determinado momento, ela vai até um determinado ponto e depois disso a o resultado é entregue pro sistema que faz o processamento lógico que a gente conhece. Isso tem uma consequência interessante para quem trabalha com mainframe, com cobol e com sistemas corporativos.

**6:07** · Muita gente, a gente ouviu falar muito disso esse ano, muita gente acredita que a IA vai substituir o próprio desenvolvedor, né? Vai substituir o próprio processo de construção desses sistemas. E eu acho exatamente o contrário. A existência da IA tá tornando mais evidente a importância dos sistemas previsíveis.

**6:30** · Quando bilhões de reais estão em jogo, a característica mais importante do sistema que vai tratar aquilo não é a inteligência dele, é a previsibilidade, é a sua confiabilidade, é a sua consistência, é a sua capacidade de reproduzir o mesmo resultado milhões de vezes, sempre da mesma maneira. E é exatamente isso que os sistemas corporativos fazem há décadas, né?

**6:55** · Então, quando você lê uma notícia dizendo que um grande projeto de I fracassou, não culpa a tecnologia, não é a tecnologia de Iá que tá fracassando, não é porque ela é uma bolha, é só uma modinha, pelo contrário, ela é realmente revolucionária. Pergunta primeiro, a IA tava sendo usada nesse projeto para interpretar informações ou ela tava pretendendo substituir o software tradicional?

**7:21** · Se você gosta desse tipo de discussão que conecta mercado de trabalho, tecnologia, sistemas corporativos, a realidade das grandes empresas, no meu curso, a gente trabalha exatamente com esse universo. Você aprende cobol num ambiente de desenvolvimento que simula um ambiente de desenvolvimento das empresas. Então você vai trabalhar com programas de verdade, arquivos de verdade, vai gerar relatórios de verdades, vai não só construir programa, mas vai também corrigir problemas que acontecem nos sistemas produtivos normais.

**7:52** · O link tá na descrição desse vídeo para quem quiser conhecer. Me diz aí nos comentários, você acha que a IA realmente ela vai substituir os sistemas tradicionais ou vai surgir um modelo onde as duas coisas vão cooperar? Diz aí o que que você acha. E semana que vem a gente volta com mais conteúdo técnico, tá bom?