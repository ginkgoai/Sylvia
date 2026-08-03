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
d=g("/workflows?limit=100")
hits=[]
for w in d["data"]:
    full=g("/workflows/"+w["id"])
    for n in full["nodes"]:
        if n["type"]=="n8n-nodes-evolution-api.evolutionApi":
            op=n.get("parameters",{}).get("operation")
            if op and op!="send-audio" and op!="send-text":
                hits.append((w["name"],n["name"],op,n["parameters"]))
print("FOUND",len(hits))
for h in hits[:6]:
    print("---",h[0],"/",h[1],"op=",h[2])
    print(json.dumps(h[3],ensure_ascii=False)[:1200])
