# Credit Obligations Register

## Purpose

Register of family credit obligations, debts, and debt-like accounts.

This file is the debt side of the Personal Office money model. It must be read together with:

- `finance/family-assets/real-estate-register.md`
- `finance/family-assets/tyumen-studio-cashflow.md`
- `finance/personal-budget/account-role-register.md`

## Last Read

- Date: 2026-06-15
- Source: ZenMoney MCP read-only calls:
  - accounts;
  - `Гашение кредита` transactions;
  - parent `Студия` transactions.
- Sensitive handling: ZenMoney account ids are intentionally not stored here.

## Obligations

| Obligation | Visible ZenMoney account / evidence | Current balance / payment | Status | Treatment | Missing facts |
|---|---|---:|---|---|---|
| Cash loan / consumer credit | `Кредит наличными` account; `Гашение кредита` payments | balance about -3.315M RUB; annuity payment about 70.45K RUB/month; annual rate 16.2%; payment day is the 4th day of each month | active, high priority, confirmed by user | Include in liabilities and monthly debt-service burden. | Bank/lender, maturity, remaining term, early repayment rules, whether payment can be reduced/refinanced. |
| Sber credit card | `Sber. Кредитка` account; user-provided current bank-app values | due by 2026-07-13; minimum payment 4,528.03 RUB; payment for interest-free period 46,038.39 RUB; total debt 159,673.56 RUB including today's operations; grace period is 120 days | active, control data confirmed by user | Include in short-term liabilities; for control, pay 46,038.39 RUB by 2026-07-13 if preserving interest-free period. | Confirm whether later operations change the payment required before due date. |
| Tinkoff / T-Bank credit card | `Tinkoff. Кредитка` account; Gmail statement in Trash | statement period 2026-05-08..2026-06-07; due 2026-07-01; minimum payment 1,700 RUB; payment for interest-free period 96,237 RUB; debt on 2026-06-07 was 96,237 RUB | active, statement found | Include in short-term liabilities; for control, pay 96,237 RUB by 2026-07-01 if preserving interest-free period. | Confirm whether this maps exactly to ZenMoney `Tinkoff. Кредитка` balance and whether later transactions changed the amount. |
| Generic debt account | `Долги` account | about -30K RUB | stale/accounting artifact | Exclude from real liabilities. | User says there is no such real debt; likely forgotten stale tracking item. |
| Tyumen studio mortgage | `Ипотека студия` account and parent `Студия` transactions | observed payments about 17-17.5K RUB/month; user recalls rate about 6%; payment date can be inferred from transaction history; ZenMoney account shows positive balance about 104.6K RUB | active but account semantics unclear | Treat as preferential/subsidized mortgage tied to the Tyumen studio; include monthly payment in obligations; do not infer principal from ZenMoney balance yet. | Outstanding principal, exact rate, maturity, lender, exact payment schedule, why ZenMoney account balance is positive. |
| Negative RUB cash account | `Наличные Рубли` account | about -376K RUB | accounting/input error | Exclude from available cash and real liabilities. | User says this is likely an input/accounting error. |
| Negative closed/investment-like accounts | `Тбанк закрытый депозит катя`, `Тинькофф тбанк инвестиции Катя`, `Точка Катя депозит` | mixed negative balances | needs clarification | Exclude from debt total until semantics are confirmed. | Whether stale/closed artifacts, real obligations, or accounting corrections. |

## Observed Debt-Service Transactions

### Cash Loan / Consumer Credit

ZenMoney category checked: `Гашение кредита`.

Observed payments:

- 2026-01-04: 70,061.43 RUB.
- 2026-05-04: 62,511.08 RUB plus 7,938.92 RUB, totaling 70,450 RUB.
- 2026-06-04: 70,450 RUB.

Working rule:

- Treat the cash loan as approximately 70.45K RUB/month recurring debt service due on the 4th day of each month.
- User confirmed this is an annuity loan with annual rate 16.2%.

### Tyumen Studio Mortgage

ZenMoney parent category checked: `Студия`.

Observed mortgage-like payments:

- 2025-12-22: 17,300 RUB.
- 2026-02-15: 17,000 RUB.
- 2026-03-02: 17,500 RUB.
- 2026-04-03: 17,500 RUB.
- 2026-05-01: 17,500 RUB transfer line visible under `Студия`.

Working rule:

- Treat the Tyumen studio mortgage as about 17-17.5K RUB/month debt service.
- It is strategically different from consumer debt because it is attached to an income-producing asset and a preferential/subsidized mortgage.
- User recalls the mortgage rate is about 6%; exact terms still need confirmation.

### Tinkoff / T-Bank Credit Card

Gmail Trash contained a statement email from T-Bank:

