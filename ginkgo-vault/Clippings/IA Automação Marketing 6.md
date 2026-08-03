---
title: "IA Automação Marketing"
source: "https://chatgpt.com/c/6a5d6741-3124-83e9-b486-4a5c45e48043"
author:
published:
created: 2026-07-23
description: "ChatGPT conversation with 6 messages"
tags:
  - "clippings"
---
**Você disse**

Notícias, Benchmarks, Cases de uso, Produtos, tudo relacionado a ia e automação, marketing, criação de conteúdo, gestão de tráfego.

---

A tarefa foi criada.

Todos os dias, pela manhã (janela flexível em torno das 08:00, no seu fuso horário), você receberá um resumo com:

- Notícias mais relevantes de IA.
- Benchmarks de modelos, ferramentas e plataformas.
- Cases reais de uso em empresas.
- Lançamentos de produtos e atualizações importantes.
- Automação (n8n, agentes, MCP, APIs, workflows, RPA).
- Marketing digital e growth.
- Criação de conteúdo (vídeo, imagem, copy e redes sociais).
- Gestão de tráfego (Meta, Google, TikTok, LinkedIn e novas estratégias).
- Oportunidades práticas para aplicar na Ginkgo AI Systems, com foco em ganho de eficiência, novos produtos e diferenciais competitivos.

O resumo priorizará informações acionáveis em vez de apenas listar notícias.

---

**20 de julho de 2026**

## 1\. Modelos chineses avançam sobre a fronteira aberta

A Moonshot AI apresentou o **Kimi K3**, modelo open-weight com 2,8 trilhões de parâmetros e janela de contexto de até 1 milhão de tokens. A empresa posiciona o modelo para programação, raciocínio e execução de tarefas longas. Os pesos completos estão previstos para 27 de julho, portanto boa parte dos resultados divulgados ainda precisa de validação independente. [^1]

A Alibaba também anunciou o **Qwen3.8 Max**, com 2,4 trilhões de parâmetros, afirmando desempenho próximo aos modelos proprietários de fronteira. O movimento reforça uma tendência: modelos abertos estão deixando de ser apenas alternativas econômicas e começando a competir em tarefas especializadas. [^2]

**Impacto prático:** não migrar infraestrutura imediatamente. Criar uma camada de roteamento — LiteLLM ou gateway próprio — para testar Kimi, Qwen, GLM, OpenAI, Anthropic e Gemini no mesmo workflow.

**Teste recomendado para a Ginkgo:**

| Tarefa | Métrica principal |
| --- | --- |
| Atendimento Leaf | resolução correta e custo por conversa |
| Geração de landing page | qualidade visual e correções necessárias |
| Agentes n8n | sucesso no uso de ferramentas |
| RAG empresarial | precisão, citações e alucinações |
| Programação | tarefas concluídas sem intervenção |

O modelo vencedor não será necessariamente o mais inteligente. Será o que entregar a tarefa com menor combinação de **custo + latência + retrabalho**.

---

## 2\. Benchmark importante: medir o agente, não apenas o modelo

O novo **RuBench 1.0** avaliou agentes de programação em tarefas reais de manutenção de repositórios. A melhor configuração resolveu 78,7% das tarefas, mas o estudo encontrou um detalhe crítico: em 20% dos testes de uma configuração, o produto substituiu silenciosamente o modelo solicitado por outro modelo de fallback. [^3]

Isso confirma uma falha comum dos benchmarks: o resultado pode representar o conjunto **modelo + prompt + ferramenta + sandbox + política de fallback**, e não o modelo isolado.

**Aplicação direta:** o benchmark interno da Ginkgo deve registrar:

- modelo efetivamente utilizado;
- chamadas de ferramentas;
- número de tentativas;
- tokens e custo;
- duração;
- intervenção humana;
- motivo da falha;
- resposta final validada.

Sem essa telemetria, comparar modelos é como avaliar pilotos sem saber qual carro cada um dirigiu.

---

## 3\. Google transforma agentes em infraestrutura gerenciada

O Google está ampliando sua plataforma de agentes empresariais com APIs gerenciadas, execução em sandbox, pesquisa paralela na web e suporte à criação de aplicações multiagente. A proposta é reduzir o trabalho de provisionar infraestrutura, ferramentas e ambientes de execução. [^4]

O movimento mostra uma mudança importante:

> O mercado está saindo do “chat com IA” e entrando no “agente como infraestrutura”.

**Oportunidade para a Ginkgo:** manter o n8n como orquestrador visual, mas transferir tarefas longas ou que exigem execução de código para runtimes especializados.

Arquitetura indicada:

```
WhatsApp / Dashboard
        ↓
      Leaf
        ↓
 n8n — roteamento e regras
        ↓
Agente especializado em sandbox
        ↓
Supabase / CRM / APIs / documentos
        ↓
Validação + log + resposta
```

O n8n deve funcionar como torre de controle, não como avião, piloto e aeroporto ao mesmo tempo.

---

## 4\. OpenAI direciona agentes para código e Workspace

A OpenAI está descontinuando o Agent Builder e o produto separado de Evals, recomendando o **Agents SDK** para agentes construídos em código e os agentes de Workspace para fluxos configurados por linguagem natural. O encerramento está previsto para 30 de novembro de 2026. [^5]

A empresa também divulgou que seus usuários internos mais intensivos já operam mais de 60 horas diárias de execução paralela de agentes Codex, demonstrando que o ganho não vem apenas da velocidade individual, mas da paralelização. [^6]

**Consequência estratégica:** fluxos críticos não devem depender exclusivamente de construtores visuais proprietários.

Para os produtos Ginkgo:

- protótipos: n8n e builders visuais;
- produção: workflows versionados em Git;
- tarefas críticas: Agents SDK, Python ou TypeScript;
- avaliação: testes próprios executados no CI;
- fallback: modelos e provedores intercambiáveis.

---

## 5\. TikTok começa a combater “fazendas de conteúdo IA”

O TikTok anunciou testes para detectar contas dedicadas a publicar spam gerado por IA, especialmente em política, notícias, finanças e saúde. A plataforma também entrou no comitê diretor da C2PA e está expandindo rotulagem e educação sobre conteúdo sintético. [^7]

Nos primeiros três meses de 2026, o TikTok afirma ter removido mais de 86 milhões de contas falsas. A plataforma está deixando claro que **volume automatizado sem originalidade será tratado como poluição algorítmica**. [^7]

**Impacto para criação de conteúdo:**

Evitar:

