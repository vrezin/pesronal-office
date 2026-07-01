# Scheduled Task: Pi Job Search Gmail Monitor

You are running as the OpenClaw `job-search` agent for the Pi-primary Personal Office repo.

The wrapper passes the canonical repo root at the top of the message. Use that path as `<repo-root>` for all file reads, writes, and shell commands. Do not assume the agent process current working directory is the repo; OpenClaw may start inside its own workspace.

Use the repo-local skills `automation-monitoring` and `personal-brand-career`.

This is an unattended run. Do not request interactive approval. If a tool, Gmail operation, MCP server, or repository write is unavailable, write a blocked run log and do not advance state.

## Objective

Scan Pi-local Gmail through the OpenClaw MCP server `google_workspace` for HH.ru / HeadHunter and LinkedIn job-search messages, dedupe through SQLite, update Personal Office job-search artifacts, and produce Telegram decision packets for actionable items when Telegram is configured.

## Runtime Contract

Use the SQLite runtime before touching any message-specific artifact:

```bash
python3 tools/job-search-runtime/job_search_runtime.py init
python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state
python3 tools/job-search-runtime/job_search_runtime.py message-status --source hh --gmail-message-id <GMAIL_ID>
python3 tools/job-search-runtime/job_search_runtime.py message-status --source linkedin --gmail-message-id <GMAIL_ID>
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source <hh|linkedin> --gmail-message-id <GMAIL_ID> --classification <classification> --status <processed|duplicate|noise|blocked|needs_human> --artifact-path <path> --notes <short note>
```

Rules:

- Do not process a Gmail message id until `message-status` says `"processed": false`.
- If `message-status` says `"processed": true`, treat the message as duplicate/no-op and include it in the run log only.
- After successfully routing a message, call `mark-message`.
- If a message cannot be routed safely, call `mark-message` with `status=needs_human` or `status=blocked` only after writing a clarification/blocking artifact.
- SQLite is the operational dedupe source. Markdown state files are compatibility snapshots.

## Gmail Scope

Use only Pi-local `google_workspace` Gmail tools.

Search with a small overlap window. Prefer recent messages first. Suggested queries:

- HH: `from:(hh.ru OR notification@hh.ru OR no-reply@hh.ru OR noreply@hh.ru) newer_than:7d`
- HeadHunter fallback: `(hh.ru OR HeadHunter) newer_than:7d`
- LinkedIn: `from:linkedin.com newer_than:7d`

Keep the first scheduled slice conservative:

- cap each source at a small batch, around 5 messages;
- read headers/snippets first;
- read bodies only for messages that may be `status_update`, `invitation`, or `new_vacancy`;
- do not mutate Gmail labels, stars, importance, archive state, or read/unread state.

## Classification

Classify each relevant message as:

- `status_update`;
- `invitation`;
- `new_vacancy`;
- `noise`.

## Routing

For `status_update`:

- update linked `tasks/active/` or `tasks/waiting/` when a known vacancy status changed;
- update the relevant `job-intake/analyses/*.md` status section if matched;
- update `job-intake/INDEX.md` if decision/status/next action changed.

For `invitation`:

- create or update a high-priority task;
- update matching analysis/index when the vacancy is known;
- if not matched, create `inbox/processed/needs-clarification-YYYY-MM-DD-hh-gmail.md` or `inbox/processed/needs-clarification-YYYY-MM-DD-linkedin.md`.

For `new_vacancy`:

- if the message contains enough JD text, archive and analyze it using `personal-brand-career`;
- select the current best CV from `personal-projects/personal-brand/workspace/OPERATING_MODEL.md`;
- include relocation/lifestyle/compensation notes at the level supported by the source;
- update `job-intake/INDEX.md` and `job-intake/COMPANY_NOTES.md`;
- if only a thin digest/link exists, create a raw intake or clarification note instead of inventing a JD.
- for actionable roles, prepare the Telegram output packet below.

For `noise`:

- record it in SQLite as `status=noise`;
- mention the count in the run log;
- do not create job-intake artifacts.

## Telegram Outbound

The wrapper passes `Telegram target` and `Telegram account` at the top of the message.

If `Telegram target` is not `unset` and OpenClaw has a configured Telegram channel, send a concise decision packet with:

```bash
openclaw message send --channel telegram --target <target> --message <packet>
```

Add `--account <account>` when `Telegram account` is not `default`.

For actionable vacancy output, use:

```text
Found: <company> - <role>
Verdict: send / maybe / skip
Why: <1-3 bullets>
CV: <selected CV path or "не готовить">
Cover letter: <draft path or "не готовить">
Next action: <send now / ask question / wait / ignore>
Artifacts: <paths>
```

If Telegram is not configured or send fails, do not block artifact writes. Write the intended Telegram packet and the send failure into the run log.

## Run Log And State

Always write a run log:

`automation/runs/YYYY-MM-DD-HHMM-pi-job-search-gmail-monitor.md`

The run log must include:

- timestamp and trigger;
- Gmail queries used;
- message ids seen;
- duplicate/no-op ids;
- processed ids and resulting artifact paths;
- Telegram packets sent or intended;
- blocked items and why;
- SQLite commands or summarized runtime status;
- whether legacy state files were updated.

Update legacy state files only after a successful scan:

- `automation/state/hh-gmail-monitor-state.md`
- `automation/state/linkedin-gmail-monitor-state.md`

Do not run Git commit/push from this monitor. Git sync is an outer operator/scheduled phase.

## If Gmail Or OpenClaw MCP Is Unavailable

Do not fake the scan.

Write a blocked run log, leave legacy state unchanged, and do not mark unseen messages as processed.
