---
title: "Hermes Agent – A PM's Field Guide and how to set up | Hermes Agent Certification"
source: "https://marily.substack.com/p/hermes-agent-a-pms-field-guide-and"
author:
  - "[[Marily Nika]]"
published: 2026-06-07
created: 2026-06-27
description: "In February 2026, a small research lab called Nous Research shipped an open-source project built on a primary premise: what if your AI got smarter the longer you used it?"
tags:
  - "clippings"
---
![](https://substackcdn.com/image/fetch/$s_!GsXe!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F336c0fed-df39-4897-990d-f931511ec2c8_1792x1294.png)

In February 2026, a small research lab called Nous Research shipped an open-source project built on a primary premise: what if your AI got smarter the longer you used it? What if it remembered your projects, learned your preferences, wrote down its own procedures, and ran errands for you while you slept?

Four months later, Hermes Agent has crossed 175,000 GitHub stars and attracted nearly a thousand contributors. In May it overtook OpenClaw, the previous open-source darling, to become the most-used open-source agent on OpenRouter’s daily inference rankings, processing over 220 billion tokens in a single day. By most measures it is the fastest-growing open-source agent framework of 2026.

This is a field guide for professionals, especially product managers, who want to understand what Hermes is, how to actually use it, what it costs, where the sharp edges are, and what its design teaches us about where AI products are headed. It’s long because the topic deserves it. Skim the headers and dive where you’re curious.

## Part 1: What Hermes Actually Is

The easiest way to understand Hermes is by what it refuses to be. It’s not a coding copilot living inside your IDE, and it’s not a chat window you visit. It’s a persistent process that runs continuously on a machine you control: your laptop, a $5/month cloud server, or serverless infrastructure that hibernates when idle.

Once it’s running, three things separate it from everything else you’ve used.

**It lives where you already are.** Hermes connects to more than twenty messaging platforms from a single gateway, including Telegram, Slack, Discord, WhatsApp, Signal, email, SMS, and Microsoft Teams. You don’t open an app to use it. You text it. Start a conversation from Slack at your desk, continue from Telegram on the train, and it’s the same session, same context, same agent.

**It remembers.** Hermes keeps a curated, persistent memory of who you are, what you’re working on, and what it has learned, and it can search every past conversation it has ever had with you. More on the mechanics below, because they’re clever.

**It improves itself.** When Hermes completes a complex multi-step task, it can write the procedure down as a reusable “skill,” a small instruction document it consults the next time something similar comes up. Over weeks it accumulates a private playbook tailored to your work. Nous calls this the learning loop, and it’s the project’s core differentiator.

It’s also model-agnostic. Hermes is the harness, not the brain. You plug in Claude, GPT, Gemini, DeepSeek, Kimi, or any of 300+ models, and switch between them with one command. No lock-in, which is itself a product stance.

---

![](https://substackcdn.com/image/fetch/$s_!yG7x!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75c40300-bd46-4761-9f34-f1180c8ac6ed_3016x1326.png)

## The hands-on Claude Code & Hermes Agent certification for professionals

Master Claude Code & Hermes Agent hands-on, then learn to evaluate agentic systems like a pro. Go from simply using AI to building full-stack applications & deploying autonomous agents.

3 learnable skills: directing Claude Code like an eng team, operating a Hermes Agent that runs 24/7 on your own infrastructure & gets smarter every week, & evaluating agentic systems so you can prove they work instead of hoping they do.

3 weeks. Your machine. Your real work. By the end, you have running agents.

**✨ Week 1 — Hands-on Claude Code:** Specs, plans, subagents, skills, MCP. You’ll ship a working tool by Friday.

**✨ Week 2 — Hands-on Hermes Agent:** Deploy it on your own infra, connect it to Slack/Telegram, put it on a schedule, & customize it to your specific use cases.

**✨ Week 3 — Evals for Agentic Systems:** Define success, build eval sets, catch failure modes & ship agents you can defend in a roadmap review.

**𝙏𝙤𝙤𝙡 𝙡𝙞𝙨𝙩** **Claude Code, Hermes Agent** & practical eval tooling & patterns you can apply to any agent.

No coding experience required. If you can write a paragraph, you can drive these tools. [SIgn-up Here](https://maven.com/marily-nika/ai-agent-certification?promoCode=MAVEN100) with the discounted rate until end of June 8. Interested in this as a bundle with [Marily’s AI Product Bootcamp](https://maven.com/marily-nika/ai-pm-bootcamp?promoCode=MAVEN100) or a private training? We can send you a custom invoice, reach out to Marily at maven@aiproduct.com. FREE Lightning Lesson on Hermes [here](https://maven.com/p/22ae96/1h-the-hermes-agent-what-it-is-why-it-matters-how-tos?utm_medium=ll_share_link&utm_source=instructor).

---

### The sixty-minute setup

Here’s the honest on-ramp. You need a terminal, or as of May the new desktop app for Mac and Windows, which wraps the same agent core in a GUI. Same memory, same skills, same sessions across both surfaces.

**Step one: install.** One command on Linux, macOS, or WSL2:

curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

The installer handles Python, dependencies, everything. No sudo required.

**Step two: connect a model.** The path of least resistance is Nous Portal, the lab’s subscription gateway:

hermes setup --portal

One OAuth login gets you 300+ models plus the bundled Tool Gateway: web search, image generation, text-to-speech, and browser automation, without signing up for Firecrawl, FAL, ElevenLabs, or any of the other five services you’d otherwise need accounts with. You can also bring your own OpenRouter or OpenAI key if you prefer.

**Step three: talk to it.**

hermes

You’re now in a full conversational CLI with file access, a terminal, and web tools. Ask it to summarize a folder of documents. Ask it what skills it has.

**Step four: give it a phone number, so to speak.** Run the gateway setup to connect Telegram or Slack. This is the moment Hermes stops being a terminal toy and becomes a personal agent, because now you can message it from anywhere, and it can message you.

**Step five: schedule something.** Hermes has a built-in cron system you configure in plain English. Tell it: “Every weekday at 8am, search for the top three stories about AI agents, summarize them with links, and send the briefing to my Telegram.” It creates the job itself. Tomorrow morning, your agent texts you first.

That’s the whole loop: install, connect, chat, deploy to messaging, automate. An hour, give or take, and most of it is waiting on OAuth screens.

## Part 2: How the Self-Improvement Loop Works

PMs should slow down for this part. Hermes’s memory architecture is a sequence of unusually disciplined product decisions, and a useful case study in designing for LLMs.

### Memory is small on purpose

Hermes’s persistent memory is two markdown files. MEMORY.md holds the agent’s own notes about your environment, your conventions, and lessons learned, capped at roughly 2,200 characters. USER.md holds its model of you, meaning preferences, communication style, pet peeves, capped at about 1,375 characters. Together that’s roughly 1,300 tokens, injected into every conversation.

Your instinct might be that this is tiny. That’s the point. Every byte of memory rides along in every prompt, costing money and diluting attention. Unbounded memory is how you get an agent that’s expensive, slow, and weirdly fixated on something you said in March. So Hermes forces a budget. When memory fills up, the agent has to consolidate, merging three stale notes into one dense one, before it can save anything new. The constraint produces curation. Scarcity is the feature.

There’s a lesson here that travels well beyond agents: when your product’s intelligence depends on context, deciding what to forget matters as much as deciding what to remember.

### The recall layer is free

Bounded memory would be crippling if it were the only memory. It isn’t. Every conversation Hermes has ever had is stored in a local SQLite database with full-text search. When the agent needs to recall that thing you discussed three weeks ago about the pricing page, it queries its own history. That’s a 20-millisecond database lookup that costs zero LLM tokens, instead of carrying everything everywhere.

So the architecture is a small, expensive, always-present working memory backed by a vast, cheap, on-demand archive. Power users can bolt on external memory providers for knowledge graphs and semantic search, but the default two-tier design covers most needs. If that division of labor sounds like how you’d design a caching layer, or how human memory works for that matter, it should.

### Skills: facts vs. procedures

Memory stores the what. Skills store the how. A skill is a markdown document with trigger conditions, a step-by-step procedure, known pitfalls, and a way to verify success. The agent loads it only when relevant. The loading itself is token-efficient through what the docs call progressive disclosure: the agent first sees a cheap index of skill names and one-line descriptions, and pulls full instructions only for the skill it needs.

Here’s where it gets interesting for users: the agent writes its own skills. Finish a gnarly multi-step task, say pulling churn data, cross-referencing support tickets, and formatting a weekly retention summary, then tell Hermes to “save what you just did as a skill called retention-report.” Next week you type /retention-report and the whole procedure runs from the playbook. Skills can even edit themselves when they hit a snag mid-run, and a recent release added an autonomous Curator that grades, consolidates, and prunes the skill library so it doesn’t rot.

One strategic detail: Hermes skills use the SKILL.md format that Anthropic published as an open specification in late 2025, a standard that Microsoft, OpenAI, Google, and dozens of other tools adopted within months. Your skills are portable files, shareable through a community hub, not assets trapped in one vendor’s silo. Nous chose interoperability over a moat, and rode a standard instead of fighting one. That’s a move worth studying.

### The compounding effect

Put it together and you get the actual product promise. Week one, Hermes is a capable but generic assistant. Week six, it knows your stack, your tone, your recurring reports, and has a dozen private skills for your specific workflows. The switching cost isn’t a contract. It’s an accumulated relationship. That’s the retention mechanic, and it’s a more honest one than a data-export fee.