# Heartbeat — proatividade programada da Sylvia

> Rotinas que rodam sem o fundador pedir. Regra de ouro: silêncio vale mais que ruído — sem novidade relevante, responder `HEARTBEAT_OK` e não notificar.

## Diário (manhã, dias úteis)

**Briefing executivo** (1 mensagem, curta, no canal principal):
1. Caixa/lucro e pendências financeiras (se houver dado novo em `70_Financeiro/`).
2. Saúde do Leaf e da operação (erros, clientes, sinais do n8n/status quando conectados).
3. Agenda e compromissos do dia; tarefas em aberto no CHECKPOINT/HANDOFF.
4. Calendário de conteúdo: o que deveria sair hoje por canal (`operacao/`).
5. Alertas: riscos, prazos, incoerências detectadas.
6. **Uma recomendação**: a próxima decisão de maior alavancagem.

## Semanal

1. **Triagem de clippings** (`cognicao/TRIAGEM_CLIPPINGS.md`) até Inbox zerado ou teto de esforço.
2. **Consolidação de memória** (`cognicao/MEMORIA.md`): índices, duplicatas, CHECKPOINT fiel.
3. **Revisão de canais**: cadência real vs. calendário planejado por conta (`operacao/CONTAS_E_CANAIS.md`).
4. **Financeiro**: fechamento semanal simples — entradas, saídas, queima, projeção (`operacao/FINANCEIRO.md`).
5. **Relatório semanal** ao fundador: feito, aprendido, travado, proposta da semana seguinte.

## Mensal

1. Auditoria de acessos e segredos: credenciais órfãs, tokens a rotacionar, permissões excessivas.
2. Revisão da constituição e runbooks: propostas de emenda se a prática divergiu do texto.
3. Revisão de portfólio: cada frente ativa com margem, esforço, aprendizado e veredito (seguir/ajustar/pausar).

## Implementação

No OpenClaw: heartbeat nativo + cron para as rotinas com horário fixo. Enquanto o runtime não estiver ativo, as rotinas podem rodar como tarefas agendadas no Claude ou manualmente em sessão de oficina — o protocolo é o mesmo.
