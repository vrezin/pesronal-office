# Routing Map

Маршрутизация входящего потока.

## Default Flow

1. Сырой вход попадает в `inbox/raw/`.
2. Intake secretary определяет тип входа.
3. Создается или обновляется артефакт в целевом разделе.
4. Если появился следующий шаг, создается задача в `tasks/active/` или `tasks/waiting/`.
5. Разобранный вход переносится или кратко фиксируется в `inbox/processed/`.

## Routing Rules

| Если вход содержит | Куда маршрутизировать | Что создать |
|---|---|---|
| дата, время, участники, созвон | `calendar/meetings/` | meeting note + follow-up tasks |
| обещание, следующий шаг, дедлайн | `tasks/active/` или `tasks/waiting/` | task note |
| деньги, сумма, платеж, актив, долг | `finance/` | finance note + task if needed |
| дом, семья, отдых, бытовой вопрос | `life/home-family-rest/` | note или task |
| здоровье, режим, сон, спорт | `life/health-lifestyle/` | note, routine или task |
| Profi.ru / личная консультация | `personal-projects/profi-ru/` или `personal-projects/consulting/` | opportunity / client note |
| вакансия, поиск работы, CV, HH, карьерное позиционирование | `personal-projects/personal-brand/` | JD archive / analysis / CV decision |
| письмо HH.ru: отклик, приглашение, отказ, новая вакансия | `personal-projects/personal-brand/workspace/job-intake/` + `tasks/` | status update / task / JD analysis |
| фактическая текущая работа, employment contract, условия занятости | `work/` | current role / contract note |
| Fincom / FinSOK | `companies/fincom/` | company artifact |
| AI Studio | `companies/ai-studio/` | company artifact |
| новый бизнес | `companies/future-companies/` | opportunity note |
| человек / контакт / договоренность | `people/` | contact / relationship / follow-up |
| устойчивый факт, предпочтение, повторяющийся контекст | `memory/` + целевой source-of-truth | memory note + source update |
| новая область знаний или навигационное правило для агентов | `wiki/maps/` | wiki map update |
| связь между сущностями, проектами, инструментами или темами | `memory/knowledge-graph/` | graph node/edge |
| регулярный агентский запуск, cron/systemd/codex exec | `automation/` | prompt / script / state / run log |
| непонятно | `inbox/processed/` | needs-clarification note |

## Known Boundary Decisions

| Item | Route |
|---|---|
| Personal brand / CV / career positioning for Vladimir Rezin | `personal-projects/personal-brand/` |
| Public Vladimir Rezin AI automation portfolio site | `personal-projects/ai-automation-portfolio/` for planning; dedicated repo for website files |
| Country house / home construction / family house documents | `life/home-family-rest/country-house/` |
| AI Studio official project, company, portfolio, process, and product truth | `<aistudio-root>` with management index in `companies/ai-studio/` |
| Fincom / FinSOK company truth | `<fincom-root>` with management index in `companies/fincom/` |

## Naming

Use stable names:

```text
YYYY-MM-DD-topic.md
```

For meetings:

```text
YYYY-MM-DD-person-or-company-topic.md
```

For tasks:

```text
YYYY-MM-DD-action-topic.md
```
