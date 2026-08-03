# BOOT — comece sempre por aqui (continuidade da Sexta-feira)

> Objetivo: NUNCA recomeçar do zero. Toda janela nova lê esta memória, retoma
> exatamente de onde parou e segue se auto-corrigindo.

## Ordem de leitura ao iniciar uma sessão
1. **BOOT.md** (este) — protocolo.
2. **STATE.md** — estado vivo: o que está feito, em andamento e o PRÓXIMO passo.
3. **LEARNINGS.md** — erros já cometidos + correções (não repetir).
4. **ENV.md** — paths, IDs, endpoints, credenciais (nomes/IDs, sem segredos).
5. **DECISIONS.md** — decisões de arquitetura e porquê.
6. **ROADMAP.md** — critérios da Fase 1 e fases futuras.
7. `checkpoints/` — diário append-only (histórico/auditoria) se precisar de detalhe.

## Protocolo de trabalho (a cada passo)
- **Antes de agir:** confirme em STATE.md onde paramos e em LEARNINGS.md se já
  erramos isso antes.
- **Ao concluir um passo:** (a) atualize STATE.md (mova de "em andamento" p/
  "feito" e defina o próximo); (b) anexe 1 entrada em `checkpoints/` com data,
  o que foi feito, evidência e próximo passo.
- **Ao tomar decisão de arquitetura:** registre em DECISIONS.md (decisão + porquê + alternativas).
- **Ao descobrir um erro/gotcha:** registre em LEARNINGS.md (sintoma → causa → correção).
- **Segredos NUNCA entram nesta memória** — só nomes/IDs/onde estão. Segredos vivem em .env (gitignored).

## Loop de auto-ensino (aperfeiçoamento contínuo)
1. Ler memória → 2. Executar o próximo passo → 3. Validar (teste/prova) →
4. Registrar checkpoint + learnings → 5. Atualizar STATE/ROADMAP → repetir.
Se algo falhar: registrar em LEARNINGS, propor correção, re-tentar — sem perder o histórico.

## Regras de ouro (herdadas da spec Sexta-feira)
- Capacidade perigosa (gasto, escrita em prod, ação irreversível) começa
  desligada / dry-run / atrás de confirmação humana.
- CALLIMA = produto comercial (WhatsApp vendas). Sexta-feira **observa**, não
  personifica nem dispara. Toolsets nunca se cruzam.
- Não inventar API/flag: consultar doc oficial antes de codar.