- dezenas de vídeos quase idênticos;
- narrador genérico sobre imagens aleatórias;
- repostagem automática sem transformação;
- contas sem presença humana ou identidade editorial.

Priorizar:

- rosto, mascote ou identidade recorrente;
- opinião original;
- demonstrações reais;
- bastidores;
- casos de clientes;
- conteúdo pesquisável;
- séries narrativas.

Para a Ginkgo, os Hatch Pets e agentes-personagem podem funcionar como assinatura editorial. A IA continua produzindo, mas o público percebe uma entidade reconhecível, não uma linha de montagem soviética de reels.

---

## 6\. Live e experiências interativas ganham força

Uma transmissão musical do TikTok realizada em 2 de julho alcançou mais de 2,1 milhões de espectadores, 5,75 milhões de curtidas e 139 mil comentários. O evento combinou entrevista, votação, recompensas e experiência dentro do aplicativo. [^8]

O case reforça que conteúdo não precisa ser apenas “assistido”. Ele pode ser transformado em **experiência participativa**.

**Aplicações comerciais:**

- demonstração ao vivo do Leaf atendendo clientes;
- auditoria pública de processos;
- criação de landing page em tempo real;
- votação para escolher o próximo produto;
- workshop com diagnóstico automatizado;
- live com oferta e onboarding imediato via WhatsApp.

---

## 7\. Case de marketing: Chime reduz tempo e custo de produção

A Chime construiu uma plataforma interna de criação integrando ferramentas como Midjourney, Runway e Veo. Segundo seu CMO, a empresa reduziu aproximadamente 60% do tempo de produção de campanhas e 30% dos custos de produção em doze meses. [^9]

O aprendizado não é simplesmente “usar IA para gerar imagens”. O ganho veio de transformar várias ferramentas em um pipeline único.

**Modelo replicável na Ginkgo Studio:**

```
Briefing
  ↓
Pesquisa de mercado
  ↓
Ângulos de copy
  ↓
Roteiro
  ↓
Imagem / vídeo / voz
  ↓
Adaptação por canal
  ↓
Aprovação
  ↓
Publicação
  ↓
Coleta de métricas
  ↓
Nova variação
```

O produto vendável não é a imagem gerada. É a **máquina de conteúdo com feedback fechado**.

---

## 8\. Marketing entra na era da descoberta por agentes

A Adobe está desenvolvendo ferramentas voltadas à presença das marcas em respostas de IA, personalização dinâmica de sites, agentes criativos e inteligência de marca. A empresa chama atenção para um novo tipo de tráfego: usuários e agentes pesquisando, comparando e tomando decisões dentro de ambientes de IA. [^10]

Isso amplia o SEO tradicional para algo próximo de:

- AEO — otimização para mecanismos de resposta;
- GEO — otimização para modelos generativos;
- estruturação semântica de produtos;
- conteúdo citável;
- dados acessíveis por API;
- reputação distribuída em múltiplas fontes.

**Ação recomendada para a Ginkgo:**

1. Criar páginas individuais para Leaf, Wave, Pyre e demais produtos.
2. Publicar documentação, FAQ, preços, casos e comparativos.
3. Usar Schema.org e dados estruturados.
4. Criar páginas de casos de uso por segmento.
5. Manter conteúdo técnico indexável, não apenas posts em redes sociais.
6. Disponibilizar catálogo e documentação legível por agentes.

No novo funil, o lead pode conhecer a Ginkgo por meio de outro agente, sem visitar o Instagram primeiro.

---

## Prioridades práticas

## Executar agora

**1\. Benchmark Ginkgo v1**

Criar um conjunto de 20 tarefas reais e comparar os modelos usados pela empresa. Não usar perguntas acadêmicas: usar atendimento, RAG, copy, código, CRM e automação.

**2\. Pipeline Ginkgo Studio**

Centralizar geração, aprovação, publicação e coleta de métricas. O objetivo inicial deve ser reduzir o tempo de produção por peça em pelo menos 50%.

**3\. Conteúdo com identidade**

Adotar personagens, apresentador recorrente ou linguagem visual própria. Evitar conteúdo IA genérico, porque as plataformas estão construindo anticorpos contra isso.

**4\. Preparação para busca por IA**

Transformar o site da Ginkgo em fonte de dados estruturada sobre automação empresarial.

**5\. Roteador multimodelo**

Nenhum produto deve ficar refém de um único provedor. Cada tarefa precisa poder escolher automaticamente o modelo mais eficiente.

## Sinal principal do dia

A vantagem competitiva está migrando do **modelo utilizado** para o **sistema que seleciona, avalia, conecta e supervisiona os modelos**.

Comprar acesso à IA é fácil. Construir uma fábrica que aprende qual máquina usar em cada etapa é onde nasce a margem.

---

## Radar IA, automação e marketing

**21 de julho de 2026**

## Sinal executivo

O mercado está convergindo para cinco movimentos:

1. **Modelos estão virando commodities intercambiáveis.**
2. **Agentes precisam de governança, memória e observabilidade.**
3. **A publicidade está migrando para interfaces conversacionais.**
4. **Conteúdo sintético funciona melhor como laboratório do que como produto final genérico.**
5. **A vantagem competitiva está nos dados proprietários e no ciclo de aprendizagem.**

Em outras palavras: o modelo é o motor; o diferencial é o veículo inteiro.

---

## 1\. OpenAI tenta construir um novo mercado publicitário

A OpenAI está expandindo sua operação de anúncios no ChatGPT, iniciada em fevereiro de 2026. A plataforma ainda opera em poucos países e possui ferramentas de segmentação e mensuração menos maduras que Google e Meta, embora já esteja adicionando recursos de localização e autosserviço para anunciantes. Analistas consultados pelo *Business Insider* consideram agressivas as projeções internas de crescimento da operação. [^11]

### O que isso significa

A publicidade conversacional não será apenas um banner dentro do chat. O formato tende a capturar uma intenção muito mais explícita:

```
Busca tradicional:
“melhor CRM para clínica”

Interface conversacional:
“Tenho uma clínica com quatro atendentes,
perco leads no WhatsApp e preciso automatizar agendamentos.”
```

Na segunda situação, a plataforma conhece problema, contexto, urgência e critérios de compra.

### Oportunidade para a Ginkgo

Começar a preparar os produtos para **Agentic Commerce**:

- catálogo estruturado;
- preços transparentes;
- demonstrações acessíveis;
- documentação indexável;
- páginas comparativas;
- FAQ orientado a problemas;
- dados Schema.org;
- APIs ou endpoints legíveis por agentes.

A batalha futura não será apenas aparecer no Google. Será ser recomendado quando uma IA montar a shortlist do comprador.

