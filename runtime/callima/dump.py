import sys, json
sys.path.insert(0, r"C:\sexta-feira\callima")
import n8n_mcp as m
m.init()
# creds
r = m.rpc("tools/call", {"name": "list_credentials", "arguments": {}})
sc = r["result"]["structuredContent"]["data"]
print("=== CREDENCIAIS ===")
for c in sc:
    print(f'{c["type"]:<22} | {c["name"]:<28} | {c["id"]}')
# schema do update_workflow
tl = m.rpc("tools/list", {})
for t in tl["result"]["tools"]:
    if t["name"] == "update_workflow":
        print("\n=== update_workflow inputSchema ===")
        print(json.dumps(t.get("inputSchema", {}), ensure_ascii=False)[:2500])
