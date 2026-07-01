# OpenClaw Capabilities And Best Practices For Personal Office

- Created: 2026-06-25
- Purpose: focused review of OpenClaw platform capabilities relevant to Personal Office architecture.
- Sources checked: official OpenClaw docs for Gateway architecture, multi-agent routing, channel routing, pairing, groups, model providers, model failover, models CLI, agent workspace, specialist lanes, delegate architecture.

## Core OpenClaw Model

OpenClaw is built around one long-running Gateway.

The Gateway:

- owns messaging surfaces;
- exposes WebSocket API for CLI, web UI, automations, nodes and apps;
- hosts agents;
- routes inbound messages;
- manages sessions and events;
- can run as foreground process or daemon under systemd/launchd.

The important architectural unit is **agent**, not just "prompt".

An agent is a scoped brain with:

- its own workspace;
- its own `AGENTS.md`, `SOUL.md`, `USER.md` style files;
- its own `agentDir`;
- its own auth profiles;
- its own model registry/config;
- its own session store.

## Multi-Agent Routing

OpenClaw supports multiple isolated agents in one Gateway.

Inbound messages are routed to agents through `bindings`.

Bindings can match:

- channel;
- account id;
- exact peer;
- parent peer/thread;
- Discord guild/roles;
- Slack team;
- channel-wide fallback;
- default agent.

Most-specific routing wins. If multiple bindings match in the same tier, config order matters.

Implication for Personal Office:

- use separate agents for separate responsibilities;
- do not overload one `main` agent with all surfaces;
- bind channels and peers deliberately.

## Channel Capabilities

OpenClaw supports many channels:

- Telegram;
- WhatsApp;
- Discord;
- Slack;
- Signal;
- iMessage;
- Google Chat;
- Microsoft Teams;
- Matrix;
- Mattermost;
- Nextcloud Talk;
- IRC;
- WebChat;
- regional channels such as LINE, WeChat, QQ, Zalo, Feishu.

Channels can run simultaneously. Channel routing is host-controlled and deterministic; the model does not freely choose where to reply.

Fastest first Personal Office path:

1. Local dashboard / WebChat.
2. Telegram bot for owner-only command channel.
3. Later: dedicated channels for automation alerts or family/company contexts.

## Pairing And Access Control

OpenClaw pairing exists for:

- DM access;
- node/device access.

For DMs, unknown senders can receive a short pairing code, and their message is not processed until approved.

Best practice for Personal Office:

- never use open DMs for a tool-enabled Personal Office agent;
- start with owner allowlist/pairing;
- use separate bots/accounts for separate agents if the channel supports it;
- require mention gating in groups;
- avoid always-on group processing until the agent has narrow tools and strong logs.

## Groups And Ambient Context

OpenClaw can operate in groups across many channels.

Defaults are conservative:

- group access restricted;
- mention required unless disabled;
- visible group replies can be controlled.

It also supports ambient room events: unmentioned group chatter can become quiet context while the agent replies visibly only through explicit message behavior.

Personal Office implication:

- group intake should be a later phase;
- if used, groups should feed an intake/review agent, not an agent with broad write access;
- always separate "quiet context capture" from "visible reply/action".

## Models And Providers

OpenClaw supports many model providers and provider variants.

Docs include providers such as:

- Anthropic;
- OpenAI / Codex;
- Google Gemini;
- OpenRouter;
- Mistral;
- DeepSeek;
- Qwen;
- Ollama / local models;
- LM Studio;
- vLLM;
- Groq;
- xAI;
- Cohere;
- Amazon Bedrock;
- many others.

Models are referenced as `provider/model`.

Default selection:

- `agents.defaults.model.primary`;
- ordered `agents.defaults.model.fallbacks`;
- provider auth failover before moving to next model;
- per-agent model override through `agents.list[].model`.

Important implication:

- Personal Office can use different models per agent.
- Cheap/fast model can classify low-risk intake.
- Strong model can handle ambiguous routing, synthesis, and project contour decisions.
- Local/private model can handle sensitive summaries if quality is sufficient.
- Fallbacks can protect availability, but should be explicit and logged.

## Auth Profiles And Failover

Auth profiles are per-agent.

OpenClaw can rotate auth profiles within a provider and then move to fallback models.

Personal Office implications:

- do not share credentials casually across agents;
- do not copy OAuth refresh tokens between agents;
- use separate API keys/profile refs where possible;
- keep sensitive model/provider credentials scoped to the agent that needs them.

### Codex Subscription Auth Finding

OpenClaw can use OpenAI/Codex subscription auth through the Codex provider/plugin path:

- install and enable `@openclaw/codex`;
- run `openclaw models auth --agent <agent-id> login --provider openai --device-code`;
- complete the device-code login in the owner's browser;
- verify with `openclaw models auth --agent <agent-id> list` and `openclaw models status --agent <agent-id>`.

Observed on the Raspberry Pi on 2026-06-25:

- device-code OAuth worked for `po-router`;
- OpenClaw stored `openai/oauth` auth in the agent auth store;
- `openclaw models status --agent po-router` reported runtime auth usable;
- the actual Codex app-server failed on the current OS image because `@openai/codex` rejected `linux (arm)`.

Best practice: before choosing Codex subscription auth as the first Personal Office runtime path, confirm `node -p 'process.platform + " " + process.arch'` returns a supported platform such as `linux arm64` or `linux x64`. A Raspberry Pi with 64-bit kernel but 32-bit `armhf` userland still reports `linux arm` to Node.

## Agent Workspace

The workspace is the agent's home and default working directory.

Important caveat:

- workspace is not a hard sandbox;
- absolute paths can still reach elsewhere on host unless sandboxing is enabled.

Personal Office implication:

