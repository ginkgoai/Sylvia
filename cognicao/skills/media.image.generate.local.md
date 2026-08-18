# Skill: media.image.generate.local

> Contrato adicionado na Wave 8 (2026-08-17). Arquivo NOVO e aditivo — nenhum arquivo
> existente da Sylvia foi modificado. A Sylvia escolhe a SKILL; ela nunca escolhe
> ComfyUI, workflows internos, checkpoints ou runtime diretamente.

## Mapping (snapshot pinado — Arsenal)

```yaml
intent: "gerar uma imagem local"        # e variações: criar imagem, foto, visual local
capability: creative.image.local
skill: media.image.generate.local
executor: n8n workflow "creative-image-local-v1"   # ai-stack/workflows/_MediaGen
output_contract: creative-asset          # CreativeGenerationResult normalizado do Pyre
privacy: local-only                      # geração 100% na workstation (RTX 4060)
```

## Como disparar

Chamar o executor (workflow n8n) com o contrato de ENTRADA — nunca o runtime:

```json
{
  "request_id": "<uuid>",
  "prompt": "<descrição da imagem>",
  "negative_prompt": "(opcional)",
  "width": 768, "height": 768,
  "seed": 12345,
  "preset": "sdxl-local-standard",
  "caller": "sylvia"
}
```

Retorno: contrato `creative-asset` (status, provider, asset{path,...}, generation{seed,...},
cost, provenance, error normalizado). Asset físico em `C:\AI\30-Assets\images\generated\pyre\`.

## Discovery futuro (documentado, não implementado)

goal → **capabilities registry** (que capacidades existem: creative.image.local, futuras
creative.image.cloud/creative.video.cloud) → **skills registry** (skill por capability +
constraints de privacy/custo/latência) → **execution mode** (n8n workflow | API direta |
agente) → workflow/tool concreto. Nesta wave o registry é este snapshot pinado; RAG sobre a
Library inteira fica para depois.

## Limites (v1)

- Somente `kind=image`, preset `sdxl-local-standard` (768×768; overrides até 1024, múltiplos de 8).
- Runtime é on-demand: primeira geração fria custa ~85s; não assumir latência interativa.
- Erros voltam normalizados (`PROVIDER_UNAVAILABLE`, `TIMEOUT`, etc.) — repassar ao usuário sem detalhes internos.
