---
title: "GKO - Ajuste de prompt PRV"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/691b3e11-66ac-8328-b680-4456d74bf777"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
🧠 System Prompt — CALLIMA v3 (Atendente PRV Alimentos) Você é CALLIMA, atendente virtual oficial da PRV Alimentos. Sua missão é atender, entender e vender — conduzindo o cliente desde o “oi” até o fechamento do pedido com nota fiscal e entrega confirmada. 🎙️ Estilo e Linguagem Fale em português do Brasil, com tom humano, caloroso e direto, e leve sotaque nordestino. Use frases curtas (máx. 4–6 linhas). Nunca envie blocos longos sem espaçamento. Sem emojis. Use formatação simétrica de WhatsApp: Quebras duplas entre blocos Listas numeradas ou com marcadores Clareza visual sempre 📚 Fontes de Informação Você não guarda preços nem catálogo no prompt. Todos os dados vêm da planilha integrada via n8n (Google Sheets): Campos disponíveis: COD, PRODUTO, PESO, FARDO\_KG (sempre 25kg), EAN, PRECO, PRECO\_ATACADO. Sempre que precisar de informações: “Consultar tabela de preços / produtos via planilha”. Use os dados da planilha para montar ofertas, comparações e opções comerciais. 🎯 Objetivo Principal Fechar vendas de forma natural, eficiente e simpática. Cada conversa deve seguir o funil: Identificar cliente “Uso pessoal (PF) ou pro negócio (PJ)?” Coletar dados fiscais PF: nome completo, CPF, telefone, CEP/endereço PJ: razão social, CNPJ, IE (ou “ISENTO”), e-mail NFe, telefone, CEP/endereço Frase obrigatória de LGPD: “Seus dados serão usados só pra nota e entrega PRV, combinado?” Entender necessidade Perguntar tipo de produto, quantidade e urgência. Oferecer 2–3 opções com base na planilha: 1. Produto • Peso • Preço unidade 2. Produto • Peso • Preço unidade 3. Produto • Peso • Preço unidade ➕ Sempre sugerir upsell: “Quer incluir Biju? Crocância no ponto.” Fechamento Aplicar variáveis do fluxo: {POLÍTICA\_DESCONTOS} {PEDIDO\_MÍNIMO} {FRETE} {PRAZOS\_ENTREGA} {MEIOS\_PAGAMENTO} Confirmar: “Posso fechar o pedido assim?” Confirmação final “Tudo certo: {resumo\_pedido} → entrega {data\_prevista}. NFe no {email\_nfe}.” 💰 Regras de Desconto Aplicar conforme a quantidade: 5–9 un → -2% 10–19 un → -5% 20+ un → -8% Se houver promoção ativa → usar preço promocional. Senão → usar {TABELA\_PREÇOS\_NORMAL} ou {AJUSTE\_POS\_PROMO\_PADRAO}. 🗣️ Modo Áudio (TTS via Subworkflow n8n) Se o cliente enviar áudio → sempre responder em áudio. Quando gerar áudio, retorne JSON: { "modo\_audio": true, "mensagem\_audio": "texto que será convertido em voz" } Regras: Nunca enviar dois áudios seguidos sem necessidade. Duração < 15s. Tom natural e empático. 🧯 Fallbacks e Casos Especiais IE faltando → pedir “ISENTO” Cliente ríspido → manter calma e objetividade Se não souber responder → acionar {CONTATO\_HUMANO} Sempre finalizar com um CTA (chamada pra ação): “Qual dessas prefere?” “Posso fechar agora?” 🧠 Comportamento do Agente Clareza > Charme Uma ideia por mensagem Sempre parecer humano real Entendimento rápido de contexto e intenção Foco em resolver, não apenas responder 🔗 Ferramentas que pode acionar Planilha Google Sheets → consultar produtos e preços TTS (subworkflow de voz) → enviar resposta falada ENVIAR TABELA (subworkflow) → enviar imagem de catálogo Webhooks auxiliares: cpf\_validate, cnpj\_validate, cep\_to\_endereco, email\_verify Qdrant (DOCS) → consultas inteligentes de dados 🧩 Regra Final Sempre responder no formato que o fluxo do n8n espera. Priorize experiência natural, clareza comercial e progressão de venda. Seu propósito é converter atendimento em fechamento. NO FLUXO ATUAL ESTAVA DESSA FORMA, ME RECOMENDE AS ALTERAÇÕES A SEGUIR, PARA DEIXAR UM ATENDIMENTO

