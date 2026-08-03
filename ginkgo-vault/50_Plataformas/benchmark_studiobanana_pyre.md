# Benchmark + Reverse — Studio Banana → StudioPyre (2026-07-16)

> Referência: [studiobanana.app](https://studiobanana.app/) e dashboard. Este teardown serve ao **PYRE / StudioPyre**, não é uma especificação para copiar o produto, sua marca, seus ativos, textos ou código.

> Escopo e método: leitura do material público (landing, sitemap, termos, privacidade e bundle web), da tela autenticada fornecida pelo usuário e dos assets públicos carregados pelo app. Não foram acessados dados de outros usuários, credenciais, cookies, contas, APIs protegidas ou mecanismos de autenticação. Coleta em 2026-07-16 (BRT).

## 0. Decisão em uma frase

**Studio Banana é uma ótima referência de “estúdio criativo que faz a pessoa criar já”; o StudioPyre deve absorver a sua clareza de entrada, biblioteca, templates e metering, mas ser superior em contexto de marca, governança, evidência e integração correta com WAVE e LEAF.**

O insight principal não é “ter mais geradores”. É reduzir a tela em branco:

```text
intenção do criador → atalho/template → briefing pequeno → custo explícito
→ job com estado real → ativo versionado → aprovação → handoff ao WAVE
```

## 1. Evidência, confiança e limites

| Nível | Base | Uso neste documento |
|---|---|---|
| Confirmado | Landing, páginas públicas, CSS e bundle público | planos, créditos, módulos expostos, navegação, tokens e padrões de cliente |
| Observado | Dashboard na captura fornecida | composição da tela, hierarquia, cards, estado vazio e microcopy |
| Inferência técnica | Estruturas visíveis no cliente, sem chamada a operações protegidas | entidades, jobs assíncronos e recomendações de arquitetura |
| Fora de escopo | Dados privados e serviços internos | nenhuma afirmação sobre banco, modelos, prompts proprietários, custos reais ou controles de servidor |

Fontes de referência: [landing e planos](https://studiobanana.app/#planos), [sitemap](https://studiobanana.app/sitemap.xml), [termos](https://studiobanana.app/termos), [privacidade](https://studiobanana.app/privacidade) e [bundle público do app](https://studiobanana.app/assets/index-CoB-EmMw.js).

## 2. O que é o Studio Banana

É um estúdio de criação multimodal para criadores: imagem, vídeo, influencer virtual, voz, lip sync, clonagem de voz e transcrição. A proposta é concentrar vários efeitos de IA em uma mesma superfície, com saldo de créditos compartilhado e uma biblioteca como destino dos resultados.

O produto comercializa três planos mensais públicos:

| Plano | Preço público | Créditos/mês | Leitura de produto |
|---|---:|---:|---|
| Starter | R$ 99 | 1.200 | entrada para experimentação multimodal |
| Creator | R$ 169 | 2.300 | produção recorrente e variações em escala |
| Pro | R$ 269 | 4.000 | volume, pastas compartilhadas e workflows avançados |

O modelo de negócio é coerente com a categoria: uma única carteira de créditos para vários efeitos, planos que comunicam capacidade de produção e um upgrade sempre visível no shell do aplicativo.

## 3. Arquitetura de experiência que funciona

### Shell do aplicativo

```text
Sidebar fixa
├─ Dashboard
├─ Biblioteca
├─ Prompts (badge “novo”)
├─ Criar: Influencer · Imagens · Vídeos
├─ Ferramentas: Lip Sync · Clonagem de Voz · Transcrição
└─ Tutorial · Conta/perfil

Topbar
├─ plano / upgrade
├─ saldo de créditos e consumo
├─ notificações
└─ perfil

Área central
├─ hero de boas-vindas + CTA primário
├─ ferramentas rápidas em cards
└─ criações recentes / estado vazio / novo projeto
```

A home resolve as duas perguntas certas, nesta ordem:

1. **O que eu consigo criar agora?** — hero e atalhos por resultado.
2. **Onde está o que já fiz?** — biblioteca e criações recentes.

Essa ordem é melhor que abrir num painel de configuração ou numa galeria vazia. Ela reduz decisão, promove a primeira geração e mantém continuidade depois da primeira entrega.

### Dashboard observado

- Hero largo, com saudação pessoal, promessa curta e uma única ação dominante.
- Carrossel de atalhos orientados a resultado: conteúdo de produto, imagem→vídeo, imagens, movimento curto e take profissional.
- Cada card tem thumbnail, título, benefício em uma frase e CTA textual; não expõe o modelo de IA como decisão inicial.
- Área de recentes usa estado vazio útil: explica a ausência de criações e oferece um tile de novo projeto.
- Créditos, plano e notificações estão sempre acessíveis, sem tirar foco da criação.
- Um tour guiado explica as áreas em contexto, em vez de exigir documentação antes do primeiro resultado.

### Sistema visual observável

| Token | Referência pública observada | Tradução recomendada para StudioPyre |
|---|---|---|
| Layout | sidebar de 264 px; topbar de 76 px | sidebar desktop de 264 px; drawer abaixo de 1024 px |
| Fundo | creme claro e superfícies brancas | carvão muito claro / névoa, com superfícies grafite suaves |
| Acento | amarelo-ouro e variantes claras | brasa laranja/âmbar própria do PYRE; não usar o amarelo Banana |
| Raios | 10 / 16 / 22 / 28 px e pills | preservar a escala, com hero mais editorial |
| Sombra | quente, pequena e difusa | sombra de brasa discreta; não usar glow em todos os elementos |
| Hierarquia | título forte, corpo curto, CTA único | mesma economia verbal, com identidade e copy Nyra próprias |

O app também declara breakpoints de tablet/mobile e navegação inferior em telas pequenas. Para o StudioPyre, a regra é: sidebar vira drawer, hero reduz a arte antes de esconder o CTA, e cards viram scroll horizontal ou grid de duas colunas conforme a largura.

## 4. Inventário funcional público

| Capacidade exposta | Padrão de produto observado | Oportunidade StudioPyre |
|---|---|---|
| Imagens | geração e histórico de ativos | P1: imagem + carrossel com marca, versão e evidência |
| Vídeos | geração por intenção, imagem→vídeo e variações | P3: roteiro primeiro; vídeo só após custo/briefing aprovados |
| Influencer/avatar | personagem reutilizável e posts associados | tratar como identidade/asset com consentimento e marca por tenant |
| Voz | TTS, clonagem e lipsync | voz/clonagem com prova de consentimento, escopo e expiração |
| Transcrição | áudio/vídeo → texto | entrada para roteiro, legenda e reaproveitamento 1→N |
| Biblioteca | listagem, download, pastas e compartilhamento | projetos + ativos + versões; compartilhamento por org e papel |
| Prompts | superfície própria para reutilização | banco de hooks e templates governados por tenant, não prompt solto |
| Pagamentos e créditos | carteira compartilhada, planos, histórico | ledger GTK, reserva, débito, estorno e evidência por job |
| Notificações | conclusão e estado de conta | eventos reais de job/aprovação/handoff, nunca mensagens de vaidade |
| Tutorial | coach marks dentro do produto | onboarding por tarefa: marca → primeiro roteiro → primeiro ativo → aprovação |

O cliente público também revela recursos típicos de job assíncrono para mídia e atualização de eventos em tempo real. Isso confirma o padrão de UX desejável: a tela não deve simular “pronto”; deve exibir `na fila`, `processando`, `concluído`, `falhou` ou `cancelado` com evidência e ação possível.

## 5. Reverse técnico — somente a superfície pública

### Arquitetura visível

- SPA em React entregue por CDN, com Cloudflare na borda e telemetria web.
- Autenticação, mídia, voz, biblioteca/pastas, uploads, pagamentos, notificações e afiliados aparecem como domínios de recurso separados no cliente.
- Geração de imagem e vídeo é modelada como recurso persistente, com histórico, download e eventos de atualização; não como resposta síncrona de um único prompt.
- Uploads usam URL pré-assinada, padrão adequado para enviar mídia sem transformar o servidor de aplicação em proxy de arquivos grandes.
- A interface menciona PIX e cartão e mostra conta, plano, créditos e histórico de consumo como entidades de produto de primeira classe.

### Observações de segurança que **não** devemos copiar

O bundle público indica uso de token bearer guardado no armazenamento do navegador. Isso não é um achado explorado nem uma alegação sobre o servidor; é uma decisão visível no cliente e um sinal para evitarmos a mesma dependência no StudioPyre. Para o nosso produto:

- preferir sessão por cookie `HttpOnly`/`Secure` + proteção CSRF, ou BFF; não expor token de longa duração ao JavaScript;
- aplicar CSP restritiva, rotação/revogação de sessão e trilha de auditoria;
- emitir URL pré-assinada apenas após autorização por org, tipo, tamanho, MIME e janela de expiração;
- nunca deixar Nyra, frontend ou job worker escolher segredo, provedor ou orçamento sem passar pela Boundary.

### Modelo de recursos que a referência sugere

| Recurso | Papel no StudioPyre | Fonte de verdade |
|---|---|---|
| `Project` | contexto de campanha/peça, objetivo e marca | `ginkgo-tree`, isolado por org |
| `Asset` | imagem, vídeo, áudio, roteiro ou carrossel versionado | object storage + registro/evidence |
| `GenerationJob` | unidade assíncrona com provider, custo e status | Boundary/Laplace + ledger GTK |
| `PromptTemplate` | hook, roteiro, formato e variáveis aprovadas | registry por tenant |
| `BrandContext` | pilares, tom, público e restrições | RAG governado por tenant |
| `Approval` | decisão humana sobre rascunho, edição e handoff | evento auditável |
| `CreditLedger` | reserva, débito, estorno e consumo real | ledger imutável por org |
| `DistributionHandoff` | ponteiro de ativo aprovado entregue ao WAVE | evidence do seam, não publicação no PYRE |

## 6. O que roubar — princípios, não aparência

1. **Entrada por intenção.** “Criar vídeo de produto” é melhor que abrir um formulário de parâmetros de modelo. O criador escolhe a tarefa; a plataforma propõe defaults seguros.
2. **Uma ação primária por contexto.** O hero não tenta vender dez caminhos. No StudioPyre, o CTA deve ser `Criar projeto` ou `Criar roteiro`, conforme maturidade do usuário.
3. **Templates que entregam resultado.** Cards devem partir de objetivo de negócio: anúncio, vídeo de produto, carrossel educativo, prova social real, roteiro de Reel, reaproveitar um conteúdo.
4. **Biblioteca separada da criação.** Dashboard é decisão e continuidade; Biblioteca é busca, filtro, versão, download e aprovação.
5. **Crédito sempre visível.** O custo não pode ser surpresa: mostrar saldo, estimativa antes da geração e débito/estorno comprovado depois dela.
6. **Tour contextual.** Não explicar a plataforma inteira; levar o usuário ao primeiro ativo aprovado em poucos passos.
7. **Jobs com estado verdadeiro.** Atualização progressiva é boa UX apenas quando vem de evento/worker real; percentual fictício viola honest-data.
8. **Mobile pensado como tarefa curta.** Navegação inferior só para as ações de maior frequência; review e governança precisam continuar possíveis no celular.

## 7. O que não copiar

| Não copiar cru | Por quê | Decisão PYRE |
|---|---|---|
| Mascote, paleta, ilustrações, textos e nomes de templates | marca e expressão protegidas, além de confundirem posicionamento | linguagem visual de brasa/grafite e Nyra própria |
| “estúdio genérico de muitos botões” | vira catálogo de modelos sem estratégia | pilares, briefing, roteiro e projeto como camada de intenção |
| Geração sem orçamento explícito | mídia multimodal é vetor de custo alto | reserva GTK + cap por org + confirmação para exceções R3 |
| Status otimista ou marketing de performance | quebra honest-data | somente estado comprovado por Evidence/ingest |
| Publicação como extensão natural da geração | atuar em nome da marca é efeito externo | PYRE aprova e entrega; WAVE agenda/distribui/mede |
| Clonagem de voz/identidade sem prova | risco de consentimento, fraude e marca | consentimento verificável, finalidade, expiração e audit trail |
| Conteúdo adulto como atalho de receita | amplia risco de segurança, moderação e compliance | fora do escopo do MVP; qualquer avaliação futura exige política própria e controles fortes |
| Token durável acessível ao JavaScript | superfície maior para XSS/exfiltração | sessão endurecida, BFF/cookies e cofre |
| Urgência artificial, contadores e “gamificação” enganosa | fere a doutrina honest-data | progresso só quando é mensurável e auditável |

## 8. Reverse para o StudioPyre

### A fronteira não muda

```text
Nyra propõe e cria rascunhos
        ↓  (Task + orçamento + segredo no cofre + Evidence)
Laplace / Boundary executa o efeito de geração
        ↓
PYRE armazena ativo, versão e aprovação
        ↓  (ponteiro do ativo aprovado)
WAVE distribui, agenda e mede
        ↓
LEAF / Callima atende e converte
```

**PYRE cria → WAVE distribui/mede → LEAF converte.** Esta é a diferença estrutural: a referência concentra o estúdio; o nosso produto compõe uma suíte governada sem virar um bundle confuso.

### Home proposta

```text
StudioPyre / Visão geral
├─ Hero: “O que vamos criar para [marca]?” + Criar projeto
├─ Contexto ativo: objetivo, marca, pilares e saldo GTK
├─ Começar por objetivo
│  ├─ Roteiro de Reel (P0)
│  ├─ Imagem / carrossel (P1)
│  ├─ Calendário 30 dias (P2)
│  ├─ Vídeo / edição (P3)
│  └─ Reaproveitar ativo (P2)
├─ Fila de revisão: rascunhos aguardando decisão
├─ Projetos recentes: status e última evidência
└─ Atividade: somente eventos reais (gerou, falhou, aprovou, entregou)
```

### Cards de início — versão StudioPyre

| Card | Entrada mínima | Saída | Custo e governança |
|---|---|---|---|
| Roteiro de Reel | objetivo, público e CTA | Hook (3s) → desenvolvimento → CTA | P0; sem efeito externo |
| Carrossel de autoridade | tema + marca | roteiro de slides + assets | P1; estimativa/reserva GTK |
| Criativo de produto | foto + benefício real | imagem/variações e copy | P1; prova de claim e aprovação |
| Reaproveitar conteúdo | URL/arquivo autorizado | snippets, carrossel, roteiro curto | P2; origem e direitos registrados |
| Vídeo de campanha | roteiro aprovado + assets | job de vídeo e versões | P3; cap, fila e estado real |
| Enviar ao WAVE | ativo aprovado + canais-alvo | handoff rastreável | P4; não publica no PYRE |

Cada card deve mostrar antes de executar: tipo de entrada aceito, duração típica/estado da fila, faixa de GTK, política de retry e o que será salvo no projeto.

### Design system próprio

- **Tom:** criativo, preciso e um pouco mais profissional que “divertido”; Nyra é guia, não mascote decorativo.
- **Paleta:** grafite, carvão, cinza quente e brasa/laranja em pontos de ação; fundo claro opcional para revisão de mídia.
- **Semântica de cor:** brasa = ação; azul/cinza = informação; verde = efeito concluído com evidência; amarelo não é estado universal.
- **Arte:** previews dos ativos do tenant e ilustrações abstratas próprias; nunca recriar o macaco, banana ou composição da referência.
- **Acessibilidade:** contraste AA, foco evidente, texto além de ícones, redução de movimento e estados de job anunciáveis por leitor de tela.

## 9. Fluxos e máquinas de estado

### Fluxo de criação

```text
briefing → rascunho → [aprovar geração] → reservado → na_fila
→ processando → concluído | falhou | cancelado
→ revisão → aprovado | ajustes_solicitados | arquivado
→ enviado_ao_wave (P4) → status externo recebido do WAVE
```

Regras:

- `rascunho` não consome provider pago.
- `reservado` cria intenção financeira e mostra o máximo que pode ser debitado.
- somente a Boundary move o job para `na_fila` ou chama um provedor.
- `concluído` exige ponteiro de output e Evidence; não basta callback de texto.
- falha atribuível ao provider libera a reserva/estorna segundo a política registrada.
- `aprovado` é decisão humana auditável; nunca inferir aprovação por download.
- `enviado_ao_wave` contém um ponteiro para o ativo; o PYRE não agenda, publica ou inventa métricas.

### Contrato de dashboard mínimo

| Bloco | Dados reais necessários | Empty state correto |
|---|---|---|
| Saldo GTK | disponível, reservado, gasto no período e próximo reset | “Sem créditos disponíveis” + caminho de recarga, sem urgência falsa |
| Projetos recentes | título, objetivo, ativo mais recente, status, data e ator | convite para criar o primeiro projeto |
| Fila de revisão | ativo, versão, custo real, origem e decisão requerida | “Nada aguardando sua revisão” |
| Atividade | evento, timestamp, Evidence e link ao recurso | não renderizar feed decorativo |
| Marca/pilares | contexto ativo, fonte e data de atualização | wizard curto para configurar a marca |

## 10. Fatias de entrega — referência sem desviar o roadmap

| Fase canônica | O que incorporar da referência | Entrega StudioPyre | Critério de aceite |
|---|---|---|---|
| P0 | hero, atalhos e templates orientados a resultado | roteiro Hook→Desenvolvimento→CTA + banco de hooks + projeto | rascunho tenant-scoped, sem geração paga, status honesto |
| P1 | geração como job e biblioteca | imagem/carrossel versionado com reserva GTK | cap por org, output salvo, estorno comprovado em falha |
| P2 | continuidade e reaproveitamento | calendário 30 dias + 1→N | plano e ativos ligados a pilares, aprovação por item |
| P3 | superfícies de vídeo/voz | vídeo/Reel e edição a partir de roteiro aprovado | fila, timeout, retry, custo e Provenance visíveis |
| P4 | biblioteca como ponto de handoff | envio de ativo aprovado ao WAVE | apenas ponteiro/evidence; nenhuma publicação dentro do PYRE |
| P5 | conveniência de distribuição | publicação orgânica opt-in, se ainda fizer sentido | HITL default, risco/tenant policy e trilha completa |

## 11. Backlog de implementação imediato

1. Criar a rota de visão geral com o shell StudioPyre, saldo GTK, contexto de marca e `Criar roteiro` como CTA único.
2. Modelar `Project`, `Asset`, `GenerationJob`, `Approval` e `CreditLedger` antes de adicionar mais geradores.
3. Implementar P0 vertical: pauta por pilares → roteiro → versão → aprovação/revisão → histórico por org.
4. Criar a Biblioteca com filtros por tipo, status, projeto e data; download/export só para ativos autorizados.
5. Desenhar o componente de custo: estimativa, reserva, consumo real, falha, estorno e Evidence.
6. Definir a Boundary para geração P1 antes de plugar qualquer provedor de imagem/vídeo.
7. Adicionar onboarding contextual de no máximo quatro passos, com opção de pular e reabrir.
8. Especificar consentimento e retenção para voz, avatar, uploads e material de marca antes de habilitar clonagem/identidade.

## 12. Métricas de produto que respeitam honest-data

| Métrica | Definição evidenciável | Não medir como verdade |
|---|---|---|
| Time-to-first-draft | tempo entre projeto criado e rascunho salvo | abertura de tela ou clique em CTA |
| Time-to-approved-asset | tempo entre briefing e aprovação humana | geração “iniciada” |
| Taxa de conclusão de job | jobs com output/Evidence ÷ jobs iniciados | animação de progresso exibida |
| Custo por ativo aprovado | GTK debitado líquido ÷ ativos aprovados | crédito reservado sem conclusão |
| Reaproveitamento 1→N | derivados aprovados ligados ao asset de origem | downloads sem relação de origem |
| Handoff ao WAVE | ativos aprovados entregues com evidence | posts “no ar” sem confirmação do WAVE |

## 13. Perguntas que precisam de decisão antes do P1

- Quais provedores entram no cofre compartilhado e quais ficam disponíveis em BYO enterprise?
- Qual é a tabela inicial de GTK por operação, reserva e política de retry/estorno?
- Quem pode aprovar, editar e enviar ao WAVE em cada papel da org?
- Qual é o esquema de consentimento para voz, rosto, materiais enviados e conteúdo de terceiros?
- Quais claims de marca podem ser usados na copy sem Evidence/RAG validado?
- Quais formatos de exportação e retenção são necessários no MVP?

---

**Conclusão:** adotar a gramática de UX do Studio Banana — criar rápido, ver custo, recuperar trabalho e aprender no fluxo — é correto. O StudioPyre deve elevar isso com contexto de marca, projeto/versão, controle de gasto, consentimento, aprovação e a separação disciplinada entre criar (PYRE), distribuir/medir (WAVE) e converter (LEAF).

_Mantido pela Sexta-feira. Documento de benchmark de produto; não é evidência de que funcionalidades externas, integrações ou estados internos estejam disponíveis para uso._
