#!/usr/bin/env python3
"""Sexta-feira · cliente RAG (AnythingLLM) — Fase 1.

Consulta a memoria longa via AnythingLLM. Stdlib apenas (urllib).

Workspaces: 'sexta-feira' (proprio) e 'callima' (leitura do conhecimento de
vendas). NUNCA escreve/treina aqui — so consulta (mode=query).

Config: bridges/rag/.env -> ANYTHINGLLM_URL, ANYTHINGLLM_API_KEY
"""
import json
import os
import sys
import argparse
import urllib.request
import urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))


def load_env():
    cfg = {}
    p = os.path.join(HERE, ".env")
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    cfg[k.strip()] = v.strip()
    url = os.environ.get("ANYTHINGLLM_URL", cfg.get("ANYTHINGLLM_URL", "http://localhost:3001"))
    key = os.environ.get("ANYTHINGLLM_API_KEY", cfg.get("ANYTHINGLLM_API_KEY", ""))
    return url.rstrip("/"), key


def query(workspace, message):
    url, key = load_env()
    if not key:
        return {"ok": False, "error": "ANYTHINGLLM_API_KEY ausente. Preencha bridges/rag/.env"}
    endpoint = url + "/api/v1/workspace/" + workspace + "/chat"
    body = json.dumps({"message": message, "mode": "query"}).encode("utf-8")
    req = urllib.request.Request(endpoint, data=body, method="POST", headers={
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"ok": False, "error": "HTTP " + str(e.code) + ": " + e.read().decode("utf-8", "ignore")[:300]}
    except Exception as e:
        return {"ok": False, "error": type(e).__name__ + ": " + str(e)}
    # Resumo: resposta textual + fontes (citations), se houver
    answer = data.get("textResponse") or data.get("response") or ""
    sources = []
    for c in (data.get("sources") or []):
        sources.append({"title": c.get("title") or c.get("docId") or "fonte", "score": c.get("score")})
    return {"ok": True, "workspace": workspace, "answer": answer, "sources": sources}


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    p = argparse.ArgumentParser(description="Sexta-feira RAG (AnythingLLM) — query only")
    p.add_argument("workspace", help="slug do workspace (ex.: sexta-feira, callima)")
    p.add_argument("message", help="pergunta")
    a = p.parse_args()
    out = query(a.workspace, a.message)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    sys.exit(0 if out.get("ok") else 1)


if __name__ == "__main__":
    main()