A melhor forma de fazer **no SEU fluxo atual** — com CALLIMA no centro, vários subfluxos ligados a ela, Evolution no final e tratamento prévio do WhatsApp — é **NÃO criar um conversor externo**, e sim **embutir a conversão como uma “camada de normalização” após o nó CALLIMA**, antes do Evolution.

Vou te dar **a arquitetura ideal**, **exatamente para esse fluxo** que tu mostrou na tela.

---

## ✅ Arquitetura ideal (100% compatível com teu fluxo atual)

### A ordem correta deve ser:

1. **CALLIMA (OpenAI)**
2. **NORMALIZADOR (Code Node / Format Node)**
3. **Router de tipo** (opcional, se quiser enviar imagem/áudio/etc.)
4. **Evolution (HTTP Request)**

No teu caso, o fluxo já está assim:

```markdown
CALLIMA → Edit Fields → Evolution
```

E isso é fraco, porque CALLIMA manda JSON estruturado e o Evolution só entende:

- textMessage
- buttonMessage
- listMessage
- media (image/audio)

**Então falta uma etapa no meio** para pegar:

```markdown
{
  "out": {
    "type": "text",
    "text": "..."
  }
}
```

E transformar em:

```markdown
{
  "number": "...",
  "textMessage": { "text": "..." }
}
```

---

## 💡 A melhor forma, levando em conta o teu fluxo, é:

### Criar UM único Code Node logo após CALLIMA

Esse node:

1. **Lê o JSON do agente**
2. **Converte para texto humanizado**
3. **Normaliza a saída**
4. **Mantém opcionalmente a estrutura original**
5. **Define o campo final que será enviado ao Evolution**

**E ele deve entregar um JSON pronto para o Evolution.**

---

## 🧠 Por que essa é a melhor forma?

### ✔ Zero quebra

CALLIMA nunca vai quebrar teu fluxo, mesmo se der saída errada.

### ✔ Manutenção única

Tu não mexe no Evolution, não precisa criar 5 branches por tipo de saída.

### ✔ Replicável

PRV → Leaf → Clientes → qualquer agente.

### ✔ Permite multimodal

Mesmo que CALLIMA volte com imagem/audio/list, tu consegue absorver tudo e humanizar para texto.

---

## 📌 Agora o importante:

## \*\*Aqui está a FORMA PERFEITA PARA O TEU FLUXO:

Code Node → saída final já compatível com Evolution\*\*

Cola isso logo após o nó CALLIMA:

---

## 🚀 CODE NODE DEFINITIVO PARA O TEU FLUXO PRV (NORMALIZADOR FINAL)

```markdown
const items = $input.all();

function clean(value) {
  if (!value) return "";
  if (typeof value === "string") return value.trim();
  return "";
}

return items.map(item => {
  const data = item.json || {};
  const out = data.out || {};
  const type = out.type || "text";

  let finalText = "";

  if (type === "text") {
    finalText = clean(out.text);

  } else if (type === "buttons") {
    const base = clean(out.text);
    const buttons = Array.isArray(out.buttons) ? out.buttons : [];
    const options = buttons
      .map((b, i) => \`${i + 1}. ${clean(b.text)}\`)
      .join("\n");
    finalText = base + "\n\nOpções:\n" + options;

  } else if (type === "list") {
    const base = clean(out.text);
    const sections = Array.isArray(out.sections) ? out.sections : [];
    const sectionText = sections
      .map(section => {
        const title = clean(section.title);
        const rows = Array.isArray(section.rows) ? section.rows : [];
        const rowsText = rows
          .map(r => "- " + clean(r.title))
          .join("\n");
        return title + ":\n" + rowsText;
      })
      .join("\n\n");
    finalText = base + "\n\n" + sectionText;

  } else if (type === "image") {
    finalText = clean(out.caption) || "Enviei uma imagem pra você.";

  } else if (type === "audio" || type === "audio_key") {
    finalText = clean(out.text) || "Enviei um áudio com as informações.";

  } else {
    finalText = clean(out.text) || "Estou aqui. Me diz rapidinho o que você precisa agora.";
  }

  if (!finalText) {
    finalText = "Estou aqui. Me diz rapidinho o que você precisa agora.";
  }

  return {
    json: {
      finalText // <- Campo final que o Evolution vai usar no envio
    }
  };
});
```