- cookbook workspace is safe only because it contains no raw data;
- do not rely on workspace path alone for data isolation;
- enable sandboxing before any agent gets raw repo access or write tools.

## Specialist Lanes

OpenClaw's own guidance: specialist lanes help only when they reduce real bottlenecks.

Bottlenecks include:

- session locks;
- provider/model capacity;
- tool capacity;
- context budget;
- ownership ambiguity.

Best practice:

- each lane needs a written contract;
- define purpose;
- define non-goals;
- define chat budget;
- define handoff rule;
- define tool-risk rule;
- keep heavy work in background tasks/subagents when possible.

Personal Office implication:

- make lanes by workflow ownership, not by abstract persona fantasy;
- every Personal Office OpenClaw agent must have a contract.

## Context Budget And Slimming

The path-validation test showed that a tiny task can still carry a heavy baseline prompt/harness overhead.

Observed on 2026-06-25 for `agent:default:yuliya-path-validation`:

- task input was a single narrow handoff file;
- agent output was compact;
- agent-reported input: `1362`;
- output: `1030`;
- cache read: `17792`;
- total: `20184`;
- prompt tokens: `19154`.

Implication:

- local installation is not enough;
- cookbook-only is not enough;
- each agent must have a context budget and a slim default prompt.

Best practice for Personal Office:

- keep `AGENTS.md` as a bootloader;
- avoid injecting non-essential identity/personality/runtime files into narrow utility agents;
- keep skills allowlists small and workflow-specific;
- expose tools only when the task requires them;
- prefer narrow handoff files over broad repo reads;
- measure prompt tokens per workflow, not only wall-clock success;
- create separate minimal utility agents for path validation, review gates, and formatting if the default router remains heavy.

Open question for the next OpenClaw setup pass:

- which injected workspace files, skills, and tool schemas can be removed from the `po-router` default route without hurting routing quality?

## Delegate Pattern

OpenClaw has a delegate architecture:

- agent has its own identity;
- acts on behalf of a human;
- never impersonates the human;
- uses explicit permissions;
- follows standing orders in `AGENTS.md`.

Personal Office implication:

- if the agent ever sends messages/emails/calendar actions, prefer delegate identity over "pretending to be the user";
- for now, keep output as drafts/patches;
- later, explicit delegated channels can handle low-risk follow-ups.

## Best-Practice Agent Set For Personal Office

### 1. `po-router`

Purpose:

- owner-facing first contact;
- classifies requests;
- extracts facts/hypotheses/ideas;
- decides which lane should own work.

Model:

- fast capable model by default;
- strong fallback for ambiguous routing.

Access:

- cookbook bundle;
- contour index when available;
- no raw sensitive folders.

Channel:

- local dashboard first;
- later owner-only Telegram.

### 2. `po-research`

Purpose:

- web/source research;
- external docs;
- market/tool/provider checks;
- source-backed summaries.

Model:

- strong reasoning model with web/search tools.

Access:

- no personal raw data by default;
- can receive explicit context packets.

### 3. `po-artifact`

Purpose:

- drafts markdown artifacts and patches.

Model:

- strong writing/reasoning model.

Access:

- approved target paths only;
- patch-first mode.

### 4. `po-context`

Purpose:

- context enrichment over people/projects/companies/memory.

Model:

- strong enough for entity linking.

Access:

- initially cookbook + indexes only;
- later controlled read-only context bundles.

### 5. `po-review`

Purpose:

- verifies route, safety, confidence labels, missing questions and patch scope.

Model:

- independent strong model when risk is high.

Access:

- proposed extraction/patch/handoff;
- no broad write tools.

### 6. `po-automation`

Purpose:

- scheduled monitor runs;
- state and logs;
- low-risk recurring workflows.

Model:

- cheap/fast model for known pattern tasks;
- escalation to stronger agent for ambiguity.

Access:

- `automation/prompts/`;
- `automation/scripts/`;
- `automation/state/`;
- `automation/runs/`;
- narrow task surfaces.

## Best-Practice Channel Plan

### Phase 1

- no external channels;
- local CLI/dashboard only;
- synthetic tests.

### Phase 2

- owner-only Telegram bot;
- DM pairing or allowlist;
- no groups;
- no autonomous writes.

### Phase 3

- separate Telegram bot/account for alerts or automation;
- route alert bot to `po-automation`;
- route owner command bot to `po-router`.

### Phase 4

- group channels only for selected contexts;
- mention gating on;
- visible replies controlled;
- group messages go to intake/review, not broad operator.

## Best-Practice Model Plan

Use different models by lane:

- router: fast reliable model;
- context/review/artifact: stronger model;
- research: strong model with web/search;
- automation: cheaper model with escalation;
- sensitive/private: local model only if quality and hardware allow.

Use fallback carefully:

- fallback is good for availability;
- fallback can change privacy/cost/quality posture;
- log fallback notices;
- do not let sensitive lanes silently fall back to a less trusted provider.

## How This Changes Our Decomposition

Earlier decomposition was component-centric. OpenClaw suggests a second axis:

- component/workflow ownership;
- agent/workspace isolation;
- channel binding;
- model/provider policy;
- skill allowlist;
- access level.
- default context budget.

So each Personal Office workflow should be specified as:

```yaml
workflow:
agent:
workspace:
channel_bindings:
model_policy:
skills:
allowed_context:
default_context_budget:
lazy_context_sources:
write_authority:
approval_gate:
handoff_rules:
logs:
```

## Recommended Immediate Next Step

Create the first OpenClaw workspace for `po-router`:

- cookbook-only workspace;
- no channels;
- no raw data;
- model configured;
- test against synthetic inputs;
- require it to output:
  - extracted facts/hypotheses/ideas;
  - confidence;
  - related context it would request;
  - target contour;
  - artifact proposal;
  - open questions.
