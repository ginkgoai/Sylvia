# Plano de Implementação: Content Recycler Skill

**Autor**: Manus AI  
**Data**: 17 de Março de 2026  
**Status**: Pronto para Implementação

---

## Visão Executiva

A skill **Content Recycler** automatiza a transformação de conteúdos longos (vídeos de YouTube, lives, podcasts) e posts de redes sociais em múltiplos formatos curtos (Reels, Stories, TikToks, Shorts, Carrosséis). O sistema utiliza ferramentas open source consolidadas e APIs de IA para identificar highlights, editar conteúdo e distribuir automaticamente nas redes sociais.

**Resultado esperado**: De 5 vídeos longos ou 10 posts diversos, gerar 50+ novos conteúdos em formatos curtos, prontos para publicação.

---

## Arquitetura Técnica

### Componentes Principais

A skill é organizada em **5 pipelines independentes**, orquestrados via **n8n** e com persistência em **Supabase**:

| Pipeline | Responsabilidade | Ferramentas | Entrada | Saída |
|:---|:---|:---|:---|:---|
| **Inventory** | Mapear conteúdo dos últimos 7 dias | Manus Data API, yt-dlp | Plataformas (YouTube, Instagram, TikTok) | Metadados + URLs de mídia em Supabase |
| **Analysis** | Identificar highlights e momentos-chave | Whisper (OpenAI), LLM (GPT-4o/Claude) | Vídeos/áudios originais | Timestamps de highlights |
| **Processing** | Editar e remixar conteúdo | Auto-Editor, FFmpeg, MoviePy | Vídeos originais + Timestamps | Clipes curtos em múltiplos formatos |
| **Generation** | Criar captions, hashtags e variações | LLM (GPT-4o/Claude) | Clipes gerados | Copy otimizado por plataforma |
| **Distribution** | Agendar e publicar | Postiz API, n8n | Clipes + Copy | Conteúdo publicado/agendado |

### Fluxo de Dados

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONTENT RECYCLER FLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  [1] INVENTORY PHASE                                             │
│      Manus Data API → yt-dlp → Supabase (raw_content)           │
│                                                                   │
│  [2] ANALYSIS PHASE                                              │
│      Whisper (transcrição) → LLM (análise) → Timestamps         │
│                                                                   │
│  [3] PROCESSING PHASE                                            │
│      Auto-Editor (silêncios) → FFmpeg (cortes) → MoviePy (crop) │
│      Resultado: Supabase (recycled_content)                     │
│                                                                   │
│  [4] GENERATION PHASE                                            │
│      LLM → Captions, Hashtags, Títulos (múltiplas variações)    │
│                                                                   │
│  [5] DISTRIBUTION PHASE                                          │
│      n8n → Postiz API → Agendamento em redes sociais            │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Ferramentas Open Source Recomendadas

### 1. Auto-Editor (⭐4k)
**Função**: Remoção automática de silêncios e "dead space" em vídeos.

```bash
# Instalar
pip3 install auto-editor

# Usar
auto-editor video.mp4 --margin 0.2sec -o output.mp4
```

**Vantagem**: Extremamente rápido (compilado em Nim), ideal para processar vídeos longos em segundos.

### 2. MoviePy (⭐14.4k)
**Função**: Edição programática (crop, composição, legendas).

```bash
# Instalar
pip3 install moviepy

# Exemplo: Crop 9:16 com legendas
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

clip = VideoFileClip("video.mp4")
# Crop centralizado para 9:16
w, h = clip.size
target_w = int(h * 9/16)
cropped = clip.crop(x1=(w-target_w)/2, y1=0, x2=(w+target_w)/2, y2=h)

# Adicionar legenda
txt = TextClip("Highlight!", fontsize=70, color='white').set_duration(cropped.duration)
final = CompositeVideoClip([cropped, txt])
final.write_videofile("output.mp4")
```

### 3. FFmpeg (Legendary - 50k+)
**Função**: Cortes precisos e conversão de formatos.

```bash
# Corte rápido (sem recodificação)
ffmpeg -i input.mp4 -ss 120 -to 180 -c copy output.mp4
```

### 4. yt-dlp (⭐90k+)
**Função**: Download de vídeos de YouTube, TikTok, Instagram, etc.

