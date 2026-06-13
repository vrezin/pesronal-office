# HH Vacancy Digest - Thin Links

- Date: 2026-06-12
- Source: HH digest email for `CTO / Co-founder CTO / Head of Product Engineering`
- Gmail message id: `19ebaf3c69f4503f`
- Gmail timestamp: `2026-06-12T08:29:57+03:00`

## What Arrived

The message was a thin vacancy digest with links only. Visible leads included:

- `134062447` - `Руководитель проектов` - `Р7`
- `134016278` - `Директор по информационным технологиям (CIO)` - `Костромской ювелирный завод Каратов`
- `133954979` - `Разработчик AI агентов` - `СБЕР`
- `134113881` - `Старший менеджер проекта (Senior Project Manager)` - `Топассистент`, salary visible in email: `от 4500 EUR/month`
- `134077560` - `Founding Engineer (AI HR Tech)` - `Технологии Будущего`
- `134086561` - `Директор проекта по внедрению ИИ` - `Мираторг, Агропромышленный холдинг`

## MCP Check

- `mcp__headhunter.hh_get_dictionaries` works, so the server starts and can reach HH public API reference endpoints.
- `mcp__headhunter.hh_get_vacancy` for `134062447` and `134086561` returned `403 Forbidden`.
- `mcp__headhunter.hh_search_vacancies` for `Руководитель проектов Р7` and `Директор проекта по внедрению ИИ Мираторг` returned `403 Forbidden`.
- Conclusion: current MCP/public API access is useful for reference data, but vacancy search/detail endpoints are blocked in this session until OAuth/app credentials or another HH access path is available.

## First-Pass Triage

- `Мираторг - Директор проекта по внедрению ИИ`: duplicate of an already reviewed/applied role; keep waiting for employer response.
- `Технологии Будущего - Founding Engineer (AI HR Tech)`: most interesting new lead from the digest; likely Startup / Product Engineering plus AI Transformation, needs full JD.
- `СБЕР - Разработчик AI агентов`: potentially relevant topic, but title suggests hands-on developer; needs full JD to separate AI engineering lead from downleveled developer role.
- `Каратов - CIO`: potentially relevant Digital Transformation / Business Unit role, but company/domain and scope are unknown; needs full JD.
- `Топассистент - Senior Project Manager`: visible salary from `4500 EUR/month` is worth a quick look, but title may be below target leadership level.
- `Р7 - Руководитель проектов`: too generic from email alone; low priority unless full JD shows product/platform/engineering ownership.

## Routing Note

No full JD text was included, and the current HeadHunter MCP session cannot fetch vacancy detail/search endpoints due to `403 Forbidden`.

Update: full JD text for all listed roles was pasted by the user later on 2026-06-12 and routed into normal job-intake archives/analyses.

Follow-up task: `tasks/active/2026-06-12-review-hh-digest-cto-product-engineering-vacancies.md`.

## Created Analyses

- `analyses/2026-06-12-r7-project-manager-analysis.md`
- `analyses/2026-06-12-karatov-cio-analysis.md`
- `analyses/2026-06-12-sber-ai-agents-developer-analysis.md`
- `analyses/2026-06-12-topassistant-senior-project-manager-ai-voice-analysis.md`
- `analyses/2026-06-12-future-technologies-founding-engineer-ai-hr-tech-analysis.md`

## Mailbox Cleanup

- Rechecked via Gmail on 2026-06-12: message `19ebaf3c69f4503f` is fully represented by this processed note, job-intake analyses, and follow-up tasks.
- Safe to move the Gmail message to Trash.
