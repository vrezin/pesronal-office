# OpenClaw Personal Office Operating Model

- Created: 2026-06-25
- Purpose: internet-backed OpenClaw setup research plus Personal Office operating model for the Raspberry Pi agent.
- Target host: `raspberrypi-codex`
- Related cookbook: `tools/raspberrypi-openclaw/personal-office-agent-cookbook.md`
- Related sync manifest: `tools/raspberrypi-openclaw/cookbook-sync-manifest.md`

## Executive Decision

The Raspberry Pi OpenClaw node should be a **cookbook-trained local agent host**, not a mirror of Personal Office private data.

The right first version is:

1. OpenClaw installed on the Pi.
2. Gateway kept local/loopback until explicitly widened.
3. Agent workspace seeded with Personal Office protocols, maps, skills, and playbooks.
4. No broad copy of `finance/`, `people/`, `life/`, `inbox/`, `memory/`, `companies/`, `calendar/`, or `tasks/`.
5. Agent asks for narrow context handoffs and prepares patches instead of freely browsing raw data.

This fits both OpenClaw's security model and the way Personal Office actually works.

## Product Constraint: Local Does Not Excuse Context Bloat

Personal Office may be sold and deployed as a local installation, but local-first deployment does not solve context overload by itself.

Even on local infrastructure, the agent will feel slow, wasteful, and unreliable if every small task loads broad workspace prompts, unused skills, irrelevant tools, raw data, and stale project context.

Therefore the product must treat prompt/context size as a first-class operating budget:

- bootloader files stay small;
- skills are short routers, not encyclopedias;
- detailed procedures live in playbooks loaded only when needed;
- raw data is never copied into the default workspace;
- context enrichment is narrow and explicit;
- path validation and patch drafting use compact handoffs;
- every agent lane should declare what it loads by default and what it must request lazily.

The goal is not only privacy. It is responsiveness, lower cognitive noise, lower model cost, and more predictable behavior.

## External OpenClaw Findings

### Official Setup Path

OpenClaw's official docs recommend:

- Node.js 24, with Node.js 22.19+ also supported.
- `openclaw onboard --install-daemon` as the guided setup path.
- `openclaw gateway status` to verify the Gateway.
- `openclaw dashboard` for local Control UI.
- A model provider/API key during onboarding.

For this Pi, the practical runtime is Node.js 22.23.1 because the Pi currently has 32-bit `armhf` userland and OpenClaw's Node 24 Linux downloads are ARM64-only.

### Gateway And Security Model

OpenClaw's official security guidance is explicitly a **single trusted operator** model:

- one user/trust boundary per Gateway;
- not a hostile multi-tenant boundary;
- split by separate gateway, credentials, OS user, or host if different trust boundaries are needed.

This is compatible with a personal home Pi agent, but only if we do not make it a shared multi-user automation box.

### Exposure Baseline

Before any remote exposure, OpenClaw's exposure runbook says to inventory:

- host, OS user, state directory;
- bind mode and Gateway URL;
- auth mode and token source;
- enabled channels and who can message them;
- reachable agents;
- tool profile and sandbox mode;
- credentials available to agents;
- backups of config and credentials.

The official minimum-safe exposed baseline is conservative:

- Gateway bound to loopback;
- token auth;
- per-channel-peer DM scoping;
- sandbox mode for non-main sessions;
- messaging tool profile;
- exec denied by default;
- elevated tools disabled.

For Personal Office, do not expose the Gateway remotely until this inventory exists as a checked artifact.

### Skills And Agent Scope

OpenClaw skills can be restricted per agent:

- omit default skill allowlist to leave unrestricted;
- set `agents.defaults.skills` for a shared baseline;
- set `agents.list[].skills: []` for no skills;
- set a non-empty agent list as the final allowed skill set.

For this project, the safe direction is a dedicated Personal Office agent with a small allowlist:

- cookbook-reading skill or filesystem access only to cookbook bundle;
- no browser/channel/cron/finance/connectors initially;
- no write tools against live Personal Office until the handoff protocol is tested.

