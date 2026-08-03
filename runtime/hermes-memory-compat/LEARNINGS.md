# LEARNINGS — erros/gotchas + correções (não repetir)

Formato: SINTOMA → CAUSA → CORREÇÃO.

1. **Hermes instalado "some" do terminal do usuário** → o instalador rodado pela
   automação (Desktop Commander, filho do app Claude empacotado) virtualizou
   %LOCALAPPDATA%/PATH no sandbox do app → **reinstalar pelo PowerShell REAL do
   usuário**. A config do Hermes deve ser feita pelo terminal do fundador, não pela automação.

2. **Claude (provider Anthropic) HTTP 400 "credit balance too low" / "extra usage"**
   → assinatura Claude Max NÃO cobre apps de terceiros de graça (mudança abr/2026);
   API key sk-ant precisa de crédito pré-pago. → modo grátis usa **Nous Portal**
   (`*:free`), trocar p/ Claude quando houver billing.

3. **AnythingLLM RAG: HTTP 500 "No OpenAI API key was set"** → a fiação do RAG
   está OK (auth/slugs certos); falta configurar o **motor do AnythingLLM**:
   Embedding=Native (grátis) + LLM=Generic OpenAI apontando p/ Nous
   (`https://inference-api.nousresearch.com/v1`, key `sk-nous-...`, modelo `:free`).

4. **n8n MCP não conecta como conector do Claude** → tela exige https+OAuth e
   rejeita `http://localhost` + Bearer. → dirigir via host shell (n8n_mcp.py, JSON-RPC).

5. **CALLIMA `$('Dados')` quebrado** → o nó se chama **`Dados1`**. Sempre `$('Dados1')`.

6. **Saída do AI Agent** vem em **`output`**, não `text`/`message`; e o agente não
   fornece instance/remoteJid → o CODE1 deve ler `output` e puxar
   INSTANCIA/NUMERO_LEAD do `Dados1`.

7. **Nós Evolution sobrescrevem `$json`** → no sub-fluxo de entrega, referencie o
   bloco via `$('Itera1').item.json.*`, nunca `$json`.

8. **Console Windows cp1252 quebra print de JSON com emoji/acentos** → no Python,
   `sys.stdout.reconfigure(encoding='utf-8')` no início.

9. **Loop Over Items (splitInBatches v3)**: saída 0 = "done", saída 1 = "loop".
   Processamento sai da "loop".

10. **Buffer Redis da Callima tem race condition** → sem guard "sou a última msg",
    rajada gera N respostas. Guard recomendado: SET `{lead}_last`=message_id antes do
    wait; depois do wait, IF message_id==_last → segue; senão noOp. (Exige teste runtime.)

11. **Postgres Chat Memory sem sessionKey** → mistura conversas. Setar
    `sessionKey = {{$('Dados1').item.json.NUMERO_LEAD}}`.

12. **update_workflow**: NÃO usar removeNode+addNode no mesmo nó (desconecta sub-nós
    ai_tool/memory/model). Usar updateNodeParameters / setNodeParameter / setNodeCredential.

13. **Modelos `:free` são fracos em tool-calling** → a fiação das integrações valida
    por teste standalone; a qualidade de "o agente decidir chamar a tool" fecha no Claude.

14. **Sessão do Cowork reinicia direto** (MCPs reconectam, "Continue...") → por isso
    esta memória existe. Sempre persistir estado antes de depender da janela.