---

## 2\. Modelos chineses tornam a estratégia multimodelo obrigatória

Executivos e autoridades norte-americanas estão debatendo riscos e possíveis restrições a modelos chineses, impulsionados pela adoção de alternativas abertas e relativamente econômicas, como Kimi K3 e Qwen3.8 Max. Existem divergências sobre segurança, competição e o risco de regulações favorecerem grandes fornecedores norte-americanos. [^12]

O lançamento do Qwen3.8 Max também reforça a expectativa de um mercado **model-agnostic**, no qual empresas selecionam diferentes modelos conforme tarefa, preço e desempenho. [^13]

### Impacto técnico

Usar diretamente um provedor em todos os workflows cria três riscos:

- aumento inesperado de preço;
- indisponibilidade ou restrição regional;
- perda de competitividade quando outro modelo se torna melhor.

### Arquitetura indicada

```
Produto Ginkgo
      ↓
Model Gateway
      ↓
┌─────────────┬─────────────┬─────────────┐
│ OpenAI      │ Anthropic   │ Google      │
│ Qwen/Kimi   │ Open models │ Model local │
└─────────────┴─────────────┴─────────────┘
      ↓
Avaliação automática
      ↓
Custo + qualidade + latência + segurança
```

**Ferramentas relevantes:** LiteLLM, OpenRouter para experimentação, Langfuse ou LangSmith para observabilidade e um catálogo interno de modelos no Supabase.

Para informações sensíveis, modelos estrangeiros ou serviços externos devem ser avaliados quanto a retenção, jurisdição e tratamento de dados antes de entrar em produção.

---

## 3\. Benchmark relevante: custo versus desempenho, não apenas pontuação

O Claude Sonnet 5 foi lançado com preço promocional de **US$ 2 por milhão de tokens de entrada e US$ 10 por milhão de saída até 31 de agosto de 2026**. Depois, os preços informados passam para US$ 3 e US$ 15, respectivamente. Segundo a Anthropic, o modelo melhora o Sonnet 4.6 em tarefas de pesquisa agentiva e uso de computador e pode alcançar o Opus 4.8 em algumas configurações de esforço. [^14]

Isso introduz uma variável importante: **esforço de inferência configurável**.

O mesmo modelo pode operar como:

- resposta rápida e barata;
- análise intermediária;
- execução longa e mais cara.

### Benchmark Ginkgo recomendado

Não comparar apenas “modelo A versus modelo B”. Comparar configurações:

| Cenário | Configuração avaliada |
| --- | --- |
| Atendimento simples | modelo econômico, esforço baixo |
| Qualificação de lead | modelo intermediário |
| RAG técnico | esforço médio + busca |
| Planejamento de campanha | esforço alto |
| Código e correção de workflows | modelo avançado + ferramentas |
| Validação final | segundo modelo independente |

### Métrica principal

```
Custo real por tarefa aceita =
tokens + ferramentas + tentativas + tempo humano de correção
```

Um modelo de US$ 0,01 que exige vinte minutos de revisão pode ser mais caro que um de US$ 0,20 que entrega corretamente de primeira.

---

## 4\. Agentes entram na fase de engenharia de contexto

O n8n publicou novos materiais sobre memória e padrões de produção para agentes. A orientação central é que LLMs começam sem memória persistente, portanto agentes de longa duração precisam separar histórico, contexto operacional, conhecimento e estado da tarefa. [^15]

A plataforma também destaca validação, governança, recuperação de erros e controle de custos como componentes fundamentais de arquiteturas agentivas em produção. [^16]

### Modelo de memória para Leaf e Sylvia

```
Memória de trabalho
Redis
Últimas mensagens, estado atual e locks

Memória episódica
Supabase/Postgres
Conversas, decisões e eventos anteriores

Memória semântica
Vector store
Documentos, políticas, produtos e conhecimento

Memória operacional
Postgres
Tarefas, ferramentas usadas, erros e resultados

Perfil do cliente
CRM
Preferências, estágio, histórico comercial e consentimentos
```

O erro comum é despejar tudo dentro do prompt. Isso transforma o agente em um quarto onde alguém jogou todos os arquivos no chão e pediu velocidade.

### Regra operacional

Cada agente deve receber somente:

- objetivo atual;
- contexto mínimo necessário;
- ferramentas permitidas;
- política aplicável;
- formato de saída;
- critério de conclusão.

---

## 5\. Governança de conteúdo automatizado vira categoria de produto

Plataformas de martech estão adicionando camadas que verificam conteúdo produzido por IA antes da publicação. A Stensul, por exemplo, adicionou filtros de governança de marca para texto e imagem; a Quiq apresentou um sistema para restringir agentes de atendimento às políticas da empresa. [^17]

### Tendência

O próximo software de criação não venderá apenas “gerar mais rápido”. Ele venderá:

- aprovação automática;
- conformidade de marca;
- validação jurídica;
- checagem factual;
- proteção de dados;
- registro de autoria;
- histórico de versões;
- explicação de por que a peça foi aprovada.

### Produto possível: Ginkgo Brand Guardian

Um módulo acoplado ao Pyre/Nyra:

```
Conteúdo gerado
      ↓
Validação de identidade visual
      ↓
Validação de tom e promessa
      ↓
Checagem de política da plataforma
      ↓
Checagem factual
      ↓
Análise de risco
      ↓
Aprovação humana ou publicação
```

Isso pode ser vendido como infraestrutura independente para agências e equipes de marketing.

---

## 6\. TikTok: IA escala testes, humanos sustentam confiança

Marcas e vendedores do TikTok Shop estão utilizando vídeos e influenciadores sintéticos para produzir mais variações de anúncios. Há relatos de conteúdos gerados por IA obtendo vendas, mas também preocupações com demonstrações irreais, baixa confiança e possíveis violações de regras publicitárias. [^18]

O TikTok vem incorporando agentes em suas ferramentas criativas. O Symphony Agent utiliza objetivos da marca, informações da plataforma e sinais de desempenho para ajudar anunciantes a desenvolver criativos dentro de uma experiência conversacional. [^19]

### Estratégia mais sólida

Usar IA em três fases:

**Fase 1 — Exploração**

Gerar dezenas de:

- hooks;
- roteiros;
- ângulos;
- ofertas;
- thumbnails;
- estruturas narrativas.

**Fase 2 — Validação barata**

Testar variações sintéticas ou semiproduzidas com orçamento limitado.

**Fase 3 — Escala humana**

Os conceitos vencedores recebem:

