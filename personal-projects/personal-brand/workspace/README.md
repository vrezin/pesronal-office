# Personal Brand Workspace: Vladimir Rezin

Дата актуализации: 2026-06-09

Эта папка - канонический рабочий контур для персонального бренда, поиска работы, CV, JD intake, cover letters и карьерного позиционирования.

Главный диспетчер:

- `OPERATING_MODEL.md`

## Структура

- `source/` - сырой экспорт / вставка из HH и другие исходные тексты.
- `cv-originals/` - копии старых резюме, cover letters, сертификатов и экспортов из `<external-downloads>`; это доноры, не актуальный source-of-truth.
- `positioning/` - бренд-архитектура, market feedback и канальные стратегии.
- `resume-targets/` - master-profile, evidence bank, experience strategy и outline-ы.
- `final-cv/` - финальные PDF-экспорты резюме и реестр версий.
- `job-intake/` - процесс сохранения и разбора вакансий: архив JD, правила матчинга, шаблон анализа и рекомендации по отклику.

## Главная идея

Не надо собирать одно универсальное резюме. Есть один master-profile и портфель финальных CV под разные рынки:

1. AI-first специалист / архитектор внедрения AI.
2. Startup CTO / co-founder CTO для быстрого поиска product-market fit.
3. Heavy enterprise technology leader для больших платформ, команд и критичных систем.
4. Transformation & digitalization leader для модернизации, процессов и цифровых изменений.
5. Stability & Governance для HH/ATS ролей про production, SDLC, reliability и predictable delivery.
6. Business Unit / Integration для интеграторов, enterprise automation, P&L, presale и delivery portfolio.

Общий бренд при этом один:

> Технологический лидер, который соединяет бизнес-цели, архитектуру, команды и AI/automation в работающие продукты и управляемые изменения.

## Что уже собрано

- Сырой HH-профиль: `source/hh-profile-raw-2026-05-31.txt`.
- Старые резюме, письма и сертификаты: `cv-originals/`.
- Карта позиционирования: `positioning/brand-architecture.md`.
- HR/market feedback и стратегия упаковки под HH/ATS/direct search: `positioning/hr-market-feedback-2026-05-31.md`.
- Инвентаризация текущих резюме: `positioning/cv-inventory.md`.
- Master-profile: `resume-targets/master-profile.md`.
- Evidence bank: `resume-targets/evidence-bank.md`.
- Матрица глубины опыта по версиям резюме: `resume-targets/experience-block-strategy.md`.
- Русская версия матрицы глубины опыта: `resume-targets/experience-block-strategy-ru.md`.
- План переработки резюме под портфель треков: `resume-targets/remix-plan.md`.
- Outline резюме под каждый трек: `resume-targets/*-cv-outline.md`.
- Отдельный ATS-friendly контур под production stabilization / engineering governance: `resume-targets/cto-stability-governance-cv-outline.md`.
- Финальные PDF-версии резюме: `final-cv/README.md`.
- Процесс разбора вакансий и выбора резюме для отклика: `job-intake/README.md`.

## Current Source-Of-Truth Rule

Держать один `master-profile.md` и производные CV из `final-cv/README.md`. Иначе резюме начнут расходиться по фактам, датам и метрикам. Master-profile является источником правды: роли, даты, метрики, компании, стек, подтверждаемые достижения.

Отдельное правило после HR feedback: для HH / ATS нужна compact версия без акцента на `26+ лет` и без подробной ранней карьеры на первом экране. Для executive/direct search масштаб оставляем, но для hands-on ролей заранее снимаем риск overqualification через формулировку `playing coach / hands-on delivery`.
