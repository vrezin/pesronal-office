# Life Planning Engine

Назначение: превращать входящие факты о жизни, здоровье, образе жизни, проектах, деньгах, встречах и обязательствах в текущие планы дня, недели и месяца.

Это не место для зашитого "плана на вчера". Это операционный протокол: факты живут в фактовых разделах, планы генерируются и корректируются на их основе.

## Источники Фактов

- Health facts: `life/health-lifestyle/health-facts/`
- Lifestyle facts: `life/health-lifestyle/lifestyle-facts/`
- Дом / семья / отдых: `life/home-family-rest/`
- Личные проекты: `personal-projects/`
- Компании: `companies/`
- Деньги и обязательства: `finance/`
- Встречи и время: `calendar/`
- Задачи и ожидания: `tasks/`
- Люди и follow-ups: `people/`

## Производные Планы

- Daily plans: `calendar/daily/YYYY-MM-DD.md`
- Weekly plans: `calendar/weekly/YYYY-Www.md`
- Monthly plans: `calendar/monthly/YYYY-MM.md`
- Shopping/menu plan: обычно часть weekly plan, с отдельным блоком "Saturday groceries".
- Medication schedule: часть daily/weekly plan, строится только из `health-facts/medications.md`.

## Skills

Use repo-local skills in `.codex/skills/`:

- `life-planning` - разобрать новый вход, обновить факты/задачи/календарь, собрать планы недели, лекарства, меню и закупки.
- `personal-office-intake` - маршрутизировать входы, которые затрагивают не только жизнь, но и компании, деньги, людей или проекты.

## Safety

- Не назначать лекарства, дозировки, диеты или тренировки от себя.
- Не менять медицинские инструкции без явного пользовательского входа.
- Если вход медицински неоднозначен или рискован, зафиксировать вопрос в `inbox/processed/needs-clarification-YYYY-MM-DD.md`.
- Планы должны быть реалистичными: учитывать сон, восстановление, поездки, встречи, бытовые блокеры и энергию.
