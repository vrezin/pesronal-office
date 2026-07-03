# HH Rejection Processed - Tensor / Saby

Date processed: 2026-07-02

## Source

User pasted an HH rejection notice:

- Company: Тензор
- Vacancy: Руководитель направления разработки
- Location: Новосибирск
- Compensation: 350000-580000 RUR per month
- Employer link: `https://my.hh.ru/b/1lzgjo0`
- Vacancy link: `https://my.hh.ru/b/1lzgjo2`
- Details link: `https://my.hh.ru/b/1lzgjo3`

User later pasted the HH chat context:

- Vacancy status in HH: archived.
- Application date: 2026-06-03.
- User's cover note emphasized architecture, product logic, high-load systems,
  engineering quality/governance, enterprise automation, business processes,
  document flow/logistics services, and the balance between architecture, team
  management, and hands-on technical expertise.
- Rejection sender: Майорова Мадина.
- Rejection reason as stated: the company has already closed the position.

Scheduled HH Gmail monitor later confirmed matching HH rejection evidence:

- Gmail id: `19f2342b5904a58d`
- Gmail timestamp: `2026-07-02T14:36:41`
- HH vacancy id: `133782222`
- Subject: `Работодатель не готов пригласить вас`
- Company: Тензор
- Vacancy: Руководитель направления разработки
- Gmail id: `19f2344884afb3be`
- Gmail timestamp: `2026-07-02T14:38:41`
- HH chat id: `5379550808`
- Subject: `Новое сообщение от работодателя`
- Chat sender: Майорова Мадина

`hh_web_open_chat_by_chat_id(5379550808)` returned `not_resolved`; the chat
page did not expose the company/vacancy. The attribution to Tensor/Saby is based
on the adjacent HH system rejection for `133782222` plus the existing
user-provided Tensor/Saby chat context with the same sender and rejection reason.

## Routing

- Updated `personal-projects/personal-brand/workspace/job-intake/INDEX.md`.
- Updated `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`.
- Added `tasks/done/2026-07-02-tensor-saby-head-development-direction-rejected.md`.

## Decision

Mark the known Tensor / Saby Novosibirsk `Руководитель направления разработки`
application lane as rejected / closed because the position was closed/archived.
Gmail now confirms the HH vacancy id `133782222`.

Do not close all future Tensor / Saby opportunities. Reopen only if a materially
different vacancy, direct contact, or new direction appears.