```bash
# Instalar
pip3 install yt-dlp

# Usar
yt-dlp "https://www.youtube.com/watch?v=..." -o "%(title)s.%(ext)s"
```

### 5. Postiz (⭐27.4k)
**Função**: Agendamento de posts em múltiplas redes sociais.

**Integração via API REST**:
```bash
curl -X POST https://seu-postiz.com/api/posts \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Novo Reel!",
    "media": ["reel_01.mp4"],
    "platforms": ["instagram", "tiktok"],
    "scheduleTime": "2026-03-18T14:00:00Z"
  }'
```

---

## Passo a Passo de Implementação

### Fase 1: Setup Inicial (Semana 1)

**Objetivo**: Configurar a infraestrutura base.

1.  **Criar repositório da skill** no GitHub:
    ```bash
    gh repo create content-recycler --private
    ```

2.  **Instalar dependências** no sandbox:
    ```bash
    sudo apt-get update && sudo apt-get install -y ffmpeg
    pip3 install moviepy auto-editor yt-dlp supabase openai
    ```

3.  **Configurar Supabase**:
    - Criar tabelas: `raw_content`, `recycled_content`, `distribution_log`
    - Definir schemas (veja seção de Banco de Dados)

4.  **Configurar n8n**:
    - Criar workflow base para orquestração dos 5 pipelines
    - Testar conexão com Supabase e APIs

### Fase 2: Implementar Pipeline de Inventory (Semana 1-2)

**Objetivo**: Mapear conteúdo dos últimos 7 dias.

**Arquivo**: `scripts/inventory.py`

```python
import os
from supabase import create_client
from datetime import datetime, timedelta

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_recent_content(days=7):
    """Busca conteúdo dos últimos N dias via Manus Data API"""
    # Implementar chamadas às APIs do YouTube, Instagram, TikTok
    # Salvar em Supabase (tabela raw_content)
    pass

def download_media(url, output_path):
    """Usa yt-dlp para baixar vídeos"""
    import subprocess
    subprocess.run(["yt-dlp", url, "-o", output_path])

if __name__ == "__main__":
    content = fetch_recent_content(days=7)
    for item in content:
        download_media(item['url'], f"./downloads/{item['id']}.mp4")
```

### Fase 3: Implementar Pipeline de Analysis (Semana 2-3)

**Objetivo**: Identificar highlights usando IA.

**Arquivo**: `scripts/analysis.py`

```python
import openai
from pydub import AudioSegment
import subprocess

def transcribe_video(video_path):
    """Transcreve vídeo usando Whisper"""
    # Extrair áudio
    subprocess.run(["ffmpeg", "-i", video_path, "-q:a", "9", "-n", "audio.mp3"])
    
    # Transcrever com Whisper
    with open("audio.mp3", "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", f)
    
    return transcript["text"]

def analyze_highlights(transcript, video_duration):
    """Usa LLM para identificar highlights"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": f"""Analise esta transcrição e identifique os melhores momentos para Reels (15-60s).
            
Transcrição:
{transcript}

Duração total: {video_duration}s

Retorne um JSON com:
[{{"start": 120, "end": 180, "reason": "Hook forte", "platform": "reels"}}]
"""
        }]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    transcript = transcribe_video("video.mp4")
    highlights = analyze_highlights(transcript, 3600)
    print(highlights)
```

### Fase 4: Implementar Pipeline de Processing (Semana 3-4)

**Objetivo**: Gerar clipes curtos em múltiplos formatos.

**Arquivo**: `scripts/processing.py`

