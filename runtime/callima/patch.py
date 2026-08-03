#!/usr/bin/env python3
# Aplica correcoes estruturais VALIDAVEIS offline no workflow CALLIMA.
import json

SRC = r"C:\Users\User\AppData\Roaming\Claude\local-agent-mode-sessions\790be790-cc84-4df3-89f4-43b3c71eb1d0\46256cf7-526d-40e8-9315-4a02ccfdf7a1\local_ba76a008-5ae6-498c-8bdb-f21b2ab66095\uploads\Callima (1).json"
DELIV = r"C:\sexta-feira\callima\humanized_delivery_fixed.json"
OUT = r"C:\sexta-feira\callima\CALLIMA_corrigido.json"

wf = json.load(open(SRC, encoding="utf-8"))
dv = json.load(open(DELIV, encoding="utf-8"))

changes = []
byname = {n["name"]: i for i, n in enumerate(wf["nodes"])}
dv_nodes = {n["name"]: n for n in dv["nodes"]}

# 1+2+3+entrega: substitui os 9 nos do sub-fluxo de entrega pelos corrigidos
for nm, node in dv_nodes.items():
    if nm in byname:
        old = wf["nodes"][byname[nm]]
        node["position"] = old.get("position", node.get("position"))  # preserva posicao do canvas
        wf["nodes"][byname[nm]] = node
        changes.append(f"node corrigido: {nm}")
    else:
        wf["nodes"].append(node)
        changes.append(f"node adicionado: {nm}")

# substitui as conexoes do sub-fluxo de entrega (mantem todas as outras)
for k, v in dv["connections"].items():
    wf["connections"][k] = v
    changes.append(f"conexoes atualizadas: {k}")

# 3. Postgres Chat Memory: sessionKey por lead (NUMERO_LEAD)
if "Postgres Chat Memory" in byname:
    pm = wf["nodes"][byname["Postgres Chat Memory"]]
    pm["parameters"] = {
        "sessionIdType": "customKey",
        "sessionKey": "={{ $('Dados1').item.json.NUMERO_LEAD }}"
    }
    changes.append("Postgres Chat Memory: sessionKey = NUMERO_LEAD")

json.dump(wf, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK ->", OUT)
print("total nodes:", len(wf["nodes"]))
for c in changes:
    print(" -", c)
# valida
json.load(open(OUT, encoding="utf-8"))
print("JSON valido")
