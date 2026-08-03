# LEAF BY GINKGO — DESIGN.md

> Sistema visual e verbal para campanhas de Facebook, Meta Ads, demonstrações comerciais e páginas do LEAF.
> Uso recomendado: anexar este arquivo a um projeto novo no Claude Design e solicitar a criação do sistema de design.

---

## 0. Brand Context

### Brand
- **Master brand:** Ginkgo AI Systems
- **Product brand:** LEAF BY GINKGO
- **Category:** Agente de Atendimento Inteligente para WhatsApp
- **Positioning:** infraestrutura de atendimento e inteligência operacional, não um chatbot genérico.
- **Primary promise:** atender clientes 24 horas por dia, qualificar oportunidades e automatizar partes do atendimento.
- **Commercial model:** núcleo completo + módulos opcionais.
- **CTA principal:** Solicitar demonstração no WhatsApp.
- **WhatsApp comercial:** (41) 9562-3287

### Strategic sentence
**LEAF é o agente inteligente que atende seus clientes 24 horas por dia, qualifica oportunidades e automatiza o atendimento da sua empresa.**

### Expansion sentence
**Conforme sua operação cresce, você adiciona CRM, agenda, voz, memória, integrações e automações, pagando apenas pelo que realmente utiliza.**

---

# 1. Visual Theme & Atmosphere

## Core atmosphere
- Futurista, sóbrio, premium e operacional.
- Alta confiança, clareza comercial e sensação de tecnologia madura.
- Visual de software B2B real, não de “arte de inteligência artificial”.
- O produto deve parecer silencioso, competente e sempre ativo.
- Misturar precisão de SaaS, elegância editorial e evidência operacional.

## Visual metaphor
O LEAF deve parecer uma central de atendimento que continua funcionando quando o escritório apaga as luzes.

## Density
- Densidade média.
- Uma mensagem central por peça.
- Espaço negativo amplo.
- Interfaces e diagramas devem ser legíveis em telas pequenas.
- Evitar excesso de efeitos, brilho ou elementos competindo entre si.

## Image direction
Priorizar:
1. Capturas reais ou mockups fiéis do produto.
2. Conversas de WhatsApp estilizadas.
3. Diagramas simples de fluxo.
4. Antes/depois operacional.
5. Founder demo.
6. Pessoas reais em contextos de atendimento, vendas ou operação.

Evitar:
- Robôs humanoides.
- Cérebros digitais.
- Rostos artificiais genéricos.
- Mãos holográficas.
- Circuitos aleatórios.
- Cyberpunk genérico.
- Neon em excesso.
- Promessas visuais sem relação com o produto.

---

# 2. Color Palette & Roles

## Primary palette

| Token | Hex | Role |
|---|---:|---|
| `--bg-core` | `#090B0D` | Fundo principal |
| `--bg-surface` | `#111417` | Cards, barras e superfícies |
| `--bg-raised` | `#181C20` | Componentes elevados |
| `--text-primary` | `#F3F0E8` | Texto principal marfim |
| `--text-secondary` | `#A8B0B7` | Texto auxiliar |
| `--leaf-deep` | `#0E5A3B` | Verde institucional do LEAF |
| `--leaf-active` | `#19A66A` | Estados ativos, sucesso e inteligência |
| `--activity-blue` | `#2F7DF6` | Fluxos, atividade e integrações |
| `--ginkgo-gold` | `#C6A85B` | Assinatura sutil Ginkgo |
| `--border` | `#2A3036` | Bordas e separadores |
| `--danger` | `#E45D5D` | Alertas, uso raro |

## Usage proportions
- 65% fundos preto/grafite.
- 20% texto marfim e cinza.
- 10% verde LEAF.
- 4% azul de atividade.
- 1% dourado Ginkgo.

## Rules
- O dourado nunca deve dominar a peça.
- Verde indica inteligência ativa, disponibilidade e conclusão.
- Azul indica fluxo, conexão, agenda, CRM ou integração.
- Não usar gradientes multicoloridos.
- Gradientes permitidos:
  - grafite → preto;
  - verde profundo → transparência;
  - azul elétrico → transparência.
- Contraste mínimo deve priorizar leitura em dispositivos móveis.

---

# 3. Typography Rules

## Font families
- **Display:** Manrope, fallback Inter, sans-serif.
- **Body/UI:** Inter, fallback Arial, sans-serif.
- **Technical labels:** IBM Plex Mono, fallback monospace.

## Hierarchy
- H1: peso 700–800, tracking -2%, frases curtas.
- H2: peso 650–750.
- H3: peso 600.
- Body: peso 400–500.
- Labels: caixa alta moderada, tracking +4%, uso raro.
- Números e preços: tabular figures quando possível.

