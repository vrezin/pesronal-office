# Review HH Digest CTO Product Engineering Vacancies

- Created: 2026-06-12
- Status: done
- Source: HH email digest for `CTO / Co-founder CTO / Head of Product Engineering`
- Gmail message id: `19ebaf3c69f4503f`
- Processed note: `inbox/processed/2026-06-12-hh-vacancy-digest-thin-links.md`

## Goal

Review the HH digest vacancies that look potentially relevant and turn only real matches into normal job-intake artifacts.

## Current Constraint

The HeadHunter MCP server starts and `hh_get_dictionaries` works, but vacancy search/detail calls currently return `403 Forbidden`:

- `hh_get_vacancy(134062447)` -> `403`
- `hh_get_vacancy(134086561)` -> `403`
- `hh_search_vacancies("Руководитель проектов Р7")` -> `403`
- `hh_search_vacancies("Директор проекта по внедрению ИИ Мираторг")` -> `403`

Until OAuth/app credentials or another HH access path is available, full JD text must be retrieved manually from HH UI or pasted by the user.

Full JD text for the digest was pasted by the user on 2026-06-12 and routed into archives/analyses.

## Vacancy Queue

| Priority | Vacancy ID | Company | Role | First-pass action |
|---|---:|---|---|---|
| High | 134077560 | Технологии Будущего | Founding Engineer (AI HR Tech) | Retrieve full JD; likely AI Transformation + Startup/Product Engineering. |
| Medium-high | 133954979 | СБЕР | Разработчик AI агентов | Retrieve full JD; check if this is lead/architect work or a downleveled developer role. |
| Medium | 134016278 | Костромской ювелирный завод Каратов | Директор по информационным технологиям (CIO) | Retrieve full JD; check scope, compensation, onsite, and transformation authority. |
| Medium-low | 134113881 | Топассистент | Старший менеджер проекта (Senior Project Manager) | Quick review because salary is visible from 4500 EUR/month; likely below target unless scope is serious. |
| Low | 134062447 | Р7 | Руководитель проектов | Review only if easy; email title is too generic. |
| Done / waiting | 134086561 | Мираторг | Директор проекта по внедрению ИИ | Already reviewed and applied; keep waiting for employer response. |

## Reviewed Outcome

- `134077560` - high priority response task created: `tasks/active/2026-06-12-respond-future-technologies-founding-engineer-ai-hr-tech.md`.
- `134113881` - medium-high priority response task created: `tasks/active/2026-06-12-respond-topassistant-senior-project-manager-ai-voice.md`.
- `133954979` - medium-high decision task created: `tasks/active/2026-06-12-decide-sber-ai-agents-developer.md`.
- `134016278` - analyzed as medium-low because Kostroma onsite and hidden comp are the main filters.
- `134062447` - analyzed as low priority / likely downlevel.
- `134086561` - duplicate of already applied Мираторг role; remains waiting for reply.

## Next Step

Digest review is complete. Follow-up actions live in separate tasks for Future Technologies, Topassistant, Sber, and existing waiting items.