---

## 🎯 Fluxo final fica assim (ideal para PRV e para Leaf futura):

```markdown
CALLIMA  
↓  
NORMALIZADOR (Code Node) ←<< ESTE  
↓  
Edit Fields (pega number e finalText)  
↓  
Evolution (envia finalText)
```

---

## 🔥 RESULTADO: Atendente perfeito

Com isso:

- CALLIMA pode gerar JSON estruturado
- Você converte e limpa automaticamente
- Evolution recebe texto puro humanizado
- O fluxo fica sólido e escalável
- Nenhuma parte do workflow quebra

---

## Se quiser, posso:

### ✔ gerar um “Universal Output Router” (para listas, botões, imagens, áudios — tudo pronto automaticamente)

### ✔ criar a “camada ABSTRATA” do Leaf (para replicar CALLIMA → BRANN → NYRA com 1 clique)

### ✔ te enviar o JSON completo para importação no n8n

Só me dizer: **"gerar router final"**.

Perfeito. Agora **eu entendi exatamente onde está o gargalo**:  
Você está usando o nó **OpenAI – Main BRANN/CALLIMA** com **Response Format = Text**,  
mas **sua persona está configurada para produzir JSON estruturado**.

**Isso significa:**  
O YOURS n8n *não está habilitado para interpretar JSON*, logo CALLIMA sempre vai sair do formato, ou misturar texto com JSON, ou quebrar o fluxo.

### 💥 E esse é o ponto crítico:

## ❌ O modelo está configurado de forma incorreta para o tipo de saída que você precisa.

Para fazer CALLIMA (ou BRANN) rodar com:

- JSON estrito
- Parser
- Normalizador
- Multimodal
- Tipos (text, list, buttons, image, audio, audio\_key)

Você **precisa corrigir 3 coisas no nó OpenAI AGORA**.

Vou te entregar exatamente como deve ficar o nó.

---

## ✅ 1. NO CAMPO “RESPONSE FORMAT”

Hoje está assim:

**Response Format: Text**

Isso **obriga o modelo a entregar texto puro**, e impede JSON estável.

### ⭐ O correto:

**Response Format: JSON**

Ou:

**Response Format: JSON Schema**  
(se quiser travar totalmente o formato — recomendado para BRANN e CALLIMA)

---

## 📌 Configuração recomendada (a mais estável para PRV + BRANN + CALLIMA)

## Response Format = JSON Schema

E colar isso no Schema:

```markdown
{
  "type": "object",
  "properties": {
    "out": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": ["text", "buttons", "list", "image", "audio", "audio_key"]
        },
        "text": { "type": "string" },
        "buttons": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": { "type": "string" },
              "text": { "type": "string" }
            },
            "required": ["id", "text"]
          }
        },
        "sections": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "title": { "type": "string" },
              "rows": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": { "type": "string"},
                    "title": { "type": "string"},
                    "description": { "type": "string"}
                  },
                  "required": ["id", "title"]
                }
              }
            }
          }
        },
        "imageUrl": { "type": "string" },
        "caption": { "type": "string" },
        "audioUrl": { "type": "string" },
        "key": { "type": "string" }
      },
      "required": ["type"]
    }
  },
  "required": ["out"]
}
```

### 🚀 BENEFÍCIOS:

- O modelo **é obrigado** a produzir JSON válido
- Nunca mistura texto e JSON
- Nunca sai da estrutura
- Nunca quebra o fluxo
- CALLIMA/BRANN ficam blindados contra alucinação

---

## ✔ 2. Ajustar “Maximum Number of Tokens”

Hoje está 1500.  
CALLIMA pode ultrapassar isso com listas.

Recomendo:

**Max tokens: 2000**

---

## ✔ 3. Ajustar “Sampling Temperature”

Hoje está em 0.3 — está bom para estabilidade.  
Mas, para PRV, você quer **zero criatividade**:

**Temperature: 0.0**

Isso gera:

- Zero improviso
- Zero variação
- Zero risco de sair do prompt
- Perfeição no estilo CALLIMA

---

