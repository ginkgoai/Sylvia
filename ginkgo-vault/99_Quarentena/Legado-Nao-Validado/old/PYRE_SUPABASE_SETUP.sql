-- ==============================================================================
-- PYRE MVP — SUPABASE SETUP SCRIPT (PASSO 1)
-- Data: 21 de Abril de 2026
-- Autor: Manus AI
-- Descrição: Criação de tabelas, RLS, policies, triggers e funções para o Pyre.
-- Instruções: Copie todo este código e cole no SQL Editor do Supabase e clique em "Run".
-- ==============================================================================

-- 1. Habilitar extensões necessárias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgvector"; -- Para futura busca semântica de memória

-- ==============================================================================
-- 2. CRIAÇÃO DAS TABELAS
-- ==============================================================================

-- Tabela de Créditos e Planos do Usuário
CREATE TABLE IF NOT EXISTS public.user_credits (
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,
    balance INTEGER NOT NULL DEFAULT 30, -- 30 créditos iniciais (Trial)
    plan TEXT NOT NULL DEFAULT 'free',   -- 'free', 'creator', 'pro', 'studio'
    stripe_customer_id TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela de Conteúdo (A Memória do Agente)
CREATE TABLE IF NOT EXISTS public.content (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('image', 'video', 'audio', 'avatar', 'text')),
    user_prompt TEXT NOT NULL,           -- O que o usuário pediu originalmente
    agent_prompt TEXT,                   -- O prompt refinado pelo Claude
    api_used TEXT,                       -- 'nanobanana', 'seedance', 'heygen', 'elevenlabs'
    media_url TEXT,                      -- URL do arquivo gerado (armazenado no storage ou link externo)
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'completed', 'failed')),
    error_message TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela de Publicações (Orquestração com Postiz/Blotato)
CREATE TABLE IF NOT EXISTS public.publications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    content_id UUID REFERENCES public.content(id) ON DELETE CASCADE NOT NULL,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    networks TEXT[] NOT NULL,            -- Ex: ['instagram', 'tiktok']
    caption TEXT,                        -- Legenda gerada pelo agente
    scheduled_for TIMESTAMPTZ,           -- NULL significa publicação imediata
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'scheduled', 'published', 'failed')),
    postiz_id TEXT,                      -- ID retornado pela API do Postiz/Blotato
    error_message TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela de Regras de Automação (O Coração da Recorrência)
CREATE TABLE IF NOT EXISTS public.automation_rules (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    name TEXT NOT NULL,                  -- Ex: "Post diário de café"
    cron_expression TEXT NOT NULL,       -- Ex: "0 12 * * *" (Todo dia ao meio-dia)
    base_prompt TEXT NOT NULL,           -- A essência que o Claude usará para gerar variações
    networks TEXT[] NOT NULL,            -- Redes alvo
    is_active BOOLEAN DEFAULT TRUE,
    last_run_at TIMESTAMPTZ,
    next_run_at TIMESTAMPTZ,             -- Calculado pelo backend/n8n
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela de Histórico de Conversas (Memória de Curto Prazo do Pierre)
CREATE TABLE IF NOT EXISTS public.chat_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ==============================================================================
-- 3. ROW LEVEL SECURITY (RLS) E POLICIES
-- ==============================================================================

-- Habilitar RLS em todas as tabelas
ALTER TABLE public.user_credits ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.content ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.publications ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.automation_rules ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.chat_history ENABLE ROW LEVEL SECURITY;

-- Policies para user_credits (Usuário só vê o próprio saldo)
CREATE POLICY "Users can view own credits" ON public.user_credits
    FOR SELECT USING (auth.uid() = user_id);

-- Policies para content (Usuário só vê/cria/edita o próprio conteúdo)
CREATE POLICY "Users can view own content" ON public.content
    FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own content" ON public.content
    FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own content" ON public.content
    FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own content" ON public.content
    FOR DELETE USING (auth.uid() = user_id);

-- Policies para publications
CREATE POLICY "Users can view own publications" ON public.publications
    FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own publications" ON public.publications
    FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own publications" ON public.publications
    FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own publications" ON public.publications
    FOR DELETE USING (auth.uid() = user_id);

-- Policies para automation_rules
CREATE POLICY "Users can view own automation rules" ON public.automation_rules
    FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own automation rules" ON public.automation_rules
    FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own automation rules" ON public.automation_rules
    FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own automation rules" ON public.automation_rules
    FOR DELETE USING (auth.uid() = user_id);

-- Policies para chat_history
CREATE POLICY "Users can view own chat history" ON public.chat_history
    FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own chat history" ON public.chat_history
    FOR INSERT WITH CHECK (auth.uid() = user_id);

-- ==============================================================================
-- 4. TRIGGERS E FUNÇÕES AUTOMÁTICAS
-- ==============================================================================

-- Função para atualizar o updated_at automaticamente
CREATE OR REPLACE FUNCTION public.handle_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar trigger de updated_at nas tabelas
CREATE TRIGGER set_updated_at_user_credits
    BEFORE UPDATE ON public.user_credits
    FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

CREATE TRIGGER set_updated_at_content
    BEFORE UPDATE ON public.content
    FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

CREATE TRIGGER set_updated_at_publications
    BEFORE UPDATE ON public.publications
    FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

CREATE TRIGGER set_updated_at_automation_rules
    BEFORE UPDATE ON public.automation_rules
    FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- Função para criar a carteira de créditos automaticamente quando um usuário se cadastra
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.user_credits (user_id, balance, plan)
    VALUES (NEW.id, 30, 'free');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger que escuta a criação de usuários no auth.users
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- ==============================================================================
-- 5. STORAGE BUCKETS (Para mídias geradas)
-- ==============================================================================

-- Criar bucket para mídias do Pyre (se não existir)
INSERT INTO storage.buckets (id, name, public) 
VALUES ('pyre-media', 'pyre-media', true)
ON CONFLICT (id) DO NOTHING;

-- Policy para permitir que usuários façam upload para sua própria pasta no bucket
CREATE POLICY "Users can upload media to their folder" ON storage.objects
    FOR INSERT WITH CHECK (
        bucket_id = 'pyre-media' AND 
        auth.uid()::text = (storage.foldername(name))[1]
    );

-- Policy para permitir leitura pública das mídias
CREATE POLICY "Public media access" ON storage.objects
    FOR SELECT USING (bucket_id = 'pyre-media');

-- ==============================================================================
-- FIM DO SCRIPT
-- ==============================================================================