## Copy rhythm
- Headline: 4 a 9 palavras.
- Subheadline: até 22 palavras.
- Corpo de anúncio: blocos curtos, sem parágrafos densos.
- CTA: verbo de ação + resultado.

## Approved headline patterns
- **Seu WhatsApp fecha. Seus clientes não.**
- **Atendimento 24 horas sem ampliar a equipe.**
- **Não é um bot. É um agente operacional.**
- **Comece com atendimento. Expanda quando precisar.**
- **Seu próximo cliente pode chegar às 2h17.**
- **Transforme conversas em oportunidades organizadas.**

---

# 4. Component Stylings

## Buttons
### Primary
- Fundo `--leaf-active`.
- Texto preto.
- Raio 10px.
- Peso 700.
- Altura mínima 48px.
- Label preferencial: **Ver demonstração**.

### Secondary
- Fundo transparente.
- Borda `--border`.
- Texto marfim.
- Label preferencial: **Conhecer módulos**.

### WhatsApp CTA
- Ícone simples.
- Texto: **Falar com o LEAF** ou **Solicitar demonstração**.
- Não usar verde WhatsApp como cor dominante da marca; manter a paleta LEAF.

## Cards
- Fundo `--bg-surface`.
- Borda 1px `--border`.
- Raio 14px.
- Sombra discreta.
- Título curto.
- Uma evidência visual ou um benefício por card.

## Feature chips
- `24/7`
- `WhatsApp`
- `RAG`
- `Áudio`
- `Imagem`
- `Handoff humano`
- `Persona`
- `CRM opcional`

## Conversation component
- Simular conversas realistas, curtas e legíveis.
- Cliente à esquerda; LEAF à direita.
- Mostrar ação útil: responder, qualificar, consultar base, enviar material ou encaminhar.
- Nunca criar depoimentos falsos.
- Usar identificadores fictícios: “Cliente”, “LEAF”, “Atendente”.

## Module card
Cada módulo deve mostrar:
1. Nome.
2. Resultado.
3. Exemplo de uso.
4. Estado “Opcional”.
5. Preço configurável ou “Sob consulta”.

---

# 5. Layout Principles

## Grid
- Desktop: 12 colunas.
- Tablet: 8 colunas.
- Mobile: 4 colunas.
- Margem mínima: 24px.
- Espaçamento base: 8px.

## Spacing scale
`4, 8, 12, 16, 24, 32, 48, 64, 96`

## Facebook Feed
- Formato principal: 4:5.
- Zona segura: 8% nas bordas.
- Headline no terço superior.
- Produto ou conversa no centro.
- CTA visual no terço inferior.

## Square
- Formato auxiliar: 1:1.
- Usar para versões de compatibilidade e posts estáticos.

## Stories/Reels
- Formato: 9:16.
- Headline dentro da área central segura.
- Evitar textos próximos ao topo e à base.
- Uma ideia por cena.
- Duração sugerida para peças animadas: 8 a 15 segundos.

## Carousel
- Slide 1: interrupção/padrão.
- Slides 2–4: problema e mecanismo.
- Slide 5: solução LEAF.
- Slide 6: módulos ou CTA.
- Não ultrapassar 7 slides em campanhas de conversão.

---

# 6. Depth & Elevation

## Shadows
- Baixa intensidade.
- Usar para separar superfícies, não para decorar.
- Exemplo:
  - `0 8px 30px rgba(0,0,0,.28)`
  - `0 0 0 1px rgba(255,255,255,.04)`

## Glow
- Permitido apenas em estados ativos.
- Verde ou azul, opacidade baixa.
- Nunca aplicar glow em todos os elementos.

## Product focus
- Conversas, dados, fluxos e módulos devem parecer componentes de produto real.
- Elementos flutuantes precisam ter motivo funcional.

---

# 7. Do's and Don'ts

## Do
- Dizer “agente de atendimento”.
- Mostrar funcionamento real.
- Explicar o modelo modular.
- Usar linguagem direta e operacional.
- Falar de disponibilidade, organização, qualificação e integração.
- Criar contraste entre atendimento manual e operação assistida.
- Deixar claro que existe handoff humano.
- Usar “a partir de” somente quando houver preço real definido.
- Inserir disclaimers quando um resultado depender da implantação do cliente.

## Don't
- Não chamar de “bot”.
- Não prometer vendas garantidas.
- Não inventar percentuais de conversão.
- Não inventar depoimentos, logos ou métricas.
- Não sugerir substituição total da equipe humana.
- Não usar medo exagerado.
- Não transformar cada recurso técnico em headline.
- Não usar excesso de jargão.
- Não copiar sistemas visuais de outras marcas 1:1.
- Não usar “IA revolucionária” ou “o futuro chegou”.

---

# 8. Responsive Behavior

## Mobile-first
- Texto mínimo de 32px para headline em peças 1080px.
- Corpo mínimo de 22px em peças 1080px.
- Chips devem quebrar em no máximo duas linhas.
- Interfaces devem ser simplificadas para celular.
- Reduzir detalhes do dashboard em versões 1:1.

