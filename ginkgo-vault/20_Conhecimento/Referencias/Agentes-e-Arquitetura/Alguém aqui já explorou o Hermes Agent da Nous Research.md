---
title: "Alguém aqui já explorou o Hermes Agent da Nous Research?"
source: "https://www.reddit.com/r/LocalLLM/comments/1t47ec0/has_anyone_here_explored_hermes_agent_by_nous/"
author:
  - "[[ComparisonLiving6793]]"
published: 2026-05-05
created: 2026-06-27
description: "Eu tenho visto isso aparecer com mais frequência em conversas sobre agentes de IA e automação. Pelo que entendi, não é apenas mai"
tags:
  - "clippings"
---
Eu tenho visto isso aparecer com mais frequência em conversas sobre agentes de IA e automação.

Pelo que entendi, não é apenas mais um chatbot ou assistente de programação, já que é posicionado como um agente de IA autoaperfeiçoável e persistente que:

- Aprende com interações passadas e constrói memória de longo prazo
- Cria e refina suas próprias “habilidades” ao longo do tempo
- Funciona de forma contínua (por exemplo, em um servidor ou VPS) em vez de ser baseado em sessão
- Integra-se entre plataformas como Slack, Telegram, CLI, etc.

Parece que está avançando em direção a algo mais próximo de um verdadeiro “operador de IA” em vez de uma ferramenta que você solicita a cada vez, o que é uma mudança bastante significativa na forma como pensamos sobre IA na prática.

**Ansioso para ouvir de qualquer um que tenha:**

- De fato implementado isso (localmente ou em um ambiente de equipe)
- Encontrado casos de uso reais além da experimentação

Particularmente interessado em saber se isso é genuinamente útil em fluxos de trabalho de produção ou ainda é mais um “conceito promissor” do que uma ferramenta prática!

---

## Comments

