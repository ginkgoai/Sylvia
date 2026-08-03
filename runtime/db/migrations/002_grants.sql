-- Sexta-feira · Fase 1 · least-privilege para status_events
-- Regra §5: Sexta-feira NUNCA tem UPDATE/DELETE. Só INSERT (append) + SELECT (leitura).
-- Role dedicada usada pelas bridges (n8n writer / Hermes reader).
-- Troque a senha via :'sexta_pw' ao aplicar (psql -v sexta_pw='...').

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'sexta_app') THEN
    CREATE ROLE sexta_app LOGIN PASSWORD 'CHANGE_ME_sexta';
  END IF;
END$$;

GRANT USAGE ON SCHEMA sexta TO sexta_app;
GRANT SELECT, INSERT ON sexta.status_events TO sexta_app;
-- Explicitamente NÃO concede UPDATE/DELETE/TRUNCATE.
REVOKE UPDATE, DELETE, TRUNCATE ON sexta.status_events FROM sexta_app;

-- Garante o default em objetos futuros do schema (defensivo).
ALTER DEFAULT PRIVILEGES IN SCHEMA sexta GRANT SELECT, INSERT ON TABLES TO sexta_app;
