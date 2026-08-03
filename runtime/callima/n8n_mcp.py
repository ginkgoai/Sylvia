#!/usr/bin/env python3
"""Cliente MCP (Streamable HTTP) para o n8n MCP Server — dirigido pelo host.
Uso:
  python n8n_mcp.py tools
  python n8n_mcp.py call <tool_name> '<json_args>'
Token: lido de C:\\sexta-feira\\callima\\.n8n_mcp.token
"""
import json, sys, urllib.request, urllib.error

URL = "http://localhost:5678/mcp-server/http"
TOKEN = open(r"C:\sexta-feira\callima\.n8n_mcp.token", encoding="utf-8").read().strip()
SESSION = {"id": None}


def _post(payload, notify=False):
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": "Bearer " + TOKEN,
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if SESSION["id"]:
        headers["Mcp-Session-Id"] = SESSION["id"]
    req = urllib.request.Request(URL, data=data, method="POST", headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        sid = resp.headers.get("Mcp-Session-Id") or resp.headers.get("mcp-session-id")
        if sid:
            SESSION["id"] = sid
        body = resp.read().decode("utf-8")
    if notify:
        return None
    # parse SSE ou json
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("data:"):
            return json.loads(line[5:].strip())
    return json.loads(body) if body.strip() else None


def init():
    _post({"jsonrpc": "2.0", "id": 1, "method": "initialize",
           "params": {"protocolVersion": "2024-11-05", "capabilities": {},
                      "clientInfo": {"name": "host-cli", "version": "1.0"}}})
    try:
        _post({"jsonrpc": "2.0", "method": "notifications/initialized"}, notify=True)
    except Exception:
        pass


def rpc(method, params, rid=2):
    return _post({"jsonrpc": "2.0", "id": rid, "method": method, "params": params})


def main():
    init()
    if len(sys.argv) < 2:
        print("uso: tools | call <name> <jsonargs>"); return
    cmd = sys.argv[1]
    if cmd == "tools":
        r = rpc("tools/list", {})
        tools = (r or {}).get("result", {}).get("tools", [])
        print("TOOLS (%d):" % len(tools))
        for t in tools:
            print(" -", t.get("name"), "::", (t.get("description") or "")[:90])
    elif cmd == "call":
        name = sys.argv[2]
        args = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
        r = rpc("tools/call", {"name": name, "arguments": args})
        print(json.dumps(r, ensure_ascii=False, indent=2)[:6000])
    elif cmd == "resources":
        r = rpc("resources/list", {})
        print(json.dumps(r, ensure_ascii=False, indent=2)[:4000])
    else:
        print("comando desconhecido")


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, e.read().decode("utf-8", "ignore")[:500])
    except Exception as e:
        print(type(e).__name__, str(e))
