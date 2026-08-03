# Relatório Estratégico: Mercado Imobiliário e Lead Generation - Centro Histórico de Pelotas-RS

Este relatório apresenta uma análise técnica do mercado imobiliário no Centro Histórico de Pelotas, com foco em investidores e compradores de alto padrão, além de uma arquitetura recomendada para automação de captação de leads baseada na metodologia solicitada.

## 1. Panorama do Mercado (Centro Histórico)

O Centro Histórico de Pelotas vive um momento de **revitalização acelerada (2025-2026)**, impulsionado por investimentos públicos (IPHAN/Prefeitura) e privados. Os principais vetores de valorização são:

*   **Retrofit e Restauro**: Linhas de crédito exclusivas (ex: CAIXA Retrofit) estão atraindo investidores para a modernização de casarões históricos para uso residencial e comercial.
*   **Empreendimentos Âncora**: O projeto **Central Park Pelotas** (Zabaleta/Solum) na Praça Coronel Pedro Osório é o principal termômetro de demanda para o público de alto padrão.
*   **Migração de Capital**: Com a queda dos juros, investidores locais e fundos (como o **PHORBIS**) estão alocando capital em ativos reais na região central.

## 2. Arquitetura de Automação Recomendada

Para escalar a captação de leads qualificados neste nicho, recomenda-se a seguinte arquitetura de integração:

### Fluxo de Dados (n8n + Manus + CRM)

1.  **Trigger (Monitoramento)**:
    *   **Google Search API**: Monitorar termos como "comprar casarão Pelotas", "investimento imobiliário Pelotas", "lançamento Central Park".
    *   **Meta Ads Library**: Rastrear anúncios ativos das construtoras identificadas (Solum, Zabaleta, Roberto Ferreira).
2.  **Processamento (Manus AI)**:
    *   Extração de nomes de perfis que interagem com posts de corretores influentes (ex: Rodrigo Maysonnave).
    *   Scoring automático baseado em cargo (LinkedIn) e histórico de investimentos.
3.  **Enriquecimento**:
    *   Uso de **Hunter.io** ou **Apollo.io** para encontrar emails corporativos dos diretores e sócios das incorporadoras.
4.  **Destino**:
    *   Inserção automática no CRM (ex: ClickUp ou CRM proprietário via API) com tag "Investidor_Pelotas_Centro".

### Pseudocódigo de Integração (Python/n8n)

```python
# Exemplo de lógica para scoring de leads imobiliários
def calculate_lead_score(lead_data):
    score = 0
    # Critério 1: Cargo de decisão
    if any(title in lead_data['job_title'].lower() for title in ['ceo', 'diretor', 'sócio', 'investidor']):
        score += 5
    # Critério 2: Interesse em projetos específicos
    if 'central park' in lead_data['context'].lower() or 'retrofit' in lead_data['context'].lower():
        score += 3
    # Critério 3: Localização
    if 'pelotas' in lead_data['location'].lower():
        score += 2
    return score

# Fluxo n8n: HTTP Request -> Manus AI -> Google Sheets
```

## 3. Principais Leads Identificados (Resumo)

| Categoria | Principais Nomes/Empresas | Potencial |
| :--- | :--- | :--- |
| **Investidores Institucionais** | PHORBIS, Enfoque Shift Partners | Altíssimo |
| **Incorporadoras Ativas** | Zabaleta, Solum, Roberto Ferreira, INC | Alto |
| **Corretores de Influência** | Rodrigo Maysonnave, Mateus Garcia | Médio (Parceria) |
| **Grupos de Investimento** | Klécio Santos (SAF Pelotas), Consórcio Xavante | Estratégico |

## 4. Próximos Passos Sugeridos

1.  **Campanha de Retargeting**: Criar anúncios no Meta Ads focados em "Retrofit e Investimento no Centro" para capturar o tráfego que já pesquisa pelos termos monitorados.
2.  **Abordagem Direta (Cold Outreach)**: Utilizar os contatos de sócios e diretores da Solum e PHORBIS para apresentar soluções de infraestrutura de automação para seus novos empreendimentos.
3.  **Monitoramento de Editais**: Acompanhar licitações de restauro do IPHAN para identificar empresas de engenharia que ganham contratos, pois estas são leads para fornecedores de tecnologia e automação.
