---
title: "Vizard.ai transformação de conteúdo"
source: "https://chatgpt.com/c/6a6798b7-311c-83e9-b9ec-9cca1437b3ae"
author:
published:
created: 2026-07-27
description: "ChatGPT conversation with 4 messages"
tags:
  - "clippings"
---
**Você disse**

https://vizard.ai/

---

## Vizard.ai — o que ele realmente vende

O Vizard não vende “edição de vídeo com IA”. Ele vende uma transformação operacional:

> **1 vídeo longo entra → dezenas de conteúdos verticais saem prontos para distribuição.**

O núcleo é uma esteira de reaproveitamento de conteúdo:

```
Upload ou URL
   ↓
Transcrição
   ↓
Detecção dos melhores momentos
   ↓
Recorte semântico
   ↓
Autoenquadramento do rosto
   ↓
Legendas + palavras destacadas + emojis
   ↓
Templates da marca
   ↓
Clipes 9:16
   ↓
Agendamento e publicação
```

A promessa pública é transformar um vídeo longo em mais de 30 clipes, com IA escolhendo trechos, reenquadrando os sujeitos e preparando o conteúdo para TikTok, Reels e Shorts. O editor também permite cortar o vídeo apagando partes da transcrição, traduzir legendas, mudar proporções e ajustar uma timeline tradicional. [^1]

---

## O que aparece no vídeo enviado

O vídeo de aproximadamente 64 segundos demonstra bem o resultado padrão do Vizard:

- formato vertical 9:16;
- título inicial em caixa destacada;
- legendas automáticas grandes;
- palavras-chave coloridas;
- emojis contextuais;
- cortes baseados na fala;
- alternância entre o narrador e o cachorro;
- preservação do áudio e da identidade do vídeo original;
- marca “made with Vizard.ai”, provavelmente resultado do plano gratuito.

O resultado é funcional e publicável, mas visualmente ainda é uma commodity. Parece um “CapCut automático”: eficiente, porém facilmente reconhecível.

O ponto importante é que o Vizard **não criou a história**. Ele encontrou, formatou e embalou uma história que já existia. É uma refinaria, não um poço de petróleo.

---

## O verdadeiro produto

## 1\. AI Clipping

O sistema identifica momentos potencialmente interessantes dentro de vídeos longos e gera múltiplos cortes. Cada clipe pode retornar:

- título;
- transcrição;
- duração;
- URL do vídeo;
- nota de viralidade de 0 a 10;
- justificativa da nota;
- temas relacionados;
- link para edição manual.

Os resultados são ordenados por viral score. [^2]

Essa pontuação não significa que o conteúdo ficará viral. É uma classificação heurística baseada em elementos como clareza, emoção, conflito, novidade, ritmo e força do início.

## 2\. Editor baseado em texto

O usuário edita o vídeo como se estivesse alterando um documento:

```
Apagou uma frase da transcrição
        ↓
O trecho correspondente desaparece do vídeo
```

Isso elimina boa parte da curva de aprendizado de Premiere, DaVinci ou CapCut. O usuário pensa em conteúdo, não em frames. [^1]

## 3\. Auto-reframe

O sistema detecta o sujeito principal e adapta vídeos horizontais para formato vertical.

Provavelmente combina:

- detecção de faces;
- rastreamento de objetos;
- identificação do locutor ativo;
- análise de movimento;
- geração dinâmica da janela de corte.

A arquitetura exata não é pública; isso é uma inferência técnica baseada no comportamento do produto.

## 4\. Camada visual

O Vizard acrescenta:

- legendas;
- emojis;
- palavras destacadas;
- B-roll sugerido por IA;
- templates;
- fontes personalizadas;
- identidade da marca;
- outros;
- diferentes proporções.

O site também lista AI B-roll, sugestões de textos sociais e palavras-chave destacadas como recursos do produto. [^3]

## 5\. Distribuição

O produto fecha o ciclo conectando edição e publicação:

```
Conteúdo → edição → aprovação → calendário → rede social
```

Os planos pagos permitem agendar publicações, enquanto o plano Business adiciona workspace compartilhado, brand kit, membros e mais contas sociais. [^3]