### Sandboxing

OpenClaw sandboxing can run tool execution in isolated backends. The docs say it is not a perfect boundary, but it materially reduces filesystem/process blast radius.

For the Pi, sandboxing is desirable before enabling real writes or external channels. Current practical blocker: Docker is not installed on the Pi yet.

### What Works

Use these patterns:

- Start with local Control UI or CLI-only testing before channels.
- Keep Gateway on loopback/local network first.
- Use explicit pairing/allowlists for DMs if channels are added.
- Keep agent workspaces separate by purpose.
- Use skills/playbooks as the durable operating layer.
- Run `openclaw doctor`, `openclaw security audit`, `openclaw security audit --deep`, and `openclaw health` before widening access.
- Prefer a strong current model for tool-using agents because weak models are easier to prompt-inject.
- Review third-party skills/plugins as code, not as harmless prompts.
- Keep logs and run state so agent actions are inspectable.

### What Does Not Work

Avoid these patterns:

- Running OpenClaw on the primary personal machine with broad host access.
- Copying all personal data into the agent workspace.
- Exposing Gateway publicly before audit and rollback plan.
- Allowing all DMs or group messages into a tool-enabled agent.
- Installing marketplace/community skills without review.
- Treating exec allowlists as a strong security boundary.
- Treating `sessionKey` or chat identity as a real auth boundary.
- Giving the agent cookies, browser profiles, finance tokens, SSH keys, or `.env` files during first setup.
- Letting the agent read arbitrary raw inbox/web pages and then execute tools without human review.

Security research and industry writeups repeatedly point to the same risk families: indirect prompt injection, unsafe tool execution, credential leakage, malicious skills/plugins, public Gateway exposure, and cross-layer policy bypass. So the deployment model must assume untrusted content and minimize authority.

## Personal Office Operating Model

### Core Principle

Personal Office is a workflow-first / owned-context operating system.

It is not:

- a chat log;
- a dump of files;
- a generic AI assistant memory;
- a replacement for every external product.

It is:

- a dispatcher and decision layer;
- a project/customer/business contour router;
- a durable routing system;
- a live action queue;
- a controlled private context;
- a way to convert messy input into artifacts, tasks, meetings, memory, and project handoffs.

### Prime Directive

Important outcomes must not remain only in chat.

If input contains a decision, promise, deadline, meeting, amount of money, obligation, risk, opportunity, person, or next step, the system creates or updates the relevant artifact.

### Default Flow

1. Capture raw input if the source matters.
2. Extract facts, fact confidence/evidence level, hypotheses, feelings/weak signals, ideas, risks, people, projects, and next steps.
3. Pull in related project, person, company, task, processed-note, and memory context when safe and available.
4. Determine the context and project/business/customer contour.
5. Decide what stays in Personal Office and what belongs in a project workspace.
6. Route it through `secretaries/routing-map.md`.
7. Choose the smallest relevant `wiki/maps/` domain.
8. Read the matching router skill from `.codex/skills/`.
9. Read the matching `wiki/playbooks/` procedure only when needed.
10. Create or update the durable artifact.
11. Create/update `tasks/active/` or `tasks/waiting/` if there is action or dependency.
12. Link reusable facts/hypotheses/ideas from wiki/navigation when needed.
13. Leave processed trace in `inbox/processed/`.
14. Close the loop later: done, waiting, blocked, stale, parked, or escalated.

### Live Queue Philosophy

The office should always answer:

- What needs attention now?
- What is waiting?
- What is blocked?
- What is stale?
- What can be ignored?
- Which insight from `inbox/processed/` needs to become active work?

Per-item active tasks are preferred over giant combined queues.

### Repo Boundary

Personal Office is the owner-management layer.

Execution belongs in the target workspace when work becomes real:

- AI Studio/MedVoice truth lives in `<aistudio-root>`;
- Fincom truth lives in `<fincom-root>`;
- Setronica truth lives in `<setronica-root>`;
- Personal Office keeps owner-side context, routing, commitments, people, and handoff envelopes.