- creator real;
- demonstração autêntica;
- melhor edição;
- prova social;
- investimento maior.

A IA funciona como túnel de vento. Não precisa necessariamente pilotar o avião diante do público.

---

## 7\. Criativo e mídia estão se fundindo

As soluções apresentadas pelo TikTok em 2026 conectam criação, descoberta, dados de intenção e ativação de campanha. A plataforma posiciona IA não apenas como geradora de peças, mas como camada que ajuda a converter sinais culturais em decisões de mídia. [^20]

O Google segue caminho semelhante ao adaptar anúncios para experiências de busca com IA. Os novos formatos são criados para responder à consulta individual e oferecer contexto durante a decisão de compra. [^21]

### Consequência para gestão de tráfego

A estrutura antiga:

```
Copywriter → Designer → Gestor → Relatório
```

está evoluindo para:

```
Dados → Hipótese → Criativo → Campanha
  ↑                            ↓
  └──── Aprendizado contínuo ──┘
```

### O Wave deveria armazenar

- conceito do anúncio;
- hook;
- promessa;
- dor explorada;
- persona;
- formato;
- modelo usado;
- criativo;
- audiência;
- investimento;
- CTR;
- retenção;
- CPA;
- ROAS;
- conversão final.

Assim, o sistema aprende **por que** uma campanha venceu, e não apenas qual anúncio venceu.

---

## 8\. Case de uso: IA como sistema operacional empresarial

A Endava relatou integrar agentes em engenharia de software e expandir o uso para jurídico, finanças e operações. Entre os resultados divulgados estão aceleração do desenvolvimento, redução de relatórios e coordenação manuais e capacidade de equipes criarem ferramentas internas sem depender integralmente de engenharia. [^22]

### Aprendizado

O maior retorno tende a surgir quando a IA atravessa vários departamentos.

Exemplo:

```
Lead entra
  ↓
Leaf qualifica
  ↓
CRM atualiza
  ↓
Wave cria audiência
  ↓
Pyre gera conteúdo
  ↓
Alfred mede custo e receita
  ↓
Sylvia identifica gargalos
```

Produtos isolados geram receita. Um sistema integrado gera dependência operacional positiva e maior retenção.

---

## Oportunidades práticas priorizadas

## P0 — Instrumentação de campanhas

Criar um **Creative Performance Ledger** no Supabase, relacionando cada anúncio aos seus componentes criativos e resultados. Sem isso, a IA apenas produz; não aprende.

## P0 — Gateway multimodelo

Padronizar todas as chamadas da Ginkgo por uma camada central com:

- fallback;
- limite de orçamento;
- roteamento por tarefa;
- registro do modelo real;
- cache;
- políticas de dados.

## P1 — Ginkgo Brand Guardian

Construir um validador de marca, conformidade, factualidade e política de plataforma para Pyre e Nyra.

## P1 — Memória estruturada da Sylvia

Separar memória de trabalho, episódica, semântica e operacional. Não usar o banco vetorial como gaveta universal.

## P2 — Preparação para anúncios conversacionais

Criar páginas e catálogos legíveis por mecanismos de IA, antecipando ChatGPT Ads, AI Search e agentes compradores.

---

## Stack tática da semana

| Necessidade | Ferramentas |
| --- | --- |
| Gateway de modelos | LiteLLM |
| Observabilidade | Langfuse ou LangSmith |
| Memória rápida | Redis |
| Histórico operacional | Supabase/Postgres |
| Conhecimento | pgvector, Qdrant ou Vector Redis |
| Orquestração | n8n + workers Python/TypeScript |
| Avaliação | dataset próprio + CI |
| Conteúdo | Pyre/Nyra + APIs de geração |
| Tráfego | Meta, Google e TikTok APIs |
| Analytics | Metabase ou dashboard próprio |

## Indicador central do dia

**O conteúdo deixa de ser o ativo principal. O ativo passa a ser o banco de hipóteses, resultados e aprendizados que produz o próximo conteúdo.**

Quem apenas gerar mais peças entrará numa guerra de volume. Quem construir memória criativa terá um sistema que melhora enquanto os concorrentes continuam apertando “regenerate”.

---

## Radar diário — IA, automação e growth

**22 de julho de 2026**

## Leitura executiva

O sinal mais relevante não é um novo “modelo supremo”. É a migração para uma arquitetura de **modelos rápidos e baratos, mensuração de tráfego vindo de agentes e controle mais rigoroso sobre conteúdo sintético**.

A consequência para negócios é direta:

```
Mais IA disponível
        ↓
Mais conteúdo e automações parecidas
        ↓
Menor vantagem por ferramenta
        ↓
Maior valor em dados, distribuição, marca e avaliação
```

---

## 1\. Google lança três novos modelos Gemini focados em escala

Em **21 de julho**, o Google anunciou:

- **Gemini 3.6 Flash**: modelo generalista rápido, voltado a agentes e programação;
- **Gemini 3.5 Flash-Lite**: opção de menor custo e latência;
- **Gemini 3.5 Flash Cyber**: especializado em segurança cibernética, inicialmente restrito a governos e parceiros confiáveis. [^23]

O lançamento sinaliza uma mudança clara: o mercado empresarial está priorizando **custo por tarefa concluída**, não somente pontuação máxima em benchmarks. [^24]

### Impacto para a Ginkgo

Não usar o mesmo modelo para tudo.

| Operação | Perfil de modelo |
| --- | --- |
| Classificação de leads | Flash-Lite |
| Resumo e extração | Flash-Lite |
| Atendimento comum | Flash |
| Construção de workflows | Flash ou modelo avançado |
| Decisão sensível | modelo forte + validação |
| Auditoria | segundo modelo independente |

### Oportunidade imediata

Adicionar ao gateway multimodelo um roteador baseado em:

```
complexidade × risco × latência × orçamento
```

O agente deve começar barato e escalar apenas quando detectar dificuldade. Usar um modelo de fronteira para classificar “sim”, “não” ou “talvez” é como chamar um reator nuclear para carregar um celular.

---

## 2\. Benchmark real: qualidade precisa ser dividida pelo custo operacional

O Google afirma que os novos modelos foram otimizados para eficiência, confiabilidade e operação de agentes em escala. Entretanto, benchmarks publicados pelo próprio fornecedor devem ser tratados como ponto de partida, não como veredito. [^23]

A métrica correta para os produtos da Ginkgo é:

```
Valor por tarefa =
resultado aprovado
÷
(tokens + ferramentas + latência + retrabalho humano)
```

### Benchmark interno recomendado

Criar um dataset com 50 tarefas reais:

