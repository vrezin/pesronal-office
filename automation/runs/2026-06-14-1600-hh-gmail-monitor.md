# HH Gmail Monitor Run

- Run started: 2026-06-14 16:00 +07
- State marker before run: 2026-06-14 12:00:00 +07
- Last processed Gmail message id before run: `19ec0d3d9c40220d`
- Last processed Gmail internal date before run: 2026-06-13T11:52:49
- Gmail access: available
- Repository write access: available
- Git commit access: available

## Search

- Overlap query: HH.ru / HeadHunter messages after 2026-06-13, excluding spam/trash.
- Rationale: one-day overlap from the saved state marker to avoid missing delayed messages.

## Results

- Messages returned by overlap search: 2
- New messages after the stored state marker: 1
- Re-seen overlap message: `19ec0d3d9c40220d`, `2026-06-13T11:52:49`, subject `Подходящие вакансии для резюме: «Директор по разработке / Технический лидер бизнес-юнита»`.
- New message: `19ec53a066478a26`, `2026-06-14T08:22:53`, subject `Подходящие вакансии для резюме: «Директор по разработке / Технический лидер бизнес-юнита»`.

## Classification

| Message id | Classification | Action |
|---|---|---|
| `19ec0d3d9c40220d` | already_processed / overlap | No artifact updates; already covered by previous successful run. |
| `19ec53a066478a26` | new_vacancy / thin digest | Created processed note and active review task. No full JD analysis created. |

## New Digest Leads

| Rank | Vacancy ID | Company | Role | Reason |
|---|---:|---|---|---|
| Interesting | 132091890 | RWB (Wildberries & Russ) | Руководитель группы разработки в Know Your Employee & Partner | Direct development-leadership signal; needs full JD for scope, salary, and format. |
| Maybe | 134108980 | Lenkep recruitment | Head of Mobile Development (iGaming) | Engineering-leadership title, but iGaming and agency context need a hard fit check. |
| Maybe | 134069614 | Рекрутинговое агентство Натальи Егоровой | Директор по развитию | Visible `from 400000 RUB/month`, but no AI/product/engineering signal from digest alone. |
| Maybe-low | 133804143 | FIX | Product Delivery Manager (B2G) | Possible delivery/product overlap; likely management-heavy until full JD proves otherwise. |
| Not interesting from digest alone | 133952093 | Первый Бит | Руководитель отдела по предоставлению IT-сервисов / Service Delivery Manager | Service-delivery/integrator signal does not match the current AI-first direction. |
| Not interesting from digest alone | 133124220 | ГК Компьютеры и сети | Руководитель проектного офиса (ИТ-проекты, г. Новосибирск) | Local PMO title lacks AI/product/engineering leverage and target-income evidence. |

## Artifact Updates

- Created `inbox/processed/2026-06-14-hh-business-unit-digest-thin-links.md`.
- Created `tasks/active/2026-06-14-review-hh-business-unit-digest-vacancies.md`.
- Did not update `job-intake/jd-archive/`, `job-intake/analyses/`, `job-intake/INDEX.md`, or `COMPANY_NOTES.md` because the email did not include full JD text.
- State file update planned after repository write and commit attempt.

## Gmail Actions

- No Gmail labels, stars, importance markers, archive state, or deletion state were changed.
- Recommended Gmail action: archive or delete the digest after the review task is resolved.

## Commit

- Commit created with message `chore: process hh gmail digest`.

## Outcome

Success: Gmail scan completed; one new HH thin vacancy digest was preserved as processed intake and queued for review.
