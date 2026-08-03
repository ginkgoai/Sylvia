# PYRE — Master Architecture & Implementation Plan

**Versão:** 2.0 (Evolução para Agente Conversacional Multicanal)  
**Data:** 21 de Abril de 2026  
**Autor:** Manus AI (Engenheiro de Automação e IA)  
**Status:** 🏗️ Arquitetura Validada e Pronta para Build

---

## 1. Visão Geral do Produto

O **Pyre** evoluiu de um simples aplicativo utilitário para um **Agente Conversacional Multicanal** (estilo Pierre). Ele não é apenas uma interface de botões; é um "copiloto criativo" com personalidade, memória persistente e capacidade de automação autônoma.

**Proposta de Valor (MVP):**
O usuário conversa com o Pyre (por texto ou áudio) para criar, editar, agendar e automatizar publicações em redes sociais. O Pyre entende a intenção, escolhe a melhor API (NanoBanana, Seedance, HeyGen), gera o conteúdo, pede aprovação e orquestra a publicação via Postiz/Blotato.

**Diferencial Competitivo:**
- **Memória Evolutiva:** Lembra do estilo preferido do usuário ("faz igual aquele post de terça").
- **Automação por Prompt:** "Posta todo dia ao meio-dia um conteúdo com essa base, mas autêntico".
- **Interface Conversacional:** Áudio bidirecional (ElevenLabs) e texto.

---

## 2. Arquitetura do Sistema (Stack Validada)

A arquitetura foi desenhada para ser escalável, modular e baseada em APIs especializadas, mantendo o custo sob controle através de um roteador inteligente.

### 2.1. O Cérebro (Roteador Inteligente)
- **Gemma 4 (Local/Grátis):** Classificação de intenção (O que o usuário quer? Criar imagem? Agendar? Áudio?).
- **Claude Sonnet 3.5:** Geração de prompts refinados para as APIs de mídia e criação de legendas.
- **Claude Opus 4.7:** Raciocínio complexo, análise de contexto longo e memória evolutiva (buscar referências passadas).

### 2.2. Os Músculos (APIs de Geração)
- **NanoBanana (Gemini 3.1 Flash Image):** Geração e edição de imagens (Text-to-Image, Image-to-Image).
- **Seedance 2.0:** Geração de vídeos curtos (Text-to-Video, Image-to-Video).
- **HeyGen:** Geração de vídeos com avatares e lip-sync.
- **ElevenLabs:** Síntese de voz (TTS) para a personalidade do agente e narração de vídeos.

### 2.3. Os Braços (Publicação e Automação)
- **Postiz / Blotato:** Orquestração de publicação em 30+ redes sociais (Instagram, TikTok, LinkedIn, etc.).
- **n8n:** Motor de automação de fluxos complexos (cron jobs, webhooks, integrações externas).

### 2.4. A Infraestrutura (Backend & Dados)
- **Supabase:** Banco de dados PostgreSQL (dados de usuários, histórico, automações) + Auth + Storage.
- **Fastify (Node.js):** Backend leve e rápido para gerenciar as rotas da API.
- **BullMQ + Redis:** Fila de processamento assíncrono para lidar com geração de mídia e agendamentos.
- **Stripe:** Pagamentos, assinaturas e tokenização de créditos.

---

## 3. Fluxos de Operação Core

### 3.1. Fluxo de Criação Conversacional
1. **Input:** Usuário envia áudio ou texto ("Cria uma imagem de um café e posta amanhã às 8h").
2. **Transcrição:** Se áudio, ElevenLabs/Whisper transcreve.
3. **Roteamento (Gemma 4):** Identifica intenção `[Tipo: Imagem, Ação: Criar, Agendamento: Amanhã 08:00]`.
4. **Refinamento (Claude Sonnet):** Gera o prompt técnico para a API.
5. **Geração:** Backend chama NanoBanana API.
6. **Resposta (ElevenLabs):** Agente responde em áudio: "Estou preparando seu café, monsieur. Só um instante."
7. **Aprovação:** App exibe a imagem gerada. Usuário aprova.
8. **Agendamento:** Backend envia payload para Postiz/Blotato agendar a publicação.

### 3.2. Fluxo de Automação Recorrente (O Diferencial)
1. **Input:** "Posta todo dia ao meio-dia uma dica de marketing com a mesma base visual."
2. **Processamento (Claude Opus):** Entende a regra de recorrência e o padrão visual desejado.
3. **Banco de Dados:** Salva a regra na tabela `automation_rules` (Cron: `0 12 * * *`).
4. **Execução (n8n / BullMQ):** Todo dia às 12:00, o worker acorda.
5. **Variação:** Claude Sonnet gera uma variação autêntica do prompt base.
6. **Geração & Publicação:** Cria a mídia (NanoBanana/Seedance) e publica via Postiz.

