# 2026-06-15 - Design Personal Office Money System

## Status

Active.

## Trigger

Initial read-only ZenMoney inspection showed that the data source works, but the Personal Office finance layer needs account roles, category mapping, and operating rituals before it can safely produce decisions.

## Goal

Design a practical money-management system in Personal Office that uses ZenMoney as source data while keeping financial decisions, obligations, budgets, and risks in durable repo artifacts.

## Immediate Steps

1. Build an account role register. - initial draft created
   - Mark each ZenMoney account as active, stale, duplicate, closed, placeholder, or needs clarification.
   - Assign a role: personal operating cash, family cash, business flow, tax reserve, debt, credit card, investment, deposit, property/studio, foreign-currency reserve.

2. Build a category-to-management-bucket mapping.
   - Keep ZenMoney labels as transaction facts.
   - Add Personal Office buckets for decision-making: baseline family spend, obligations, housing/property, children, health, transport, debt service, business/project, investment/capital, discretionary, taxes.

3. Check data freshness.
   - Verify whether no transactions after 2026-06-10 is expected or a sync/API issue.

4. Create a monthly close template.
   - Income received.
   - Committed obligations.
   - Actual baseline spend.
   - Debt movement.
   - Cash runway.
   - Tax reserve.
   - Big decisions and risks.

5. Decide what should be automated.
   - Read-only ZenMoney pulls are safe by default.
   - Writes to ZenMoney require explicit user approval.
   - Repository artifacts should store summaries and decisions, not raw full transaction dumps.

## Next Control Layer

To switch from inventory to financial control, build these artifacts next:

1. Monthly close template.
   - Actual income received.
   - Mandatory debt service.
   - Credit-card due dates and required payments.
   - Family baseline spend.
   - Studio rent, mortgage offset, коммуналка reimbursements and net effect.
   - Large one-off expenses.
   - Cash runway.
   - Decisions for next month.

2. Debt calendar.
   - Cash loan payment date and amount. - known: annuity, 16.2% annual, about 70.45K RUB/month, due on the 4th day of each month
   - Tyumen studio mortgage payment date and amount. - partially known from transactions, rate recalled as about 6%, exact terms still needed
   - Sber credit-card statement date, due date, minimum payment and grace-period status. - current control values known: due 2026-07-13, minimum 4,528.03 RUB, grace payment 46,038.39 RUB, total debt 159,673.56 RUB, grace period 120 days
   - Tinkoff credit-card statement date, due date, minimum payment and grace-period status. - partially known from Gmail Trash: period 2026-05-08..2026-06-07, due 2026-07-01, minimum 1,700 RUB, grace payment 96,237 RUB

3. Cash buckets.
   - Operating family cash.
   - Personal operating cash.
   - Business/project cash.
   - Tax reserve.
   - Foreign-currency reserve.
   - Deposits/savings.
   - Investments.
   - Excluded/stale accounting artifacts.

4. Category management map.
   - Map ZenMoney categories into control buckets: baseline, children, home, health, transport, debt service, studio/property, business/project, investments, discretionary, taxes, capital expenses.

5. Weekly finance review checklist.
   - Check ZenMoney sync freshness.
   - Classify unknown transactions.
   - Match studio коммуналка reimbursements.
   - Check credit-card risk.
   - Update debt/cash runway.

## Source Artifacts

- `finance/family-assets/real-estate-register.md`
- `finance/family-assets/vehicle-register.md`
- `finance/family-assets/tyumen-studio-cashflow.md`
- `finance/obligations/credit-obligations-register.md`
- `finance/personal-budget/2026-06-15-zenmoney-initial-snapshot.md`
- `finance/personal-budget/account-role-register.md`
- `inbox/processed/2026-06-15-zenmoney-money-system-intake.md`

## Open Questions

- Which accounts should be excluded from analysis?
- Which debts have mandatory monthly payments and due dates?
- Should business/project money be analyzed together with household money or as a separate contour?
- How should EUR/USD reserves be represented in monthly reports?
- What are the exact preferential mortgage terms, tax treatment, and owner-side коммуналка baseline after applying the 2-2.5K RUB/month realtor reimbursement rule for the Tyumen studio?
- What is the remaining cost-to-finish for the Berdsk country house?
- What are the mileage, configuration, condition, annual costs, and market valuation for the 2013 Volkswagen Tiguan?
- Credit-card evidence is restored enough for control: Gmail Trash contained the T-Bank statement; user provided current Sber bank-app values, though Sber amount may change with today's/future operations.
- What are the exact terms, due dates, grace-period status, and payoff priorities for all credit obligations?
