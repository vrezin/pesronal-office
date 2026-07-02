# Pi Intake Secretary

- Date: 2026-07-02
- Status: Active
- Runtime target: Raspberry Pi OpenClaw
- Proposed agent: `intake`
- Telegram account: `personal-office-intake-telegram`

## Decision

The Pi-primary Personal Office should have a general `intake` secretary for
incoming non-domain-specific mess.

`job-search` remains a specialized downstream contour. It should not own direct
Telegram input or output.

## Role

The intake secretary is the first routing layer:

1. receive raw input from Telegram/Gmail/manual messages;
2. classify it using `secretaries/routing-map.md`;
3. create the smallest durable trace;
4. update the owning artifact or create a domain handoff;
5. create active/waiting tasks when needed;
6. ask a clarification question when the route is unsafe to guess.

## Boundary

The intake secretary must not own every domain.

Examples:

- vacancies, HH, LinkedIn, CV, cover letters -> hand off to `job-search`;
- recruiter messages that look like consulting/advisory/fractional CTO/CIO
  opportunities -> route as `personal-projects/opportunities/` first, even if
  the link is on LinkedIn;
- meetings, interview prep, reminders -> Calendar secretary route;
- money, debts, assets, payments -> Finance secretary route;
- AI Studio / Fincom / Setronica -> Company secretary route;
- weekly cleanup and repeated noise -> Archivist route.

## Telegram Account Strategy

Use the existing Telegram bot token as the Personal Office intake front door.

The old `job-search-telegram` binding is deprecated. The intended state is:

- `personal-office-intake-telegram` -> `intake`;
- no direct Telegram binding for `job-search`.

The intake secretary owns user-facing language. Domain agents should return
structured handoffs in the minimal format defined by
`secretaries/handoff-contract.md`.

## Repo Artifacts Added

- `secretaries/operating-model.md` - secretary roles and composition model.
- `automation/prompts/pi-intake-secretary.md` - Pi intake prompt.
- `automation/scripts/setup-pi-intake-telegram-channel.sh` - secret-free setup
  helper for a separate intake Telegram account.
- `tools/raspberrypi-openclaw/intake-agent-workspace-AGENTS.md` - bootstrap
  instructions copied to the OpenClaw `intake` workspace.
- `tools/raspberrypi-openclaw/intake-agent-workspace-BOOTSTRAP.md` - runtime
  bootstrap override that disables generic OpenClaw onboarding for the intake
  workspace.
- `secretaries/handoff-contract.md` - minimal internal agent handoff format.
- `automation/prompts/pi-job-search-handoff-dispatch.md` - single-handoff
  prompt for the `job-search` agent.
- `automation/scripts/dispatch-pi-job-search-handoff.sh` - dispatcher from
  intake-created handoff artifact to `job-search` agent run and structured
  handoff output.

## Runtime Evidence

2026-07-02:

- OpenClaw agent `intake` was created on the Pi.
- Workspace:
  `/home/openclaw/personal-office-agent/openclaw-workspaces/intake`.
- Agent dir:
  `/home/openclaw/personal-office-agent/openclaw-agents/intake`.
- Model: `openai/gpt-5.5`.
- Initial routing rules: `0` before Telegram binding migration.
- Telegram account `personal-office-intake-telegram` is configured and enabled.
- Active binding:
  `intake <- telegram accountId=personal-office-intake-telegram`.
- `job-search` has `0` routing rules and no direct Telegram binding.
- `openclaw-gateway.service` was restarted and is active on the Pi.
- First Telegram test exposed pairing mode; sender `telegram:113174019` was
  approved with `openclaw pairing approve telegram <code>`.
- Second Telegram test proved gateway routing to
  `session:agent:intake:telegram:direct:113174019`, but failed because the
  isolated `intake` agent had no OpenAI auth profile.
- Runtime fix: initialized
  `/home/openclaw/personal-office-agent/openclaw-agents/intake` from the
  working default agent runtime state, then corrected
  `schema_meta.agent_id` in `intake/openclaw-agent.sqlite` from `default` to
  `intake`.
- Final Telegram smoke succeeded: the intake agent created
  `inbox/processed/2026-07-02-reminder-call-insurance.md`,
  `tasks/active/2026-07-03-call-insurance.md`, created OpenClaw cron
  `08e9a569-a568-456d-93dc-8a6a01daf279`, and sent a Telegram reply without
  the previous auth/database identity errors.
- Follow-up routing smoke showed the remaining gap:
  `intake -> durable handoff artifact` worked, and `job-search -> structured
  handoff` worked when run manually, but there was no small dispatcher joining
  those two steps.
- Dispatcher target:
  `intake handoff -> dispatch-pi-job-search-handoff.sh -> job-search structured
  handoff -> intake/output reply`.
- Dispatcher installed and smoke-tested:
  `automation/scripts/dispatch-pi-job-search-handoff.sh` processed the existing
  HH vacancy `134758284` handoff, called `job-search`, wrote
  `automation/runs/2026-07-02-1805-pi-job-search-handoff-dispatch.md`, and
  returned a structured handoff.
- Integrated intake smoke succeeded: after the prompt update, `intake` routed a
  Telegram-style HH vacancy message, reused the handoff artifact, called the
  dispatcher, and returned a concise intake/output reply without exposing raw
  dispatcher output as the user-facing answer.
- Intake model was changed from `openai/gpt-5.5` to
  `openai/gpt-5.4-mini`; `job-search` remains on `openai/gpt-5.5`.
- Post-switch mini smoke succeeded: `intake` correctly classified a
  non-operational smoke message as requiring no durable artifact.

## Setup Sketch

Use the existing Telegram bot token file on the Pi:

```bash
OPENCLAW_TELEGRAM_BOT_TOKEN_FILE=/home/openclaw/.config/personal-office/secrets/telegram-job-search-bot-token.txt \
TELEGRAM_INTAKE_TARGET=<owner-chat-id> \
automation/scripts/setup-pi-intake-telegram-channel.sh
```

Expected binding:

```text
intake <- telegram accountId=personal-office-intake-telegram
job-search has no direct Telegram binding
```

## Acceptance

First slice is done when:

- OpenClaw has an `intake` agent;
- Telegram account `personal-office-intake-telegram` is configured and bound to
  `intake`;
- `job-search` has no direct Telegram binding;
- a manual Telegram message such as "remind me tomorrow to call X" creates or
  updates the correct repo artifact;
- the bot replies with route, artifact path, and next action;
- a job-search-shaped Telegram input is routed via intake instead of direct
  job-search binding.
