---
title: "GKO - Fluxo de processamento JSON"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/6920de26-73a8-8327-bf57-208e07c5d1d7"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 21 de nov. às 18:48

ajustando a leitura de qualquer doc no fluxo do brann. agora ta saindo como json, qual a melhor maneira de transcrevermos doc e entregar pro agent

Hoje o “erro” não é sair como JSON. O problema é **entregar esse JSON cru pro agente**.  
O melhor padrão: **extrair → normalizar pra `text` → (opcional) resumir → mandar pro BRANN**. Tudo igual ao que já fazemos com áudio/vídeo/imagem.

Visao-geral-do-fluxo

Vou te passar um modelo direto pra n8n.

---

## 1) Padrão geral do fluxo

Depois do `Route Document Types` (PDF / XLS / XLSX / CSV / etc):

1. `Extract from PDF` / `Extract from XLS` / `Extract from XLSX`
2. `Map JSON` (organiza o JSON bruto em um shape único: `type`, `pages`, `rows`, `filename` …)
3. **Function “DOC → TEXT” (novo)** → cria um campo `text` único
4. Esse `text` entra no teu `Map3` / `Text Final` e depois vai para o BUFFER → Agent BRANN

Ou seja: você mantém o JSON pra uso técnico, mas o agente sempre recebe **um campo texto limpo**.

---

## 2) Function Node: DOC → TEXT (cola direto)

Adiciona logo depois do `Map JSON` (saída dos extratores):

```markdown
// DOC → TEXT
// Normaliza qualquer documento para um campo .text pronto pro agente

const out = [];

for (const item of items) {
  const j = item.json;
  let text = '';

  const type = (j.type || j.docType || '').toLowerCase();

  // PDF (ex.: { pages: [{ text: '...' }, ...] })
  if (type === 'pdf' || j.pages) {
    const pages = j.pages || [];
    text = pages
      .map((p, i) => \`--- Página ${i + 1} ---\n${p.text || ''}\`)
      .join('\n\n');
  }

  // PLANILHA / TABELA (XLS, XLSX, CSV)
  else if (['xls', 'xlsx', 'csv'].includes(type) || j.rows || j.data) {
    const rows = j.rows || j.data || [];
    if (rows.length) {
      const headers = Object.keys(rows[0]);
      text = rows
        .map((row, i) =>
          \`Linha ${i + 1}: \` +
          headers
            .map((h) => \`${h}: ${row[h] ?? ''}\`)
            .join(' | ')
        )
        .join('\n');
    }
  }

  // DOCX / TXT / OUTROS
  else if (j.text) {
    text = j.text;
  } else {
    // fallback: stringify do JSON
    text = JSON.stringify(j, null, 2);
  }

  out.push({
    json: {
      ...j,
      text,
    },
  });
}

return out;
```

Depois desse node, **todo documento vira `item.json.text`**, independente do formato original.

---

## 3) Entrega para o Agent BRANN

No nó que prepara a entrada do Agent (ex.: `Text Final` ou `Map?` antes do BUFFER):

1. Garante que `text` esteja lá:
	- `text = {{$json.text}}`
2. Junta com a mensagem original do usuário (ex.: `user_message` vindo do Whats):

Exemplo de `System` + `User` no Chat Model / Agent:

**System (BRANN para docs)**  
Algo assim:

```markdown
Você é o BRANN, atendente da Ginkgo. 
Você recebe a mensagem do usuário + o conteúdo de um documento em texto.
Use o documento apenas como contexto. Responda de forma objetiva, sem colar o documento inteiro.
Se o documento for uma planilha, interprete as linhas como registros.
Se não encontrar a informação, diga que não encontrou e ofereça ajuda alternativa.
```

**User:**

```markdown
Mensagem do usuário:
{{ $json.user_message }}

Conteúdo do documento (texto bruto):
{{ $json.text }}
```

Ou, se quiser proteger tokens:

```markdown
Conteúdo do documento (pode estar cortado):
{{ $json.text.substring(0, 12000) }}
```

---

## 4) Extra: docs grandes (chunk + resumo)

Quando o documento for gigante, o ideal é:

1. Depois do `DOC → TEXT`:
	- `SplitInBatches` ou `Function` que quebra `text` em pedaços de ~4000 caracteres.
2. Loop:
	- Nó “Resumo Parcial (OpenAI)”  
		System: “Resuma este trecho do documento…”  
		User: `{{$json.chunk}}`