### 3.3. Fluxo de Memória Evolutiva
1. **Input:** "Faz igual aquele post da semana passada, mas muda a cor para azul."
2. **Busca Semântica:** Consulta no Supabase (pgvector) pelo histórico do usuário.
3. **Recuperação:** Encontra o prompt original e a imagem de referência.
4. **Adaptação (Claude Opus):** Modifica o prompt mantendo a essência e alterando a cor.
5. **Geração:** Executa a criação com o novo prompt.

---

## 4. Schema de Banco de Dados (Supabase)

O schema foi otimizado para suportar o MVP e a memória do agente.

```sql
-- Tabela de Conteúdo (Memória do Agente)
CREATE TABLE content (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users NOT NULL,
  type TEXT NOT NULL,             -- 'image', 'video', 'audio', 'avatar'
  user_prompt TEXT,               -- O que o usuário pediu
  agent_prompt TEXT,              -- O prompt refinado pelo Claude
  api_used TEXT,                  -- 'nanobanana', 'seedance', 'heygen'
  media_url TEXT,                 -- URL do arquivo gerado
  status TEXT DEFAULT 'pending',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela de Publicações
CREATE TABLE publications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content_id UUID REFERENCES content NOT NULL,
  user_id UUID REFERENCES auth.users NOT NULL,
  networks TEXT[] NOT NULL,       -- ['instagram', 'tiktok']
  caption TEXT,
  scheduled_for TIMESTAMPTZ,      -- NULL = imediato
  status TEXT DEFAULT 'pending',
  postiz_id TEXT,                 -- ID de referência na API de publicação
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela de Automações (O "Coração" da Recorrência)
CREATE TABLE automation_rules (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users NOT NULL,
  name TEXT,
  cron_expression TEXT NOT NULL,  -- Ex: "0 12 * * *"
  base_prompt TEXT NOT NULL,      -- A "base" que o usuário quer manter
  networks TEXT[] NOT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  last_run_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela de Créditos (Economia do App)
CREATE TABLE user_credits (
  user_id UUID REFERENCES auth.users PRIMARY KEY,
  balance INTEGER NOT NULL DEFAULT 30,
  plan TEXT DEFAULT 'free',
  stripe_customer_id TEXT
);
```

---

## 5. Economia de Tokens e Custos (Stripe)

O modelo de negócios baseia-se em uma assinatura mensal + pacotes de créditos (tokenização).

**Custo por Ação (Estimativa Interna):**
- Classificação (Gemma 4): 0 créditos
- Geração de Imagem (NanoBanana): 15 créditos
- Geração de Vídeo (Seedance): 80 créditos
- Vídeo com Avatar (HeyGen): 50 créditos
- Áudio TTS (ElevenLabs): 10 créditos
- Publicação (Postiz): 2 créditos

**Planos (Stripe):**
- **Free:** 30 créditos (Trial)
- **Criador:** R$ 29,90/mês (300 créditos)
- **Pro:** R$ 79,90/mês (1.000 créditos)
- **Studio:** R$ 149,90/mês (3.000 créditos)

---

## 6. Roadmap de Implementação (Zero to Deploy)

Para garantir que o MVP seja entregue rápido e sem bloqueios, a ordem de construção deve ser estrita:

### Fase 1: Fundação Backend & Cérebro (Semana 1)
- Setup do Supabase (Tabelas, RLS, Auth).
- Setup do Fastify + BullMQ + Redis.
- Implementação do Roteador Inteligente (Gemma 4 + Claude Sonnet).
- Integração com ElevenLabs para a "voz" do agente.

### Fase 2: Integração de Mídia (Semana 2)
- Integração NanoBanana API (Imagens).
- Integração Seedance API (Vídeos).
- Testes de geração via chamadas REST (Postman/Insomnia).

### Fase 3: Publicação & Automação (Semana 3)
- Integração Postiz API (Conexão de contas e publicação).
- Implementação do motor de Cron Jobs (BullMQ) para ler a tabela `automation_rules`.
- Testes de agendamento e postagem recorrente.

### Fase 4: App Mobile (Expo/React Native) (Semana 4)
- Setup do Expo Router.
- Tela de Chat (Interface principal com o agente, suporte a áudio/texto).
- Tela de Preview (Aprovação de mídia gerada).
- Tela de Automações (Gerenciar regras ativas).

### Fase 5: Monetização & Deploy (Semana 5)
- Integração Stripe (Assinaturas e controle de créditos).
- Testes End-to-End no celular físico.
- Submissão para Google Play Store.

---

## 7. Próximos Passos Imediatos

A arquitetura está validada. As APIs estão confirmadas. O próximo passo prático é iniciar a **Fase 1**.

Como seu engenheiro copiloto, recomendo que comecemos pelo **Setup do Backend e do Banco de Dados (Supabase)**, pois ele será a espinha dorsal de todo o roteamento e memória do agente.
