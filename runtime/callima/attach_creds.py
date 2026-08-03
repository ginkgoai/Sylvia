import sys, json
sys.path.insert(0, r"C:\sexta-feira\callima")
import n8n_mcp as m
m.init()

WF = "zo9FqQ9XVRcU8AJZ"

def sc(node, key, cid, cname):
    return {"type": "setNodeCredential", "nodeName": node,
            "credentialKey": key, "credentialId": cid, "credentialName": cname}

EVO = ("evolutionApi", "tWl4eIzULkFUsVvg", "Evolution account")
RED = ("redis", "7jA7FDW5kyJrZb01", "Redis Callima")
ANT = ("anthropicApi", "FmcBEbsrAPrHxSCG", "Anthropic account")

ops = []
for n in ["Ler", "Typing Indicator", "Evolution1", "Evolution2"]:
    ops.append(sc(n, *EVO))
for n in ["CRIAR LISTA MSG", "BUSCA MSGS", "APAGA MSG"]:
    ops.append(sc(n, *RED))
ops.append(sc("Analyze document", *ANT))

r = m.rpc("tools/call", {"name": "update_workflow",
          "arguments": {"workflowId": WF, "operations": ops}})
print(json.dumps(r.get("result", r), ensure_ascii=False, indent=2)[:3000])
