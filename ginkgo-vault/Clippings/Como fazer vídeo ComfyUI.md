---
title: "Como fazer vídeo ComfyUI"
source: "https://chatgpt.com/c/6a658301-5f88-83e9-b25a-3b9e35f95e29"
author:
published:
created: 2026-07-26
description: "ChatGPT conversation with 4 messages"
tags:
  - "clippings"
---
**Você disse**

Como faz esse tipo de vídeo, é no ComfyUI?

---

**Dá para reproduzir no ComfyUI, mas este vídeo provavelmente não foi feito apenas com ComfyUI.**

Pelos frames, ele parece ter sido construído com uma destas duas rotas:

1. **Animação 3D tradicional**, com personagem rigado, expressões faciais e câmera animada.
2. **Vídeo real ou animação-base transformada por IA**, usando video-to-video para trocar a pessoa pelo personagem.

A segunda hipótese é bem provável. As mãos, o casaco, o rosto e os movimentos permanecem consistentes durante quase nove segundos. Isso indica que existe uma **performance-base controlando o movimento**, em vez de um simples prompt text-to-video.

## Anatomia do vídeo

O pipeline provável é:

```
Vídeo de referência com atuação
        ↓
Captura do movimento corporal/facial
        ↓
Personagem 3D ou referência visual
        ↓
Video-to-video / renderização
        ↓
Máscara circular + efeito olho mágico
        ↓
Zoom final no rosto/olho
        ↓
Color grading e exportação
```

A borda circular não é parte complexa da geração. É basicamente:

- máscara circular;
- fundo preto;
- leve distorção fisheye;
- vinheta;
- zoom progressivo no final.

Isso pode ser feito no CapCut, After Effects, DaVinci Resolve ou diretamente com FFmpeg.

## Como eu faria no ComfyUI

### Etapa 1 — Criar o personagem

Gerar uma imagem-base frontal do personagem:

```
stylized 3D animated male character, expressive angular face,
black beanie, oversized brown fur coat, cinematic soft lighting,
high-end animated feature film style, consistent character design
```

Criaria também:

- frente;
- três quartos;
- perfil;
- expressão neutra;
- expressão desconfiada;
- boca aberta;
- close do rosto.

Essas imagens viram o “DNA visual” do personagem.

### Etapa 2 — Gravar a atuação

Você grava uma pessoa executando exatamente:

- bocejo;
- mão no rosto;
- ajuste no casaco;
- olhar lateral;
- aproximação da câmera;
- olhar direto para a lente.

Esse vídeo deve ter câmera estável e fundo simples. A IA trabalha melhor quando não precisa resolver o apocalipse inteiro em um único prompt.

### Etapa 3 — Transformar em personagem

No ComfyUI, a estrutura seria aproximadamente:

```
Load Video
   ↓
Resize / Crop 1:1
   ↓
Extração de pose, profundidade ou movimento
   ↓
Referência visual do personagem
   ↓
Modelo video-to-video
   ↓
Controle de intensidade/denoise
   ↓
Decodificação
   ↓
Interpolação de frames
   ↓
Upscale
   ↓
Video Combine
```

Modelos e workflows de vídeo podem rodar dentro do ComfyUI. A documentação oficial atualmente inclui fluxos de image-to-video, text-to-video, controle por múltiplos frames e video-to-video com famílias como Wan, LTX-Video, Hunyuan e VACE. [^1]

Para esse caso, eu priorizaria:

### Melhor opção técnica

**Wan + VACE/video-to-video**

Porque você precisa conservar:

- gesto das mãos;
- direção do olhar;
- movimento da cabeça;
- composição;
- timing da atuação.

### Opção mais simples

**Imagem do personagem + image-to-video**

Funciona para testes, mas dá menos controle. O modelo pode interpretar livremente o movimento e transformar o bocejo em possessão demoníaca digital no frame 63.

### Configuração inicial sugerida

```
Resolução de geração: 512×512 ou 720×720
Duração por geração: 3–5 segundos
FPS de geração: 12–16
FPS final: 24 ou 30
Denoise video-to-video: 0,35–0,55
Guidance: moderado
Seed: fixa durante os testes
Movimento de câmera: baixo
```

Não começaria tentando gerar os 8,6 segundos inteiros. Dividiria em:

```
Cena 1: bocejo e mão no rosto
Cena 2: ajuste no casaco e olhar lateral
Cena 3: aproximação e close no olho
```

Depois juntaria as cenas no editor.

## O detalhe mais importante

O ComfyUI seria o **motor de transformação**, não necessariamente o estúdio completo.

A arquitetura mais confiável seria:

```
Atuação gravada
   → ComfyUI para estilização e personagem
   → editor para máscara circular, zoom e acabamento
```

Para consistência profissional absoluta, o caminho seria:

```
Blender/Unreal
   → personagem rigado
   → captura facial e corporal
   → render
   → pós-produção
```

Para produção rápida de Reels, Nyra ou influencers da Ginkgo:

