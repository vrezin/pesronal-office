# Pi Job Search Handoff Dispatch

- Started at: 2026-07-02T18:13:28+07:00
- Completed at: 2026-07-02T18:13:28+07:00
- Trigger: intake handoff dispatcher
- Agent: `job-search`
- Handoff path: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-hh-vacancy-134758284-handoff.md`
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Telegram mutation: none
- Git mutation: none
- Monitor state mutation: none
- Status: success / already processed

## Summary

Processed the intake handoff for HH vacancy `134758284`.

The vacancy was already durably processed in the canonical Personal Office repo. No duplicate JD archive, analysis, index row, company note, CV, or cover-letter artifact was created.

## Live Source Check

Attempted a fresh HH connector fetch with `hh_web_get_vacancy` for vacancy `134758284`.

Result: `EXTRACTION_FAILED`; `Page.goto` timed out while opening `https://hh.ru/vacancy/134758284`.

Because durable artifacts already exist, the existing JD archive and analysis remain the evidence source per handoff rules.

## Durable Evidence

- JD archive: `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-02-uzum-technologies-team-lead-payment-mechanics.md`
- Analysis: `personal-projects/personal-brand/workspace/job-intake/analyses/parked/2026-07-02-uzum-technologies-team-lead-payment-mechanics-analysis.md`
- Intake handoff: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-hh-vacancy-134758284-handoff.md`
- Index row present in `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- Company note present in `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`

## Vacancy Snapshot From Durable Artifacts

- Vacancy: UZUM TECHNOLOGIES. IT, `Team Lead команды разработки (Payment Mechanics)`
- HH id: `134758284`
- Location/format: Moscow / remote from anywhere
- Salary: not specified
- Experience: more than 6 years
- Published by HH: 2026-07-01
- Team: 7 people: 2 system analysts, 3 Java backend developers, 2 QA engineers
- Best CV: `personal-projects/personal-brand/workspace/final-cv/CTO - Head of Engineering - Stability and Governance.pdf`
- Decision: `maybe / selective`
- Effort class: `B/C-class`

## Handoff

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: "HH vacancy 134758284 was already processed as UZUM TECHNOLOGIES. IT Team Lead Payment Mechanics; no duplicate artifacts created. Live HH refetch timed out, so existing durable JD archive and analysis remain the evidence source."
verdict: maybe
reasons:
  - "Real fintech engineering-management role with good Stability & Governance overlap: SDLC, incidents, CI/CD, technical debt, architecture decisions, and team health."
  - "Likely downleveled for the current target profile: Team Lead for a 7-person team, with hidden salary and possible Java/payments hard filters."
  - "Remote-from-anywhere plus Uzbekistan IT Park/legal setup may be practical, but compensation, legal setup, and hands-on backend depth must be clarified first."
cv: "personal-projects/personal-brand/workspace/final-cv/CTO - Head of Engineering - Stability and Governance.pdf"
cover_letter: null
next_action: "Clarify compensation band, remote/legal setup, and hands-on Java/payments depth before applying."
artifacts:
  - "personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-02-uzum-technologies-team-lead-payment-mechanics.md"
  - "personal-projects/personal-brand/workspace/job-intake/analyses/parked/2026-07-02-uzum-technologies-team-lead-payment-mechanics-analysis.md"
  - "personal-projects/personal-brand/workspace/job-intake/processed/2026-07-02-hh-vacancy-134758284-handoff.md"
  - "automation/runs/2026-07-02-1813-pi-job-search-handoff-dispatch.md"
blocked_on:
  - "Live HH refetch timed out; use durable saved JD unless a fresh source check is explicitly required."
```
