# Resolved: MOEX Delivery Lead HH Rejection

Date: 2026-06-23
Source: Gmail / hh.ru
Gmail message id: `19ef02ca444bdd43`
Gmail thread id: `19eee26f86a8c863`
HH chat id: `5393565315`
Email timestamp: 2026-06-22T16:31:57

## Summary

HH sent a new employer chat message after the previous monitor state marker.

User later matched the chat to:

- Company: Московская Биржа
- Vacancy: Delivery Lead
- HH state: `Вакансия в архиве`

Employer message:

> Спасибо за интерес к вакансии! Мы ценим ваше желание работать с нами, но уже закрыли эту позицию.
>
> Возможно, скоро снова появится подходящая для вас позиция - можете подписаться на вакансии компании, чтобы не пропустить.
>
> С уважением, Богатырева Юлия

## Classification

`status_update`

This is a rejection / closed-position update.

## Resolution

2026-06-23 follow-up: attempted `hh_web_open_chat_by_chat_id` for chat `5393565315`, but the tool did not expose the vacancy/company from the chat page. A direct applications sweep also did not surface this archived MOEX vacancy in the fresh visible rejected list, so the user supplied the missing chat context.

User supplied the missing chat context: this is `Московская Биржа - Delivery Lead`, an archived vacancy.

Updated:

- `tasks/waiting/2026-06-09-moex-delivery-lead-employer-response.md` moved to `tasks/done/2026-06-23-moex-delivery-lead-rejected.md`;
- `personal-projects/personal-brand/workspace/job-intake/analyses/closed/2026-06-09-moex-delivery-lead-api-first-analysis.md`;
- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`.

## Follow-Up

None for this archived vacancy. Keep MOEX/API First as a market signal.