```
Vídeo-base humano
   → ComfyUI V2V
   → personagem padronizado
   → CapCut/After Effects
```

**Diagnóstico final:** é possível fazer no ComfyUI, mas eu não classificaria o exemplo como “prompt → vídeo”. Ele parece uma animação controlada, ou um vídeo-base convertido em personagem. O segredo não está no prompt; está no controle temporal.

---

**Você disse**

E este

---

Este é **bem mais compatível com IA generativa de vídeo** do que o anterior.

Minha leitura: provavelmente foi feito com **imagem-base do personagem + image-to-video/text-to-video**, dividido em várias cenas, e depois montado em editor. Pode ter passado pelo ComfyUI, mas também pode ter sido produzido em uma plataforma fechada de geração de vídeo.

## O que o vídeo mostra tecnicamente

São aproximadamente **12 segundos, 24 fps**, com pelo menos cinco planos distintos:

```
1. Close da personagem com a arma
2. Aparição dos cães de sombra
3. Close agressivo da criatura
4. Disparo e clarão
5. Personagem saindo da fumaça + glitch final
```

Isso é importante: dificilmente alguém gerou tudo como um único clipe perfeito. O caminho mais provável foi:

```
Personagem consistente
        ↓
5 imagens-chave cinematográficas
        ↓
Animação individual de cada imagem
        ↓
Montagem dos planos
        ↓
Som, tiro, fumaça, glitch e color grading
```

## É ComfyUI?

**Pode ser.** Este estilo encaixa muito bem em ComfyUI porque ele permite controlar:

- personagem por imagem de referência;
- estilo visual;
- enquadramento;
- início e fim de cada cena;
- movimento da câmera;
- consistência entre planos;
- interpolação e upscale.

Mas visualmente não existe uma “assinatura” que prove que foi ComfyUI. ComfyUI é o cockpit; o resultado depende do modelo rodando por trás.

## Como reproduzir

### 1\. Criar a personagem principal

Primeiro, uma ficha visual consistente:

- cabelo azul-acinzentado;
- sardas;
- casaco branco;
- uniforme tático;
- arma futurista;
- estilo anime realista;
- fundo branco minimalista.

Produzir:

```
Close frontal
Perfil
Corpo inteiro
Costas
Pose segurando arma
Expressão neutra
Expressão de combate
```

O ideal é treinar uma pequena LoRA da personagem ou usar referência facial e de roupa em todas as cenas.

### 2\. Criar os cães de sombra

Separadamente:

```
massive shadow hound made of black smoke,
glowing white eyes, ember particles,
ink-like tendrils, terrifying silhouette,
high-key white background, cinematic fantasy
```

Depois você combina personagem e criatura nas imagens-chave.

### 3\. Montar cinco keyframes

Exemplo de storyboard:

```
Cena 1 — personagem abre os olhos
Cena 2 — criatura surge atrás dela
Cena 3 — monstro avança
Cena 4 — personagem dispara
Cena 5 — fumaça desaparece e ela continua caminhando
```

Cada cena deve ser gerada como uma imagem estática forte. Isso reduz muito a loteria do vídeo.

### 4\. Animar no ComfyUI

Estrutura básica:

```
Load Image
   ↓
Imagem de referência da personagem
   ↓
Modelo image-to-video
   ↓
Controle de movimento
   ↓
Frames
   ↓
Interpolação
   ↓
Upscale
   ↓
Video Combine
```

Configuração inicial prática:

```
Duração por plano: 2 a 3 segundos
Resolução de geração: 720p ou inferior
FPS gerado: 12–16
FPS final: 24
Movimento: moderado
Câmera: movimentos simples
Seed: fixa durante testes
```

Não tente pedir:

> “Personagem luta com cães de sombra, atira, corre, câmera gira e tudo permanece consistente.”

Isso é convocar um sindicato de mutações digitais.

Peça uma ação por plano.

## Elementos feitos provavelmente fora da geração

Alguns detalhes parecem pós-produção:

- clarão do disparo;
- som da arma;
- impacto;
- distorção do frame;
- barras de glitch no final;
- transições;
- shake de câmera;
- contraste e brilho.

Esses elementos são fáceis de fazer no:

- DaVinci Resolve;
- After Effects;
- CapCut;
- FFmpeg.

## Pipeline recomendado para a Ginkgo/Pyre

```
Roteiro curto
   ↓
Storyboard automático
   ↓
Gerador de imagens-chave
   ↓
Validação de consistência
   ↓
ComfyUI image-to-video
   ↓
Interpolação/upscale
   ↓
FFmpeg para montagem
   ↓
SFX + música + glitch
   ↓
QC automático
```

**Conclusão:** este vídeo é reproduzível no ComfyUI com boa fidelidade. Diferente do anterior, não exige necessariamente captura humana ou rig 3D. O segredo aqui é gerar **vários planos curtos com a mesma personagem**, não tentar criar o filme inteiro em uma única geração.

[^1]: [docs.comfy.org](https://docs.comfy.org/development/core-concepts/workflow?utm_source=chatgpt.com)