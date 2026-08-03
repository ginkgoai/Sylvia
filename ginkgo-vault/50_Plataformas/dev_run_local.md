# Rodar o tronco LEAF local (dev) — receita + armadilhas

> Como subir api + web + worker na máquina (fora do Docker), e os gotchas que custaram tempo. honest-data.

## Subir o stack (host, dev)
- **API** (`:3333`) e **Web** (`:3000`): `tsx watch src/index.ts` — precisam do env no shell. O Code sobe com o env carregado.
- **Worker** (processa a Task do Brann/cognição → OpenRouter): **precisa do `.env` carregado**. Os scripts `pnpm dev` são `tsx watch` puros (NÃO carregam `.env`). Subir assim (detached, sobrevive a quedas):
  ```
  node --env-file=C:\dev\ginkgo-tree\.env --import tsx C:\dev\ginkgo-tree\apps\worker\src\index.ts
  ```
  Boot saudável = `[worker] listening on queue "ginkgo-tasks"` + `[worker] seeded N skills`.

## Armadilha 1 — Prisma + Windows + Docker = `localhost` quebra
- Sintoma: worker dá **"Can't reach database server at localhost:5433"** mesmo com a porta reachable; a API conecta.
- Causa: o engine Rust do Prisma resolve `localhost` como **IPv6 (`::1`)** e o forward IPv6 do Docker Desktop reseta (ECONNRESET).
- **Fix:** no `.env`, `DATABASE_URL` usa **`127.0.0.1`** (não `localhost`). (Editado em 2026-06-27 — só o host, senha intacta.) ioredis (Redis) lida com `localhost` ok; só o Prisma precisa de IPv4.

## Armadilha 2 — workers zumbis
- Subir worker várias vezes deixa processos velhos vivos (com env/`.env` antigo) poluindo o log.
- Matar TODOS antes de subir um novo: processos `node` cujo CommandLine tem `--env-file` (é só o worker; api/web não usam).
  ```powershell
  Get-CimInstance Win32_Process -Filter "name='node.exe'" | ? { $_.CommandLine -like '*--env-file*' } | % { Stop-Process -Id $_.ProcessId -Force }
  ```

## Caveats
- O worker assim roda **sem auto-restart** (não é `tsx watch`). Se cair, subir de novo. Pra demo, ok.
- Mapeamentos host: Postgres `ginkgo-postgres` 5432→**5433** · Redis `ginkgo-redis` 6379→**6380** (com senha).

_Mantido pela Sexta-feira._
