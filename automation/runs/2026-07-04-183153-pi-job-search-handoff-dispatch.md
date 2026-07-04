# Pi Job Search Handoff Dispatch - HH Vacancy 134804503 Duplicate

- Run timestamp: 2026-07-04T18:31:53+07:00
- Source agent: job-search
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md`

## Extracted Identifiers

- HH vacancy id: `134804503`
- URL: `https://novosibirsk.hh.ru/vacancy/134804503?utm_source=hh-chatbot&utm_campaign=push_recommend_vacancy_no_image&utm_medium=chatbot_tg`
- Company: `Emphasoft`
- Role: `Руководитель Проектного офиса`

## Exact Search Result

Exact-id search found that this vacancy was already processed in the canonical job-intake workspace.

Existing durable artifacts:

- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-emphasoft-project-office-head.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-emphasoft-project-office-head-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`
- `automation/runs/2026-07-04-182521-pi-job-search-handoff-dispatch.md`

No new JD archive, analysis, CV, or cover-letter artifact was created in this duplicate dispatch.

## Decision

Verdict: no-op.

Use the existing analysis result: `maybe / clarify first`.

Key reasons preserved from the existing analysis:

- The role is a real IT custom-development PMO/portfolio-governance role.
- It has plausible fit with Business Unit / Integration and Stability & Governance positioning.
- Salary, Алматы/remote requirement, B2B economics, and PMO-building versus hands-on firefighting load remain unresolved.

## Structured Handoff

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: HH vacancy 134804503 for Emphasoft was already archived and analyzed; no duplicate artifacts were created.
verdict: no-op
reasons:
  - Exact HH id 134804503 already has a durable JD archive and analysis.
  - Existing decision is maybe / clarify first for an IT custom-development PMO role.
  - Remaining blockers are salary, Алматы or remote B2B format, and PMO-building versus hands-on firefighting scope.
cv: personal-projects/personal-brand/workspace/final-cv/Director of Development - Business Unit Technical Leader.pdf
cover_letter: null
next_action: Use the existing analysis and clarify remote/B2B format, compensation range and PMO mandate before applying.
artifacts:
  - personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-emphasoft-project-office-head.md
  - personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-emphasoft-project-office-head-analysis.md
  - personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md
  - automation/runs/2026-07-04-182521-pi-job-search-handoff-dispatch.md
  - automation/runs/2026-07-04-183153-pi-job-search-handoff-dispatch.md
blocked_on:
  - Is Novosibirsk remote B2B acceptable, or is Алматы presence required?
  - What is the compensation range?
  - How much of the role is PMO building versus personal firefighting on key projects?
```
