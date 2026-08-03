#!/usr/bin/env python3
"""Sexta-feira Â· cliente READ-ONLY da API REST do n8n (Fase 1).

Stdlib apenas (urllib) â€” roda em qualquer Python 3.

SeguranÃ§a (spec Â§3.4):
  - Leitura: list-executions / get-execution / list-workflows / get-workflow.
  - trigger-workflow: DRY-RUN por padrÃ£o. SÃ³ executa com --confirm,
    e ainda assim apenas declara a intenÃ§Ã£o (nÃ£o dispara sem webhook
    explÃ­cito). Nada irreversÃ­vel acontece sem confirmaÃ§Ã£o.

Config: lÃª N8N_API_URL e N8N_API_KEY de bridges/n8n/.env (mesmo diretÃ³rio)
ou das variÃ¡veis de ambiente.
"""
import json
import os
import sys
import argparse
import urllib.request
import urllib.error
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))


def load_env():
    cfg = {}
    envp = os.path.join(HERE, ".env")
    if os.path.exists(envp):
        with open(envp, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                cfg[k.strip()] = v.strip()
    url = os.environ.get("N8N_API_URL", cfg.get("N8N_API_URL", "http://localhost:5678/api/v1"))
    key = os.environ.get("N8N_API_KEY", cfg.get("N8N_API_KEY", ""))
    return url.rstrip("/"), key


def api_get(path, params=None):
    url, key = load_env()
    if not key:
        return {"ok": False, "error": "N8N_API_KEY ausente. Preencha bridges/n8n/.env"}
    full = url + path
    if params:
        full += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(full, headers={"X-N8N-API-KEY": key, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return {"ok": True, "data": json.loads(resp.read().decode("utf-8"))}
    except urllib.error.HTTPError as e:
        return {"ok": False, "error": f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:300]}"}
    except Exception as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}"}


def cmd_list_executions(a):
    return api_get("/executions", {"status": a.status, "limit": a.limit, "workflowId": a.workflow})


def cmd_get_execution(a):
    return api_get(f"/executions/{a.id}", {"includeData": "true"})


def cmd_list_workflows(a):
    return api_get("/workflows", {"limit": a.limit, "active": a.active})


def cmd_get_workflow(a):
    return api_get(f"/workflows/{a.id}")


def cmd_trigger_workflow(a):
    # GATE: dry-run por padrÃ£o. Nada dispara sem --confirm.
    intent = {"action": "trigger_workflow", "workflow_id": a.id, "dry_run": not a.confirm}
    if not a.confirm:
        intent["message"] = ("DRY-RUN: disparo NAO executado. Declare a intencao ao "
                             "fundador e rode com --confirm apos aprovacao explicita.")
        return {"ok": True, "data": intent}
    intent["message"] = ("CONFIRMADO. Disparo real exige a webhook URL do workflow "
                         "(nao ha endpoint publico de 'run' arbitrario no n8n). "
                         "Acione o webhook do workflow ou ative-o manualmente.")
    return {"ok": True, "data": intent}


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    p = argparse.ArgumentParser(description="Sexta-feira n8n read-only client")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("list-executions"); s.add_argument("--status", choices=["error", "success", "waiting"], default=None)
    s.add_argument("--limit", type=int, default=20); s.add_argument("--workflow", default=None); s.set_defaults(fn=cmd_list_executions)

    s = sub.add_parser("get-execution"); s.add_argument("id"); s.set_defaults(fn=cmd_get_execution)

    s = sub.add_parser("list-workflows"); s.add_argument("--limit", type=int, default=50)
    s.add_argument("--active", choices=["true", "false"], default=None); s.set_defaults(fn=cmd_list_workflows)

    s = sub.add_parser("get-workflow"); s.add_argument("id"); s.set_defaults(fn=cmd_get_workflow)

    s = sub.add_parser("trigger-workflow"); s.add_argument("id")
    s.add_argument("--confirm", action="store_true"); s.set_defaults(fn=cmd_trigger_workflow)

    a = p.parse_args()
    out = a.fn(a)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    sys.exit(0 if out.get("ok") else 1)


if __name__ == "__main__":
    main()