Há suporte direto a redes como Instagram, YouTube, Facebook e X, respeitando as limitações das APIs de cada plataforma. Por exemplo, o Instagram conectado precisa ser Creator ou Business, enquanto a publicação no Facebook exige uma Página. [^4]

---

## Modelo comercial

A unidade de consumo é simples:

> **1 crédito = 1 minuto de vídeo enviado.**

O plano gratuito oferece 60 créditos mensais, exportação em 720p, uma conta social, armazenamento por três dias e vídeos com limitações como a marca d’água. Os planos pagos partem de 600 créditos mensais, removem a marca, liberam exportação em 4K e aumentam armazenamento, contas sociais e limites de API. [^3]

A engenharia comercial é inteligente:

```
Grátis
  ↓
Usuário vê o resultado
  ↓
Marca d’água e armazenamento curto incomodam
  ↓
Assina o Creator
  ↓
Conecta redes sociais
  ↓
Cria templates e histórico
  ↓
Custo de troca aumenta
  ↓
Equipe migra para Business
```

Não é só SaaS de edição. É um funil PLG com aprisionamento saudável por workflow, histórico, templates e integrações.

---

## A API é a parte mais relevante para a Ginkgo

A API REST permite enviar vídeos provenientes de:

- URL remota;
- YouTube;
- Google Drive;
- Vimeo;
- StreamYard.

Depois do envio, o sistema processa o projeto e o resultado pode ser recuperado por polling ou entregue por webhook. [^5]

O acesso à API está disponível nos planos pagos e consome os mesmos créditos de minutos usados na interface. [^5]

## Fluxo n8n imediato

```
Google Drive / YouTube / Upload
              ↓
        Webhook do Pyre
              ↓
       Registrar projeto
              ↓
    POST Create Project Vizard
              ↓
      Guardar projectId
              ↓
     Webhook ou polling 30s
              ↓
      Receber lista de clipes
              ↓
 Filtrar viralScore mínimo
              ↓
  Nyra analisa hook e contexto
              ↓
 Gerar copy por plataforma
              ↓
       Aprovação humana
              ↓
    Agendar ou publicar
              ↓
 Coletar métricas reais
              ↓
Comparar score previsto × performance
```

O próprio Vizard recomenda polling em intervalos de aproximadamente 30 segundos enquanto o processamento estiver em andamento. [^2]

---

## Como encaixar no Pyre

O erro seria transformar o Pyre em outro editor de vídeo genérico.

A melhor posição é:

> **Vizard processa o vídeo. Pyre governa a operação de conteúdo.**

## Divisão ideal

### Vizard

- transcrição;
- clipping;
- reenquadramento;
- renderização;
- legendas;
- exportação.

### Nyra

- escolha de pauta;
- pesquisa de tendências;
- análise da audiência;
- definição de hooks;
- geração de títulos;
- copy por país;
- CTA;
- interpretação dos resultados.

### Pyre

- calendário;
- aprovação;
- governança;
- contas e marcas;
- distribuição;
- testes A/B;
- analytics;
- atribuição;
- aprendizado;
- fila operacional.

O Vizard é um motor. O Pyre deve ser o cockpit.

---

## Produto comercial que podemos montar rapidamente

## Pyre Repurpose

Uma camada própria conectada ao Vizard, sem tentar reconstruir a tecnologia pesada inicialmente.

### Promessa

> Transforme cada podcast, reunião, treinamento ou vídeo em uma semana inteira de conteúdo.

### Entrada

- link do YouTube;
- arquivo;
- Google Drive;
- Zoom, Meet ou gravação;
- pasta monitorada;
- webhook.

### Saída

- 3 a 15 cortes;
- título;
- legenda;
- descrição;
- hashtags;
- CTA;
- capa;
- classificação por potencial;
- calendário;
- publicação;
- relatório de desempenho.

## Nichos iniciais

O melhor nicho não é “criadores em geral”. Isso joga o produto numa guerra de clones.

Começaria por:

1. **Mentores e consultores**  
	Transformar aulas, calls e lives em conteúdo de autoridade.
2. **Imobiliárias**  
	Cortes de visitas, análises de mercado, lives e apresentações.
3. **Podcasts regionais**  
	Operação completa de cortes, publicação e mensuração.
4. **Empresas B2B**  
	Webinars, treinamentos e reuniões convertidos em LinkedIn, Reels e Shorts.
