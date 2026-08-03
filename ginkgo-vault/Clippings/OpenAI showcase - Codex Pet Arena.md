---
title: "OpenAI showcase - Codex Pet Arena"
source: "https://developers.openai.com/showcase/codex-pet-arena"
author:
published:
created: 2026-07-18
description: "Built with Codex + ImageGen + hatch-pet by Gabriel Chua"
tags:
  - "clippings"
---
## Codex Pet Arena

Author: Gabriel Chua

A fast, colorful platform arena where animated pets collect tokens, grow, and bonk their rivals.

[Try it live](https://codex-pet-arena-20260709.openai.chatgpt.site/)

![Codex Pet Arena app screenshot](https://developers.openai.com/showcase/codex-pet-arena.webp)

Description

Codex Pet Arena is a single-player browser game built by Gabriel Chua with Codex, ImageGen, and the hatch-pet skill. Players choose an animated pet, race CPU rivals for glowing Codex tokens across a wide side-scrolling arena, grow as their score rises, and battle through rotating city maps with moving platforms, hazards, power-ups, and a low-gravity Moon.

## Build notes

### Initial prompt

```
Build a playful single-player browser game called “Codex Pet Arena.” The player chooses one of eight original animated pets and competes against CPU-controlled pets in a large side-scrolling platform arena.

The main goal is to collect glowing Codex tokens placed across platforms, moving routes, hidden corners, and risky high places. Each token increases the pet’s score and gradually makes it bigger. Pets can bump or stomp one another, causing some tokens to spill out for anyone to collect. The biggest, highest-scoring pet should feel powerful and lead the leaderboard.

Start with a fun core: responsive movement and jumping, a scrolling arena, simple platforms, collectible tokens, and CPU pets that can move around and compete for them. Then add growth up to 3×, attacks, occasional power-ups, changing maps, and satisfying effects.

Use ImageGen and the hatch-pet skill to create eight original pets with distinct personalities and a small set of consistent animations.

Make the arena wide enough to explore in both directions. Add moving platforms, spring pads, shortcuts, hazards, and rewarding token routes. Change the map and rearrange the platforms every 30 seconds. Give different maps their own playful effects, including a Moon map with low gravity.

Keep the interface simple and let the game fill the screen. Add upbeat music, fun sound effects, particles, screen shake, and other small touches that make collecting tokens and hitting rivals feel satisfying.

Make it colorful, fast, slightly chaotic, and easy to understand within a few seconds. Focus on creating something genuinely fun and playable rather than reproducing every possible feature.
```

### Iterations

1. Prototyped the core loop with placeholder shapes, one map, player movement, jumping, camera scrolling, platforms, and collectible Codex tokens, then tuned movement and collecting until they felt good.
2. Added CPU rivals that find nearby tokens, move between reachable platforms, and occasionally chase or avoid the player.
3. Added growth and combat so tokens increase score and size, pets can stomp and knock back rivals, and defeated pets spill tokens for others to steal.
4. Replaced the placeholders with eight original animated pets created with ImageGen and the hatch-pet skill once the mechanics were stable.
5. Expanded the arena with a wider world, an improved camera, natural platform arrangements, moving platforms, spring pads, shortcuts, and risky routes.
6. Introduced rotating maps that rearrange platforms every 30 seconds and add gameplay twists such as low gravity or faster movement.
7. Layered in arcade effects with power-ups, a super ability, combos, token storms, particles, music, sound effects, and screen shake.
8. Polished the interface and CPU decisions, tested keyboard and touch controls plus performance across map rotations, and published the playable version.
9. Final step
	Completed keyboard, touch, and multi-map performance testing, then published the polished single-player arena with animated pets, rotating maps, growth, combat, and arcade effects.