import json, urllib.request, uuid
cfg={}
for line in open(r"C:\sexta-feira\bridges\n8n\.env",encoding="utf-8"):
    line=line.strip()
    if line and not line.startswith("#") and "=" in line:
        k,v=line.split("=",1); cfg[k.strip()]=v.strip()
BASE=cfg["N8N_API_URL"].rstrip("/"); KEY=cfg["N8N_API_KEY"]
def req(method,path,body=None):
    data=json.dumps(body).encode() if body is not None else None
    r=urllib.request.Request(BASE+path,data=data,method=method,
        headers={"X-N8N-API-KEY":KEY,"Accept":"application/json","Content-Type":"application/json"})
    return json.loads(urllib.request.urlopen(r,timeout=40).read().decode())

WF="oeAXd3LE30lzOIor"
def nid(): return str(uuid.uuid4())

start={"parameters":{},"type":"n8n-nodes-base.executeWorkflowTrigger","typeVersion":1.1,
  "position":[2600,1850],"id":nid(),"name":"Start"}
hook={"parameters":{"httpMethod":"POST","path":"enviar-midia-test","responseMode":"lastNode","options":{}},
  "type":"n8n-nodes-base.webhook","typeVersion":2,"position":[2600,2080],"id":nid(),
  "name":"Test Webhook","webhookId":nid()}
prep={"parameters":{"assignments":{"assignments":[
    {"id":nid(),"name":"instance","type":"string","value":"={{ $json.body ? $json.body.instance : $json.instance }}"},
    {"id":nid(),"name":"phone","type":"string","value":"={{ $json.body ? $json.body.phone : $json.phone }}"},
    {"id":nid(),"name":"media","type":"string","value":"={{ $json.body ? $json.body.media : $json.media }}"},
    {"id":nid(),"name":"caption","type":"string","value":"={{ $json.body ? $json.body.caption : $json.caption }}"}
  ]},"options":{}},"type":"n8n-nodes-base.set","typeVersion":3.4,
  "position":[2860,1960],"id":nid(),"name":"Prep"}
ev={"parameters":{"resource":"messages-api","operation":"send-image",
    "instanceName":"={{ $json.instance }}","remoteJid":"={{ $json.phone }}",
    "media":"={{ $json.media }}","caption":"={{ $json.caption }}","options_message":{"delay":1200}},
  "type":"n8n-nodes-evolution-api.evolutionApi","typeVersion":1,"position":[3120,1960],
  "id":nid(),"name":"Evolution Send Image",
  "credentials":{"evolutionApi":{"id":"tWl4eIzULkFUsVvg","name":"Evolution account"}}}
note={"parameters":{"content":"## ENVIAR MIDIA\nEnvia midia existente (catalogo) via Evolution send-image.\nTool da Callima: passa instance, phone, media(URL), caption.\nFuturo: resolver rotulo->URL via media_assets (Supabase) antes do envio.\nTest Webhook: POST /webhook/enviar-midia-test {instance,phone,media,caption}","height":260,"width":420},
  "type":"n8n-nodes-base.stickyNote","typeVersion":1,"position":[2560,1560],"id":nid(),"name":"Doc"}

nodes=[start,hook,prep,ev,note]
conns={
  "Start":{"main":[[{"node":"Prep","type":"main","index":0}]]},
  "Test Webhook":{"main":[[{"node":"Prep","type":"main","index":0}]]},
  "Prep":{"main":[[{"node":"Evolution Send Image","type":"main","index":0}]]}
}
payload={"name":"ENVIAR MIDIA","nodes":nodes,"connections":conns,"settings":{"executionOrder":"v1"}}
out=req("PUT","/workflows/"+WF,payload)
print("PUT ok:",out.get("name"),"nodes:",len(out.get("nodes",[])))
act=req("POST","/workflows/"+WF+"/activate")
print("active:",act.get("active"))
