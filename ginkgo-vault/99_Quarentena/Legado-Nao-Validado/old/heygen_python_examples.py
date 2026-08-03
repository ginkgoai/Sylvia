#!/usr/bin/env python3
"""
Exemplos de integração com HeyGen API em Python
Útil para testes, scripts standalone ou integração com agentes customizados
"""

import requests
import json
import time
from typing import Dict, Optional
import os
from datetime import datetime

# Configuração
HEYGEN_API_KEY = os.getenv("HEYGEN_API_KEY", "your-api-key-here")
HEYGEN_BASE_URL = "https://api.heygen.com/v2"

# IDs pré-configurados
AVATAR_ID = os.getenv("HEYGEN_AVATAR_ID", "your-avatar-id")
VOICE_ID = os.getenv("HEYGEN_VOICE_ID", "your-voice-id")


class HeyGenClient:
    """Cliente para interagir com a API do HeyGen"""
    
    def __init__(self, api_key: str, base_url: str = HEYGEN_BASE_URL):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }
    
    def list_avatars(self) -> Dict:
        """Lista todos os avatares disponíveis"""
        url = f"{self.base_url}/avatars"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def list_voices(self) -> Dict:
        """Lista todas as vozes disponíveis"""
        url = f"{self.base_url}/voices"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def create_video(
        self,
        script: str,
        avatar_id: Optional[str] = None,
        voice_id: Optional[str] = None,
        title: str = "Generated Video",
        caption: bool = True,
        width: int = 1080,
        height: int = 1920,
        callback_id: Optional[str] = None,
        callback_url: Optional[str] = None
    ) -> Dict:
        """
        Cria um novo vídeo com avatar
        
        Args:
            script: Texto do script (máximo 5000 caracteres)
            avatar_id: ID do avatar (usa AVATAR_ID se não fornecido)
            voice_id: ID da voz (usa VOICE_ID se não fornecido)
            title: Título do vídeo
            caption: Se deve adicionar legendas automáticas
            width: Largura do vídeo em pixels
            height: Altura do vídeo em pixels
            callback_id: ID customizado para tracking
            callback_url: URL para webhook de conclusão
        
        Returns:
            Dict com video_id e status
        """
        avatar_id = avatar_id or AVATAR_ID
        voice_id = voice_id or VOICE_ID
        
        payload = {
            "title": title,
            "caption": caption,
            "dimension": {
                "width": width,
                "height": height
            },
            "video_inputs": [
                {
                    "character": {
                        "type": "avatar",
                        "avatar_id": avatar_id,
                        "avatar_style": "normal"
                    },
                    "voice": {
                        "type": "text",
                        "input_text": script,
                        "voice_id": voice_id,
                        "speed": 1.0
                    },
                    "background": {
                        "type": "color",
                        "value": "#000000"
                    }
                }
            ]
        }
        
        if callback_id:
            payload["callback_id"] = callback_id
        
        if callback_url:
            payload["callback_url"] = callback_url
        
        url = f"{self.base_url}/video/generate"
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()
    
    def get_video_status(self, video_id: str) -> Dict:
        """Obtém o status de um vídeo"""
        url = f"{self.base_url}/video/{video_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def wait_for_video(
        self,
        video_id: str,
        max_wait_seconds: int = 600,
        poll_interval: int = 5
    ) -> Dict:
        """
        Aguarda até que o vídeo esteja pronto
        
        Args:
            video_id: ID do vídeo
            max_wait_seconds: Tempo máximo de espera (padrão 10 minutos)
            poll_interval: Intervalo entre verificações em segundos
        
        Returns:
            Dict com status final e URL de download
        """
        start_time = time.time()
        
        while time.time() - start_time < max_wait_seconds:
            status_response = self.get_video_status(video_id)
            status = status_response.get("status")
            
            print(f"[{datetime.now().isoformat()}] Status: {status}")
            
            if status == "completed":
                return status_response
            elif status == "failed":
                raise Exception(f"Video generation failed: {status_response}")
            
            time.sleep(poll_interval)
        
        raise TimeoutError(f"Video {video_id} did not complete within {max_wait_seconds}s")
    
    def download_video(self, video_url: str, output_path: str) -> None:
        """Baixa o vídeo da URL fornecida"""
        response = requests.get(video_url, stream=True)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Video downloaded to {output_path}")


# ============================================================================
# EXEMPLO 1: Criar um vídeo simples e aguardar conclusão
# ============================================================================

def example_1_simple_video():
    """Exemplo básico: criar vídeo e aguardar"""
    client = HeyGenClient(HEYGEN_API_KEY)
    
    script = "Você responde cliente em quanto tempo? Ah, depende? Então já perdeu. A Ginkgo não depende."
    
    print("Creating video...")
    response = client.create_video(
        script=script,
        title="Nyra na Rua - Teste 01",
        callback_id="test_001"
    )
    
    video_id = response.get("video_id")
    print(f"Video created with ID: {video_id}")
    
    print("Waiting for video to complete...")
    final_status = client.wait_for_video(video_id)
    
    video_url = final_status.get("video_url")
    print(f"Video ready! URL: {video_url}")
    
    # Baixar
    client.download_video(video_url, f"/tmp/{video_id}.mp4")


# ============================================================================
# EXEMPLO 2: Listar avatares e vozes disponíveis
# ============================================================================

