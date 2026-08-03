---
title: "GKO - Corrigir quebra de mensagem"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/690a43b9-0850-8327-95f2-5aa7722b2a50"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
ter., 4 de nov. às 15:20

e como garante que o if manda para o loop?

ter., 4 de nov. às 17:37

assim?

ter., 4 de nov. às 23:30

?

Sim. Duas formas simples:

## A) Pelo tamanho

Defina um limite baixo para “forçar” 3 partes. Ex.: `MAX=80`.  
No **Code** deixe só:

```markdown
const text = ($json.reply ?? $json.text ?? '').toString();
const phone = $json.phone, instance = $json.instance;
const MAX = 80; // ajuste fino pra gerar ~3 pedaços nesse tipo de frase
const SEP = /(?<=\.|\?|!|\n)/;

function splitSmart(t, max){
  const parts = t.split(SEP).map(s=>s.trim()).filter(Boolean);
  const out=[]; let buf='';
  for (const p of parts){
    if ((buf+' '+p).trim().length<=max) buf=(buf?buf+' ':'')+p;
    else { if (buf) out.push(buf);
      if (p.length<=max) out.push(p);
      else for(let i=0;i<p.length;i+=max) out.push(p.slice(i,i+max));
      buf='';
    }
  }
  if (buf) out.push(buf);
  return out;
}

const chunks = splitSmart(text, MAX);
return chunks.map((c,i)=>({ json:{ text:c, phone, instance, index:i+1, total:chunks.length }}));
```

Teste e ajuste `MAX` até virar 3.

## B) Pelo número de partes (fixo em 3)

Primeiro quebra por frases. Depois “empacota” para **exatamente** 3 blocos balanceados.

```markdown
const text = ($json.reply ?? $json.text ?? '').toString();
const phone = $json.phone, instance = $json.instance;
const TARGET = 3; // <- 3 partes fixas
const sentences = text.split(/(?<=\.|\?|!|\n)/).map(s=>s.trim()).filter(Boolean);
if (sentences.length === 0) return [{json:{text:text, phone, instance, index:1, total:1}}];

// soma total e comprimento alvo
const totalLen = sentences.reduce((a,s)=>a+s.length,0);
const targetLen = Math.ceil(totalLen / TARGET);

// empacotamento guloso até atingir 3
const chunks=[]; let buf='', len=0;
for (const s of sentences){
  if ((len + s.length) <= targetLen || chunks.length >= TARGET-1){
    buf += (buf ? ' ' : '') + s; len += s.length;
  } else {
    chunks.push(buf); buf = s; len = s.length;
  }
}
if (buf) chunks.push(buf);

// se passou de 3, mescla últimos
while (chunks.length > TARGET) {
  const a = chunks.pop(); chunks[chunks.length-1] += ' ' + a;
}

return chunks.map((c,i)=>({ json:{ text:c.trim(), phone, instance, index:i+1, total:chunks.length }}));
```

### No Evolution

- Mensagem: `{{ $json.text }}`
- Número: `{{ $json.phone }}`
- Instância: `{{ $json.instance || 'BRANN' }}`
- Split in Batches: batch=1, continue→wait→volta.

Escolha A para controle por **tamanho**.  
Escolha B quando quiser **exatamente 3** mensagens, independentemente do tamanho.

qual a melhor maneira? para padronizarmos e sempre acontecer desse jeito para a conversa ficar mais humana

Use divisão semântica com alvo dinâmico + ritmo humano. Fica natural e previsível.

## Padrão recomendado

1. **Quebre por sentido**: frases e parágrafos, sem cortar links, listas ou blocos de código.
2. **Alvo dinâmico**: escolha 2–4 pedaços conforme o tamanho do texto.
3. **Conector sutil**: finalize cada parte (exceto a última) com “segue 👇” ou “…” opcional.
4. **Ritmo humano**: `Wait` com jitter 450–900 ms entre envios.
5. **Sem contadores** por padrão. Ative `(1/3)` só para debug.

## Code node (cole e use “Run Once for All Items”)

Gera itens prontos para o Evolution.

