# Pi Job Search Handoff Dispatch - HH Vacancy 134804503

- Run timestamp: 2026-07-04T18:25:21+07:00
- Source agent: job-search
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md`

## Extracted Identifiers

- HH vacancy id: `134804503`
- URL: `https://novosibirsk.hh.ru/vacancy/134804503?utm_source=hh-chatbot&utm_campaign=push_recommend_vacancy_no_image&utm_medium=chatbot_tg`
- Company: `Emphasoft`
- Role: `Руководитель Проектного офиса`

## Exact Search

Exact-id/company search found the current handoff, earlier Emphasoft thin handoff/digest mentions, and prior blocked dispatch logs. No full JD archive or analysis existed before this run.

## Enrichment

`hh_web_get_vacancy` succeeded for vacancy `134804503` and returned the normalized JD.

Key facts:

- Company: Emphasoft
- Role: Руководитель Проектного офиса
- Location / format: Алматы
- Salary: not shown
- Contract: B2B / ИП
- Scope: 20+ custom-development/outstaffing projects, PMO standards, PM team development, resource conflicts, risk/escalation management, key-project ownership

## Artifacts Written

- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-emphasoft-project-office-head.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-emphasoft-project-office-head-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`

## Decision

Verdict: maybe / clarify first.

Reasoning:

- This is a real IT custom-development PMO role, not only a thin HH alert.
- Fit is plausible through Business Unit / Integration and Stability & Governance.
- Salary, Алматы/remote reality, B2B economics and the balance between PMO building and hands-on project firefighting are unresolved.

## Structured Handoff

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: HH vacancy 134804503 is Emphasoft's Project Office Head role for IT custom-development/outstaffing portfolio governance; full JD was archived and analyzed.
verdict: maybe
reasons:
  - Real IT PMO/custom-development portfolio role with Business Unit / Integration and Stability & Governance overlap.
  - Technical background is a plus, which helps bridge engineering leadership into delivery-process authority.
  - Salary, Алматы/remote requirement, B2B economics and hands-on firefighting load are unclear.
cv: personal-projects/personal-brand/workspace/final-cv/Director of Development - Business Unit Technical Leader.pdf
cover_letter: null
next_action: Clarify remote/B2B format, compensation range and PMO mandate before applying.
artifacts:
  - personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-emphasoft-project-office-head.md
  - personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-emphasoft-project-office-head-analysis.md
  - personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-vacancy-134804503-emphasoft-handoff.md
  - automation/runs/2026-07-04-182521-pi-job-search-handoff-dispatch.md
blocked_on:
  - Is Novosibirsk remote B2B acceptable, or is Алматы presence required?
  - What is the compensation range?
  - How much of the role is PMO building versus personal firefighting on key projects?
```
