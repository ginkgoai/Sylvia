---
title: "GKO - Modelo agente Flowise n8n"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68ed44aa-beb4-832b-9139-0e79a9d25f1e"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
seg., 13 de out. às 15:28

seg., 13 de out. às 16:59

qual?

e aqui?

Vamos direto: **o híbrido Flowise (cérebro) + n8n (músculos)** é superior ao “tudo no n8n” para o BRANN. Ganha em clareza de papéis, evolução rápida, tool-use robusto e portabilidade de modelos. Use n8n puro só para fluxos 100% determinísticos (broadcast, rotinas, ETL).

## Veredito técnico (curto e sincero)

- **Híbrido é melhor** quando há: multimodal, RAG, chamadas de ferramentas, personalidades, memória e escalabilidade.
- **Trade-offs:** +1 salto de rede (latência ~300–600 ms), mas compensa em manutenção, testes A/B e troca de LLM sem reescrever orquestração.
- **Custo:** gpt-4o-mini + cache + RAG enxuto costuma sair mais barato que “promptzão monolítico no n8n” retrabalhando contexto a cada turno.

---

## Arquitetura BRANN v1.0 (referência)

**Ingress**  
Evolution API → `n8n /inbox` (normaliza texto, mídia, metadados).

**Consciência (Flowise)**

- LLM: `gpt-4o-mini` (primário); fallback: Gemini 1.5 Flash; contingência local: Llama-3.1-8B-Instruct via Ollama.
- Planner ReAct + **Ferramentas HTTP** (nomes estáveis) → n8n.
- **Memória curta**: Redis (TTL 72h, janela 15–20 trocas).
- **RAG**: Supabase PGVector (coleções: `brand`, `faq`, `contratos`, `cliente/{id}`) com *rerank* leve no próprio LLM.
- **Políticas/guardrails:** anti-injeção, PII mask, orçamento por turno, whitelists de tools.

**Orquestração (n8n)**

- **Router** (`/router`): recebe mensagem, chama Flowise e interpreta `TOOL_CALL`.
- **Dispatcher**: envia para micro-fluxos (ferramentas); retries, circuit-breaker, fila Redis.
- **Observabilidade**: Postgres logs + Healthchecks.io; alertas Telegram/Discord.

**Armazenamento**

- Redis (sessões/fila), Postgres (telemetria/eventos), Supabase (vetores + arquivos).

**Áudio/Visão**

- **STT**: Faster-Whisper (n8n microserviço).
- **TTS**: **Kokoro** (n8n: `send_audio`).
- **OCR/Docs**: Unstructured/PDF → ingestão via n8n antes de ir ao vetor.
- **Visão**: 4o-mini (imagem) direto no Flowise quando chegar mídia.

---

## Arsenal de ferramentas (via n8n, com contratos fixos)

Use esses nomes no Flowise (1:1 com webhooks do n8n):

1. **kb\_search** `{ "query": "texto", "top_k": 5 }` → Supabase Vetores → retorna `passages[]`.
2. **db\_query** `{ "op": "get|set", "entity": "lead|plano|contrato", "where": {...}, "data": {...} }` → Supabase DB.
3. **serp\_search** `{ "query": "texto", "num": 5 }` → SERPAPI (fallback quando kb falhar).
4. **send\_message** `{ "to": "+55...", "type": "text|image|document", "text": "...", "media_url": "..." }` → Evolution.
5. **send\_audio** `{ "to": "+55...", "text": "conteúdo TTS" }` → Kokoro.
6. **schedule\_meeting** `{ "name": "Onboarding", "when": "YYYY-MM-DD HH:mm -03", "duration_min": 30 }` → Calendar.
7. **create\_contract\_pdf** `{ "cliente": {...}, "plano": "Básico|Futurista", "vars": {...} }` → PDF + link.
8. **drive\_save** `{ "path": "cliente/{id}/...", "url": "..." }` → Supabase Storage/Drive.
9. **ticket\_escalate** `{ "reason": "...", "priority": "P2|P1" }` → Pipefy/Notion/Discord.

---

## Modo de operação (ciclo de 1 turno)

1. Evolution → `n8n/inbox` (normaliza/identifica canal).
2. `router` → Flowise com `{message, sessionId, context}`.
3. Flowise: ReAct → se precisar, **TOOL\_CALL** (apenas JSON).
4. n8n executa tool(s) com retries/circuit-breaker → retorna resultado.
5. Flowise compõe resposta final (ou decide mandar áudio via `send_audio`).
6. n8n envia pelo Evolution + registra telemetria.

**Metas de performance**

- FRT (primeiro token): ≤ 1.8 s (texto simples).
- Turno com tool: ≤ 6–8 s (inclui TTS).
- Tool success rate: ≥ 98%.
- Custo/conversa (margem): monitorar; cachear respostas frequentes + *context packing* mínimo.

---

## Quando usar n8n-puro

- Campanhas, disparos massivos, funis lineares, cálculo determinístico, ETLs, webhooks internos.
- Você ainda pode chamar LLM “de apoio”, mas sem planner/agent (respostas enlatadas ou *prompted functions*).

---

## Segurança e confiabilidade

- **Whitelists de tool** no prompt + validação de schema no n8n.
- **Idempotência**: `request_id` por tool para evitar duplicatas.
- **Rate-limit** por `sessionId` e por destino (WhatsApp/Meta).
- **Backoff exponencial** e **quarentena** de integrações instáveis.
- **Segredos** só no n8n (Flowise recebe *tokens* temporários quando estritamente necessário).

---

## Stack sugerida (pragmática)

- **LLM primário:** gpt-4o-mini; **fallback:** Gemini 1.5 Flash; **contingência local:** Llama-3.1-8B (Ollama).
- **Vetores:** Supabase PGVector (1536–3072 dims).
- **STT/TTS:** Faster-Whisper + Kokoro.
- **Scraping:** Firecrawl (quando SERPAPI entregar URL) → sanitiza → vetor.
- **MCP servers:** padronizar acesso a DB, Storage, Calendar, Finance, Mail (facilita trocar n8n se precisar).

---

## KPIs para governar o bicho

- **CSAT / “resolveu?”**, **tempo médio por turno**, **tool success rate**, **handoff rate**, **custo por conversa**, **Nº de jailbreaks bloqueados**, **receita/lead**.

---

## Passo imediato

- Subir 3 tools no n8n: `kb_search`, `send_message`, `send_audio`.
- Colar o prompt do BRANN no Flowise com planner + memória + RAG.
- Testar intents: “meu plano”, “contrato”, “marcar horário”, “manda áudio explicando”.

Com isso você tem um **atendente generativo de vendas** escalável, observável e replicável, com cérebro trocável e músculos bem treinados.

Quero que você elabore um passo a passo completo para essa ideia, esse projeto sair do 0 ao funcionamento total como atendente da ginkgo no whatsapp. Use de pesquisa profunda para examinar a concorrência e ver os métodos utilizados, mantenha o princípio, um agente de vendas inteligente, emocional, que sabe atender e vender com memória curta e longa e acesso a banco de dados, utilizando apenas n8n, flowise, kokoro, evolution api, evolution aí, tools e ferramentas dos próprios aplicativos e/ou integrações com mcps servers, use conhecimento de um engenheiro para projetar o passo a passo exato sem erros, utilize-me como um contrutor sem conhecimento que vai seguir suas ordens mais simples possível, copia/cola ou de fácil entendimento.

Para montar um passo a passo completo e confiável para o BRANN, preciso só de dois detalhes antes:

1. Você já tem conta configurada nos seguintes serviços?
	- Evolution API (envio e recebimento de mensagens)
		- Supabase (para banco de dados e vetores)
		- Kokoro (voz/texto para áudio)
		- SERP API (para pesquisa web)
		- Flowise e n8n já instalados no Easypanel (como vimos)
2. O agente vai funcionar só em **WhatsApp** mesmo, ou também terá versões futuras para Instagram, site, Telegram etc?

Com isso, eu já começo o guia completo pra tirar o BRANN do papel até a primeira venda real.

Perfeito. Vou montar um passo a passo completo e confiável para colocar o BRANN em produção como atendente de vendas da Ginkgo no WhatsApp, com escalabilidade futura para Instagram e site. A arquitetura será baseada em Flowise (consciência), n8n (orquestrador), Evolution API (canal), Kokoro (áudio), Supabase (banco e vetores) e SERP API (pesquisa externa).

