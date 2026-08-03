import json, urllib.request, urllib.error, uuid
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
        return {"ERR":e.code,"body":e.read().decode()[:400]}
def nid(): return str(uuid.uuid4())

sysmsg=("Você é o Pyre, gerador de conteúdo da Ginkgo AI Systems. Escreva 1 post de "
        "LinkedIn B2B em português, tom humano e técnico. Hook forte na 1a linha, corpo "
        "com 1 ideia clara, CTA no fim, no máximo 3 hashtags.")
jb=("={{ JSON.stringify({ model: 'google/gemini-2.0-flash-001', messages: ["
    "{ role: 'system', content: " + json.dumps(sysmsg, ensure_ascii=False) + " }, "
    "{ role: 'user', content: 'Pilar: ' + $json.pilar + ' | Tema: ' + $json.tema + "
    "' | Ângulo: ' + $json.angulo + ' | CTA: ' + $json.cta } ] }) }}")

schedule={"parameters":{"rule":{"interval":[{"field":"weeks"}]}},"type":"n8n-nodes-base.scheduleTrigger","typeVersion":1.2,"position":[2400,1900],"id":nid(),"name":"Schedule Semanal"}
brief={"parameters":{"assignments":{"assignments":[
    {"id":nid(),"name":"org_id","type":"string","value":"DEFINIR_ORG_GINKGO"},
    {"id":nid(),"name":"pilar","type":"string","value":"Educar"},
    {"id":nid(),"name":"tema","type":"string","value":"IA aplicada a atendimento no WhatsApp"},
    {"id":nid(),"name":"angulo","type":"string","value":"Quanto custa um lead que espera 3h por resposta"},
    {"id":nid(),"name":"cta","type":"string","value":"Comente AGENTE que eu te mostro como"},
    {"id":nid(),"name":"canal","type":"string","value":"linkedin"}
]},"options":{}},"type":"n8n-nodes-base.set","typeVersion":3.4,"position":[2620,1900],"id":nid(),"name":"Brief"}
pyre={"parameters":{"method":"POST","url":"https://openrouter.ai/api/v1/chat/completions",
    "authentication":"predefinedCredentialType","nodeCredentialType":"openRouterApi",
    "sendBody":True,"specifyBody":"json","jsonBody":jb,"options":{}},
    "type":"n8n-nodes-base.httpRequest","typeVersion":4.2,"position":[2840,1900],"id":nid(),
    "name":"Pyre — Gerar Post","credentials":{"openRouterApi":{"id":"XxZ9pd0yUms0f8w7","name":"OpenRouter account"}}}
extrair={"parameters":{"assignments":{"assignments":[
    {"id":nid(),"name":"post","type":"string","value":"={{ $json.choices[0].message.content }}"}
]},"options":{}},"type":"n8n-nodes-base.set","typeVersion":3.4,"position":[3060,1900],"id":nid(),"name":"Extrair Texto"}
insert={"parameters":{"operation":"executeQuery",
    "query":"INSERT INTO brann_actions (org_id, type, channel, payload, status, requires_hitl) VALUES ($1::uuid, 'social_post', 'linkedin', jsonb_build_object('text', $2::text, 'pilar', $3::text, 'tema', $4::text), 'pending', true) RETURNING id;",
    "options":{"queryReplacement":"={{ $('Brief').item.json.org_id }},={{ $json.post }},={{ $('Brief').item.json.pilar }},={{ $('Brief').item.json.tema }}"}},
    "type":"n8n-nodes-base.postgres","typeVersion":2.6,"position":[3280,1900],"id":nid(),
    "name":"Inserir Rascunho (HITL)","credentials":{"postgres":{"id":"zp3JG0Ln3Dd9ZJ8F","name":"Supabase LEAF"}}}
note={"parameters":{"content":"## Content Engine — LinkedIn (esqueleto)\nSchedule -> Brief -> Pyre(OpenRouter) -> Extrair -> Inserir Rascunho (brann_actions, social_post, pending=HITL).\nINATIVO. Falta: credito OpenRouter + definir org_id da Ginkgo no Brief.\nDepois: 'Social Publisher' (consumer) le aprovados -> Postiz publica.\nFuturo: Brief vem de content_calendar (Supabase) + tendencias; Atomizador p/ IG/Reels/X.","height":320,"width":460},
    "type":"n8n-nodes-base.stickyNote","typeVersion":1,"position":[2360,1560],"id":nid(),"name":"Doc"}
postiz={"parameters":{"content":"## Postiz Publish (pos-aprovacao)\nNAO inline aqui (violaria o HITL). Sera um consumer separado que pega\nbrann_actions status=approved type=social_post -> POST Postiz API -> publica.\nEspelha o 'LEAF - Brann Actions Consumer' (email).","height":220,"width":420},
    "type":"n8n-nodes-base.stickyNote","typeVersion":1,"position":[3260,1560],"id":nid(),"name":"DocPostiz"}

nodes=[schedule,brief,pyre,extrair,insert,note,postiz]
conns={
 "Schedule Semanal":{"main":[[{"node":"Brief","type":"main","index":0}]]},
 "Brief":{"main":[[{"node":"Pyre — Gerar Post","type":"main","index":0}]]},
 "Pyre — Gerar Post":{"main":[[{"node":"Extrair Texto","type":"main","index":0}]]},
 "Extrair Texto":{"main":[[{"node":"Inserir Rascunho (HITL)","type":"main","index":0}]]}
}
payload={"name":"Content Engine — LinkedIn","nodes":nodes,"connections":conns,"settings":{"executionOrder":"v1"}}
out=rq("POST","/workflows",payload)
print(json.dumps(out)[:400] if "ERR" in out else ("CRIADO id="+out.get("id","?")+" name="+out.get("name","?")+" active="+str(out.get("active"))))
