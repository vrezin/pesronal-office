# LinkedIn Gmail Monitor Run - 2026-06-14 12:01 +07

- Status: commit_failed
- Mode: unattended cron
- Gmail query: `from:linkedin.com after:2026/6/13 -in:spam -in:trash`
- Previous successful scan: 2026-06-14 08:01:30 +07
- Previous last processed Gmail message id: `19ec1d2802672390`
- Previous last processed Gmail internal date: `2026-06-13T16:30:57`

## Messages Reviewed

Six LinkedIn message ids were returned by the overlap search. One message was newer than the saved marker and required artifact updates.

| Gmail id | Timestamp | Subject | Classification | Result |
|---|---:|---|---|---|
| `19ec465a43721708` | 2026-06-14T04:30:55 | `Новые вакансии, похожие на вакансию «Director of Platform Engineering» в компании Overstory` | `new_vacancy` | Processed. Gmail body was a similar-jobs digest. LinkedIn MCP enrichment promoted Totalmobile and Unisys into full job-intake artifacts; remaining cards were kept in the processed trace. |
| `19ec1d2802672390` | 2026-06-13T16:30:57 | `Я хочу установить контакт` | overlap/invitation | Equal to the saved state marker; already processed in a previous successful run. |
| `19ec088e45b23621` | 2026-06-13T10:30:55 | `Head of Engineering в компании Vyking` | overlap/new_vacancy | Older than the saved state marker; already captured in `inbox/processed/2026-06-13-linkedin-vyking-digest-thin-links.md`. |
| `19ec02d1e17a3e66` | 2026-06-13T08:50:42 | `Ваша заявка на вакансию «Head of Engineering» в компании Shaw Daniels Solutions` | overlap/status_update | Older than the saved state marker; Shaw Daniels rejection already reflected in prior artifacts. |
| `19ec01c84fd1f9a8` | 2026-06-13T08:32:32 | `Head of Engineering в компании Vyking` | overlap/new_vacancy | Older than the saved state marker; duplicate Vyking digest already captured. |
| `19ebfad6cc4c3f36` | 2026-06-13T06:31:11 | `Head of Engineering в компании Vyking` | overlap/new_vacancy | Older than the saved state marker; duplicate Vyking digest already captured. |

## Artifact Updates

- Created `inbox/processed/2026-06-14-linkedin-overstory-similar-jobs-digest.md`.
- Created `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-14-totalmobile-platform-software-engineering-director.md`.
- Created `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-14-totalmobile-platform-software-engineering-director-analysis.md`.
- Created `tasks/active/2026-06-14-review-totalmobile-platform-software-engineering-director.md`.
- Created `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-14-unisys-senior-director-ai-platforms.md`.
- Created `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-14-unisys-senior-director-ai-platforms-analysis.md`.
- Created `tasks/active/2026-06-14-review-unisys-senior-director-ai-platforms.md`.
- Updated `personal-projects/personal-brand/workspace/job-intake/INDEX.md`.
- Updated `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`.
- Did not update `automation/state/linkedin-gmail-monitor-state.md` because the required git commit failed.

## Gmail Cleanup

No Gmail labels, stars, importance markers, read/unread state, or archive state were changed.

Recommended Gmail action: optional manual archive/label of processed LinkedIn digest `19ec465a43721708`; no unattended Gmail mutation was performed.

## LinkedIn MCP

The registered `mcp__linkedin` server was available and returned full job details for:

- Totalmobile job id `4424231462`
- Unisys job id `4418182935`

The remaining digest job ids were recorded in the processed trace for later focused review.

## Commit / State

Commit failed in this cron sandbox:

```text
fatal: Unable to create '/home/adre/personal-office/.git/index.lock': Read-only file system
```

Repository artifact changes were left in place. The successful scan marker was left unchanged, as required when commit fails.
