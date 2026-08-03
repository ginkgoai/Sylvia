---
title: "GKO - Grupão automático com n8n"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69cdc559-0120-83e9-95de-f773f3e7a56f"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
qua., 1 de abr. às 22:24

qui., 2 de abr. às 16:24

Fluxo de Promoções - ML, Shopee, Amazon.json

Arquivo

analise / vamos corrigir e configurar

e agora

?

Você está **quase lá**, mas tem um detalhe crítico quebrando tudo:

👉 **sua tabela NÃO tem a coluna `hash` ainda**

Por isso o campo tá vermelho.

---

## ⚠️ CORREÇÃO IMEDIATA (isso destrava tudo)

## Vá na tabela promo\_ml\_hashes

Clique em:  
👉 **Add Column**

Crie exatamente isso:

### Coluna 1 (ESSENCIAL)

- Nome: `hash`
- Tipo: `string`

---

## (já aproveita e cria essas também)

### Coluna 2

- `product_id` → string

### Coluna 3

- `title` → string

### Coluna 4

- `price` → number

### Coluna 5

- `source` → string

---

## 💡 Por que isso é importante?

Seu node está fazendo isso:

```markdown
{{ $json.hash }}
```

Mas sua tabela não sabe o que é `hash`.

Resultado:  
❌ filtro quebra  
❌ duplicação não funciona  
❌ fluxo trava silenciosamente

---

## 🔧 Depois de criar a coluna

Volta no node **Buscar Duplicado**

E deixa assim:

- Column: `hash`
- Condition: `Equals`
- Value:
```markdown
{{ $json.hash }}
```

---

## ⚠️ OUTRO DETALHE IMPORTANTE

Na esquerda está aparecendo:

👉 **"No input data"**

Isso significa:

❌ você não executou os nodes anteriores  
ou  
❌ o fluxo antes não está passando dados

---

## Resolve assim:

Clica em:  
👉 **Execute previous nodes**

---

## 🧠 Como validar que tá certo

Depois disso:

1. Executa fluxo completo
2. Primeira vez → deve enviar
3. Segunda vez → NÃO deve enviar

---

## 🧬 Se quiser validar rápido

Depois do envio, olha sua tabela:

Ela deve ter algo tipo:

```markdown
hash: MLB123456_194
product_id: MLB123456
title: Fogão 4 bocas
price: 194
source: mercadolivre
```

Se isso aparecer → sistema vivo  
Se não aparecer → o insert node ainda não está conectado

---

## 📌 Estado atual do seu sistema

Você está exatamente aqui:

```markdown
[Infra pronta] ✅
[Memória criada] ✅
[Deduplicação quase] ⚠️
[Envio automático] 🔜
```

---

## 🚀 Próximo passo (depois disso funcionar)

Te recomendo já emendar:

- limitar 3–5 produtos por execução
- delay entre envios (anti-ban)
- filtro de qualidade melhor
- melhorar copy

---

Se quiser, no próximo passo eu te mostro:

👉 **onde exatamente ligar cada node (visual estilo mapa n8n)**  
👉 ou reviso seu fluxo completo print a print contigo

Agora você já saiu do modo iniciante.  
Só falta alinhar esses detalhes e vira operação.

assim

Perfeito. Agora está **100% correto estruturalmente**.  
Você já tem a base pronta — falta só conectar o “cérebro” com o “corpo”.

Agora vamos ligar isso no fluxo de verdade.

---

## ✅ O que você já fez (status real)

```markdown
Tabela criada ✅
Colunas criadas ✅
Estrutura correta ✅
```

Essa linha com `Null` pode ignorar — foi criada automaticamente.

---

## ⚙️ AGORA VAMOS CONECTAR NO N8N

## 1\. NODE → GERAR HASH (CONFERE SE EXISTE)

Antes do node **Buscar Duplicado**, você precisa ter isso:

### Code Node (obrigatório)

```markdown
return items.map(item => {
  const productId = item.json.id || item.json.title;
  const price = item.json.price;

  const hash = \`${productId}_${price}\`;

  return {
    json: {
      ...item.json,
      hash
    }
  };
});
```

👉 Se não tiver isso, o resto não funciona.

---

## 2\. NODE → BUSCAR DUPLICADO (o que você já abriu)

Configuração correta (igual você está fazendo):

- Table: `promo_ml_hashes`
- Column: `hash`
- Condition: `Equals`
- Value:
```markdown
{{ $json.hash }}
```

✔️ Isso já está certo

---

## 3\. NODE → IF (DECISÃO)

Depois do “Buscar Duplicado”

Cria um node **IF**

### Condição:

```markdown
{{ $json.length === 0 }}
```

---

### Saídas:

- ✅ TRUE → segue fluxo (produto novo)
- ❌ FALSE → ignora (já enviado)

---

## ⚙️ 4. NODE → ENVIO (Evolution)

Só conecta o TRUE no envio.

---

## ⚙️ 5. NODE → SALVAR NA TABELA (CRÍTICO)

Depois do envio, cria:

👉 **Data Table → Insert Row**

Campos:

```markdown
{
  "hash": "={{ $json.hash }}",
  "product_id": "={{ $json.id }}",
  "title": "={{ $json.title }}",
  "price": "={{ $json.price }}",
  "source": "mercadolivre"
}
```

---

## 🧠 VISUAL DO FLUXO

```markdown
Buscar produtos
   ↓
Normalizar
   ↓
Gerar HASH
   ↓
Buscar na tabela
   ↓
IF (já existe?)
   ↓ NÃO
Enviar WhatsApp
   ↓
Salvar na tabela
```

---

## ⚠️ TESTE QUE VOCÊ TEM QUE FAZER AGORA

### Teste 1:

- Executa → deve enviar ofertas