```python
import subprocess
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import json

def remove_silence(video_path, output_path):
    """Remove silêncios com Auto-Editor"""
    subprocess.run([
        "auto-editor", video_path,
        "--margin", "0.2sec",
        "-o", output_path
    ])

def cut_clip(video_path, start, end, output_path):
    """Corta clipe com FFmpeg (rápido)"""
    subprocess.run([
        "ffmpeg", "-i", video_path,
        "-ss", str(start), "-to", str(end),
        "-c", "copy", output_path
    ])

def crop_and_add_subtitles(video_path, output_path, format_type="reels"):
    """Crop 9:16 e adiciona legendas com MoviePy"""
    clip = VideoFileClip(video_path)
    
    # Definir dimensões por formato
    formats = {
        "reels": (1080, 1920),      # 9:16
        "stories": (1080, 1920),    # 9:16
        "posts": (1080, 1080),      # 1:1
    }
    
    target_w, target_h = formats.get(format_type, (1080, 1920))
    w, h = clip.size
    
    # Crop centralizado
    if w > target_w:
        x1 = (w - target_w) / 2
        x2 = x1 + target_w
        clip = clip.crop(x1=x1, x2=x2)
    
    # Redimensionar se necessário
    clip = clip.resize((target_w, target_h))
    
    # Adicionar legenda (exemplo)
    txt_clip = TextClip("Novo Reel!", fontsize=70, color='white')
    txt_clip = txt_clip.set_position(('center', 50)).set_duration(clip.duration)
    
    final = CompositeVideoClip([clip, txt_clip])
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")

def process_highlights(video_path, highlights_json, output_folder):
    """Processa todos os highlights"""
    with open(highlights_json) as f:
        highlights = json.load(f)
    
    for i, highlight in enumerate(highlights):
        # 1. Remover silêncios
        temp_edited = f"{output_folder}/temp_{i}.mp4"
        remove_silence(video_path, temp_edited)
        
        # 2. Cortar
        temp_cut = f"{output_folder}/temp_cut_{i}.mp4"
        cut_clip(temp_edited, highlight['start'], highlight['end'], temp_cut)
        
        # 3. Crop e legendas
        output = f"{output_folder}/reel_{i}.mp4"
        crop_and_add_subtitles(temp_cut, output, format_type=highlight.get('platform', 'reels'))
        
        print(f"✅ Gerado: {output}")

if __name__ == "__main__":
    process_highlights("video.mp4", "highlights.json", "./output")
```

### Fase 5: Implementar Pipeline de Generation (Semana 4)

**Objetivo**: Gerar captions e variações de copy.

**Arquivo**: `scripts/generation.py`

```python
import openai

def generate_captions(video_description, platform="instagram"):
    """Gera captions otimizadas por plataforma"""
    
    platform_guidelines = {
        "instagram": "Máx 2200 caracteres, use emojis, hashtags no final",
        "tiktok": "Máx 150 caracteres, use trending sounds, call-to-action",
        "linkedin": "Profissional, máx 1300 caracteres, foco em valor",
    }
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": f"""Gere 3 variações de caption para este vídeo, otimizadas para {platform}.

Diretrizes: {platform_guidelines[platform]}

Descrição do vídeo: {video_description}

Retorne um JSON:
[{{"caption": "...", "hashtags": ["tag1", "tag2"], "cta": "..."}}]
"""
        }]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    captions = generate_captions("Dica de produtividade", platform="instagram")
    print(captions)
```

### Fase 6: Integração com Postiz (Semana 4-5)

**Objetivo**: Agendar conteúdo nas redes sociais.

**Arquivo**: `scripts/distribution.py`

```python
import requests
import os
from datetime import datetime, timedelta

POSTIZ_API_URL = os.getenv("POSTIZ_API_URL")
POSTIZ_API_TOKEN = os.getenv("POSTIZ_API_TOKEN")

def schedule_post(media_path, caption, platforms, schedule_time=None):
    """Agenda um post no Postiz"""
    
    if schedule_time is None:
        schedule_time = (datetime.now() + timedelta(hours=2)).isoformat()
    
    headers = {
        "Authorization": f"Bearer {POSTIZ_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "content": caption,
        "media": [media_path],
        "platforms": platforms,
        "scheduleTime": schedule_time
    }
    
    response = requests.post(
        f"{POSTIZ_API_URL}/api/posts",
        json=payload,
        headers=headers
    )
    
    return response.json()

if __name__ == "__main__":
    result = schedule_post(
        "reel_01.mp4",
        "Novo conteúdo! 🎬 #reels #viral",
        ["instagram", "tiktok"],
        schedule_time="2026-03-18T14:00:00Z"
    )
    print(result)
```

---

## Banco de Dados (Supabase)

### Schema das Tabelas

