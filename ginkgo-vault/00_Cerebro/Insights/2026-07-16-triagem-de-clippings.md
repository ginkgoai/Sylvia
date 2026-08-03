# Triagem de clippings — insights da Sexta-feira

> Leitura classificada em 2026-07-16. Os clippings são referências externas ou conversas antigas; nenhum deles substitui evidência atual do produto.

## Segurança de agentes

**Fontes:** `ai-jail`, artigos de segurança de agentes e material Burp/PortSwigger.

- **Insight:** autonomia útil precisa de fronteiras técnicas, não só de instruções ao modelo. O padrão é ambiente isolado, mínimos mounts, rede limitada, credenciais efêmeras, logs redigidos e revisão antes de publicar.
- **Aplicação:** para desenvolvimento local, preferir WSL/ambiente isolado e permissões por projeto. Para Ginkgo, reforça a Boundary já prevista; não justifica rodar ferramentas ofensivas nem alterar produção.
- **Ação sugerida:** criar um check de segurança de desenvolvimento antes de qualquer operação autônoma com credenciais. Prioridade média; mudança somente após teste local.

## Tese de produto: agentes verticais

**Fontes:** `IA Agêntica Vertical` e materiais de ecossistema Hermes.

- **Insight:** a vantagem da Ginkgo não é “ter muitos agentes”, mas fechar um loop vertical com contexto, ação limitada, prova e resultado de negócio.
- **Aplicação:** LEAF continua sendo a cunha certa: mensagem → entendimento → CRM/agendamento/oferta → handoff humano → evidência. PYRE e WAVE só entram quando o loop manual demonstrar margem e repetição.
- **Risco:** projetos que prometem “sistema operacional de agentes” antes de um caso de uso verificável diluem foco e acumulam integrações frágeis.

## Operação comercial no WhatsApp

**Fonte:** Umbler Talk e conversas Gabbih/LEAF.

- **Insight:** o cliente compra uma equipe ampliada, mas confia quando vê controle: qualificação, agenda, encaminhamento e histórico. “24/7” sem handoff e fatos fundamentados é promessa vazia.
- **Aplicação:** posicionar Callima como atendimento de escopo estreito, com resposta fundamentada, memória por tenant, caixa de entrada humana e handoff comprovável. O diferencial da Ginkgo é honest-data, não somente conversa natural.

## Agenciamento, conteúdo e frentes da Ginkgo

**Fontes:** Studio Ginkgo, News For You, YouTube/Bitrix e mapas de patrimônio.

- **Insight:** o Studio é a superfície ativa de agenciamento da Ginkgo: clientes, Ginkgo Motor e redes próprias. Ele não concorre com o foco de produto do LEAF, mas precisa ser operado como portfólio com escopo, margem, métrica, capacidade e próximo passo claros.
- **Aplicação:** materiais de cada cliente ou frente ficam no seu espaço em `75_Studio/`; referências de YouTube entram como pesquisa de conteúdo, respeitando termos das plataformas e direitos autorais. Novas teses de curadoria devem ter hipótese, teto de esforço e gate de continuidade antes de receber capacidade recorrente.
- **Pessoal:** os quatro mapas de patrimônio são uma constituição pessoal, não documentação de produto; ficam separados em `70_Financeiro/Diario-e-Patrimonio`.

## Qualidade do acervo

- Há 126 clippings textuais (75 de julho, 51 de junho) e duplicatas exatas. O valor está na destilação, não em manter múltiplas cópias no contexto ativo.
- Conteúdo adulto/sensível, prompts antigos, dumps e mídia de origem incerta devem permanecer em quarentena até finalidade explícita e revisão de direitos/privacidade.
