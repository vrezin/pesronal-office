# 2026-06-15 - ZenMoney Money System Intake

## Source

- User request in chat: check what is currently visible through ZenMoney and start designing how money should be managed inside Personal Office.
- ZenMoney MCP read-only calls on 2026-06-15:
  - accounts;
  - categories;
  - June 2026 budgets;
  - transactions for 2026-06-01..2026-06-15.

## Route

- Primary route: `finance/`.
- Supporting route: `tasks/active/` because the money operating system needs follow-up design and data cleanup.

## Resulting Artifacts

- `finance/personal-budget/2026-06-15-zenmoney-initial-snapshot.md`
- `tasks/active/2026-06-15-design-personal-office-money-system.md`

## Handling Rules Applied

- ZenMoney was used read-only.
- Sensitive raw identifiers and full transaction dumps were not copied into repository artifacts.
- The first decision is to treat ZenMoney as transaction/source data, not as the whole Personal Office finance operating model.