> **Winter-Editor-9230** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0hi2e/) · 12 points
> 
> É muito mais refinado do que openclaw se você usar corretamente. Muito intuitivo também.
> 
> > **Due-Tangelo-8704** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0m8gs/) · 5 points
> > 
> > o que ele faz melhor que openclaw?
> > 
> > > **Sufficient\_Prune3897** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0sl5b/) · 10 points
> > > 
> > > Segurança, estabilidade, solicitação, gerenciamento de tokens. Praticamente tudo.
> 
> > **florinandrei** · [2026-05-11](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ol81erz/) · 3 points
> > 
> > Meu maior problema com o OpenClaw é que ele foi construído de maneira descuidada. Pequenos bugs chatos que ficam por aí, que um ser humano teria descoberto imediatamente. Parece que eles estão confiando demais no desenvolvimento puramente em IA, ou talvez a forma como usam a IA seja descuidada.
> > 
> > Como o Hermes se compara nesse aspecto?
> > 
> > > **Winter-Editor-9230** · [2026-05-11](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ol86j1t/) · 1 points
> > > 
> > > Hermes é muito mais bem construído profissionalmente
> > > 
> > > **Character-Pudding872** · [2026-05-25](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/onp4e1k/) · 1 points
> > > 
> > > Eu acho que, de forma geral, era só coisas gimmicky.
> > > 
> > > A Nous Research parece ser muito mais séria do que OpenClaw e Moltbook kkk.
> 
> > **MathmoKiwi** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/om3o4zh/) · 1 points
> > 
> > OpenClaw, no entanto, é muito mais rápido: [https://x.com/atomicbot\_ai/status/2055405319455715373](https://x.com/atomicbot_ai/status/2055405319455715373)
> > 
> > > **Daniel15** · [2026-05-21](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/on0dwnf/) · 1 points
> > > 
> > > Esse benchmark é meio burro já que eles não usaram raciocínio para o OpenClaw, mas raciocínio médio para o Hermes (os valores padrão para cada um). Claro que vai demorar mais quando se usa raciocínio.

> **One\_Key\_8127** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0j029/) · 17 points
> 
> Eu configurei em um mini pc, com LLM servido pelo Mac Studio. Eu testei com o Gemma4 26b a4b local até que ele modificou seus próprios scripts em python e os bagunçou, e eu tive que consertar isso sozinho (bom, na verdade, eu dei o script bagunçado para o claude e ele consertou).
> 
> Aí eu mudei para o Qwen3.6 35b a3b (ainda local no Mac Studio). Ele navega bem na web, definitivamente consegue fazer as coisas - ele configurou o tailscale e OpenWebUI para que eu possa conversar com ele pelo smartphone, ele configurou o hermes webui que é outra forma de conversar com ele pelo smartphone. Enviar e-mails foi uma dor de cabeça, mas eu consegui fazer funcionar, e agora ele navega na web e busca alguns itens que eu gostaria de comprar em mercados de segunda mão e me envia um e-mail se algo interessante aparecer. Ele procura novos lançamentos de modelos e me informa sobre eles para que eu não precise ficar verificando pessoalmente.
> 
> Ele consome quantidades ridículas de tokens, especialmente os em cache. Eu tinha um limite padrão de 60 chamadas de ferramenta e era muito baixo, eu aumentei para 90, depois para 150 e depois para 300. Eu pedi para ele trabalhar duro e validar o trabalho, e ele está tranquilo em fazer 300+ chamadas de ferramenta para alcançar o objetivo. Estou tranquilo com o uso de tokens porque é meu hardware; se você paga por tokens, definitivamente precisa de um modelo com cache de prompts com desconto e precisa configurá-lo de acordo (limite de chamadas de ferramenta mais baixo, instruções para seguir as direções em vez de ser proativo e explorar opções alternativas, etc.) porque os custos vão ser brutais.
> 
> Por outro lado, um modelo forte provavelmente usará muito menos iterações e menos tokens. A diferença entre Qwen3.6 35b a3b e Sonnet é enorme. Mas funciona, e se você disser para ele ser minucioso e fazer muitas pesquisas e navegação na web antes de dar uma resposta - ele vai.
> 
> > **ganonfirehouse420** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0s9f9/) · 4 points
> > 
> > Mastigando fichas infinitas? Como é típico de uma ferramenta de agente.
> > 
> > > **FinancialMoney6969** · [2026-05-12](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/olg3g3a/) · 1 points
> > > 
> > > Modelos estúpidos... Depende do que você está fazendo, né
> 
> > **Global-Respond-9796** · [2026-05-14](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/olpx1gp/) · 2 points
> > 
> > mano, eu tentei no quen 2.5 14B 4 bit, por que caramba é tão lento
> > 
> > > **One\_Key\_8127** · [2026-05-14](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/olqv0kt/) · 1 points
> > > 
> > > seu modelo denso, usa 14B parâmetros para produzir cada token. Qwen3.6 35b a3b usa apenas 3B parâmetros para produzir cada token. Qwen2.5 está obsoleto, use Qwen3.6 35b a3b, ou se você não conseguir encaixar isso na sua VRAM, então será melhor com GPT-OSS-20b que também é MoE e vai rodar rápido.
> > > 
> > > A propósito, depois de brincar com isso por um tempo, estou bem decepcionado. Não tenho certeza se é um problema com o Qwen ou o Hermes, mas não consegue entregar o trabalho. Os crons continuam quebrando, o gateway continua quebrando (isso quebra todas as integrações), quando conserta uma coisa, quebra 3 outras. Acho que vou tentar voltar para o Gemma e ver se isso ajuda. Caso contrário, posso esperar pelo lançamento do Qwen3.6 122b a10b, ou mudar para claw, ou investir em hardware melhor para rodar modelos Minimax ou densos de ~30b.
> > > 
> > > > **Global-Respond-9796** · [2026-05-14](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/olr8zv1/) · 1 points
> > > > 
> > > > ig vai usar openrouter e um dos mais baratos deles, deve ser melhor que gpt-oss, estava apenas testando coisas no verão, a pobreza pega pesado lol
> > > > 
> > > > > **dzr0001** · [2026-05-14](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/oltw1td/) · 1 points
> > > > > 
> > > > > Com o que você está servindo a Qwen? Eu tive um aumento massivo na performance quando mudei para vllm-mlx de llama.cpp.

