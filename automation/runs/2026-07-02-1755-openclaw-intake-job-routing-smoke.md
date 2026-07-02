# OpenClaw Intake / Job-Search Routing Smoke

- Timestamp: 2026-07-02 17:55 +07
- Runtime: Raspberry Pi OpenClaw
- Telegram account: `personal-office-intake-telegram`
- Intake agent: `intake`
- Job-search agent: `job-search`
- Gmail account: `v.rezin@gmail.com`
- Gmail mutation: none; read-only search/read
- Telegram mutation: smoke replies only where explicitly tested; job-search did not send Telegram directly

## Routing Shape

OpenClaw gateway routing is channel-level:

```text
telegram:personal-office-intake-telegram -> intake
```

Intent-level routing currently happens inside the `intake` agent prompt. Intake writes
handoff artifacts for the target domain. It does not yet perform an automatic live
`intake -> job-search -> intake reply` dispatch.

## Smoke Results

### Reminder Baseline

Earlier Telegram smoke proved the general intake path:

- Telegram direct message from `telegram:113174019` reached `intake`.
- Intake created:
  - `inbox/processed/2026-07-02-reminder-call-insurance.md`
  - `tasks/active/2026-07-03-call-insurance.md`
- OpenClaw cron reminder created:
  - `08e9a569-a568-456d-93dc-8a6a01daf279`

### Opportunity-Shaped LinkedIn Message

Input: recruiter message for `Implementation Partner (Former CTO/CIO) for Russia`
with LinkedIn job id `4431259712`.

Result:

- Correctly routed by intent as opportunity/consulting/fractional CTO-CIO first,
  not as ordinary LinkedIn vacancy analysis.
- Created:
  - `inbox/processed/2026-07-02-linkedin-implementation-partner-russia-opportunity.md`
  - `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-linkedin-implementation-partner-russia-opportunity-handoff.md`
  - `tasks/waiting/2026-07-02-review-linkedin-implementation-partner-russia-requirements.md`
- Blocker: LinkedIn requirements are not captured in the repo yet.

### Plain HH Vacancy Link

Input: HH vacancy URL for vacancy id `134758284`.

Result:

- Correctly routed to `job-search` / `personal-projects/personal-brand/workspace/job-intake/`.
- Intake did not perform deep JD analysis itself.
- Created:
  - `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-hh-vacancy-134758284-handoff.md`

### Job-Search Agent Handoff Processing

Manual direct `job-search` run processed the HH handoff.

Result:

- No duplicate vacancy artifacts were created.
- Existing durable artifacts were recognized as source of truth:
  - `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-02-uzum-technologies-team-lead-payment-mechanics.md`
  - `personal-projects/personal-brand/workspace/job-intake/analyses/parked/2026-07-02-uzum-technologies-team-lead-payment-mechanics-analysis.md`
  - `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
  - `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`
- Created:
  - `automation/runs/2026-07-02-1746-hh-vacancy-134758284-smoke-test.md`
- Job-search returned a structured `secretaries/handoff-contract.md` user-reply handoff.
- Live HH connector access was degraded: `hh_web_healthcheck` and `hh_web_get_vacancy`
  timed out on `hh.ru`, but the fallback to durable archive was correct.

### Gmail Monitor

Manual `automation/scripts/run-pi-job-search-gmail-monitor.sh` run completed.

Result:

- Pi-local `google_workspace` Gmail read-only search/read succeeded.
- SQLite dedupe was used before message-specific processing.
- Processed one new HH thin digest:
  - `inbox/processed/2026-07-02-hh-product-engineering-thin-digest.md`
- Recorded one LinkedIn duplicate/no-op:
  - `inbox/processed/2026-07-02-linkedin-application-status-updates.md`
- Updated monitor state:
  - `automation/state/hh-gmail-monitor-state.md`
  - `automation/state/linkedin-gmail-monitor-state.md`
- Created run logs:
  - `automation/runs/2026-07-02-1749-pi-job-search-gmail-monitor.md`
  - `automation/runs/2026-07-02-1752-pi-job-search-gmail-monitor.md`
- No user-facing Telegram packet was sent because no actionable full JD was found.

## Model Map

Current OpenClaw agent model settings:

| Agent | Model | Auth |
|---|---|---|
| `default` | `openai/gpt-5.5` | `openai:v.rezin@gmail.com` |
| `po-router` | `openai/gpt-5.5` | `openai:v.rezin@gmail.com` |
| `po-path-validator` | `openai/gpt-5.5` | `openai:v.rezin@gmail.com` |
| `job-search` | `openai/gpt-5.5` | `openai:v.rezin@gmail.com` |
| `intake` | `openai/gpt-5.5` | `openai:v.rezin@gmail.com` |
| `main` | `openai/gpt-5.5` in config | no local auth profile |

Implication: `intake` currently uses the same strong/default model as `job-search`,
although intake mostly performs classification, artifact routing, and concise
reply formatting.

## Gaps

- No automatic live dispatcher yet for:

```text
intake handoff -> job-search agent -> structured handoff -> intake user reply
```

- Current working behavior is:

```text
intake -> durable handoff artifact
operator/manual wrapper -> job-search
job-search -> structured handoff
```

- HH live enrichment is intermittently degraded by page navigation timeout. Existing
durable archives prevent data loss, but fresh HH vacancy fetches need connector
hardening or retry policy.

## Recommendation

- Keep `job-search` on a stronger model for JD analysis, CV selection, and cover
letter/reply reasoning.
- Move `intake` to a cheaper/smaller model after one more Telegram end-to-end
smoke, because its job is mostly routing and output polishing.
- Add a small dispatcher wrapper for job-search handoffs before relying on fully
automatic Telegram job reviews.
