# HH AI Transformation Digest Web MCP Check

- Date processed: 2026-06-12
- Source: Gmail / HH.ru
- Gmail message id: `19eacd159a057d49`
- Email timestamp: 2026-06-09 14:37:39
- Subject: `Подходящие вакансии для резюме: «AI Transformation Lead / AI Automation Architect»`
- Processing tool: `tools/headhunter-web-mcp`

## Outcome

The HH web MCP successfully classified the email as `vacancy_digest`, extracted 6 unique vacancy links, opened them through the authenticated HH browser session, and separated readable vacancies from an inaccessible one.

## Readable New Vacancies

| Vacancy ID | Company | Role | Status | Next artifact |
|---:|---|---|---|---|
| 134000469 | Группа НЛМК ИТ и Диджитал | Лидер продукта (Умное производство) | `ok` | `tasks/active/2026-06-12-review-hh-ai-transformation-digest-vacancies.md` |
| 133895248 | ООО Ростелеком Информационные Технологии | Техлид / Tech Lead | `ok` | `tasks/active/2026-06-12-review-hh-ai-transformation-digest-vacancies.md` |
| 133996966 | «Филип Моррис Интернэшнл» в России, IT | Руководитель ИТ-платформы (ESB) | `ok` | `tasks/active/2026-06-12-review-hh-ai-transformation-digest-vacancies.md` |
| 133831768 | ООО Клеркгрупп | AI & Process Transformation Lead | `ok` | `tasks/active/2026-06-12-review-hh-ai-transformation-digest-vacancies.md` |
| 133977292 | APi Executive Consulting | Руководитель ИИ-проектов в золотодобычу / Product Owner AI | `ok` | `tasks/active/2026-06-12-review-hh-ai-transformation-digest-vacancies.md` |

## Inaccessible Vacancy

| Vacancy ID | Company from email | Role from email | Status | Note |
|---:|---|---|---|---|
| 133997086 | МФК ВЭББАНКИР | Руководитель IT-практик | `access_denied` | HH shows the vacancy as unavailable to this applicant; do not create a parsed JD from it. |

## Tool Feedback

- `access_denied` handling works and returns `success=false`.
- The digest parser found the correct count: 6 total / 6 unique.
- The report now exposes flattened `title`, `company`, and `salary` fields for email triage, in addition to the nested full vacancy object.
- Remaining gap: chat emails by `chat_id` can still return `not_resolved` when HH does not render chat contents in headless mode.

## Gmail Cleanup

The source email can be moved to Trash after this note and the review task are saved.
