# Job Intake Process

Цель процесса: каждый новый JD сохранять, разбирать по единой логике и быстро получать практический ответ:

- каким резюме откликаться;
- нужно ли делать tailored version;
- что подчеркнуть в сопроводительном письме;
- какие риски снять заранее;
- какие вопросы задать рекрутеру / hiring manager.

## Input

Пользователь кидает в чат текст вакансии или ссылку + текст.

Минимально полезно сохранить:

- дата разбора;
- источник: HH, LinkedIn, direct, recruiter, referral;
- название компании, если известно;
- название роли;
- полный текст JD;
- заметки пользователя: "вкусная", "сомнительная", "хочу откликнуться", "похоже на X".

## Storage

Новые вакансии сохраняются в:

- `jd-archive/YYYY-MM-DD-company-role.md`

Разбор сохраняется в:

- `analyses/YYYY-MM-DD-company-role-analysis.md`

Если компания неизвестна, использовать `unknown-company`.

## Analysis Output

Каждый раз выдавать пользователю короткий ответ:

1. `Вердикт`: откликаться / откликаться после адаптации / не приоритет / рискованный матч.
2. `Лучшее резюме`: одно из финальных CV или рекомендация сделать tailored copy.
3. `Почему матч`: 5-7 конкретных совпадений с JD.
4. `Риски`: overqualification, hands-on mismatch, age/years signal, domain gap, tech-stack gap, relocation/format, salary/level ambiguity.
5. `Как снять риски`: 2-4 формулировки для сопроводительного или интервью.
6. `Сопроводительное`: готовый текст.
7. `Вопросы`: 2-5 вопросов, которые стоит задать.

## Current Final CV Set

- `AI Transformation Lead - AI Automation Architect.pdf`
- `CTO - Co-founder CTO - Head of Product Engineering.pdf`
- `CTO - Head of Engineering - Stability and Governance.pdf`
- `CTO - VP Engineering - Director of Engineering.pdf`
- `Digital - Technology Transformation Director.pdf`

## Default Recommendation Logic

- AI / GenAI / automation / agents / RAG / AI transformation -> AI Transformation Lead.
- Early-stage, MVP, first customers, product roadmap, co-founder, product engineering -> Startup / Scale-up CTO.
- Large engineering org, VP Engineering, Director Engineering, platform scale, 100+ engineers -> Heavy Enterprise.
- Digital transformation, modernization program, business process transformation, CIO transformation -> Digital / Technology Transformation.
- Production stability, technical debt, SDLC, release governance, incidents, legacy modernization, predictable delivery -> Stability & Governance.
- Integrator, ERP, 1C, business unit, P&L, enterprise implementation -> Business Unit / Integration track, not yet finalized as a PDF.

## Rule Discussion Backlog

Правила нужно отдельно согласовать и уточнять на реальных вакансиях:

- когда не откликаться вообще;
- когда выбирать HH-резюме, а когда делать tailored copy;
- насколько агрессивно скрывать ранний опыт;
- когда оставлять `23 years`, а когда держать `12-15 years`;
- как писать про hands-on без дауншифтинга;
- как оценивать tech-stack gaps;
- как учитывать российский / международный рынок;
- как классифицировать вакансии интеграторов и business-unit roles.
