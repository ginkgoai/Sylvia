---
title: "Como Gerar Imagens Fotorealistas NSFW com Flux Klein 9.b (Fluxo de Trabalho Completo)"
source: "https://www.reddit.com/r/comfyui/comments/1sb7xdn/how_to_generate_photorealistic_nsfw_images_with/"
author:
  - "[[rudar133]]"
published: 2026-04-03
created: 2026-07-08
description:
tags:
  - "clippings"
---
---

## Comments

> **GreenHell** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe1xqic/) · 23 points
> 
> > O Hack de Prompting (Não pule isso): Em vez de tentar adivinhar o que o modelo quer, vá para o Grok. Diga a ele: "Escreva um prompt altamente realista para geração de imagem do Flux klein 9.b para \[o que você quiser ver\]." \* Certifique-se de pedir especificamente que ele verifique como escrever prompts para isso. O Grok escreve de uma forma que o Flux realmente entende, e o salto de realismo é enorme.
> 
> Eu costumo fazer referência ao guia de prompting do [Flux.2 klein](https://docs.bfl.ml/guides/prompting_guide_flux2_klein) desenvolvido pelo Black Forest Labs, e coloco alguns exemplos de imagens feitas com o Flux que eu gosto. Você precisa criar o prompt uma vez e salvá-lo, mas depois pode usá-lo sempre.
> 
> Se você também estiver executando algo como Open WebUI, pode criar um modelo customizado (basicamente um modelo com seu próprio prompt de sistema) que faz isso. Eu criei "Flux.2 klein prompt engineer" para esse propósito. Posso dizer o que quero e ele fará o modo yolo, onde adiciona os detalhes que estão faltando (iluminação, ambiente, etc.), ou me perguntará por esses detalhes para elaborar o "prompt perfeito" do Flux.
> 
> Posso compartilhar se houver interesse.
> 
> > **TheSlateGray** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe1yr7t/) · 6 points
> > 
> > Eu fiz uma habilidade usando os guias oficiais do flux e alguns guias da comunidade. Qualquer modelo que consegue fazer chamadas de ferramenta para ler arquivos pode simplesmente refinar o arquivo markdown sem treinamento especial.
> > 
> > Basicamente, é um prompt de sistema bem longo com exemplos. Engraçado como coisas principais e de código fechado estão alcançando coisas como cartões de personagem e chamando isso de novo como "skills.md".
> > 
> > > **GreenHell** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe22luk/) · 21 points
> > > 
> > > A mesma coisa, na verdade.
> > > 
> > > Aqui está o meu.
> > > 
> > > Prompt do sistema:
> > > 
> > > Você é um assistente especializado em engenharia de prompt, focado em criar prompts de alta qualidade para o modelo de geração de imagem FLUX.2 \[klein\]. Seu único propósito é transformar as ideias dos usuários em prompts envolventes, no estilo de romances, que aproveitam a força do Klein na geração de prosa centrada na cena.
> > > 
> > > ## PRINCÍPIOS CENTRAIS (Sempre Siga)
> > > 
> > > 1. \*\*Escreva Como um Romancista\*\*: Nunca use listas de palavras-chave. Sempre escreva prosa fluida e descritiva com relações claras entre os elementos.
> > > 
> > > 2. \*\*Estruture Seus Prompts\*\*: Siga esta ordem:
> > >    - Sujeito (quem/o que é o foco principal)
> > >    - Cenário (onde isso acontece)
> > >    - Detalhes (elementos visuais específicos)
> > >    - Iluminação (fonte, qualidade, direção, temperatura)
> > >    - Atmosfera (humor e tom emocional)
> > > 
> > > 3. \*\*Priorize os Elementos\*\*: Os elementos mais importantes devem vir primeiro no seu prompt.
> > > 
> > > 4. \*\*Iluminação é Crítica\*\*: Sempre inclua detalhes explícitos sobre a iluminação. Se o usuário disser "iluminação normal", interprete isso como "luz natural suave e difusa" e justifique essa escolha.
> > > 
> > > 5. \*\*Adicione Estilo/Tags de Humor\*\*: Termine os prompts com anotações opcionais de estilo e humor para consistência.
> > > 
> > > ## DOIS MODOS DE OPERAÇÃO
> > > 
> > > ### Modo 1: YOLO (Geração Automática)
> > > - Use quando a ideia do usuário for suficiente ou quando solicitado explicitamente
> > > - Preencha os detalhes faltantes de forma criativa com base no contexto
> > > - Gere um prompt completo em uma resposta
> > > - Mantenha os prompts entre 30-80 palavras para a maioria dos casos
> > > 
> > > ### Modo 2: GUIADO (Geração Interrogativa)
> > > - Use quando a ideia do usuário for vaga ou incompleta
> > > - Faça UMA pergunta direcionada de cada vez
> > > - Siga esta sequência de perguntas:
> > >   1. Cenário/Localização
> > >   2. Detalhes Visuais (elementos específicos)
> > >   3. Preferências de Iluminação
> > >   4. Humor/Atmosfera
> > > - Gere o prompt final apenas após coletar informações suficientes ou quando o usuário indicar que está pronto.
> > > 
> > > ## LÓGICA DE SELEÇÃO DE MODO
> > > - Se a entrada do usuário contiver um sujeito claro E contexto suficiente → modo YOLO
> > > - Se a entrada for mínima (por exemplo, apenas um sujeito) → modo GUIADO
> > > - Se o usuário disser "yolo" ou "apenas faça isso" → modo YOLO
> > > - Se o usuário disser "me guie" ou "faça perguntas" → modo GUIADO
> > > 
> > > ## FORMATO DE RESPOSTA
> > > 
> > > \*\*Resposta em Modo YOLO:\*\*
> > > \`\`\`
> > > \[Prompt completo entre aspas\]
> > > 
> > > Breve explicação das escolhas criativas feitas.
> > > \`\`\`
> > > 
> > > \*\*Resposta em Modo Guiado:\*\*
> > > \`\`\`
> > > \[Texto da pergunta\]
> > > \`\`\`
> > > 
> > > OU quando pronto para gerar:
> > > \`\`\`
> > > \[Prompt completo entre aspas\]
> > > 
> > > Confirmação de que o prompt segue a estrutura Sujeito→Cenário→Detalhes→Iluminação→Atmosfera.
> > > \`\`\`
> > > 
> > > ## EXEMPLOS
> > > 
> > > \*\*Usuário:\*\* mulher com cabelo loiro curto
> > > \*\*Você (Guiado):\*\* Que tipo de cenário você gostaria?
> > > 
> > > \*\*Usuário:\*\* um estúdio fotográfico bem iluminado com fundo branco
> > > \*\*Você (Guiado):\*\* Que tipo de detalhes existem? Há elementos visuais específicos?
> > > 
> > > \*\*Usuário:\*\* brincos coloridos e um colar, queixo na mão
> > > \*\*Você (Guiado):\*\* Que tipo de iluminação há na cena?
> > > 
> > > \*\*Usuário:\*\* apenas algo normal
> > > \*\*Você (Guiado):\*\* Qual é o humor e o tom emocional geral?
> > > 
> > > \*\*Usuário:\*\* neutro
> > > \*\*Você:\*\* 'Uma mulher com cabelo loiro curto está posando contra um fundo claro e neutro. Ela está usando brincos coloridos e um colar, apoiando o queixo na mão. A imagem tem um tom suave e quente, com um estilo minimalista.'
> > > 
> > > ---
> > > 
> > > \*\*Usuário:\*\* cidade cyberpunk
> > > \*\*Você (Yolo):\*\* 'Uma extensa metrópole cyberpunk à noite. Placas de neon em azul elétrico e magenta refletem nas ruas molhadas pela chuva. Uma figura solitária em um casaco tático caminha por um beco. Luz artificial dura das placas sobrepostas cria contrastes dramáticos entre sombras profundas e destaques vívidos. A atmosfera é tensa e misteriosa, evocando uma sensação de isolamento urbano em um mundo de alta tecnologia. Estilo: estética cyberpunk com influências de Blade Runner. Humor: noir, contemplativo, levemente ominoso.'
> > > \`\`\`
> > > 
> > > ---
> > > 
> > > ## LEMBRETES IMPORTANTES
> > > - Nunca produza prompts no estilo de palavras-chave
> > > - Sempre seja específico sobre a iluminação
> > > - Quando estiver em dúvida, opte por iluminação suave e difusa
> > > - Mantenha as perguntas concisas e focadas
> > > - No modo YOLO, faça suposições criativas razoáveis e anote-as    
> > > 
> > > E meu guia de referência é longo demais para um comentário no reddit, então aparece
> > > 
> > > > **Woisek** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe2jxyy/) · 1 points
> > > > 
> > > > Qual LLM você usa, já que o Grok não faz isso (mais)?
> > > > 
> > > > > **GreenHell** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe2lhwq/) · 1 points
> > > > > 
> > > > > Eu uso o Open WebUI como uma interface com um modelo local. Se você quiser usar isso com outra interface (por exemplo, Grok na web), você pode usar isso como um primeiro prompt e depois começar a conversa.
> > > > > 
> > > > > > **Woisek** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe2oxyg/) · 2 points
> > > > > > 
> > > > > > Sim... *qual* modelo local? 🙂
> > > > > > 
> > > > > > > **GreenHell** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe2yrjh/) · 3 points
> > > > > > > 
> > > > > > > [Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)
> > > > > > > 
> > > > > > > > **Woisek** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe30iss/) · 2 points
> > > > > > > > 
> > > > > > > > Uau, legal. O full 8 Bit? Ou 4 também são suficientes?
> > > > > > > > 
> > > > > > > > > **GreenHell** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe333xy/) · 1 points
> > > > > > > > > 
> > > > > > > > > Q4 funciona para mim, sem problemas. Mas eu só peguei um modelo sem censura e fui com ele, não comparei com outros modelos locais como Qwen 3, Gemma 3/4 ou Mistral. Um pensamento que surgiu é que o Qwen3 pode funcionar melhor, já que o Flux.2 Klein também usa o Qwen3 como codificador de texto.
> > > > > > > > > 
> > > > > > > > > > **Woisek** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe3czx9/) · 2 points
> > > > > > > > > > 
> > > > > > > > > > Sim, de fato é uma boa ideia. Também vou testar isso.
> > > > > > > 
> > > > > > > > **raindownthunda** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe4mrrc/) · 1 points
> > > > > > > > 
> > > > > > > > Esse é um ótimo coringa <sup>^</sup> e para algo com mais "sabor", experimente o Bluestar 27b [https://huggingface.co/zerofata/Q3.5-BlueStar-27B](https://huggingface.co/zerofata/Q3.5-BlueStar-27B)
> > > 
> > > > **i\_did\_nothing\_** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe4ioqu/) · 1 points
> > > > 
> > > > Isso é incrível, obrigado!
> > > > 
> > > > **kash326** · [2026-05-29](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oomem4u/) · 1 points
> > > > 
> > > > você tem um arquivo de fluxo de trabalho para isso?
> 
> > **janosibaja** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe2pan3/) · 2 points
> > 
> > Estou interessado, obrigado por compartilhar.
> > 
> > **Unique-Mix-913** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe31xls/) · 1 points
> > 
> > Eu acho que o Grok exagera. E isso fica irritante
> > 
> > **TechnicianOver6378** · [2026-04-04](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe7cxh2/) · 1 points
> > 
> > Estou interessado no seu "Flux.2 klein prompt engineer" também. Eu tenho estado meio que brincando com comfui por alguns anos, de vez em quando... mas sempre precisei usar ferramentas baseadas na nuvem.

> **Woisek** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe2gw7p/) · 4 points
> 
> Quais prompts o Grok criou para os seus exemplos?

> **bethworldismine** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe1femn/) · 2 points
> 
> você consegue fazer um fluxo de edição de múltiplas imagens também???? ou um fluxo de edição de uma única imagem com consistência facial
> 
> > **rudar133** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe28b6b/) · 1 points
> > 
> > Você pode conseguir consistência facial muito facilmente se estiver usando a LORA do seu modelo que você treinou. Você só precisa adicionar Carregar LORA e colocar a sua, e a consistência será muito boa.

> **a\_beautiful\_rhind** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe39jl9/) · 2 points
> 
> Então, essas são as 2 loras que eu preciso? Vou ver como se sai em comparação com o chroma.
> 
> > **Old-Buffalo-9349** · [2026-06-04](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/opnb5pl/) · 2 points
> > 
> > Isso tem 2 meses, mas como foi?
> > 
> > > **a\_beautiful\_rhind** · [2026-06-04](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/opolptf/) · 2 points
> > > 
> > > Parece de qualidade superior e um pouco mais rápido que o chroma, mas com um conjunto de treinamento mais limitado, especialmente para conteúdo NSFW. O Flux é mais propenso a gerar membros duplos em um prompt conflitante do que a ignorá-lo.
> 
> > **rudar133** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe45gbu/) · 2 points
> > 
> > Sim, esses dois loras funcionam, mas se você quer consistência na aparência, também precisa do seu modelo lora.

> **TheInternalNet** · [2026-06-01](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/op63uvg/) · 2 points
> 
> Eu estive correndo em círculos por mais de 30 horas nos últimos três dias tentando descobrir como passei de gerar literalmente qualquer coisa para tudo ficando vestido ou arredondado. Para resolver um erro de OOM, desativei todos os meus LORAS... MUITO OBRIGADO!!!!!

> **NostradamusJones** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe28nkz/) · 3 points
> 
> Obrigado por isso. O fluxo de trabalho que você forneceu não tem carregador lora, é fácil de corrigir, mas você sabe que algumas pessoas não têm ideia de como fazer esse tipo de coisa.
> 
> > **Ethan\_Hart1** · [2026-04-25](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oi4fx94/) · 2 points
> > 
> > Na era da IA, não se pode mais dizer: "Não faço ideia sobre essas coisas"
> > 
> > > **NostradamusJones** · [2026-04-25](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oi5lhwf/) · 2 points
> > > 
> > > Bem, antes disso era o Google. Deus me livre se alguém quisesse interagir com outro humano e fazer uma pergunta sobre um tópico específico em um fórum que existe para discutir esse tópico.
> 
> > **Woisek** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe2dyt8/) · \-13 points
> > 
> > Pessoas que "não têm ideia de como fazer essas coisas" deveriam aprender primeiro, antes de tentar criar coisas inúteis ou qualquer outra tarefa específica.
> > 
> > > **NostradamusJones** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe2ivai/) · 10 points
> > > 
> > > Bom, obrigado por dedicar um tempo para passar aqui e fazer um comentário sarcástico
> > > 
> > > Ideiticamente, deveríamos ser uma comunidade receptiva e prestativa. Quanto mais pessoas usarem o comfyUI, melhor ele ficará como ferramenta.
> > > 
> > > > **Woisek** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe2roqw/) · \-8 points
> > > > 
> > > > Ah, e você fez um comentário melhor, Sherlock?
> > > > 
> > > > O que não era "acolhedor e útil" para apontar como *aprender* de fato essa ferramenta? Enfiar um fluxo de trabalho na cara de cada novato não ajuda o ComfyUI, já que esses usuários *ainda* não entendem como funciona e, portanto, não podem contribuir com nada valioso para fazer o Comfy avançar. Só no Reddit tem *MUITA* coisa para aprender, sem contar no YT. Mas perguntar aqui é muito mais fácil, por causa desse comportamento "acolhedor e útil", que não faz nada para incentivar o aprendizado.
> > > > 
> > > > Já temos essa mentalidade idiota de "Você pode compartilhar o fluxo de trabalho?" para cada coisinha minúscula aqui, porque ninguém quer pensar mais. Apenas pegando a próxima oportunidade e se masturbando.
> > > > 
> > > > Não, obrigado. Não é isso que eu vou apoiar.

> **Scriabinical** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe40ngt/) · 2 points
> 
> Esse combo tem sido meu pão com manteiga nas últimas semanas. Você pode mudar qualquer coisa ou manter tudo bem rigoroso. Eu geralmente começo com uma imagem grosseira no SDXL só para deixar tudo do jeito que eu quero em termos de proporções corporais e pose (os modelos semi-realistas e anime são tão flexíveis). Depois, eu jogo no Klein 9B com SNOFS e uma lora SmartphoneReality do Civit. É simplesmente incrível. O Klein é um modelo absurdamente poderoso. Não me vejo usando outro modelo por um tempo.
> 
> > **Individual\_Holiday\_9** · [2026-05-22](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/on9ysny/) · 1 points
> > 
> > como você solicita isso? apenas "adicione detalhes realistas a esta imagem base" ou algo assim?

> **kermesse-xoxo** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe5uwh2/) · 1 points
> 
> Ótimo

> **JohnRobertSmith1234** · [2026-04-26](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oib4h40/) · 1 points
> 
> Obrigado!
> 
> Tem um modelo runpod para isso?
> 
> > **rudar133** · [2026-04-26](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oibs4b1/) · 1 points
> > 
> > Com este fluxo de trabalho específico, ainda não. Mas você pode usar o modelo normal e arrastar o fluxo de trabalho para dentro dele.
> > 
> > > **JohnRobertSmith1234** · [2026-04-26](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oicwech/) · 1 points
> > > 
> > > Eu me lembro vagamente de baixar loras nsfw sendo meio complicado por causa dos logins necessários. Mas isso pode ser uma notícia bem antiga. O modelo que eu experimentei não permitia a importação de fluxos de trabalho por arrastar e soltar. Não sei o que eu estava fazendo de errado, lembro que era diferente.
> > > 
> > > > **rudar133** · [2026-04-29](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oiwgd45/) · 1 points
> > > > 
> > > > Sim, você precisa acessar o token no seu perfil, mas com a ajuda da IA isso não é realmente um problema

> **Open\_Task\_6440** · [2026-06-10](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oqt6zn6/) · 1 points
> 
> Desculpe, sou novo em tudo isso, então eu baixei o fluxo de trabalho, conforme sugerido no post, e os LORAs, como eu adiciono os nós ao fluxo de trabalho para o SNOFS e o ultrareal da Lenovo funcionarem, por favor?
> 
> > **rudar133** · [2026-06-10](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oqvlhwp/) · 0 points
> > 
> > Você só precisa conectá-los logo após o seu Checkpoint Loader.
> > 
> > Adicione dois nós **Load LoRA**. Conecte Checkpoint -> LoRA 1 (SNOFS) -> LoRA 2 (Lenovo) -> KSampler/Prompts. Certifique-se de que os arquivos estão colocados em `ComfyUI/models/loras/` e clique em atualizar na sua interface se você não os vê nos menus suspensos!

> **cannabasics** · [2026-06-10](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oqwthuf/) · 1 points
> 
> [u/rudar133](https://www.reddit.com/user/rudar133/) Eu configurei tudo e funcionou em tipo 2 fotos, mas agora tudo fica coberto ou muito embaçado

> **maxiedaniels** · [2026-06-12](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/or9nho8/) · 1 points
> 
> Isso conserta o fato de não seguir instruções simples de Nsfw? Tipo, até mesmo apenas remover roupas.

> **ARC1T3CT** · [2026-06-19](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/osmmjzy/) · 1 points
> 
> Obrigado pelo aviso e pelo guia de configuração! Eu uso o Darkbeast em vez do fluxklein9b. É uma má ideia? E quais prompts você usou para obter esses resultados incríveis nos seus exemplos?

> **ShutUpYoureWrong\_** · [2026-04-04](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe675fv/) · 1 points
> 
> Se livrem dessa baboseira de propaganda. Ninguém quer seu link de referência do Runpod.
> 
> Moderadores, façam seu trabalho.

> **InternetsUser** · [2026-07-06](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/ovvmxat/) · 1 points
> 
> Segui este guia, mas não consigo conseguir nada sem calcinha. Alguma ideia?

> **niggistperson** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe1ezdx/) · \-13 points
> 
> você pode definitivamente fazer vídeos NSFW, mas a maior parte das coisas open source é uma dor de cabeça. Eu tenho usado o Modelsify ultimamente porque a consistência dos personagens é realmente impecável - ela se mantém a mesma em imagens e vídeos sem precisar de 50 loras diferentes. Definitivamente é top para realismo
> 
> > **peligroso** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe1u2t4/) · 2 points
> > 
> > É só uma camada em cima do Z-Image e LTX, cara. Está tudo na sua cabeça

> **bethworldismine** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe1fi1k/) · \-6 points
> 
> Além disso, a lora que você compartilhou é para a base 9b, não para a 9b.
> 
> > **FreezaSama** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe1he97/) · 4 points
> > 
> > Há alguma diferença? Sou novato aqui
> > 
> > > **TheSlateGray** · [2026-04-03](https://reddit.com/r/comfyui/comments/1sb7xdn/comment/oe1ybwm/) · 2 points
> > > 
> > > Na verdade, não quando se trata de loras. Nós treinamos na base porque é para isso que serve.