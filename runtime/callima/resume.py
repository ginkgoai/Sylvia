#!/usr/bin/env python3
"""RESUME — 1 comando de recontexto + health do n8n MCP.
Uso: python C:\\sexta-feira\\callima\\resume.py
Mostra: onde paramos (STATE.md) + ultimo checkpoint + saude do n8n MCP
(versao, Callima ativa?, credenciais). Se der 401 = token expirado.
"""
import sys, os, glob, json, urllib.error
sys.path.insert(0, r"C:\sexta-feira\callima")

MEM = r"C:\sexta-feira\memory"

def head(path, n=40):
    try:
        with open(path, encoding="utf-8") as f:
            return "".join(f.readlines()[:n])
    except Exception as e:
        return f"(sem {path}: {e})"

print("=" * 70)
print("ONDE PARAMOS  (memory/STATE.md)")
print("=" * 70)
print(head(os.path.join(MEM, "STATE.md"), 60))

cps = sorted(glob.glob(os.path.join(MEM, "checkpoints", "*.md")))
print("ULTIMO CHECKPOINT:", os.path.basename(cps[-1]) if cps else "(nenhum)")

print("\n" + "=" * 70)
print("HEALTH n8n MCP")
print("=" * 70)
try:
    import n8n_mcp as m
    init = m._post({"jsonrpc": "2.0", "id": 1, "method": "initialize",
                    "params": {"protocolVersion": "2024-11-05", "capabilities": {},
                               "clientInfo": {"name": "resume", "version": "1"}}})
    try:
        m._post({"jsonrpc": "2.0", "method": "notifications/initialized"}, notify=True)
    except Exception:
        pass
    sv = init.get("result", {}).get("serverInfo", {})
    print("OK -", sv.get("name"), sv.get("version"))
    wf = m.rpc("tools/call", {"name": "search_workflows", "arguments": {"query": "Callima"}})
    d = wf["result"]["structuredContent"]["data"]
    if d:
        print(f"Callima: id={d[0]['id']} active={d[0]['active']}")
    cr = m.rpc("tools/call", {"name": "list_credentials", "arguments": {}})
    cl = cr["result"]["structuredContent"]["data"]
    print("Credenciais (%d):" % len(cl), ", ".join(c["name"] for c in cl))
except urllib.error.HTTPError as e:
    if e.code in (401, 403):
        print("TOKEN EXPIRADO/INVALIDO (HTTP %d)." % e.code)
        print("-> n8n Settings -> Instance-level MCP -> Connection details -> Access token")
        print("-> cole o novo em C:\\sexta-feira\\callima\\.n8n_mcp.token e rode de novo.")
    else:
        print("HTTP", e.code, e.read().decode("utf-8", "ignore")[:300])
except Exception as e:
    print("FALHA:", type(e).__name__, str(e), "(n8n no ar? localhost:5678)")
