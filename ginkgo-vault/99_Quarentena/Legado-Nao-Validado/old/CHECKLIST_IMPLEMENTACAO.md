# Checklist de Implementação: Automação de Vídeos HeyGen + Ginkgo

## Fase 1: Preparação (1-2 dias)

### Credenciais e Acesso
- [ ] Criar conta HeyGen (heygen.com)
- [ ] Gerar API Key no HeyGen Dashboard
- [ ] Criar Photo Avatar "Nyra" no HeyGen
- [ ] Obter Avatar ID da Nyra
- [ ] Escolher Voice ID (português, feminino, natural)
- [ ] Testar acesso à API com curl:
  ```bash
  curl -X GET "https://api.heygen.com/v2/avatars" \
    -H "X-API-KEY: your-api-key"
  ```

### Banco de Dados
- [ ] Criar tabela `heygen_videos` no Supabase (ver SQL no documento)
- [ ] Testar conexão Supabase com credenciais
- [ ] Criar índices para melhor performance

### Ambiente n8n
- [ ] Acessar instância n8n (self-hosted ou cloud)
- [ ] Criar credencial HeyGen (HTTP Header Auth)
- [ ] Criar credencial OpenAI (API Key)
- [ ] Criar credencial Supabase

---

## Fase 2: Desenvolvimento (3-5 dias)

### Workflow 1: Geração de Vídeo
- [ ] Criar novo workflow no n8n
- [ ] Adicionar Webhook Trigger (ou Schedule)
- [ ] Adicionar nó HTTP Request para OpenAI (geração de script)
- [ ] Testar geração de script com dados de teste
- [ ] Adicionar nó HTTP Request para HeyGen (criação de vídeo)
- [ ] Testar criação de vídeo (verificar video_id retornado)
- [ ] Adicionar nó Supabase Insert (salvar metadados)
- [ ] Adicionar Error Handler
- [ ] Salvar e ativar workflow

### Workflow 2: Conclusão de Vídeo
- [ ] Criar novo workflow no n8n
- [ ] Adicionar Webhook Trigger (para callback do HeyGen)
- [ ] Adicionar nó Supabase Select (buscar registro)
- [ ] Adicionar nó Supabase Update (atualizar status)
- [ ] Adicionar nó HTTP Request (baixar vídeo)
- [ ] Adicionar nó Evolution API (enviar WhatsApp) OU Google Drive Upload
- [ ] Testar fluxo completo com webhook manual
- [ ] Salvar e ativar workflow

### Testes Unitários
- [ ] Testar geração de script com 3 prompts diferentes
- [ ] Testar criação de vídeo com script curto (< 30s)
- [ ] Testar webhook de conclusão com payload simulado
- [ ] Testar download de vídeo
- [ ] Testar envio via WhatsApp

---

## Fase 3: Integração (2-3 dias)

### HeyGen Webhook
- [ ] Configurar webhook global no HeyGen Dashboard OU
- [ ] Passar callback_url em cada requisição de criação
- [ ] Testar recebimento de webhook no n8n
- [ ] Verificar payload do webhook

### Integração com Brann
- [ ] Documentar como Brann receberá leads dos vídeos
- [ ] Configurar CTA (Call-to-Action) nos vídeos
- [ ] Testar fluxo: Vídeo → WhatsApp → Brann

### Integração com Alfred
- [ ] Documentar como Alfred receberá dados após fechamento
- [ ] Configurar passagem de dados entre Brann e Alfred

### Monitoramento
- [ ] Criar dashboard n8n com métricas:
  - Total de vídeos criados
  - Taxa de sucesso/falha
  - Tempo médio de geração
  - Custo estimado
- [ ] Configurar alertas para falhas

---

## Fase 4: Otimização (1-2 dias)

### Performance
- [ ] Implementar rate limiting (máximo 5 vídeos/hora)
- [ ] Adicionar retry logic (máximo 3 tentativas)
- [ ] Otimizar tamanho de payload

### Custo
- [ ] Calcular custo por vídeo (HeyGen + OpenAI + n8n)
- [ ] Implementar limite de gastos mensal
- [ ] Documentar ROI esperado

### Escalabilidade
- [ ] Testar com 100 vídeos/mês
- [ ] Testar com 1000 vídeos/mês
- [ ] Documentar limites da arquitetura

