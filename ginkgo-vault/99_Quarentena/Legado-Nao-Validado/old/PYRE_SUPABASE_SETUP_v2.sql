-- ==============================================================================
-- PYRE MVP — SUPABASE SETUP SCRIPT v2 (CORRIGIDO)
-- Data: 21 de Abril de 2026
-- Correção: Removido pgvector (não disponível no plano Free). Memória semântica = Fase 2.
-- Instruções: Cole no SQL Editor do Supabase e clique em "Run".
-- ==============================================================================

-- 1. Habilitar extensão uuid (já vem ativa na maioria dos projetos, mas garantimos)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ==============================================================================
-- 2. CRIAÇÃO DAS TABELAS
-- ==============================================================================

-- Tabela de Créditos e Planos do Usuário
CREATE TABLE IF NOT EXISTS public.user_credits (
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,
    balance INTEGER NOT NULL DEFAULT 30,
    plan TEXT NOT NULL DEFAULT 'free',
    stripe_customer_id TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela de Conteúdo (A Memória do Agente)
CREATE TABLE IF NOT EXISTS public.content (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('image', 'video', 'audio', 'avatar', 'text')),
    user_prompt TEXT NOT NULL,
    agent_prompt TEXT,
    api_used TEXT,
    media_url TEXT,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'completed', 'failed')),
    error_message TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela de Publicações
CREATE TABLE IF NOT EXISTS public.publications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    content_id UUID REFERENCES public.content(id) ON DELETE CASCADE NOT NULL,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    networks TEXT[] NOT NULL,
    caption TEXT,
    scheduled_for TIMESTAMPTZ,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'scheduled', 'published', 'failed')),
    postiz_id TEXT,
    error_message TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela de Regras de Automação (Recorrência)
CREATE TABLE IF NOT EXISTS public.automation_rules (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    name TEXT NOT NULL,
    cron_expression TEXT NOT NULL,
    base_prompt TEXT NOT NULL,
    networks TEXT[] NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_run_at TIMESTAMPTZ,
    next_run_at TIMESTAMPTZ,
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

ALTER TABLE public.user_credits ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.content ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.publications ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.automation_rules ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.chat_history ENABLE ROW LEVEL SECURITY;

-- Policies: user_credits
CREATE POLICY "Users can view own credits" ON public.user_credits
    FOR SELECT USING (auth.uid() = user_id);

-- Policies: content
CREATE POLICY "Users can view own content" ON public.content
    FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own content" ON public.content
    FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own content" ON public.content
    FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own content" ON public.content
    FOR DELETE USING (auth.uid() = user_id);

-- Policies: publications
CREATE POLICY "Users can view own publications" ON public.publications
    FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own publications" ON public.publications
    FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own publications" ON public.publications
    FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own publications" ON public.publications
    FOR DELETE USING (auth.uid() = user_id);

-- Policies: automation_rules
CREATE POLICY "Users can view own automation rules" ON public.automation_rules
    FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own automation rules" ON public.automation_rules
    FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own automation rules" ON public.automation_rules
    FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own automation rules" ON public.automation_rules
    FOR DELETE USING (auth.uid() = user_id);

-- Policies: chat_history
CREATE POLICY "Users can view own chat history" ON public.chat_history
    FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own chat history" ON public.chat_history
    FOR INSERT WITH CHECK (auth.uid() = user_id);

-- ==============================================================================
-- 4. TRIGGERS E FUNÇÕES
-- ==============================================================================

-- Função para atualizar updated_at automaticamente
CREATE OR REPLACE FUNCTION public.handle_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

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

-- Função: cria carteira de créditos automaticamente ao cadastrar usuário
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.user_credits (user_id, balance, plan)
    VALUES (NEW.id, 30, 'free');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- ==============================================================================
-- 5. STORAGE BUCKET para mídias geradas
-- ==============================================================================

INSERT INTO storage.buckets (id, name, public)
VALUES ('pyre-media', 'pyre-media', true)
ON CONFLICT (id) DO NOTHING;

CREATE POLICY "Users can upload to own folder" ON storage.objects
    FOR INSERT WITH CHECK (
        bucket_id = 'pyre-media' AND
        auth.uid()::text = (storage.foldername(name))[1]
    );

CREATE POLICY "Public media read access" ON storage.objects
    FOR SELECT USING (bucket_id = 'pyre-media');

-- ==============================================================================
-- FIM DO SCRIPT v2
-- ==============================================================================