### Teste 2:

- Executa de novo

👉 Resultado esperado:

```markdown
Nenhuma mensagem enviada (ou menos)
```

Se repetir → erro no hash ou no IF

---

## ⚠️ ERROS COMUNS (fica esperto)

### ❌ Erro 1

hash não existe no item  
→ resolve no Code node

### ❌ Erro 2

Buscar duplicado não retorna array  
→ muda para "Get Many Rows"

### ❌ Erro 3

Insert não está conectado  
→ não salva → repete tudo

---

## 🔥 MELHORIA RÁPIDA (recomendo já)

Troca o hash para algo mais robusto:

```markdown
const hash = \`${productId}_${price}_${item.json.permalink}\`;
```

Evita duplicação mesmo se o preço oscilar.

---

## 📌 Estado atual do seu sistema

```markdown
Infra pronta ✅
Memória funcionando 🔜
Anti-spam quase ativo 🔥
Automação real a 1 passo 🚀
```

---

Se quiser, próximo passo eu te entrego:

👉 sistema com **ranking de ofertas (só envia as melhores)**  
👉 ou **delay inteligente pra não tomar block no WhatsApp**

Agora você já tá operando nível semi-profissional.

Agora sim — isso aqui já é um **fluxo real de produção**.  
Mas tem **1 bug crítico + 3 melhorias obrigatórias** pra ele não falhar silenciosamente.

Vou direto no que importa.

---

## 🚨 BUG CRÍTICO (isso quebra sua lógica de duplicado)

## ❌ Problema

Seu node **“Nao Foi Enviado”** está errado.

Hoje ele faz isso:

```markdown
leftValue: {{ $json.id || '' }}
operation: empty
```

👉 Isso não tem NADA a ver com duplicação.

---

## 💣 O que deveria acontecer

O node anterior (**Buscar Duplicado**) retorna:

- **\[\] (vazio)** → NÃO existe → pode enviar
- **\[registro\]** → já existe → NÃO enviar

---

## ✅ CORREÇÃO

### No node “Nao Foi Enviado”

Troca a condição para:

```markdown
{{ $items().length === 0 }}
```

OU (mais seguro):

```markdown
{{ $json.length === 0 }}
```

---

## 💡 Resultado

```markdown
Se NÃO encontrou no banco → envia
Se encontrou → bloqueia
```

---

## ⚠️ PROBLEMA 2 — VOCÊ NÃO ESTÁ SALVANDO NA TABELA CERTA

## ❌ Hoje:

Você salva em:

```markdown
promo_logs
```

Mas você está buscando duplicado em:

```markdown
promo_ml_hashes
```

---

## 💣 Resultado:

Seu sistema NÃO aprende.

Vai mandar a mesma oferta pra sempre.

---

## ✅ CORREÇÃO

No node **Salvar Historico**, muda para:

👉 tabela:

```markdown
promo_ml_hashes
```

E campos:

```markdown
{
  "hash": "={{ $json.hash }}",
  "product_id": "={{ $json.productId }}",
  "title": "={{ $json.title }}",
  "price": "={{ $json.newPrice }}",
  "source": "mercadolivre"
}
```

---

## ⚠️ PROBLEMA 3 — HASH PODE REPETIR ERRADO

Hoje você usa:

```markdown
hash: \`ml:${item.id}:${current}\`
```

👉 Isso é bom, mas pode falhar se:

- preço muda
- mesma oferta com variação

---

## 🔥 MELHOR VERSÃO

Troca para:

```markdown
hash: \`ml:${item.id}:${item.permalink}\`
```

Ou ultra robusto:

```markdown
hash: \`ml:${item.id}:${current}:${item.permalink}\`
```

---

## ⚠️ PROBLEMA 4 — SPAM EM MASSA (cuidado)

Você está fazendo:

```markdown
10 keywords × 10 resultados = 100 produtos por execução
```

A cada 30 minutos = 💀

---

## ✅ SOLUÇÃO RÁPIDA

Adiciona depois do filtro:

👉 **Limit Node**

- Limit: `3` ou `5`

---

## 🔥 OTIMIZAÇÃO EXTRA (vale MUITO)

## Adicionar delay dinâmico

No node Evolution:

```markdown
"delay": 3000
```

👉 Evita:

- ban
- bloqueio
- throttling

---

## 🧠 FLUXO FINAL CORRIGIDO

```markdown
Cron
→ Keywords
→ Split
→ Buscar ML
→ Normalizar
→ Filtro desconto
→ Buscar duplicado
→ IF (length === 0)
→ LIMIT (3-5)
→ Montar mensagem
→ Enviar
→ Salvar em promo_ml_hashes
```

---

## 📊 ESTADO DO SEU SISTEMA AGORA

```markdown
Arquitetura: 9/10
Lógica: 7/10 → (corrigindo IF sobe pra 10)
Escalabilidade: 6/10 → (falta fila/ranking)
Risco de spam: ALTO ⚠️
```

---

## 🚀 PRÓXIMO NÍVEL (se quiser evoluir)

Posso te montar agora:

### 🔹 V2 inteligente

- ranking de ofertas (IA ou score)
- só envia TOP 3
- prioriza desconto + demanda

### 🔹 V3 monetização

- link afiliado automático
- tracking de clique
- ROI por produto

### 🔹 V4 máquina real

- múltiplos grupos
- rotação de conteúdo
- comportamento humano simulado

---

## 🧠 Resumo direto

Você já construiu:

👉 um bot funcional  
👉 com ingestão real  
👉 com filtro  
👉 com envio automático

Faltava só:

- corrigir duplicação
- salvar no lugar certo
- limitar volume

---

Se quiser, manda o próximo passo:

👉 “quero ranking inteligente”  
ou  
👉 “quero evitar ban total”