## Component collapse
- Módulos: 3 colunas → 1 coluna.
- Comparações: lado a lado → sequência vertical.
- Fluxos: horizontal → vertical.
- Botões: largura total em mobile.
- Conversas: manter no máximo 4 mensagens visíveis.

---

# 9. Agent Prompt Guide

## Master generation prompt
Crie um sistema de campanha para Facebook e Meta Ads do LEAF BY GINKGO usando este DESIGN.md como fonte de verdade.

Objetivo:
- Gerar demanda para um agente de atendimento inteligente no WhatsApp.
- Posicionar o LEAF como infraestrutura operacional, não como chatbot.
- Comunicar núcleo completo + módulos opcionais.
- Direcionar para uma demonstração no WhatsApp.

Entregáveis:
1. Uma página de revisão do sistema visual.
2. Seis posts estáticos 4:5.
3. Três carrosséis de seis slides.
4. Seis criativos de anúncios 4:5.
5. Versões 1:1 dos seis anúncios.
6. Três sequências 9:16 para Stories/Reels.
7. Uma biblioteca de componentes reutilizáveis.
8. Um quadro com headline, copy, CTA, público e estágio do funil.
9. Exportações organizadas por campanha.

Restrições:
- Não usar robôs, cérebros, hologramas ou cyberpunk genérico.
- Não inventar métricas, depoimentos ou resultados.
- Usar mockups realistas de WhatsApp, fluxos e interfaces.
- Manter a folha dourada Ginkgo como assinatura sutil.
- Usar português do Brasil.
- CTA para o WhatsApp: (41) 9562-3287.
- Headline curta e legível em celular.
- Criar peças visualmente distintas, mas pertencentes ao mesmo sistema.

## Variant prompts

### Executive variant
Reduza detalhes técnicos. Foque em disponibilidade, organização, qualificação, velocidade e expansão modular.

### Technical variant
Mostre RAG, multimodalidade, handoff, integrações, memória e automações em diagramas simples.

### Demonstration variant
Crie peças que simulem uma conversa curta: lead chega, LEAF entende a necessidade, consulta a base, envia material e encaminha para o atendente.

### Modular variant
Crie uma composição com núcleo LEAF no centro e módulos orbitando: CRM, agenda, voz, memória, ERP, automações e multicanal.

### Founder variant
Crie uma peça para vídeo ou imagem do fundador demonstrando o produto. Manter layout editorial e usar o produto como evidência principal.

---

# 10. Commercial Offer Architecture

## LEAF Essencial — núcleo
Inclui:
- Atendimento 24/7.
- WhatsApp.
- Respostas humanizadas.
- Qualificação de leads.
- Encaminhamento para atendente.
- Base de conhecimento RAG.
- Persona personalizada.
- Entendimento de texto, áudio e imagem.
- Envio de imagens, PDFs, catálogos e materiais.
- Histórico de conversas.

## Expansion modules
- **CRM:** pipeline, dados de leads, estágio e acompanhamento.
- **Agenda:** coleta de disponibilidade e agendamento.
- **Google Calendar:** sincronização e gestão de eventos.
- **Voz:** transcrição e respostas por áudio.
- **Memória avançada:** contexto persistente por cliente.
- **ERP/Sistema próprio:** consulta e atualização de dados.
- **Automações:** tarefas, alertas, follow-ups e processos.
- **Multicanal:** Instagram, Messenger e Webchat.

## Commercial rule
O núcleo precisa resolver o atendimento sozinho. Os módulos ampliam a operação; não corrigem um produto incompleto.

---

# 11. Approved CTAs

- Solicitar demonstração.
- Ver o LEAF atendendo.
- Falar com um especialista.
- Montar meu LEAF.
- Conhecer os módulos.
- Ativar atendimento inteligente.
- Quero testar no meu negócio.

## Prefilled WhatsApp message
Olá, vi a campanha do LEAF BY GINKGO. Quero uma demonstração do agente de atendimento para minha empresa.

---

# 12. Export Naming

Formato:
`LEAF_[FUNIL]_[CONCEITO]_[FORMATO]_[VARIANTE]_V01`

Exemplos:
- `LEAF_TOFU_WHATSAPP_ABERTO_4X5_A_V01`
- `LEAF_MOFU_BOT_VS_AGENT_CARROSSEL_V01`
- `LEAF_BOFU_DEMO_WHATSAPP_9X16_V01`

Pastas:
- `00_DESIGN_SYSTEM`
- `01_ORGANIC_POSTS`
- `02_META_ADS`
- `03_CAROUSELS`
- `04_STORIES_REELS`
- `05_COPY`
- `06_EXPORTS`
- `07_ARCHIVE`
