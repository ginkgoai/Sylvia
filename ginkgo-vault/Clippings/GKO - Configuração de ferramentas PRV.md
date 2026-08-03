---
title: "GKO - Configuração de ferramentas PRV"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69371cb1-3100-8331-bd3c-f425508ba6ba"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
seg., 8 de dez. às 15:45

Perfeito. Vamos **configurar as duas ferramentas (Gmail + Google Sheets) dentro do agente PRV**, seguindo o padrão corporativo de arquitetura que já montamos no fluxo do Brann.

A ideia:

1. **Sempre que um pedido for fechado → enviar e-mail automático para a equipe PRV.**
2. **Registrar/atualizar os dados do cliente e do pedido em uma planilha do Google Sheets.**

Abaixo está tudo destrinchado como arquiteto de dados + automação n8n.

---

## 1\. GMAIL – “Send a message in Gmail”

### OBJETIVO

Enviar um alerta para a PRV sempre que o agente detectar um pedido finalizado.

### 1.1. Antes de tudo: Criar a credencial no n8n

No n8n:

```markdown
Credentials → New → Gmail OAuth2
```

Configurar:

- OAuth Client ID (Google Cloud)
- OAuth Secret
- Autorização da conta PRV → clicar → conceder acesso.

Depois disso, a credencial aparecerá no dropdown do node.

---

### 1.2. Configuração do Node Gmail (copy/cola)

**Operation:** `Send`

**To:**

```markdown
vendas@prvalimentos.com (ou o email oficial)
```

**Subject:**

```markdown
Novo pedido recebido – PRV Alimentos
```

**Email Type:** `HTML`

**Message (copy/paste com variáveis):**

```markdown
<html>
<body>
<h2>Novo Pedido Recebido</h2>
<p><strong>Cliente:</strong> {{$json.nome_cliente}}</p>
<p><strong>Telefone:</strong> {{$json.phone}}</p>
<p><strong>Itens:</strong> {{$json.itens}}</p>
<p><strong>Total:</strong> R$ {{$json.total}}</p>
<p><strong>Endereço:</strong> {{$json.endereco}}</p>
<hr>
<p>Gerado automaticamente pelo agente CALLIMA via plataforma Ginkgo.</p>
</body>
</html>
```

### 1.3. O agente CALLIMA deve disparar esse node quando:

No bloco final do fluxo, depois que CALLIMA retorna um JSON tipo:

```markdown
{
  "pedido_finalizado": true,
  "nome_cliente": "...",
  "phone": "...",
  "itens": "...",
  "total": "...",
  "endereco": "..."
}
```

→ Criamos um **IF Node**:

**Condition:**

```markdown
{{$json.pedido_finalizado === true}}
```

**Se TRUE → Gmail Node**  
**Se FALSE → segue fluxo normal**

---

## 2\. GOOGLE SHEETS – “Get Row(s) / Append Row”

Você abriu o node "Get Row(s)", mas para registrar pedidos precisamos **Append Row** ou **Update Row**.

O fluxo ideal é:

1. CALLIMA gera o JSON final com dados.
2. REGISTRA NA PLANILHA.
3. Envia e-mail (opcional).

---

## 2.1. Criar a planilha PRV – Modelo recomendado

**Nome:** `Pedidos PRV`

**Aba:** `Pedidos`

**Colunas:**

```markdown
timestamp | nome_cliente | telefone | pedido | total | endereco | pagamento | status
```

---

## 2.2. Criando a credencial no n8n

```markdown
Credentials → New → Google Sheets OAuth2
```

Conceder acesso.

---

## 2.3. Node correto: “Append Row”

Configuração:

**Operation:** `Append Row`

**Document:** selecione a planilha  
**Sheet:** `Pedidos`

**Fields (copy/paste):**

```markdown
timestamp: {{$now}}
nome_cliente: {{$json.nome_cliente}}
telefone: {{$json.phone}}
pedido: {{$json.itens}}
total: {{$json.total}}
endereco: {{$json.endereco}}
pagamento: {{$json.pagamento}}
status: "Recebido"
```

---

## 2.4. Se quiser “atualizar” quando o pedido progredir

Você usa:

- “Get Row(s)” para buscar pelo telefone ou ID do pedido
- “Update Row” usando o Row ID retornado

**Get Row(s) Filtro:**

```markdown
Column: telefone
Value: {{$json.phone}}
```

---

## 3\. Integração no agente CALLIMA (PRV)

Para funcionar perfeitamente, o agente deve retornar SEMPRE:

```markdown
{
  "out": { ... },
  "pedido_finalizado": true,
  "nome_cliente": "...",
  "phone": "...",
  "itens": "...",
  "total": "...",
  "endereco": "...",
  "pagamento": "Pix / Crédito / etc"
}
```

Assim n8n consegue:

**1\. Registrar → Sheets**  
**2\. Avisar → Gmail**

---

## 4\. FLUXO FINAL (MENTAL MAP SCIFI)

Imagine CALLIMA como um “dronelogista” digital dentro da PRV:

1. O drone recebe o pedido → organiza → valida.
2. Quando o pedido está completo → ele dispara dois feixes:
	- **Feixe 1:** grava o pedido no “Cérebro Operacional” (Google Sheets).
		- **Feixe 2:** envia um “alerta vermelho” para o QG (Gmail).
3. Tudo ocorre em menos de 1s.

Essa é a **cadeia operacional impecável** do agente PRV.

---

## 5\. Checklist de implementação

### Google Sheets

- Criar planilha
- Criar aba `Pedidos`
- Criar credencial Sheets
- Node "Append Row" configurado
- IF condicional do pedido finalizado

### Gmail

- Criar credencial Gmail OAuth2
- Configurar template HTML
- Conectar no IF do pedido finalizado

### Agent CALLIMA

- Garantir que o output JSON inclua todos os campos
- Garantir flag `pedido_finalizado: true`
- Testar ponta-a-ponta com pedido fictício

---

Se quiser, eu **monto agora os nodes completos em JSON de import** (Gmail + Sheets + IF + mapeamento FINAL).