-- Sexta-feira · Fase 1 · contrato §5
-- Fonte única de verdade para status/consumo/jobs. APPEND-ONLY.
-- Roda no Postgres do stack leaf (aistack_db). Schema dedicado: sexta.

CREATE SCHEMA IF NOT EXISTS sexta;

CREATE TABLE IF NOT EXISTS sexta.status_events (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source      TEXT NOT NULL,          -- 'n8n' | 'bullmq' | 'claude_api' | 'claude_code' | 'hermes'
  job_ref     TEXT,                   -- id de execução / workflow / run
  status      TEXT NOT NULL,          -- 'queued'|'running'|'done'|'failed'|'awaiting_approval'
  cost_usd    NUMERIC(10,4),          -- nullable; preenchido p/ chamadas Claude
  tokens_in   INTEGER,                -- nullable
  tokens_out  INTEGER,                -- nullable
  payload     JSONB,                  -- detalhe livre
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_status_events_source_created
  ON sexta.status_events (source, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_status_events_status
  ON sexta.status_events (status);
