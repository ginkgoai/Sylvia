# Identidade visual dos agentes — Brann & Callima (canônico)

> 2026-07-02. Direção de arte definida pelo fundador (refs em `./refs/`). **Isto substitui o rascunho SVG anterior (era slop).** Não redesenhar do zero — estas refs são a fonte da verdade; o avatar é **imagem** (asset), não SVG gerado.

## BRANN — o copiloto da plataforma (identidade fixa da marca)
Base: um **corvo preto** roliço e carismático — calmo, sábio, misterioso-mas-amigável (não mascote-palhaço).
Assinaturas (o que torna Brann *Brann*):
1. **Chapéu cônico de palha** (kasa/sugegasa), quase preto, textura de trama sutil + marcas de costura "✕". Viajante, operador quieto.
2. **Olho = anel de neon ciano** (círculo luminoso vazado) — a marca de **presença/atenção**. É o ícone: lê a 16px como um anel que brilha.
3. **Berloques pendurados na aba** do chapéu: uma **gema ciano**, um **anel**, e uma **engrenagem violeta**. → A engrenagem é doutrina: **Brann carrega a "engrenagem" (a Callima-engine)** literalmente na silhueta.
Variantes fornecidas (é um pequeno **sistema**, não uma imagem só):
- **Neon holográfico** (fundo líquido iridescente azul/roxo/magenta, glow alto) → herói / marketing.
- **Render 3D limpo** sobre creme → **avatar no app / plataforma**.
- **Traço mínimo (ink, mono)** → sticker, estados de loading, favicon.
- **Ilustração ink com berloques + um gatinho preto** na aba → easter-egg / momento lúdico.
Vibe: mystical-tech, curioso, acolhedor. Expressividade nível Duolingo, alma própria.

## CALLIMA — a secretária do cliente (avatar default do agente)
Base: **silhueta elegante sem rosto** (busto), com **cabelo/ombros/gola traçados por luz** — azul elétrico + dourado quente correndo pelos fios e pela clavícula.
- **Sem rosto de propósito:** universal + personalizável (o cliente projeta a marca dele) **e** honest-data na identidade — ela é **interface/vaso**, não uma "pessoa" fabricada.
- **6 opções nativas unissex** (`callima_fem_01..03`, `callima_masc_01..03`) — todas sem rosto / feitas de luz → **gênero-neutro por construção**. É um **pacote**, não um rótulo: o cliente escolhe qualquer uma independente do gênero dele. Estilo idêntico (silhueta + luz azul/dourada) mantém coesão visual.
Vibe: elegante, premium, luminosa, discreta, confiável. "Presença humana feita de luz."

## Amarração com a doutrina (por que essa arte é certa)
- Engrenagem do Brann = **"Callima como engrenagem"** visível.
- Anel ciano = sinal honesto de que o sistema está **atento** (não finge).
- Callima sem rosto = **interface, não pessoa falsa** → honest-data no nível da identidade.

## Como isso vira produto (feature de avatar por-tenant — corrige a nota anterior)
- **Brann** = identidade **fixa** da plataforma (não é per-tenant).
- **Avatar do agente do cliente = ASSET DE IMAGEM** (`AgentProfile.avatarAssetId`, blob/objeto), **não SVG gerado**:
  - **Built-ins** que já entregamos: Callima (fem/masc), corvo, silhueta-luz, monograma.
  - **Importar o próprio** (upload do cliente) — "essa imagem do personagem ou uma importada pelo usuário".
- Onde: picker no dashboard + o Brann configura por conversa ("usa a Callima feminina" / "sobe esse PNG").
- **Lapidação pós-core** (junto da fatia de design), agora **com arte real** — não é mais um rascunho.

## Assets — salvos e mapeados em `./refs/` ✓
**Brann (4):** `brann_render.png` (avatar app · fundo creme) · `brann_neon.png` (herói · holográfico) · `brann_ink.jpg` (mínimo · sticker/estado) · `brann_ink_gato.jpg` (easter-egg · com o gatinho).
**Callima (6 unissex):** `callima_fem_01..03.jpg` · `callima_masc_01..03.jpg` — silhuetas de luz, gênero-neutro.
`_dup_brann_neon.png` = duplicata (pode apagar). Na fatia do picker o Fable move/otimiza p/ `apps/web/public/avatars/` e liga no `avatarAssetId`.

---
## Assets canônicos dos mascotes (rev. 2026-07-06 — geração Lovart)
- **Heroes transparentes (USAR ESTES):** `refs/transparent/{brann,callima,nyra,alfred}_hero_transp.png` — recortados do branco, fundo transparente, bordas limpas. São os avatares oficiais (hero, cards, chips flutuantes).
- **Assinatura da família:** anel-ciano em cada um (Alfred=olho, Brann=olho, **Callima = figura de LUZ com o anel como cabeça**, Nyra=olho). Paleta: Alfred azul · Brann preto+ciano · Callima ciano-luz · Nyra violeta. Colar com nome.
- **Arquivado:** `*_pokemon_icon.png` (Pokébola = IP Nintendo) → `_alpha_beta/icones_pokemon_IP/`. Os `*Minimalista*` (line-art fininho) seguem em `refs/`, mas são fracos p/ chip — preferir os heroes ou os badges circulares do `Ícone Alternativo`.
- **Fonte p/ chips redondos:** `Brann - Ícone Alternativo Corvo.png` e `Nyra - Ícone Alternativo Raposa Kitsune.png` trazem folhas de badges circulares (recortar quando precisar de ícone pequeno).
- Originais Lovart (fundo branco) ficam em `refs/` com nomes "— Mascote / Ícone …".
