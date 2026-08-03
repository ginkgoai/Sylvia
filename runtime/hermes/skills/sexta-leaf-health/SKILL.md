---
name: sexta-leaf-health
description: >-
  Observa a saude do Leaf e transforma sinais tecnicos em riscos operacionais
  para o fundador. Somente leitura nesta fase.
---

# Skill: sexta-leaf-health

Use quando o fundador perguntar sobre a saude do Leaf, capacidade de atender
usuarios, erros, integracao da Callima, prontidao de lancamento ou risco de
receita.

## Fontes e ordem

1. `sexta-status summary --hours 24` e eventos falhos recentes.
2. `sexta-n8n` para execucoes, falhas e workflows que alimentam a Callima.
3. O endpoint publico de saude do Leaf, quando disponivel:

```powershell
Invoke-WebRequest http://127.0.0.1:3333/health -UseBasicParsing
```

4. O estado conhecido em `memory/STATE.md`, deixando claro quando ele estiver
defasado ou sem telemetria recente.

## Relatorio executivo

Responda sempre nestas quatro linhas, quando houver dados:

1. **Servico:** disponivel, degradado ou desconhecido.
2. **Cliente:** impacto em conversas, leads, agenda ou campanha.
3. **Dinheiro:** risco ou oportunidade de receita/margem.
4. **Decisao:** proxima acao e se precisa de aprovacao do fundador.

## Limites

- Ausencia de eventos nao e saude: diga explicitamente "sem telemetria".
- Nao reinicie servicos, altere banco, reconfigure n8n ou execute workflows.
- A Callima e observada como runtime do Leaf; nao personifique nem altere o
  atendimento de clientes por esta skill.