def example_2_list_resources():
    """Exemplo: listar avatares e vozes"""
    client = HeyGenClient(HEYGEN_API_KEY)
    
    print("=== AVATARES DISPONÍVEIS ===")
    avatars = client.list_avatars()
    for avatar in avatars.get("avatars", [])[:5]:  # Primeiros 5
        print(f"- {avatar.get('name')} (ID: {avatar.get('avatar_id')})")
    
    print("\n=== VOZES DISPONÍVEIS ===")
    voices = client.list_voices()
    for voice in voices.get("voices", [])[:5]:  # Primeiras 5
        print(f"- {voice.get('name')} (ID: {voice.get('voice_id')}, Lang: {voice.get('language')})")


# ============================================================================
# EXEMPLO 3: Integração com Supabase (salvar metadados)
# ============================================================================

def example_3_with_supabase():
    """Exemplo: criar vídeo e salvar no Supabase"""
    from supabase import create_client, Client
    
    # Inicializar Supabase
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(supabase_url, supabase_key)
    
    client = HeyGenClient(HEYGEN_API_KEY)
    
    # Dados do cliente
    cliente_nome = "João Silva"
    dor_principal = "Demora em responder cliente"
    script = f"Tu responde cliente em quanto tempo? Ah, depende? Então já perdeu. A Ginkgo não depende."
    
    # Criar vídeo
    print(f"Creating video for {cliente_nome}...")
    response = client.create_video(
        script=script,
        title=f"Nyra na Rua - {cliente_nome}",
        callback_id=f"{cliente_nome}_{int(time.time())}"
    )
    
    video_id = response.get("video_id")
    
    # Salvar no Supabase
    supabase.table("heygen_videos").insert({
        "video_id": video_id,
        "status": "pending",
        "script": script,
        "callback_id": response.get("callback_id")
    }).execute()
    
    print(f"Video {video_id} saved to Supabase")
    
    # Aguardar conclusão
    print("Waiting for video...")
    final_status = client.wait_for_video(video_id)
    
    # Atualizar no Supabase
    supabase.table("heygen_videos").update({
        "status": "completed",
        "video_url": final_status.get("video_url")
    }).eq("video_id", video_id).execute()
    
    print("Video completed and updated in Supabase!")


# ============================================================================
# EXEMPLO 4: Gerar script com OpenAI e criar vídeo
# ============================================================================

def example_4_with_openai():
    """Exemplo: gerar script com OpenAI e criar vídeo"""
    from openai import OpenAI
    
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    heygen_client = HeyGenClient(HEYGEN_API_KEY)
    
    # Dados do cliente
    cliente_nome = "Maria Santos"
    dor_principal = "Perder vendas por demora"
    
    # Gerar script com OpenAI
    print("Generating script with OpenAI...")
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Você é a Nyra, uma IA que faz entrevistas virais. Seja direto, provocativo e educativo."
            },
            {
                "role": "user",
                "content": f"Crie um script curto (máximo 30 segundos) para questionar {cliente_nome} sobre '{dor_principal}' e apresentar a solução Ginkgo."
            }
        ],
        max_tokens=150
    )
    
    script = response.choices[0].message.content
    print(f"Generated script:\n{script}\n")
    
    # Criar vídeo
    print("Creating video...")
    video_response = heygen_client.create_video(
        script=script,
        title=f"Nyra na Rua - {cliente_nome}",
        callback_id=f"{cliente_nome}_{int(time.time())}"
    )
    
    video_id = video_response.get("video_id")
    print(f"Video created: {video_id}")


# ============================================================================
# EXEMPLO 5: Batch processing (múltiplos vídeos)
# ============================================================================

def example_5_batch_processing():
    """Exemplo: criar múltiplos vídeos em sequência"""
    client = HeyGenClient(HEYGEN_API_KEY)
    
    clientes = [
        {"nome": "Cliente A", "dor": "Demora em responder"},
        {"nome": "Cliente B", "dor": "Perder vendas"},
        {"nome": "Cliente C", "dor": "Falta de automação"},
    ]
    
    videos_criados = []
    
    for cliente in clientes:
        script = f"Tu {cliente['dor']}? A Ginkgo resolve isso automaticamente."
        
        print(f"Creating video for {cliente['nome']}...")
        response = client.create_video(
            script=script,
            title=f"Nyra - {cliente['nome']}",
            callback_id=f"{cliente['nome']}_{int(time.time())}"
        )
        
        video_id = response.get("video_id")
        videos_criados.append({
            "cliente": cliente['nome'],
            "video_id": video_id
        })
        
        # Aguardar entre requisições para evitar rate limiting
        time.sleep(2)
    
    print(f"\n{len(videos_criados)} videos created!")
    for video in videos_criados:
        print(f"- {video['cliente']}: {video['video_id']}")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        example_num = sys.argv[1]
        
        if example_num == "1":
            example_1_simple_video()
        elif example_num == "2":
            example_2_list_resources()
        elif example_num == "3":
            example_3_with_supabase()
        elif example_num == "4":
            example_4_with_openai()
        elif example_num == "5":
            example_5_batch_processing()
        else:
            print("Unknown example. Use 1-5.")
    else:
        print("Usage: python heygen_python_examples.py <example_number>")
        print("Examples:")
        print("  1 - Simple video creation")
        print("  2 - List avatars and voices")
        print("  3 - Integration with Supabase")
        print("  4 - Generate script with OpenAI")
        print("  5 - Batch processing")
