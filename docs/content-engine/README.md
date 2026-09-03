# Ginkgo Autonomous Content Engine

## Status
ARCHITECTURE / P0 PLANNING

## Objective
Create a governed agentic content factory with two primary outputs:

1. automated vertical short-form video production and publishing;
2. interactive NPC live-stream direction for TikTok LIVE-compatible execution surfaces.

The engine shares strategy, scripts, personas, assets, moderation, observability and analytics while keeping each execution path isolated.

## Core architecture

```text
Content Strategy / Topic Discovery
            |
            v
     Script + Hook Engine
            |
      +-----+------------------+
      |                        |
      v                        v
video.stickman.direct     live.npc.direct
      |                        |
Storyboard / Prompt Pack   Persona + State Machine
      |                        |
video.render               live.npc.react
      |                        |
video.assemble             Renderer / OBS Adapter
      |                        |
QA / Moderation            Moderation / Human Override
      |                        |
 social.vertical.publish    TikTok LIVE execution surface
      |                        |
      +-----------+------------+
                  v
        analytics.content.evaluate
                  |
                  v
        content.strategy.optimize
```

## Canonical capabilities

### P0 capabilities
- `video.stickman.direct`
- `social.vertical.publish`
- `live.npc.direct`
- `live.npc.react`
- `live.moderate`
- `analytics.content.evaluate`

### Later capabilities
- `content.topic.discover`
- `content.script.generate`
- `video.render`
- `audio.voice`
- `video.caption`
- `video.assemble`
- `social.publish`
- `content.strategy.optimize`

## Vertical-video pipeline

```text
Topic
-> Script
-> Hook
-> Storyboard
-> Stickman Director
-> Render Provider
-> Voice / Captions
-> FFmpeg Assembly
-> QA
-> Publish Adapter
-> Metrics
-> Strategy Optimizer
```

### Invariants
- vertical-first default: `9:16`;
- storyboard approval before paid rendering;
- provider-agnostic direction contract;
- AI-generated-content metadata when required by destination platform;
- deterministic QA before publishing;
- credentials never embedded in capability contracts;
- publishing remains a separate capability from creation;
- every execution returns evidence and cost metadata.

## NPC LIVE pipeline

```text
Live Event
-> Event Adapter
-> Policy / Moderation
-> NPC State Machine
-> live.npc.react
-> Animation / Scene / Voice Action
-> Renderer / OBS Adapter
-> Streaming Surface
-> Evidence + Metrics
```

### Supported event classes
- comment;
- like milestone;
- follow;
- gift;
- timer;
- state threshold;
- moderator command;
- operator override.

### NPC state example

```text
idle
  -> excited
  -> rage
  -> boss_mode
  -> cooldown
  -> idle
```

State transitions must be explicit, bounded and auditable.

## Safety and platform invariants
- no fake representation of human presence;
- no autonomous bypass of platform rules or access restrictions;
- moderation runs before generative response execution;
- operator kill switch is mandatory for LIVE;
- rate limits for comments, gifts and reactions;
- no secrets in prompts, logs or public evidence;
- external platform policies remain authoritative;
- live execution adapter remains replaceable because TikTok LIVE access surfaces can change.

## Ginkgo Runtime integration

```text
Intent / Event
-> CapabilityRequest
-> Capability Bus
-> Policy
-> Executor Router
-> Executor Contract
-> Executor
-> Normalized Result + Evidence
```

The Content Engine does not recreate the Runtime. It registers capabilities and adapters that the Runtime can execute.

## Arsenal model

Each external integration must be represented through the Ginkgo Arsenal model:

`Capability -> Skill -> Binding -> Adapter -> Provider -> Endpoint`

Examples:

```text
video.render
-> stickman-render
-> production-binding
-> comfyui-adapter
-> local-comfyui
-> /prompt
```

```text
social.vertical.publish
-> publish-short-video
-> tiktok-production
-> tiktok-content-posting-adapter
-> TikTok
-> Content Posting API
```

```text
live.npc.react
-> npc-reaction
-> live-production
-> obs-render-adapter
-> OBS / authorized live surface
-> live renderer endpoint
```

## n8n role
n8n is an executor/orchestrator, not the decision brain.

Use n8n for:
- scheduling;
- queues;
- webhook handling;
- media handoff;
- publishing workflows;
- analytics ingestion;
- retries and operational notifications.

Do not put canonical policy, tenancy rules or capability semantics only inside workflow nodes.

## Observability
Every run should capture:
- `request_id`;
- `capability_id`;
- `provider`;
- `execution_handle`;
- normalized status;
- result summary;
- evidence refs;
- token/API/render cost;
- duration;
- moderation outcome;
- publish/live destination;
- performance metrics when available.

## Roadmap

### P0 — Contracts and governance
Define contracts, state machines, schemas, provider boundaries, moderation and evidence.

### P1 — Vertical-video production
Connect one render provider, FFmpeg assembly, captions/voice and a controlled publish adapter.

### P2 — NPC LIVE prototype
Implement a local/controlled renderer with deterministic event simulation, state transitions, moderation and operator override before connecting a real live surface.

### P3 — Autonomous content loop
Use performance evidence to choose topics, hooks, formats, publishing windows and which characters/themes graduate into LIVE experiments.

## Promotion criteria
A capability moves from PROTOTYPE to VALIDATED only when:
- request/result schemas are stable;
- deterministic contract tests pass;
- provider failure is normalized;
- cost boundaries exist;
- moderation and human override are tested where applicable;
- evidence is persisted;
- no secret or provider-specific leakage exists in the canonical contract.

## Upstream reference
The Stickman direction concept was inspired by `kaomei/stickman-video-director` (MIT). Preserve upstream attribution and license requirements if code or substantial prompt material is reused.
