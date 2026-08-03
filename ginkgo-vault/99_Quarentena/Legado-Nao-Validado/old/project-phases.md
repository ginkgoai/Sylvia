# Roadmap do Projeto S+ (Shion)

Este documento define as fases de implementação do Projeto S+, desde a configuração inicial até a operação autônoma avançada.

## Fase 1: Fundação (Semanas 1-2)
**Objetivo:** Estabelecer a infraestrutura base e a comunicação primária.

- [x] Definição da arquitetura do sistema.
- [x] Criação do repositório GitHub (`gingkosystems/ginkgo-s-plus`).
- [ ] Provisionamento da VPS (Ubuntu 22.04+).
- [ ] Instalação do Node.js 24+ e dependências.
- [ ] Instalação e configuração do Openclaw Gateway.
- [ ] Configuração do bot no Telegram via `@BotFather`.
- [ ] Configuração de segurança (allowlist com ID do Telegram do Gabriel).
- [ ] Teste de comunicação básica (ping/pong) via Telegram.

## Fase 2: Voz e Personalidade (Semanas 3-4)
**Objetivo:** Implementar a comunicação bidirecional por linguagem natural.

- [ ] Criação de conta e obtenção de API Key na ElevenLabs.
- [ ] Desenvolvimento do plugin STT (Speech-to-Text) para processar áudios do Telegram.
- [ ] Desenvolvimento do plugin TTS (Text-to-Speech) usando ElevenLabs.
- [ ] Configuração da voz (clonagem ou seleção de voz premium).
- [ ] Integração do fluxo de áudio no loop do agente Openclaw.
- [ ] Testes de latência e qualidade de transcrição/geração.

## Fase 3: Memória Estruturada (Semanas 5-6)
**Objetivo:** Conectar o agente ao Obsidian para atuar como sistema de pensamento externo.

- [ ] Configuração do vault do Obsidian na VPS (ou sincronização segura com local).
- [ ] Desenvolvimento do plugin de integração Openclaw <-> Obsidian.
- [ ] Implementação da lógica de leitura (index -> mocs -> methods -> claims).
- [ ] Implementação da lógica de escrita (type, agent, relevance, etc.).
- [ ] Testes de criação de logs automáticos após execuções.
- [ ] Implementação da regra de compressão (anti-caos) para nodes similares.

## Fase 4: Acesso e Automação (Semanas 7-8)
**Objetivo:** Conceder acesso profundo ao sistema e iniciar a automação de tarefas.

- [ ] Habilitação e configuração segura da ferramenta `exec` no Openclaw.
- [ ] Habilitação da ferramenta `browser` para automação web.
- [ ] Configuração de túnel seguro (ex: Tailscale) entre VPS e computador local.
- [ ] Criação de scripts de automação base (ex: deploy de containers Docker).
- [ ] Testes de execução de comandos shell via linguagem natural (Telegram).
- [ ] Auditoria de segurança e revisão de logs no Obsidian.

## Fase 5: Evolução e Skills (Contínuo)
**Objetivo:** Expandir as capacidades do agente através de novas integrações.

- [ ] Desenvolvimento de skill para integração com Supabase (banco de dados principal).
- [ ] Desenvolvimento de skill para integração com n8n (orquestração de fluxos complexos).
- [ ] Desenvolvimento de skill para integração com Evolution API (WhatsApp).
- [ ] Refinamento contínuo dos prompts e do grafo de conhecimento no Obsidian.
- [ ] Monitoramento de performance e otimização de custos (APIs).