#### Tabela: `raw_content`
```sql
CREATE TABLE raw_content (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  platform VARCHAR(50) NOT NULL,
  source_url TEXT NOT NULL,
  title VARCHAR(500),
  description TEXT,
  duration_seconds INT,
  media_url TEXT,
  local_path TEXT,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Tabela: `recycled_content`
```sql
CREATE TABLE recycled_content (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  source_id UUID REFERENCES raw_content(id),
  format VARCHAR(50) NOT NULL, -- 'reels', 'stories', 'posts'
  media_path TEXT NOT NULL,
  duration_seconds INT,
  start_time INT, -- timestamp no vídeo original
  end_time INT,
  captions JSONB, -- múltiplas variações
  hashtags TEXT[],
  status VARCHAR(50) DEFAULT 'draft', -- 'draft', 'approved', 'published'
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Tabela: `distribution_log`
```sql
CREATE TABLE distribution_log (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  recycled_content_id UUID REFERENCES recycled_content(id),
  platform VARCHAR(50) NOT NULL,
  scheduled_time TIMESTAMP,
  published_time TIMESTAMP,
  post_url TEXT,
  status VARCHAR(50) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Integração com n8n

### Workflow Base

```json
{
  "name": "Content Recycler - Main Orchestration",
  "nodes": [
    {
      "name": "Trigger Daily",
      "type": "trigger",
      "schedule": "0 0 * * *"
    },
    {
      "name": "Inventory Pipeline",
      "type": "webhook",
      "url": "http://localhost:3000/api/inventory"
    },
    {
      "name": "Analysis Pipeline",
      "type": "webhook",
      "url": "http://localhost:3000/api/analysis"
    },
    {
      "name": "Processing Pipeline",
      "type": "webhook",
      "url": "http://localhost:3000/api/processing"
    },
    {
      "name": "Generation Pipeline",
      "type": "webhook",
      "url": "http://localhost:3000/api/generation"
    },
    {
      "name": "Distribution Pipeline",
      "type": "webhook",
      "url": "http://localhost:3000/api/distribution"
    },
    {
      "name": "Log Results",
      "type": "supabase",
      "action": "insert",
      "table": "distribution_log"
    }
  ]
}
```

---

## Próximos Passos (Roadmap)

### Curto Prazo (Próximas 2 semanas)
- [ ] Implementar Pipeline de Inventory
- [ ] Integrar com Supabase
- [ ] Testar download de vídeos com yt-dlp

### Médio Prazo (Próximas 4 semanas)
- [ ] Implementar Pipelines de Analysis e Processing
- [ ] Testar Auto-Editor e MoviePy
- [ ] Criar n8n workflow de orquestração

### Longo Prazo (Próximas 8 semanas)
- [ ] Implementar Pipeline de Generation
- [ ] Integrar com Postiz
- [ ] Testes de produção com conteúdo real
- [ ] Dashboard de monitoramento

---

## Estimativa de Recursos

| Recurso | Quantidade | Custo |
|:---|:---|:---|
| Supabase (Database) | 1 | $25/mês (Pro) |
| OpenAI API (Whisper + GPT-4o) | Variável | ~$50-200/mês |
| Postiz (Self-hosted) | 1 | $0 (open source) |
| n8n (Self-hosted) | 1 | $0 (open source) |
| Servidor (4GB RAM, 2 CPU) | 1 | $10-20/mês |
| **Total estimado** | | **$85-245/mês** |

---

## Conclusão

A skill **Content Recycler** oferece uma solução completa e escalável para transformar conteúdo longo em dezenas de novos formatos curtos, otimizados para redes sociais. Utilizando ferramentas open source consolidadas (Auto-Editor, MoviePy, FFmpeg) e APIs de IA (Whisper, GPT-4o), o sistema é robusto, flexível e economicamente viável.

**Recomendação**: Começar pela implementação do Pipeline de Inventory (Semana 1-2) para validar a integração com Supabase e APIs de dados. Depois, proceder com os Pipelines de Analysis e Processing em paralelo (Semanas 2-4).

---

## Contato e Suporte

Para dúvidas sobre a implementação ou customizações específicas, consulte a documentação técnica no repositório GitHub ou entre em contato com o time de automação da Ginkgo AI Systems.
