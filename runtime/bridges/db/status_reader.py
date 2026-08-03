#!/usr/bin/env python3
"""Sexta-feira · leitor READ-ONLY de sexta.status_events (Fase 1).

Le a fonte de verdade de status/consumo/jobs. NUNCA escreve/edita/apaga
(o role sexta_app nem tem permissao). Usa `docker exec psql` no container
ai-stack-postgres — sem dependencia Python extra.

Senha do role sexta_app: lida de C:\\sexta-feira\\.sexta_db_pw.txt
"""
import json
import os
import sys
import argparse
import subprocess

PW_FILE = r"C:\sexta-feira\.sexta_db_pw.txt"
CONTAINER = "ai-stack-postgres"
DB = "aistack_db"
USER = "sexta_app"
SEP = "\x1f"


def load_pw():
    try:
        with open(PW_FILE, "r", encoding="utf-8") as fh:
            for line in fh:
                if "=" in line:
                    return line.split("=", 1)[1].strip()
    except FileNotFoundError:
        pass
    return os.environ.get("SEXTA_DB_PASSWORD", "")


def run_sql(sql):
    pw = load_pw()
    if not pw:
        return None, "Senha de sexta_app ausente (.sexta_db_pw.txt)"
    cmd = ["docker", "exec", "-e", "PGPASSWORD=" + pw, CONTAINER,
           "psql", "-U", USER, "-d", DB, "-t", "-A", "-F", SEP, "-c", sql]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
    except Exception as e:
        return None, type(e).__name__ + ": " + str(e)
    if r.returncode != 0:
        return None, (r.stderr or r.stdout).strip()[:300]
    return r.stdout.strip(), None


COLS = ["created_at", "source", "status", "job_ref", "cost_usd", "tokens_in", "tokens_out"]


def cmd_recent(a):
    where = []
    if a.source:
        where.append("source = " + sql_lit(a.source))
    if a.status:
        where.append("status = " + sql_lit(a.status))
    wsql = (" WHERE " + " AND ".join(where)) if where else ""
    sql = ("SELECT created_at, source, status, coalesce(job_ref,''), "
           "coalesce(cost_usd::text,''), coalesce(tokens_in::text,''), "
           "coalesce(tokens_out::text,'') FROM sexta.status_events"
           + wsql + " ORDER BY created_at DESC LIMIT " + str(int(a.limit)) + ";")
    out, err = run_sql(sql)
    if err:
        return {"ok": False, "error": err}
    rows = []
    for line in (out.splitlines() if out else []):
        if not line.strip():
            continue
        parts = line.split(SEP)
        rows.append(dict(zip(COLS, parts)))
    return {"ok": True, "count": len(rows), "events": rows}


def cmd_summary(a):
    sql = ("SELECT source, status, count(*) FROM sexta.status_events "
           "WHERE created_at > now() - interval '" + str(int(a.hours)) + " hours' "
           "GROUP BY source, status ORDER BY source, status;")
    out, err = run_sql(sql)
    if err:
        return {"ok": False, "error": err}
    summary = []
    for line in (out.splitlines() if out else []):
        if not line.strip():
            continue
        s, st, c = line.split(SEP)
        summary.append({"source": s, "status": st, "count": int(c)})
    return {"ok": True, "window_hours": a.hours, "summary": summary}


def sql_lit(v):
    return "'" + str(v).replace("'", "''") + "'"


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    p = argparse.ArgumentParser(description="Sexta-feira status_events reader (read-only)")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("recent")
    s.add_argument("--limit", type=int, default=20)
    s.add_argument("--source", default=None)
    s.add_argument("--status", default=None)
    s.set_defaults(fn=cmd_recent)
    s = sub.add_parser("summary")
    s.add_argument("--hours", type=int, default=24)
    s.set_defaults(fn=cmd_summary)
    a = p.parse_args()
    out = a.fn(a)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    sys.exit(0 if out.get("ok") else 1)


if __name__ == "__main__":
    main()
