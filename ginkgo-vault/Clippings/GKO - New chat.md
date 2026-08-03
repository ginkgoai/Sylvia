---
title: "GKO - New chat"
source: "https://chatgpt.com/g/g-p-68c232d960748191b8826de2fe1ff36f/c/690adb2b-f4c0-832a-9ed1-5993fac803dc"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
qua., 5 de nov. às 2:05

Sobre a Nyra, vi um template n8n que copia vídeos/Reels virais, podemos configurar esse template e colocar ele em uma plataforma conversacional por linguagem natural usando lovable? A pessoa manda quero um vídeo igual a esse pro meu negócio e a automação retorna um vídeo viral estilo o q foi recebido só que autenticado para a pessoa. Também podemos implementar automações como clipagem de vídeos longos e posts automáticos, tudo junto

Sim. Arquitetura viável com n8n + Lovable + Nyra. Abaixo o desenho enxuto e os blocos prontos para você colar e montar.

## Visão do sistema

Entrada NL → Lovable (app conversacional) → Webhook n8n (Job) → Sub-workflows Nyra:

1. “Replica Viral” ético
2. “Clipagem Longa → Shorts”
3. “Postagem automática”

Saída: MP4 vertical 9:16 com legendas, capa, descrição, CTAs, variantes e link para download. Opcional: publicação direta.

---

## Fluxo 1 — “Replica Viral” ético (não plagiar)

**Ideia:** extrair estrutura e elementos de estilo do vídeo referência e gerar um novo roteiro e edição com branding do cliente.

## Etapas no n8n

1. **Webhook In** `POST /nyra/jobs`
	- Recebe JSON (ver “Schema do Job”).
2. **Validar/Normalizar** (Function)
	- Checa URL, preferências, permissões de uso.
3. **Baixar Referência** (Command/HTTP Request)
	- `yt-dlp` ou serviço externo. Saída: MP4 + metadados.
4. **Transcrição e Captação de Estrutura**
	- Transcrever áudio → texto.
		- “Parser de estilo”: detectar *hook*, bullets, pacing, número de cortes, tempo médio por cena, uso de captions, música, CTA.
5. **Resumo e Roteiro Original** (LLM)
	- Prompt: “Gerar roteiro novo, mesmo nicho, mesmo *pacing*, ganchos diferentes, CTA própria, zero cópia de frases.”
6. **Geração de Assets**
	- Legendas: SRT/ASS do novo roteiro.
		- B-roll: busca por termos do roteiro (biblioteca própria, stock livre, assets do cliente).
		- Música: biblioteca royalty-free.
		- Branding: cores, logo, @handle, moldura.
7. **Montagem** (FFmpeg + filtros)
	- Layout 9:16, cortes na cadência do estilo, *jump cuts*, *auto-reframe*, *loudness normalize*, *burn-in* de legendas.
8. **Capa (thumbnail)** (LLM + gerador de imagem opcional)
	- Título curto + arte com marca.
9. **Qualidade** (Function)
	- Duração 20–35s, bitrate alvo, loudness -14 LUFS, legibilidade fonte > 42 px em 1080x1920.
10. **Export** (Supabase Storage)
	- MP4 final + SRT + thumb + descrição.
11. **Retorno/Status**
	- URL de download + *metadata* + legenda pronta.

---

## Fluxo 2 — “Clipagem Longa → Shorts”

1. **Upload/Link do vídeo longo**
2. **Transcrição** → **Detecção de highlights** (regra + LLM)
	- Sinais: picos de entonação, palavras-chave, risos, perguntas, insights.
3. **Segmentação** (PySceneDetect/FFmpeg) + **Roteirização curta**
4. **Edição automática** 9:16 com cortes, *zoom punch-in*, *auto-captions*, moldura e CTA.
5. **Lote**: até N shorts por vídeo, cada um com título, descrição e *tags*.

---

## Fluxo 3 — “Postagem automática”

- **Planejador**: agenda por plataforma.
- **Publicadores**:
	- Instagram Reels: Graph API com conta Comercial.
		- YouTube Shorts: YouTube Data API.
		- TikTok: Open API “Direct Post”.
- **Fallback**: se token ausente, gerar *package* (MP4 + descrição + checklist) e enviar no WhatsApp/Email para postar manualmente.

---

## Schema do Job (cole no n8n → Webhook)

```markdown
{
  "job_type": "viral_replicate|clip_long|auto_post",
  "reference_url": "https://…", 
  "brand": {
    "name": "Ginkgo",
    "handle": "@ginkgo.ai",
    "colors": ["#5B3DF5", "#111111", "#FFD700"],
    "logo_url": "https://…"
  },
  "niche": "imobiliária|restaurante|infoproduto",
  "language": "pt-BR",
  "tone": "direto|humor|autoridade",
  "targets": { "duration_sec": 25, "count": 1 },
  "assets": { "broll_policy": "stock_free|client_only|mixed" },
  "cta": "Fale no WhatsApp | Link na bio",
  "posting": {
    "platforms": ["instagram","tiktok","youtube"],
    "schedule_iso": null
  },
  "delivery": { "notify": ["whatsapp","+55…","email","..."] },
  "compliance": { "no_plagiarism": true, "royalty_free": true }
}
```

