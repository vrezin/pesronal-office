# HH Gmail Monitor Run

- Run started: 2026-06-14 00:01:25 +07
- Run completed: 2026-06-14 00:01:25 +07
- Previous successful scan marker: 2026-06-13 16:02:00 +07
- Previous last processed Gmail message id: `19ebaf3c69f4503f`
- Previous last processed Gmail internal date: 2026-06-12T08:29:57
- Status: success

## Gmail Search

Connector access was available.

Queries:

```text
(from:noreply@hh.ru OR from:hh.ru OR from:headhunter OR subject:(hh OR HeadHunter OR hh.ru OR Хедхантер) OR "hh.ru" OR "HeadHunter" OR "Хедхантер") after:2026/6/12 -in:spam -in:trash
(from:noreply@hh.ru OR from:hh.ru OR from:headhunter OR subject:(hh OR HeadHunter OR hh.ru OR Хедхантер) OR "hh.ru" OR "HeadHunter" OR "Хедхантер") after:2026/6/11 -in:spam -in:trash
```

Result: 1 unique message id.

Overlap policy: used searches from 2026-06-12 and 2026-06-11 against the previous marker to avoid missing delayed HH messages.

## Classification

| Gmail message id | Timestamp | Subject | Classification | Action |
|---|---|---|---|---|
| `19ec0d3d9c40220d` | 2026-06-13T11:52:49 | `Подходящие вакансии для резюме: «Директор по разработке / Технический лидер бизнес-юнита»` | new_vacancy / thin digest | Already represented by `inbox/processed/2026-06-13-hh-business-unit-digest-thin-links.md` and `tasks/active/2026-06-13-review-hh-business-unit-digest-vacancies.md`; no duplicate artifact created. |

Counts:

- status_update: 0
- invitation: 0
- new_vacancy: 1
- noise: 0

## Artifact Updates

Created:

- `automation/runs/2026-06-14-0001-hh-gmail-monitor.md`

Updated:

- `automation/state/hh-gmail-monitor-state.md`

No `job-intake/analyses/`, `job-intake/INDEX.md`, or `job-intake/COMPANY_NOTES.md` files were updated because the only new-vacancy message was a thin digest and the existing processed trace/task already captures the review queue.

## Gmail Actions

No Gmail labels, stars, importance markers, or messages were mutated during the unattended run.

Recommended manual Gmail action after the review task is resolved:

- archive or delete message `19ec0d3d9c40220d` once represented by full JD artifacts or explicitly skipped.

## Commit And State Update

The Gmail scan and repo-local artifact processing completed successfully. `automation/state/hh-gmail-monitor-state.md` was advanced after processing the message batch.
