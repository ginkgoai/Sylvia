---
title: "GKO - Integração Manus API"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/69a41a4c-3840-832d-9622-1279bc8cd59e"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
dom., 1 de mar. às 7:52

![253570a9-0738-4543-b204-a31b736ff0a2.png](https://chatgpt.com/backend-api/estuary/content?id=file_000000004de871f5911422208707c396&ts=495692&p=fs&cid=1&sig=99f62295ed7048ca7c574242b222ff0fc238c63de5bffd18880fe0d04bb114ab&v=0) ![cab375f4-183f-4fa9-b5e2-93fbfda8965a.png](https://chatgpt.com/backend-api/estuary/content?id=file_00000000d7e871f5b8435d596aa07950&ts=495692&p=fs&cid=1&sig=a7f033dd05504a2aacb89a596641566aad466452967c0579a7978f60d98f3521&v=0)

🎯 Qual você prefere? Opção 1: Usar endpoint Manus direto (mais simples ) Opção 2: Usar skill n8n-manus-api (mais robusto) Me diga qual você quer que vou criar a fórmula correta! 🚀 2 Lendo a skill n8n-manus-api para entender como integrar corretamente... Identifiquei erro de permissão nas variáveis de ambiente. A solução é usar a API do Manus diretamente ou a skill n8n-manus-api, dependendo da preferência do usuário. Próximo passo: implementar a opção escolhida. 07:46 ✅ Solução com Skill n8n-manus-api Perfeito! Vou criar o nó HTTP correto usando a skill n8n-manus-api. Preciso de algumas informações: URL da sua API Manus: (ex: https://manus-api.example.com ) me ajude a responder isso

Você precisa responder para a Manus com **a URL base da sua API Manus** — ou seja, o endpoint onde sua instância está rodando.

Pelo seu print, você está usando:

```markdown
https://manus.im/app/...
```

⚠️ Mas isso é a interface web, não é a API.

---

## ✅ O que você deve responder

Se você estiver usando a API oficial da Manus (cloud deles), normalmente a base é algo como:

```markdown
https://api.manus.im
```

Ou (dependendo do plano/instância):

```markdown
https://manus.im/api
```

---

## 🔎 Como descobrir a URL correta

1. Vá no painel da Manus
2. Procure por:
	- **API**
		- **Developer**
		- **Base URL**
		- **API Docs**
3. Copie a **Base URL da API**, não a URL do navegador.

---

## 🎯 Resposta que você pode enviar agora

Se for cloud padrão da Manus, responda assim:

```markdown
URL da API Manus: https://api.manus.im
```

Se você estiver rodando Manus self-hosted no VPS, então seria algo como:

```markdown
https://manus.seudominio.com
```

ou

```markdown
http://IP-DO-SEU-VPS:PORTA
```

---

## ⚠️ Importante

Além da URL, ele vai pedir também:

- API Key
- tenant\_id (ex: ginkgo)
- agent\_id (ex: brann)

Se quiser, me confirma:

- Você está usando Manus cloud ou self-hosted?
- Tem domínio próprio configurado?

Eu já te devolvo a resposta exata, pronta para colar no n8n.

Perfeito. Pela sua imagem você está em:

```markdown
manus.im/app/settings/integrations/api
```

Ali só aparecem **API Keys**.  
A **Base URL não fica nessa tela**.

---

## ✅ Onde está a Base URL da Manus

Se você está usando **Manus Cloud (manus.im)**, a base padrão é:

```markdown
https://manus.im/api
```

Ou, dependendo da versão:

```markdown
https://api.manus.im
```

---

## 🎯 Como confirmar 100%

1. Clique em **“Documentação”** (botão no canto da tela que você mostrou).
2. Vai abrir a página de API Docs.
3. Lá no topo vai aparecer algo como:
```markdown
Base URL: https://manus.im/api
```

Essa é a que você deve usar no n8n.

---

## 🚀 O que você deve responder para o assistente da Manus agora

Provavelmente:

```markdown
URL da API Manus: https://manus.im/api
```

Se der erro 404, teste:

```markdown
https://api.manus.im
```

---

## ⚠️ Estrutura correta no n8n depois

No HTTP Node:

**Method:** POST  
**URL:**

```markdown
https://manus.im/api/v1/ask
```

Headers:

```markdown
Authorization: Bearer SUA_API_KEY
Content-Type: application/json
```

---

Se quiser, me manda:

- Qual agente você vai chamar (brann, alfred, etc.)
- Se vai usar tenant ginkgo

Que eu já te entrego o nó HTTP completo pronto para colar no n8n.

Tenant é o **identificador lógico do seu workspace/projeto dentro da Manus**.

Pensa assim:

```markdown
Manus (infra)
 └── Tenant (sua organização)
      └── Agent (brann, alfred, nyra...)
```

---

## 🎯 No seu caso

Pelo seu padrão de organização (Ginkgo como holding), o mais coerente é:

```markdown
tenant_id: ginkgo
```

E os agentes seriam:

```markdown
agent_id: brann
agent_id: alfred
agent_id: nyra
```

---

## ⚠️ Mas como confirmar o tenant real?

Faça isso:

1. Vá na Manus
2. Clique em **Projects**
3. Veja o nome do projeto principal onde o agente está criado

Se seu projeto se chama:

- `Ginkgo` → tenant = `ginkgo`
- `ALFRED` → tenant = `alfred`
- `Brann` → tenant = `brann`

O tenant normalmente é o **slug do projeto**, tudo minúsculo.

---

## 🚀 Exemplo final para você usar

Se o projeto principal for Ginkgo e você estiver chamando o Brann:

```markdown
X-Tenant-Id: ginkgo
X-Agent-Id: brann
```

---

Se quiser me mandar:

- Nome exato do projeto onde o agente está
- Nome exato do agente

Eu já te devolvo a configuração perfeita, sem tentativa e erro.