- 10 atendimentos Leaf;
- 10 consultas RAG;
- 10 automações n8n;
- 10 peças de conteúdo;
- 10 análises de campanhas.

Registrar:

- modelo efetivamente usado;
- custo total;
- tempo de resposta;
- ferramentas chamadas;
- tentativas;
- intervenção humana;
- erro factual;
- aprovação final.

**Decisão estratégica:** não escolher um “modelo oficial da empresa”. Escolher um vencedor por categoria de tarefa.

---

## 3\. Google Analytics passa a identificar tráfego vindo de assistentes de IA

O Google Analytics adicionou o canal padrão **AI Assistants**, permitindo identificar visitas originadas de serviços como ChatGPT, Gemini, DeepSeek, Copilot e Grok. O agrupamento não inclui o tráfego proveniente do AI Mode ou dos AI Overviews do próprio Google. [^25]

Isso marca a transformação de **GEO/AEO** em um canal mensurável, e não apenas uma tendência conceitual.

### Ações práticas

Criar no GA4 uma visão específica para:

- sessões por assistente;
- página de entrada;
- conversão;
- receita ou lead;
- produto citado;
- taxa de engajamento;
- país;
- campanha assistida.

### Oportunidade de produto

O Wave pode incorporar um painel:

```
AI Discovery
├── ChatGPT
├── Gemini
├── Copilot
├── Claude
├── DeepSeek
└── Grok
```

E cruzar isso com CRM:

```
assistente de origem → landing page → lead → venda
```

Isso permite oferecer **AI Visibility Analytics** como serviço recorrente.

---

## 4\. A busca generativa está reduzindo cliques tradicionais

Um estudo acadêmico analisando 161.382 pares de artigos estimou que a exibição de AI Overviews reduziu aproximadamente **15% do tráfego diário** para páginas da Wikipédia analisadas. O efeito foi maior em assuntos respondidos satisfatoriamente por resumos curtos. [^26]

Outro estudo, com mais de 55 mil consultas, encontrou AI Overviews em 13,7% do total e em 64,7% das consultas formuladas como perguntas. Também identificou que cerca de 11% das afirmações analisadas não eram sustentadas pelas páginas citadas. [^27]

### Impacto para marketing

O funil antigo:

```
pesquisa → clique → site → conversão
```

Está virando:

```
pergunta → resposta da IA → shortlist → visita ou compra
```

### Estratégia correta

O conteúdo precisa cumprir duas funções:

1. Ser compreensível por máquinas.
2. Ser valioso o bastante para justificar o clique humano.

Priorizar:

- comparativos;
- calculadoras;
- demonstrações;
- dados próprios;
- templates;
- ferramentas gratuitas;
- cases detalhados;
- documentação técnica;
- preços e critérios claros.

Artigos genéricos do tipo “o que é automação” tendem a ser engolidos pelo resumo da IA antes de verem a luz do Analytics.

---

## 5\. Plataformas ampliam o combate ao “AI slop”

YouTube, TikTok, Pinterest, Substack e plataformas da Meta estão reforçando políticas, identificação ou mecanismos de redução de conteúdo sintético repetitivo e de baixa qualidade. A tendência não é proibir IA, mas diferenciar **criação assistida** de produção massiva inautêntica. [^28]

No TikTok Shop, vídeos sintéticos estão aumentando o volume de ofertas, mas marcas já demonstram preocupação com demonstrações irreais e perda de confiança. Algumas restringem conteúdo de afiliados criado integralmente por IA. [^29]

### Regra para o Pyre

A IA pode produzir:

- pesquisa;
- variações de hook;
- roteiro;
- storyboard;
- legendas;
- cortes;
- tradução;
- versões por plataforma.

Mas o conteúdo final deve conter pelo menos um elemento proprietário:

- rosto ou personagem reconhecível;
- demonstração real;
- opinião;
- dado próprio;
- case;
- narrativa serializada;
- estilo visual consistente.

**Volume sem identidade virou passivo algorítmico.**

---

## 6\. Case de criação: automação com validação aumenta fidelidade

Uma pesquisa sobre geração automatizada de imagens comerciais apresentou um pipeline com geração, avaliação e supervisão humana. O sistema relatou melhora de **30,77% na fidelidade do objeto comercial** e aumento de **52% na preferência humana** em relação ao resultado-base. [^30]

O aprendizado central é que o ganho veio da camada de avaliação, não apenas do gerador.

### Arquitetura recomendada para Ginkgo Studio

```
Briefing
   ↓
Geração de variações
   ↓
Validação do produto
   ↓
Validação de marca
   ↓
Detecção de artefatos
   ↓
Ranking automático
   ↓
Aprovação humana
   ↓
Publicação
```

### Ferramentas possíveis

- geração: Gemini Image, modelos via Fal ou APIs equivalentes;
- consistência: embeddings visuais e comparação por similaridade;
- aprovação: painel próprio ou Supabase;
- automação: n8n;
- versionamento: armazenamento do prompt, seed, modelo e resultado;
- avaliação: visão computacional + rubric LLM.

O produto não deve ser “gerador de posts”. Deve ser uma **esteira de conteúdo auditável**.

---

## 7\. Gestão de tráfego entra na fase de first-party intelligence

O Google Ads está migrando integrações de conversões offline e Enhanced Conversions for Leads para a **Data Manager API**. Desde 15 de junho de 2026, determinados uploads pela API tradicional passaram a depender de acesso legado. [^31]

Isso reforça a importância de devolver às plataformas o resultado real do funil:

```
clique
  ↓
lead
  ↓
qualificação
  ↓
reunião
  ↓
proposta
  ↓
receita
```

### Impacto para o Wave e Leaf

Integrar os dados do CRM com as plataformas de anúncios permite otimizar não apenas para formulário preenchido, mas para:

- lead qualificado;
- consulta realizada;
- venda;
- valor da venda;
- recorrência;
- margem.

### Prioridade técnica

Construir uma camada de eventos padronizada:

```json
{
  "event": "qualified_lead",
  "lead_id": "internal_id",
  "source": "meta",
  "campaign_id": "campaign",
  "value": 2500,
  "occurred_at": "timestamp",
  "consent": true
}
```

Depois criar adaptadores para Google, Meta, TikTok e analytics. Um evento interno, múltiplos destinos.

---

## Oportunidades priorizadas

## P0 — AI Traffic Dashboard

Adicionar ao Wave acompanhamento de tráfego e conversões provenientes de assistentes de IA.

**Valor comercial:** nova categoria de relatório para clientes antes que a maioria das agências perceba que o tráfego mudou de espécie.

