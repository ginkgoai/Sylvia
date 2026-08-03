# Relatório de Pesquisa de Produto: Dealism (Instagram DM Automation)

Este relatório apresenta uma análise técnica e de mercado da **Dealism**, focando em seu serviço de automação de DMs no Instagram, com insights para implementação em ecossistemas de automação de IA.

---

## 1. Visão Geral e Conceito: "Vibe Selling"

A Dealism se posiciona como o primeiro **Agente de Vendas de IA** baseado em **Vibe Selling**. Diferente de chatbots tradicionais (como ManyChat) que dependem de fluxos rígidos e palavras-chave, a Dealism utiliza LLMs (Large Language Models) para:

*   **Mimetizar o tom de voz:** O agente aprende a "vibe" da marca para soar humano.
*   **Negociação Dinâmica:** Capaz de lidar com objeções, preços e fechamento de vendas sem scripts pré-definidos.
*   **Orquestração Multi-Agente:** Diferentes instâncias de IA podem ser configuradas para partes específicas do funil (ex: um agente para qualificação, outro para agendamento).

---

## 2. Arquitetura Técnica e Integrações

Para um arquiteto de automação, os detalhes de conectividade são cruciais:

### Canais e Conectividade
| Canal | Método de Conexão | Status de Conformidade |
| :--- | :--- | :--- |
| **Instagram DM** | API Oficial do Messenger (Meta) | **Alta** (Seguro contra banimentos) |
| **WhatsApp** | Dispositivos Conectados (WhatsApp Web) | **Média** (Risco de banimento se não houver aquecimento) |
| **Web Chat** | Widget de Chat Nativo | **Alta** |

### Fluxo de Dados e Treinamento
O "cérebro" do agente é alimentado por uma **Base de Conhecimento (Knowledge Base)** que aceita:
1.  **URLs:** Raspagem automática de sites e catálogos.
2.  **Documentos:** Upload de PDFs com manuais de produtos e FAQs.
3.  **Texto Manual:** Definição de estratégias de vendas e diretrizes de comportamento.

### Integração com Ecossistemas (n8n, CRM, APIs)
Embora a Dealism não possua um nó nativo no n8n (até Março/2026), a integração é feita via **Webhooks**:
*   **Entrada:** Gatilhos de DMs, comentários ou menções no Instagram.
*   **Saída:** Envio de leads qualificados para CRMs (HubSpot, Salesforce) ou bancos de dados (Supabase) via n8n.
*   **Sincronização:** Capacidade de sincronizar conversas entre múltiplos canais em um dashboard unificado.

---

## 3. Funcionalidades de Vendas e E-commerce

A Dealism é otimizada para conversão direta:

*   **Links de Checkout:** O agente pode enviar links de pagamento diretamente no DM após confirmar o interesse.
*   **Recuperação de Carrinho:** Identifica intenção de compra e faz follow-up automático.
*   **Agendamento:** Integração com calendários para marcação de reuniões ou consultas.
*   **Handoff Humano:** Sistema de transição suave para um atendente humano quando a IA detecta uma complexidade que exige intervenção.

---

## 4. Análise de Preços (BRL)

Os planos são baseados no volume de conversas mensais:

| Plano | Preço Mensal | Cota de Conversas | Recursos |
| :--- | :--- | :--- | :--- |
| **Membro Mensal 1** | R$ 99 | 1.000 | Agentes ilimitados, Base de Conhecimento, Suporte Multilíngue. |
| **Membro Mensal 2** | R$ 199 | 2.000 | Todos os recursos + maior volume. |
| **Membro Anual** | R$ 1.999/ano | 2.000/mês | Desconto para pagamento antecipado. |
| **Enterprise** | Sob consulta | Personalizado | Suporte dedicado e treinamento de modelo customizado. |

---

## 5. Comparativo de Mercado: Dealism vs. Concorrentes

| Critério | Dealism | ManyChat | Chatwoot (Self-hosted) |
| :--- | :--- | :--- | :--- |
| **Lógica de Resposta** | IA Generativa (LLM) | Fluxos de Árvore (If/Else) | Híbrido (Manual + Bot) |
| **Facilidade de Setup** | Alta (No-code) | Média (Requer lógica de fluxo) | Baixa (Requer infraestrutura) |
| **Foco** | Vendas e Conversão | Marketing e Broadcast | Atendimento ao Cliente |
| **Personalização** | Tom de voz adaptativo | Scripts fixos | Depende da integração de IA |

---

## 6. Recomendações para Implementação (Ginkgo AI Systems)

Para integrar a Dealism em sua infraestrutura de automação:

1.  **Arquitetura de Leads:** Use a Dealism como a "camada de conversação" (Front-end) no Instagram. Configure um Webhook para disparar dados de leads qualificados para o seu **n8n**.
2.  **Armazenamento:** No n8n, processe os dados e armazene no **Supabase** para análise de dados e retreinamento de agentes futuros.
3.  **Estratégia de "Vibe":** Aproveite a base de conhecimento para injetar o tom de voz específico de cada cliente SaaS que você atende, garantindo que o agente não soe como um bot genérico.
4.  **Escalabilidade:** Para clientes de alto volume, o plano Enterprise permite uma orquestração multi-agente que pode ser gerenciada via API para automação de criação de sub-contas (se disponível via suporte).

---

> **Nota Técnica:** A Dealism utiliza uma abordagem de "Continual Learning", o que significa que o agente melhora à medida que interage. Para Gabriel, isso reduz o overhead de manutenção de fluxos de automação complexos no n8n, permitindo focar na infraestrutura de dados e integrações de backend.