Do not leak Personal Office concerns into company repos, and do not mirror all company internals into Personal Office.

If a project does not exist yet, Personal Office should either initiate project creation through the user, keep the material in its own contour until the project exists, or park/close the idea if it dies.

### Skills Architecture

The active skill architecture is deliberately small:

- `personal-office-intake` - raw intake and routing.
- `memory-system` - memory retrieval, capture, consolidation, entities, graph.
- `personal-brand-career` - vacancies, HH, CVs, cover letters, career economics.
- `life-planning` - health/lifestyle facts, medication, meals, groceries, plans.
- `company-work` - AI Studio, Fincom, Setronica, contracts, company signals, handoffs.
- `automation-monitoring` - scheduled jobs, prompts, state, run logs, monitors.

Detailed procedures live in `wiki/playbooks/`.

This is intentional: router skills stay short, playbooks carry detail, old micro-skills remain disabled as history.

### Automation Pattern

Scheduled automation should update the same surfaces the user uses manually:

- `automation/prompts/` for prompts;
- `automation/scripts/` for wrappers;
- `automation/state/` for idempotency and last-run markers;
- `automation/runs/` for logs;
- `tasks/active/` and `tasks/waiting/` for real next actions.

Automation must not need Git commits to be considered successful. Run logs and state markers are enough for unattended durability.

### Memory Pattern

Memory helps retrieval but does not replace source of truth.

Rules:

- facts belong first in domain artifacts;
- memory summarizes and indexes;
- sensitive details stay minimal;
- link to source artifacts instead of copying raw private data;
- if memory and source disagree, source wins.

### Clarification Stop

When routing is unclear, do not guess.

Create a `needs-clarification-YYYY-MM-DD-topic.md` note with:

- what was captured;
- what is known;
- plausible route choices;
- exact missing facts;
- what must not happen until clarified.

## Personal Office Ideas To Preserve

### Workflow-First OS

The core product idea is not "AI OS" as a fancy interface.

The useful version is:

> intake -> classification -> decision -> task/calendar/memory/project artifact -> recheck/close the loop.

The missing layer is the live action queue, not a new visual shell.

### Owned-Context OS

The system should preserve user-owned context across tools instead of forcing migration into one SaaS.

Google, Yandex, mail, docs, calendar, Telegram, Obsidian/Notion, CRM, finance tools and project repos can remain inputs or execution surfaces.

Personal Office owns:

- routing;
- durable state;
- workflow truth;
- traceability;
- action queue;
- memory and context recovery.

### Private AI Office

The broader product thesis:

> a client-controlled private operating contour for owner context, decisions, documents, tasks and workflows.

The buyer is not buying "AI" or "cloud". The buyer buys less context loss, fewer forgotten promises, fewer stale decisions, better recovery of the working picture, and workflow adaptation.

### AI Chief Of Staff Wedge

First sellable wedge:

> AI Chief of Staff for a founder/business owner.

It should:

- read allowed inbox/messages;
- remember commitments;
- extract tasks and follow-ups;
- track stale decisions;
- prepare meeting summaries;
- prepare weekly control;
- distinguish routine from uncertainty;
- prepare context for human decisions without replacing the owner.

The 14-day pilot should be one person, one channel, one workflow, one weekly control loop.

### AI Roles In The Office

The user's repeated role model:

1. Orchestrator - connects tools and routes work.
2. Validator/assistant/secretary - checks, remembers, summarizes, follows up.
3. Software developer - creates small task-specific tools when needed.

The third role is powerful but should not be the buyer-facing headline.

### Client-Controlled, Provider-Not-Readable

For premium/sensitive segments, the product must be:

> installable, supportable, recoverable and updateable, but not provider-readable.

Provider supplies:

- workflow packages;
- agent configurations;
- updates;
- health checks;
- backup/restore procedures;
- security hardening;
- audit/logging patterns;
- operator training.