## P0 — Model Router por risco

Implementar seleção automática entre modelos Lite, Flash e avançados.

**Resultado esperado:** reduzir custo sem comprometer tarefas críticas.

## P0 — Creative Performance Ledger

Salvar cada criativo com:

- hook;
- roteiro;
- formato;
- modelo;
- prompt;
- avatar;
- oferta;
- público;
- CTR;
- retenção;
- CPA;
- vendas.

Isso transforma campanha em memória treinável.

## P1 — Brand Guardian

Validador automático de:

- produto;
- identidade visual;
- afirmações;
- conformidade;
- transparência de IA;
- políticas da plataforma.

## P1 — Closed-loop Ads

Conectar Leaf, CRM e Wave para enviar às plataformas eventos de receita e qualificação, e não somente leads brutos.

---

## Stack tática

| Camada | Ferramenta ou abordagem |
| --- | --- |
| Roteamento de modelos | LiteLLM ou gateway próprio |
| Observabilidade | Langfuse |
| Avaliação | dataset interno + rubrics |
| Automação | n8n + workers Python/TypeScript |
| Dados | Supabase/Postgres |
| Analytics | GA4 + painel próprio |
| Conversões | APIs de dados das plataformas |
| Conteúdo | geração multimodelo |
| Validação visual | embeddings + visão |
| Aprendizado criativo | Creative Performance Ledger |

## Sinal central do dia

**2026 está separando empresas que usam IA das empresas que aprendem com cada execução da IA.**

Gerar é barato. Medir, validar, memorizar e realimentar o sistema é onde nasce o verdadeiro motor de crescimento.

---

## Radar diário — IA, automação, conteúdo e growth

**23 de julho de 2026**

## Sinal executivo

O movimento mais importante das últimas horas não é outro chatbot com nome mitológico. É a consolidação de uma nova categoria:

> **Agentes operacionais governados, avaliados continuamente e conectados diretamente aos sistemas da empresa.**

Ao mesmo tempo, marketing e mídia estão adotando **MCP, agentes de campanha e mensuração de presença em respostas de IA**. A vantagem deixa de ser “usar IA” e passa a ser controlar o ciclo:

```
dados → decisão → ação → avaliação → correção → nova ação
```

---

## 1\. OpenAI lança o Presence para agentes de voz e chat em produção

Em **22 de julho de 2026**, a OpenAI anunciou o **OpenAI Presence**, produto empresarial para implantar agentes em atendimento, vendas e fluxos internos de maior risco. A solução combina conhecimento restrito por função, políticas, ações autorizadas, simulações, avaliações, regras de escalonamento humano e um processo de melhoria assistido pelo Codex. O produto está em disponibilidade limitada para clientes empresariais e não é self-service. [^32]

O case interno divulgado é relevante: o agente usado no suporte telefônico da OpenAI estaria resolvendo **75% dos chamados recebidos sem assistência humana**. Um ciclo de melhoria teria reduzido os encaminhamentos humanos em 15 pontos percentuais em dez dias. Esses números são divulgados pela própria empresa e ainda devem ser tratados como resultados do fornecedor, não como benchmark universal. [^32]

### Impacto para Leaf

O Presence valida diretamente a arquitetura que o Leaf deve perseguir:

```
Canal
WhatsApp / voz / chat
        ↓
Agente especializado
        ↓
Políticas + conhecimento permitido
        ↓
Ferramentas autorizadas
        ↓
Ação ou escalonamento humano
        ↓
Avaliação da sessão
        ↓
Proposta de melhoria
```

A mensagem estratégica é clara: **RAG e prompt não formam um produto de atendimento completo**. O produto real inclui políticas, ferramentas, aprovação, avaliação e evolução controlada.

### Oportunidade comercial

Posicionar o Leaf não apenas como “CRM com IA”, mas como:

**Customer Operations Agent para WhatsApp**

Essa formulação aproxima o produto de uma categoria empresarial mais valiosa: resolução operacional, não apenas conversa automática.

---

## 2\. Benchmark realista mostra que agentes ainda falham em automações empresariais

O **AutomationBench** avalia agentes em fluxos que atravessam CRM, e-mail, calendário, mensagens e outras aplicações por APIs. As tarefas exigem descoberta de endpoints, cumprimento de políticas e alteração correta do estado final dos sistemas. Segundo o estudo, mesmo os melhores modelos avaliados ficaram abaixo de **10% de sucesso**. [^33]

Isso parece contradizer demos impressionantes, mas na prática revela a diferença entre:

```
Demo:
“Envie um e-mail para João.”

Operação real:
“Identifique o João correto, valide consentimento,
consulte o CRM, aplique a política comercial,
registre a ação e não duplique o contato.”
```

### Consequência técnica

Fluxos críticos precisam combinar:

- IA para interpretar contexto;
- regras determinísticas para restrições;
- identificadores internos confiáveis;
- validação antes da escrita;
- idempotência;
- confirmação do estado final;
- rollback ou compensação;
- escalonamento humano.

O agente pode dirigir. Os guardrails continuam sendo o guard-rail da estrada — remover ambos para ganhar velocidade costuma acabar em episódio piloto de série distópica.

### Benchmark recomendado para Ginkgo

Avaliar o sistema pelo **estado final**, não pela beleza da resposta:

| Métrica | Exemplo |
| --- | --- |
| Task success | cliente realmente foi atualizado |
| Policy compliance | desconto respeitou o limite |
| Tool accuracy | API e registro corretos |
| Duplicate rate | nenhuma ação repetida |
| Escalation precision | humano acionado quando necessário |
| Recovery rate | workflow recuperado após falha |
| Cost per accepted task | custo total da execução válida |

---

## 3\. MCP avança do desenvolvimento para marketing e publicidade

O ecossistema martech está adotando MCP rapidamente. Entre os lançamentos recentes estão servidores MCP da **6sense** para sinais de intenção de compra, **Omneky** para geração de criativos, **OneSignal** para marketing de ciclo de vida e **Wistia** para consulta e uso de bibliotecas de vídeo. [^34]

O TikTok também apresentou um **TikTok Ads MCP Server**, permitindo que agentes e ferramentas externas atuem sobre desenvolvimento e gerenciamento de campanhas na plataforma. [^35]

### Impacto para o Wave

O Wave pode evoluir de painel de campanhas para **Marketing Agent Control Plane**:

```
Wave
├── Meta Ads adapter
├── Google Ads adapter
├── TikTok Ads MCP
├── Analytics
├── CRM / Leaf
├── Creative Ledger
└── Approval Engine
```

