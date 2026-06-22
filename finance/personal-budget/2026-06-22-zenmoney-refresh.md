# 2026-06-22 - ZenMoney Finance Refresh

## Scope

Read-only refresh from ZenMoney for the Personal Office finance control layer.

This updates the 2026-06-15 initial snapshot. It is still not a single net-worth statement because several accounts remain business, family, stale, closed, or semantically unclear.

## Source Calls

- ZenMoney MCP `get_accounts`.
- ZenMoney MCP `get_budgets` for 2026-06-01..2026-06-30.
- ZenMoney MCP `get_transactions` for 2026-06-01..2026-06-22.
- Mode: read-only.
- Sensitive handling: account ids and transaction ids are intentionally not stored here.

## Freshness

The previous snapshot saw transactions only through 2026-06-10. This refresh returned transactions through 2026-06-21.

Interpretation:

- ZenMoney sync/API freshness looks usable again for current control.
- There were no transactions returned for 2026-06-22 at the time of the pull.
- Continue checking freshness during weekly finance review.

## June 2026 Budget

Visible June budget:

- income budget: `Зарплата` 1,065,641 RUB;
- visible planned expense budgets: about 648,124 RUB.

Largest planned expense blocks:

- `Дети`: 104,817 RUB;
- `Продукты`: 100,000 RUB;
- `Гашение кредита`: 87,950 RUB;
- `Автомобиль`: 87,348 RUB;
- `Школьные расходы`: 84,000 RUB;
- `Квартира (дом)`: 52,409 RUB;
- `Медицина`: 40,500 RUB;
- `Студия`: 25,000 RUB.

Interpretation:

- June budget is still a useful planning baseline, but it mixes family baseline, obligations, car, children, studio/property, and possible one-off items.
- The next useful artifact remains the category-to-management-bucket mapping.

## Account Role Highlights

Selected visible balances on 2026-06-22:

- family operating RUB cash: about 75.7K RUB across `Black Катя` and `МИР Сберкарта Катя`;
- personal visible RUB operating cash remains thin in ZenMoney: `Tinkoff. Debit RUB` about 14 RUB and `МИР Сберкарта` about 3.4K RUB;
- short-term savings / deposits: about 1.06M RUB in visible active RUB deposit/savings accounts;
- business/project Tochka balances: about 17.3K RUB across three active-looking duplicated `Счёт в банке Точка` accounts, still not safe to mix into household cash;
- foreign-currency reserve: about 15.3K EUR plus trivial USD balances;
- RUB investment accounts with positive balances: about 828.4K RUB before unresolved negative investment-like account treatment;
- active visible credit-card balances: Sber about -178.0K RUB, Tinkoff about -97.1K RUB;
- cash loan / consumer credit: about -3.315M RUB;
- unchanged stale/accounting artifacts still visible: `Долги` about -30K RUB and `Наличные Рубли` about -376K RUB.

Interpretation:

- Do not infer disposable cash from total positive balances.
- Family deposits, foreign currency, investments, business cash, and current operating cash must stay separated.
- The credit-card balances in ZenMoney are not the same thing as grace-period payments from the bank app/statement.

## Important June Transactions And Signals

Transactions returned for 2026-06-01..2026-06-22 include:

- 2026-06-03: Tyumen studio mortgage-like payment of 17,000 RUB and studio коммуналка-like expense of 932.19 RUB;
- 2026-06-04: cash loan payment of 70,450 RUB;
- 2026-06-16: rental income of 22,000 RUB;
- 2026-06-18: tax/fee payment to FNS of 16,067.62 RUB;
- 2026-06-21: latest visible transaction date, including groceries, pharmacy, transport, internet for parents, and a furniture/home purchase.

Recent 2026-06-15..2026-06-21 spending pattern:

- groceries and daily food;
- cafes/restaurants during travel or movement days;
- fuel and transport;
- medicine/pharmacy;
- home/furniture/building-store purchases;
- internet/mobile communication;
- one tax/fee payment.

## Credit And Obligation Control

Current ZenMoney balances:

- `Кредит наличными`: about -3.315M RUB;
- `Sber. Кредитка`: about -178.0K RUB;
- `Tinkoff. Кредитка`: about -97.1K RUB;
- `Ипотека студия`: positive 104.6K RUB, account semantics still unclear.

Known due-date control from previous evidence remains:

- Tinkoff/T-Bank credit card: pay 96,237 RUB by 2026-07-01 if preserving the interest-free period, unless bank app shows a newer corrected amount.
- Sber credit card: previous bank-app grace-preserving amount was 46,038.39 RUB by 2026-07-13, but the ZenMoney balance now shows a larger current balance. Recheck Sber bank app before deciding payment.
- Cash loan: recurring payment about 70.45K RUB, due around the 4th day of each month.
- Tyumen studio mortgage: recurring payment about 17-17.5K RUB/month; exact terms still missing.

## Open Items

- Recheck current bank-app grace-payment amounts for Sber and T-Bank before the July due dates.
- Confirm what `МИР Сберкарта` now represents, since it moved from zero/stale to a small active-looking balance after a subsidy transaction.
- Label the duplicated Tochka accounts so business/project cash can be separated cleanly.
- Confirm whether negative deposit/investment-like accounts are stale/closed artifacts or real obligations.
- Build category-to-management-bucket mapping and monthly close template.
