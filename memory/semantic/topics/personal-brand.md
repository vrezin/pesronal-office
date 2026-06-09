# Personal Brand

## Source Of Truth

- `personal-projects/personal-brand/`
- `personal-projects/personal-brand/workspace/OPERATING_MODEL.md`
- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`
- `personal-projects/personal-brand/workspace/job-intake/`
- `personal-projects/personal-brand/workspace/final-cv/`
- `personal-projects/personal-brand/workspace/resume-targets/master-profile.md`
- `finance/personal-budget/career-relocation-baseline.md`
- `personal-projects/ai-automation-portfolio/`

## Stable Rules

- Personal brand and career work belong in Personal Office, not AI Studio.
- Job search, HH/vacancy intake, CV decisions, cover letters, and career positioning belong in `personal-projects/personal-brand/`, not `work/employment-search/`.
- `OPERATING_MODEL.md` is the dispatcher for source-of-truth order and the current CV portfolio.
- `job-intake/INDEX.md` is the reviewed-vacancy memory: check it before analyzing similar roles.
- `job-intake/COMPANY_NOTES.md` is company/bucket memory derived from prior intakes.
- Recurring normalization and indexing work is proceduralized as skills: `personal-brand-workspace-normalization`, `vacancy-history-indexing`, `job-intake-company-notes`, and `routing-sync`.
- Vacancy analysis must include relocation, family lifestyle impact, market salary, and target income through `career-offer-life-economics`.
- HH.ru Gmail monitoring is a recurring workflow: scan HH mail, classify status updates / invitations / new vacancies, update tasks, update analyses/indexes, star important invitations when possible, and save run logs in `automation/runs/`.
- Public website files may live in a dedicated site repo/folder, while planning and operating context stays here.