3. `Aggregate` juntando todos os resumos parciais em um `summary`.
4. BRANN recebe só:
```markdown
Resumo do documento:
{{ $json.summary }}

Mensagem do usuário:
{{ $json.user_message }}
```

Assim você não explode contexto e ainda fica muito mais rápido.

---

## 5) Em resumo (padrão que eu usaria)

- **Manter JSON**: para logs, BI, salvar em Supabase, etc.
- **Criar sempre um `text` limpo**: Function `DOC → TEXT`.
- **Opcional**: nó de “Resumo de Documento” antes do Agent.
- **Agent BRANN** recebe sempre: `user_message` + `text` (ou `summary`).

Se quiser, me manda um print do JSON que está saindo do `Extract from PDF` / `Extract from XLSX` e eu ajusto o `DOC → TEXT` exatamente pro shape que teu node está devolvendo.

A mensagem do erro está certa: o problema **não é o node Extract from PDF**, é o que está chegando nele.

No print dá pra ver:

- `File Name: data.json`
- `File Extension: json`
- `Mime Type: application/json`

Ou seja: você está mandando um **JSON** como se fosse **PDF**, então o node acusa `Invalid PDF structure`.

Vamos arrumar em duas camadas:

---

## 1\. Garantir que o Extract from PDF receba um PDF de verdade

Onde você baixa o arquivo (node `Download Document` / `HTTP Request`):

1. Se for `HTTP Request`:
	- `Response Format`: **File**
		- `Binary Property`: `data`
		- Não deixar como “JSON”.
2. Se for um node específico (Google Drive, S3, etc.):
	- Confirma que a saída está em aba **Binary** como `data` com `mimeType: application/pdf`, não como `.json`.

Teste rápido:

1. Cria um fluxo simples só pra testar:
	- Node `Read Binary File`
		- Aponta para um PDF local qualquer.
		- Node `Extract from PDF`
		- `Input Binary Field`: `data`
2. Executa.
	- Se funcionar, está provado que o node de PDF está ok.
		- Então o problema é **só** o que vem antes no fluxo do BRANN.

Em seguida, no teu fluxo real:

- No node de roteamento (`Route Document Types`), só manda para `Extract from PDF` quando:
	- `{{$json["mimeType"]}} == "application/pdf"`  
		ou
		- `{{$json["fileExtension"]}} == "pdf"`

Se cair um `.json`, `.xlsx`, `.csv` etc, isso vai por outro caminho (não passa pelo `Extract from PDF`).

---

## 2\. O que fazer quando o arquivo for JSON mesmo

Quando o documento for literalmente um `.json` (como está no print):

1. **Não** usar `Extract from PDF`.
2. Cria um branch no `Route Document Types` para `type = json` / `fileExtension = json`.
3. Nesse branch, usa só um `Function` para transformar o JSON em texto que o agente consiga ler, algo nesse formato:
```markdown
// JSON → TEXT
const out = [];

for (const item of items) {
  const j = item.json;

  const text = \`Documento JSON recebido. Conteúdo:\n\` +
    JSON.stringify(j, null, 2);

  out.push({
    json: {
      ...j,
      text,
      type: 'json',
    },
  });
}

return out;
```

Depois disso é igual ao resto: esse `text` entra no teu `Map3` / `Text Final` e segue pro BUFFER → Agent.

---

## 3\. Como entregar para o Agent (padrão final)

Independente do tipo:

- PDF → `Extract from PDF` → `Function DOC → TEXT` (`text` = concat das páginas)
- XLS/XLSX/CSV → `Extract from XLS(X)` → `Function` que vira linhas em texto → `text`
- JSON → `Function JSON → TEXT` → `text`

No nó antes do Agent (ex.: `Text Final`):

```markdown
Mensagem do usuário:
{{ $json.user_message }}

Conteúdo do documento:
{{ $json.text }}
```

Opcional: corta pra não estourar contexto:

```markdown
{{ $json.text.substring(0, 12000) }}
```

---

### Resumão

- Esse erro específico é porque **o binary é um `.json`**, não um PDF.
- Corrige o node que baixa o arquivo pra trazer **file** (binário) quando for PDF.
- Usa o roteador para separar PDF de JSON/planilha.
- Sempre converte para um campo `text` e manda isso pro BRANN.

Se quiser, me manda um print do node logo **antes** do `Download Document` mostrando o JSON da mensagem do WhatsApp, que eu te devolvo a configuração exata do `HTTP Request` / `Download` pra virar PDF binário certinho.