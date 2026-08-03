import json, urllib.request, urllib.error
cfg={}
for line in open(r"C:\sexta-feira\bridges\n8n\.env",encoding="utf-8"):
    line=line.strip()
    if line and not line.startswith("#") and "=" in line:
        k,v=line.split("=",1); cfg[k.strip()]=v.strip()
BASE=cfg["N8N_API_URL"].rstrip("/"); KEY=cfg["N8N_API_KEY"]
def rq(m,p,b=None):
    d=json.dumps(b).encode() if b is not None else None
    r=urllib.request.Request(BASE+p,data=d,method=m,headers={"X-N8N-API-KEY":KEY,"Accept":"application/json","Content-Type":"application/json"})
    try:
        return json.loads(urllib.request.urlopen(r,timeout=40).read().decode())
    except urllib.error.HTTPError as e:
        return {"ERR":e.code,"body":e.read().decode()[:300]}
ORG="6696c0e0-b24b-42cc-8595-83e42d530fbc"
w=rq("GET","/workflows/k82S6bzBEqtIU5ps")
for n in w["nodes"]:
    if n["name"]=="Brief":
        for a in n["parameters"]["assignments"]["assignments"]:
            if a["name"]=="org_id": a["value"]=ORG
pl={"name":w["name"],"nodes":w["nodes"],"connections":w["connections"],"settings":{"executionOrder":"v1"}}
print("put", rq("PUT","/workflows/k82S6bzBEqtIU5ps",pl).get("name","ERR"))
