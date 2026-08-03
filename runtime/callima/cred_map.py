import json, collections
src = r"C:\Users\User\AppData\Roaming\Claude\local-agent-mode-sessions\790be790-cc84-4df3-89f4-43b3c71eb1d0\46256cf7-526d-40e8-9315-4a02ccfdf7a1\local_ba76a008-5ae6-498c-8bdb-f21b2ab66095\uploads\Callima (1).json"
wf = json.load(open(src, encoding="utf-8"))

# tipos de no que NAO usam credencial (utilitarios)
NO_CRED = {"n8n-nodes-base.set", "n8n-nodes-base.code", "n8n-nodes-base.if",
           "n8n-nodes-base.switch", "n8n-nodes-base.wait", "n8n-nodes-base.splitInBatches",
           "n8n-nodes-base.noOp", "n8n-nodes-base.executeWorkflow", "n8n-nodes-base.webhook",
           "n8n-nodes-base.executeWorkflowTrigger", "n8n-nodes-base.stickyNote",
           "n8n-nodes-base.convertToFile", "n8n-nodes-base.extractFromFile",
           "@n8n/n8n-nodes-langchain.agent", "@n8n/n8n-nodes-langchain.toolThink",
           "@n8n/n8n-nodes-langchain.toolCalculator", "@n8n/n8n-nodes-langchain.toolWorkflow",
           "@n8n/n8n-nodes-langchain.toolHttpRequest"}

rows = []
for n in wf["nodes"]:
    t = n["type"]
    creds = n.get("credentials", {})
    if t in NO_CRED and not creds:
        continue
    if creds:
        for ctype, c in creds.items():
            rows.append((ctype, n["name"], t, "ANEXADA: " + c.get("name", "?")))
    elif t not in NO_CRED:
        rows.append(("?", n["name"], t, "FALTA"))

rows.sort()
print("%-26s | %-28s | %s" % ("CRED TYPE", "NODE", "STATUS"))
print("-" * 90)
for ctype, name, t, st in rows:
    print("%-26s | %-28s | %s  [%s]" % (ctype, name[:28], st, t.split('.')[-1]))
print("\nTotal nos que tocam credencial:", len(rows))
