# PRD Técnico do Ginkgo Workforce para Cinquenta Usuários

## Resultado

O PRD instrutivo completo foi produzido com arquitetura, requisitos, épicos, histórias técnicas, critérios de aceitação, esforço, cronograma Mermaid, custos, CI/CD, SLOs, segurança, Ginkgo Credits, migração shadow da Callima, prompts, `soul.md`, schema de `AgentPackage` e checklist de produção.

[Baixar o PRD técnico completo](sandbox:/mnt/data/PRD_Ginkgo_Workforce_MVP50.md)

## Decisão sobre o Laplace

Para o MVP, **PostgreSQL + pgvector é suficiente**. Ele preserva vetores, documentos, versões, ACLs e ledger no mesmo domínio transacional, com RLS para isolamento. Qdrant fica atrás de uma interface e entra quando busca híbrida, multivetores, milhões de chunks ou latência justificarem outro datastore. citeturn2search1turn2search4turn1search3turn1search11

## Guardrail principal

O documento define o **Laplace Evidence Kernel**: source router, answerability gate, evidence packs, claims atômicos, verificação determinística e semântica, abstention e auditoria. LangGraph fornece persistência e interrupções duráveis; Hermes permanece integralmente isolado por tenant. citeturn0search0turn0search4turn0search5

## Planejamento

A estimativa-base é de **3.460 horas**, cerca de **3.980 com contingência**, em 18–21 semanas. A infraestrutura inicial foi estimada em **US$ 300–1.200/mês**, variando principalmente com LLMs e GPU. citeturn5search5turn5search8turn5search0