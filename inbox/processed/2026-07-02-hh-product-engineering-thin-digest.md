# HH Product Engineering Thin Digest

- Source: Gmail / HH similar-vacancies digest
- Gmail message id: `19f222a760eeb4d3`
- Gmail thread id: `19f222a760eeb4d3`
- Received: 2026-07-02 12:30:35 MSK
- Subject: `Подходящие вакансии для резюме: «CTO / Co-founder CTO / Head of Product Engineering»`
- Classification: `new_vacancy`
- Routing result: raw intake only; no full JD analysis

## Summary

HH sent a similar-vacancies digest for the `CTO / Co-founder CTO / Head of Product Engineering` resume. The email exposes only job-card level data: title, company when present, and one salary card. It does not include full descriptions, requirements, remote/legal setup, application status, or enough evidence to select a CV or prepare a user-facing decision packet.

## Job Cards

| Role | Company | Compensation | Notes |
|---|---|---|---|
| Lead Software Engineer | Offer Now | up to `7000 EUR/month` | Thin card only. |
| Технический директор (СТО) | Словософт | not shown | Thin card only. |
| Technical product owner | Таймвэб.Клауд | not shown | Thin card only. |
| COO / Операционный директор | Кривошеев Александр Викторович | `200000-350000 RUB/month` | Thin card only; likely not a core technology-leadership fit without more context. |
| Senior AI / R&D Engineer | ГК Орбита | not shown | Thin card only. |
| Team Lead команды разработки (Payment Mechanics) | UZUM TECHNOLOGIES | not shown | Already analyzed separately as `job-intake/analyses/parked/2026-07-02-uzum-technologies-team-lead-payment-mechanics-analysis.md`. |

## Triage

- No actionable vacancy packet: no full JD text, no location/remote details, no requirements, no application links captured as stable ids in the email body.
- `UZUM TECHNOLOGIES` is already represented in the job-intake index and should not be reprocessed from this thin digest.
- `Offer Now`, `Словософт`, `Таймвэб.Клауд`, and `ГК Орбита` may be worth reopening only if a full HH posting is fetched later.

## Handoff

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