> **HumanDrone8721** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0htyw/) · 7 points
> 
> Há também um AMA com a equipe por trás disso:
> 
> [https://old.reddit.com/r/LocalLLaMA/comments/1suw9on/ama\_announcement\_nous\_research\_the\_opensource\_lab/](https://old.reddit.com/r/LocalLLaMA/comments/1suw9on/ama_announcement_nous_research_the_opensource_lab/)
> 
> Eles ouvem os pedidos de recursos e dão conselhos para novos usuários.
> 
> > **Most-Fill6278** · [2026-05-09](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/okqvqyq/) · 1 points
> > 
> > Valeu, cara. Eu continuo vendo atualizações e ainda estou no terminal. Pelo menos o openclaw me ensinou muito porque eu realmente passei bastante tempo consertando as coisas LOL
> > 
> > > **slow70** · [2026-05-15](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/olzzs3x/) · 1 points
> > > 
> > > Estou aqui apenas aprendendo quais são os limites de token....
> > > 
> > > Como alguém que não tem um pé nesse ecossistema - parece que tenho muito a aprender.
> 
> > **MathmoKiwi** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/om3olg7/) · 1 points
> > 
> > Isso não é o AMA real, isso é:
> > 
> > [https://www.reddit.com/r/LocalLLaMA/comments/1sz2y76/ama\_with\_nous\_research\_ask\_us\_anything/](https://www.reddit.com/r/LocalLLaMA/comments/1sz2y76/ama_with_nous_research_ask_us_anything/)
> > 
> > > **HumanDrone8721** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/om3t5c2/) · 1 points
> > > 
> > > Obrigado pela correção.

> **joshualander** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0iazh/) · 5 points
> 
> Formado da OpenClaw para a Hermes no mês passado.
> 
> > **Thistlemanizzle** · [2026-05-06](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok6mtue/) · 4 points
> > 
> > Qual tem sido sua experiência?

> **lilbittygoddamnman** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0kces/) · 4 points
> 
> Sim, eu uso quase exclusivamente desde que descobri. Não é perfeito, mas funciona muito bem. Definitivamente sou fã.

> **Necessary-Assist-986** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0gnqb/) · 2 points
> 
> Parece mais um conceito promissor agora, especialmente para agentes persistentes, mas ainda é cedo para uso em produção estável.  
> Ótimo para experimentação, especialmente se você quiser explorar memória de longo prazo e fluxos de trabalho autônomos.

> **putrasherni** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0iu6y/) · 2 points
> 
> É, tá tranquilo
> 
> Tem seus pontos fortes e fracos
> 
> Isso faz memória especialmente bem e se melhora

> **Riseing** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok1ot18/) · 2 points
> 
> Eu achei muito lento, e consome fichas a milhões. Voltei para o pi.
> 
> > **slacy** · [2026-05-12](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ola5pu1/) · 1 points
> > 
> > O Pi é mais um agente pessoal persistente ou é apenas para codificação interativa?
> > 
> > > **screenslaver5963** · [2026-05-14](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/olpn2u0/) · 1 points
> > > 
> > > coding interativo, embora seja super extensível.
> 
> > **FinancialMoney6969** · [2026-05-12](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/olg3lg4/) · 1 points
> > 
> > o que você estava usando para alimentá-lo? qual LLM?

