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
w=rq("GET","/workflows/oeAXd3LE30lzOIor")
for n in w["nodes"]:
    if n["name"]=="Start":
        n["parameters"]={"workflowInputs":{"values":[{"name":"instance"},{"name":"phone"},{"name":"media"},{"name":"caption"}]}}
pl={"name":w["name"],"nodes":w["nodes"],"connections":w["connections"],"settings":{"executionOrder":"v1"}}
putres=rq("PUT","/workflows/oeAXd3LE30lzOIor",pl)
print("put",json.dumps(putres)[:400])
print("act",rq("POST","/workflows/oeAXd3LE30lzOIor/activate"))