O agente poderia:

1. Ler performance.
2. Identificar anomalias.
3. Gerar hipótese.
4. Criar variações.
5. Propor redistribuição de orçamento.
6. Solicitar aprovação.
7. Executar.
8. Medir impacto incremental.

### Regra de segurança operacional

Não permitir que o agente altere orçamento ilimitadamente. Usar níveis:

```
Até 5% de ajuste → automático
5% a 15% → aprovação rápida
Acima de 15% → revisão humana
Nova campanha → aprovação obrigatória
```

Autonomia sem orçamento máximo é apenas um cartão corporativo entregue a um robô otimista.

---

## 4\. Marketing começa a vender para agentes, não apenas para humanos

Já surgem redes e produtos desenhados para entregar recomendações patrocinadas diretamente a agentes de IA. A **Agents Not Ads**, por exemplo, foi apresentada como uma rede que conecta dados de patrocinadores à intenção capturada em consultas conversacionais. Plataformas como Cision, Profound e serviços especializados também estão medindo frequência, precisão e contexto das aparições de marcas nas respostas de modelos. [^34]

### Nova jornada de compra

```
Antes:
anúncio → clique → landing page → formulário

Agora:
pergunta à IA → comparação → shortlist
→ site ou conversa → compra
```

### Oportunidade para Ginkgo

Criar uma oferta de **AI Visibility Audit** para clientes:

- presença em ChatGPT, Gemini, Claude e Perplexity;
- perguntas em que a marca aparece;
- concorrentes mais citados;
- descrições incorretas;
- fontes usadas pelos modelos;
- lacunas de conteúdo;
- evolução mensal da visibilidade.

O Wave poderia armazenar isso como um canal adicional:

```
Organic Search
Paid Search
Social
Referral
AI Discovery
```

---

## 5\. Conteúdo B2B: autoridade humana ganha valor com a saturação sintética

O LinkedIn reforçou que confiança e comunicação liderada por pessoas se tornam diferenciais à medida que conteúdo gerado por IA se torna abundante. A própria plataforma recomenda respostas específicas a dúvidas dos clientes, terminologia consistente, pontos de vista claros e participação de funcionários e especialistas para aumentar a visibilidade em mecanismos de busca por IA. [^36]

A Meta também declarou que está priorizando conteúdo original e reduzindo a distribuição de publicações reaproveitadas ou pouco transformadas no Facebook. [^37]

### Estratégia para o perfil pessoal e Ginkgo

A IA pode executar a fábrica, mas a tese precisa ter dono.

**Estrutura recomendada:**

```
Gabriel:
visão, opinião, demonstração e decisão

Ginkgo:
frameworks, cases, dados e produtos

Pyre:
pesquisa, roteiro, edição, distribuição e aprendizagem
```

### Formatos com maior valor estratégico

- construção pública do Leaf;
- desmontagem técnica de automações;
- resultados antes/depois;
- decisões arquiteturais;
- erros encontrados em produção;
- benchmark próprio;
- opinião contrária fundamentada;
- demonstrações com dados reais anonimizados.

O conteúdo genérico será produzido em escala infinita. O que permanece escasso é **experiência verificável acompanhada de identidade**.

---

## 6\. Pesquisa de cliente começa a usar “gêmeos digitais” de audiência

A Dovetail expandiu sua plataforma com representações sintéticas de segmentos de clientes, geradas a partir de pesquisas e feedbacks anteriores. A proposta é simular como diferentes perfis reagiriam a conceitos e produtos. Outras ferramentas estão usando entrevistas automatizadas, transcrições e dados qualitativos para produzir mensagens de go-to-market e landing pages. [^34]

### Uso correto

Esses gêmeos não devem substituir clientes reais. Devem funcionar como filtro intermediário:

```
20 ideias
   ↓
Simulação sintética
   ↓
5 hipóteses
   ↓
Teste com audiência real
   ↓
2 vencedoras
   ↓
Escala de mídia
```

### Aplicação no Leaf e Shopify

Criar personas baseadas em:

- reviews reais;
- conversas de suporte;
- objeções comerciais;
- entrevistas;
- pesquisas;
- comportamento de compra.

Depois testar:

- oferta;
- headline;
- preço;
- criativo;
- objeções;
- sequência de WhatsApp.

O ganho está em reduzir ideias ruins antes de gastar mídia, não em declarar que um avatar inventado “validou o mercado”.

---

## 7\. ChatGPT Work demonstra o novo padrão de automação do conhecimento

O ChatGPT Work, lançado em 9 de julho, pode atuar sobre arquivos, aplicativos e web, executar projetos longos e gerar documentos, planilhas, apresentações e sistemas internos. A OpenAI apresentou cases em que a ferramenta identificou falhas de follow-up comercial, reduziu análises de semanas para horas e automatizou processos antes mantidos em Excel. [^38]

Entre os casos divulgados:

- a Zapier identificou potencial de vendas não capturado ao analisar milhares de leads;
- a RingCentral ampliou o suporte operacional de um gestor de produto para cerca de 50;
- a Virgin Atlantic reduziu análises competitivas de semanas para horas;
- a NVIDIA automatizou preparação e avaliação de um grande evento. [^38]

### Impacto para consultorias de automação

O serviço de baixo valor “conectar ferramenta A à ferramenta B” sofrerá pressão.

O valor migra para:

- modelagem do processo;
- organização dos dados;
- definição de políticas;
- arquitetura de permissões;
- integração com sistemas legados;
- avaliação;
- observabilidade;
- governança;
- transformação operacional.

A automação simples está virando recurso nativo. A arquitetura continua sendo serviço premium.

---

## Prioridades práticas para a Ginkgo

## P0 — Agent Evaluation Kernel

Construir um módulo compartilhado entre Leaf, Pyre, Wave e Sylvia para registrar:

- objetivo;
- contexto;
- modelo;
- ferramentas;
- políticas aplicadas;
- estado inicial e final;
- resultado;
- custo;
- escalonamento;
- avaliação automática;
- aprovação humana.

Isso evita que cada produto reconstrua sua própria caixa-preta.

## P0 — Leaf Resolution Engine

Trocar a métrica central de “mensagens respondidas” por:

```
problemas resolvidos
÷
problemas recebidos
```

Métricas complementares:

- resolução sem humano;
- tempo até resolução;
- taxa de reabertura;
- transferência correta;
- satisfação;
- custo por resolução.

## P1 — Wave MCP Gateway

Criar adaptadores padronizados para plataformas de mídia, começando por leitura e recomendação. Escrita e alteração de orçamento entram depois, com aprovação e limites.

