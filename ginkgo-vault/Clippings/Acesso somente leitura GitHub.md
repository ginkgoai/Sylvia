---
title: "Acesso somente leitura GitHub"
source: "https://chatgpt.com/c/6a6e7915-daa8-83e9-9cc0-c714da16e2ae"
author:
published:
created: 2026-08-02
description: "ChatGPT conversation with 9 messages"
tags:
  - "clippings"
---
**Você disse**

como eu dou acesso administrativo apenas para vizualização e leitura de repositórios privados e publics sem poder alterar nada

---

**Você disse**

---

**Você disse**

---

**Você disse**

---

Perfeito. Então **não precisa transferir nada**.

Com os repositórios já dentro da `GinkgoAI-Systems` e:

```
Base permissions: Read
```

faça apenas:

1. Abra **GinkgoAI-Systems → People**.
2. Clique em **Invite member**.
3. Digite o usuário ou e-mail GitHub da pessoa.
4. Selecione:
```
Organization role: Member
```
5. Envie o convite.

Quando ela aceitar, terá automaticamente:

- leitura dos repositórios privados;
- acesso aos repositórios públicos;
- permissão para visualizar e clonar código;
- acesso a commits, branches e pull requests;
- sem poder executar `push`, merge, editar arquivos ou alterar configurações.

Depois confira em:

```
Organization → People → nome do usuário
```

O papel deve aparecer como:

```
Member
```

Também verifique em **Teams** e nos acessos individuais dos repositórios se não existe alguma permissão superior como:

```
Write
Maintain
Admin
```

Com `Member + Base permissions: Read`, está configurado exatamente como acesso global somente leitura.

---

**Você disse**

não estao, quero transferir eles

---

Correto — a captura confirma **0 repositórios** na organização. Minha leitura anterior estava errada.

## Melhor caminho: transferir vários de uma vez

Na sua conta pessoal `ginkgoai`:

1. Clique na foto de perfil, no canto superior direito.
2. Abra **Settings**.
3. Na lateral, vá em **Access → Organizations**.
4. Procure **Move to an organization**.
5. Clique em **Move work to an organization**.
6. Escolha a organização existente:
```
GinkgoAI-Systems
```
7. Selecione os repositórios e projetos que deseja mover.
8. Confirme em **Move to an organization**.

O GitHub oferece esse fluxo justamente para mover repositórios e projetos de uma conta pessoal para uma organização existente. [^1]

## Alternativa: transferir repositório por repositório

Abra cada repositório pessoal:

```
Repository
→ Settings
→ General
→ role até Danger Zone
→ Transfer
```

Na janela de transferência:

```
New owner: GinkgoAI-Systems
Repository name: mantenha o nome atual
```

Digite o nome exato do repositório para confirmar e clique em:

```
I understand, transfer this repository
```

Você precisa ter acesso administrativo ao repositório e permissão para criar repositórios na organização de destino — como `Owner` da `GinkgoAI-Systems`, você atende esse requisito. Não pode existir na organização outro repositório com o mesmo nome. [^2]

## O que será preservado

A transferência normalmente mantém:

- código e histórico de commits;
- branches e tags;
- issues e pull requests;
- releases;
- wiki;
- estrelas e watchers;
- webhooks;
- secrets;
- deploy keys.

Os links antigos do repositório passam a redirecionar para a nova localização. Mesmo assim, é recomendável atualizar o endereço remoto nos projetos locais. [^2]

Depois de transferir cada projeto, execute na pasta local correspondente:

```bash
git remote set-url origin https://github.com/GinkgoAI-Systems/NOME-DO-REPOSITORIO.git
```

Confirme com:

```bash
git remote -v
```

## Verificação crítica depois da transferência

A transferência preserva colaboradores existentes. Portanto, ela **não garante automaticamente que todos ficarão somente como leitura**. [^2]

Depois de mover os repositórios:

```
Repositório
→ Settings
→ Collaborators and teams
```

Revise e remova qualquer permissão explícita:

```
Write
Maintain
Admin
```

O colaborador deve aparecer somente como:

```
Read
```

ou com acesso herdado da organização:

```
Member
Base permission: Read
```

Comece pelo fluxo **Settings → Organizations → Move work to an organization**, porque você possui vários repositórios. É a esteira industrial; o método pela `Danger Zone` é o transporte peça por peça.

---

**Você disse**

---

Agora está no ponto certo.

Clique em:

```
Move work to an organization
```

Na próxima tela:

1. Escolha **Existing organization**.
2. Selecione:
```
GinkgoAI-Systems
```
3. Marque os repositórios pessoais que deseja transferir.
4. Marque também os GitHub Projects, caso existam.
5. Revise o destino de cada item.
6. Clique em **Move to an organization**.
7. Ao finalizar, clique em **Go to your organization**. Esse processo transfere os itens selecionados sem converter nem apagar sua conta pessoal. [^3]

Depois da transferência, os repositórios aparecerão como:

```
github.com/GinkgoAI-Systems/NOME-DO-REPOSITORIO
```

A organização passará a aplicar suas configurações padrão aos repositórios transferidos. Portanto, como você já definiu:

```
Base permissions: Read
```

os membros receberão leitura por padrão, salvo quando houver alguma permissão individual ou de equipe mais alta. [^4]

### Depois de concluir

Abra cada repositório em:

```
Repository
→ Settings
→ Collaborators and teams
```

Remova acessos explícitos `Write`, `Maintain` ou `Admin` que não deveriam continuar. Colaboradores existentes normalmente são preservados durante a transferência. [^4]

Também atualize o remoto nos projetos clonados localmente:

```bash
git remote set-url origin https://github.com/GinkgoAI-Systems/NOME-DO-REPOSITORIO.git
git remote -v
```

Os endereços antigos costumam redirecionar, mas o próprio GitHub recomenda atualizar os remotos locais. [^4]

[^1]: [docs.github.com](https://docs.github.com/en/account-and-profile/how-tos/account-management/moving-your-work-to-an-organization)

[^2]: [docs.github.com](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)

[^3]: [docs.github.com](https://docs.github.com/en/enterprise-cloud%40latest/account-and-profile/how-tos/account-management/moving-your-work-to-an-organization)

[^4]: [docs.github.com](https://docs.github.com/en/enterprise-cloud%40latest/repositories/creating-and-managing-repositories/transferring-a-repository)