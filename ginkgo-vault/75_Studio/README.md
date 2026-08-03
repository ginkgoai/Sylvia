# 75_Studio — Agenciamento ativo

Esta pasta é a frente ativa de agenciamento da Ginkgo, não um arquivo de projetos secundários. Ela reúne operações de clientes, o Ginkgo Motor e o agenciamento das redes da própria Ginkgo.

## Roteamento

| Espaço | Uso |
|---|---|
| `agencia-hot/` | Operações que exigem tratamento restrito e fluxo manual controlado. No estado atual, inclui a frente `vip-gabi`. |
| `agencia-white/` | Operações de marca, canais e motores: `gabrielschaun-motor`, `ginkgo-motor` e `zavancenografia-motor`. |
| `Projetos/` | Materiais de projeto e referências Studio que ainda não pertencem a uma operação de cliente específica. |

## Contrato de cada frente

Cada cliente ou operação deve ter, na sua própria pasta, o mínimo necessário para operar com continuidade:

- briefing, objetivo e escopo autorizado;
- estratégia, entregas, calendário e responsáveis;
- métricas, evidências e próximo passo;
- runbook operacional e limites de aprovação;
- documentos, ativos e referências específicos da frente.

Não mova dados detalhados de uma frente para o cérebro global. A Sexta-feira pode abrir o escopo pertinente para analisar e preparar trabalho, mas publicação, gastos, comunicação externa, deleção ou mudança em dados de cliente continuam sujeitos a confirmação ou runbook pré-aprovado.
