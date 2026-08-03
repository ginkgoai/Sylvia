# Ginkgo VSL Avatar Engine v1

Template técnico para vídeos verticais 9:16 com avatar humano, fala direta
para a câmera, estética intimista e estrutura de conversão.

## Entrada

- retrato mestre do avatar;
- vídeo-guia de microexpressões;
- narração WAV;
- briefing da oferta;
- identidade visual.

## Saída

- MP4 vertical 1080 × 1920;
- avatar estável;
- sincronização labial;
- legendas;
- CTA;
- versão limpa e versão final.

## Arquitetura

```text
Avatar Master + Driver íntimo
        ↓
LivePortrait — microexpressões e movimento estável
        ↓
MuseTalk 1.5 — sincronização labial principal
        ↓
QA
   ├─ aprovado → montagem VSL
   └─ reprovado → LatentSync 1.6 → montagem VSL
        ↓
VideoHelperSuite / FFmpeg
        ↓
Legendas + overlays + CTA + exportação 9:16
```

## Decisão de engenharia

LivePortrait controla cabeça, olhos, respiração e expressão. MuseTalk controla
principalmente boca e articulação. LatentSync é fallback premium. Essa
separação reduz deriva de rosto, roupa e fundo.

## Perfis de movimento

- `INTIMATE_NEUTRAL`: contato visual, piscar natural, quase imóvel.
- `WARM_HOOK`: leve sorriso e pequena ênfase na pergunta.
- `EXPLAIN`: microacenos lentos, expressão consultiva.
- `EMPHASIS`: sobrancelha e queixo discretos.
- `CTA`: confiança, sorriso contido e pausa final.

## Estrutura de VSL de 45–50 segundos

- 0–3s: gancho direto.
- 3–10s: dor reconhecível.
- 10–20s: mecanismo e solução.
- 20–32s: benefícios e demonstração.
- 32–42s: prova, objeção ou diferenciação.
- 42–50s: CTA único.
