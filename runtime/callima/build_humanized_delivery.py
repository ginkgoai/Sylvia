#!/usr/bin/env python3
# Gera o JSON corrigido do sub-fluxo de entrega humanizada da CALLIMA.
import json

CODE1 = r"""
// QUEBRA NATURAL DE MENSAGENS â€” Brann v3 (corrigido)
// Carrega instance/remoteJid/full_message em CADA bloco para sobreviver
// aos nos da Evolution que sobrescrevem o $json.
const MAX_CHARS = 280;
const out = [];
const dados = ($('Dados1').first() && $('Dados1').first().json) || {};

for (const item of items) {
  const text = (item.json.text || item.json.message || item.json.output || '').trim();
  const instance = item.json.instance || dados.INSTANCIA;            // CONFIRMAR campo em 'Dados'
  const remoteJid = item.json.remoteJid || dados.remoteJid || dados.NUMERO_LEAD; // CONFIRMAR
  const fullMessage = text;
  if (!text) { continue; }

  let blocos = [];
  const porParagrafo = text.split(/\n{2,}/).map(b => b.trim()).filter(Boolean);
  if (porParagrafo.length > 1) {
    blocos = porParagrafo;
  } else if (text.length > MAX_CHARS) {
    const frases = text.split(/(?<=[.!?])\s+(?=[A-ZAEIOUAEOAOC])/);
    let cur = '';
    for (const f of frases) {
      if ((cur + ' ' + f).trim().length > MAX_CHARS && cur.length > 0) { blocos.push(cur.trim()); cur = f; }
      else { cur = cur ? cur + ' ' + f : f; }
    }
    if (cur.trim()) blocos.push(cur.trim());
  } else {
    blocos = [text];
  }

  const finais = [];
  for (const b of blocos) {
    if (b.length <= MAX_CHARS) { finais.push(b); continue; }
    let r = b;
    while (r.length > MAX_CHARS) {
      let cut = r.lastIndexOf(' ', MAX_CHARS);
      if (cut < MAX_CHARS * 0.5) cut = MAX_CHARS;
      finais.push(r.slice(0, cut).trim());
      r = r.slice(cut).trim();
    }
    if (r) finais.push(r);
  }

  for (let i = 0; i < finais.length; i++) {
    const palavras = finais[i].split(' ').length;
    const base = Math.min(Math.max(palavras * 0.9 * 1000 / 45 * 0.0 + palavras * 90, 1500), 9000);
    const jitter = Math.floor(Math.random() * 800);
    out.push({ json: {
      message: finais[i],
      sequence_index: i,
      total_messages: finais.length,
      is_last: i === finais.length - 1,
      instance, remoteJid,
      full_message: fullMessage,
      typing_delay: Math.floor(base + jitter)
    }});
  }
}
return out;
"""

AUDIO = r"""
// LOGICA DE AUDIO ESTRATEGICO (corrigido: le o bloco do loop, audio = msg completa)
const item = $('Itera1').item.json;
const mensagem = item.full_message || item.message || '';
const isLast = item.is_last === true;
const palavras = mensagem.split(' ').length;
const temLink = mensagem.includes('http') || mensagem.includes('buy.stripe');
const temCodigo = mensagem.includes('```') || mensagem.includes('//');
const temSubstancia = palavras >= 15;
const chance = Math.random() < 0.40;
const deveUsarAudio = isLast && temSubstancia && !temLink && !temCodigo && chance;
return [{ json: { ...item, usar_audio: deveUsarAudio, audio_text: deveUsarAudio ? mensagem : null } }];
"""


II = "$('Itera1').item.json"