- Sender: `inform@emails.tinkoff.ru`.
- Subject: `Выписка по кредитной карте за период с 08.05.2026 по 07.06.2026`.
- Email timestamp: 2026-06-08.
- Statement period: 2026-05-08..2026-06-07.
- Pay by: 2026-07-01.
- Minimum payment: 1,700 RUB.
- Payment for interest-free period: 96,237 RUB.
- Debt on 2026-06-07: 96,237 RUB.

Working rule:

- To keep the interest-free period, plan 96,237 RUB by 2026-07-01 unless the bank app shows a newer corrected amount.
- Minimum payment only protects against formal delinquency; it does not satisfy the interest-free-period goal.

Gmail Trash also contained a T-Bank email `Информация о платежах` from `credit@emails.tinkoff.ru` dated 2026-06-05. It points to a statement for 2026-05-05..2026-06-04 and says payments are automatically debited from a debit card, but the email body did not expose amount/date. Treat it as a pointer to inspect in the bank app, not as extracted debt evidence.

### Sber Credit Card

User provided current bank-app/control values:

- Due date: 2026-07-13.
- Minimum payment: 4,528.03 RUB.
- Payment for interest-free period: 46,038.39 RUB.
- Total debt: 159,673.56 RUB.
- Grace period: 120 days.

Interpretation:

- Total debt includes today's operations and can differ from the current ZenMoney balance.
- To preserve the interest-free period, plan 46,038.39 RUB by 2026-07-13 unless the bank app shows an updated amount before due date.
- Minimum payment protects against formal delinquency but does not satisfy the interest-free-period goal.

## Gmail Evidence Search Summary

On 2026-06-15, Gmail was searched read-only for Sber/Tinkoff/T-Bank credit-card statements, minimum payment wording, debt wording, and sender-domain variants.

Result:

- Main mailbox search excluding Trash did not find reliable credit-card statement emails.
- Trash search found the current T-Bank credit-card statement above.
- Trash search did not find a reliable Sber credit-card statement.
- User checked another mailbox/copy and did not find the Sber statement; likely deleted.

Interpretation:

- T-Bank credit-card control data is partially restored from Gmail Trash.
- Sber credit-card current control values were provided by user from bank-app/current source.
- Earlier recurring rule was due date around the 14th day of each month; current concrete due date is 2026-07-13.
- Likely next sources for Sber: bank app, SMS/push notifications, next email statement, or more precise sender/subject examples.

## Monthly Debt-Service Baseline

Known recurring debt service before credit-card minimums:

- Cash loan: about 70.45K RUB/month, due on the 4th day of each month.
- Tyumen studio mortgage: about 17-17.5K RUB/month.

Working known baseline: about 87.5-88K RUB/month.

This excludes one-off/current credit-card grace payments:

- Sber full interest-free-period payment: 46,038.39 RUB due 2026-07-13.
- T-Bank full interest-free-period payment: 96,237 RUB due 2026-07-01.
- any real meaning of negative closed/deposit/investment-like accounts;
- taxes/fees/insurance connected to loans.

## Reporting Rules

- Separate strategic mortgage debt from consumer debt.
- Do not count the Tyumen studio mortgage as a pure negative without the asset and rent offset.
- Treat credit-card balances as risky/high-priority until grace-period status is known.
- For Sber credit card, preserving grace period currently requires 46,038.39 RUB by 2026-07-13 according to user-provided current bank-app values; total debt is 159,673.56 RUB and can differ from ZenMoney because it includes today's operations.
- For T-Bank credit card, preserving grace period requires 96,237 RUB by 2026-07-01 according to the statement found in Gmail Trash.
- Exclude `Долги` and `Наличные Рубли` from real liabilities unless new evidence appears; they are currently classified as stale/accounting artifacts.
- Do not include other ambiguous negative accounts in a headline liability total until explained.
- Monthly close must show:
  - total mandatory debt service;
  - credit-card due dates/minimums;
  - consumer loan balance;
  - mortgage offset from studio rent;
  - debt risks for the next 30 days.

## High-Priority Questions

- What are the exact terms of the cash loan: bank, rate, maturity, remaining principal, monthly payment, early repayment conditions?
- Are the Sber and Tinkoff credit-card balances inside grace period or already interest-bearing?
- Does the Sber grace-preserving amount change before 2026-07-13 because of today's/future operations?
- Has the T-Bank statement amount changed after 2026-06-07, or is 96,237 RUB still the correct interest-free-period payment by 2026-07-01?
- What are the exact Tyumen studio mortgage terms and why does the ZenMoney account show a positive balance?
- Are the negative closed/deposit/investment-like accounts real obligations or stale accounting artifacts?
