---
title: "Anil-matcha/awesome-claude-fable-5: Curated Claude Fable 5 use cases, tutorials, integrations, demos, and benchmark evidence with source links. Access Claude Fable 5 exclusively via MuAPI."
source: "https://github.com/Anil-matcha/awesome-claude-fable-5#case-29-hermes-agent-integration-setup-by-ibuzovskyi"
author:
published:
created: 2026-06-14
description: "Curated Claude Fable 5 use cases, tutorials, integrations, demos, and benchmark evidence with source links. Access Claude Fable 5 exclusively via MuAPI. - Anil-matcha/awesome-claude-fable-5"
tags:
  - "clippings"
---
---

## 🔌 Platform, API, and Tool Integration### Case 29: [Hermes Agent Integration Setup](https://x.com/IBuzovskyi/status/2064427654942740608) (by [@IBuzovskyi](https://x.com/IBuzovskyi))**Configure Hermes to use `anthropic/claude-fable-5` for complex `/goal` runs and cached long-horizon tasks.**

HERMES AGENT NOW RUNS ON CLAUDE FABLE 5, Anthropic's first public Mythos-class model.

Released June 9. Built for the kind of work Hermes does best: long-horizon autonomous tasks.

Add it to any profile through Nous Portal, OpenRouter, or the native Anthropic API:

hermes model

Pick provider, then:

/model anthropic/claude-fable-5

Why Fable 5 fits Hermes specifically:

→ Built for days-long tasks. The longer the task, the bigger its lead. Hermes `/goal` runs that span hours benefit most.

→ Self-corrects in a loop. Anthropic's own guidance is: design a goal or rubric, let it self-correct, step back. This is exactly how Hermes `/goal` works.

→ Strong on memory across sessions. On Continual Learning Bench it completed the full loop: fail → investigate → verify → distill → consult. Hermes memory system feeds this directly.

→ 80.3% on SWE-Bench Pro. Best coding model available. Point your code-reviewer profile at it.

Pricing through the API:

- $10/million input
- $50/million output
- 90% discount with prompt caching. Hermes attaches 1-hour cache breakpoints automatically.

One note: cybersecurity, biology, and chemistry queries fall back to Opus 4.8. This fires in under 5% of sessions. Keep it in mind for security-focused profiles.

Best setup: Fable 5 for complex `/goal`s, cheaper models for routine cron jobs.

Type: Tutorial | Date: 2026-06-09

---

### Case 30: [Capabilities, Pricing, and Subscription Notes](https://x.com/btibor91/status/2064441061079134598) (by [@btibor91](https://x.com/btibor91))**Use this case to understand when Fable 5 is available, what it costs, and which guarded domains may fall back to another model.**

Anthropic released Claude Fable 5 and Claude Mythos 5, two versions of their most capable model yet.

Fable 5 is for general use.

Mythos 5 is for a small set of trusted partners.

The only real difference is which safeguards are in place.

- Claude Fable 5's capabilities exceed those of any model Anthropic has ever made generally available.
- It is state-of-the-art on nearly all tested benchmarks.
- The longer and more complex the task, the larger its lead.
- On requests related to cybersecurity, biology and chemistry, or distillation, Fable 5's response is handled by Claude Opus 4.8 instead.
- Distillation means attempts to extract Claude's capabilities to train competing models.
- You are informed when this happens, and it triggers in less than 5% of sessions on average.
- Claude Mythos 5 is the same underlying model as Fable 5 with the safeguards lifted in some areas.
- Mythos 5 was deployed first to Project Glasswing cyberdefenders in collaboration with the US government.
- Anthropic says Mythos 5 has the strongest cybersecurity capabilities of any model in the world.
- The system card reveals a separate safeguard that limits Claude's effectiveness on frontier LLM development requests.
- Those requests include pretraining pipelines, distributed training infrastructure, and ML accelerator design.
- Unlike the other safeguards, this one is not visible to you and does not fall back to another model.
- It works through methods like prompt modification, steering vectors, or parameter-efficient fine-tuning.
- Both models are offered at $10 per million input tokens and $50 per million output tokens.
- That is less than half the price of Claude Mythos Preview.
- Fable 5 is included at no extra cost on Pro, Max, Team, and seat-based Enterprise plans from launch through June 22.
- On June 23, it is removed from those plans and using it requires usage credits.
- The included window may be extended if capacity allows.
- The goal is to restore Fable 5 as a standard part of subscription plans as quickly as possible.

Type: Tutorial | Date: 2026-06-09

---

### Case 31: [Launch, Access, Pricing, and Safety Summary](https://x.com/ctgptlb/status/2064410460963934479) (by [@ctgptlb](https://x.com/ctgptlb))**Use this launch summary to choose access route, API model name, context window, caching strategy, and subscription timing.**

A summary of what you should know about Claude Fable 5, the Mythos-class model that is finally generally available.

Anthropic announced Claude Fable 5, the first generally available Mythos-class model positioned above Opus and the first member of the Claude 5 family.

Access:

- API model name: `claude-fable-5`
- Available through Claude API, AWS, Google Cloud, and Microsoft Foundry
- Claude Code supports a 1M-token context window on Pro, Max, Team, and Enterprise

Benchmark notes:

- SWE-bench Pro: 80.3%