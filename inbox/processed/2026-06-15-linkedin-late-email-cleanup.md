# LinkedIn Late Email Cleanup

- Date processed: 2026-06-15
- Source: Gmail `from:linkedin.com -in:spam -in:trash`
- Purpose: confirm current LinkedIn emails were represented in job-search artifacts before Gmail cleanup.

## Processed Messages

| Gmail message id | Timestamp | Subject | Classification | Action |
|---|---|---|---|---|
| `19ecad59f8a5fd94` | 2026-06-15T10:30:56 | `Senior Director, Global Head of Solution Development & AI Platforms в компании Unisys` | duplicate / low-priority digest | Unisys job id `4418182935` was already analyzed and parked. Remaining cards were location/management-heavy market noise for the current search focus. |
| `19ecabfe6233215a` | 2026-06-15T10:07:13 | `Ваша заявка на вакансию «Head of Machine Learning» в компании KDR Talent Solutions` | rejection | Updated KDR job-intake status to `rejected / closed`. |
| `19ec543614d183c0` | 2026-06-14T08:33:05 | `Senior Director, Data Platform and AI в компании Oyster` | already processed | Oyster application is recorded and waiting for employer response. |
| `19ec4d37face4463` | 2026-06-14T06:30:55 | `FS Technology Consulting - Engineering Lead, Features Team- Director - Dublin в компании EY` | already processed / parked | EY was analyzed and parked because Dublin hybrid consulting is not a target. |
| `19ec465a43721708` | 2026-06-14T04:30:55 | `Новые вакансии, похожие на вакансию «Director of Platform Engineering» в компании Overstory` | already processed | Prior monitor promoted Totalmobile and Unisys into job-intake; both are now parked. |

## Cleanup Decision

All listed messages have repository traces and do not require active inbox handling. They can be moved to Gmail Trash.
