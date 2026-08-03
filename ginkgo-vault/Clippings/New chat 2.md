---
title: "New chat"
source: "https://chatgpt.com/c/6a625040-3fa8-83e9-9348-16f9631ba688"
author:
published:
created: 2026-07-23
description: "ChatGPT conversation with 4 messages"
tags:
  - "clippings"
---
**Você disse**

como gera webhook do teams

---

Para gerar um **webhook de entrada no Microsoft Teams** — por exemplo, para o n8n enviar alertas ao canal — use o aplicativo **Workflows**, que é o método atual recomendado.

## 1\. Criar o webhook no Teams

1. Abra o **Microsoft Teams**.
2. Entre no **canal** ou **chat** que receberá as mensagens.
3. Clique nos três pontos `⋯`.
4. Selecione **Workflows / Fluxos de trabalho**.
5. Pesquise por:
	**Enviar alertas de webhook para um canal**
	Para chat, escolha **Enviar alertas de webhook para um chat**.
6. Escolha a conta/conexão do Microsoft 365.
7. Selecione a **Equipe** e o **Canal**.
8. Clique em **Salvar**.
9. Na tela de detalhes, copie a **URL HTTP POST** gerada.

Essa URL será algo semelhante a:

```
https://prod-00.brazilsouth.logic.azure.com/workflows/...
```

O Teams gera a URL depois que o workflow é salvo. [^1]

## 2\. Configurar no n8n

Adicione um node **HTTP Request**:

```
Method: POST
URL: URL_DO_WEBHOOK_DO_TEAMS
Authentication: None
Send Body: JSON
Content-Type: application/json
```

Use este body:

```json
{
  "type": "message",
  "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "contentUrl": null,
      "content": {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
          {
            "type": "TextBlock",
            "text": "Alerta Ginkgo",
            "weight": "Bolder",
            "size": "Large"
          },
          {
            "type": "TextBlock",
            "text": "Webhook n8n → Microsoft Teams funcionando.",
            "wrap": true
          }
        ]
      }
    }
  ]
}
```

O webhook atual aceita requisições `POST` com Message Cards ou Adaptive Cards nesse formato. [^2]

## 3\. Usando dados dinâmicos do n8n

Dentro do Adaptive Card:

```json
{
  "type": "TextBlock",
  "text": "{{$json.message}}",
  "wrap": true
}
```

Exemplo completo:

```json
{
  "type": "message",
  "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "contentUrl": null,
      "content": {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
          {
            "type": "TextBlock",
            "text": "{{$json.title || 'Nova notificação'}}",
            "weight": "Bolder",
            "size": "Medium"
          },
          {
            "type": "TextBlock",
            "text": "{{$json.message}}",
            "wrap": true
          },
          {
            "type": "FactSet",
            "facts": [
              {
                "title": "Status",
                "value": "{{$json.status || 'Processado'}}"
              },
              {
                "title": "Data",
                "value": "{{$now}}"
              }
            ]
          }
        ]
      }
    }
  ]
}
```

## Autenticação

Ao criar o workflow, existem opções como permitir chamadas de qualquer pessoa ou restringir a usuários do tenant. Para integração simples com n8n, selecione **Anyone / Qualquer pessoa**. Nesse modo, não envie header de autenticação; enviar um token pode fazer a requisição falhar. [^2]

Guarde a URL como credencial ou variável de ambiente:

```
TEAMS_WEBHOOK_URL=https://...
```

Não exponha essa URL no GitHub: ela funciona praticamente como uma chave de acesso para publicar naquele canal.

---

**Você disse**

o que acontece quando ele não está salvando o workflow

---

Quando o **workflow não salva**, o Teams **não gera a URL do webhook**. A URL só aparece depois que o fluxo é criado com sucesso. Portanto, o problema está na camada **Teams/Power Automate**, antes do n8n. [^3]

As causas mais comuns são:

### 1\. Conexão do Microsoft Teams inválida

A autenticação pode estar expirada, especialmente após alteração de senha, MFA ou política da empresa.

Faça:

1. Abra o **Power Automate** no navegador.
2. Vá em **Conexões**.
3. Localize **Microsoft Teams**.
4. Clique nos três pontos.
5. Selecione **Corrigir conexão** ou **Entrar novamente**.
6. Volte ao workflow e tente salvar.

Erros `401` normalmente significam autenticação expirada. [^4]

### 2\. Equipe ou canal não selecionado corretamente

Dentro do workflow, revise a ação de postagem:

```
Post as: Flow bot
Post in: Channel
Team: sua equipe
Channel: seu canal
```

Procure campos com borda vermelha, aviso ou valor vazio. Campos obrigatórios incompletos são uma das principais causas de falha ao salvar. [^5]

### 3\. Sua conta não tem permissão no canal

Isso costuma gerar erro `403 Forbidden`.

Verifique se:

- Você é membro da equipe.
- Consegue publicar manualmente no canal.
- Não está usando uma conta convidada ou de outro tenant.
- O canal não possui uma política restritiva.

Também pode existir uma política **DLP — Data Loss Prevention** bloqueando o conector do Teams no Power Automate. [^4]

### 4\. O administrador bloqueou Workflows ou Power Automate

Em contas empresariais, o administrador pode bloquear aplicativos do Teams.

O administrador deve verificar:

```
Teams Admin Center
→ Teams apps
→ Manage apps
→ procurar Workflows / Power Automate
→ status: Allowed
```

As políticas de permissão também podem liberar o aplicativo apenas para alguns usuários. [^6]

### 5\. O botão fica preso em “Saving…”

Nesse caso:

1. Abra diretamente pelo **Power Automate**, não pelo painel embutido do Teams.
2. Atualize a página com `Ctrl + F5`.
3. Tente uma janela anônima/InPrivate.
4. Recrie o workflow usando o template:
```
Send webhook alerts to a channel
```

A própria documentação recomenda atualizar o designer quando ele permanece indefinidamente em “Saving”. [^5]

### Diagnóstico rápido pelo erro

| Erro | Causa provável | Correção |
| --- | --- | --- |
| `401` | Login ou token expirado | Corrigir conexão |
| `403` | Permissão ou política DLP | Verificar acesso/admin |
| `Invalid connection` | Conexão removida ou quebrada | Criar nova conexão |
| `500` | Falha temporária Microsoft | Tentar novamente |
| `502` | Falha de comunicação entre serviços | Reabrir/recriar workflow |
| Saving infinito | Interface ou sessão travada | Power Automate + InPrivate |

Esse template de webhook **não exige licença Premium**, então normalmente a causa não é cobrança ou plano. [^3]

O caminho mais eficiente é: **Power Automate → Conexões → Microsoft Teams → Corrigir conexão → reabrir o fluxo → selecionar equipe/canal → salvar**.

[^1]: [support.microsoft.com](https://support.microsoft.com/pt-br/workflows/send-messages-in-teams-using-incoming-webhooks)

[^2]: [learn.microsoft.com](https://learn.microsoft.com/en-us/connectors/teams/)

[^3]: [support.microsoft.com](https://support.microsoft.com/en-us/teams/apps-service/create-incoming-webhooks-with-workflows-for-microsoft-teams)

[^4]: [learn.microsoft.com](https://learn.microsoft.com/en-us/power-automate/fix-connection-failures)

[^5]: [learn.microsoft.com](https://learn.microsoft.com/en-us/power-automate/troubleshoot-flow-errors)

[^6]: [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoftteams/manage-apps?utm_source=chatgpt.com)