# Guia de Implementação: Projeto S+ (Shion)

Este guia detalha os passos práticos para implementar a arquitetura do Projeto S+, integrando Openclaw, ElevenLabs, Obsidian e acesso total ao sistema.

## Fase 1: Configuração Base do Openclaw

O primeiro passo é garantir que o ambiente base esteja configurado corretamente na VPS.

1. **Instalação do Node.js**: Certifique-se de ter o Node.js versão 24+ instalado.
2. **Instalação do Openclaw**: Execute o script de instalação oficial (`curl -fsSL https://openclaw.ai/install.sh | bash`).
3. **Configuração do Gateway**: Inicialize o gateway com `openclaw onboard --install-daemon`.
4. **Configuração do Telegram**:
   - Crie um bot no `@BotFather` e obtenha o token.
   - Configure o arquivo `config.yaml` do Openclaw para habilitar o canal Telegram.
   - Defina a política de DM (`dmPolicy`) como `allowlist` e adicione seu ID numérico do Telegram para garantir acesso exclusivo.

## Fase 2: Integração com ElevenLabs (Voz)

Para habilitar a comunicação por voz natural, precisamos integrar a API da ElevenLabs.

1. **Obtenção da API Key**: Gere uma chave de API no painel da ElevenLabs.
2. **Desenvolvimento do Plugin (Skill)**:
   - Crie um plugin para o Openclaw que intercepte mensagens de áudio do Telegram.
   - Utilize a API de Speech-to-Text (STT) para transcrever o áudio para texto.
   - Passe o texto transcrito para o agente cognitivo (Shion).
   - Quando o agente decidir responder por voz, utilize a API de Text-to-Speech (TTS) da ElevenLabs para gerar o áudio.
   - Envie o arquivo de áudio gerado de volta para o usuário via Telegram.

## Fase 3: Integração com Obsidian (Memória)

O Obsidian atuará como a memória estruturada do agente.

1. **Configuração do Vault**: Crie um vault do Obsidian na VPS ou configure a sincronização com seu vault local.
2. **Desenvolvimento do Plugin (Skill)**:
   - Crie um plugin para o Openclaw que permita leitura e escrita de arquivos Markdown no vault.
   - Implemente a lógica de "Gatilhos de Leitura" (consultar o cofre antes de agir).
   - Implemente a lógica de "Gatilhos de Escrita" (registrar claims, methods, logs e insights).
   - Garanta que o plugin respeite a estrutura mínima de cada node (type, agent, relevance, created_at, linked_to) e o uso obrigatório de wikilinks.

## Fase 4: Acesso Total ao Sistema

Para que o agente atue como um "copiloto operador", ele precisa de acesso profundo ao sistema.

1. **Exec Tool**: Habilite e configure a ferramenta nativa `exec` do Openclaw para permitir a execução de comandos shell na VPS.
2. **Browser Tool**: Habilite a ferramenta de automação web para interações com painéis e sites.
3. **Acesso ao Computador Local**:
   - Configure um túnel seguro (ex: SSH reverso, Tailscale, ou Cloudflare Tunnels) entre a VPS e seu computador local.
   - Alternativamente, instale uma instância secundária do Openclaw (como sub-agente) na sua máquina local, conectada ao Gateway na VPS.

## Fase 5: Refinamento e Evolução

Com a base estabelecida, o foco muda para a evolução contínua.

1. **Criação de Skills**: Desenvolva novas skills (plugins) para tarefas específicas (ex: deploy de containers, análise de logs, integração com APIs externas).
2. **Compressão de Conhecimento**: Implemente a regra de compressão no Obsidian (consolidar 3+ nodes similares em um novo method).
3. **Monitoramento**: Acompanhe os logs de execução e refine os prompts do sistema para melhorar a tomada de decisão do agente.
