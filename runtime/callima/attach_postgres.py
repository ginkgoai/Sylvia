import sys, json
sys.path.insert(0, r"C:\sexta-feira\callima")
import n8n_mcp as m
m.init()
WF = "zo9FqQ9XVRcU8AJZ"

# acha credencial postgres
r = m.rpc("tools/call", {"name": "list_credentials", "arguments": {}})
creds = r["result"]["structuredContent"]["data"]
pg = next((c for c in creds if "postgres" in c["type"].lower()), None)
if not pg:
    print("POSTGRES NAO ENCONTRADA. Credenciais:", [(c["type"], c["name"]) for c in creds]); sys.exit(0)
print("Postgres cred:", pg["type"], pg["name"], pg["id"])

ops = [
    {"type": "setNodeCredential", "nodeName": "Postgres Chat Memory",
     "credentialKey": pg["type"], "credentialId": pg["id"], "credentialName": pg["name"]},
    {"type": "updateNodeParameters", "nodeName": "Postgres Chat Memory",
     "parameters": {"sessionIdType": "customKey",
                    "sessionKey": "={{ $('Dados1').item.json.NUMERO_LEAD }}"}},
]
r2 = m.rpc("tools/call", {"name": "update_workflow",
           "arguments": {"workflowId": WF, "operations": ops}})
print(json.dumps(r2.get("result", r2), ensure_ascii=False, indent=2)[:1500])