```markdown
const raw = ($json.reply ?? $json.text ?? '').toString();
const phone = $json.phone;
const instance = $json.instance;

// 1) proteção de formatação
const isList = s => /^(\-|\*|\d+\.)\s/.test(s.trim());
const isCodeFence = s => s.trim().startsWith('\`\`\`');
const hasLink = s => /https?:\/\/\S+/.test(s);

// 2) split básico por parágrafo e frase
const paras = raw.split(/\n{2,}/).map(p => p.trim()).filter(Boolean);
const sentences = [];
for (const p of paras) {
  if (isCodeFence(p)) { sentences.push(p); continue; }
  const parts = p.split(/(?<=\.|\?|!)(\s+)/).reduce((acc,cur)=>{
    if (!cur.trim()) return acc;
    // junta pontuação + espaço com frase anterior
    if (acc.length && /^\s+$/.test(cur)) { acc[acc.length-1]+=cur; }
    else acc.push(cur);
    return acc;
  }, []);
  const joined = [];
  let buf = '';
  for (const s of parts) {
    const chunk = (buf + s);
    // preserva listas/links inteiras
    if (isList(s) || hasLink(s)) { if (buf) { joined.push(buf); buf=''; } joined.push(s); }
    else if (chunk.length <= 220) buf = chunk; // ~3–4 frases curtas por bloco
    else { if (buf) joined.push(buf); buf = s; }
  }
  if (buf) joined.push(buf);
  sentences.push(...joined);
}

// 3) alvo dinâmico de pedaços (2–4)
const totalLen = raw.length;
let targetParts = totalLen < 300 ? 1 : totalLen < 800 ? 2 : totalLen < 1600 ? 3 : 4;

// reempacota de forma “equilibrada”
const targetLen = Math.ceil(totalLen / Math.max(1, targetParts));
const chunks = [];
let buf = '', len = 0;
for (const s of sentences) {
  if (isCodeFence(s) || isList(s) || hasLink(s)) {
    if (buf) { chunks.push(buf.trim()); buf=''; len=0; }
    chunks.push(s.trim());
    continue;
  }
  const add = (buf ? ' ' : '') + s.trim();
  if ((len + add.length) <= targetLen || chunks.length >= targetParts-1) {
    buf += add; len += add.length;
  } else {
    if (buf) chunks.push(buf.trim());
    buf = s.trim(); len = buf.length;
  }
}
if (buf) chunks.push(buf.trim());

// Se estourou, mescla até caber no limite de 4
while (chunks.length > 4) {
  const last = chunks.pop();
  chunks[chunks.length-1] += ' ' + last;
}

// 4) conector humano
const connector = ' (segue 👇)';
const out = chunks.map((c,i,arr)=>({
  json: {
    text: i < arr.length-1 ? c.replace(/\s+$/,'') + connector : c,
    phone, instance,
    index: i+1, total: arr.length
  }
}));

return out.length ? out : [{ json: { text: raw, phone, instance, index:1, total:1 } }];
```

## Evolution (send-text)

- Instância: `{{ $json.instance || 'BRANN' }}`
- Número: `{{ $json.phone }}`
- Mensagem: `{{ $json.text }}`
- Envio **Per Item**. “Continue On Fail”: **true**.

## Loop

- **Split in Batches**: Batch Size 1, Always Output Data ON.
- **Wait**: `={{ $jitter(450,900) }}` ms; porta **Continue** de volta para o Split.
- Porta **Done** segue o fluxo.

## Observações

- Quer sempre 3 partes? Troque `targetParts` por `3`.
- Precisa contador? Adicione `({{ $json.index }}/{{ $json.total }})` no final do texto.
- Se o provedor suportar “typing”, envie antes de cada chunk para ainda mais naturalidade.

Com isso, toda resposta longa vira 2–4 mensagens coesas, ritmo humano e sem cortes feios.

qua., 5 de nov. às 1:56

deu certo?

Sim, pelo print parece correto. Confirme em 30s:

1. **Code → Output**
- Deve mostrar **N itens** (≥2) quando você testa com texto longo.
- Cada item com `{ text, phone, instance, index, total }`.
2. **Loop**
- `Split in Batches` com **Batch Size=1** e **Always Output Data=ON**.
- Porta **Continue** → `Wait` → volta no `Split`.
- Porta **Done** segue adiante.
3. **Evolution**
- Instância: `{{ $json.instance || 'BRANN' }}`
- Número: `{{ $json.phone }}`
- Mensagem: `{{ $json.text }}`
- **Per Item** habilitado.
4. **Ritmo**
- `Wait` com `={{ $jitter(450,900) }}` ms.

Teste rápido:

- No Code, defina temporariamente `const TARGET = 3` (ou `MAX = 80`) para forçar 3 partes.
- Execute só o bloco até o Evolution. Deve enviar 3 mensagens com o conector “segue 👇” nas duas primeiras.

Se ainda sair 1 mensagem:

- O `Code` gerou só 1 item → reduza `MAX` ou fixe `TARGET = 3`.
- O Evolution está lendo outro caminho (ex.: `$('Code...').item...`) → troque para **`$json.text`**.
- O If desviou para o caminho “curto” → ajuste a expressão do If ou elimine-o e sempre passe pelo loop.

Quer que **sempre** quebre em 3? Troque no Code:

```markdown
const TARGET = 3; // fixa em 3 partes
```

O resto fica igual.