## P1 — AI Visibility Audit

Transformar GEO/AEO em oferta comercial recorrente, com monitoramento de presença, concorrência, erros factuais e oportunidades editoriais.

## P1 — Synthetic Audience Lab

Usar dados reais de CRM e entrevistas para simular objeções e priorizar criativos antes de investir em tráfego.

---

## Stack relevante do dia

| Necessidade | Ferramenta ou abordagem |
| --- | --- |
| Orquestração | n8n + workers TypeScript/Python |
| Comunicação entre agentes | MCP + APIs internas |
| Avaliação | rubrics, simulações e estado final |
| Observabilidade | Langfuse + Postgres |
| Políticas | regras versionadas em Git |
| Memória operacional | PostgreSQL |
| Estado temporário | Redis |
| Conteúdo | Pyre + Creative Ledger |
| AI visibility | consultas monitoradas + analytics |
| Controle de mídia | aprovação, limites e auditoria |

## Indicador central

**Taxa de tarefas concluídas corretamente, sem intervenção humana e dentro das políticas.**

Não medir apenas tokens, mensagens ou quantidade de agentes. Um exército de robôs que conversa muito e conclui pouco é apenas uma reunião corporativa automatizada.

[^1]: [reuters.com](https://www.reuters.com/world/china/chinas-moonshot-unveils-worlds-largest-open-ai-model-closing-us-rivals-2026-07-17/?utm_source=chatgpt.com)

[^2]: [wsj.com](https://www.wsj.com/tech/ai/alibaba-says-new-ai-model-is-just-second-to-anthropics-fable-5-ba88a55b?utm_source=chatgpt.com)

[^3]: [arxiv.org](https://arxiv.org/abs/2607.06411?utm_source=chatgpt.com)

[^4]: [developers.googleblog.com](https://developers.googleblog.com/all-the-news-from-the-google-io-2026-developer-keynote/?utm_source=chatgpt.com)

[^5]: [openai.com](https://openai.com/index/introducing-agentkit/?utm_source=chatgpt.com)

[^6]: [openai.com](https://openai.com/index/how-agents-are-transforming-work/?utm_source=chatgpt.com)

[^7]: [newsroom.tiktok.com](https://newsroom.tiktok.com/?lang=en-AU&utm_source=chatgpt.com)

[^8]: [newsroom.tiktok.com](https://newsroom.tiktok.com/?lang=en&utm_source=chatgpt.com)

[^9]: [businessinsider.com](https://www.businessinsider.com/most-innovative-cmos-power-list-2026-6?utm_source=chatgpt.com)

[^10]: [techradar.com](https://www.techradar.com/pro/live/adobe-summit-2026?utm_source=chatgpt.com)

[^11]: [businessinsider.com](https://www.businessinsider.com/openai-projects-chatgpt-ad-growth-market-doubts-2026-7?utm_source=chatgpt.com)

[^12]: [wsj.com](https://www.wsj.com/tech/ai/top-american-ai-execs-sound-alarm-on-chinese-models-3c74f8c1?utm_source=chatgpt.com)

[^13]: [barrons.com](https://www.barrons.com/articles/alibaba-stock-price-new-ai-model-acc68d72?utm_source=chatgpt.com)

[^14]: [anthropic.com](https://www.anthropic.com/news/claude-sonnet-5?utm_source=chatgpt.com)

[^15]: [blog.n8n.io](https://blog.n8n.io/ai-agent-memory/?utm_source=chatgpt.com)

[^16]: [blog.n8n.io](https://blog.n8n.io/agentic-ai-design-patterns/?utm_source=chatgpt.com)

[^17]: [martech.org](https://martech.org/the-latest-ai-powered-martech-news-and-releases/?utm_source=chatgpt.com)

[^18]: [businessinsider.com](https://www.businessinsider.com/tiktok-shop-creators-brands-using-ai-to-replace-human-slop-2026-7?utm_source=chatgpt.com)

[^19]: [newsroom.tiktok.com](https://newsroom.tiktok.com/tiktok-at-cannes-lions-2026?lang=en-150&utm_source=chatgpt.com)

[^20]: [newsroom.tiktok.com](https://newsroom.tiktok.com/tiktok-world-26-turning-discovery-into-business-growth-with-ai-powered-innovations-vertical-experiences-and-high-impact-brand-solutions?lang=en&utm_source=chatgpt.com)

[^21]: [blog.google](https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/?utm_source=chatgpt.com)

[^22]: [openai.com](https://openai.com/index/endava-frontiers/?utm_source=chatgpt.com)

[^23]: [blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/?utm_source=chatgpt.com)

[^24]: [axios.com](https://www.axios.com/2026/07/21/google-gemini-ai-models?utm_source=chatgpt.com)

[^25]: [support.google.com](https://support.google.com/analytics/answer/9164320?hl=en&utm_source=chatgpt.com)

[^26]: [arxiv.org](https://arxiv.org/abs/2602.18455?utm_source=chatgpt.com)

[^27]: [arxiv.org](https://arxiv.org/abs/2605.14021?utm_source=chatgpt.com)

[^28]: [businessinsider.com](https://www.businessinsider.com/ai-slop-substack-youtube-tiktok-pinterest-facebook-instagram-threads-2026-7?utm_source=chatgpt.com)

[^29]: [wsj.com](https://www.wsj.com/cmo-today/ai-videos-are-flooding-tiktok-shop-c86a88e0?utm_source=chatgpt.com)

[^30]: [arxiv.org](https://arxiv.org/abs/2602.13349?utm_source=chatgpt.com)

[^31]: [support.google.com](https://support.google.com/google-ads/answer/12077475?hl=en&utm_source=chatgpt.com)

[^32]: [openai.com](https://openai.com/index/introducing-openai-presence/)

[^33]: [arxiv.org](https://arxiv.org/abs/2604.18934?utm_source=chatgpt.com)

[^34]: [martech.org](https://martech.org/the-latest-ai-powered-martech-news-and-releases/)

[^35]: [newsroom.tiktok.com](https://newsroom.tiktok.com/tiktok-unveils-native-experiences-and-creative-ai-to-power-app-growth-in-southeast-asia?lang=en-SG&utm_source=chatgpt.com)

[^36]: [linkedin.com](https://www.linkedin.com/business/marketing/blog/events/why-trust-is-your-most-valuable-asset-in-the-ai-era?utm_source=chatgpt.com)

[^37]: [about.fb.com](https://about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/?utm_source=chatgpt.com)

[^38]: [openai.com](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)