import sys, json
sys.path.insert(0, r"C:\sexta-feira\callima")
import n8n_mcp as m
m.init()
WF = "zo9FqQ9XVRcU8AJZ"

dv = json.load(open(r"C:\sexta-feira\callima\humanized_delivery_fixed.json", encoding="utf-8"))
params = {n["name"]: n["parameters"] for n in dv["nodes"]}

# 6 nos com params corrigidos (replace=True). NAO mexe em Itera1/Espera1/Send Audio Brann params.
FIX = ["CODE1", "Audio Logic", "Typing Indicator", "Wait Typing", "Evolution1", "Send Audio?"]
ops = []
for nm in FIX:
    ops.append({"type": "updateNodeParameters", "nodeName": nm,
                "parameters": params[nm], "replace": True})

# religacao aditiva: audio enviado volta ao loop
ops.append({"type": "addConnection", "source": "Send Audio Brann", "target": "Itera1",
            "sourceIndex": 0, "targetIndex": 0, "connectionType": "main"})

r = m.rpc("tools/call", {"name": "update_workflow",
          "arguments": {"workflowId": WF, "operations": ops}})
res = r.get("result", r)
sc = res.get("structuredContent", {})
print("appliedOperations:", sc.get("appliedOperations"))
print("warnings:", len(sc.get("validationWarnings", [])))
for w in sc.get("validationWarnings", []):
    print("  -", w.get("nodeName"), ":", w.get("code"))
