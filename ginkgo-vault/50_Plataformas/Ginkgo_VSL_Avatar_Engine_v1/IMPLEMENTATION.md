# Implementação por subgrafos

## A — Avatar Master
Flux/PuLID/IPAdapter -> FaceDetailer -> Save Image

## B — Motion Base
Load Image -> Load Driver Video -> LivePortraitKJ -> VHS Video Combine

Parâmetros:
- relative motion ligado;
- stitching ligado;
- eye retargeting ligado;
- lip retargeting desligado;
- expressão baixa;
- 25 fps.

## C — Lip Sync
VHS Load Video -> MuseTalk -> VHS Video Combine + áudio original

Calibrar `bbox_shift` por avatar e salvar o valor no perfil da personagem.

## D — Fallback Premium
VHS Load Video -> LatentSync 1.6 -> VHS Video Combine

Executar somente em trechos reprovados.

## E — VSL Assembly
Segmentos aprovados -> concatenação -> legendas -> overlays -> CTA -> upscale
-> MP4 final.

## Cortes

Produzir em blocos de 5–10 segundos. Esconder cortes com:
- punch-in de 3–8%;
- B-roll;
- tela do celular;
- card tipográfico;
- transição curta de 4–8 frames.

## Ambiente

O pipeline completo depende de custom nodes. Validar as versões instaladas
antes de montar o JSON importável final.
