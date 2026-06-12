# Personal Office vs AI-OS Gap Analysis

Дата: 2026-06-10

Цель: сравнить текущую репу `Personal Office` с рамкой AI-OS на уровне продукта и операционной системы.

## Короткий вывод

`Personal Office` уже сильнее многих AI-OS-концептов в части реального контекста, маршрутизации и долговременного хранения артефактов.
Но у репы пока слабее публичный "продуктовый слой": единый пользовательский опыт, явная автономия агентов, завершенный цикл проверки и наглядная витрина зрелости системы.

## Таблица

| Область | У нас есть | У нас нет / слабее | Где мы лучше | Где недотягиваем |
|---|---|---|---|---|
| Входящий поток | `inbox/raw/`, `inbox/processed/`, rules of routing, clarification notes | Нет единого inbox cockpit с явной action queue, который сразу показывает каждый новый вход, его статус, владельца, next step и блокеры | Реальный ingress pipeline с маршрутизацией, traceability и сохранением обработки в артефактах | Пока это больше backend intake pipeline, чем пользовательский inbox, который каждый день отвечает: что делать сейчас |
| Задачи и follow-ups | `tasks/active/`, `tasks/waiting/`, `tasks/someday/`, `tasks/done/` | Нет единой orchestration-надстройки, которая сама собирает и закрывает next steps | Хорошая база для обязательств, зависимостей и ownership | Не хватает авто-приоритизатора, статуса по каждой задаче и “one place to act” |
| Календарь и время | `calendar/daily/`, `weekly/`, `monthly/`, `meetings/`, rules for meetings | Нет time cockpit, который сводит задачи, встречи и свободные окна в один план | Сильная структуризация временных обязательств и встреч | Не хватает briefing/scheduling слоя и явного автоплана на день/неделю |
| Память | `memory/short-term/`, `episodic/`, `semantic/`, `entities/`, `knowledge-graph/`, retrieval rules | Нет зрелого semantic retrieval как обязательного product layer | Сильнее большинства “чат-ботов” за счет долговременной памяти и связей | Не хватает надежной автоматической консолидации и очевидного recall UX |
| Люди и отношения | `people/contacts/`, `relationship-notes/`, `follow-ups/` | Нет богатого relationship CRM поверх личных контактов | Лучше многих личных AI-OS идей, потому что люди уже как сущности | Слабее в напоминаниях, истории взаимодействий и следующем шаге по каждому контакту |
| Деньги | `finance/`, отдельная интеграция с ZenMoney, правила приватности | Нет полноценного personal finance cockpit с прогнозами и сценариями | Есть настоящий домен денег, а не абстракция | Недотягивает в аналитике, сценариях, cashflow-view и decision support |
| Проекты и компании | `personal-projects/`, `companies/`, карты доменов, отдельные рабочие контуры | Нет единого project OS с общими метриками статуса/риска/следующего шага | Сильная доменная разметка и границы между контекстами | Недостаточно единого dashboard'а по всем проектам |
| Автоматизация | `automation/`, cron/systemd, run logs, state markers, HH и LinkedIn monitors | Нет большого набора автономных агентов и end-to-end workflow orchestration | Лучше большинства концептов тем, что есть реальные scheduled jobs и traces | Не хватает более широкого слоя действий “после триггера” и resilient orchestration |
| Модель работы | `AGENTS.md`, `wiki/README.md`, `wiki/maps/`, playbooks, secretary routing | Нет одного простого публичного интерфейса “как этим пользоваться” для пользователя | Сильная внутренняя операционная дисциплина и маршрутизация | Недотягивает в простоте онбординга и видимой ценности на первом экране |
| Проверка и честность | Правила не оставлять важное только в чате, source-of-truth подход, clarifications | Нет явного зрелого verify/review слоя на каждом типе артефакта | Лучше многих AI-OS идей, потому что строится вокруг source-of-truth | Не хватает встроенной в продукт проверки качества результата и confidence signaling |
| Публичная витрина | Есть `personal-projects/ai-automation-portfolio/` | Нет полностью собранного consumer-style AI-OS продукта | Есть материал для позиционирования и портфолио | Не хватает цельного narrative + polished surface + demo path |

## Итоговая оценка

Если сравнивать с “идеальной” AI-OS из плаката, то у нас:

- `уже есть` прочный backend личной операционной системы;
- `уже есть` структура памяти, задач, календаря, людей, денег, проектов и автоматизаций;
- `лучше` многих концептов в честности, трассируемости и работе с реальным контекстом;
- `хуже` в едином продуктовом опыте, видимой автономии и удобстве для пользователя.

## Product Direction Clarification

Вывод из gap analysis: правильная ось - не generic AI assistant, а workflow-first operating system.

Цикл выглядит так:

- intake -> classification -> decision;
- decision -> task / calendar / memory / people / finance / project artifact;
- scheduled automation -> recheck -> close the loop.

То есть chat - это один из режимов intake, а не центр продукта.

### Why The Action Queue Matters

The missing piece is not a prettier inbox. It is a living action queue.

Without it, the system can store everything correctly and still feel тупое because the user must manually reconstruct:

- what needs attention now;
- what is waiting on someone else;
- what is blocked;
- what is stale;
- what can be ignored.

The action queue is the layer that turns stored context into daily operating clarity.

The concrete follow-up for this gap is tracked in:

- `tasks/active/2026-06-10-design-action-queue-for-personal-office.md`

## Surface Strategy

The likely best default is not to replace Google/Yandex surfaces up front.

Instead:

- use existing ecosystems for input and notification surfaces where they are already strong;
- keep Personal Office as the workflow brain, state machine, and traceable source of truth;
- only build a custom UI where it creates a materially better action cockpit, not just a prettier shell;
- add a thin unified dashboard later if the product needs one screen for status, risk, and next step.

So the question is not “do we build a new face?”, but “where does a new face create a workflow advantage that existing surfaces cannot provide?”

## Практический смысл

Наш сильный козырь не в “AI chat”, а в `owned-context OS`: система, где входящий поток превращается в действия и память.

Главная недостача сейчас:

- единый верхнеуровневый продуктовый слой;
- более очевидный status/priority dashboard;
- больше автоматической проактивности;
- понятный путь для внешнего пользователя или демо-сценария.
