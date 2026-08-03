# PYRE — Guia de Configuração Manual e Fluxos n8n

**Data:** 21 de Abril de 2026  
**Autor:** Manus AI (Engenheiro de Automação e IA)  
**Status:** 📋 Mapeamento Concluído

Este documento detalha exatamente a divisão de responsabilidades entre a IA (eu, Manus) e você (Gabriel) para a construção do Pyre, com foco especial nos fluxos do n8n e integrações externas.

---

## 1. O Estado Atual do Repositório (`ginkgo-pyre`)

Analisei o repositório atual. Ele contém:
- **App Mobile (Expo/React Native):** Uma tela inicial básica (`index.tsx`) com um input de texto para o prompt.
- **Backend (Fastify):** Uma rota `/generate` que usa Claude Haiku para rotear a intenção e salva no Supabase.
- **Gaps Identificados:** Não há fluxos n8n no repositório atual do Pyre. A lógica de automação recorrente e a integração com Postiz/Blotato ainda precisam ser construídas.

No entanto, analisando seus outros repositórios (`ginkgo-platform`, `ginkgo-leaf`), identifiquei o padrão arquitetural que você usa:
- **Worker Queues (Redis/BullMQ):** Para processamento assíncrono.
- **n8n como "Músculo":** Usado via webhooks (`N8nToolExecutor`) para executar ações externas.

---

## 2. Divisão de Responsabilidades (IA vs. Gabriel)

Como seu copiloto operador, eu vou escrever o código, configurar o banco e estruturar a arquitetura. Você precisará atuar nas configurações de ambiente, chaves de API e setup visual do n8n.

### 🤖 O que a IA (Manus) vai fazer:
1. **Supabase:** Criar as tabelas (`content`, `publications`, `automation_rules`, `user_credits`), configurar RLS (Row Level Security) e policies.
2. **Backend (Fastify):** 
   - Atualizar o roteador inteligente para usar Gemma 4 (via API) e Claude Opus.
   - Criar os endpoints de webhook para o n8n se comunicar com o backend.
   - Implementar a lógica de débito de tokens (reaproveitando o padrão do `tokenRouter.ts` do Ginkgo Platform).
3. **App Mobile:** Desenvolver as telas de Chat (interface estilo Pierre), Preview de Mídia e Gerenciamento de Automações.
4. **Integração de APIs (Código):** Escrever os services no backend para chamar NanoBanana, Seedance, HeyGen e ElevenLabs.

### 👨‍💻 O que VOCÊ (Gabriel) precisa fazer:

#### A. Configuração de Ambiente (Variáveis)
Você precisará criar o arquivo `.env` no backend e no n8n com as seguintes chaves (eu te darei o template exato na hora do deploy):
- `SUPABASE_URL` e `SUPABASE_SERVICE_KEY`
- `ANTHROPIC_API_KEY` (Claude)
- `ELEVENLABS_API_KEY`
- `HEYGEN_API_KEY`
- `NANOBANANA_API_KEY`
- `BLOTATO_API_KEY` ou `POSTIZ_API_KEY`
- `STRIPE_SECRET_KEY` e `STRIPE_WEBHOOK_SECRET`

#### B. Configuração do n8n (A sua principal tarefa manual)
Como o n8n é uma ferramenta visual, eu desenharei a arquitetura lógica dos fluxos, mas você precisará importá-los/criá-los na sua instância do n8n.

**Serão necessários 3 Fluxos Principais no n8n:**

1. **Fluxo 1: O Motor de Recorrência (Cron Job)**
   - **Trigger:** Schedule Trigger (rodando a cada 1 hora).
   - **Ação:** Faz um GET no backend do Pyre (`/api/automations/pending`) para buscar quais regras de automação precisam rodar naquela hora.
   - **Processamento:** Para cada regra, chama o Claude para gerar a variação do prompt, chama a API de mídia (NanoBanana/Seedance) e agenda no Postiz.
   - **Por que você faz:** Precisa configurar o nó HTTP Request com a URL do seu backend em produção.

2. **Fluxo 2: Webhook de Publicação (Postiz/Blotato)**
   - **Trigger:** Webhook (recebe o payload do backend do Pyre quando o usuário clica em "Aprovar e Postar").
   - **Ação:** Conecta com o nó nativo do Postiz/Blotato (ou via HTTP Request) para efetuar a postagem nas redes sociais.
   - **Por que você faz:** Você precisará autenticar suas contas de redes sociais (Instagram, TikTok, etc.) dentro do n8n ou no painel do Postiz/Blotato. A IA não tem acesso aos seus logins sociais.

3. **Fluxo 3: Webhook de Pagamento (Stripe)**
   - **Trigger:** Stripe Trigger (eventos `invoice.paid`, `checkout.session.completed`).
   - **Ação:** Atualiza o saldo de créditos do usuário no Supabase.
   - **Por que você faz:** Precisa conectar sua conta Stripe no n8n.

#### C. Contas e Credenciais Externas
- **Postiz / Blotato:** Você precisará criar a conta, conectar as redes sociais de teste e gerar a API Key.
- **Google AI Studio:** Gerar a API Key para usar o Gemma 4 gratuitamente.

---

## 3. Próximos Passos Práticos

Para começarmos a "colocar a mão na massa", o fluxo ideal é:

1. **Passo 1 (IA):** Eu gero o script SQL completo para você rodar no Supabase e criar toda a estrutura de banco de dados necessária para o Pyre MVP.
2. **Passo 2 (IA):** Eu reescrevo o backend (`server.ts` e rotas) para suportar a nova arquitetura e te entrego o código.
3. **Passo 3 (Gabriel):** Você sobe o backend, configura as variáveis de ambiente e testa a rota de geração.
4. **Passo 4 (Gabriel/IA):** Eu te dou o JSON dos fluxos do n8n, você importa na sua instância e conecta as credenciais.

Se estiver de acordo com essa divisão de tarefas e com os 3 fluxos do n8n mapeados, me dê o "ok" e eu já gero o script SQL do Supabase (Passo 1) para começarmos o build!