Vou organizar esse guia com instruções simples e diretas, como se você fosse seguir copiando e colando, sem precisar entender detalhes técnicos. Também vou mapear práticas atuais da concorrência em IA conversacional para garantir que BRANN seja competitivo.

Te aviso assim que estiver tudo pronto.

## Guia Passo a Passo – Atendente Virtual Inteligente para Vendas no WhatsApp (Ginkgo)

## Visão Geral do Projeto

Este projeto irá criar um **agente de vendas inteligente e emocional** atuando via WhatsApp (posteriormente integrável ao Instagram e site). Utilizaremos ferramentas **low-code** e open-source como **n8n** (automação de fluxo), **Flowise AI** (construção de chatbots com LLM), **Evolution API** (API de integração com WhatsApp) e **Kokoro** (geração de voz por IA) para desenvolver o atendente virtual. O bot terá **memória de curto e longo prazo**, acesso a banco de dados para informações de cliente/produto, e será capaz de conduzir conversas de atendimento e vendas de forma **personalizada e empática**. A seguir detalhamos cada etapa, da instalação à configuração e expansão futura, em instruções claras que você pode seguir mesmo sem experiência prévia.

## Passo 1: Configuração do Ambiente de Desenvolvimento

Para começar, precisamos instalar e configurar as principais ferramentas envolvidas.

**1.1 – Instalar e Configurar a Evolution API (WhatsApp):**

