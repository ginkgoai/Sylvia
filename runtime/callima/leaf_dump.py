#!/usr/bin/env python3
"""Exporta os workflows da 'pasta LEAF' do n8n (ai-stack :5678) para JSON, via o
MCP local (reusa n8n_mcp.py). Roda NO HOST (localhost:5678). Uso:
    python C:\\sexta-feira\\callima\\leaf_dump.py
Saída: C:\\sexta-feira\\callima\\leaf_dump\\<nome>.json (a Sexta-feira lê e verifica nó-a-nó).
Sem segredos no output — só nomes/estrutura.
"""
import sys, os, re, json
sys.path.insert(0, r"C:\sexta-feira\callima")
import n8n_mcp as m

OUT = r"C:\sexta-feira\callima\leaf_dump"
os.makedirs(OUT, exist_ok=True)
# nomes que consideramos "LEAF" (case-insensitive, substring)
LEAF = ["callima", "pix_link", "pix link", "content engine", "enviar midia",
        "enviar mídia", "brann actions", "audio fem", "audio brann"]

m.init()
tools = (m.rpc("tools/list", {}) or {}).get("result", {}).get("tools", [])
names = [t.get("name", "") for t in tools]

def pick(*subs):
    for n in names:
        low = n.lower()
        if all(s in low for s in subs):
            return n
    return None

list_tool = pick("list", "workflow") or pick("workflows") or pick("search", "workflow")
get_tool  = pick("get", "workflow") or pick("workflow", "get")

if not list_tool or not get_tool:
    print("!! Não identifiquei as tools de workflow. Cole isto pra Sexta-feira:")
    for t in tools:
        print("  -", t.get("name"), "::", (t.get("description") or "")[:90])
    sys.exit(0)

print(f"list_tool={list_tool}  get_tool={get_tool}")

def unwrap(r):
    sc = (r or {}).get("result", {})
    if isinstance(sc, dict) and "structuredContent" in sc:
        return sc["structuredContent"]
    c = sc.get("content", []) if isinstance(sc, dict) else []
    if c and isinstance(c[0], dict) and c[0].get("type") == "text":
        try: return json.loads(c[0]["text"])
        except Exception: return c[0]["text"]
    return sc

def call(tool, args):
    return unwrap(m.rpc("tools/call", {"name": tool, "arguments": args}))

lst = call(list_tool, {})
wfs = lst.get("data", lst) if isinstance(lst, dict) else lst
if not isinstance(wfs, list):
    print("!! Resposta inesperada do list. Bruto:", json.dumps(lst, ensure_ascii=False)[:600]); sys.exit(0)
print(f"workflows na instância: {len(wfs)}")

def is_leaf(nm):
    low = (nm or "").lower()
    return any(s in low for s in LEAF)

def get_full(wid):
    for key in ("id", "workflowId", "workflowID"):
        full = call(get_tool, {key: wid})
        if isinstance(full, dict) and (full.get("nodes") or full.get("data")):
            return full
    return full

dumped = []
for w in wfs:
    nm, wid = w.get("name", ""), w.get("id")
    if not is_leaf(nm):
        continue
    full = get_full(wid)
    nodes = full.get("nodes") if isinstance(full, dict) else None
    if nodes is None and isinstance(full, dict):
        nodes = (full.get("data") or {}).get("nodes")
    fn = re.sub(r"[^a-zA-Z0-9_-]+", "_", nm)[:40] + ".json"
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        json.dump(full, f, ensure_ascii=False, indent=2)
    n = len(nodes) if isinstance(nodes, list) else "?"
    dumped.append((nm, n))
    print(f"  ✓ {nm}  ({n} nós) -> {fn}")

print(f"\nOK: {len(dumped)} fluxos LEAF em {OUT}")
if not dumped:
    print("(nenhum casou os nomes LEAF — me manda o print do list que eu ajusto o filtro)")