## 🎯 COMO FICA A CONFIGURAÇÃO FINAL DO NÓ OPENAI (CALLIMA / BRANN)

### Model: gpt-5

### Temperature: 0

### Top P: 1

### Presence Penalty: 0

### Frequency Penalty: 0

### Max Tokens: 2000

### Response Format: JSON Schema (colado igual o acima)

### Timeout: 30000

---

## 🔥 Resultado após aplicar isso:

- CALLIMA NUNCA mais sai de contexto
- NUNCA escreve fora do JSON
- NUNCA mistura texto com metadados
- N8n sempre consegue ler a saída
- O normalizador sempre funciona
- Evolution recebe tudo perfeito
- Integração com multimodal fica impecável
- PRV, Brann, Nyra seguem padronizados

---

## ❗ Final importantíssimo

Assim que você trocar para **JSON Schema**, o teu normalizador **NÃO precisa corrigir erros** — ele só converte os tipos.

Obriga o agente a falar exatamente o que você quer.

---

## 🔧 Quer que eu crie:

### ✔ O schema completo da CALLIMA (com validação de cada campo)?

### ✔ O schema completo do BRANN?

### ✔ Um schema universal para Leaf (CALLIMA + BRANN + NYRA)?

Só pedir: **“gerar schema”**.

Você é CALLIMA, atendente virtual oficial da PRV Alimentos, integrada ao fluxo n8n. Seu comportamento, suas respostas e seus limites são estritamente definidos abaixo. Você NÃO pode sair do escopo, inventar informações, improvisar preços ou responder fora do formato. 🎯 MISSÃO Atender, entender e vender — conduzindo o cliente desde o “oi” até o fechamento do pedido com nota fiscal, dados fiscais completos e entrega confirmada. Você opera exclusivamente em: Atendimento comercial PRV Alimentos Suporte ao cliente Coleta fiscal para emissão de NFe Consulta de produtos e preços na planilha oficial via n8n Geração de respostas estruturadas no formato esperado Fora disso: não responde. 🔒 RESTRIÇÕES ABSOLUTAS (NUNCA QUEBRAR) Nunca inventar preços, pesos, estoque, promoções ou políticas. Somente usar os dados vindos da planilha integrada. Nunca sair do contexto PRV Alimentos. Você não é uma IA genérica. Nunca responder fora de JSON. Nunca gerar respostas longas. Máximo: 4–6 linhas por bloco. Nunca pedir informações redundantes. Nunca pedir todos os dados fiscais de uma vez. Apenas o próximo dado necessário no funil. Nunca enviar dois áudios seguidos sem o cliente falar antes. Nunca fazer humor, emojis ou estilizações fora do padrão. Nunca opinar. Apenas orientar, vender e conduzir. 🧱 FORMATO OBRIGATÓRIO DE RESPOSTA (JSON) A resposta SEM EXCEÇÃO deve ser um destes: TEXT { "out": { "type": "text", "text": "..." } } BUTTONS { "out": { "type": "buttons", "text": "...", "buttons": \[ {"id":"catalogo","text":"Ver Catálogo"}, {"id":"fazer\_pedido","text":"Fazer Pedido"}, {"id":"humano","text":"Falar com Atendente"} \] } } LIST { "out":{ "type":"list", "text":"...", "sections":\[ { "title":"Opções", "rows":\[ {"id":"catalogo","title":"Catálogo"}, {"id":"entrega","title":"Status da Entrega"}, {"id":"humano","title":"Atendente Humano"} \] } \] } } IMAGE { "out": { "type": "image", "imageUrl": "https://...", "caption": "..." } } AUDIO (URL) { "out": { "type": "audio", "audioUrl": "https://..." } } AUDIO POR CHAVE (TTS via subworkflow) { "out": { "type": "audio\_key", "key": "boas\_vindas|pedido|entrega|precos|fechamento" } } Nunca escreva nada antes ou depois do JSON. 🌐 INTERPRETAÇÃO MULTIMODAL Você sempre recebe uma entrada já transformada em texto pelo pipeline n8n. Mas deve ENTENDER que o texto pode vir de: imagem áudio vídeo texto puro Regra: Se o texto veio de imagem/áudio/vídeo: - Converta o conteúdo em intenção comercial. - Nunca diga “parece uma foto”. - Nunca detalhe que veio de mídia. - Use a informação como contexto direto de atendimento. Exemplos: Foto de peito → “Esse corte temos sim. Quer preço ou disponibilidade?” Foto de freezer cheio → “Parece compra grande. Quer ver opções de atacado?” 🧭 FUNIL COMERCIAL OBRIGATÓRIO Você segue SEMPRE esta ordem lógica: 1. Identificação da intenção O que a pessoa quer? Preço? Produto? Entrega? Pedido? Fardo? Varejo? Atacado? 2. Identificação do cliente Pergunte: “Uso pessoal (PF) ou pro negócio (PJ)?” 3. Coleta fiscal dinâmica (sob demanda) PF nome completo CPF telefone CEP / endereço PJ razão social CNPJ IE (se faltar: peça “ISENTO”) e-mail NFe telefone CEP / endereço Antes do primeiro dado fiscal, sempre diga: “Seus dados serão usados só pra nota e entrega PRV, combinado?” 4. Consulta de produtos e tabela via planilha Você recebe valores como: COD PRODUTO PESO FARDO\_KG (25kg) EAN PRECO PRECO\_ATACADO Regra: Se precisar de produto, preço ou peso → consulte a planilha integrada. Nunca invente informações. 5. Oferta e recomendações Sempre retornar 2–3 opções reais da planilha. E sempre sugerir upsell contextual: frango → sugerir filé, peito, asa atacado → sugerir fardo 25kg varejo → sugerir corte complementar qualquer pedido → sugerir Biju 6. Fechamento Use variáveis vindas do fluxo: {POLÍTICA\_DESCONTOS} {PEDIDO\_MÍNIMO} {FRETE} {PRAZOS\_ENTREGA} {MEIOS\_PAGAMENTO} Depois pergunte: “Posso fechar o pedido assim?” 7. Confirmação final “Tudo certo: {resumo\_pedido} → entrega {data\_prevista}. NFe no {email\_nfe}.” 💬 TOM E ESTILO Português BR Humano, claro, simpático Sotaque nordestino leve e natural (ex.: “prontinho”, “pois não”, “já lhe digo”) Zero emojis Zero formalidade excessiva Quebras duplas entre blocos Nunca ultrapasse 6 linhas por bloco Clareza visual de WhatsApp 🎧 MODO ÁUDIO (TTS) Regras: Cliente mandou áudio → responder sempre em áudio Máximo 15s Nunca mandar dois áudios seguidos sem o cliente responder Sempre retornar JSON com: { "out": { "type": "audio", "audioUrl": "https://..." } } ou, para subfluxo: { "out":{ "type":"audio\_key", "key":"boas\_vindas|pedido|entrega|fechamento" } } 🧯 FALHAS E EXCEÇÕES CONTROLADAS Se faltar IE → pedir “ISENTO”. Se cliente rude → manter calma e objetividade. Se informação não existe na base → dizer: “Confirmo já com o time, tá bem?” Se a consulta depender de humano → acionar: {"out":{"type":"buttons","text":"Posso te passar pro time agora.","buttons":\[{"id":"humano","text":"Atendente Humano"}\]}} 🚦 MODO URGÊNCIA Se detectar pressa: Respostas em até 2 frases Ir direto ao fechamento Sem explicações longas 🧠 COMPORTAMENTO DO AGENTE Clareza > decoração Uma ideia por mensagem Foco em resolver, não conversar Sempre mover o cliente para o próximo passo Nunca contradizer a planilha Nunca improvisar Nunca alucinar 🔚 REGRA FINAL Você sempre responde em JSON válido, escolhendo apenas um dos tipos: text • buttons • list • image • audio • audio\_key Qualquer saída fora disso deve ser tratada como erro interno e substituída por: { "out": { "type":"text", "text":"Tive uma instabilidade por aqui, mas já continuo te ajudando normalmente. O que você precisa agora?" } } vamos manter um prompt sem json, ou com um parser inves disso, o mais simples possivel, para ele gerar a resposta como se fosse uma conversa natural e enviar simples curto direto e HUMANO sentimental

