# Tyumen Studio Cashflow

## Scope

Cashflow note for the Tyumen studio apartment.

This is a management view based on user-provided facts and ZenMoney read-only transaction checks. It is not a formal accounting statement.

## Asset Link

- Real-estate register: `finance/family-assets/real-estate-register.md`
- Related ZenMoney account: `Ипотека студия` in `finance/personal-budget/account-role-register.md`

## Property Facts

- Address: Tyumen, Novgorodskaya 96, apt. 111.
- Type: small studio apartment.
- Area: approximately 24 sq m.
- Ownership share: 100%.
- Building: fresh/new building, likely built in 2024 or 2025.
- Renovation: completed in the past winter.
- Encumbrance: mortgage, exact terms not yet captured.
- User recalls the mortgage rate is about 6%.

## Rental Model

- The apartment is handed over to realtors / rental operators.
- Contractual payment to the family: 22K RUB/month.
- The operator's actual rent collected from tenants is not the family's operating concern under the current arrangement.
- Utility expenses by meters are on the rental operator/tenant side.
- Non-metered communal expenses are on the family side.
- Wife confirmed that realtors usually reimburse 2-2.5K RUB/month for communal expenses.
- Actual net cashflow fluctuates because additional expenses periodically arise.
- Strategic framing: the deal was considered successful/positive because the mortgage is preferential/subsidized and the rental payment at least partially offsets the mortgage payment while the family keeps the asset.

## ZenMoney Evidence

### Rental Income

ZenMoney category checked: `Студия / Доход от аренды`.

Observed receipts:

- 2026-02: 18,678 RUB.
- 2026-03: 23,976 RUB.
- 2026-04: 22,000 RUB.
- 2026-05: 18,778 RUB.

Observed average for 2026-02..2026-05: about 20.9K RUB/month.

Interpretation:

- The 22K RUB/month contract is a useful gross baseline.
- Actual received monthly amount should be reported separately as observed net/gross receipt because it varies.
- The correct success metric is not pure monthly profit. The first metric is mortgage offset under a preferential loan.

### Mortgage / Studio Payments

ZenMoney parent category checked: `Студия`.

Observed mortgage-like payments:

- 2025-12: 17,300 RUB.
- 2026-02: 17,000 RUB.
- 2026-03: 17,500 RUB.
- 2026-04: 17,500 RUB.
- 2026-05: 17,500 RUB transfer line visible under `Студия`.

Interpretation:

- Treat the mortgage as a recurring obligation of about 17-17.5K RUB/month until exact loan terms are captured.
- User recalls the rate is about 6%.
- The mortgage account/loan terms should be confirmed from account data or loan documents.

### Communal / Owner Expenses

ZenMoney categories checked:

- `Студия / коммунальные платежи`;
- parent `Студия`.

Observed owner-side communal or utility-like expenses:

- 2026-04: 3,421.35 RUB to `АО "ТРИЦ"`.
- 2026-04: 1,800 RUB to `ООО УК Правый берег`.
- 2026-04: 62.70 RUB to `AO "Gazprom energosbyt"`.
- 2026-05: 3,244.54 RUB to `АО "ТРИЦ"`.
- 2026-05: 921.81 RUB to `ООО УК Правый берег`.

Interpretation:

- Owner-side non-metered communal expenses appear material and must be deducted from rental receipts.
- Exact split between metered tenant/operator-paid and non-metered owner-paid costs should be captured.
- коммуналка deduction should be net of realtor reimbursements.
- Confirmed working rule: realtors usually reimburse 2-2.5K RUB/month for communal expenses.

### Possible Communal Reimbursements

ZenMoney category checked: `Возврат затрат`.

Candidate reimbursements near the observed communal-payment period:

- 2026-04-10: +2,500 RUB.
- 2026-04-12: +1,000 RUB.
- 2026-04-21: +1,000 RUB.
- 2026-04-23: +3,000 RUB.
- 2026-05-15: +3,600 RUB.

Interpretation:

- 2-2.5K RUB incoming payments from realtors/wife's accounts should be treated as коммуналка reimbursement candidates by default.
- Larger or differently described `Возврат затрат` payments need manual review before assigning them to the studio.
- The studio cashflow model should include a reconciliation step: match owner-side communal expenses to nearby 2-2.5K RUB incoming reimbursements before treating коммуналка as a family net cost.

### Renovation / Capital Expenses

ZenMoney exact subcategory `Студия / Ремонт` had no transactions in the checked period.

However, parent category `Студия` contains repair/capital-looking expenses in 2025-10..2025-12 and a later capital purchase:

- 2025-10..2025-12: multiple `Студия` payments to Екатерина Р. / anonymous payees, totaling roughly 65K RUB in the checked output.
- 2026-04: 23,700 RUB to `ООО "ЛИГАСТРОЙ 72"` for air conditioner.

Interpretation:

- Renovation costs were likely categorized under parent `Студия`, not the child `Ремонт` tag.
- For clean analysis, historical studio renovation/capital expenses should be separated from recurring operating expenses.

## Working Monthly Model

Preliminary recurring model:

- Contractual rent: 22K RUB/month.
- Observed receipt average: about 20.9K RUB/month for 2026-02..2026-05.
- Mortgage obligation: about 17-17.5K RUB/month observed.
- Owner-side communal expenses: variable; observed April-May owner-side коммуналка/utilities about 4.2-5.3K RUB/month before classification cleanup.
- Realtor коммуналка reimbursement: working rule 2-2.5K RUB/month.

Current implication:

- Gross rent covers a large part of the observed mortgage payment.
- The deal remains strategically positive if the preferential mortgage economics and asset ownership are the main point.
- Net monthly cashflow should be calculated after applying the 2-2.5K RUB/month коммуналка reimbursement rule.
- Do not classify the studio as a negative cashflow asset until reimbursement matching is done.

## Open Questions

- Exact mortgage terms: outstanding principal, rate, monthly payment, maturity date, early repayment rules.
- Exact recurring owner-side коммуналка baseline.
- Match коммуналка payments to incoming 2-2.5K RUB reimbursement transactions on wife's accounts.
- Whether the 22K RUB/month contractual amount is guaranteed regardless of tenant vacancy.
- Whether renovation/capital expenses are complete or more finishing costs remain.
- Tax treatment for rental income.
