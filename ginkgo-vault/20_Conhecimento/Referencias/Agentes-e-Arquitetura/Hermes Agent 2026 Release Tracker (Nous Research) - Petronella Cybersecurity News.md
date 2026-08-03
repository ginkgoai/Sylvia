---
title: "Hermes Agent 2026 Release Tracker (Nous Research) - Petronella Cybersecurity News"
source: "https://petronellatech.com/blog/hermes-agent-ai-guide-2026/"
author:
  - "[[Petronella Technology Group]]"
published: 2026-04-16
created: 2026-06-27
description: "Nous Research Hermes 2026 tracker: Hermes 4.3 training shifts, Agent v0.4-v0.10 changelog, tool-call formats, breaking changes, and GPU upgrade math."
tags:
  - "clippings"
---
If you installed Hermes Agent when it launched in early 2026 and you are wondering what has changed since, this article is for you. It is not an installation guide. The [Hermes Agent install and configuration tutorial](https://petronellatech.com/blog/hermes-agent-ai-guide/) covers that from scratch. This is a running digest of what Nous Research has shipped across the Hermes model family and the Hermes Agent project in 2026, what changed between major versions, and what teams running Hermes in production should know before upgrading.

At [Petronella Technology Group](https://petronellatech.com/ai/ai-consulting-services-raleigh-nc/), we track open-source agent frameworks as part of our AI consulting practice for clients across cybersecurity, compliance, and IT infrastructure. Hermes is one of the frameworks we recommend for on-premise deployments where data residency matters. What follows reflects our reading of public release notes, technical reports, and HuggingFace model cards as of April 2026.

## The Nous Research Model Lineage: Hermes 1 Through 4

Nous Research has been releasing Hermes fine-tunes since the early days of open-weight LLMs. The lineage matters for understanding why Hermes Agent, the agentic framework that launched in February 2026, feels different from other open-source agent projects. The models and the agent share a philosophy: reduce refusals, improve steerability, prioritize tool-use reliability.

The original Hermes 1 models were fine-tunes of Llama 1 and Llama 2, focused primarily on instruction-following and reducing the over-refusals baked into base model RLHF. They were widely adopted by the open-source community specifically because they followed complex instructions without refusing tasks that other models would block. At the time this was a meaningful gap in the ecosystem.

Hermes 2 expanded on that foundation with multiple size variants and improved function-calling support. The ChatML format, which became something of a standard in the open-weight world, was consistently used across the Hermes 2 family. Tool-calling in Hermes 2 worked, but it was still brittle compared to what GPT-4 offered at the time.

Hermes 3 arrived in August 2024, built on Meta's Llama 3.1 base models (8B, 70B, and 405B). The Hermes 3 Technical Report (arXiv 2408.11857) described the primary improvements as advanced agentic capabilities, significantly better multi-turn coherence, and more reliable structured output. The tool-calling format matured: the model learned to emit `<tool_call>` tagged JSON reliably within a single assistant turn, rather than requiring external parsing hacks. This reliability shift made Hermes 3 the first version of the model family that teams seriously considered for production agentic pipelines.

Hermes 4 is a meaningful departure from that lineage. The base model shifted away from Llama entirely. We will cover that in the next section.

## What Changed in Hermes 4: Model Architecture Shifts

Hermes 4 represents the point where Nous Research moved from fine-tuning Meta's Llama models to working with a broader set of base models. The 14B variant released in January 2025 and the 70B and 405B FP8 variants released in September 2025 established the Hermes 4 generation. A Technical Report for Hermes 4 was published (arXiv 2508.18255).

The 405B FP8 variant is worth noting because it signals ambition at the high end of open-weight scale. Running a 405B model requires either a multi-GPU cluster or cloud inference. For teams with on-premise GPU infrastructure this is relevant for planning, though most production deployments we have seen use the 70B or smaller variants for cost and latency reasons.

The post-training corpus for Hermes 4 was approximately 1M samples covering around 1.2 billion tokens, according to the Hermes 4.3 model card which compares its own expanded corpus against the Hermes 4 baseline. That gives a reference point for the scale of fine-tuning investment that went into each generation.

What Hermes 4 kept from Hermes 3: the ChatML-adjacent formatting, the tool-call JSON structure, the commitment to reduced refusal rates relative to base models. What changed: different base models opened different capability profiles, particularly at the reasoning end of the task spectrum.

## Hermes 4.3: The Decentralized Training Experiment

Hermes 4.3 is the most technically interesting release in the 2025-2026 window, and it is currently the most recent model variant available from Nous Research on HuggingFace as of April 2026. It was released August 25, 2025 and is built on ByteDance's Seed 36B base model.

The notable departure from prior Hermes releases: Hermes 4.3 was trained using Nous Research's Psyche decentralized training network rather than a traditional centralized GPU cluster. The model card explicitly calls this out as the first Hermes model trained this way. Whether decentralized training at this scale becomes a repeatable production method or remains an experiment is worth watching. The training results are competitive, which at minimum demonstrates that the approach is viable.

The post-training corpus for Hermes 4.3 expanded substantially: approximately 5 million samples covering around 60 billion tokens, compared to roughly 1.2 billion tokens for Hermes 4. That is a roughly 50x expansion in training token count for the fine-tuning stage. The intended effect was improved reasoning quality across math, code, STEM, logic, and creative writing tasks.

Two capability additions in Hermes 4.3 matter for agent use specifically:

**Hybrid reasoning mode.** The model supports explicit `<think>...</think>` segments within responses. When enabled, the model can work through multi-step reasoning before producing a final answer. For agent tasks involving planning, decomposition, or tool selection decisions, this is directly relevant. The mode is activated either via a `thinking=True` flag in supported inference servers or by including an explicit instruction in the system prompt.

**Improved schema adherence.** Hermes 4.3 was specifically trained to produce valid JSON when given a schema. For agent frameworks that depend on structured tool calls, schema adherence failures are a significant source of runtime errors. This improvement addresses one of the more common pain points that practitioners reported with Hermes 3 in complex multi-tool workflows.

Benchmark scores from the model card (on Hermes 4.3 36B Psyche): MATH-500 at 93.8%, MMLU at 87.7%, BBH at 86.4%, AIME 24 at 71.9%, GPQA Diamond at 65.5%. These are strong scores for a 36B model and outperform the larger Hermes 4 70B on several benchmarks according to the model card.

RefusalBench is worth singling out: Hermes 4.3 scored 74.6% (meaning it answered 74.6% of questions that other aligned models refuse), compared to 59.5% for Hermes 4 70B. For teams where instruction-following on sensitive business tasks is a priority and where over-refusal from base models has caused workflow problems, this is a concrete improvement.

Available quantizations: GGUF variants at 4, 5, 6, and 8-bit are available on HuggingFace under `NousResearch/Hermes-4.3-36B-GGUF`. The 36B model fits on a two-GPU RTX 4090 setup at 4-bit quantization or a single A100 80GB at higher precision. Inference is also available through the Nous Portal and Chutes.

## Hermes Agent 2026 Release Tracker (v0.4 Through v0.10)

Hermes Agent launched in February 2026 and has been releasing at a pace that most open-source projects do not sustain. Between late March and mid-April 2026 alone, the project shipped seven major versions. Here is what each version actually changed, based on the official release notes:

### v0.4.0 (March 23, 2026) -- The Platform Expansion Release

This version was primarily about breadth. The OpenAI-compatible API server (`/v1/chat/completions`) landed here, which matters for teams who want to drop Hermes Agent behind an existing OpenAI-compatible client without rebuilding integrations. Six new messaging adapters were added: Signal, DingTalk, SMS, Mattermost, Matrix, and Webhooks. MCP server management got a CLI with OAuth 2.1 PKCE flow. At-context references (`@file`, `@url`) with tab completion arrived. Over 200 bug fixes were included in a comprehensive reliability pass.

### v0.5.0 (March 28, 2026) -- The Hardening Release

The headline item for security-conscious teams: the project removed litellm as a dependency following supply chain concerns and pinned all remaining dependencies. This is exactly the kind of decision that matters for organizations with software composition analysis requirements. Hugging Face became a first-class inference provider, meaning you can run Hermes Agent against models hosted on HuggingFace Inference Endpoints without a custom provider configuration. Plugin lifecycle hooks arrived: `pre_llm_call`, `post_llm_call`, `on_session_start`, and `on_session_end`. A Nix flake for reproducible builds was added for teams using NixOS or Nix-managed environments.

### v0.6.0 (March 30, 2026) -- The Multi-Instance Release

Profiles system: you can now run multiple isolated Hermes Agent instances from a single installation, each with separate memories, skills, credentials, and configurations. This resolves a common request from teams wanting to maintain separate personas for different clients or projects on the same host. MCP server mode arrived in this version, meaning Hermes Agent can itself expose conversations via the Model Context Protocol. Official Docker container support also shipped here.

### v0.7.0 (April 3, 2026) -- The Resilience Release

Pluggable memory provider interface: the memory backend is no longer hard-coded. Third-party backends can now be registered, which opens the door to integrations with vector databases and external memory stores. Same-provider credential pools with automatic rotation address the case where you have multiple API keys for a single provider and want automatic failover when one hits rate limits. The API server gained session continuity via `X-Hermes-Session-Id` headers, meaning HTTP clients can maintain conversational context across requests.

### v0.8.0 (April 8, 2026) -- The Intelligence Release

Background task auto-notifications (`notify_on_complete`) let long-running tasks surface results without requiring the user to poll. Live model switching across all platforms via the `/model` command arrived: you can change the underlying model mid-conversation without restarting the agent. Native Google AI Studio (Gemini) provider integration was added. The agent now benchmarks its own tool-use guidance and self-optimizes the prompts it uses to call GPT and Codex-style models. 82 resolved issues and 209 merged PRs in this version.

### v0.9.0 (April 13, 2026) -- The Everywhere Release

Mobile support via Termux on Android allows native on-device execution of the agent without a server. This is primarily useful for developers who want an always-available agent on their phone, not for enterprise deployments, but it demonstrates the project's infrastructure flexibility. iMessage support via BlueBubbles, WeChat, and WeCom arrived. A local web dashboard for agent management without a terminal is now available. Fast Mode toggle (`/fast`) enables priority processing on OpenAI and Anthropic endpoints. Background process monitoring with `watch_patterns` can trigger real-time alerts when monitored processes change state. The project reached 16 supported messaging platforms in this version, up from 8 at launch.

### v0.10.0 (April 16, 2026) -- The Tool Gateway Release

The current release as of this writing. The Nous Tool Gateway arrived: Nous Portal subscribers now have access to web search, image generation, text-to-speech, and browser automation through the agent without configuring separate third-party APIs. This reduces the setup friction for teams who want capable tool use without managing individual service accounts for every capability. Over 180 commits of bug fixes were included across the agent core, gateway, CLI, and tools.

## MCP Integration: How Tool Support Evolved

The Model Context Protocol integration in Hermes Agent has matured significantly across the 2026 releases. At launch, MCP support existed as a documented feature but required manual configuration of each MCP server and had no management interface. By v0.4.0, a CLI for MCP server management shipped with OAuth 2.1 PKCE flow for authenticated MCP servers. By v0.6.0, Hermes Agent could itself act as an MCP server, exposing its conversation interface to other MCP clients.

This bidirectional MCP capability is architecturally interesting. A team running Claude as a primary reasoning layer can route specific tool calls or specialized tasks to a locally-running Hermes Agent instance via MCP, using Hermes as a specialized subagent rather than a standalone system. Petronella Technology Group has clients exploring this pattern for on-premise compliance workflows where certain data cannot leave the internal network but still needs to interact with cloud-based orchestration.

For teams integrating with Langchain, Hermes Agent's OpenAI-compatible API server (shipped in v0.4.0) makes the integration straightforward. Any Langchain chain or agent configured to use an OpenAI-compatible endpoint can be redirected to a local Hermes Agent instance by changing the base URL. No code changes beyond that are required for basic integration.

## Tool-Calling Format Changes Across Generations

This is worth mapping explicitly because the format changed between generations and mixing model versions with incompatible parsing logic is a common source of silent failures in production systems.

Hermes 2 and early Hermes 3 used ChatML format with `<tool_call>` tags containing JSON, parsed via the `<|im_start|>` / `<|im_end|>` message boundary tokens. The format was `<tool_call>{"name": "function_name", "arguments": {...}}</tool_call>`.

Hermes 3 on Llama 3.1 maintained the same `<tool_call>` tag structure but the underlying prompt format shifted to Llama-3-Chat-style role headers rather than pure ChatML. Parsers written for Hermes 2 may fail silently on Hermes 3 models if they rely on ChatML-specific token detection.

Hermes 4 and 4.3 use Llama-3-Chat format with the same `<tool_call>{...}</tool_call>` structure for the actual tool invocation. Hermes 4.3 adds reasoning mode where a `<think>...</think>` block may appear before the tool call in the assistant turn. Parsers that assume the first content in an assistant turn is either text or a tool call will need to handle the reasoning preamble.

For Hermes Agent (the framework, not the model), the agent abstracts tool-call parsing away from the end user. If you are using Hermes Agent as your orchestration layer and swapping the underlying model via the `/model` command or the `hermes model` CLI, the agent handles format differences. If you are using the raw Hermes models directly in your own stack, verify your parser handles all three format variants.

## Community Fine-Tunes and Derivative Projects

The Hermes model family has generated a consistent stream of community fine-tunes and quantizations since Hermes 2. By Hermes 3, the pattern was well established: within days of a new Hermes release, TheBloke and later bartowski would publish GGUF quantizations across multiple bit depths. Those quantizations significantly expanded adoption on consumer hardware.

For Hermes 4.3, Nous Research published official GGUF variants under their own organization on HuggingFace, reducing dependence on community quantizers for that format. This is a maturation of the release process rather than a change in direction.

Notable derivative patterns in the community: role-play fine-tunes built on the Hermes base (which inherits the steerability that Nous Research emphasizes), specialized coding fine-tunes layered on top of Hermes, and several instruct fine-tunes targeting specific domains like legal document analysis. We are not listing specific third-party fine-tune repositories because that inventory changes quickly and any specific list here would age poorly. The HuggingFace models page filtered by base model provides current listings.

One category worth flagging: several community projects use Hermes as the underlying model for OpenClaw deployments. For teams evaluating Hermes Agent vs OpenClaw for agent use, [our OpenClaw vs Hermes Agent comparison](https://petronellatech.com/blog/openclaw-vs-hermes-agent-2026/) covers that decision in depth, and the [OpenClaw guide](https://petronellatech.com/blog/openclaw-ai-agent-guide/) covers OpenClaw-specific configuration separately.

## Breaking Changes and Deprecations to Watch

Based on the v0.5.0 release notes, the removal of litellm as a dependency is the change most likely to break existing installations if you had configured custom providers through litellm's abstraction layer. If your Hermes Agent setup used litellm as an intermediary, you will need to reconfigure those providers using the native provider system. The v0.5.0 release notes describe this as a supply chain hardening decision, and the project added direct provider support for the most commonly used litellm backends simultaneously.

The Psyche decentralized variant of Hermes 4.3 (accessible via Nous Portal and Chutes) uses a slightly different model ID than the standard variant. If you are programmatically referencing model IDs in your configuration, verify you are using `NousResearch/Hermes-4.3-36B` for the standard HuggingFace version vs the Psyche endpoint identifiers for Nous Portal inference. Mixing these up produces model-not-found errors rather than capability degradation, which makes them easier to catch.

The Llama 3.1 base models that underlie Hermes 3 use a context window of 128K tokens. If you built pipelines that pass very long context to Hermes 3 and are migrating to Hermes 4.3 (Seed 36B base), verify the effective context length for your use case. The Hermes 4.3 model card does not specify an extended context window beyond the Seed 36B base, and the Seed 36B's default context configuration should be verified against your production requirements before migration.

For Hermes Agent specifically: the profiles system introduced in v0.6.0 changed how configuration files are organized on disk. Teams upgrading from earlier versions should review the v0.6.0 migration notes in the project README before upgrading, as existing single-instance configurations may need to be moved into a default profile directory.

## Upgrade Considerations for Production GPU Teams

For teams running Hermes models on local GPU infrastructure, the Hermes 4.3 36B parameter count is meaningfully different from the Hermes 3 70B that many production teams standardized on. Here is how that plays out practically:

A Hermes 3 70B at Q4\_K\_M quantization requires approximately 40GB of VRAM, which means two A100 40GB cards or a single A100 80GB. Hermes 4.3 36B at Q4\_K\_M requires roughly 21GB of VRAM, which fits on a single A100 40GB or two RTX 4090s. If your infrastructure runs RTX 4090s, the move from Hermes 3 70B to Hermes 4.3 36B may actually reduce GPU requirements while improving several benchmark metrics. That is worth evaluating before assuming you need to hold at 70B for capability reasons.

The recommended sampling parameters from the Hermes 4.3 model card are `temperature=0.6, top_p=0.95, top_k=20`. If your inference configuration was tuned for Hermes 3 defaults and you are migrating to 4.3, re-evaluate sampling parameters. Parameters tuned for one model generation often produce suboptimal results on the next, particularly when the training corpus and alignment approach changed significantly (as they did here).

For Hermes Agent, the framework itself is model-agnostic. You can run it against Hermes 4.3 locally via HuggingFace or Ollama, or against any of the 200+ models on OpenRouter. The framework upgrade path (v0.x version bumps) is separate from the model upgrade path and both should be evaluated independently when planning a production update cycle.

Teams running on-premise deployments for compliance reasons should note that Hermes Agent v0.5.0's supply chain hardening (removal of litellm, pinned dependencies) and v0.6.0's official Docker container support together make the framework more suitable for environments with strict software composition requirements. Both are worth verifying with your security team before deployment in regulated contexts.

## When Hermes Makes Sense in 2026 vs Alternatives

Hermes models and the Hermes Agent framework make sense when two conditions are both true: you need model-level steerability that base-model alignment reduces (Hermes consistently scores higher on RefusalBench than comparable-size alternatives), and you are comfortable with or require open-weight deployment on your own infrastructure. Teams with data residency requirements, air-gapped compliance environments, or GPU infrastructure they want to fully utilize are the natural fit. For teams without those constraints and comfortable with API-only providers, the open-weight model operational overhead is a cost that does not pay off. Our [full Hermes Agent guide](https://petronellatech.com/blog/hermes-agent-ai-guide/) covers the framework-level trade-offs against alternatives in more detail.

## Roadmap Signals and What to Expect by Year-End

Nous Research has not published a formal roadmap document as of April 2026. What can be reasonably inferred from the release trajectory:

The Psyche decentralized training network is clearly an active investment. Hermes 4.3 being explicitly the first model trained this way suggests Nous Research is treating Psyche as a production training infrastructure path, not a one-off experiment. Subsequent model releases will likely also use Psyche, and the decentralized training approach may enable larger parameter counts or faster iteration cycles as the network grows.

The Nous Tool Gateway that shipped in v0.10.0 positions Nous Portal as a full-stack inference and tooling platform rather than just a model hosting service. If the gateway expands to cover more tool categories (retrieval, specialized code execution, domain-specific data sources), Hermes Agent on Nous Portal becomes meaningfully more capable for subscribers without requiring external service configuration.

The pace of messaging platform additions suggests the agent team is pushing toward comprehensive coverage of business communication tools. At 16 platforms as of v0.9.0, the remaining high-value additions are primarily enterprise-specific platforms. Microsoft Teams integration is the conspicuous absence for enterprise use cases and would likely be the highest-impact addition from a business adoption standpoint.

Community inference capacity for Hermes 4.3 via GGUF quantizations continues to grow. If Nous Research follows its pattern from Hermes 3, the next model release will be in late 2025 or 2026 on a larger or different base with continued expansion of the post-training corpus. Hermes 5, if that naming convention continues, is reasonable to anticipate, though Nous Research has not announced a timeline.

## Using Hermes Agent in Compliance and Security Contexts

Petronella Technology Group works with organizations that need AI agent capabilities but operate under compliance frameworks including CMMC, HIPAA, and CJIS. The questions we hear most often about Hermes in those contexts:

**Can Hermes Agent run fully air-gapped?** Yes, with some configuration. You need a local inference backend (Ollama is the simplest path), a local model (Hermes 4.3 GGUF variants work well), and you need to disable or not configure any cloud provider endpoints. The agent will run without internet connectivity if the inference backend is local. The Nous Tool Gateway (v0.10.0) requires Nous Portal access and is not available in air-gapped deployments, but web search and browser automation can be replaced with MCP-based local alternatives.

**How does the skills system interact with sensitive data?** Skills are stored as files on the local filesystem in the skills directory. If a skill is created from a task involving sensitive data and the skill includes examples or context from that task, those are in the skill file. Review your skills directory periodically in sensitive environments. The skills improvement system edits existing skill files when it finds better approaches, so skill files can grow over time.

**What about the memory system and data retention?** Memory files are stored locally. There is no automatic cloud sync of memory in the self-hosted configuration. The `USER.md` and other memory files are plaintext and can be reviewed, edited, or deleted as needed for compliance purposes. If you are building workflows that will process PHI or CUI, Petronella Technology Group recommends a formal data mapping exercise before deployment to document where agent memory may capture regulated information.

If your organization is evaluating Hermes Agent for regulated environments and needs assistance with the architecture review, deployment configuration, or compliance implications, the Petronella Technology Group AI consulting team can help. Reach us at [(919) 348-4912](tel:+19193484912) or through our [AI consulting services page](https://petronellatech.com/ai/ai-consulting-services-raleigh-nc/).