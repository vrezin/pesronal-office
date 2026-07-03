# Pi Job Search Gmail Monitor Run

- Timestamp: 2026-07-02 17:52:59 +0700
- Trigger: scheduled task, Pi Job Search Gmail Monitor
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram target: `113174019` compatibility only
- Telegram account: `job-search-telegram` compatibility only
- Gmail account: `v.rezin@gmail.com`
- Gmail mutation: none; read-only search/read
- Git mutation: none
- User-facing Telegram mutation: none; handoff written internally only

## Runtime

- Ran `python3 tools/job-search-runtime/job_search_runtime.py init`.
- Ran `python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state`.
- Used the wrapper-held SQLite lock `pi-job-search-gmail-monitor` owner `2026-07-02-1749-3799048`.
- Checked every seen Gmail id with `message-status` before message-specific processing.
- SQLite was the operational dedupe source.

Runtime status after marking:

```text
Processed messages:
- hh needs_human: 1
- hh noise: 4
- hh processed: 2
- hh seeded_from_markdown_state: 1
- linkedin duplicate: 1
- linkedin noise: 7
- linkedin processed: 8
- linkedin seeded_from_markdown_state: 1
```

## Gmail Queries

- HH primary: `from:(hh.ru OR notification@hh.ru OR no-reply@hh.ru OR noreply@hh.ru) newer_than:7d`
- HH fallback: `(hh.ru OR HeadHunter) newer_than:7d`
- LinkedIn: `from:linkedin.com newer_than:7d`

## Message IDs Seen

### HH

- `19f222a760eeb4d3` / thread `19f222a760eeb4d3`
- `19f191abaf5759ab` / thread `19f191abaf5759ab`
- `19f12cd62b56bebe` / thread `19f12cd62b56bebe`
- `19f0d7d179bacbb7` / thread `19f0d7d179bacbb7`

The HH fallback query returned the same four ids.

### LinkedIn

- `19f2261db60003a6` / thread `19f2261db60003a6`
- `19f21faa18a56d48` / thread `19f21faa18a56d48`
- `19f21f3f0697f7ec` / thread `19f21f3f0697f7ec`
- `19f21e3d77f5ca26` / thread `19f21e3d77f5ca26`
- `19f21ba7638665c1` / thread `19f21ba7638665c1`

## Duplicate / No-op IDs

Already present in SQLite before this run:

- HH: `19f191abaf5759ab`, `19f12cd62b56bebe`, `19f0d7d179bacbb7`
- LinkedIn: `19f21faa18a56d48`, `19f21f3f0697f7ec`, `19f21e3d77f5ca26`, `19f21ba7638665c1`

Marked during this run as content-duplicate/no-op:

- LinkedIn: `19f2261db60003a6` - Dr.Head `Директор по ИТ` alert for job id `4434956568`, already captured from application confirmation in `inbox/processed/2026-07-02-linkedin-application-status-updates.md`.

## Processed Items

### HH Raw Intake

- Gmail message id: `19f222a760eeb4d3`
- Subject: `Подходящие вакансии для резюме: «CTO / Co-founder CTO / Head of Product Engineering»`
- Sender: `hh.ru <noreply@hh.ru>`
- Date: `Thu, 2 Jul 2026 12:30:35 +0300 (MSK)`
- Classification: `new_vacancy`
- Status: `processed`
- Artifact: `inbox/processed/2026-07-02-hh-product-engineering-thin-digest.md`

The message was an HH similar-vacancies digest with thin cards only. Captured cards: Offer Now `Lead Software Engineer`, Словософт `Технический директор (СТО)`, Таймвэб.Клауд `Technical product owner`, Кривошеев Александр Викторович `COO / Операционный директор`, ГК Орбита `Senior AI / R&D Engineer`, and UZUM TECHNOLOGIES `Team Lead команды разработки (Payment Mechanics)`.

No full JD analysis, CV selection, cover letter, `job-intake/INDEX.md`, or `COMPANY_NOTES.md` update was made because the email did not include responsibilities, requirements, stable posting ids, or enough JD text.

### LinkedIn Duplicate

- Gmail message id: `19f2261db60003a6`
- Subject: `Директор по ИТ в компании Dr.Head`
- Classification: `new_vacancy`
- Status: `duplicate`
- Artifact: `inbox/processed/2026-07-02-linkedin-application-status-updates.md`

This alert repeated the same Dr.Head LinkedIn job id `4434956568` already recorded from the application confirmation. The status note was updated; no new raw intake was created.

## SQLite Commands

```bash
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source hh --gmail-message-id 19f222a760eeb4d3 --classification new_vacancy --status processed --artifact-path inbox/processed/2026-07-02-hh-product-engineering-thin-digest.md --notes "Thin HH similar-vacancies digest for Product Engineering resume; raw intake only, no full JD or handoff beyond no-op."
python3 tools/job-search-runtime/job_search_runtime.py mark-message --source linkedin --gmail-message-id 19f2261db60003a6 --classification new_vacancy --status duplicate --artifact-path inbox/processed/2026-07-02-linkedin-application-status-updates.md --notes "Duplicate LinkedIn Dr.Head IT Director alert for job id 4434956568; application confirmation already recorded."
```

## User Reply Handoff

No actionable vacancy packet was produced. The only handoff is the low-priority no-op handoff embedded in `inbox/processed/2026-07-02-hh-product-engineering-thin-digest.md`:

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: low
user_intent: vacancy_review
summary: HH sent a thin product-engineering similar-vacancies digest; captured raw cards only.
verdict: no-op
reasons:
  - Email contains only thin job cards, not full JDs.
  - UZUM card is already analyzed separately.
  - No CV or cover letter can be selected safely from this digest.
cv: null
cover_letter: null
next_action: ignore unless the operator asks to fetch one full HH posting
artifacts:
  - inbox/processed/2026-07-02-hh-product-engineering-thin-digest.md
blocked_on: []
```

## Telegram

- Direct Telegram send: none.
- Intended user-facing packets: none.
- Reason: job-search monitor is not the Telegram voice, and no actionable vacancy decision packet was produced.

## Blocked Items

- None. Pi-local `google_workspace` Gmail search/read succeeded.

## Artifacts

- Run log: `automation/runs/2026-07-02-1752-pi-job-search-gmail-monitor.md`
- HH raw intake: `inbox/processed/2026-07-02-hh-product-engineering-thin-digest.md`
- LinkedIn status note updated: `inbox/processed/2026-07-02-linkedin-application-status-updates.md`

## Legacy State

- Updated `automation/state/hh-gmail-monitor-state.md` after successful scan.
- Updated `automation/state/linkedin-gmail-monitor-state.md` after successful scan.