5. **Agências**  
	Workspace multicliente, brand kits, aprovação e produção em lote.

---

## MVP enxuto

## Tela 1 — Fontes

```
Adicionar vídeo
[ YouTube ] [ Upload ] [ Drive ] [ Pasta automática ]
```

## Tela 2 — Configuração

```
Quantidade: 5 cortes
Duração: 30–60 segundos
Idioma: Português
Formato: 9:16
Marca: Ginkgo
Tom: Didático e direto
CTA: Conheça o Leaf
```

## Tela 3 — Processamento

```
Transcrevendo
Detectando momentos
Gerando cortes
Aplicando identidade
Criando copies
```

## Tela 4 — Resultados

Cada card teria:

- preview;
- viral score;
- hook;
- duração;
- plataformas recomendadas;
- editar;
- aprovar;
- descartar;
- agendar.

## Tela 5 — Calendário

```
Segunda — Instagram
Terça — TikTok
Quarta — Shorts
Quinta — LinkedIn
Sexta — Repost vencedor
```

---

## Arquitetura recomendada

```
Next.js Dashboard
       │
       ▼
Pyre API / Orchestrator
       │
 ┌─────┼───────────────┐
 ▼     ▼               ▼
n8n   PostgreSQL     Object Storage
 │
 ▼
Vizard API
 │
 ▼
Webhook Receiver
 │
 ▼
Nyra Content Agent
 │
 ├── títulos
 ├── copies
 ├── hashtags
 ├── CTA
 └── classificação
 │
 ▼
Approval Queue
 │
 ▼
Social Publishing Layer
 │
 ▼
Analytics + Learning Loop
```

## Dados principais

```
workspace
brand
source_video
processing_project
generated_clip
content_variant
approval
publication
social_account
performance_metric
learning_signal
```

---

## Construir do zero ou integrar?

## Agora: integrar

Motivos:

- API já disponível;
- webhooks;
- clipping pronto;
- infraestrutura de vídeo cara;
- renderização é operacionalmente pesada;
- reduz o tempo de MVP para semanas;
- permite validar clientes antes de montar uma usina nuclear no porão.

## Depois: substituir por módulos próprios

Ordem recomendada:

1. transcrição própria;
2. análise semântica;
3. pontuação de trechos;
4. FFmpeg para cortes;
5. geração de legendas;
6. auto-reframe;
7. templates;
8. B-roll;
9. editor visual.

O componente mais difícil não é cortar o vídeo. É produzir consistentemente um corte que retenha atenção e não pareça ter sido feito por um robô administrativo.

---

## Veredito

**Vizard faz bastante sentido como motor inicial do Pyre.**

Não criaria um “clone do Vizard” neste momento. Criaria um produto verticalizado que usa o Vizard por baixo e entrega algo que ele não resolve completamente:

> **estratégia + produção + governança + publicação + aprendizado operacional.**

A vantagem competitiva não será “geramos cortes”.

Será:

> **O sistema entende sua marca, transforma todas as suas gravações em conteúdo, agenda, publica, mede e aprende sozinho.**

O Vizard entrega clipes.  
O Pyre deve entregar uma máquina de crescimento.

---

**Você disse**

Tava pensando em montarmos um "visard.ai" exatamente igual para comercializar, antes de elaborar e melhorar o Pyre, uma versão enxuta como a deles de empacotar automações de cortes, tudo utilizando da Stack ai que temos, pesquise no meu Github Stack ai.

