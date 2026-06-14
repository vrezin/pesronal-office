# LinkedIn Gmail Monitor Run - 2026-06-14 16:02 +07

- Status: processing_complete_commit_pending
- Mode: unattended cron
- Gmail query: `from:linkedin.com after:2026/6/13 -in:trash -in:spam`
- Previous successful scan: 2026-06-14 08:01:30 +07
- Previous last processed Gmail message id: `19ec1d2802672390`
- Previous last processed Gmail internal date: `2026-06-13T16:30:57`

## Messages Reviewed

Seven LinkedIn message ids were returned by the overlap search. Three messages were newer than the saved marker. One of those had already been processed by a prior failed-commit monitor run and remained uncommitted in the worktree; two were processed in this run.

| Gmail id | Timestamp | Subject | Classification | Result |
|---|---:|---|---|---|
| `19ec543614d183c0` | 2026-06-14T08:33:05 | `Senior Director, Data Platform and AI в компании Oyster®` | `new_vacancy` | Processed. LinkedIn MCP enrichment returned a full JD; promoted into job intake and active review task. |
| `19ec4d37face4463` | 2026-06-14T06:30:55 | `FS Technology Consulting - Engineering Lead, Features Team- Director - Dublin в компании EY` | `new_vacancy` | Processed. LinkedIn MCP enrichment returned a full JD; promoted into job intake and active review task. |
| `19ec465a43721708` | 2026-06-14T04:30:55 | `Новые вакансии, похожие на вакансию «Director of Platform Engineering» в компании Overstory` | `new_vacancy` | Already processed by `automation/runs/2026-06-14-1201-linkedin-gmail-monitor.md`; artifacts are still uncommitted because that run could not create a git index lock. |
| `19ec088e45b23621` | 2026-06-13T10:30:55 | `Head of Engineering в компании Vyking` | overlap/new_vacancy | Older than saved marker; already captured previously. |
| `19ec02d1e17a3e66` | 2026-06-13T08:50:42 | `Ваша заявка на вакансию «Head of Engineering» в компании Shaw Daniels Solutions` | overlap/status_update | Older than saved marker; Shaw Daniels rejection already reflected in prior artifacts. |
| `19ec01c84fd1f9a8` | 2026-06-13T08:32:32 | `Head of Engineering в компании Vyking` | overlap/new_vacancy | Older than saved marker; duplicate Vyking digest already captured. |
| `19ebfad6cc4c3f36` | 2026-06-13T06:31:11 | `Head of Engineering в компании Vyking` | overlap/new_vacancy | Older than saved marker; duplicate Vyking digest already captured. |

## Artifact Updates

Created in this run:

- `inbox/processed/2026-06-14-linkedin-oyster-ey-vacancy-digests.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-14-oyster-senior-director-data-platform-ai.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-14-oyster-senior-director-data-platform-ai-analysis.md`
- `tasks/active/2026-06-14-review-oyster-senior-director-data-platform-ai.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-14-ey-engineering-lead-director-dublin.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-14-ey-engineering-lead-director-dublin-analysis.md`
- `tasks/active/2026-06-14-review-ey-engineering-lead-director-dublin.md`

Updated in this run:

- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`

Existing uncommitted LinkedIn monitor artifacts from the 12:01 failed-commit run were left in place and should be committed together with this run if git becomes available:

- `inbox/processed/2026-06-14-linkedin-overstory-similar-jobs-digest.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-14-totalmobile-platform-software-engineering-director.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-14-totalmobile-platform-software-engineering-director-analysis.md`
- `tasks/active/2026-06-14-review-totalmobile-platform-software-engineering-director.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-14-unisys-senior-director-ai-platforms.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-14-unisys-senior-director-ai-platforms-analysis.md`
- `tasks/active/2026-06-14-review-unisys-senior-director-ai-platforms.md`

## Ranking

- Oyster / Senior Director, Data Platform and AI: `interesting`; high fit with AI platform, organizational AI adoption, knowledge architecture, LLM orchestration, and remote-first work.
- EY / Engineering Lead Director Dublin: `maybe`; credible engineering delivery leadership, but likely relocation/hybrid consulting and weaker AI-product alignment.
- Overstory similar-jobs digest: already handled by the 12:01 run; Totalmobile and Unisys were promoted then.

## Gmail Cleanup

No Gmail labels, stars, importance markers, read/unread state, or archive state were changed.

Recommended Gmail action: optional manual archive/label of processed LinkedIn digests `19ec543614d183c0`, `19ec4d37face4463`, and `19ec465a43721708`; no unattended Gmail mutation was performed.

## LinkedIn MCP

The registered `mcp__linkedin` server was available and returned full job details for:

- Oyster job id `4424899985`
- EY job id `4385040545`

## Commit / State

Commit has not yet been attempted at the time this log was first written.

The successful scan marker must be advanced to Gmail id `19ec543614d183c0` / timestamp `2026-06-14T08:33:05` only after the repository commit succeeds.