- **Instalação:** A Evolution API é uma solução open-source que permite conectar-se ao WhatsApp via API [doc.evolution-api.com](https://doc.evolution-api.com/v1/en/get-started/introduction#:~:text=Evolution%20API%20is%20a%20project,a%20part%20of%20the%20project). A forma mais fácil de rodá-la é via **Docker**. Execute o comando abaixo no terminal do seu servidor (com Docker instalado) para iniciar a API em segundo plano:
	```markdown
	docker run -d \
	    --name evolution_api \
	    -p 8080:8080 \
	    -e AUTHENTICATION_API_KEY=SUA_CHAVE_API \
	    atendai/evolution-api:latest
	```
	*(Substitua `SUA_CHAVE_API` por uma chave secreta de sua escolha. Esse será o token de autenticação para acessar a API) [doc.evolution-api.com](https://doc.evolution-api.com/v1/en/get-started/introduction#:~:text=Terminal).*
- **Conectar ao WhatsApp:** Com o contêiner rodando, acesse a interface de gerenciamento da Evolution API. Abra um navegador e vá para `http://SEU_SERVIDOR:8080/manager` (ou `http://localhost:8080/manager` se estiver local). Use a chave API definida acima para autenticar. No painel, **crie uma nova instância** do WhatsApp. Isso gerará um **QR Code** que você deve escanear com o WhatsApp (no app vá em *Aparelhos Conectados* > *Conectar um aparelho*) para parear a API com sua conta do WhatsApp [hacodered.co.uk](https://www.hacodered.co.uk/n8n-and-evolution-api/#:~:text=Adding%20Webhook%20to%20Instance) [hacodered.co.uk](https://www.hacodered.co.uk/n8n-and-evolution-api/#:~:text=The%20following%20is%20the%20configuration,is%20a%20new%20WhatsApp%20message). Após escanear, a instância ficará “online” e pronta para enviar/receber mensagens. Anote o **ID da instância** (ou nome) e a **API Key individual** gerada para essa instância (cada conexão WhatsApp terá sua própria chave API [community.n8n.io](https://community.n8n.io/t/evolution-api-and-n8n-how-to-configure/96559#:~:text=Solution%3A)).
- **Webhooks de Mensagens:** Configure os **eventos (webhooks)** para receber mensagens. No Evolution Manager, selecione a instância e adicione um webhook para o evento de mensagem recebida (geralmente chamado `messages.upsert`). Informe a URL do webhook que o **n8n** vai escutar (configuraremos o n8n no próximo passo) e marque pelo menos o evento de nova mensagem [hacodered.co.uk](https://www.hacodered.co.uk/n8n-and-evolution-api/#:~:text=To%20receive%20message%20upsert%20events,via%20a%20HTTP%20Post%20request). Assim, sempre que seu WhatsApp receber uma mensagem, a Evolution API enviará um POST para o endereço configurado com os dados da mensagem em tempo real. *Dica:* Durante testes, você pode usar um serviço como `webhook.site` para verificar se os eventos estão sendo enviados corretamente [community.n8n.io](https://community.n8n.io/t/evolution-api-n8n-coolify-webhook-works-with-test-url-but-fails-to-receive-data-with-production-url/145846#:~:text=Evolution%20API%20can%20successfully%20deliver,data%20to%20my%20production%20url).

**1.2 – Instalar e Configurar o n8n (Automação de Fluxos):**

- **Instalação:** O n8n pode ser executado localmente ou em um servidor (recomendado para produção). Também há imagem Docker. Por exemplo, você pode usar:
	```markdown
	docker run -d -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n
	```
	Esse comando inicia o n8n na porta 5678 e persiste a configuração no diretório `~/.n8n`. Após subir, acesse a interface web do n8n em `http://SEU_SERVIDOR:5678` (se local, `http://localhost:5678`). Crie sua conta de usuário se solicitado.
- **Community Nodes:** Habilite o uso de nós da comunidade no n8n (vá em *Settings > Community Nodes* e habilite). Em seguida, instale o pacote **Evolution API** community node. No menu de instalação de nodes, informe o nome do pacote `n8n-nodes-evolution-api` e instale [hacodered.co.uk](https://www.hacodered.co.uk/n8n-and-evolution-api/#:~:text=Community%20Node). *Observação:* O n8n permite integrar a Evolution API tanto via este node específico (que simplifica autenticação e chamadas) quanto via nós HTTP genéricos. Usaremos o node dedicado para facilidade.
- **Credenciais Evolution API:** Após instalar o node, adicione uma nova credencial do tipo "Evolution API". Preencha a URL do servidor (por exemplo, `http://SEU_SERVIDOR:8080` sem a barra final) e a chave API da instância do WhatsApp configurada no passo anterior [community.n8n.io](https://community.n8n.io/t/evolution-api-and-n8n-how-to-configure/96559#:~:text=Solution%3A). *Importante:* Use a chave individual da instância (não a chave global `AUTHENTICATION_API_KEY`, mas sim aquela gerada quando você conectou o WhatsApp) [community.n8n.io](https://community.n8n.io/t/evolution-api-and-n8n-how-to-configure/96559#:~:text=the%20n8n,gets%20an%20individual%20API%20Key). Teste a conexão para garantir que está tudo correto (o node community deve conseguir acessar a API). Se houver problemas, verifique se a URL está correta (incluindo protocolo http/https) e sem porta se necessário (alguns usuários relataram remover `:8080` da URL nas credenciais caso dê erro) [community.n8n.io](https://community.n8n.io/t/evolution-api-and-n8n-how-to-configure/96559#:~:text=Just%20by%20luck%2C%20i%20found,other%20key%20and%20tried%20it).

**1.3 – Instalar o Flowise AI (Plataforma de Chatbot com LLM):**

- **Instalação:** O Flowise pode ser auto-hospedado facilmente. Você pode instalá-lo via npm ou Docker. Por simplicidade, use Docker:
	```markdown
	docker run -d -p 3000:3000 flowiseai/flowise:latest
	```
	Isso inicia o Flowise na porta 3000. Acesse `http://SEU_SERVIDOR:3000` para abrir a interface web. (Você também pode instalar via `npx flowise` se tiver Node.js, conforme a documentação do Flowise).
- **Configuração Inicial:** Na primeira execução, o Flowise não terá chatflows definidos. Também será necessário configurar os provedores de modelo. Para um agente de vendas inteligente, recomendamos inicialmente integrar o Flowise com a API da OpenAI (usando GPT-4 ou GPT-3.5) para obter respostas de alta qualidade em português. No Flowise, vá em *Settings* ou *Nodes* e adicione uma credencial do OpenAI (chave da API). *Alternativa:* Se preferir modelos open-source, o Flowise suporta modelos locais via HuggingFace, GPT4All, etc., mas isso pode exigir mais recursos de hardware. Comece com OpenAI se possível, pela facilidade.
- **Chave da API do Flowise:** Habilite a API do Flowise para permitir chamadas externas. Em *Flowise Settings*, gere uma API Key (ou anote a padrão se houver). Precisaremos do endpoint HTTP do Flowise e dessa API key para integrar via Evolution API ou n8n. O endpoint base normalmente será `http://SEU_SERVIDOR:3000/api/v1/prediction/{chatflow-id}` para chamadas de previsão, conforme veremos.

**1.4 – (Opcional) Instalar o Kokoro (Texto para Fala Emocional):**  
Se deseja que o atendente envie **áudios humanizados** (voz) pelo WhatsApp, integre o Kokoro. O **Kokoro** é um gerador de voz por IA que produz falas naturais e de alta qualidade [easypanel.io](https://easypanel.io/docs/templates/kokoro#:~:text=Kokoro%20is%20a%20powerful%2C%20browser,applications%20with%20OpenAI%20API%20compatibility). Você pode **auto-hospedar** o Kokoro para ter controle total e compatibilidade com a API do OpenAI TTS [easypanel.io](https://easypanel.io/docs/templates/kokoro#:~:text=,projects%2C%20virtual%20assistants%2C%20and%20more). Algumas opções:

- Utilize o template Docker pronto (imagem `ghcr.io/eduardolat/kokoro-web:0.1.3` conforme a doc Kokoro). Por exemplo:
	```markdown
	docker run -d -p 5000:5000 ghcr.io/eduardolat/kokoro-web:0.1.3
	```
	(Este comando hipotético expõe uma API web do Kokoro na porta 5000). Verifique a documentação oficial para a versão atual e endpoints.
- Uma vez rodando, teste um endpoint do Kokoro para gerar áudio. Por exemplo, pode haver um endpoint `/synthesize` onde você envia um texto e obtém um arquivo de áudio (WAV/MP3) ou um link. Confirme o formato de chamada e resposta. Kokoro promete integração compatível com API do OpenAI, então possivelmente a chamada é semelhante ao Whisper ou um endpoint de conversão de texto em fala.
- **Obs:** Este passo é opcional. Inicialmente, você pode fazer o bot responder apenas em texto (mais simples). A adição de voz é um diferencial para tornar o atendimento mais **humano e emocional**, muito usado no Brasil já que muitos clientes enviam e preferem áudio no WhatsApp. Recomendamos implementar o Kokoro após o básico estar funcionando, visto que adiciona complexidade (conversão de texto para áudio e envio de mídia pelo WhatsApp).

**1.5 – Configurar Banco de Dados para Memória Longa (Opcional):**  
Para memória de longo prazo ou armazenamento de informações (perfil do cliente, histórico de compras, etc.), é útil ter um banco de dados. Você pode usar:

- Uma solução simples como **SQLite** (o próprio n8n usa SQLite internamente e pode guardar dados via nós do tipo Database),
- Ou um banco externo como **PostgreSQL/MySQL**. Alternativamente, serviços na nuvem como Supabase (Postgres) funcionam bem se preferir.

No contexto do nosso bot, o DB pode armazenar, por exemplo: dados de clientes (nome, contato, preferências), histórico resumido de conversas, ou catálogo de produtos para consultas. Configure um DB e crie tabelas conforme necessário (por exemplo, uma tabela `clientes` e uma `historico_conversas`). Mais à frente integraremos isso via n8n. Se não tiver familiaridade, você pode inicialmente usar um **Google Sheets** via n8n (como banco rudimentar) ou até mesmo JSON files. Porém, um DB SQL dará mais robustez. *Este passo não é obrigatório para o funcionamento básico*, mas será utilizado para recursos avançados de memória longa e integração com sistemas de vendas/CRM.

## Passo 2: Construção do Fluxo de Conversa (Chatbot Flowise)

Agora vamos criar a lógica do chatbot dentro do Flowise, definindo como o agente conversa, sua personalidade de vendas, memória e uso de dados.

**2.1 – Criar um Novo Chatflow no Flowise:**

- Na interface web do Flowise, acesse a seção *Chatflows* e clique em **Add New** para criar um novo fluxo de chat [toolify.ai](https://www.toolify.ai/ai-news/flowise-ai-build-whatsapp-chatbots-with-nocode-3505734#:~:text=1). Dê um nome como "Atendente Ginkgo". Você verá uma interface visual de fluxo, onde podemos adicionar nós (nodes) representando componentes da conversa (modelo de IA, memórias, prompts, ferramentas etc.).
- **Idioma e Persona:** Defina que o bot interaja em Português do Brasil, com tom amigável e vendedor. Para isso, adicione um nó de tipo **System Prompt** (pode ser um node *Text input* configurado como system message, ou dependendo da versão, um componente específico para prompt inicial). Escreva instruções no prompt do sistema descrevendo o comportamento desejado, por exemplo (em português): *"Você é um assistente virtual de vendas chamado Ginkgo. Sua missão é atender o cliente de forma calorosa, emocional e profissional, entendendo as necessidades dele e oferecendo os produtos/soluções da empresa de maneira consultiva. Mantenha um tom amigável, use linguagem simples, chame o cliente pelo nome (quando conhecido) e use empatia. Responda sempre em Português. Seja conciso, mas personalize as recomendações de produto conforme as preferências do cliente."* Esse prompt garantirá que o modelo responda alinhado a esse perfil em todas as interações.

**2.2 – Adicionar o Modelo de Linguagem (LLM):**

- Arraste para o fluxo um nó do tipo **ChatOpenAI** (se estiver usando OpenAI GPT) ou outro modelo que preferir [toolify.ai](https://www.toolify.ai/ai-news/flowise-ai-build-whatsapp-chatbots-with-nocode-3505734#:~:text=,of%20a%20new%20conversational%20flow). Conecte a saída do seu nó de Prompt do sistema à entrada do modelo (de modo que o prompt do sistema seja fornecido antes das mensagens do usuário). Configure o nó do modelo com a credencial da API (por exemplo, OpenAI API Key) e escolha o modelo (GPT-4 ou GPT-3.5-turbo). Ajuste parâmetros como *temperature* (um valor ~0.7 pode dar respostas criativas sem perder muita coerência) e *max tokens* conforme desejado.
- **Modelo Open-Source (Alternativa):** Se não usar OpenAI, escolha um nó de modelo local suportado. Por exemplo, Flowise suporta modelos via HuggingFace. Você poderia usar um modelo como Llama2 7B ou 13B em português, porém a qualidade pode ser inferior e a configuração mais complexa. Para início, usar a API da OpenAI tende a acelerar o desenvolvimento e garantir qualidade nas respostas em linguagem natural.

**2.3 – Implementar Memória de Curto Prazo (Contexto da Conversa):**

- Para que o bot lembre do que o usuário acabou de dizer e do que ele mesmo respondeu (contexto dentro da sessão atual), adicione um nó de **Memória** do tipo *Buffer* ou *Buffer Window*. Por exemplo, o **Buffer Memory** simples armazena todo o histórico, enquanto o **Buffer Window Memory** pode armazenar apenas os últimos N interações para não sobrecarregar contexto [docs.flowiseai.com](https://docs.flowiseai.com/integrations/langchain/memory#:~:text=). Conecte esse nó apropriadamente no fluxo: tipicamente, o nó de memória se conecta ao nó do modelo de forma que ele insira a variável `{history}` no prompt para o LLM. O Flowise/LangChain fará automaticamente o gerenciamento do histórico: cada nova mensagem do usuário e resposta do AI serão armazenadas.
- **Parâmetro Session ID:** Configure o nó de memória (na lateral, ao clicar nele) para usar um **Session ID** dinâmico. Isso é crucial para separar conversas de usuários diferentes e ter memória independente por contato. No campo *SessionId* do nó, coloque algo como `{{sessionId}}` (o Flowise permite placeholders) ou deixe para fornecer via API. Quando chamarmos o Flowise via requisição HTTP no n8n, passaremos o identificador único do usuário (no caso, o número de telefone do WhatsApp) como sessionId. O Flowise suporta essa abordagem: ao usar a API de previsão, podemos enviar um JSON incluindo `"overrideConfig": { "sessionId": "5511999999999" }` por exemplo [docs.flowiseai.com](https://docs.flowiseai.com/integrations/langchain/memory#:~:text=1.%20In%20the%20%60%2Fapi%2Fv1%2Fprediction%2F%7Byour,overrideConfig). Dessa forma, todas as mensagens daquele número serão agrupadas em uma sessão e o histórico carregado automaticamente para o modelo lembrar.
- **Memória Curta vs Longa:** A memória via contexto tem limite (especialmente se usar GPT-3.5/4, há limite de tokens). Por isso, definiremos a memória “curta” como as últimas interações relevantes (por ex., últimas 10 mensagens) [n8n.io](https://n8n.io/workflows/3586-ai-powered-whatsapp-chatbot-for-text-voice-images-and-pdfs-with-memory/#:~:text=). Isso garante fluidez no diálogo recente [n8n.io](https://n8n.io/workflows/3586-ai-powered-whatsapp-chatbot-for-text-voice-images-and-pdfs-with-memory/#:~:text=). Já a “memória longa” trataremos a seguir com resumos ou armazenamento persistente.

**2.4 – Implementar Memória de Longo Prazo (Persistência de Informações):**

- Para que o atendente recorde informações importantes em interações futuras (fora da sessão atual ou após longos diálogos), podemos usar **memória de resumo** e banco de dados. Adicione um nó **Conversation Summary Memory** no Flowise [docs.flowiseai.com](https://docs.flowiseai.com/integrations/langchain/memory#:~:text=). Este componente gera periodicamente um resumo condensado da conversa e armazena, evitando perder detalhes importantes de interações longas. Conecte-o no fluxo de forma que após cada resposta do AI ele atualize o resumo. O resumo pode ser incluído no prompt do sistema ou contexto inicial para conversas futuras (“context carry-over”).
- **Armazenamento em Banco:** Considere integrar uma etapa onde, após cada conversa (ou quando a conversa é marcada como encerrada), o resumo gerado seja gravado em um banco de dados externo. O Flowise por si só não possui node de escrita em banco diretamente, então aqui entra o n8n: podemos enviar o resumo via n8n para o DB. Outra abordagem é usar memórias específicas integradas a DBs – Flowise/LangChain têm opções para usar **Redis, DynamoDB, MongoDB ou Zep** como store de memória [docs.flowiseai.com](https://docs.flowiseai.com/integrations/langchain/memory#:~:text=). Por exemplo, o node *Redis-Backed Chat Memory* poderia ser usado se você configurar um Redis, tornando a memória de conversa persistente entre reinícios. Se preferir usar um SQL, pode omitir a parte de memória persistente no Flowise e simplesmente usar o n8n para consultar dados do cliente (ver próximo passo).
- **Perfil do Cliente:** Uma prática usada em chatbots de venda profissionais é guardar perfil do usuário. Por exemplo, quando o cliente diz o nome ou preferências ("Eu gosto do produto X"), o bot pode salvar isso. Podemos configurar no Flowise um **agente ou ferramenta customizada** que detecta certas informações e faz chamada a uma API para salvar dados. Porém, para simplicidade, faremos via n8n: toda vez que chegar uma mensagem, podemos verificar se já temos aquele usuário no DB; se não, criar um registro. Da mesma forma, após uma interação relevante (cliente mencionou um interesse em um produto), podemos atualizar um campo "interesse" no registro. Essa lógica será implementada no fluxo n8n (explicado no Passo 3), já que o n8n intermedia as mensagens.

**2.5 – Integração com Base de Conhecimento e Ferramentas:**

- Além de conversar de forma genérica, o bot pode responder dúvidas específicas sobre produtos, estoque, preços etc. Para isso, conecte fontes de dados: por exemplo, se há um catálogo de produtos ou FAQs da Ginkgo, podemos criar um **RAG (Retrieval-Augmented Generation)**. Uma maneira é carregar documentos ou planilhas com informações no Flowise (ex.: usar um node de **Documentos + Vector Store** para permitir busca semântica). Você poderia ingerir um PDF/CSV com descrição de produtos e usar um **Vector DB (como Chroma)** dentro do Flowise, permitindo ao bot buscar dados relevantes quando perguntado [toolify.ai](https://www.toolify.ai/ai-news/flowise-ai-build-whatsapp-chatbots-with-nocode-3505734#:~:text=Setting%20up%20a%20RAG%20%28Retrieval,Chatbot). Outra forma é usar um **SQL Agent** do Flowise/LangChain [toolify.ai](https://www.toolify.ai/ai-news/flowise-ai-build-whatsapp-chatbots-with-nocode-3505734#:~:text=This%20section%20outlines%20the%20step,56%20and%20information%20dissemination) para consultar diretamente um banco de dados de produtos: existe um node *SQL Database* ou *SQL Agent* onde você configura a conexão e ele permite ao LLM executar queries. Por exemplo, se o usuário perguntar "Tem camisa tamanho M em estoque?", o agente de SQL poderia rodar uma query na tabela de estoque e retornar a resposta exata.
- *Nota:* Ferramentas de consulta aumentam a capacidade do bot vender de forma assertiva (concorrentes frequentemente integram os bots ao estoque e CRM para respostas exatas). Configure essas integrações conforme sua necessidade e disponibilidade de dados. No início, se não tiver esse backend pronto, você pode inserir manualmente no prompt algumas informações estáticas de produto para teste. Porém, planeje a integração com dados reais para o bot ser realmente útil (ex.: consultar preços atualizados, verificar promoções). O n8n também pode auxiliar nisso, chamando APIs externas ou DB e alimentando a resposta – avaliaremos isso no fluxo do n8n.

**2.6 – Testar o Chatflow localmente:**  
Antes de integrar ao WhatsApp, teste dentro do próprio Flowise: utilize a interface de chat do Flowise (há um botão de *chat* ou *play* no editor do fluxo). Escreva mensagens simulando o cliente e veja as respostas do bot. Verifique se ele:

- Mantém contexto dentro de algumas trocas (memória curta funcionando),
- Responde em tom amigável e personalizado (de acordo com o prompt do sistema),
- Consegue acessar informações do conhecimento (se integrou base de dados ou colocou fatos no prompt),
- Não fica muito prolixo (ajuste *max\_tokens* ou instruções se necessário para respostas mais objetivas de vendas).

Ajuste os nós conforme necessário: por exemplo, se as respostas estiverem muito genéricas, refine o prompt de sistema adicionando instruções ou exemplos de atendimento. Você pode fornecer **exemplos de diálogo** no prompt (few-shot) para treinar o comportamento: ex.: *"Exemplo: Cliente: 'Estou interessado em uma calça jeans.' Assistente: 'Que ótimo! Temos diversos modelos de calça jeans. Você busca algo para uso casual ou algo mais formal?...'"*. Essas demonstrações ajudam o modelo a seguir o estilo desejado.

## Passo 3: Integração do Chatbot com WhatsApp via n8n + Evolution API

Com o chatbot configurado, vamos conectá-lo ao canal WhatsApp usando o n8n para orquestrar a entrada e saída de mensagens entre a Evolution API (WhatsApp) e o Flowise (IA).

**3.1 – Fluxo de Recebimento de Mensagens (Webhook no n8n):**

- No n8n, crie um **novo workflow** chamado "WhatsApp Bot Ginkgo". Adicione um nó **Webhook** como gatilho (Trigger). Configure-o no modo *POST* e copie a URL gerada (será algo como `https://seu-n8n-host/webhook/uuid...`). Se o n8n estiver local, você precisará expor esse webhook publicamente (usando um túnel ou hospedando o n8n em um servidor com domínio). Cole essa URL no Evolution API Manager, na configuração de webhook de mensagens (feito no Passo 1.1). Certifique-se de incluir eventos de `messages.upsert` para novas mensagens [hacodered.co.uk](https://www.hacodered.co.uk/n8n-and-evolution-api/#:~:text=To%20receive%20message%20upsert%20events,via%20a%20HTTP%20Post%20request). Salve a configuração no Evolution.
- **Teste Inicial:** Envie uma mensagem qualquer do seu WhatsApp para o número conectado. O Evolution API deve encaminhar um POST ao webhook do n8n. No n8n, deixe o workflow ativado e abra a execução (modo teste) para ver se o webhook disparou. Você deverá ver os dados brutos da mensagem na saída do nó Webhook: um JSON contendo informações como o ID da instância, o número de telefone do remetente (`remoteJid`), nome do contato (`pushName`), tipo e conteúdo da mensagem, etc. Garanta que isso está funcionando antes de prosseguir. *Dica:* A Evolution API envia dados de eventos em um formato específico; consulte a documentação de eventos para entender os campos relevantes [hacodered.co.uk](https://www.hacodered.co.uk/n8n-and-evolution-api/#:~:text=Automating%20Workflows%20with%20n8n%20and,uperts%20to%20your%20defined%20webhook).
- **Filtro de Mensagens:** Ainda antes de chamar o bot, pode ser útil filtrar tipos de mensagem. Adicione um nó **IF** ou **Switch** após o Webhook: se o campo indicando o tipo da mensagem for texto (por ex., `message.text.body` existe), seguimos; se for mídia (áudio, imagem, etc.), trataremos separadamente; se for mensagem do próprio bot ou de grupo, podemos ignorar (ex.: Evolution API pode enviar eventos de mensagens enviadas pelo bot, que você não quer reprocessar). Configure essas condições conforme a estrutura do JSON de evento.

**3.2 – Tratamento de Mídias (áudio, imagem) – Opcional:**  
*(Se não for suportar mídia inicialmente, pode pular este sub-passo.)*

- **Áudio (Voice Notes):** Caso deseje que o bot entenda áudios dos clientes, integre um passo de **Speech-to-Text (STT)**. Uma solução rápida é usar o **OpenAI Whisper API** para transcrição, ou um modelo local se preferir. Por exemplo, no n8n coloque um nó HTTP Request para `https://api.openai.com/v1/audio/transcriptions` com o arquivo de áudio (que você pode obter via Evolution API download URL). A Evolution API geralmente fornece um URL ou ID para baixar a mídia. Use um nó HTTP GET para baixar o arquivo de áudio do WhatsApp (pode ser necessário fornecer cabeçalhos de autenticação da Evolution API). Depois, envie o arquivo para o Whisper API com o parâmetro `language=pt` para forçar português. Receba o texto transcrito.
- **Imagens/ PDFs:** Se o bot for lidar com imagens (ex.: cliente envia foto de um produto), você poderia usar um serviço de visão computacional ou OCR. Contudo, isso é avançado. Em muitos casos de vendas, imagens não são necessárias de processar automaticamente. Decida conforme seu caso. (Concorrentes costumam restringir o que o bot faz: alguns bots respondem a imagens dizendo "Posso ajudar com informações, mas não consigo ler imagens" ou usam OCR para ler texto em imagens se relevante). Para nosso escopo, podemos ignorar ou dar uma resposta padrão a mídias não suportadas inicialmente.
- **Atualize o Fluxo:** No Switch/IF do n8n, se for áudio, faça o processo de transcrição e então defina a variável de **texto da mensagem** com o texto transcrito; se for texto normal, use diretamente o conteúdo enviado. Assim, ao entrar na próxima etapa (chamada ao bot), teremos sempre uma variável unificada, digamos `mensagemCliente`, contendo o texto em português do que o usuário quer.

**3.3 – Chamar o Flowise (Modelo de IA) via n8n:**  
Agora vem a parte principal: enviar a mensagem do usuário para o modelo e obter a resposta. Há duas abordagens possíveis: usar a integração nativa Evolution API + Flowise, ou fazê-lo manualmente no n8n. Vamos optar pelo controle via n8n para poder interagir com DB e outras lógicas.

- **Requisição HTTP ao Flowise:** Adicione um nó **HTTP Request** após o tratamento da mensagem. Configure-o para método **POST** com URL apontando para o endpoint de previsão do Flowise, por exemplo: `http://SEU_SERVIDOR_FLOWISE:3000/api/v1/prediction/{chatflow-id}`. (Substitua `{chatflow-id}` pelo ID do chatflow que você criou no Passo 2 – você encontra esse ID na URL ou na lista de chatflows no Flowise UI).
- **Cabeçalhos e Corpo:** No header, inclua a API Key do Flowise (ex: `Authorization: Bearer SUA_KEY`). No corpo (JSON), envie os campos conforme a API do Flowise espera: geralmente algo como:
	```markdown
	{
	  "question": "<<<MENSAGEM DO CLIENTE>>>",
	  "overrideConfig": {
	      "sessionId": "<<<ID_SESSAO>>>"
	  }
	}
	```
	Onde em `"question"` você coloca o texto do cliente (use a referência da variável do nó anterior, ex: `{{$node["Webhook"].json["body"]["text"]}}` ou similar, dependendo de como n8n parseou) e em `sessionId` use o identificador único do usuário. Para o WhatsApp, pode usar o próprio número de telefone (Ex.: `"5511999999999"`). A Evolution API fornece `remoteJid` que costuma ser algo como `<numero>@s.whatsapp.net`. Você pode usar o número puro ou o JID completo – mas **atenção**: mantenha consistente, pois o Flowise tratará sessionIds diferentes como conversas separadas. Recomenda-se usar o número celular como ID da sessão. Assim, o Flowise retornará respostas lembrando do histórico desse usuário [docs.flowiseai.com](https://docs.flowiseai.com/integrations/langchain/memory#:~:text=You%20can%20separate%20the%20conversations,sessionId) [docs.flowiseai.com](https://docs.flowiseai.com/integrations/langchain/memory#:~:text=1.%20In%20the%20%60%2Fapi%2Fv1%2Fprediction%2F%7Byour,overrideConfig).
- **Recebendo a Resposta:** O Flowise retornará um JSON com a resposta do chatbot (campo geralmente chamado `answer` ou `response` dependendo da versão). Capture essa saída no n8n. Você pode fazer um parse JSON se necessário ou acessar diretamente o campo via expressão (ex: `{{$node["HTTP Request"].json["answer"]}}`). Este será o texto que o nosso atendente virtual quer enviar de volta ao cliente.
- **Tratamento da Resposta (emoção e formatação):** Opcionalmente, você pode pós-processar o texto antes de enviar. Por exemplo, pode adicionar **emojis** adequados para transmitir emoção (🙂🙌 etc.), ou ajustar quebras de linha para WhatsApp. Muitos chatbots de vendas utilizam emojis e tom informal para criar conexão emocional. Você pode decidir inserir isso no próprio prompt do sistema (ex: "use emojis ocasionalmente") ou fazer via n8n. Por simplicidade, defina isso já no prompt do Flowise para o modelo fazer – modelos como GPT conseguem colocar emojis naturalmente se instruídos.

**3.4 – Enviar a Resposta ao Usuário (WhatsApp via Evolution API):**  
Com a resposta pronta, use a Evolution API para enviar ao cliente no WhatsApp. Se instalou o node da Evolution API, use um nó específico **Evolution API → Send Message**: configure com as credenciais Evolution API, selecione o tipo de mensagem (texto ou áudio) e preencha o destinatário e conteúdo. Caso seu node não tenha a opção, podemos fazer manualmente via HTTP:

- **Mensagem de Texto:** A Evolution API possui um endpoint para enviar mensagens de texto (provavelmente `POST /instances/{id}/message` ou similar – ver docs). Com o node ou via HTTP, informe o número do destinatário (no formato internacional, ou use o JID fornecido) e o texto. Por exemplo, corpo JSON:
	```markdown
	{
	  "remoteJid": "5511999999999@s.whatsapp.net",
	  "message": "Conteúdo da resposta gerada pelo bot"
	}
	```
	Use a instância correta (se for via HTTP talvez a URL inclua o ID da instância). O node community do Evolution API simplifica isso, pedindo apenas o texto e destinatário. Ao executar, o Evolution API enviará a mensagem através do seu WhatsApp conectado.
- **Mensagem de Áudio (usando Kokoro):** Se optou por implementar voz, aqui é o momento de usar. Ao invés (ou além) de enviar texto, você pode enviar um áudio do bot falando aquela resposta. Use um nó HTTP para chamar o Kokoro: por exemplo, se Kokoro tiver endpoint `/v1/generate` onde você manda um texto e escolhe uma voz. Mande o texto da resposta e receba o áudio (algumas APIs retornam um URL para download, outras o binário/base64). Depois, utilize a Evolution API para mandar o áudio: provavelmente via um endpoint de envio de mídia (ex: `POST /instances/{id}/sendAudio` ou enviar mensagem com tipo áudio). Preencha os campos requeridos (geralmente o áudio em base64 ou um ID de mídia já carregada). Certifique-se de definir o mimetype correto (audio/ogg, mp3, etc., conforme o WhatsApp exige).
	> **Nota:** O envio de áudio é mais complexo: precisa garantir que o formato é suportado pelo WhatsApp (opus/ogg é usual para voz no WhatsApp). Pode ser necessário converter o áudio gerado para.ogg. Ferramentas como FFmpeg podem ser usadas via n8n (ex.: usando um nó de Exec para converter formato). Se não quiser complicar agora, você pode simplesmente enviar texto e implementar o áudio depois de validar o fluxo principal.
- **Enviar Imagens/Outros:** Similarmente, se o bot precisar enviar imagens (ex.: catálogo de produto), Evolution API suporta envio de mídia. Você usaria endpoints ou nó "Send Media". Isso não foi explicitamente requisitado, mas saiba que é possível. Por exemplo, concorrentes aproveitam para enviar folhetos ou fotos do produto via bot. Você precisaria hospedar ou dispor da imagem e chamar a API com a URL/base64 da imagem.

**3.5 – Integração com Banco de Dados via n8n:**  
Vamos incorporar aqui a interação com o banco de dados para memória longa e registro de leads:

- **Registro de Cliente Novo:** Antes de gerar resposta (logo após receber a mensagem, por exemplo), você pode adicionar um nó **Database** (MySQL/Postgres) ou **Spreadsheet** (Google Sheets) para verificar se o número do cliente já existe na tabela de clientes. Use o número (remoteJid ou telefone) como chave. Se não existir, o bot pode **perguntar o nome** do cliente na resposta ou simplesmente criar um registro vazio agora. Por exemplo, insira uma linha com `telefone=...` e talvez `nome=NULL`. Na próxima interação, quando o cliente fornecer o nome (você pode detectar padrão "meu nome é..."), atualize o registro. *Exemplo prático:* A Rasayel cita que muitos bots eficazes já começam perguntando informações do cliente na primeira interação [learn.rasayel.io](https://learn.rasayel.io/en/blog/whatsapp-chatbot-use-cases/#:~:text=When%20a%20new%20lead%20messages,%E2%80%9D%20It%20starts%20qualifying) – você pode implementar o bot para perguntar “Posso te chamar pelo nome? Qual seria?” e assim que o usuário responder, salvar no DB e passar a tratá-lo pelo nome. Isso cria uma experiência personalizada.
- **Salvar Históricos/Recomendações:** Após o bot responder, registre em uma tabela de histórico a pergunta e resposta, timestamp, etc., se quiser monitorar o desempenho ou para compliance. Também registre qualquer *sinal de venda* – por exemplo, se o cliente mostrou interesse em um produto específico, grave isso. Esses dados podem ser usados para **follow-ups** posteriores (ex.: se cliente não fechou a compra, o bot ou um vendedor humano pode entrar em contato mais tarde com uma oferta, usando o que foi aprendido na conversa).
- **Consulta de Dados no Meio da Conversa:** Suponha que o cliente pergunte "meu pedido #123 já foi enviado?". Você poderia, via n8n, detectar a palavra "pedido" e número e consultar seu sistema de pedidos (via node HTTP ou DB) e então **injetar a informação na conversa**. Uma forma: antes de chamar o Flowise, se a mensagem bate certos critérios, faça a consulta e formule uma resposta parcial ou fornecer ao Flowise como contexto extra. Por exemplo, você pode acrescentar no prompt do usuário algo como "Dados do pedido 123: enviado em 10/10, em trânsito". O LLM então incorpora isso na resposta final. Essa técnica garante respostas precisas em consultas de dados estruturados.

Em resumo, o n8n fica como **cérebro integrador** entre o WhatsApp, a IA (Flowise) e o mundo externo (DBs, APIs diversas), permitindo que seu atendente virtual tenha *conhecimento atualizado e memória persistente*. É nesse tipo de integração que muitos projetos comerciais se destacam.

**3.6 – Testar o Fluxo Completo no WhatsApp:**  
Ative o workflow no n8n e envie mensagens reais para o número do WhatsApp conectado, simulando interações de clientes. Teste cenários como:

- Primeira mensagem de um cliente novo (o bot deve cumprimentar e talvez perguntar nome ou como pode ajudar),
- Perguntas sobre produtos (o bot deve responder com detalhes e incentivar compra, ex. "Tem sim, posso te enviar o link para compra" ou "Esse produto está em promoção essa semana!"),
- Sequência de diálogo (ver se o bot lembra das respostas anteriores dentro da mesma conversa – ex.: Cliente: "Quero um notebook." Bot sugere alguns; Cliente: "Prefiro com mais memória." Bot deve lembrar do contexto e ajustar a recomendação),
- Emoções: teste o tom, se está amigável e paciente. Faça perguntas grosseiras ou confusas para ver se o bot mantém a calma (você pode instruir no prompt para ser **emocionalmente inteligente**, ou seja, lidar com cliente irritado com empatia).
- Se implementou voz, teste enviando um áudio de pergunta e veja se responde com áudio. Avalie a qualidade da voz gerada (Kokoro 82M por exemplo deve ter voz natural) e se o tempo de resposta é razoável.

Durante os testes, monitore o log do n8n e os logs do Evolution API (no console Docker ou no manager) para qualquer erro. Problemas comuns: formatação incorreta do número do destinatário, falta de sessão, expiração da sessão WhatsApp (se o WhatsApp desconectar, você terá que re-escanear QR), limites da OpenAI (se mandar mensagens muito longas ou muitas em pouco tempo, pode dar erro 429). Ajuste conforme necessário:

- Pode implementar retentativas no n8n (ex.: se o modelo falhar, tentar novamente ou mandar mensagem de erro amigável ao usuário).
- Use a função **keep session open** do Evolution API se disponível para não fechar a sessão do bot entre mensagens [doc.evolution-api.com](https://doc.evolution-api.com/v2/en/integrations/flowise#:~:text=,to%20simulate%20typing%20before%20sending) [doc.evolution-api.com](https://doc.evolution-api.com/v2/en/integrations/flowise#:~:text=,will%20not%20activate%20the%20bot) (no config do bot, `keepOpen: true` evita que cada mensagem reinicie o fluxo, embora usando nosso próprio controle isso não se aplica muito, pois nós mesmos gerimos a sessão via sessionId no Flowise).

## Passo 4: Aperfeiçoamento do Agente de Vendas (Treinamento e Melhorias)

Com o protótipo funcionando, é importante **refinar o comportamento** para maximizar resultados de vendas, seguindo boas práticas que observamos na concorrência:

- **Qualificação de Leads:** Garanta que o bot faz as perguntas certas inicialmente para qualificar o cliente. Por exemplo, bots de vendas bem-sucedidos perguntam logo de cara pelo interesse principal do cliente e filtros (ex.: orçamento, preferência) [learn.rasayel.io](https://learn.rasayel.io/en/blog/whatsapp-chatbot-use-cases/#:~:text=When%20a%20new%20lead%20messages,%E2%80%9D%20It%20starts%20qualifying). Isso permite oferecer o produto/solução adequada rapidamente. Treine o agente (via prompt ou fluxos condicionais) para fazer essas perguntas de qualificação de forma natural e não muito interrogativa (deixe conversacional).
- **Personalização e Conexão Emocional:** Utilize o nome do cliente nas respostas (após capturá-lo). Ex.: "Entendi, João! 😊 Vamos encontrar o melhor produto para você." – Esse toque pessoal melhora o engajamento. Insira algumas expressões de empatia: se o cliente expressa uma frustração ("Não encontrei X"), responda reconhecendo: "Sinto muito que você não tenha encontrado o que procura. Vamos resolver isso juntos, ok?". Essa inteligência emocional no atendimento é um diferencial que humaniza o bot. Você pode incorporar detecção de sentimento simples – por exemplo, se a mensagem contém palavras como "chateado", "não gostei", sinalize o modelo para responder de forma apaziguadora. Modelos avançados já capturam algum tom, mas não infalivelmente, então ajustar no prompt ajuda (ex: "Se o cliente demonstrar insatisfação, responda com empatia e oferecendo ajuda.").
- **Scripts de Vendas:** Muitos bots de vendas têm **scripts** ou fluxos pré-definidos para situações comuns: quando o cliente demonstra interesse em comprar, o bot pode oferecer um cupom de desconto; se o cliente hesita, o bot pode destacar uma vantagem ou estoque limitado para urgência. Planeje essas estratégias e incorpore-as. Isso pode ser via prompt (dando orientações do tipo "sempre que apropriado, ofereça um incentivo de venda") ou via lógica n8n (por ex., se o usuário digitar "vou pensar", o n8n pode interceptar e fazer o bot responder com algo preparado como "Claro, entendo. Posso reservar o item para você por 24h e oferecer um desconto de 5% se fechar hoje 😉"). Misturar automação de regras com a flexibilidade do LLM traz ótimos resultados.
- **Fallback e Handover:** Nenhum bot é perfeito. Defina um comportamento para quando o bot não souber responder corretamente ou o usuário insistir em falar com humano. Exemplos:
	- Se a confiança do modelo for baixa (difícil medir diretamente sem classificação adicional, mas você pode usar as mensagens do modelo como sinal – se ele responde com muita incerteza, talvez capturar frases como "não tenho certeza"), então retorne uma resposta padrão: "Desculpe, não possuo essa informação no momento. Posso conectar você a um atendente humano para ajudar com isso?".
		- Se o usuário escrever algo como "humano", "falar com atendente", etc., acione um fluxo de transferência. Isso poderia notificar um vendedor humano via e-mail ou plataforma (ex: integrar com Chatwoot ou CRM). A Evolution API pode se integrar ao Chatwoot [hacodered.co.uk](https://www.hacodered.co.uk/n8n-and-evolution-api/#:~:text=Today%2C%20Evolution%20API%20is%20not,support%20for%20Instagram%20and%20Messenger), que é uma plataforma onde humanos podem assumir chats. Implementar o handover: você poderia programar no n8n que, ao receber "quero falar com humano", ele muda um estado para não responder mais automaticamente e envia uma mensagem no grupo de suporte ou no Chatwoot indicando que o humano deve intervir. Esse é um requisito frequente em soluções profissionais, garantindo que a experiência do cliente não trava quando a IA falha.
- **Monitoramento de Performance:** Use o n8n para logar conversas e talvez acionar alertas. Por exemplo, envie as conversas para uma planilha do Google ou banco, e periodicamente reveja as interações para treinar melhorias. Verifique pontos onde o bot não converteu a venda ou perguntas que não conseguiu responder. Essa fase de *aprendizado contínuo* é o que diferencia um projeto bem-sucedido – a cada semana você pode ajustar prompts, adicionar conhecimento (FAQs novas) e melhorar a taxa de sucesso.
- **Prevenção de Erros e Conteúdo Inadequado:** Embora o modelo vá ser moldado pelo seu prompt, sempre há risco de respostas impróprias ou alucinações. Use mecanismos de segurança: por exemplo, implemente no n8n uma verificação das respostas do bot antes de enviar – procurar palavrões, dados sensíveis ou respostas incoerentes. Se encontrar, pode filtrar ou editar. Manter o sistema seguro é importante para não ofender clientes. (Produtos concorrentes às vezes colocam listas de palavras proibidas ou definem que se a resposta tiver baixa confiança, pedem desculpas e não respondem a aquela pergunta).

## Passo 5: Expansão para Instagram e Site (Omnichannel)

Tendo o agente funcionando no WhatsApp, podemos ampliar o alcance para Instagram Direct e um chat no site, reutilizando a mesma inteligência. A arquitetura será similar, mudando apenas a camada de entrada/saída de mensagens:

**5.1 – Integração com Instagram Direct:**

- O Evolution API anunciou suporte futuro a Instagram e Messenger [hacodered.co.uk](https://www.hacodered.co.uk/n8n-and-evolution-api/#:~:text=Today%2C%20Evolution%20API%20is%20not,support%20for%20Instagram%20and%20Messenger). Verifique se já está disponível na sua versão (a partir de 2025, essa funcionalidade pode ter sido adicionada). Se sim, o processo deve ser análogo ao do WhatsApp: criar uma instância Instagram na Evolution API, autenticar (provavelmente via token do Instagram Graph API ou login), e configurar webhook de mensagens do Instagram para o n8n. A Evolution API pretende unificar múltiplos canais, o que simplificaria muito – o mesmo fluxo n8n poderia tratar eventos de diferentes canais (verifique no payload do webhook um identificador do canal e adapte se necessário).
- Se a Evolution API ainda não oferecer Instagram, você pode integrar manualmente via **Instagram Graph API** (oferecido pelo Meta para contas Business). Nesse caso, seria um fluxo paralelo: configurar no Meta Developers uma webhook subscription para mensagens do Instagram, apontando para outro Webhook node do n8n. Recebe-se as mensagens e então passa igualmente para o Flowise (pode até usar o mesmo chatflow e sessionId como o username do IG) e responde via endpoints do Graph API (enviar mensagem de texto pela API do Instagram). Esse caminho exige uma página do Facebook vinculada e aprovação de mensagens, etc., mas é oficial. Se optar por algo mais rápido, **Chatwoot** é uma ferramenta que já integra Instagram e pode ser combinada com nosso bot: por exemplo, Chatwoot recebe a mensagem do Instagram, você configura Chatwoot para chamar uma *inbox automation webhook* (n8n) com a mensagem, o n8n obtém a resposta da IA e retorna via Chatwoot API. É uma arquitetura possível se já usar Chatwoot como central de atendimento (muitos concorrentes usam para integrar vários canais).
- O importante é que o **núcleo de IA** (Flowise chatflow e n8n logic) permaneça reutilizável. Apenas adicione novos triggers no n8n para outros canais que encaminham as consultas ao mesmo fluxo de tratamento (pode até unificar num só workflow, discriminando pelo campo source). Certifique-se de adaptar detalhes de formatação para cada canal (ex.: Instagram suporta menos caracteres por mensagem, ou não suporta certos tipos de mensagem como WhatsApp – verifique as limitações). Mas conceitualmente, seu agente Ginkgo passará a atender em todos canais de mensagem usados pelos clientes, mantendo consistência nas respostas.

**5.2 – Integração com Chat do Site:**

- Para o site da empresa, você pode implementar um **widget de chat** conectado ao bot. Há diversas abordagens:
	- **Usar o próprio Flowise UI/Widget:** O Flowise pode servir uma interface de chat embutida. Ele possui um endpoint de *embedded chat* que separa usuários automaticamente [docs.flowiseai.com](https://docs.flowiseai.com/integrations/langchain/memory#:~:text=UI%20%26%20Embedded%20Chat). Você poderia usar um iframe apontando para `http://SEU_FLOWISE:3000/chat/{chatflow-id}` que apresenta uma janela de chat pronta no site. Esse é o jeito mais simples – sem código, apenas embed. Cada visitante ganharia um `chatId` único gerado pelo Flowise para separar conversas [docs.flowiseai.com](https://docs.flowiseai.com/integrations/langchain/memory#:~:text=UI%20%26%20Embedded%20Chat). Teste essa solução: estilize conforme necessário (Flowise permite customizar um pouco ou você envolve num container no site).
		- **Integração via Typebot ou Similar:** Evolution API integra com o Typebot [hacodered.co.uk](https://www.hacodered.co.uk/n8n-and-evolution-api/#:~:text=Today%2C%20Evolution%20API%20is%20not,support%20for%20Instagram%20and%20Messenger), que é uma plataforma para chatbots web. Você poderia criar um bot no Typebot que na verdade usa Evolution/Flowise por trás. Porém, isso talvez seja redundante já que temos nosso próprio pipeline.
		- **Chatwoot Widget:** Se usar Chatwoot, ele oferece um widget de chat para site facilmente instalável. As mensagens chegariam no Chatwoot, e similar ao Instagram integration citada, você usaria automação via n8n para responder automaticamente. A vantagem do Chatwoot é que se o bot não responder, um humano do suporte pode ver e intervir diretamente na plataforma, tornando a transição invisível para quem está no site.
		- **Construir do zero:** Pode-se criar uma página de chat custom usando a API do Flowise diretamente no front-end (por exemplo, um script JavaScript que envia a pergunta do usuário ao endpoint REST do Flowise e exibe a resposta). Como já temos o n8n, poderíamos até expor um endpoint unificado (via webhook) para site: o site faz AJAX para o n8n, n8n manda ao Flowise e responde. Mas usar o embed nativo ou Chatwoot é muito mais rápido de implementar e menos propenso a bugs de CORS, etc.
- **Coerência entre canais:** Lembre-se de alinhar o tom e estilo do bot em todos os canais. Provavelmente o prompt criado já vale para todos (o bot se apresenta como assistente Ginkgo). Eventualmente, você pode variar saudações conforme canal (ex.: no WhatsApp pode usar saudações mais informais com emojis, no site talvez um pouco mais formal dependendo do público). Você pode detectar o canal e modificar a mensagem inicial no prompt via n8n (adicionar contexto "esta conversa veio do Instagram" se precisar). Mas, inicialmente, manter um único comportamento é ok.
- **Testes Multi-canal:** Repita os testes no Instagram (se integrado) e no site, para garantir que mensagens fluem corretamente e o sessionId isolado por usuário/canal (no site via embed Flowise isso já ocorre, no Instagram use o user ID do IG como sessionId, etc.). Garanta que se a mesma pessoa falar no WhatsApp e depois no Instagram, o bot **não** confunda as conversas – isso não deve acontecer se usamos identificadores diferentes por canal.

## Passo 6: Monitoramento, Manutenção e Considerações Finais

Agora o atendente virtual inteligente da Ginkgo está funcional. Alguns últimos pontos para garantir operação contínua e melhorias:

- **Escalabilidade:** Se o volume de usuários crescer, monitore o uso de recursos. O Flowise/OpenAI pode ser o gargalo. Para muitos usuários simultâneos, considere usar *streaming de respostas* para melhorar a experiência (Flowise e Evolution API suportam enviar mensagens enquanto são geradas, acho que não nativamente em nossa config, mas é algo a explorar). Também planeje limites – por exemplo, por segurança, você pode limitar a 5 perguntas por minuto por usuário para evitar abusos que gerem custo alto na API.
- **Custos:** Usando GPT-4/3.5, acompanhe o custo na conta OpenAI. Otimize tokens do prompt (resumos, limits) para economizar [n8n.io](https://n8n.io/workflows/3586-ai-powered-whatsapp-chatbot-for-text-voice-images-and-pdfs-with-memory/#:~:text=). Se o custo for alto, pode valer fine-tuning de um modelo menor ou uso de um modelo open-source hospedado (custo de servidor vs custo API – faça o balanço). A Evolution API em si é gratuita e auto-hospedada, mas lembre do risco: por ser não oficial para WhatsApp, há possibilidade do número ser banido se usar indevidamente (ex.: disparo massivo de mensagens *push* pode sinalizar como spam). Pelo relato de usuários, se usado para responder **somente mensagens entrantes** e sem comportamento suspeito, funciona estável (gente usando por 1 ano com 300 msgs/dia sem ban [reddit.com](https://www.reddit.com/r/n8n/comments/1m6ugx1/anyone_here_using_evolution_api_with_n8n_for/#:~:text=%E2%80%A2%20%202mo%20ago)). Apenas evite enviar muitas mensagens iniciando chat ou para grupos, para não violar os termos do WhatsApp [reddit.com](https://www.reddit.com/r/n8n/comments/1m6ugx1/anyone_here_using_evolution_api_with_n8n_for/#:~:text=%E2%80%A2%20%202mo%20ago).
- **Segurança e Privacidade:** Armazene as chaves API (Evolution, OpenAI) de forma segura, não exponha em front-end. Tenha atenção à LGPD: informe aos usuários que é um atendente virtual e possivelmente que as conversas podem ser armazenadas para melhorar serviço. Dados pessoais coletados (nome, telefone, preferências) devem ser protegidos. Implementar opção de o usuário solicitar falar com humano ou até *opt-out* do atendimento automatizado pode ser uma boa prática.
- **Melhorias Contínuas:** Leve em conta feedbacks. Talvez alguns usuários perguntem coisas fora do escopo (small talk ou assuntos pessoais). Decida como lidar – talvez programar o bot para responder brevemente e redirecionar de volta ao assunto de vendas. Mantenha o foco em conversão, mas sem ignorar cordialidade. Muitos chatbots perdem o usuário por não entenderem humor ou perguntas casuais – treine o seu para responder simpaticamente a um "Obrigado!" ou "Bom dia!" e manter o engajamento.
- **Resultados de Negócio:** Estabeleça métricas para avaliar o bot: taxa de conversão (quantos chats viram vendas ou leads qualificados), satisfação (você pode enviar ao final "Esta conversa te ajudou? \[👍/👎\]"), tempo médio de resposta (deve ser segundos). Compare esses números com antes do bot. Há casos de sucesso onde um bot qualifica leads em 2 minutos e dobra o número de reuniões marcadas para vendas [learn.rasayel.io](https://learn.rasayel.io/en/blog/whatsapp-chatbot-use-cases/#:~:text=Image%3A%20A%20chatbot%20flow%20for,routing%20qualified%20leads). Use esses indicadores para justificar o ROI e guiar ajustes.

Por fim, ao seguir este passo a passo, você construiu do zero um **atendente virtual de vendas multicanal** usando apenas ferramentas de baixo custo e alto poder. 🎉 Ao evoluir o projeto, você pode incorporar novas features (por exemplo: pagamentos via WhatsApp, sugestões proativas de promoção, integração com ERP para emitir pedidos, etc.). Mantenha a arquitetura modular – n8n e Flowise permitem adicionar quantas etapas quiser – e documente suas customizações. Boa sorte com seu agente de vendas inteligente da Ginkgo em produção! 🚀

**Fontes e Referências Utilizadas:**

- Documentação oficial Evolution API (WhatsApp) – instalação e conceitos [doc.evolution-api.com](https://doc.evolution-api.com/v1/en/get-started/introduction#:~:text=Evolution%20API%20is%20a%20project,a%20part%20of%20the%20project) [doc.evolution-api.com](https://doc.evolution-api.com/v1/en/get-started/introduction#:~:text=Terminal).
- Comunidade n8n – integração com Evolution API e dicas de configuração [community.n8n.io](https://community.n8n.io/t/evolution-api-and-n8n-how-to-configure/96559#:~:text=Solution%3A) [hacodered.co.uk](https://www.hacodered.co.uk/n8n-and-evolution-api/#:~:text=To%20receive%20message%20upsert%20events,via%20a%20HTTP%20Post%20request).
- FlowiseAI Docs – uso de memória e separação de sessões por usuário [docs.flowiseai.com](https://docs.flowiseai.com/integrations/langchain/memory#:~:text=You%20can%20separate%20the%20conversations,sessionId) [docs.flowiseai.com](https://docs.flowiseai.com/integrations/langchain/memory#:~:text=1.%20In%20the%20%60%2Fapi%2Fv1%2Fprediction%2F%7Byour,overrideConfig).
- Kokoro TTS – descrição da ferramenta de voz AI de alta naturalidade [easypanel.io](https://easypanel.io/docs/templates/kokoro#:~:text=Kokoro%20is%20a%20powerful%2C%20browser,applications%20with%20OpenAI%20API%20compatibility).
- Exemplo de fluxo n8n com memória para WhatsApp – demostrando uso de janela de 10 interações [n8n.io](https://n8n.io/workflows/3586-ai-powered-whatsapp-chatbot-for-text-voice-images-and-pdfs-with-memory/#:~:text=).
- Estudo de caso (Rasayel) – melhores práticas de chatbots de vendas no WhatsApp (qualificação rápida de leads) [learn.rasayel.io](https://learn.rasayel.io/en/blog/whatsapp-chatbot-use-cases/#:~:text=When%20a%20new%20lead%20messages,%E2%80%9D%20It%20starts%20qualifying) [learn.rasayel.io](https://learn.rasayel.io/en/blog/whatsapp-chatbot-use-cases/#:~:text=Image%3A%20A%20chatbot%20flow%20for,routing%20qualified%20leads).