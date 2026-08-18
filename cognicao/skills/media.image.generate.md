# Skill: media.image.generate (genérica)

> Contrato adicionado na Wave 10 (2026-08-18). Arquivo NOVO e aditivo. A Sylvia fornece
> **constraints** — ela nunca seleciona ComfyUI, Gemini, fal.ai ou modelo. O Pyre decide o
> provider elegível (somente VALIDATED; hoje: local).

## Mapping

```yaml
intent: "gerar imagem"            # forma geral; sem exigência de execução local
skill: media.image.generate
executor: n8n workflow "creative-image-generate-v1"
output_contract: creative-asset
```

## Como a Sylvia traduz intenção em constraints

| O usuário diz | constraints |
|---|---|
| "gere localmente" / "sem sair da máquina" | `privacy: local_only` |
| "gere rápido e pode usar cloud" | `privacy: cloud_allowed, latency: fast` |
| "sem custo" | `max_cost_usd: 0` |
| "qualidade alta" | `quality: high` |
| (nada específico) | omitir — policy padrão escolhe o VALIDATED disponível (local) |

## Regras

- Campos `provider`/`tool`/`model` NUNCA são enviados (o Pyre rejeita com INVALID_REQUEST).
- `NO_VALIDATED_PROVIDER` pode voltar quando nenhuma opção validada satisfaz (ex.: pedido
  cloud-only enquanto o provider cloud segue EXPERIMENTAL) — repassar honestamente, sem
  tentar contornar por outro caminho.
- Para reprodutibilidade explícita local, usar a skill específica
  [[media.image.generate.local]] (`cognicao/skills/media.image.generate.local.md`).
