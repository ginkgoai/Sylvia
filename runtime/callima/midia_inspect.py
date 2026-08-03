import json, urllib.request
cfg={}
for line in open(r"C:\sexta-feira\bridges\n8n\.env",encoding="utf-8"):
    line=line.strip()
    if line and not line.startswith("#") and "=" in line:
        k,v=line.split("=",1); cfg[k.strip()]=v.strip()
BASE=cfg["N8N_API_URL"].rstrip("/"); KEY=cfg["N8N_API_KEY"]

def g(path):
    req=urllib.request.Request(BASE+path,headers={"X-N8N-API-KEY":KEY,"Accept":"application/json"})
    return json.loads(urllib.request.urlopen(req,timeout=30).read().decode())

wf=g("/workflows/oeAXd3LE30IzOIor")
print("== ENVIAR MIDIA ==", wf.get("name"), "active:", wf.get("active"))
for n in wf["nodes"]:
    print("NODE:", n["name"], "|", n["type"], "v"+str(n.get("typeVersion")))
print("\n== Evolution node detail ==")
for n in wf["nodes"]:
    if "evolution" in n["type"].lower() or "Evolution" in n["name"]:
        print(json.dumps(n, ensure_ascii=False, indent=1)[:2500])
