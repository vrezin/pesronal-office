# 2026-06-15 - ZenMoney Initial Snapshot

## Scope

Read-only initial snapshot from ZenMoney for designing the Personal Office money system.

This is not a final net-worth statement. ZenMoney currently contains mixed currencies, duplicate-looking accounts, historical or placeholder accounts, family accounts, business-related categories, investments, deposits, debts, and transfers. The first useful step is classification, not a single headline number.

## What Is Visible

### Accounts

ZenMoney exposes many active accounts across RUB, EUR, USD and a few other currencies.

Visible groups:

- day-to-day RUB cards and current accounts;
- family/Katya-named cards and deposits;
- foreign-currency liquidity, especially EUR bank and cash balances;
- broker and investment accounts;
- deposits and savings accounts;
- credit cards and loan/debt accounts;
- business-looking Tochka accounts;
- closed, zero, duplicate-looking, or placeholder accounts.

Important visible obligations and risk markers:

- a large cash loan balance;
- credit-card balances;
- a generic debt account;
- a negative RUB cash account that needs explanation;
- negative or closed deposit/investment-like accounts that should not be interpreted before cleanup.

### Categories

The category tree is rich enough for budgeting and analysis, but it is not yet a clean management taxonomy.

Useful existing areas:

- family baseline: food, children, home, medicine, transport, car;
- obligations: loan repayment, banking costs;
- income: salary, business/project income, investment income, rental income;
- assets and capital: investments, studio, home/construction;
- business/project categories: Fincom and other project-related buckets.

Cleanup needed:

- duplicate or near-duplicate categories, for example logoped-related categories;
- categories that mix income and expense semantics;
- overlap between business income, investment income, and personal income;
- project/business categories mixed into personal spending analysis.

### June 2026 Budget

ZenMoney has a June 2026 income budget for salary of about 1.066M RUB.

Visible planned expense budgets add up to roughly 631K RUB before any deeper validation. The largest visible blocks are:

- food;
- children and school-related expenses;
- car;
- loan repayment;
- home/apartment;
- medicine;
- studio;
- transport and smaller lifestyle categories.

This looks like a useful starting budget, but it should be reconciled against actual recurring obligations and account roles.

### Recent Transactions

For 2026-06-01..2026-06-15, ZenMoney returned recent June transactions, but the latest visible transaction in the sampled result is 2026-06-10.

Visible month-to-date patterns:

- frequent groceries and daily household spending;
- pharmacy/medicine spending;
- home/furniture/building-store purchases;
- regular loan repayment;
- own-account transfers;
- one unclear person/payee expense that needs classification.

The absence of visible transactions after 2026-06-10 may mean either no synced transactions, no actual transactions, or an API/sync/window issue. Treat freshness as unverified.

## First Interpretation

ZenMoney is already a useful source of transaction facts, budgets, categories and balances.

But Personal Office should not simply mirror ZenMoney. It needs a higher-level financial control layer:

- which money is personal operating cash;
- which money is family operating cash;
- which money belongs to business/project flow;
- which balances are investments or long-term assets;
- which balances are debts and obligations;
- which accounts are stale, duplicate, closed or placeholders;
- which categories are decision categories rather than raw transaction labels.

## Proposed Personal Office Money Model

### 1. Source Layer

ZenMoney remains the transaction source:

- account balances;
- transactions;
- categories;
- monthly budgets.

Default access mode: read-only.

### 2. Normalization Layer

Personal Office should maintain lightweight registries:

- account role register: operating cash, family, business, tax reserve, debt, investment, property/studio, foreign-currency reserve, stale/ignore;
- category mapping: ZenMoney categories mapped into management buckets;
- recurring obligations register: loan payments, credit cards, rent/studio, subscriptions, school/children, taxes, insurance;
- data-quality notes: duplicates, unclear negative balances, stale sync, unclassified payees.

### 3. Control Layer

Monthly views should answer:

- how much cash is actually available for the month;
- what is committed already;
- what is debt service;
- what must be reserved for taxes or business obligations;
- what is family baseline spend;
- what is discretionary;
- what is investment/capital movement rather than spend;
- where the next financial decision or risk is.

### 4. Rituals

Suggested operating rhythm:

- weekly 15-minute cleanup: new transactions, unknown payees, sync freshness, credit-card and cash mismatches;
- monthly close: actual vs budget, debt movement, cash runway, tax reserve, next-month commitments;
- decision notes: any large purchase, loan, investment, tax move, relocation cost, business cashflow decision, or family asset decision gets a separate finance artifact.

## Open Questions

- Which accounts are real active accounts and which should be ignored as historical, duplicate, closed, or placeholder?
- Which accounts belong to personal, family/Katya, business, investment, debt, tax, or property/studio contours?
- Why is there a negative RUB cash balance?
- Are transactions after 2026-06-10 missing because of sync delay, API behavior, or no activity?
- What is the intended currency policy for EUR/USD balances: store as reserve, convert to RUB view, or keep separate?
- Which ZenMoney categories should be treated as true recurring baseline and which are one-off/capital/project categories?
- What debt schedule and minimum-payment rules should be tracked outside raw transactions?

## Next Action

Create the account role register first. Without it, any automatic net-worth, budget, runway, or cashflow conclusion will be unreliable.
