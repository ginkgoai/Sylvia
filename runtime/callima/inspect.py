import json, sys
src = r"C:\Users\User\AppData\Roaming\Claude\local-agent-mode-sessions\790be790-cc84-4df3-89f4-43b3c71eb1d0\46256cf7-526d-40e8-9315-4a02ccfdf7a1\local_ba76a008-5ae6-498c-8bdb-f21b2ab66095\uploads\Callima (1).json"
wf = json.load(open(src, encoding="utf-8"))
print("TOTAL NODES:", len(wf["nodes"]))
want = ["CRIAR LISTA MSG","BUSCA MSGS","APAGA MSG","ESPERA","AGRUPA MSG",
        "Intermediação Humana","Postgres Chat Memory","Finalize Track","Analyze document",
        "Callima","CODE1","Send Audio Brann","Dados1"]
byname = {n["name"]: n for n in wf["nodes"]}
for nm in want:
    n = byname.get(nm)
    if not n:
        print("\n### [FALTANDO]", nm); continue
    print("\n### NODE:", nm, "| type:", n["type"], "| tv:", n.get("typeVersion"))
    print(json.dumps(n.get("parameters", {}), ensure_ascii=False)[:1200])
print("\n=== CONNECTIONS (relevantes) ===")
for k in ["CRIAR LISTA MSG","ESPERA","BUSCA MSGS","AGRUPA MSG","APAGA MSG","Intermediação Humana","Analyze document","Finalize Track","Callima"]:
    if k in wf["connections"]:
        print(k, "->", json.dumps(wf["connections"][k], ensure_ascii=False)[:400])