Client controls:

- data;
- keys;
- documents;
- local memory;
- connectors;
- model/API keys;
- logs and indexes.

### Family Office As Channel, Not Core

Family office/private wealth is a useful validation channel because it exposes strong trust constraints:

- sensitive documents;
- high-value decisions;
- no provider content access;
- need for continuity, backup, audit, restore;
- trusted internal operators.

But the general product is not wealth reporting by default.

### Cookbook Before Data

For the Raspberry Pi/OpenClaw node, the correct first principle is:

> teach the agent the office protocol before giving it office facts.

The Pi receives cookbooks, not private records.

The agent should answer:

1. Which route applies?
2. Which context is needed?
3. Which artifact would change?
4. Can it draft a patch from user-provided input alone?

## Raspberry Pi Implementation Implications

### Current State

- OpenClaw 2026.6.10 installed.
- Node.js 22.23.1 installed in user-local path.
- Gateway not running.
- Tailscale exposure off.
- Cookbook bundle synced to `/home/pi/personal-office-agent/cookbooks/personal-office/`.
- A too-wide partial copy exists at `/home/pi/personal-office-agent/workspaces/personal-office/`; do not use it.

### Next Safe Steps

1. Remove or quarantine the broad partial copy.
2. Create an OpenClaw agent workspace that points only to the cookbook bundle.
3. Seed the workspace with a short `AGENTS.md`/`USER.md` that names `tools/raspberrypi-openclaw/personal-office-agent-cookbook.md` as the entrypoint.
4. Run local CLI or dashboard smoke test.
5. Ask the agent to classify a synthetic input using only cookbooks.
6. Ask the agent to request a narrow context handoff instead of reading raw data.
7. Only then decide whether to enable a channel such as Telegram.

### First Agent Policy

The Personal Office Pi agent should be configured as:

- single operator;
- local gateway;
- no public exposure;
- no broad file workspace;
- no channel initially;
- no raw Personal Office data;
- no browser profile/cookies;
- no finance tools;
- no unattended writes;
- explicit human approval for any proposed live repo change.

### Later Capabilities

Only after the cookbook-only loop works:

- Telegram or local dashboard for commands;
- narrow context handoff script;
- patch-generation workflow;
- read-only task queue summaries;
- approved writeback to source repo;
- systemd user service;
- health checks and run logs;
- Tailscale-only remote access if needed.

## To-Be Decomposition

The component/workflow/skill decomposition for OpenClaw lives in:

- `tools/raspberrypi-openclaw/personal-office-openclaw-decomposition.md`

## Source Notes

External sources checked on 2026-06-25:

- OpenClaw README: https://github.com/openclaw/openclaw
- Getting started: https://docs.openclaw.ai/start/getting-started
- Onboarding CLI: https://docs.openclaw.ai/start/wizard
- Security: https://docs.openclaw.ai/gateway/security
- Gateway exposure runbook: https://docs.openclaw.ai/gateway/security/exposure-runbook
- Skills: https://docs.openclaw.ai/tools/skills
- Configuration: https://docs.openclaw.ai/gateway/configuration
- Sandboxing: https://docs.openclaw.ai/gateway/sandboxing
- Agent bootstrapping: https://docs.openclaw.ai/start/bootstrapping
- Security-risk background: https://arxiv.org/abs/2603.27517
- Runtime hardening idea: https://arxiv.org/abs/2603.11853
- Practical safety article: https://www.techradar.com/pro/how-to-safely-experiment-with-openclaw

Personal Office sources:

- `AGENTS.md`
- `wiki/README.md`
- `secretaries/routing-map.md`
- `.codex/skills/`
- `wiki/playbooks/`
- `tools/raspberrypi-openclaw/`
- `companies/future-companies/2026-06-21-private-ai-office-product-one-pager.md`
- `companies/future-companies/2026-06-24-private-ai-office-architecture-product-frame.md`
- `tasks/active/2026-06-21-validate-premium-personal-ai-cloud-offer.md`
