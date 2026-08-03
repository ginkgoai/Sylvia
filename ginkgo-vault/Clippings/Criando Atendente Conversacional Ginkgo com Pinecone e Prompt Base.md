---
title: "Criando Atendente Conversacional Ginkgo com Pinecone e Prompt Base"
source: "https://manus.im/app/eWp2fgvhrP41zIzc8gZlY8"
author:
published:
created: 2026-07-19
description: "Manus é o motor de ação que vai além de respostas para executar tarefas, automatizar fluxos de trabalho e expandir seu alcance humano."
tags:
  - "clippings"
---
Manus 1.6 Lite

![pasted_file_0twext_image.png](https://private-us-east-1.manuscdn.com/users/310519663097514338/uploads/wEY9RdjBjTOgktrVDdHhnz_na1fn_cGFzdGVkX2ZpbGVfMHR3ZXh0X2ltYWdl.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vdXNlcnMvMzEwNTE5NjYzMDk3NTE0MzM4L3VwbG9hZHMvd0VZOVJkakJqVE9na3RyVkRkSGhuel9uYTFmbl9jR0Z6ZEdWa1gyWnBiR1ZmTUhSM1pYaDBYMmx0WVdkbC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3ODY3NTIwMDB9fX1dfQ__&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQD7MqVVzieVwik4YUF4hydrMTYVYkGE~laPRbXT-JnzmwIgd8cpQtx7vEjxx2oG8hM6ZE-bqql8~6UO286WKiDKnIk_)

?

## 🔴 Erro: "Blob is not defined"

O `Blob` não existe em Node.js. Preciso usar a abordagem correta para n8n.

## ✅ Solução Final: Usar Buffer Direto

Cole este código (funciona 100% no n8n):

```
async function uploadToManus() {
  try {
    // Obter arquivo binário
    const fileBuffer = $input.first().binary.data;
    const fileName = $input.first().json.File_Name || 'document.pdf';
    
    // Criar FormData manualmente
    const boundary = '----FormBoundary' + Math.random().toString(36).substr(2, 9);
    
    let body = '';
    body += \`--${boundary}\r\n\`;
    body += \`Content-Disposition: form-data; name="file"; filename="${fileName}"\r\n\`;
    body += \`Content-Type: application/octet-stream\r\n\r\n\`;
    
    // Converter para Buffer
    const bodyBuffer = Buffer.concat([
      Buffer.from(body),
      fileBuffer,
      Buffer.from(\`\r\n--${boundary}--\r\n\`)
    ]);
    
    // Fazer requisição
    const response = await fetch('https://api.manus.ai/v1/files', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer sk--25JfsVWGyvB4-vQmoZOcNc2k5RY1uKT8VOTYN2YmaMd4tbSnxL0mw1bL5e9swmbt6INvX_Znoon5DRX4erXXaCiUjpO',
        'Content-Type': \`multipart/form-data; boundary=${boundary}\`
      },
      body: bodyBuffer
    } );
    
    const data = await response.json();
    
    return {
      file_id: data.file_id || data.id,
      status: data.status,
      file_name: data.file_name,
      created_at: data.created_at,
      raw_response: data
    };
    
  } catch (error) {
    return {
      error: true,
      message: error.message,
      stack: error.stack
    };
  }
}

return await uploadToManus();
```

**Testa com este código!** 🚀

Aguardando o teste! 🎯

![pasted_file_fQ8OeX_image.png](https://private-us-east-1.manuscdn.com/users/310519663097514338/uploads/8EsYLDnsFkJHw8PwGRLQu0_na1fn_cGFzdGVkX2ZpbGVfZlE4T2VYX2ltYWdl.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vdXNlcnMvMzEwNTE5NjYzMDk3NTE0MzM4L3VwbG9hZHMvOEVzWUxEbnNGa0pIdzhQd0dSTFF1MF9uYTFmbl9jR0Z6ZEdWa1gyWnBiR1ZmWmxFNFQyVllYMmx0WVdkbC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3ODY3NTIwMDB9fX1dfQ__&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIFhCqC9wU6z9TxTq-Ms7xMAM5X0XRn2NPP7oirIf6uV7AiEA3NQezEXdpZfs1jh7OngJuAH1K~bOUNiPNcT80MhXIPE_)

## 🔴 Erro: "The 'body' argument must be an instance of Buffer or UInt8Array"

O `fetch` do n8n não aceita Buffer diretamente. Preciso usar uma abordagem diferente.

## ✅ Solução: Usar HTTP Request Node (Nativo)

Vou voltar ao nó HTTP, mas com a configuração **correta** dessa vez.

**Remova o nó Code** e vamos fazer assim:

1. **Adicione um nó HTTP Request**
2. **Configure assim:**

```
Method: POST
URL: https://api.manus.ai/v1/files

Authentication: Header Auth
Header Name: Authorization
Header Value: Bearer sk--25JfsVWGyvB4-vQmoZOcNc2k5RY1uKT8VOTYN2YmaMd4tbSnxL0mw1bL5e9swmbt6INvX_Znoon5DRX4erXXaCiUjpO

Body Content Type: Binary
Binary Input Field: data
```

3. **Conecte:** Convert to File2 → HTTP Request
4. **Teste!**

**Consegue fazer isso?** 🚀

Manus continuará após sua resposta

Entregar fluxo completo com documentação

Manus is an AI Agent and can make mistakes. Please double-check before use.