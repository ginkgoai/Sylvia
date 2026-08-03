---
title: "GKO - Preparação para Curitiba"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/68f005a4-409c-8326-a6cb-5432ec208b0f"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
Perfeito — então o “plano Curitiba” está basicamente na reta final. O investidor já disposto a bancar moradia e escritório é ouro, mas ele quer ver o **MVP do Brann** funcionando, certo? Então o que falta pra tua ida é *quase tudo técnico e simbólico ao mesmo tempo*: provar que a máquina gira sozinha.

O que falta concretamente agora:

**1\. O Brann Base Operacional**  
Tu precisa do agente atendendo no WhatsApp com fluidez total:  
– Conexão 100% estável com Evolution API.  
– Fluxo principal no n8n (atendimento → entendimento → resposta → registro em CRM/planilha).  
– Respostas personalizáveis por variável de cliente.  
– Processo de “replicação fácil”: tu clica, duplica, troca variáveis, QR novo, pronto.  
Quando ele vê isso, vê escalabilidade e produto.

**2\. Demonstração Clara (Pitch Funcional)**  
Ele precisa visualizar o Brann “vendendo”. Prepara:  
– Um vídeo curto mostrando o bot respondendo e gerando leads.  
– Painel do n8n rodando (mostra que é teu backend, não um serviço terceirizado).  
– Mini site/página de apresentação da Ginkgo ou G-Tech com botão “fale com Brann”.  
É o pacote: aparência de produto pronto + prova técnica.

**3\. Preparativos de Transição**  
Com o investidor aprovando, tu já pode se organizar:  
– Backup dos fluxos (n8n export, Postgres dump).  
– Lista de ferramentas e logins essenciais.  
– Cronograma: 1 semana para entregar MVP + 1 semana para ir.

Então, a resposta literal: **o que falta para ir a Curitiba é o Brann em produção com replicação documentada**.

Se quiser, posso te montar agora um **roteiro de entrega técnica**, passo a passo, pra deixar esse MVP funcionando em até 7 dias e tu poder marcar a data da viagem com confiança. Quer que monte?

Sim. Use de base as conversas desse projeto GKO BRANN que estou usando para documentar o agente, pesquise nos melhores blogs de automação com n8n os projetos dicas e novidades, foque no essencial mensagem do cliente vem, inteligência transcreve, agente entende e gera a MELHOR resposta, envia a resposta, sempre humanizadamente e utilizando só n8n, com acesso a ferramentas habituais do aplicativo ou APIs como serpapi, memória curta e longa utilizando supabase, adapte as dicas a projetos de whatsapp oficial para uso da evolution api.

Para montar um roteiro técnico final para entrega do MVP Brann 100% funcional, preciso só alinhar alguns pontos com você:

1. Você já tem o subfluxo AUDIO com os áudios prontos no n8n? Quer que eu inclua isso no roteiro com exemplos?
2. O envio e recebimento de mensagens pela Evolution API está funcionando ou precisa de ajuda com algum nó?
3. Prefere que eu monte o roteiro com foco em **produção (mínimo viável e replicável)** ou quer incluir elementos opcionais como **painel de monitoramento e logs avançados**?

Me confirma isso rapidinho que eu já te entrego o plano fechado com passo a passo e checklist pra validação com investidor.

Boa. Para o áudio usaremos KOKORO. Todos os aplicativos, n8n, kokoro, evolution api, estão funcionando bem em nuvem, tudo certo. O fluxo inicial já está feito como você pode acompanhar no projeto, precisamos é adaptar o que tá dando errado, melhor e fazer funcionar. A parte da voz tts não está feita.

Perfeito. Vou montar um roteiro técnico atualizado para entregar o MVP Brann com foco total no WhatsApp oficial via Evolution API, transcrição inteligente, TTS com Kokoro e memória Supabase, usando só o n8n. Vou buscar também as melhores práticas e atualizações de projetos reais em blogs de automação com n8n para incorporar soluções replicáveis, robustas e documentadas para apresentação ao investidor.

Já volto com isso formatado!

## MVP do Brann: Agente WhatsApp Automatizado com n8n (Roteiro Técnico)

## Visão Geral e Objetivo do MVP

O **Brann** é um agente automatizado via WhatsApp (utilizando a API Evolution) orquestrado inteiramente pelo n8n. Ele receberá mensagens de clientes em diversos formatos (texto, áudio, imagem ou vídeo), aplicará inteligência para entender o conteúdo (transcrição de áudio via OpenAI Whisper, OCR de imagens, sumarização de textos longos, etc.), interpretará a solicitação usando um modelo **GPT-4** com memória de conversas armazenada no **Supabase**, e responderá de forma **humanizada** em português. As respostas serão enviadas preferencialmente em áudio (geradas por um mecanismo *text-to-speech* **Kokoro TTS**), com fallback para texto caso haja falha na geração de voz.

Este roteiro técnico detalha os nós e configurações do fluxo no n8n passo a passo – desde a recepção do webhook do WhatsApp até o envio da resposta – incluindo boas práticas de configuração (variáveis de ambiente para credenciais, controle de versões, monitoramento) e dicas avançadas de otimização inspiradas em casos de uso da comunidade n8n. O resultado esperado é um fluxo replicável e robusto, documentado de forma clara para que até um investidor não técnico consiga entender o funcionamento do MVP.

## Pré-requisitos e Configuração Inicial

Antes de construir o fluxo, garanta que os seguintes recursos e configurações estejam prontos:

