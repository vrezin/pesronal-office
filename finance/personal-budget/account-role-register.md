# Account Role Register

## Purpose

This register maps ZenMoney accounts into Personal Office management roles.

ZenMoney remains the source of account balances and transactions. This file defines how those accounts should be interpreted for budgeting, runway, obligations, investments, and decision-making.

## Last Read

- Date: 2026-06-22
- Source: ZenMoney MCP `get_accounts`
- Mode: read-only
- Sensitive handling: ZenMoney account ids are intentionally not stored here.

## Latest Refresh Notes

- Refresh artifact: `finance/personal-budget/2026-06-22-zenmoney-refresh.md`.
- ZenMoney balances were readable on 2026-06-22.
- Transactions are visible through 2026-06-21, so the earlier 2026-06-15 freshness concern about no transactions after 2026-06-10 is currently resolved.
- Do not treat this register as a single net-worth report; it is still a role/classification layer.

## Status Values

- `active` - should be included in reports for its assigned role.
- `needs clarification` - visible in ZenMoney, but interpretation is not safe yet.
- `stale/zero` - likely old, unused, or empty; exclude from decision reports unless reactivated.
- `closed/check` - appears closed or inconsistent; exclude until confirmed.
- `ignore unless needed` - technical/minor balance; do not use in high-level reports by default.

## Role Values

- `personal operating cash`
- `family operating cash`
- `business/project flow`
- `tax reserve`
- `debt`
- `credit card debt`
- `investment`
- `deposit/savings`
- `property/studio`
- `foreign-currency reserve`
- `cash`
- `technical/placeholder`
- `needs classification`

## Accounts