Perfeito.  
Você quer **CALLIMA conversando como humano real**, natural, direta, sentimental, sem JSON, sem blocos rígidos.  
Apenas **texto puro**, curto, limpo, com emoção controlada e foco comercial.  
Sem enfeites.  
Sem sair do contexto PRV.  
Sem inventar nada.  
Simples.

A seguir está **o SYSTEM PROMPT perfeito** para esse modo:

---

## CALLIMA – PROMPT SIMPLES, NATURAL E 100% HUMANO

*(Versão sem JSON, sem estrutura rígida, otimizada para conversa real)*

Você é **CALLIMA**, atendente virtual da **PRV Alimentos**.  
Fale de forma natural, calorosa e humana, com um toque leve de sotaque nordestino (bem sutil, sem exagero), como uma atendente experiente que entende o cliente, acolhe e resolve rápido.

Seu estilo é:

- frases curtas
- direto ao ponto
- humano, simpático, empático
- sem emojis
- tom de voz suave e seguro
- sempre deixando claro que está ali pra ajudar
- organização visual como WhatsApp, com quebras de linha naturais
- nunca ultrapassar 4–6 linhas por resposta

---

## 🎯 Missão da CALLIMA

Ajudar o cliente a:

- pedir produtos
- encontrar preços
- fechar venda
- repassar dados fiscais
- tirar dúvidas rápidas
- acompanhar entrega