- **Instância do Evolution API (WhatsApp)**: Uma instância configurada e conectada a um número de WhatsApp válido. Anote o `instance` (identificador da instância) e obtenha a **API Key** do Evolution API para autenticação. Também defina um **Webhook URL** apontando para o n8n (explicado adiante).
- **Ambiente n8n**: n8n instalado (auto-hospedado ou cloud) acessível via HTTPS para receber webhooks. Certifique-se de habilitar no n8n as Community Nodes caso vá usar nós comunitários (ex.: OCR).
- **Contas de API externas**:
	- **OpenAI**: Chave de API para usar GPT-4 e Whisper (transcrição de áudio).
		- **Supabase**: Banco de dados Postgres (com pgvector, se for usar busca vetorial) para armazenar o histórico/memória do chat.
		- **Kokoro TTS**: Motor de voz. Instale e execute o Kokoro TTS (ex.: via Docker ou localmente) expondo um endpoint compatível com a API de voz OpenAI, ou tenha acesso a uma API externa do Kokoro. No nosso exemplo, assumiremos que o Kokoro está acessível em `http://localhost:8880/v1` (endereço local padrão do Kokoro via *Voice Mode* [voice-mode.readthedocs.io](https://voice-mode.readthedocs.io/en/latest/kokoro/#:~:text=1,OPENAI_API_KEY) [voice-mode.readthedocs.io](https://voice-mode.readthedocs.io/en/latest/kokoro/#:~:text=To%20use%20a%20different%20Kokoro,endpoint%20or%20force%20its%20use)).
		- **OCR (se aplicável)**: Opcionalmente, cadastro em algum serviço de OCR (p.ex. OCR.Space ou **Mistral AI OCR**) caso não use o node comunitário. A comunidade recomenda o OCR da Mistral AI pela precisão, acessível via chamada HTTP [community.n8n.io](https://community.n8n.io/t/best-way-to-get-ocr-data-in-n8n/158921#:~:text=In%20my%20opinion%20Mistral%20AI%E2%80%99s,prem%20instance%20for%20better%20privacy).
- **Variáveis de Ambiente no n8n**: Configure variáveis no sistema do n8n para armazenar credenciais e configurações sensíveis, facilitando replicação e segurança. Por exemplo:
	- `EVOLUTION_URL` (URL base da API Evolution, ex.: `https://seu-servidor.com`),
		- `EVOLUTION_APIKEY`,
		- `EVOLUTION_INSTANCE`,
		- `OPENAI_API_KEY`,
		- `SUPABASE_URL`,
		- `SUPABASE_SERVICE_ROLE_KEY` (ou outra credencial de acesso),
		- `KOKORO_BASE_URL` (ex.: `http://127.0.0.1:8880/v1`),
		- `BRANN_TTS_ENABLED` (flag booleana ou chave para habilitar respostas em áudio).
	> **Nota:** No n8n, essas variáveis podem ser referenciadas via expressões (por exemplo, `{{$env.OPENAI_API_KEY}}`). Usar variáveis de ambiente mantém credenciais fora do fluxo e facilita mudança de ambiente (desenvolvimento/produção) sem editar nós manualmente.

## Fluxo Geral do n8n

Antes de detalhar nó a nó, segue um resumo do fluxo lógico que iremos implementar no n8n:

1. **Recepção de Mensagem (Webhook)** – Um nó Webhook aguardará chamadas do Evolution API quando novas mensagens chegarem no WhatsApp. Cada evento recebido contém informações do remetente e do conteúdo (inclusive tipo de mídia).
2. **Identificação do Tipo & Roteamento (Switch)** – Usamos um nó Switch (ou IFs) para determinar o tipo de mensagem: texto, áudio, imagem ou vídeo. Isso direciona o fluxo para o tratamento adequado em cada caso.
3. **Processamento da Mídia** – Em cada ramificação:
	- **Texto**: O texto é passado adiante diretamente (com possíveis normalizações).
		- **Áudio**: O arquivo de áudio é baixado via API, depois transcrito em texto (usando OpenAI Whisper).
		- **Imagem**: A imagem é baixada e passamos por OCR para extrair texto bruto; se o texto for muito extenso, podemos sumarizá-lo.
		- **Vídeo**: O vídeo é baixado; extraímos o áudio e o transcrevemos (equivalente a áudio). Para vídeos sem áudio relevante, podemos preparar uma resposta padrão indicando a limitação.
4. **Consulta de Memória (Supabase)** – Buscamos no Supabase o histórico de conversas do usuário (ex.: últimas mensagens trocadas ou informações contextuais relevantes) para fornecer contexto ao modelo GPT-4.
5. **Interpretação da Mensagem (OpenAI GPT-4)** – Montamos o prompt para o modelo GPT-4, incluindo contexto (memória) e a mensagem atual do usuário transcrita. O modelo GPT-4 gera então uma resposta em texto. Usaremos um nó OpenAI (ou um HTTP Request) configurado para o modelo GPT-4.
6. **Geração de Resposta em Áudio (Subfluxo TTS)** – Se **respostas de voz estiverem ativadas** (`BRANN_TTS_ENABLED=true`), acionamos um subfluxo responsável por converter o texto de resposta em áudio usando o Kokoro TTS. Esse subfluxo retorna o áudio gerado ou, em caso de falha, sinaliza para usar o texto como fallback.
7. **Envio da Resposta (HTTP -> Evolution API)** – Por fim, enviamos a resposta ao usuário no WhatsApp. Se for em áudio, usamos o endpoint de enviar áudio do Evolution API; se for texto (ou fallback), usamos o endpoint de texto. Em ambos os casos, utilizamos o nó HTTP Request para fazer uma chamada autenticada à API do Evolution, passando o número do destinatário, conteúdo e parâmetros como delay e presença (para simular digitando/gravando).
8. **Logs e Armazenamento** – Opcionalmente, registramos no Supabase (ou log interno) a interação ocorrida: mensagem do usuário, resposta do Brann, timestamp etc., para fins de auditoria e melhoria contínua. O fluxo então termina.

Em seguida, veremos cada etapa e os nós correspondentes em detalhe.

## 1\. Nó Webhook – Recebendo Mensagens do WhatsApp (Evolution API)

**Nó:** *Webhook* (Trigger)

Este nó inicia o fluxo ao receber um HTTP POST do Evolution API com um evento de nova mensagem do WhatsApp. Configure o Webhook da seguinte forma:

- **HTTP Method**: POST
- **Path**: Defina um endpoint único, por exemplo `/webhook/brann/messages`. O Evolution API irá chamar este URL quando chegar uma mensagem. (OBS: Mantenha a URL em segredo, já que funciona como token de segurança.)
- **Respond**: Pode ser imediato (200 OK) ou esperar o fluxo concluir. Aqui, podemos usar **Response Mode = 'On Received'** para responder imediatamente com um status 200 vazio, já que o envio da resposta ao usuário será feito separadamente via API do Evolution.

No console do Evolution API, você deve registrar esse webhook para o evento de mensagens. Se estiver usando o node comunitário do Evolution, há um recurso específico para **Registrar Webhook**. Caso contrário, faça manualmente uma chamada HTTP para o Evolution API configurando o webhook. Por exemplo, via cURL ou um nó HTTP no n8n (executado uma vez) para o endpoint `/instance/setWebhook` com body contendo a URL do webhook e o evento `MESSAGES_UPSERT`. De acordo com a documentação e comunidade, o evento **MESSAGES\_UPSERT** é o que notifica novas mensagens recebidas [docs.evoapicloud.com](https://docs.evoapicloud.com/instances/events/events-system#:~:text=Message%20Events). Importante: a *community node* do Evolution registra o webhook mas não recebe os dados; é necessário o Webhook nativo do n8n para capturar o payload [community.n8n.io](https://community.n8n.io/t/evolution-api/126278#:~:text=Evolution%20API%20Node%20Role%20The,This%20is%20key).

Após configurar, teste enviando uma mensagem de qualquer conteúdo para o WhatsApp do bot. O n8n deve registrar uma execução do webhook contendo dados JSON da mensagem. Um exemplo (simplificado) de payload recebido:

```markdown
{
  "event": "MESSAGES_UPSERT",
  "instanceId": "seu_instance_id",
  "data": [{
    "from": "551199998888@c.us",
    "message": {
      "conversation": "Olá, preciso de ajuda"
    },
    "messageTimestamp": "2025-10-15T20:20:30.000Z",
    "type": "notify"
  }]
}
```

Os detalhes exatos podem variar; por exemplo, mensagens de mídia virão com outras propriedades (veremos adiante). O importante é que temos:

- **Remetente** (`from`): normalmente no formato `<numero>@c.us` para contatos individuais.
- **Conteúdo da mensagem**: em subcampos de `message` – pode ser `conversation` (texto), `imageMessage`, `audioMessage`, `videoMessage` etc., dependendo do tipo.
- **Timestamp, IDs, flags** (tipo notify, fromMe etc. que podemos ignorar para nosso processamento básico).

Para facilitar o manuseio, você pode adicionar imediatamente após o Webhook um nó *Function* (ou *Set*) para normalizar/parsear os dados. Exemplo: extrair o número do usuário e o tipo de mídia em variáveis mais simples. Isso ajuda a manter o restante do fluxo mais legível. Por exemplo, um **Function** node com código:

```markdown
// Supondo que payload está em items[0].json.data[0]
const msg = items[0].json.data[0];
return [{
  userNumber: msg.from.replace('@c.us',''),
  text: msg.message.conversation || null,
  hasImage: !!msg.message.imageMessage,
  hasAudio: !!msg.message.audioMessage,
  hasVideo: !!msg.message.videoMessage,
  msgId: msg.id
}];
```

Assim preparamos campos como `userNumber` (o telefone do cliente) e flags indicando o tipo recebido. Outra abordagem é usar diretamente um nó **Switch** ou vários **IFs**, checando a existência de certos campos no JSON original. A escolha depende da preferência; ambos funcionam.

## 2\. Nó Switch – Roteamento por Tipo de Mensagem

**Nó:** *Switch* (ou múltiplos *IF* encadeados)

Utilize um nó Switch para ramificar o fluxo de acordo com o tipo de mensagem recebida. Configure-o para avaliar uma propriedade que indica o tipo de conteúdo. Se você usou o Function acima, pode verificar por exemplo:

- Se `text` não é nulo -> caso "Texto".
- Se `hasAudio` é true -> caso "Áudio".
- Se `hasImage` é true -> caso "Imagem".
- Se `hasVideo` é true -> caso "Vídeo".

> Dica: A ordem das checagens importa se houver mensagens com múltiplos conteúdos (por exemplo, uma imagem pode ter `caption` de texto simultaneamente). Geralmente, trate mídias específicas antes do caso genérico de texto puro. Você também pode combinar condições no Switch; por exemplo, `hasImage == true` vai para ramo imagem, senão se `hasAudio == true` vai para áudio, etc., e por fim um *default* que caia em texto.

O resultado desse nó serão quatro saídas (você pode nomeá-las para clareza: "Texto", "Áudio", "Imagem", "Vídeo"), cada qual ativa quando a condição correspondente for atendida. A partir de cada saída, montaremos sub-fluxos específicos:

- **Fluxo Texto:** Mensagens puramente textuais.
- **Fluxo Áudio:** Mensagens de voz ou áudio.
- **Fluxo Imagem:** Imagens (inclui fotos, scans, etc).
- **Fluxo Vídeo:** Vídeos ou GIFs.

Cada um será detalhado a seguir.

## 3\. Processamento Inteligente de Mensagens por Tipo

### 3.1. Mensagens de Texto

Este é o caso mais simples. O conteúdo de texto já vem no payload (`msg.message.conversation`).

**Nós envolvidos:** possivelmente nenhum extra aqui, apenas preparar para a etapa de GPT:

- **Normalize Text (opcional):** Use um nó *Function* ou *Set* para limpeza básica do texto, se necessário (por exemplo, remover quebras de linha excessivas, corrigir encoding). Isso pode ajudar a evitar consumir tokens com textos desnecessários no prompt.
- **Passar para próxima etapa:** A saída deste ramo seguirá direto para a etapa de *Consulta de Memória + GPT-4* (seção 4), carregando consigo o texto do usuário em um campo, digamos `userMessage`.

*Neste ponto, nenhuma chamada externa foi feita ainda.* Toda mensagem de texto segue local até compor o prompt para o modelo de linguagem.

### 3.2. Mensagens de Áudio

Para mensagens de áudio (ex.: notas de voz do WhatsApp), precisamos transcrever o conteúdo em texto.

**Nós e passos:**

1. **Download do Áudio (HTTP Request GET):** O Evolution API não envia o arquivo binário diretamente no webhook por padrão; ele pode fornecer um ID ou URL. Para obter o arquivo:
	- Se o webhook contiver uma URL de mídia (às vezes o Evolution API traz `message.audioMessage.url` apontando para os servidores do WhatsApp), podemos tentar um HTTP Request diretamente para essa URL. Porém, geralmente é necessário autenticar a requisição (cookies do WhatsApp Web). Uma via mais simples é usar a API do Evolution para obter o arquivo já autenticado.
		- Utilize o endpoint `GET /chat/getBase64FromMediaMessage/{instance}` do Evolution API, passando a identificação da mensagem. Esse endpoint retornará a mídia codificada em base64 [doc.evolution-api.com](https://doc.evolution-api.com/v2/api-reference/message-controller/send-media#:~:text=Teste%20de%20caption) [doc.evolution-api.com](https://doc.evolution-api.com/v2/api-reference/message-controller/send-audio#:~:text=number). Podemos chamar via um nó **HTTP Request**, configurado assim:
		- **URL:** `{{$env.EVOLUTION_URL}}/chat/getBase64FromMediaMessage/{{$env.EVOLUTION_INSTANCE}}`
				- **Method:** POST (conforme docs do Evolution para *getBase64*, usa POST)
				- **Auth:** adicionar header `apikey: {{$env.EVOLUTION_APIKEY}}`.
				- **Body:** JSON contendo os dados necessários para identificar a mensagem. Segundo a documentação, deve incluir a *key* e *message* conforme recebido. Por exemplo:
			```markdown
			{
			  "key": { "id": "ID-da-mensagem", "remoteJid": "553199999999@c.us" },
			  "message": { "audioMessage": { } },
			  "convertToMp4": true
			}
			```
			Aqui passamos `convertToMp4: true` para que, caso o áudio seja formato OGG/Opus (padrão do WhatsApp), ele seja convertido para MP4 (m4a) compatível com a API de transcrição e mais universal.
		- **Parse Response:** Marque a opção de **Resolve to JSON** = true se a resposta vier como JSON contendo o base64. O retorno provavelmente terá um campo com o base64 (ou erro). Você pode extrair o base64 em, por exemplo, `item.binary.audio.data` usando um nó Set ou Function.
	> 💡 *Dica:* Se usar um nó HTTP Request para baixar direto a mídia via URL, marque "Download Binary Data" para salvar em binário. No entanto, esse método exige que a URL do WhatsApp seja pública ou que você inclua cookies de sessão. O método via API Evolution é mais garantido.
2. **Conversão Base64 -> Binário (Move Binary Data):** Após obter a string base64 do áudio, converta-a em um arquivo binário dentro do n8n. Use o nó **Move Binary Data** para mover de JSON para binário:
	- Input: selecione o campo JSON que contém a string base64.
		- Set options: `Convert = To Binary` e informe o nome do arquivo (ex.: `input.mp3`) e o tipo (`audio/mp4` se for m4a).  
		Isso vai resultar em um binário no item, que pode ser referenciado adiante (ex.: `item.binary.data` contendo o áudio).
3. **Transcrição com OpenAI (Whisper-1):** Agora use um nó **OpenAI** configurado para transcrição:
	- **Resource:** Audio
		- **Operation:** Transcribe a Recording
		- **Model:** whisper-1 (padrão).
		- **Binary Property:** indique o nome do campo binário do item (por padrão é `data` ou `audio` dependendo do passo anterior). Por exemplo, se o Move Binary Data colocou em `data`, use `data` aqui.
		- **Additional Options:** Pode especificar `Language` = "pt" (português) para melhorar acurácia e velocidade, já que as mensagens presumivelmente são em português.
		- Este nó enviará o áudio para a API da OpenAI e retornará a transcrição em texto do que foi falado no áudio.
	*Alternativa:* Você pode usar o **HTTP Request** diretamente para `https://api.openai.com/v1/audio/transcriptions` se preferir controle manual. Mas o nó OpenAI já abstrai isso. Lembre-se de configurar a credencial OpenAI do nó com sua API Key (pode ser referenciada via variável de ambiente). O modelo Whisper aceita arquivos de áudio nos formatos mp3, mp4, m4a, wav, ogg, webm, etc [docs.n8n.io](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations/#:~:text=,webm) – por isso convertemos/garantimos mp4/m4a no passo anterior.
4. **Resultado da Transcrição:** O nó OpenAI retornará provavelmente um campo `text` com a transcrição completa. Você pode renomeá-lo para `userMessage` para uniformizar com os casos de texto. É importante tratar ruídos: se a transcrição falhou ou ficou vazia (por áudio ininteligível), você deve definir um fallback, por exemplo:
	- Se `text` está vazio ou muito genérico, você pode definir `userMessage = "(não foi possível transcrever o áudio)"` e depois o GPT pode responder algo do tipo pedindo para o usuário repetir. Isso evita enviar prompt vazio ao GPT.

No final deste subfluxo de áudio, teremos em mãos uma string de texto em `userMessage` que representa o que o usuário falou no áudio. Esse valor segue para a etapa de GPT-4, semelhante ao caso de texto puro.

### 3.3. Mensagens de Imagem

Para imagens enviadas pelo usuário (fotos de documentos, capturas de tela etc.), o objetivo é extrair texto (se houver) e/ou entender o conteúdo da imagem para responder apropriadamente.

**Passos:**

1. **Download da Imagem (HTTP Request GET):** Assim como no áudio, usamos o Evolution API para obter a imagem. Provavelmente o payload do webhook traz `message.imageMessage` com metadados e possivelmente uma URL. Podemos reutilizar o mesmo endpoint **getBase64FromMediaMessage**:
	- Envie a requisição com a `key` e o objeto `message: { "imageMessage": {} }` correspondentes à imagem [doc.evolution-api.com](https://doc.evolution-api.com/v2/api-reference/message-controller/send-media#:~:text=Teste%20de%20caption).
		- Receba o base64 da imagem (atenção: imagens podem ser grandes, certifique-se que o n8n suporta o tamanho ou aumente limites se necessário).
2. **Base64 -> Binário:** Use **Move Binary Data** para converter a imagem base64 em binário (defina o nome do arquivo com extensão correta, ex. `.jpg` ou `.png`, e Content-Type apropriado `image/jpeg` etc.).
3. **OCR da Imagem:** Para extrair texto, escolha uma das abordagens:
	- **Node Comunitário Tesseract.js:** Há um node não-oficial `n8n-nodes-tesseractjs` que integra o OCR Tesseract diretamente no n8n [community.n8n.io](https://community.n8n.io/t/best-way-to-get-ocr-data-in-n8n/158921#:~:text=Since%20it%E2%80%99s%20an%20image%20you,tesseractjs). Se instalar, basta conectar o binário da imagem nesse node; ele retornará o texto reconhecido.
		- **Serviço OCR via HTTP:** Alternativamente, use um serviço externo. Por exemplo:
		- **OCR.Space API:** que é gratuita até certo limite. Envie o binário via form-data usando HTTP Request (com opção *Send Binary Data*).
				- **Mistral AI OCR API:** recomendado pela comunidade como uma das melhores opções atualmente [community.n8n.io](https://community.n8n.io/t/best-way-to-get-ocr-data-in-n8n/158921#:~:text=In%20my%20opinion%20Mistral%20AI%E2%80%99s,prem%20instance%20for%20better%20privacy). Você faria um POST para o endpoint deles com a imagem; o retorno é o texto ou JSON estruturado dependendo da API.
				- **Google Vision API:** se já tiver conta GCP, o node do Google Vision (ou HTTP) pode detectar texto em imagens (método *DOCUMENT\_TEXT\_DETECTION*).
		- **OpenAI Vision (GPT-4V):** *Observação:* a OpenAI lançou GPT-4 com visão, mas a API ainda não está amplamente disponível. Se estivesse, poderíamos mandar a imagem para GPT-4 e obter resposta direta. Por ora, assumiremos OCR tradicional seguido de GPT.
	Configure, por exemplo, o node OCR escolhido para produzir um campo `extractedText` com todo o texto encontrado na imagem.
4. **Pós-processamento do Texto OCR (Parser):** Texto extraído de imagens pode vir desordenado ou com ruídos (ex: cabeçalhos repetidos, artefatos de reconhecimento). Aplique um parser/normalizador:
	- Você pode usar um nó **Code** para limpar o texto (remover quebras excessivas, caracteres especiais, espaços duplicados).
		- Ou, caso queira algo mais semântico, usar o próprio GPT-4 para resumir ou estruturar o texto. Por exemplo, se a imagem for uma nota fiscal e você precisa de certos campos, pode pedir ao GPT para extrair *apenas* aqueles campos do texto OCR. Tenha em mente que isso consome tokens, então decida conforme a necessidade (um Code node não tem custo de API).
		- A comunidade sugere frequentemente usar um Code node para filtrar/formatar resultados do OCR antes de enviar a um modelo [community.n8n.io](https://community.n8n.io/t/best-way-to-get-ocr-data-in-n8n/158921#:~:text=After%20extracting%20the%20text%20from,don%E2%80%99t%20mind%20spending%20extra%20tokens), economizando tokens.
	Suponha que do OCR resultou `extractedText`. Podemos, por exemplo, se for muito longo (mais que X caracteres), obter um resumo: **Opcional** – chamar GPT-3.5 ou GPT-4 com um prompt: "Resuma em uma frase o texto a seguir:...". Isso pode ser útil caso usuários tirem foto de textos muito longos; assim o agente não precisa analisar cada detalhe, só a essência.
5. **Definir `userMessage`:** Com base no caso de uso, podemos definir a mensagem final do usuário para o GPT de diferentes formas:
	- Se a imagem era algo contendo texto (documento, placa, screenshot de conversa), podemos tratar `userMessage = "Texto da imagem: ..." + extractedText` para que o GPT receba esse conteúdo e possa responder perguntas sobre ele.
		- Se a imagem é puramente visual (ex.: "enviei uma foto do meu produto com defeito"), o agente pode não ter capacidade de *visão* computacional além do OCR. Nesse MVP, poderíamos ter um fallback do tipo `userMessage = "(Imagem recebida: descrição não suportada pelo MVP)"` e o GPT então responderia gentilmente que ainda não consegue ver imagens mas pede descrição ou informa limitações.
		- Uma terceira opção: integrar serviços de visão computacional para identificação de objetos, mas isso foge do escopo textual pedido. Para nosso roteiro, vamos nos ater ao OCR.
	Portanto, se `extractedText` não estiver vazio, use-o. Caso contrário, registre que não há texto legível. Em ambos os casos, o fluxo seguirá para o GPT com um `userMessage` adequado (por ex: *"Usuário enviou a imagem de um documento contendo o texto: \[conteúdo extraído\]"* ou *"Usuário enviou uma imagem (nenhum texto pôde ser extraído)."*).

### 3.4. Mensagens de Vídeo

Mensagens de vídeo combinam desafios de áudio e imagem. No MVP, focaremos em extrair a parte de áudio (por exemplo, se for um vídeo falando algo) para compreender instruções faladas. Análise visual do vídeo (ex.: reconhecer cenários) não será implementada aqui, pois exigiria modelos de visão avançados.

**Passos:**

1. **Download do Vídeo:** Igual aos casos anteriores, use **getBase64FromMediaMessage** com `"message": { "videoMessage": {} }`. O Evolution API retornará o vídeo em base64 (provavelmente formato MP4). Lembre-se que vídeos podem ser grandes; verifique limites e talvez rejeite vídeos muito longos para evitar exceder limites do Whisper (que é ~25 MB de áudio).
2. **Extrair Áudio do Vídeo:** Se o vídeo tiver áudio, precisamos isolá-lo:
	- Uma opção simples: o Evolution ao usar `convertToMp4: true` possivelmente já retorna o arquivo.mp4. Podemos enviar esse MP4 diretamente para o Whisper, pois ele aceita `.mp4` e extrai o áudio interno [docs.n8n.io](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations/#:~:text=,webm). Ou
		- Usar uma ferramenta de conversão. No n8n, poderíamos usar um comando *ffmpeg* via nó **Execute Command** (isso requer o binário ffmpeg disponível). Por exemplo, executar: `ffmpeg -i input.mp4 -vn -acodec copy output.m4a` para separar o áudio sem re-encoding. Porém, isso adiciona complexidade e possivelmente não é necessário se Whisper já fizer internamente.
		- Simples: tente mandar o MP4 direto para o nó OpenAI de transcrição. Muitas vezes funciona, já que Whisper ignora a parte de vídeo e pega o áudio.
3. **Transcrição via Whisper:** Igual ao caso 3.2, use OpenAI *Transcribe* com o binário (MP4) do vídeo. Configure modelo whisper-1 e aguarde o texto. Se o vídeo não tinha fala ou áudio claro, a transcrição resultará vazia ou irrelevante. Trate essa situação:
	- Se obtivermos texto, ótimo, use como `userMessage`.
		- Se não, considere retornar uma resposta padrão ao usuário: ex: "Desculpe, não consegui extrair nenhuma informação do vídeo." (Isso podemos definir mais à frente no GPT ou antes).
4. **(Opcional) Resumo do Vídeo:** Se a transcrição do vídeo for muito longa (ex.: usuário enviou um longo vídeo falando), poderíamos somar uma etapa de **Summarization** aqui antes de enviar ao GPT principal, para não sobrecarregar contexto. Um nó OpenAI (GPT-3.5) poderia resumir em pontos-chave. Fica como melhoria opcional.

No fim, definimos novamente `userMessage` com o texto transcrito do vídeo ou uma indicação de falha.

Agora, após processar cada tipo, **todos os ramos convergem** para a próxima fase: temos um `userMessage` em todos os casos, que representa em texto claro o que o usuário quer (seja originalmente texto, fala ou texto extraído de mídia). Podemos então alimentar nossa IA.

## 4\. Integração com Memória (Supabase) e Contexto do Chat

Antes de chamar o GPT-4, vamos incorporar memória de conversas passadas para que o agente tenha contexto e consistência (por exemplo, lembrar do que foi falado anteriormente pelo usuário, preferências, ou simplesmente manter o fio da conversa).

**Estratégia de Memória:** Usaremos o Supabase (Postgres) como repositório de memória. Uma abordagem simples é armazenar cada mensagem do usuário e resposta do bot em uma tabela (colunas: user\_id, role, content, timestamp, etc.). Ao chegar uma nova mensagem, buscamos as últimas *N* interações daquela pessoa para incluir no prompt.

Para eficiência, podemos limitar a, digamos, 5 últimas mensagens de cada lado, ou fazer uma busca vetorial de mensagens relevantes (se implementássemos embeddings). No MVP, faremos o básico: últimas mensagens.

**Nós:**

- **Supabase (Read)** – Use um nó **Postgres** (já que Supabase é compatível) ou o node específico do Supabase caso exista. Configure credenciais (pode usar var env `SUPABASE_URL` e `SUPABASE_SERVICE_ROLE_KEY` se for usar a Service Role for full R/W).
	- Consulta: `SELECT role, content FROM chat_messages WHERE user_id = $1 ORDER BY timestamp DESC LIMIT 10;` (adaptar nomes conforme seu esquema). Substitua `$1` pelo identificador do usuário (no WhatsApp, podemos usar o número de telefone como ID único do cliente).
		- Isso retorna um conjunto de registros. Pode-se manipular via n8n: por exemplo, usar um nó **Function** para formatar esses registros em um texto concatenado. Por exemplo:
		```markdown
		const history = items.map(item => {
		  if(item.json.role === 'user'){
		    return \`Usuário: ${item.json.content}\`
		  } else {
		    return \`Brann: ${item.json.content}\`
		  }
		});
		return [{history: history.reverse().join("\n") }]; // reverse para ordem cronológica
		```
		Aqui concatenamos as últimas falas do usuário e do Brann. Ajuste o formato conforme desejar no prompt (podemos manter colado como diálogo).
		- Otimização: Em vez de concatenar puro, alguns preferem estruturar em JSON para fazer *few-shot*, mas GPT-4 entende linguagem natural bem, então podemos fornecer como um script de conversa.
- **Tratar histórico vazio:** Se for a primeira interação do usuário, a query retornará vazio. Garanta que seu nó seguinte saiba lidar – por exemplo, se nenhum histórico, defina `history = ""` (string vazia). O prompt então será apenas a mensagem atual.

> **Nota:** Há também a possibilidade de usar *Postgres Chat Memory* node, se disponível, que abstrai parte disso. Mas a forma manual acima é transparente e flexível. O importante é que mantenhamos uma **memória longa** para o GPT. A Supabase é escalável para isso – exemplos de integrações similares comprovam sua utilidade em chatbots com contexto [n8n.io](https://n8n.io/integrations/postgres-chat-memory/#:~:text=Telegram%2C%20Google%20Gemini%20AI%2C%20and,Chat%20with%20Internal%20Documents%20using) [n8n.io](https://n8n.io/integrations/postgres-chat-memory/#:~:text=WhatsApp%20Create%20a%20WhatsApp%20Customer,WhatsApp%2083%20Automated%20US%20Stock).

## 5\. Nó OpenAI (GPT-4) – Resposta da IA com Contexto

**Nó:** *OpenAI* (ou *AI* generic) – Chamada do modelo GPT-4.

Este é o coração do agente Brann. Configuração:

- **Credencial OpenAI:** selecione aquela configurada com sua API Key (já deve estar definida via var ambiente).
- **Resource:** *Chat* (conversational).
- **Model:** escolha GPT-4 (por exemplo, `gpt-4` ou uma versão específica disponível).
- **Prompt/Messages:** Monte as mensagens para envio. Como usaremos histórico, devemos preencher:
	- Uma mensagem de sistema (opcional mas recomendado) definindo o papel do assistente. Por exemplo: *"Você é Brann, um assistente virtual de atendimento via WhatsApp, educado e prestativo. Responda de forma humanizada, em português, mantendo um tom profissional e empático. Utilize frases curtas e objetivas. Caso não saiba a resposta, ofereça ajuda alternativa."*
		- Em seguida, insira as mensagens do histórico de forma alternada usuário/assistente. Se você formatou o histórico como texto contínuo no passo anterior, pode inserir tudo isso como uma única mensagem de sistema também ("contexto da conversa até agora:..."). Contudo, o ideal é usar o campo próprio:
		- **Add variable**: O node OpenAI do n8n permite referenciar data. Você pode fornecer a lista de mensagens como variável. Porém, mais simples: Preencha manualmente no JSON:
			```markdown
			[
			  {{#if $json["history"]}}
			    {{ $json["history"] }},
			  {{/if}}
			  {"role": "user", "content": "{{$json["userMessage"]}}"}
			]
			```
			*Obs:* A sintaxe exata depende de como o node espera input. Alternativamente, use a interface do node: adicione várias mensagens e em cada conteúdo use expressões do tipo `{{$node["Supabase"].json["content"]}}`. Isso pode ficar complexo.  
			Uma abordagem prática: Combine tudo em uma única string e mande como system, mas marcando falas. Exemplo:
			```markdown
			system: "Contexto:\n{{ $json["history"] }}\nInstrução: Responda adequadamente."
			user: "{{ $json["userMessage"] }}"
			```
			O GPT-4 então recebe o contexto e a pergunta atual.
- **Temperature e Max Tokens:** Ajuste conforme desejado. Para atendimento, talvez manter temperatura moderada (~0.7) para respostas criativas mas controladas. Max tokens pode ser algo como 1000 para evitar cortar respostas (depende do caso; aqui como MVP e sem interface de texto, 1000 tokens é suficiente para uma resposta bem longa em PT).
- **Funções (se aplicável):** GPT-4 API suporta *functions*, mas não precisamos aqui, a não ser que quiséssemos acionar ações. No MVP, ignoramos.

Ao executar, este nó enviará o prompt com o histórico + mensagem atual e receberá a resposta do GPT-4. O resultado normalmente vem em `item.json.choices[0].message.content` (o texto da resposta). O node pode já simplificar isso para um campo como `completion` dependendo da versão do n8n.

Vamos supor que temos o texto final da resposta em um campo `assistantReply`.

**Salvar memória:** Muito importante – antes de prosseguir para TTS, devemos registrar essa interação no Supabase:

- Use um nó **Supabase (Insert)** ou **Postgres** para inserir duas linhas:
	1. Uma para a mensagem do usuário (`role='user', content=userMessage, user_id=...`).
		2. Outra para a resposta do bot (`role='assistant', content=assistantReply, user_id=...`).
	Isso garante que no próximo turno, a conversa atual também será considerada. Essa inserção pode ser feita em paralelo com o envio da resposta para não acrescentar latência (veremos otimizações).

Com a resposta gerada e armazenada, estamos prontos para a etapa final: entregar ao usuário.

## 6\. Subfluxo de Áudio (TTS Kokoro + Fallback)

**Nó:** *Execute Workflow* (Subworkflow) – *Gerar Áudio da Resposta*

Vamos tratar a conversão de texto -> fala em um subworkflow separado, tanto por organização quanto para permitir execução paralela se desejarmos. Nomeie o subworkflow como "Brann\_TTS\_Subflow".

### Subfluxo "Brann\_TTS\_Subflow"

**Entrada:** Espera-se receber o texto da resposta (`assistantReply`) e talvez parâmetros como idioma ou voz. No nosso caso, voz padrão feminina PT.

Dentro do subfluxo, crie os seguintes nós:

1. **HTTP Request (Kokoro TTS):** Faz uma requisição POST para o endpoint do Kokoro para gerar áudio:
	- **URL:** `{{$env.KOKORO_BASE_URL}}/audio/generate` (supondo que o Kokoro imita a rota OpenAI. Verifique a documentação exata do endpoint - por exemplo, pode ser `/v1/audio/generations`).
		- **Headers:** Se Kokoro exige algum header (talvez não, se é local sem auth; se fosse openAI seria o Bearer token).
		- **Body:** JSON contendo pelo menos o texto. Possivelmente modelo e voz. Exemplo hipotético:
		```markdown
		{
		  "model": "tts-1", 
		  "input": "{{ $json["assistantReply"] }}",
		  "voice": "af_sky" 
		}
		```
		Onde `"voice": "af_sky"` é o código de uma voz (Afrikaans female, mas no doc essa era default e chamada *sky* – você escolheria uma voz PT se disponível). **Kokoro TTS** por padrão vem treinado em inglês, mas suporta outros idiomas; para PT-BR pode-se usar a voz padrão que tende a ler com sotaque leve. Ajuste conforme as opções de voz disponíveis [voice-mode.readthedocs.io](https://voice-mode.readthedocs.io/en/latest/kokoro/#:~:text=Available%20Voices%C2%B6).
		- **Response:** Queremos o arquivo de áudio. O Kokoro (sendo compatível com OpenAI TTS) provavelmente retorna o áudio binário diretamente (Content-Type audio/mpeg) ou um base64. Para garantir:
		- Habilite **Download Binary Data** = true no nó HTTP, e marque *Ignore Response Code* se necessário (às vezes ferramentas retornam 200 OK com arquivo).
				- Defina um nome de arquivo, ex.: `response.mp3`.
		- **Timeout:** Áudio TTS pode levar 1-3 segundos para gerar [voice-mode.readthedocs.io](https://voice-mode.readthedocs.io/en/latest/kokoro/#:~:text=Kokoro%20runs%20locally%20on%20your,3%20seconds%20for%20short%20phrases). Ajuste o timeout do node HTTP para talvez 30 segundos para segurança.
2. **Verificação de Falha:** Temos duas possibilidades após a requisição:
	- Sucesso: item.binary.data contendo o MP3/ WAV gerado.
		- Falha: o HTTP node retornou erro (o subworkflow pode encerrar se não tratar) ou retornou um JSON de erro.  
		Para capturar isso dentro do subworkflow, podemos marcar "Continue on Fail" no HTTP node. Assim, mesmo se falhar, o fluxo continua e podemos checar o código de status:
		- Use um **IF** node para checar `status` ou presença de erro na saída HTTP. Ex: *Condition:* `{{$json["status"]}} != 200` ou `contains($json["error"], "AxiosError")` caso a resposta de erro seja nesse formato [community.n8n.io](https://community.n8n.io/t/send-whatsapp-audio-by-evolution-in-n8n/127817#:~:text=,).
		- Se houve falha, defina um caminho que prepara o fallback:
		- Use um nó **Set** para marcar `fallback = true` e carregar o texto de resposta original (`assistantReply`) para ser usado como texto final.
		- Se sucesso, defina `fallback = false` (pode nem precisar explicitar) e passe adiante o binário.
3. **Saída do Subfluxo:** Ajuste o node *Return* do sub-workflow para devolver tanto o binário do áudio quanto um indicador de fallback. Por exemplo, se sucesso:
	- `binary.data` (o áudio)
		- `json.fallback = false`  
		Se falhou:
		- `json.fallback = true`
		- `json.text = assistantReply` (para saber o texto a enviar em vez do áudio)

No **Executar Workflow** node (no fluxo principal) que chama este subfluxo, mapeie a variável `assistantReply` como input. Configure para **esperar conclusão** (não simultâneo, a não ser que use paralelismo avançado).

> **Dica:** Poderíamos disparar o TTS em paralelo ao envio do texto como fallback, mas como vamos escolher um ou outro, mantemos sequencial – porém otimizações são possíveis (ver seção 8).

De volta ao fluxo principal, após executar o subworkflow, teremos ou um binário de áudio pronto, ou um sinal de fallback.

## 7\. Envio da Resposta ao Usuário (HTTP para Evolution API)

Por fim, enviamos a resposta pelo canal WhatsApp usando as chamadas da Evolution API adequadas:

Vamos usar dois nós HTTP separados: um para texto e outro para áudio, com controle de execução baseado no resultado anterior (fallback ou não).

**Para mensagem de texto:**

- **HTTP Request – Send Text:** Configuração:
	- URL: `{{$env.EVOLUTION_URL}}/message/sendText/{{$env.EVOLUTION_INSTANCE}}`
		- Method: POST
		- Headers: `Content-Type: application/json`, `apikey: {{$env.EVOLUTION_APIKEY}}`
		- Body:
		```markdown
		{
		  "number": "{{ $json["userNumber"] }}",
		  "text": "{{ $json["assistantReply"] }}",
		  "delay": 1000,
		  "presence": "composing"
		}
		```
		Explicando:
		- `"number"`: o telefone do destinatário em formato internacional (código do país + número). **Importante:** incluir código do país (ex: 55 para Brasil) [community.n8n.io](https://community.n8n.io/t/send-whatsapp-message-evolution-api-v2/92235#:~:text=I%E2%80%99ve%20also%20noticed%20your%20number,in%20front%20of%20the%20number). O nosso `userNumber` já deve estar nesse formato sem o `@c.us`.
				- `"text"`: o conteúdo da resposta em texto. (Estamos usando a variável do assistantReply.)
				- `"delay"`: um delay de X ms antes de enviar. Colocamos 1000 (1s) para simular tempo de digitação.
				- `"presence"`: define o status de presença no WhatsApp. `"composing"` faz aparecer *"Brann está digitando..."* para o usuário [community.n8n.io](https://community.n8n.io/t/send-whatsapp-audio-by-evolution-in-n8n/127817#:~:text=%E2%80%9Coptions%E2%80%9D%3A%20,%E2%80%99). Isso combinado com o delay dá uma sensação humanizada.
		Esses campos seguem o formato esperado pelo Evolution API v2 [community.n8n.io](https://community.n8n.io/t/send-whatsapp-message-evolution-api-v2/92235#:~:text=Try%20using%20,the%20parameters%20of%20this%20endpoint). No forum, por exemplo, recomendam usar `"text"` simples em vez de estruturas aninhadas [community.n8n.io](https://community.n8n.io/t/send-whatsapp-message-evolution-api-v2/92235#:~:text=Try%20using%20,the%20parameters%20of%20this%20endpoint), exatamente como acima.
		- Este nó deve **executar somente se** o fallback de texto for necessário. Podemos conseguir isso conectando condicionalmente:
		- Se **subfluxo TTS** retornou `fallback = true`, direcionamos para este nó de texto.
				- Ou usar um **IF** no fluxo principal: condição `{{$node["Brann_TTS_Subflow"].json["fallback"]}} == true` conectando ao HTTP de texto.
				- Em alternativa, podemos usar a saída de erro do subfluxo (mas já tratamos internamente, então IF é claro).

**Para mensagem de áudio:**

- **HTTP Request – Send Audio:** Configuração:
	- URL: `{{$env.EVOLUTION_URL}}/message/sendWhatsAppAudio/{{$env.EVOLUTION_INSTANCE}}`
		- Method: POST
		- Headers: mesmo esquema (Content-Type JSON, apikey).
		- Body:
		```markdown
		{
		  "number": "{{ $json["userNumber"] }}",
		  "audio": "{{ $json["audioBase64"] }}",
		  "options": {
		     "delay": 1000,
		     "presence": "recording"
		  }
		}
		```
		Explicando:
		- `"audio"`: aqui deve ser o áudio em base64. Precisamos pegar o binário gerado pelo subfluxo TTS e codificar. Use novamente um **Move Binary Data** antes deste HTTP:
			- Input: pegue o binário `data` do subfluxo e **Convert to**: texto (base64). Coloque no campo JSON `audioBase64`.
				- Passe `audioBase64` então no JSON do HTTP (como acima).
				- `"options"`: muitos endpoints usam esse campo para coisas extras. O doc do *sendWhatsAppAudio* não deixou explícito se aceita *presence* assim, mas vimos em exemplos do fórum: usar *presence: "recording"* simula *"gravando áudio..."* e o *delay* antes de enviar [community.n8n.io](https://community.n8n.io/t/send-whatsapp-audio-by-evolution-in-n8n/127817#:~:text=%E2%80%9Coptions%E2%80%9D%3A%20,%E2%80%99). Adicione também se disponível `"encoding": true` (em alguns casos, indica que o base64 já está codificado). Em todo caso, configuramos similar ao exemplo oficial [community.n8n.io](https://community.n8n.io/t/send-whatsapp-audio-by-evolution-in-n8n/127817#:~:text=According%20to%20the%20official%20Evolution,the%20correct%20POST%20format%20is).
		- **Observação:** A documentação do Evolution API mostra que o campo esperado é `"audio": "<string>"` onde esse string pode ser uma URL ou base64 do áudio [doc.evolution-api.com](https://doc.evolution-api.com/v2/api-reference/message-controller/send-audio#:~:text=number). Estamos fornecendo base64 diretamente (prefixos data URI não são necessários). Certifique-se de remover qualquer prefixo tipo `data:audio/mp3;base64,` caso o n8n inclua – idealmente o Move Binary Data fornece limpo. Caso tenha problemas de *Bad Request*, verifique se não há aspas a mais ou se o JSON está mal formadado [community.n8n.io](https://community.n8n.io/t/send-whatsapp-audio-by-evolution-in-n8n/127817#:~:text=Among%20several%20issues%20trying%20to,like%20the%20one%20I%20mentioned).
		- Esse nó deve ser executado quando **fallback = false** (ou seja, áudio gerado com sucesso). Use um IF inverso ou simplesmente ligue a saída sucesso do subfluxo TTS -> Move Binary -> HTTP Audio.

**Envio paralelo (opcional):** Por simplicidade, estamos ativando apenas um dos nós de envio conforme o caso. O outro fica inativo. Poderíamos, no design, sempre enviar texto *e* áudio para garantir entrega, mas o usuário receberia duplicado em dois formatos – não é desejável a menos que intencional. Então, mantemos mutuamente exclusivo:

- Se áudio ok, envia áudio.
- Se áudio falhou ou está desativado, envia texto.

Ambos os nós devem retornar status 200 e um JSON de confirmação contendo `messageId` etc., que podemos ignorar.

Assim, a mensagem chega ao WhatsApp do cliente. Por exemplo, se foi áudio, chegará como mensagem de voz (PTT) com duração e tudo. Se foi texto, como chat normal.

## 8\. Boas Práticas Adicionais e Otimizações

Com o fluxo básico funcional, podemos incorporar várias melhorias sugeridas por experiências da comunidade n8n e blogs para tornar o agente mais robusto, performático e fácil de manter:

- **Execução Paralela de Tarefas Independentes:** Para reduzir o tempo de resposta total, identifique etapas que podem ocorrer em paralelo. Por exemplo, enquanto o Whisper transcreve um áudio do usuário, poderíamos simultaneamente consultar o Supabase pelo histórico ou pré-carregar alguma informação. O n8n suporta um modelo de *fan-out/fan-in* (disparar subworkflows em paralelo e depois juntar resultados) [n8n.io](https://n8n.io/workflows/6247-optimize-speed-critical-workflows-using-parallel-processing-fan-outfan-in/#:~:text=When%20should%20you%20use%20this%3F,for%20them%20all%20to%20finish). No contexto do Brann, poderíamos:
	- Iniciar a busca no Supabase **em paralelo** ao processamento de mídia. Como a transcrição e OCR podem ser demorados (~segundos), já ganharíamos tempo obtendo o histórico.
		- Para isso, podemos usar um nó **Split In Batches** ou simplesmente ligar o nó Supabase diretamente após o Switch *antes* dos nós de processamento de mídia, fazendo com que ambos executem em paralelo (n8n executa ramos paralelos simultaneamente por padrão quando possível).
		- Após ambos terminarem, usar um nó **Merge** (modo *Wait All*) para reunir os dados e então formar o prompt do GPT. Esse padrão de *Parallel processing* é demonstrado em tutoriais do n8n, aumentando velocidade quando há múltiplas tarefas independentes [n8n.io](https://n8n.io/workflows/6247-optimize-speed-critical-workflows-using-parallel-processing-fan-outfan-in/#:~:text=This%20template%20is%20a%20hands,In%20model) [n8n.io](https://n8n.io/workflows/6247-optimize-speed-critical-workflows-using-parallel-processing-fan-outfan-in/#:~:text=1.%20Fan,from%20all%20the%20parallel%20tasks).
- **Fallbacks e Tratamento de Erros:** Já implementamos fallback para TTS. Podemos expandir isso:
	- Se a chamada ao GPT-4 falhar (tempo excedido ou erro de API), podemos automaticamente tentar novamente ou usar um modelo alternativo (ex.: GPT-3.5) para não deixar o usuário sem resposta. Isso exigiria um bloco do tipo *IF error -> OpenAI (GPT-3.5)*.
		- Configurar fluxos de erro globais: n8n permite um **Error Trigger** workflow que executa quando qualquer outro workflow falha. Configure um desses para logar exceções (por exemplo, enviar um alerta no Slack/Email ao admin contendo o erro e dados da execução). Assim, você fica sabendo de problemas em tempo real e o sistema ganha robustez.
		- Dentro do fluxo, usamos *Continue On Fail* em pontos estratégicos (ex.: no TTS) para tratar internamente, mas em pontos críticos (ex.: transcrição) preferimos falhar explicitamente e deixar o Error Trigger logar. Decida caso a caso.
- **Função para Normalização (Parser):** Usamos pequenos trechos de JavaScript nos nós Function para normalizar telefone, compor histórico, limpar texto de OCR, etc. Centralize essas lógicas de limpeza em um único lugar quando possível. Por exemplo, poderíamos ter um subworkflow utilitário “ParseIncomingMessage” que recebe o JSON bruto do webhook e devolve o objeto padronizado (`userNumber`, `userMessage`, flags). Isso deixa o fluxo principal mais legível e facilita manutenção. Além disso, se evoluirmos o formato do Evolution API (v3 etc.), só precisaremos atualizar esse parser.
	- A comunidade destaca que muitas vezes após extrair texto de OCR ou transcrição é útil passar por um *Code node* para filtrar dados irrelevantes antes de prosseguir [community.n8n.io](https://community.n8n.io/t/best-way-to-get-ocr-data-in-n8n/158921#:~:text=After%20extracting%20the%20text%20from,don%E2%80%99t%20mind%20spending%20extra%20tokens) – mantivemos essa prática no design.
- **Aguardar de forma inteligente (Wait Node):** Em interações com usuários, pode ser interessante inserir pequenas esperas. Já usamos *delay* para presença no WhatsApp. Poderíamos também:
	- Usar um nó **Wait** antes de enviar resposta para sincronizar paralelos (caso implementados) ou para agendar alguma ação. Por exemplo, se quisermos mandar uma pesquisa de satisfação 5 minutos após resolver o problema do usuário, um Wait node agendado seria útil.
		- No contexto do agente, não queremos esperas desnecessárias que atrasem resposta. Mas um uso "esperto" do Wait é pausar o fluxo principal até todos subtarefas terminarem (similar ao Merge wait). Como citamos, o Merge node ou até mesmo o próprio node GPT pode atuar como ponto de sincronização se receber dados de múltiplos ramos.
- **Uso de *Environment Variables* e Config externamente:** Já adotamos variáveis de ambiente para credenciais. Isso também vale para parâmetros de ajuste fino:
	- Coloque, por exemplo, o nome do modelo GPT como variável (para rapidamente alternar entre `gpt-4` e `gpt-4-32k` se precisar).
		- O flag de áudio `BRANN_TTS_ENABLED` pode ser ligado/desligado sem alterar o fluxo. Um investidor não técnico poderia ter um botão em uma UI para desativar respostas em áudio temporariamente – bastaria mudar a var e reiniciar minimalmente. No nosso fluxo, implementaríamos isso com um simples IF logo após GPT: *Se TTS\_ENABLED == true -> executar subfluxo TTS; senão -> pular para envio texto*. Assim, podemos testar facilmente os dois modos.
- **Logs e Versionamento:** Mantenha um log estruturado das conversas:
	- Além de salvar no Supabase, considere logar eventos importantes em um Google Sheet ou em um arquivo. Por exemplo, cada vez que o usuário envia mídia, logue tipo e tamanho, cada vez que o GPT responde, logue quantos tokens foram usados (a OpenAI API retorna contagem de tokens na resposta).
		- Isso ajuda a monitorar custos e performance ao longo do tempo.
		- Versionamento do fluxo em si: exporte a workflow do n8n (JSON) regularmente e armazene num repositório Git. Pode-se automatizar isso com um fluxo agendado que toda noite use o endpoint da API do n8n para obter as workflows e comitar no GitHub [n8n.io](https://n8n.io/workflows/6544-forward-chatwoot-messages-to-whatsapp-via-evolution-api-with-media-support/#:~:text=,built%20integration). Assim, qualquer mudança fica historicamente registrada. Como melhor prática, antes de grandes mudanças duplique a workflow no n8n (versão v1, v2...) ou use a funcionalidade de versionamento interna se disponível.
- **Segurança e Privacidade:** Como estamos lidando com dados possivelmente sensíveis de clientes:
	- Garanta que a comunicação entre Evolution API e n8n seja segura (HTTPS). Configure um token de verificação no webhook (Evolution API permite enviar um header ou param secreto que você verifica no n8n).
		- Na hora de salvar histórico no Supabase, **anonimize** ou evite guardar dados pessoais irrelevantes. Guarde um user\_id abstrato em vez do telefone bruto, ou hash do número, para proteger privacidade caso necessário.
		- Se for implementar em produção, siga as políticas do WhatsApp Business API para bots (como responder dentro de 24h window, etc., embora usando Baileys isso não se aplica estritamente, convém manter-se dentro das boas práticas para não ser marcado como spam).
- **Testes de Fluxo:** Finalmente, realize um teste completo cobrindo todos os cenários:
	1. **Texto -> Texto:** Envie uma mensagem de texto comum e verifique se o bot responde com texto correto e se a conversa é registrada no Supabase.
		2. **Áudio -> Áudio:** Envie um áudio (voz). O bot deve transcrever corretamente e responder em áudio. Confira se o áudio do Brann contém o conteúdo esperado (use um player). Se o TTS falhar (simule desligando o serviço Kokoro), o bot deve automaticamente voltar a texto.
		3. **Imagem -> Texto:** Envie uma imagem com texto claro (por ex., foto de um cartaz). Veja se extraiu o texto via OCR e se o GPT respondeu algo coerente. Ex.: se o usuário manda foto de um endereço, o bot poderia responder confirmando detalhes.
		4. **Vídeo -> Áudio/Texto:** Envie um pequeno vídeo falando algo. O bot deve transcrever e responder apropriadamente. Depois, teste um vídeo sem áudio (o bot deve informar que não conseguiu extrair info, de modo cortês).
		5. **Volume e Paralelo:** Teste enviar várias mensagens em rápida sucessão para ver se o n8n aguenta e se a memória funciona – por exemplo, mande "Olá", espere resposta, depois imediatamente "Qual era meu nome mesmo?" (se tivesse sido mencionado). O Brann, com memória, deveria lembrar.
	Ao acompanhar esses testes, use o monitor de execuções do n8n e logs do Supabase para inspecionar eventuais erros. Qualquer falha, revise o error output no n8n (que graças ao Error Trigger ou logs adicionados você conseguirá ver rapidamente).

Com todas essas etapas implementadas e testadas, teremos entregue o MVP do Brann: um agente WhatsApp cognitivo, capaz de entender voz, imagens e texto, manter contexto e responder de forma natural. A arquitetura está desenhada de modo que futuras melhorias possam ser incorporadas – por exemplo, adicionar compreensão de intenção, integração com sistemas externos (CRM, base de conhecimento) para respostas mais ricas, ou até suporte a outros canais (o Evolution API já permitiria Instagram/Messenger no futuro).

## Conclusão

Este relatório detalhou a construção de um agente de atendimento automatizado no WhatsApp, usando exclusivamente o n8n como orquestrador. Passamos por cada componente: recepção via Evolution API, processamento multimodal (texto, áudio, imagem, vídeo), inteligência com GPT-4 e memória via Supabase, e resposta via texto ou áudio com TTS. Também foram destacadas melhores práticas de implementação e ideias para otimização inspiradas por casos reais da comunidade n8n (como paralelismo para ganho de velocidade [n8n.io](https://n8n.io/workflows/6247-optimize-speed-critical-workflows-using-parallel-processing-fan-outfan-in/#:~:text=When%20should%20you%20use%20this%3F,for%20them%20all%20to%20finish) e uso de ferramentas de OCR recomendadas [community.n8n.io](https://community.n8n.io/t/best-way-to-get-ocr-data-in-n8n/158921#:~:text=In%20my%20opinion%20Mistral%20AI%E2%80%99s,prem%20instance%20for%20better%20privacy)).

O resultado é um fluxo modular e de fácil replicação, adequado para demonstrar a investidores o potencial da plataforma: o **Brann** consegue atender usuários de forma automatizada e humanizada, 24/7, escalando o suporte sem perder o toque pessoal. Além disso, a solução é *low-code*, construída rapidamente aproveitando integrações existentes – evidenciando agilidade de desenvolvimento e economia de recursos. Com logs centralizados e versionamento, o MVP também prepara terreno para evolução futura, mantendo confiabilidade e auditabilidade desde cedo.

Em suma, entregamos um MVP funcional e bem arquitetado, pronto para impressionar em demos e servir de base para um produto final robusto.

**Referências Técnicas Utilizadas:**

- Configuração do webhook no Evolution API e necessidade de nó Webhook do n8n [community.n8n.io](https://community.n8n.io/t/evolution-api/126278#:~:text=Evolution%20API%20Node%20Role%20The,This%20is%20key).
- Formato de envio de texto pelo Evolution API (uso de `"text"` e número com código país) [community.n8n.io](https://community.n8n.io/t/send-whatsapp-message-evolution-api-v2/92235#:~:text=Try%20using%20,the%20parameters%20of%20this%20endpoint).
- Envio de áudio pelo Evolution API (campo `"audio"` com base64) [doc.evolution-api.com](https://doc.evolution-api.com/v2/api-reference/message-controller/send-audio#:~:text=number) e uso de presença/delay [community.n8n.io](https://community.n8n.io/t/send-whatsapp-audio-by-evolution-in-n8n/127817#:~:text=%E2%80%9Coptions%E2%80%9D%3A%20,%E2%80%99).
- Suporte do OpenAI Whisper a diversos formatos de áudio, incluindo vídeo MP4 [docs.n8n.io](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations/#:~:text=,webm).
- Sugestão de OCR via node comunitário Tesseract e via API Mistral (com melhor acurácia segundo comunidade) [community.n8n.io](https://community.n8n.io/t/best-way-to-get-ocr-data-in-n8n/158921#:~:text=Since%20it%E2%80%99s%20an%20image%20you,tesseractjs) [community.n8n.io](https://community.n8n.io/t/best-way-to-get-ocr-data-in-n8n/158921#:~:text=In%20my%20opinion%20Mistral%20AI%E2%80%99s,prem%20instance%20for%20better%20privacy).
- Padrão de processamento paralelo em n8n para acelerar workflows intensivos [n8n.io](https://n8n.io/workflows/6247-optimize-speed-critical-workflows-using-parallel-processing-fan-outfan-in/#:~:text=When%20should%20you%20use%20this%3F,for%20them%20all%20to%20finish).