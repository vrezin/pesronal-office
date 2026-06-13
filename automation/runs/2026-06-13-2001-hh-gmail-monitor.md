# HH Gmail Monitor Run

- Run started: 2026-06-13 20:01:56 +07
- Run completed: 2026-06-13 20:01:56 +07
- Previous successful scan marker: 2026-06-13 16:02:00 +07
- Previous last processed Gmail message id: `19ebaf3c69f4503f`
- Previous last processed Gmail internal date: 2026-06-12T08:29:57
- Status: blocked after scan; repository commit failed

## Gmail Search

Connector access was available.

Query:

```text
(from:noreply@hh.ru OR from:hh.ru OR from:headhunter OR subject:(hh OR HeadHunter OR hh.ru OR Хедхантер)) after:2026/6/11 -in:spam -in:trash
```

Result: 2 message ids.

Overlap policy: used `after:2026/6/11` against the previous marker `2026-06-12T08:29:57` to avoid missing delayed HH messages.

## Classification

| Gmail message id | Timestamp | Subject | Classification | Action |
|---|---|---|---|---|
| `19ec0d3d9dda3671` | 2026-06-13T11:52:49 | `Вчера ваше резюме привлекло внимание` | noise | Resume-view notification only; no employer decision, invitation, or full vacancy JD. No artifact update beyond this run log. |
| `19ec0d3d9c40220d` | 2026-06-13T11:52:49 | `Подходящие вакансии для резюме: «Директор по разработке / Технический лидер бизнес-юнита»` | new_vacancy / thin digest | Created processed digest trace and active review task. No full job-intake analysis was created because the email lacks full JD text. |

Counts:

- status_update: 0
- invitation: 0
- new_vacancy: 1
- noise: 1

## Artifact Updates

Created:

- `inbox/processed/2026-06-13-hh-business-unit-digest-thin-links.md`
- `tasks/active/2026-06-13-review-hh-business-unit-digest-vacancies.md`

Changed before commit attempt:

- `automation/state/hh-gmail-monitor-state.md`
- `automation/runs/2026-06-13-2001-hh-gmail-monitor.md`

No `job-intake/analyses/`, `job-intake/INDEX.md`, or `job-intake/COMPANY_NOTES.md` files were updated because the only new-vacancy message was a thin digest and did not contain full JD text.

## Gmail Actions

No Gmail labels, stars, importance markers, or messages were mutated during the unattended run.

Recommended manual Gmail action after the review task is resolved:

- archive or delete message `19ec0d3d9c40220d` once represented by full JD artifacts or explicitly skipped;
- optionally archive the resume-view notification `19ec0d3d9dda3671` as noise.

## Commit And State Update

The Gmail scan and repo-local artifact processing completed, but the required repository commit failed:

```text
fatal: Unable to create '/home/adre/personal-office/.git/index.lock': Read-only file system
```

Per the unattended monitor rule, `automation/state/hh-gmail-monitor-state.md` was restored to the previous successful marker. Last successful scan remains `2026-06-13 16:02:00 +07`; last processed Gmail message id remains `19ebaf3c69f4503f`; last processed Gmail internal date remains `2026-06-12T08:29:57`.