[![](https://chatgpt.com/images/ecosystem/apps/github/icon.png)](https://chatgpt.com/plugins/plugin_connector_1p_1a69035c238881919c4190932b2df699?plugin_detail_origin=inline_selection_pill)

[GitHub](https://chatgpt.com/plugins/plugin_connector_1p_1a69035c238881919c4190932b2df699?plugin_detail_origin=inline_selection_pill)

---

## Veredito

**Sim, faz sentido criar primeiro um “Vizard enxuto” como produto independente.**

Depois de auditar `ginkgoai/ai-stack`, `ginkgoai/ginkgo-pyre`, `ginkgoai/ginkgo-tree` e `ginkgoai/ginkgo-platform`, a conclusão é:

> Você já possui aproximadamente **55–65% da infraestrutura horizontal** necessária, mas praticamente **0% do motor especializado de processamento de vídeo**.

A fundação já tem banco, filas, créditos, publicação, automação e alguns padrões SaaS. O que falta é justamente o reator nuclear do produto:

- transcrição temporal;
- seleção inteligente dos cortes;
- enquadramento automático;
- legendas dinâmicas;
- renderização;
- editor de cortes;
- armazenamento de vídeos;
- processamento assíncrono de arquivos pesados.

A estratégia correta é criar um novo repositório, por exemplo:

```
ginkgoai/ginkgo-clips
```

Nome comercial provisório:

```
Ginkgo Clips
```

Não colocaria isso dentro do Pyre agora. O produto deve ser pequeno, vertical e comercializável sozinho. Depois, o Pyre consome o Ginkgo Clips como um motor interno.

---

## 1\. O que o Vizard vende hoje

O produto atual do Vizard une:

- upload e transcrição;
- identificação de highlights;
- cortes automáticos;
- auto-reframe para 9:16;
- legendas;
- palavras destacadas;
- emojis;
- B-roll;
- tradução;
- templates;
- editor;
- publicação e agendamento;
- workspace e brand kit;
- API.

O modelo comercial é baseado em minutos processados: atualmente, **um crédito corresponde a um minuto de vídeo processado**. Os planos superiores adicionam exportação em 4K, remoção de marca, armazenamento, contas sociais, workspace e brand kit. [^6]

O fluxo público central continua sendo:

```
Upload
  ↓
Transcrição
  ↓
IA encontra os melhores momentos
  ↓
Auto-reframe
  ↓
Legendas e design
  ↓
Exportação ou publicação
```

A própria Vizard descreve seu diferencial como encontrar momentos envolventes e centralizar automaticamente os sujeitos para TikTok, Reels e Shorts. [^7]

Podemos replicar a **categoria, funcionalidade e jornada**, mas não devemos copiar literalmente:

- nome;
- identidade;
- copy;
- componentes visuais;
- interface pixel por pixel;
- assets;
- lógica proprietária ou código.

O alvo é um concorrente funcional, não uma xerox com bigode falso.

---

## 2\. O que já existe no seu GitHub

## ginkgoai/ai-stack

Essa é a melhor fundação operacional.

Ela já contém:

- PostgreSQL;
- Redis;
- n8n;
- n8n Worker;
- BullMQ;
- Postiz;
- Temporal;
- AnythingLLM;
- infraestrutura Docker;
- isolamento de serviços por rede.

O n8n já opera em modo fila, com o processo principal enviando execuções para Redis e um worker separado consumindo os jobs.

O Postiz também já está configurado com PostgreSQL, Redis, upload local e Temporal.

### O que isso resolve

```
Orquestração
Webhooks
Filas de automação
Banco
Cache
Agendamento
Publicação em redes sociais
Logs operacionais
```

### O que isso não resolve

```
Upload SaaS de arquivos grandes
Object Storage escalável
FFmpeg
Transcrição de vídeo
Detecção de cenas
Detecção e rastreamento facial
Seleção de cortes
Renderização de legendas
Geração das versões finais
```

Portanto, o `ai-stack` é o **chassi**, não o motor de vídeo.

---

## ginkgoai/ginkgo-pyre

O Pyre já possui um backend Fastify com módulos de:

- chat;
- conteúdo;
- publicações;
- automações;
- créditos;
- webhooks.

Esses módulos já estão registrados numa API única.

Também há integração de publicação com Postiz e controle de créditos. A rota de publicação busca o conteúdo, debita créditos, registra a publicação e tenta enviar para o Postiz.

O serviço de publicação já implementa chamadas para criação de posts e leitura de integrações no Postiz.

### O que podemos reaproveitar

- contratos de publicação;
- conceito de biblioteca de conteúdo;
- controle de créditos;
- tabelas de publicações;
- integração com Postiz;
- estrutura modular Fastify;
- padrão de webhooks;
- parte da experiência mobile.

### O problema

O Pyre atual é um protótipo funcional, não uma base segura para um SaaS comercial.

O backend libera CORS para qualquer origem e não registra middleware de autenticação nas rotas.

Existem endpoints que retornam conteúdos, automações e saldo apenas recebendo um `user_id`, sem verificar se o solicitante é realmente aquele usuário.

Isso cria risco de IDOR: um usuário pode tentar trocar o identificador e acessar dados de outro.

Também encontrei no histórico do repositório um commit que continha uma credencial sensível do Supabase aparentemente real em um arquivo de exemplo. Não vou reproduzi-la. Mesmo que o arquivo tenha sido removido depois, a chave pode permanecer no histórico do Git.

### Ação de segurança obrigatória

Antes de reutilizar qualquer componente do Pyre:

1. rotacionar a chave do Supabase;
2. remover segredos do histórico;
3. adicionar autenticação;
4. aplicar RLS;
5. adicionar isolamento por workspace;
6. retirar `user_id` enviado pelo cliente como fonte de autoridade;
7. obter o usuário pelo token autenticado.

---

## ginkgoai/ginkgo-tree

Aqui está a arquitetura mais madura.

O projeto já possui:

- Kernel;
- máquina de estados;
- TaskRunner;
- Prisma;
- BullMQ;
- API Fastify;
- Worker;
- token ledger;
- policies;
- skill registry;
- evidence;
- eventos.

A estrutura já separa `core`, banco, API, worker e produtos.

O desenho foi feito para permitir que Leaf, Pyre e Wave registrem skills sem alterar o Kernel.

### Decisão

Não usaria o `ginkgo-tree` inteiro neste primeiro produto.

Ele é adequado para uma plataforma com múltiplos agentes, políticas, evidências e operações. Para um cortador de vídeo, seria como usar a ponte de comando da Enterprise para fazer café.

Porém, copiaria ou extrairia três ideias:

- estado determinístico dos jobs;
- fila API → worker;
- token ledger.

---

## ginkgoai/ginkgo-platform

Esse repositório apresenta a estrutura SaaS que mais interessa para a camada de produto:

- Next.js;
- Fastify;
- Supabase Auth;
- RLS;
- multi-tenancy;
- Stripe;
- Upstash Redis;
- pacotes compartilhados;
- biblioteca shadcn/ui.

A documentação declara Supabase Auth e RLS como base de isolamento multi-tenant.

Podemos reaproveitar conceitos e componentes visuais, mas não devemos transportar toda a lógica Leaf para o novo projeto.

---

## 3\. Arquitetura recomendada

```
┌────────────────────────────────────────────┐
│               NEXT.JS WEB                  │
│ Upload · Projetos · Clips · Editor · Conta │
└─────────────────────┬──────────────────────┘
                      │
                      ▼
┌────────────────────────────────────────────┐
│              FASTIFY API                   │
│ Auth · Workspaces · Billing · Signed URLs  │
│ Projetos · Clips · Templates · Webhooks    │
└──────────┬───────────────────┬─────────────┘
           │                   │
           ▼                   ▼
   PostgreSQL/Supabase    Storage S3/R2
           │                   │
           ▼                   ▼
     Redis + BullMQ       Vídeos originais
           │              Áudios e renders
           ▼
┌────────────────────────────────────────────┐
│          VIDEO WORKER — PYTHON             │
│                                            │
│ FFmpeg                                     │
│ faster-whisper / WhisperX                  │
│ PySceneDetect                              │
│ OpenCV / MediaPipe                         │
│ LLM Clip Analyzer                         │
│ Subtitle Renderer                         │
└─────────────────────┬──────────────────────┘
                      │
                      ▼
              Clips renderizados
                      │
          ┌───────────┴────────────┐
          ▼                        ▼
       Download                 Postiz
                            Publicação social
```

---

## 4\. Regra arquitetural importante

## n8n não deve processar o vídeo

O n8n pode:

- receber webhooks;
- disparar notificações;
- chamar APIs;
- registrar eventos;
- publicar no Postiz;
- enviar e-mails;
- fazer onboarding;
- processar eventos do Stripe.

Ele não deve:

- carregar binários de vários gigabytes;
- rodar FFmpeg;
- transcrever uma hora de vídeo;
- rastrear rosto frame a frame;
- renderizar dez clips simultaneamente.

Essa operação precisa morar em workers especializados.

```
n8n = gerente da fábrica
Worker de vídeo = maquinário industrial
```

Colocar FFmpeg dentro do n8n funcionaria em demonstração e começaria a pegar fogo quando entrassem três clientes juntos.

---

## 5\. Pipeline técnico do produto

## Etapa 1 — Ingestão

Entradas do MVP:

- upload MP4/MOV;
- URL pública;
- YouTube;
- Google Drive posteriormente.

Processo:

```
Cliente solicita upload
        ↓
API gera signed URL
        ↓
Cliente envia direto ao storage
        ↓
Storage confirma upload
        ↓
API cria projeto
        ↓
Job entra no BullMQ
```

O arquivo não atravessa o servidor Fastify. Ele vai diretamente do navegador para o object storage.

---

## Etapa 2 — Probing

O worker executa `ffprobe` e extrai:

- duração;
- resolução;
- bitrate;
- codec;
- FPS;
- canais de áudio;
- tamanho;
- orientação.

Também rejeita:

- arquivo corrompido;
- duração superior ao plano;
- codec não suportado;
- arquivo sem áudio;
- dimensões inválidas.

---

## Etapa 3 — Extração e transcrição

```
Vídeo
  ↓ FFmpeg
Áudio WAV mono 16 kHz
  ↓
faster-whisper / WhisperX
  ↓
Transcrição com timestamps
```

Formato armazenado:

```json
{
  "start": 121.4,
  "end": 124.9,
  "speaker": "SPEAKER_01",
  "text": "Essa é a parte que ninguém percebe."
}
```

O WhisperX pode ser introduzido quando precisarmos de alinhamento palavra por palavra e diarização mais precisa.

---

## Etapa 4 — Inteligência de cortes

Não mandaria o vídeo para o LLM. Mandaria a transcrição estruturada.

O sistema divide a transcrição em janelas narrativas e classifica:

- força do hook;
- clareza;
- autonomia do trecho;
- surpresa;
- tensão;
- utilidade;
- emoção;
- fechamento;
- potencial de retenção;
- risco de começar ou terminar no meio de uma frase.

Exemplo:

```json
{
  "start": 118.2,
  "end": 164.8,
  "score": 8.7,
  "hook": "A maioria das empresas está automatizando o processo errado.",
  "reason": "Contraste forte, argumento completo e fechamento claro.",
  "category": "insight",
  "platforms": ["reels", "shorts", "tiktok"]
}
```

A Vizard também utiliza modelos de clipping, diferentes proporções e processamento assíncrono com consulta posterior ou webhook. [^8]

---

## Etapa 5 — Refinamento temporal

O primeiro corte sugerido pelo LLM não deve ir direto para renderização.

O worker ajusta os limites:

```
timestamp sugerido pelo LLM
           ↓
busca pausa anterior
           ↓
busca final de sentença
           ↓
remove silêncio excessivo
           ↓
evita corte no meio da palavra
```

Essa etapa é decisiva. Um clip brilhante que termina no meio da frase continua sendo lixo brilhante.

---

## Etapa 6 — Auto-reframe

Para o MVP:

- detectar rosto;
- rastrear centro do rosto;
- suavizar movimento da janela;
- gerar crop 9:16;
- limitar velocidade de deslocamento.

Pipeline:

```
Frames reduzidos
    ↓
MediaPipe Face Detection
    ↓
Tracking do sujeito
    ↓
Suavização temporal
    ↓
Coordenadas de crop
    ↓
FFmpeg crop dinâmico
```

Cenários iniciais:

1. uma pessoa falando;
2. podcast com duas pessoas;
3. screen recording com webcam;
4. entrevista alternando locutor.

O caso com uma pessoa deve ser impecável antes de tentar construir um diretor de cinema autônomo para dez participantes.

---

## Etapa 7 — Legendas

O worker gera `.ASS`, porque esse formato permite:

- estilos;
- palavras destacadas;
- posição;
- animação;
- contorno;
- sombra;
- tamanhos;
- fontes;
- cores;
- emojis.

Templates iniciais:

```
Clean
Hormozi
Podcast
Minimal
Neon
Corporate
```

O vídeo final é renderizado com FFmpeg:

```
vídeo recortado
+ crop vertical
+ subtitles ASS
+ título
+ logo
+ outro
= MP4 final
```

---

## 6\. O MVP realmente vendável

Não tentaria copiar todas as funcionalidades atuais do Vizard de uma vez.

## Escopo da V1

### Entrada

- upload;
- URL de YouTube;
- vídeos de até 60 minutos;
- português, inglês e espanhol.

### Processamento

- transcrição;
- identificação de 3 a 10 cortes;
- viral score;
- justificativa do score;
- corte automático;
- auto-reframe;
- remoção de silêncios nas extremidades;
- legendas;
- palavras destacadas;
- template visual.

### Saída

- preview;
- download MP4;
- download SRT;
- copiar título;
- copiar legenda social;
- publicar pelo Postiz.

### Produto

- login;
- workspace;
- histórico de projetos;
- sistema de minutos;
- plano gratuito com marca d’água;
- assinatura Stripe;
- armazenamento temporário;
- painel de consumo.

---

## 7\. O que fica fora da V1

- editor completo estilo Premiere;
- timeline multicamada;
- colaboração em tempo real;
- B-roll gerado por IA;
- tradução de voz;
- clonagem de voz;
- 4K;
- remoção de fundo;
- múltiplos brand kits;
- aplicativo mobile;
- API pública;
- agência multi-workspace;
- publicação automática baseada em score;
- analytics avançado.

O editor inicial pode ter somente:

```
Ajustar início
Ajustar fim
Editar legenda
Trocar template
Trocar proporção
Trocar título
Renderizar novamente
```

Isso entrega a sensação de edição sem precisar construir o CapCut dentro da garagem.

---

## 8\. Estados do processamento

Eu aproveitaria o conceito de máquina de estados do `ginkgo-tree`.

```
CREATED
   ↓
UPLOADING
   ↓
UPLOADED
   ↓
QUEUED
   ↓
PROBING
   ↓
TRANSCRIBING
   ↓
ANALYZING
   ↓
GENERATING_CLIPS
   ↓
RENDERING
   ↓
READY
```

Estados alternativos:

```
FAILED
CANCELLED
EXPIRED
RETRYING
```

Cada etapa emite:

- progresso;
- timestamps;
- consumo;
- erro;
- tentativas;
- worker responsável;
- artefatos produzidos.

---

## 9\. Modelo de dados

```
users
workspaces
workspace_members
subscriptions
usage_ledger
projects
source_videos
transcripts
transcript_segments
clip_candidates
clips
clip_renders
brand_templates
social_integrations
publications
job_events
```

## Ledger de consumo

```
1 minuto enviado = 1 crédito
```

Registros:

```json
{
  "workspace_id": "wrk_123",
  "project_id": "prj_123",
  "operation": "video_processing",
  "units": 47,
  "status": "debited"
}
```

O crédito deve ser reservado antes do processamento e confirmado quando o vídeo passar pelo probing.

---

## 10\. Matriz de reaproveitamento

| Componente | Decisão |
| --- | --- |
| PostgreSQL do `ai-stack` | Reaproveitar |
| Redis do `ai-stack` | Reaproveitar |
| BullMQ | Reaproveitar |
| n8n | Reaproveitar para automações laterais |
| Postiz | Reaproveitar |
| Temporal do Postiz | Manter apenas para o Postiz |
| AnythingLLM | Não usar no motor |
| Evolution API | Não usar |
| Discord bots | Não usar |
| Pyre `publishService` | Adaptar |
| Pyre sistema de créditos | Reescrever com transações |
| Pyre rotas atuais | Não reutilizar sem autenticação |
| Ginkgo Tree TaskRunner | Extrair padrão |
| Ginkgo Tree token ledger | Extrair padrão |
| Ginkgo Platform UI/Auth | Reaproveitar componentes e padrões |
| FFmpeg worker | Construir |
| Transcription worker | Construir |
| Clip scoring | Construir |
| Object storage | Adicionar |

---

## 11\. Estrutura do novo repositório

```
ginkgo-clips/
├── apps/
│   ├── web/
│   │   ├── app/
│   │   ├── components/
│   │   └── lib/
│   │
│   ├── api/
│   │   └── src/
│   │       ├── auth/
│   │       ├── projects/
│   │       ├── uploads/
│   │       ├── clips/
│   │       ├── templates/
│   │       ├── billing/
│   │       └── webhooks/
│   │
│   └── video-worker/
│       ├── pipeline/
│       │   ├── probe.py
│       │   ├── audio.py
│       │   ├── transcribe.py
│       │   ├── analyze.py
│       │   ├── boundaries.py
│       │   ├── tracking.py
│       │   ├── subtitles.py
│       │   └── render.py
│       ├── templates/
│       └── worker.py
│
├── packages/
│   ├── db/
│   ├── contracts/
│   ├── queue/
│   ├── billing/
│   ├── storage/
│   └── ui/
│
├── infra/
│   ├── docker-compose.yml
│   └── ffmpeg/
│
└── docs/
    ├── ARCHITECTURE.md
    ├── PIPELINE.md
    └── SECURITY.md
```

---

## 12\. Épicos de construção

## Épico 0 — Segurança e fundação

- rotacionar credenciais expostas;
- Supabase Auth;
- RLS;
- workspaces;
- signed URLs;
- rate limiting;
- isolamento por tenant;
- ledger transacional.

## Épico 1 — Projetos e uploads

- dashboard;
- criação de projeto;
- upload direto;
- storage;
- `ffprobe`;
- progresso;
- validações.

## Épico 2 — Transcrição

- extração do áudio;
- faster-whisper;
- timestamps;
- SRT;
- tela de transcrição;
- idioma automático.

## Épico 3 — Clip Intelligence

- segmentação narrativa;
- análise pelo LLM;
- viral score;
- hook;
- justificativa;
- ajuste de limites;
- candidatos ordenados.

## Épico 4 — Auto-reframe

- face detection;
- tracking;
- suavização;
- crop 9:16;
- layouts de uma e duas pessoas.

## Épico 5 — Render Engine

- FFmpeg;
- ASS;
- legendas dinâmicas;
- palavras destacadas;
- logo;
- título;
- marca d’água;
- templates.

## Épico 6 — Clip Editor

- preview;
- ajuste de início e fim;
- texto;
- template;
- proporção;
- re-renderização.

## Épico 7 — Billing

- Stripe;
- planos;
- limites;
- reserva de créditos;
- débito;
- reembolso por falha;
- painel de consumo.

## Épico 8 — Distribuição

- Postiz;
- redes conectadas;
- publicação;
- agendamento;
- copy social;
- histórico.

---

## 13\. Posicionamento comercial

Não venderia como “editor de vídeos com IA”.

Venderia como:

> **Envie uma gravação. Receba uma semana de conteúdo pronto.**

Versão para creators:

> Transforme podcasts, aulas e vídeos longos em Shorts, Reels e TikToks automaticamente.

Versão para empresas:

> Transforme webinars, reuniões e treinamentos em conteúdo de autoridade.

Versão para agências:

> Produza cortes para todos os seus clientes sem multiplicar sua equipe de edição.

---

## Decisão final

O produto deve nascer assim:

```
Ginkgo Clips
Produto separado
Uma promessa
Uma entrada
Um processamento
Um resultado
```

Não deve nascer como módulo do Pyre, nem como uma nova camada do Ginkgo Tree.

A sequência estratégica fica:

```
1. Ginkgo Clips torna-se comercializável
2. Valida-se processamento, custos e demanda
3. O motor vira uma API interna
4. Pyre consome essa API
5. Pyre passa a gerar, cortar, publicar e aprender
```

Isso transforma o Ginkgo Clips no **motor de mídia** e o Pyre no **sistema operacional de conteúdo**.

O próximo passo correto é criar o repositório `ginkgo-clips` e iniciar pelo **Épico 0 — segurança, multi-tenancy e contrato do pipeline**, antes de qualquer tela bonita ou nó do n8n.

[^1]: [vizard.ai](https://vizard.ai/)

[^2]: [docs.vizard.ai](https://docs.vizard.ai/docs/retrieve-video-clips)

[^3]: [vizard.ai](https://vizard.ai/pricing)

[^4]: [help.vizard.ai](https://help.vizard.ai/en/articles/14631679-posting-limits-best-practices)

[^5]: [docs.vizard.ai](https://docs.vizard.ai/docs/quickstart)

[^6]: [vizard.ai](https://vizard.ai/pricing?utm_source=chatgpt.com)

[^7]: [vizard.ai](https://vizard.ai/?utm_source=chatgpt.com)

[^8]: [docs.vizard.ai](https://docs.vizard.ai/docs/quickstart?utm_source=chatgpt.com)