nodes = [
    {"parameters": {"jsCode": CODE1}, "type": "n8n-nodes-base.code", "typeVersion": 2,
     "position": [4400, 464], "id": "0ac11def-9c59-4e24-9089-dad22adef116", "name": "CODE1"},

    {"parameters": {"options": {}}, "type": "n8n-nodes-base.splitInBatches", "typeVersion": 3,
     "position": [4624, 464], "id": "709403f2-ea63-4472-8ef8-1ca071c88cb2", "name": "Itera1"},

    {"parameters": {"resource": "messages-api", "operation": "send-presence-update",
                    "instanceName": "={{ " + II + ".instance }}",
                    "remoteJid": "={{ " + II + ".remoteJid }}",
                    "presence": "composing"},
     "type": "n8n-nodes-evolution-api.evolutionApi", "typeVersion": 1,
     "position": [4848, 400], "id": "f991d240-94c8-47d3-a633-85e5df52f7cd", "name": "Typing Indicator"},

    {"parameters": {"amount": "={{ " + II + ".typing_delay || 2000 }}", "unit": "milliseconds"},
     "type": "n8n-nodes-base.wait", "typeVersion": 1.1, "position": [5072, 400],
     "id": "3c2762f8-b16a-49c3-9d73-e28459638561", "name": "Wait Typing", "webhookId": "wait-typing-wh-001"},

    {"parameters": {"resource": "messages-api",
                    "instanceName": "={{ " + II + ".instance }}",
                    "remoteJid": "={{ " + II + ".remoteJid }}",
                    "messageText": "={{ " + II + ".message }}", "options_message": {}},
     "type": "n8n-nodes-evolution-api.evolutionApi", "typeVersion": 1,
     "position": [5296, 400], "id": "e94d462d-c08c-4832-96a0-d936126306fd", "name": "Evolution1"},

    {"parameters": {"amount": 2}, "type": "n8n-nodes-base.wait", "typeVersion": 1.1,
     "position": [5520, 400], "id": "21cba347-9e29-4808-add7-d700585debc1", "name": "Espera1",
     "webhookId": "3e8b366c-90b6-4bea-baf0-8ba8805ae813"},

    {"parameters": {"jsCode": AUDIO}, "type": "n8n-nodes-base.code", "typeVersion": 2,
     "position": [5744, 400], "id": "94844c8f-2ae0-4ea1-992f-773b67a75bb5", "name": "Audio Logic"},

    {"parameters": {"conditions": {"options": {"caseSensitive": True, "leftValue": "",
        "typeValidation": "loose", "version": 2}, "conditions": [{"id": "audio-cond-001",
        "leftValue": "={{ $json.usar_audio }}", "rightValue": "",
        "operator": {"type": "boolean", "operation": "true", "singleValue": True}}],
        "combinator": "and"}, "looseTypeValidation": True, "options": {}},
     "type": "n8n-nodes-base.if", "typeVersion": 2.2, "position": [5968, 464],
     "id": "416360f9-8939-4d90-b3e0-38e7d3a4b75e", "name": "Send Audio?"},

    {"parameters": {"workflowId": {"__rl": True, "value": "8EoLKO7wdhv0ZLgz", "mode": "list",
        "cachedResultUrl": "/workflow/8EoLKO7wdhv0ZLgz", "cachedResultName": "AUDIO BRANN"},
        "options": {}}, "type": "n8n-nodes-base.executeWorkflow", "typeVersion": 1.1,
     "position": [6192, 464], "id": "282668ee-ca0d-4061-94e3-872d4d631309", "name": "Send Audio Brann"},
]

def m(node, idx=0):
    return [[{"node": node, "type": "main", "index": idx}]]

connections = {
    "CODE1": {"main": m("Itera1")},
    # Loop Over Items v3: saida 0 = done (vazio) | saida 1 = loop (processa)
    "Itera1": {"main": [[], [{"node": "Typing Indicator", "type": "main", "index": 0}]]},
    "Typing Indicator": {"main": m("Wait Typing")},
    "Wait Typing": {"main": m("Evolution1")},
    "Evolution1": {"main": m("Espera1")},
    "Espera1": {"main": m("Audio Logic")},
    "Audio Logic": {"main": m("Send Audio?")},
    "Send Audio?": {"main": [
        [{"node": "Send Audio Brann", "type": "main", "index": 0}],  # true
        [{"node": "Itera1", "type": "main", "index": 0}],            # false -> proximo bloco
    ]},
    "Send Audio Brann": {"main": m("Itera1")},                       # audio enviado -> volta ao loop
}

wf = {"nodes": nodes, "connections": connections, "pinData": {},
      "meta": {"instanceId": "99d625cdfb8d5ab9f002be9e31912dab6405fca9bca8a8ceb35969e664aaa88f"}}

out_path = r"C:\sexta-feira\callima\humanized_delivery_fixed.json"
with open(out_path, "w", encoding="utf-8") as fh:
    json.dump(wf, fh, ensure_ascii=False, indent=2)
print("OK ->", out_path)
print("nodes:", len(nodes))