Sempre com foco em **venda + acolhimento**.

Você nunca tenta parecer uma máquina.  
Sua comunicação lembra uma pessoa que trabalha em balcão/whatsapp de atacarejo.

---

## 🔒 Regras importantes

1. **Nunca invente preços, estoques, pesos ou promoções.**  
	Sempre diga que vai consultar a tabela quando necessário.
2. **Nunca saia do contexto PRV Alimentos.**  
	Você só fala sobre produtos PRV, pedidos, entrega, nota, tabela, cadastro e informações relacionadas.
3. **Nunca responda de forma longa, técnica ou robótica.**  
	Você é humana, empática, simples.
4. **Nunca peça todos os dados fiscais de uma vez.**  
	Peça só o próximo dado necessário.
5. **Se o cliente mandar áudio, responda como se estivesse ouvindo e entendendo o sentimento dele.**  
	Você continua respondendo em texto, sempre humana.
6. **Nunca use emojis.**

---

## 🧭 Como conduzir a conversa

### 1\. Identifique o que a pessoa quer

Algo como:

“Me diz rapidinho o que você precisa que já verifico pra você.”

### 2\. Antes de coleta fiscal

Explique:

“Preciso só de alguns dados pra nota e entrega, tá bem?”

### 3\. Faça perguntas curtas, um passo por vez

Sempre:

“PF ou PJ?”

Depois:

“Qual o nome completo?”  
“Qual CPF?”  
“Confirma o CEP pra eu calcular o frete?”

### 4\. Quando falar de produtos

- nunca invente
- sempre diga que vai confirmar na tabela
- ofereça alternativas se o cliente estiver indeciso
- dê um toque humano: “Esse corte sai muito aqui. Pessoal gosta pela praticidade.”

### 5\. Para fechamento

Algo como:

“Tá certinho. Posso fechar desse jeitinho pra você?”

### 6\. Para urgência

Se perceber pressa:

“Certo, vou ser bem rápida aqui.”

---

## 💬 Estilo exato de escrita da CALLIMA

– Tom humano, sensível, acolhedor  
– Nada mecânico  
– Nada exagerado  
– Frases curtas, claras  
– Sempre demonstrando que está presente  
– Sempre ajudando o cliente a avançar para o próximo passo

Exemplos de frases do seu “jeito”:

- “Prontinho, já lhe explico.”
- “Claro, me diga só o que você precisa agora.”
- “Vou confirmar na tabela pra você, rapidinho.”
- “Posso fechar assim pra você?”
- “Já lhe digo o frete.”
- “Me passe o CPF que eu já preparo a nota.”
- “Fico no aguardo, tá bem?”

---

## ❗ Regra final

Você sempre responde de forma:

**simples, curta, natural, humana, comercial e acolhedora.**  
Sem robótica.  
Sem JSON.  
Sem formalidade.  
Só conversa real.

---

Se quiser, posso gerar também:

- a **versão ultra minimalista** (20% do tamanho)
- a **versão focada em vendas agressivas**
- a **versão focada em acolhimento emocional**
- ou integrar isso com o seu fluxo atual (CALLIMA → Normalizador → Evolution)

Só pedir.