---

## Nós essenciais no n8n (nomes e tipos)

- **Webhook In** (n8n-nodes-base.webhook)
- **Function: validate\_job** (n8n-nodes-base.function)
- **Execute Command: download\_ref** (`yt-dlp "{{ $json.reference_url }}" -o "/data/ref.mp4"`)
- **HTTP Request / OpenAI Whisper** ou provedor equivalente
- **Function: style\_parser** (extrai estrutura)
- **LLM: script\_writer** (Provider de sua escolha)
- **Function: captions\_srt**
- **Execute Command: montage\_ffmpeg**
- **HTTP Request: image\_gen\_thumb** (se usar gerador)
- **Supabase: upload\_assets**
- **If: posting\_enabled** → **Subworkflow: auto\_post**
- **Respond to Webhook** com JSON de status/URLs
- **Subworkflow: auto\_post** com conectores por plataforma e fallback via WhatsApp (Evolution API) ou Email.

---

## FFmpeg base (cole no Execute Command)

```markdown
ffmpeg -i /data/ref.mp4 -i /data/music.mp3 \
-filter_complex "[0:v]scale=-2:1920, crop=1080:1920, fps=30,eq=contrast=1.05:brightness=0.02[v]; \
[aud1]loudnorm=I=-14:TP=-1.5:LRA=11[a1]" \
-map "[v]" -map "[a1]" -c:v libx264 -preset veryfast -crf 18 -c:a aac -b:a 192k /data/out.mp4
```

Depois aplique *burn-in* de legendas:

```markdown
ffmpeg -i /data/out.mp4 -vf "subtitles=/data/captions.srt:force_style='Fontsize=42,PrimaryColour=&H00FFFFFF&'" -c:a copy /data/final.mp4
```

---

## Prompt do roteirista (LLM) — cole no nó “script\_writer”

```markdown
Objetivo: criar roteiro ORIGINAL no estilo do vídeo referência, sem copiar frases.
Entrada:
- Nicho, persona da marca, transcrição do vídeo referência, estrutura detectada (hook, cortes, CTA, pacing).
Saída:
- Roteiro para 25–35s, com:
  1) Hook de 2 linhas;
  2) 4–6 bullets com verbos de ação e prova social;
  3) CTA único e rastreável;
  4) Instruções de tela (B-roll, close, punch-in), timecodes aproximados.
Regras:
- Proíba frases idênticas ao referência.
- Simplifique vocabulário. Tom: {tone}. Idioma: {language}.
- Respeite a marca: cores, handle, proposta de valor.
```

---

## Lovable: app conversacional NL

**Integração:**

- Front: chat NL + upload/link do vídeo.
- Back: chama `POST /nyra/jobs` do n8n e exibe status.
- Webhook de retorno mostra “Pronto para download”, *preview* do MP4 e botões “Postar agora” por plataforma.

**Prompt para o Lovable (cole na descrição do app):**

```markdown
Você é a interface conversacional da NYRA.
Tarefas:
- Entender pedidos como “quero um vídeo igual a esse para meu negócio”.
- Coletar: link do vídeo referência, nicho, handle, cores, tom, CTA e se deseja postar automático.
- Montar JSON no schema exigido e enviar para POST /nyra/jobs.
- Acompanhar status via GET /nyra/jobs/{id}.
- Exibir links de download, thumb, descrição e botões de postagem.
Políticas:
- Nunca copie frases do vídeo original. Apenas mimetize ritmo, estrutura e estética.
- Se faltar permissão de postagem, ofereça pacote para postagem manual.
```

---

## Supabase

- **Bucket** `nyra-outputs`: `final.mp4`, `captions.srt`, `thumb.jpg`, `desc.txt`.
- **Tabela** `nyra_jobs`:
	- `id`, `payload`, `status` (queued|processing|done|failed), `outputs`, `timestamps`, `user_id`.

---

## WhatsApp e Email

- **Evolution API**: notificar “job pronto” com link do MP4 e CTA.
- **Email**: fallback com pacote ZIP.

---

## Publicação direta

- Exija tokens e permissões por plataforma.
- Se token inválido, retorne instruções simples e pacote pronto.

---

## Limites e compliance

- Sem reutilizar trechos de áudio/vídeo do original sem licença.
- Use biblioteca royalty-free ou assets do cliente.
- Marcas de terceiros: fl blur se aparecerem sem autorização.
- Logue fonte de mídia para auditoria.

---

## MVP checklist

- Webhook n8n + validação + fila
- Download + transcrição
- Parser de estilo + roteiro LLM
- Captions + montagem FFmpeg
- Supabase storage + retorno
- Lovable chat com schema e status
- Notificação Evolution API
- Publicadores com fallback

Quer que eu gere os três sub-workflows n8n com os nós nomeados e *placeholders* de ambiente para você importar?