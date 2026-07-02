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
- `secretaries/handoff-contract.md` - minimal internal agent handoff format.

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
