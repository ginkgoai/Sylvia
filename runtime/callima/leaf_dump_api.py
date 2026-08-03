#!/usr/bin/env python3
"""Dump dos workflows LEAF via n8n REST API (roda NO HOST — localhost:5678).

PRÉ-REQUISITO (1x): no n8n → Settings → "n8n API" → Create an API key → copie e
salve em C:\\sexta-feira\\callima\\.n8n_api.key (uma linha, gitignored).

Uso:  python C:\\sexta-feira\\callima\\leaf_dump_api.py
Saída: C:\\sexta-feira\\callima\\leaf_dump\\*.json  (nós + conexões; sem segredos no stdout)
"""
import os, re, json, urllib.request, urllib.error

BASE = os.environ.get("N8N_URL", "http://localhost:5678").rstrip("/")
KEYF = r"C:\sexta-feira\callima\.n8n_api.key"
OUT  = r"C:\sexta-feira\callima\leaf_dump"
LEAF = ["callima", "pix_link", "pix link", "content engine", "enviar midia",
        "enviar mídia", "brann actions", "audio fem", "audio brann"]

def main():
    if not os.path.exists(KEYF):
        print("!! Falta a API key. Crie no n8n (Settings > n8n API) e salve em:", KEYF); return
    key = open(KEYF, encoding="utf-8").read().strip()
    os.makedirs(OUT, exist_ok=True)

    def api(path):
        req = urllib.request.Request(BASE + path,
              headers={"X-N8N-API-KEY": key, "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=40) as r:
            return json.loads(r.read().decode("utf-8"))

    items, cursor = [], None
    while True:
        q = "/api/v1/workflows?limit=100" + (f"&cursor={cursor}" if cursor else "")
        d = api(q)
        items += d.get("data", [])
        cursor = d.get("nextCursor")
        if not cursor:
            break
    print("workflows na instância:", len(items))

    def is_leaf(nm):
        low = (nm or "").lower()
        return any(s in low for s in LEAF)

    dumped = []
    for w in items:
        nm, wid = w.get("name", ""), w.get("id")
        if not is_leaf(nm):
            continue
        full = api(f"/api/v1/workflows/{wid}")
        nodes = full.get("nodes", []) or []
        fn = re.sub(r"[^a-zA-Z0-9_-]+", "_", nm)[:40] + ".json"
        with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
            json.dump(full, f, ensure_ascii=False, indent=2)
        dumped.append(nm)
        print(f"  OK  {nm}  ({len(nodes)} nós) -> {fn}")

    print(f"\n{len(dumped)} fluxos LEAF exportados em {OUT}")
    if not dumped:
        print("nenhum casou o filtro; nomes vistos:", [w.get("name") for w in items][:40])

if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, e.reason, "->", e.read().decode("utf-8", "ignore")[:300])
        if e.code in (401, 403):
            print("Auth: confira a API key em", KEYF, "(Settings > n8n API no n8n).")
    except Exception as e:
        print(type(e).__name__, str(e))