> **donotfire** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok1qyip/) · 2 points
> 
> Tem algumas ideias ótimas, mas ainda acho que vale mais a pena construir seu próprio agente. Se você tem o conhecimento, nada supera uma configuração totalmente personalizada.
> 
> > **SkyberSec123** · [2026-05-06](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/okc17rx/) · 1 points
> > 
> > Alguns recursos?
> > 
> > > **donotfire** · [2026-05-06](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/okcaxww/) · 1 points
> > > 
> > > Carregue qualquer sistema agente no Claude Code e pergunte como ele funciona. Eu recomendaria meu repositório [Second Brain](https://github.com/henrydaum/second-brain) , já que é menor e mais fácil de entender, mas ainda cobre tudo. Para fazê-lo, não me baseei em nenhum recurso publicado, foram principalmente tentativas e erros.
> > > 
> > > E, para ser sincero, eu sugeriria jogar Factorio se você ainda não jogou, é uma ótima inspiração para projetos de software.
> > > 
> > > > **Such\_Distribution789** · [2026-05-07](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/okhzufs/) · 1 points
> > > > 
> > > > Pergunta genuína, como Factorio se conecta a isso? Eu vi uma vez antes como um jogo de sobrevivência em um planeta alienígena.
> > > > 
> > > > > **donotfire** · [2026-05-07](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/okifxlg/) · 1 points
> > > > > 
> > > > > Você constrói uma fábrica e isso envolve muita otimização. As fábricas acabam parecendo um pouco com uma placa de circuito. É como se fosse redstone do Minecraft em esteroides. É muito divertido. Peter Steinberger é fã.
> > 
> > > **jonydevidson** · [2026-05-10](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ol2ayp9/) · 1 points
> > > 
> > > Repositórios Codex, Pi e Hermes no github.

> **This\_Maintenance\_834** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok2z0y5/) · 2 points
> 
> para mim funciona muito melhor do que openclaw. quando você tenta mudar o modelo de backend, ele realmente muda. openclaw deixou o padrão muito baixo.

> **Sirius\_Sec\_** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok43lw6/) · 2 points
> 
> Eu troquei para hermes. Open claw estava travando diariamente. Estou usando hermes há uma semana sem problemas.

> **Otherwise\_Wave9374** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok0kvde/) · 2 points
> 
> Eu não implantei o Hermes especificamente, mas a ideia do "agente persistente" tende a falhar nos mesmos lugares:
> 
> 1. Memória: você precisa de uma memória que seja escopo (por projeto/usuário) e versionada, caso contrário, ela se desvia
> 2. Habilidades: trate as habilidades como código, testes, avaliações e changelogs
> 3. Segurança: tenha acesso a ferramentas em sandbox e tenha níveis de permissão explícitos
> 
> Se você tentar, eu começaria com um loop estreito (como triagem de problemas do GitHub ou geração de relatórios noturnos) onde você pode medir a confiabilidade.
> 
> Estamos coletando alguns padrões práticos de guarda-fatos/memória para agentes de longa duração em [https://www.agentixlabs.com/](https://www.agentixlabs.com/) caso seja útil.

> **parxyval** · [2026-05-06](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/okc5apd/) · 1 points
> 
> desculpe pela pergunta provavelmente boba, ainda estou começando com isso. é como uma alternativa ao OpenClaw?

> **pink\_daemon** · [2026-05-25](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ontn7ph/) · 1 points
> 
> Ainda não. Estou um pouco cético em relação à empresa. Alguém tem boas fontes para conhecê-los melhor?

> **Farenheith200** · [2026-06-01](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/op4c3kc/) · 1 points
> 
> Para mim, o melhor agente para usar com modelos locais até agora, mas você precisa limitar o Kanban nos cartões em progresso para não sobrecarregar todo o seu hardware

> **Snoo\_81913** · [2026-06-10](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/oqx7phw/) · 1 points
> 
> Hermes escreveu isso?

> **Thistlemanizzle** · [2026-05-05](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/ok4p79j/) · 1 points
> 
> Está sendo spamado sem parar em vários subreddits de LLM.
> 
> Nunca vou usar isso por causa de quão incrivelmente spammys a equipe tem sido.
> 
> > **ampereAlpha1111** · [2026-05-12](https://reddit.com/r/LocalLLM/comments/1t47ec0/comment/olg3j1t/) · 1 points
> > 
> > sim, definitivamente tem muito marketing rolando, nunca tinha ouvido falar disso e nos últimos dois dias estou vendo em todo lugar; eles mesmos inserem seu agente em muitas respostas no twitter
> > 
> > O Twitter está cheio desse tipo de anúncio ultimamente