---

## Fase 5: Produção (1 dia)

### Deploy
- [ ] Ativar workflows em produção
- [ ] Configurar logs e alertas
- [ ] Documentar runbook de troubleshooting

### Treinamento
- [ ] Treinar time sobre como usar a automação
- [ ] Documentar como adicionar novos clientes/ideias
- [ ] Documentar como monitorar vídeos

### Documentação
- [ ] Documentar todos os endpoints utilizados
- [ ] Documentar estrutura de dados
- [ ] Documentar fluxo completo com screenshots

---

## Fase 6: Análise e Melhoria (Contínuo)

### Métricas
- [ ] Rastrear taxa de clique dos vídeos
- [ ] Rastrear taxa de conversão (vídeo → lead → cliente)
- [ ] Rastrear tempo de geração vs. custo
- [ ] Rastrear satisfação com qualidade dos vídeos

### Iterações
- [ ] A/B testar diferentes prompts da Nyra
- [ ] A/B testar diferentes avatares
- [ ] A/B testar diferentes vozes
- [ ] Refinar script baseado em performance

---

## Recursos Necessários

### Arquivos Fornecidos
- [x] `arquitetura_heygen_ginkgo.md` - Visão geral da arquitetura
- [x] `implementacao_heygen_n8n.md` - Guia passo a passo de implementação
- [x] `heygen_python_examples.py` - Exemplos de código Python
- [x] `fluxo_heygen.png` - Diagrama visual do fluxo

### Ferramentas Necessárias
- n8n (self-hosted ou cloud)
- HeyGen (conta + API Key)
- Supabase (projeto + credenciais)
- OpenAI (API Key)
- Evolution API (para WhatsApp)
- Google Drive (opcional, para armazenar vídeos)

### Conhecimento Necessário
- Básico de APIs REST
- Básico de n8n (workflows, nós, credenciais)
- Básico de SQL (para Supabase)
- Básico de webhooks

---

## Estimativa de Tempo

| Fase | Tempo | Responsável |
| :--- | :--- | :--- |
| 1. Preparação | 1-2 dias | DevOps/Admin |
| 2. Desenvolvimento | 3-5 dias | Engenheiro n8n |
| 3. Integração | 2-3 dias | Engenheiro n8n + Brann |
| 4. Otimização | 1-2 dias | Engenheiro n8n |
| 5. Produção | 1 dia | DevOps/Admin |
| **Total** | **8-13 dias** | |

---

## Custos Estimados (Mensal)

| Item | Custo | Notas |
| :--- | :--- | :--- |
| HeyGen | $15-50 | 100-300 vídeos |
| OpenAI | $1-5 | Geração de scripts |
| n8n | $10-50 | Plano starter ou pro |
| Supabase | $5-25 | Incluído no starter |
| Evolution API | $0-50 | Depende do volume WhatsApp |
| **Total** | **$31-180** | Escalável com volume |

---

## Troubleshooting Comum

### Problema: HeyGen retorna erro 401
**Solução**: Verificar se a API Key está correta e não expirou. Gerar nova chave no dashboard.

### Problema: Vídeo fica em status "pending" indefinidamente
**Solução**: Verificar limites de taxa (rate limiting). Aguardar ou contatar suporte HeyGen.

### Problema: Webhook do HeyGen não é recebido
**Solução**: Verificar se a URL do webhook está acessível publicamente. Testar com ngrok se em localhost.

### Problema: Script gerado pelo OpenAI é muito longo
**Solução**: Reduzir `max_tokens` no prompt ou adicionar validação de comprimento.

### Problema: Vídeo tem qualidade ruim
**Solução**: Aumentar resolução (width/height) ou escolher outro avatar/voz.

---

## Próximas Melhorias

- [ ] Integrar com Canva para adicionar gráficos/textos nos vídeos
- [ ] Suporte a múltiplos idiomas (tradução automática)
- [ ] Geração de thumbnails customizados
- [ ] Publicação automática em Reels/TikTok
- [ ] Analytics dashboard em tempo real
- [ ] A/B testing automático de scripts

---

**Versão**: 1.0  
**Data**: 22 de Março de 2026  
**Autor**: Manus AI  
**Status**: Pronto para Implementação