| Account | Currency | Current role | Status | Reporting treatment | Notes |
|---|---:|---|---|---|---|
| Black Катя | RUB | family operating cash | active | include in available family cash | Family/Katya-named daily balance. |
| МИР Сберкарта Катя | RUB | family operating cash | active | include in available family cash | Family/Katya-named daily balance. |
| Tinkoff. Debit RUB | RUB | personal operating cash | active | include in personal operating cash | Small balance, but active-looking daily account. |
| Копилка Сергей Р. | RUB | deposit/savings | active | include in short-term savings | User-named savings bucket. |
| Счёт в банке Точка | RUB | business/project flow | needs clarification | include only in business cash after confirmation | Multiple Tochka accounts share the same name; needs labeling. |
| Счёт в банке Точка | RUB | business/project flow | needs clarification | include only in business cash after confirmation | Multiple Tochka accounts share the same name; needs labeling. |
| Счёт в банке Точка | RUB | business/project flow | needs clarification | include only in business cash after confirmation | Multiple Tochka accounts share the same name; needs labeling. |
| Счёт в банке Точка | RUB | business/project flow | stale/zero | exclude until confirmed | Zero balance duplicate-looking Tochka account. |
| Точка. Основной счет | RUB | business/project flow | stale/zero | exclude until confirmed | Explicit Tochka account, zero balance. |
| Точка. Копилка на налоги | RUB | tax reserve | stale/zero | include in tax reserve only after reactivation | Tax reserve account exists but balance is zero. |
| Точка. Фонд 7% на налоги | RUB | tax reserve | stale/zero | include in tax reserve only after reactivation | Tax reserve account exists but balance is zero. |
| BoC. Main account | EUR | foreign-currency reserve | active | include in EUR reserve, not RUB cashflow by default | Significant EUR balance. |
| Наличные Евро | EUR | foreign-currency reserve | active | include in EUR reserve, not RUB cashflow by default | Cash EUR reserve. |
| Револют катя | EUR | foreign-currency reserve | ignore unless needed | include only in detailed FX view | Small family/Katya EUR balance. |
| Tinkoff. Debit EUR | EUR | foreign-currency reserve | ignore unless needed | include only in detailed FX view | Minor balance. |
| Tinkoff. Debit USD | USD | foreign-currency reserve | ignore unless needed | include only in detailed FX view | Minor balance. |
| LT373250095291778090 | USD | foreign-currency reserve | ignore unless needed | include only in detailed FX view | Minor balance; account label needs clarification if used. |
| Revolute. Main account EUR | EUR | foreign-currency reserve | stale/zero | exclude until confirmed | Zero balance. |
| Revolute. Main account UAE Dh | AED | foreign-currency reserve | stale/zero | exclude until confirmed | Zero balance. |
| LT373250095291778090 | TRY | foreign-currency reserve | stale/zero | exclude until confirmed | Zero balance. |
| LT373250095291778090 | GBP | foreign-currency reserve | stale/zero | exclude until confirmed | Zero balance. |
| VTB broker | RUB | investment | active | include in investment assets | Broker/investment account. |
| Zorko(IPO) | RUB | investment | active | include in investment assets | IPO/investment account. |
| Sber. Брокерский счёт | RUB | investment | active | include in investment assets | Small broker balance. |
| Tinkoff. Брокерский счёт | RUB | investment | stale/zero | exclude until confirmed | Zero balance. |
| Брокерский счёт 422UR1R | RUB | investment | stale/zero | exclude until confirmed | Zero balance. |
| Тинькофф тбанк инвестиции Катя | RUB | investment | needs clarification | exclude from net asset view until explained | Negative investment-like balance. |
| Invest | EUR | investment | stale/zero | exclude until confirmed | Zero balance. |
| Депозит т банк катя | RUB | deposit/savings | active | include in savings/deposits | Family/Katya-named deposit. |
| Т банк вклад на 2 месяца Катя | RUB | deposit/savings | active | include in savings/deposits | Family/Katya-named deposit. |
| Тбанк депозит катя 121000 | RUB | deposit/savings | active | include in savings/deposits | Family/Katya-named deposit. |
| Тинькоф депозит | RUB | deposit/savings | active | include in savings/deposits | Deposit account. |
| Тбанк закрытый депозит катя | RUB | deposit/savings | closed/check | exclude until explained | Name says closed; negative balance. |
| Точка Катя депозит | RUB | deposit/savings | needs clarification | exclude until explained | Deposit-like account with negative balance. |
| Точка депозит | RUB | deposit/savings | stale/zero | exclude until confirmed | Zero balance. |
| Накопительный счёт | RUB | deposit/savings | stale/zero | exclude until confirmed | Zero balance. |
| Сберегательный счет | RUB | deposit/savings | stale/zero | exclude until confirmed | Zero balance. |
| Кредит наличными | RUB | debt | active | include in liabilities and debt schedule | Large loan balance. See `finance/obligations/credit-obligations-register.md`. |
| Sber. Кредитка | RUB | credit card debt | active | include in liabilities and monthly obligations | Credit-card liability. See `finance/obligations/credit-obligations-register.md`. |
| Tinkoff. Кредитка | RUB | credit card debt | active | include in liabilities and monthly obligations | Credit-card liability. See `finance/obligations/credit-obligations-register.md`. |
| Долги | RUB | technical/placeholder | stale/accounting artifact | exclude from real liabilities | User confirmed there is no real debt like this; likely forgotten stale tracking item. See `finance/obligations/credit-obligations-register.md`. |
| Наличные Рубли | RUB | technical/placeholder | accounting/input error | exclude from available cash and real liabilities | User says this is likely an input/accounting error. See `finance/obligations/credit-obligations-register.md`. |
| Ипотека студия | RUB | property/studio debt/mortgage | needs clarification | exclude from net view until loan semantics confirmed; include recurring payment in obligations once terms are captured | Likely mortgage account for Tyumen studio. Cross-check with `finance/family-assets/real-estate-register.md` and `finance/family-assets/tyumen-studio-cashflow.md`. |
| Sber. Дебит | RUB | personal operating cash | stale/zero | exclude until confirmed | Zero balance. |
| МИР Сберкарта | RUB | personal operating cash | needs clarification | include only in detailed operating cash until confirmed | Small active-looking balance appeared after a 2026-06-17 subsidy transaction; confirm whether this account should be reactivated in reports. |
| Cashback Card MIR | RUB | personal operating cash | stale/zero | exclude until confirmed | Zero balance. |
| AIR MasterCard! | RUB | personal operating cash | stale/zero | exclude until confirmed | Zero balance. |
| Visa Platinum PREMIER Катя | RUB | family operating cash | ignore unless needed | exclude from high-level reports | Near-zero negative balance. |
| Мастер-счет в рублях | RUB | technical/placeholder | stale/zero | exclude until confirmed | Zero balance. |
| Текущий счет | RUB | technical/placeholder | stale/zero | exclude until confirmed | Duplicate generic name, zero balance. |
| Текущий счет | EUR | technical/placeholder | stale/zero | exclude until confirmed | Duplicate generic name, zero balance. |
| Текущий счет | RUB | technical/placeholder | ignore unless needed | exclude from high-level reports | Duplicate generic name, trivial balance. |
| Текущий счет | USD | technical/placeholder | stale/zero | exclude until confirmed | Duplicate generic name, zero balance. |
| Текущий счет "Клик" | USD | technical/placeholder | stale/zero | exclude until confirmed | Zero balance. |
| Сергей Резин | RUB | technical/placeholder | stale/zero | exclude until confirmed | Zero balance; may be legacy/person account. |
| Тинькофф Мобайл | RUB | technical/placeholder | stale/zero | exclude until confirmed | Zero balance; probably service account. |
| Обезлич. мет. счета (золото) | AUR | investment | stale/zero | exclude until confirmed | Metal account, zero balance. |
| Обезлич. мет. счета (серебро) | ARG | investment | stale/zero | exclude until confirmed | Metal account, zero balance. |
| Обезлич. мет. счета (платина) | PTR | investment | stale/zero | exclude until confirmed | Metal account, zero balance. |
| Обезлич. мет. счета (палладий) | PDR | investment | stale/zero | exclude until confirmed | Metal account, zero balance. |

## Immediate Reporting Rules

Until this register is confirmed:

- Do not produce a single net-worth number.
- Do not mix EUR/USD reserves into RUB monthly cashflow.
- Do not treat negative cash/deposit/investment-like balances as ordinary liabilities without clarification.
- Do not mix business/project Tochka balances into household cash.
- Include credit cards and the cash loan in obligations reporting.
- Treat family/Katya-named balances as family contour, not automatically personal disposable cash.

## Needs User Review

High-priority confirmations:

- Confirm whether `МИР Сберкарта` should move back from stale/zero into active personal operating cash.
- What are the exact terms and account semantics for `Ипотека студия`: outstanding principal, monthly payment, rate, maturity date, and why the ZenMoney account currently shows a positive balance?
- What are the exact terms and due dates for all credit obligations in `finance/obligations/credit-obligations-register.md`?
- Which Tochka accounts are active business/project accounts, and what should each be named?
- Should Katya-named deposits be counted in shared family savings, protected family reserve, or excluded from personal runway?
- Are `Тинькофф тбанк инвестиции Катя`, `Тбанк закрытый депозит катя`, and `Точка Катя депозит` real negative balances or stale/closed artifacts?
- Which zero accounts should be archived/ignored permanently?

## Next Registers

- Category-to-management-bucket mapping.
- Recurring obligations register.
- Monthly close template.
