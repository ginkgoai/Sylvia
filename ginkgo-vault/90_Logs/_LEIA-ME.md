# 90_Logs

Registro **append-only** das decisões e ações da Sexta-feira (observabilidade).

Formato sugerido por entrada (1 arquivo por dia: `AAAA-MM-DD.md`):

```
## HH:MM — <ação>
- gatilho: <pedido do usuário / evento>
- decisão: <o que a Sexta-feira decidiu>
- ferramenta: <skill / fluxo n8n / script>
- payload: <resumo>
- resultado: <ok / erro / aguardando aprovação>
```

Nunca editar entradas antigas — só acrescentar.
