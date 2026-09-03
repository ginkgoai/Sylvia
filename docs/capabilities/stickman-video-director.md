# Stickman Video Director — Ginkgo Capability

Status: PROTOTYPE CANDIDATE
Source inspiration: `kaomei/stickman-video-director` (MIT)
Owner domain: Content / Video / Agent-facing capability

## Objective

Transform a user idea, article, script or campaign concept into a production-ready short-form stickman video package, with explicit directing decisions before generation.

The Ginkgo version should treat the upstream project as a reference implementation and reusable design pattern — not as the final product boundary.

## Core promise

Input → narrative compression → scene direction → prompt package → render orchestration → assembly → publishable asset.

Primary output target:
- 45–60 second short video;
- 6 scenes of roughly 8–10 seconds;
- 9:16 as default for TikTok/Reels/Shorts;
- optional 16:9 and 1:1;
- consistent character, palette, typography, VO, soundtrack and transitions.

## Proposed Ginkgo pipeline

```text
User / Campaign / Agent
        ↓
Content Brief
        ↓
Script & Hook Planner
        ↓
Stickman Director
        ↓
6-scene Storyboard Contract
        ↓
Prompt Pack
        ↓
Video Provider Adapter
   ├─ Gemini video generation
   ├─ ComfyUI workflow
   └─ future providers
        ↓
Scene Validator
        ↓
FFmpeg / Assembly
        ↓
Caption + Audio + Branding
        ↓
Postiz / Social Publisher
```

## Capability boundary

### Capability
`video.stickman.direct`

Purpose: convert approved content into a deterministic storyboard/prompt contract.

It must NOT own model credentials, social publishing, storage, billing, or provider-specific execution.

### Inputs

```json
{
  "source": "string",
  "language": "pt-BR",
  "output_language": "pt-BR",
  "aspect_ratio": "9:16",
  "duration_seconds": 60,
  "theme": "light|dark",
  "accent_colors": ["#hex"],
  "tone": "educational|viral|story|sales|motivational",
  "brand_context_ref": "optional-ref",
  "voice_ref": "optional-ref"
}
```

### Canonical outputs

```json
{
  "title": "string",
  "hook": "string",
  "narration": "string",
  "visual_language": {},
  "scenes": [
    {
      "index": 1,
      "duration_seconds": 10,
      "voiceover": "string",
      "visual_metaphor": "string",
      "camera": "string",
      "motion": "string",
      "onscreen_text": [],
      "transition_in": "string",
      "transition_out": "string",
      "sfx": [],
      "prompt": "string",
      "negative_prompt": "string"
    }
  ],
  "assembly_notes": {},
  "evidence": []
}
```

## Product behavior

1. Accept raw idea, script, article, offer or educational topic.
2. Preserve factual meaning; do not fabricate claims.
3. Generate a strong hook and coherent 6-scene narrative.
4. Produce a human-readable director proposal first.
5. Require approval before expensive render execution.
6. After approval, emit independent prompts with repeated consistency locks.
7. Render each scene through a provider adapter.
8. Validate duration, aspect ratio, continuity and missing scenes.
9. Assemble scenes, narration, music, SFX, captions and brand marks.
10. Return final asset + evidence + cost metadata.

## Ginkgo architecture fit

### Arsenal
Register as agent-facing capability with:
- input/output schema;
- provider bindings;
- cost policy;
- credential refs;
- fallback policy;
- lifecycle evidence.

### Runtime
Execution path:

```text
Intent
→ CapabilityRequest(video.stickman.direct)
→ Capability Bus
→ Policy
→ Executor Router
→ Video Director Executor
→ Normalized Result + Evidence
```

### n8n
n8n may orchestrate:
- campaign trigger;
- approval gate;
- render fan-out for six scenes;
- polling/callbacks;
- FFmpeg assembly;
- upload to storage;
- Postiz scheduling/publishing.

n8n is executor/orchestrator, not the source of truth for the capability contract.

### ComfyUI
Use as an optional visual/video execution backend where suitable. The director contract must remain provider-agnostic.

### Postiz
Publishing layer only. It receives the approved final asset and platform metadata; it does not control directing logic.

## MVP P0

Goal: one prompt in → one validated 9:16 stickman short package out.

P0 scope:
- PT-BR source;
- PT-BR or EN narration;
- 9:16;
- light/dark style;
- 6 scenes;
- storyboard approval gate;
- prompt pack export;
- no automatic paid render required.

Acceptance criteria:
- exactly six ordered scenes;
- total target duration 45–60 seconds;
- hook in first scene;
- every scene has VO + visual action + camera/motion + transition + prompt;
- global visual consistency locks repeated in every independent generation prompt;
- no unsupported factual claims added;
- output validates against canonical schema;
- provider-independent output.

## P1 — Render orchestration

Add:
- Gemini/video provider adapter;
- ComfyUI adapter where applicable;
- parallel scene execution;
- retry policy;
- cost estimation before execution;
- normalized render result;
- scene-level evidence.

## P2 — Assembly

Add:
- FFmpeg assembly;
- TTS/voice layer;
- captions;
- BGM/SFX;
- normalization;
- branding presets;
- final QA.

## P3 — Viral content factory

Add:
- topic/lead/campaign intake;
- reusable hooks library;
- A/B variants;
- batch generation;
- Postiz scheduling;
- performance feedback loop;
- winning-template reuse.

End-state loop:

```text
Trend / Offer / Knowledge
→ Script
→ Director
→ Render
→ Publish
→ Metrics
→ Learn
→ Generate next variant
```

## Guardrails

- No credentials in prompts or repository docs.
- Paid generation requires explicit policy/budget approval.
- Keep generation providers replaceable.
- Preserve provenance for factual source material.
- Do not publish automatically unless a publishing policy explicitly allows it.
- Copyright/license provenance must be tracked for imported templates/assets.

## Upstream reuse strategy

The upstream project is MIT licensed and can be studied or reused under its license terms. Preserve attribution/license where copied code or substantial prompt content is incorporated.

Preferred approach:
1. extract the directing contract and behavioral tests;
2. adapt it into Ginkgo Arsenal schema;
3. keep provider bindings external;
4. add render/cost/evidence contracts;
5. integrate with Runtime only after validation.

## Next slice

`STICKMAN-P0.1 — Director Contract`

Deliver only:
- canonical request schema;
- canonical result schema;
- six-scene invariant;
- approval-state contract;
- provider-agnostic prompt pack;
- deterministic validation tests.

Do not implement render providers in P0.1.
