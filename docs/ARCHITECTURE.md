# Sylvia — Arquitetura Visual

> Arquitetura atual da Sylvia v2.1. Fonte normativa: `SYLVIA.md`. Este documento substitui o diagrama histórico da antiga Sexta-feira como mapa operacional principal.

## 1. Mapa do sistema

```mermaid
flowchart TB
    F[Fundador]

    subgraph COG[Cognição e coordenação]
        OC[OpenClaw\nCérebro e runtime principal]
        CTX[Composição de contexto]
        HB[Heartbeat e rotinas]
        POL[Autonomia e políticas]
    end

    subgraph MEM[Memória institucional]
        CON[SYLVIA.md\nConstituição]
        BRAIN[ginkgo-vault/00_Cerebro\nMemória canônica]
        INBOX[ginkgo-vault/00_Inbox\nClippings brutos]
        BIZ[empresas/ + operacao/\nContexto de negócio]
    end

    subgraph GOV[Execution Fabric]
        AOS[Agent OS\nPolicy, risco, orçamento e aprovação]
        AUD[Auditoria e evidência]
    end

    subgraph EXEC[Executores]
        H[Hermes\nExecution runtime]
        N8N[n8n\nAutomações determinísticas]
        CODE[Coding Fabric\nOpenCode / Codex / Claude Code]
        MCP[MCPs e APIs]
    end

    subgraph DATA[Infra operacional]
        PG[(Postgres)]
        RD[(Redis)]
        GH[GitHub\nFonte de verdade da engenharia]
    end

    F --> OC
    OC --> CTX
    CTX --> CON
    CTX --> BRAIN
    CTX --> BIZ
    INBOX -->|triagem| BRAIN
    HB --> OC
    POL --> AOS
    OC --> AOS
    AOS --> H
    AOS --> N8N
    AOS --> CODE
    H --> MCP
    N8N --> PG
    N8N --> RD
    CODE --> GH
    H --> AUD
    N8N --> AUD
    CODE --> AUD
    AUD --> BRAIN
    AOS -->|gate quando necessário| F
```

## 2. Fluxo de uma ação com efeito colateral

```mermaid
sequenceDiagram
    participant F as Fundador
    participant S as Sylvia / OpenClaw
    participant A as Agent OS
    participant E as Executor
    participant X as Sistema externo
    participant M as Memória/Auditoria

    F->>S: objetivo ou instrução
    S->>S: compõe contexto e intenção
    S->>A: missão + risco + orçamento + escopo
    A->>A: classifica política e permissões
    alt ação exige aprovação
        A-->>F: intenção + impacto + pedido de aprovação
        F-->>A: aprova ou rejeita
    end
    A->>E: execução governada
    E->>X: ação autorizada
    X-->>E: resultado/evidência
    E-->>A: status + evidência
    A->>M: trilha auditável
    A-->>S: resultado validado
    S-->>F: síntese e próxima decisão
```

## 3. Memória e verdade

```mermaid
flowchart LR
    RAW[Material bruto] --> IN[ginkgo-vault/00_Inbox]
    IN --> TRI[Triagem de clippings]
    TRI -->|comprovado / relatado / hipótese| CAN[ginkgo-vault/00_Cerebro]
    CAN --> CP[CHECKPOINT / HANDOFF / CONTEXT_LOG]
    CAN --> DEC[Decisões e Insights]
    CAN --> BOOT[Boot da Sylvia]
    BOOT --> ACT[Decisão / coordenação]
    ACT --> LOG[Registro do que foi feito e por quê]
    LOG --> CAN

    EXT[Dados vivos de sistemas] --> VERIFY[Verificação na fonte real]
    VERIFY --> ACT
```

Regra: conversa não registrada não é memória institucional; estado de sistema vivo não deve ser inferido da memória.

## 4. Coding Fabric

```mermaid
flowchart TD
    NEED[Necessidade de engenharia] --> PLAN[Sylvia define escopo e acceptance criteria]
    PLAN --> AOS[Agent OS classifica risco]
    AOS --> WORKER{Selecionar executor}
    WORKER --> OC[OpenCode\npreferencial para tarefa delimitada]
    WORKER --> CX[Codex\nfallback / revisão]
    WORKER --> CC[Claude Code\nfallback / revisão premium]
    OC --> BR[Branch / worktree / sandbox]
    CX --> BR
    CC --> BR
    BR --> TEST[Quality gates]
    TEST --> REVIEW[Revisão]
    REVIEW --> PR[Pull Request]
    PR --> MERGE{Aprovação de merge}
    MERGE -->|aprovado| MAIN[main]
    MAIN --> DEPLOY{Gate separado de deploy}
    DEPLOY --> PROD[Produção]
```

Invariantes: nenhum coding worker recebe segredos; `main` não é alvo direto por padrão; merge e deploy são decisões separadas; `SUCCESS` exige quality gates aplicáveis.

## 5. Fronteiras do ecossistema

```mermaid
flowchart LR
    S[Sylvia\nCEO cognitiva da holding]
    G[Ginkgo AI Systems]
    SC[Scale Group]
    P[Operação pessoal/patrimonial autorizada]

    S --> G
    S --> SC
    S --> P

    G --> TREE[Tree / Laplace]
    G --> LEAF[Leaf]
    G --> CONNECT[Connect]
    G --> WORK[Workforce]
    G --> PYRE[Pyre]
    G --> WAVE[Wave]
    G --> AEGIS[Aegis]
    G --> LEXRA[Lexra]
    G --> COM[Commerce OS]
    G --> LAB[AI Stack]

    S -. não personifica .-> CALLIMA[Callima\nAgente comercial de cliente]
```

Sylvia governa a holding e prepara execução; não é um produto, não atende clientes e não compartilha identidade com Callima.

## 6. Responsabilidades por camada

| Camada | Responsabilidade |
|---|---|
| OpenClaw | intenção, contexto, heartbeat, coordenação e comunicação |
| Agent OS | política, risco, orçamento, permissões, aprovação e auditoria |
| Hermes | terminal, browser, skills, jobs, MCPs/APIs e delegação executiva |
| n8n | processos repetíveis, integrações estáveis, retries e workflows aprovados |
| Coding Fabric | implementação/revisão de engenharia com workers substituíveis |
| GitHub | fonte de verdade técnica e fluxo branch/PR |
| ginkgo-vault | memória institucional e biblioteca documental, sem segredos/PII |

## 7. Histórico

A arquitetura v1 da antiga **Sexta-feira** usava Hermes como núcleo. Ela foi sucedida pela Sylvia v2.x: OpenClaw tornou-se cérebro/runtime principal e Hermes passou a executor governado. Para decisões atuais, prevalecem `SYLVIA.md`, `cognicao/AUTONOMIA.md` e `docs/feature_sylvia_execution_fabric.md`.
