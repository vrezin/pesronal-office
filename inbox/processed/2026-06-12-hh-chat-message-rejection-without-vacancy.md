# HH Chat Message - Rejection Without Vacancy Context

Date processed: 2026-06-12

## Source

- Gmail message id: `19eb4d004f807b9c`
- Subject: `Новое сообщение от работодателя`
- HH timestamp: `2026-06-11T03:53:11`
- Chat link includes `chat_id=5389973874`

## Message

Employer wrote:

```text
Здравствуйте!
Большое спасибо за интерес к вакансии! К сожалению, сейчас мы не готовы пригласить вас на следующий этап.
Ценим ваше внимание и будем рады получать ваши отклики на другие позиции.
```

## Routing

- This is a rejection signal.
- The email body does not include vacancy title or company.
- Do not update a specific vacancy status without resolving `chat_id=5389973874` to an application/vacancy.

## Tooling Gap

- `headhunter-web-mcp` needs a tool to open/parse HH chat links by `chat_id` and return:
  - company;
  - vacancy title;
  - vacancy id;
  - latest message text;
  - inferred status;
  - related application record if available.

## Mailbox Cleanup

- Safe to move Gmail message `19eb4d004f807b9c` to Trash after preserving this unresolved signal.
