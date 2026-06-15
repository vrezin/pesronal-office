# Real Estate Register

## Purpose

Family real-estate asset register for Personal Office.

This file is the management view of family property. It is not a legal title register, cadastral extract, or formal appraisal.

## Last Updated

- Date: 2026-06-15
- Source types:
  - user-provided family asset facts;
  - local country-house materials;
  - public market references for preliminary valuation ranges.

## Valuation Confidence

- `user estimate` - value supplied by user, not externally validated.
- `market range` - public listing market used for rough range.
- `unknown` - not enough facts for useful valuation.
- `needs formal appraisal` - should be appraised by real-estate professional or formal service before high-stakes decisions.

## Assets

| Asset | Location | Type | Key facts | Preliminary value | Confidence | Treatment |
|---|---|---|---|---:|---|---|
| Novosibirsk apartment | Novosibirsk, Sirenevaya 29, apt. 33 | 3-room apartment | 118 sq m; renovation is tired and likely needs cosmetic refresh, but not emergency-level condition. | 13-18M RUB working range | market range, needs formal appraisal | Include as family real-estate asset; do not treat as liquid. |
| Berdsk country house | Berdsk, ZhSK Novy 2 | House + land plot | Profiled cedar timber; current readiness tracked in country-house control layer; electricity, cold water, sewerage and gas are brought to the plot; approximately 10 minutes walking distance to Ob Bay shore. | 12M RUB working estimate | user estimate, needs formal appraisal | Include as family real-estate asset under construction / incomplete readiness. |
| Tyumen studio apartment | Tyumen, Novgorodskaya 96, apt. 111 | Studio apartment | Small studio, approximately 24 sq m; fresh/new building likely built in 2024 or 2025; renovation completed in the past winter; 100% ownership; preferential/subsidized mortgage; transferred to realtors for rental management; contractual rent is 22K RUB/month; realtors usually reimburse 2-2.5K RUB/month for коммуналка. | 3-4.5M RUB working range | income-supported rough estimate, needs market appraisal | Track as positive strategic asset: subsidized mortgage plus rental offset. Report gross rent, mortgage offset, коммуналка reimbursement, and reconciled net cashflow separately. |
| Garage near Sirenevaya | Novosibirsk, Sirenevaya 29, next to apartment entrance | Garage / self-built structure | About 6 x 4 m; sandwich-panel construction; good physical condition; electricity available; no security; physically very convenient for residents of the same building; legal status is not permitted / self-built, one of about 15 similar structures near the house; practical use right is transferable, but most likely as part of the Sirenevaya apartment package. | 0.8M RUB working estimate | user estimate, legal risk but low practical demolition risk | Treat primarily as value enhancer for the Sirenevaya apartment; avoid double-counting as separate liquid real estate. |

## Source Notes

### Novosibirsk Apartment

User facts:

- 3-room apartment;
- 118 sq m;
- renovation is old/tired and cosmetic renovation would already be desirable;
- located at Novosibirsk, Sirenevaya 29, apt. 33.

Public market reference:

- Yandex Realty public listing page for 3-room apartments in Novosibirsk showed 7,270 active listings, with overall price-per-square-meter range from 45,290 to 505,882 RUB and examples around 103-126.5 sq m listed at 18.2-21.7M RUB.
- Because this is not an exact-address appraisal and the apartment needs cosmetic refresh, the working range is set conservatively at 13-18M RUB.

Source URL:

- `https://realty.yandex.ru/novosibirsk/kupit/kvartira/tryohkomnatnaya/`

### Berdsk Country House

User facts:

- profiled cedar timber house;
- located at Berdsk, ZhSK Novy 2;
- house is on its own land plot in the practical sense relevant for family asset tracking;
- electricity, cold water, sewerage and gas are brought to the plot;
- approximately 10 minutes walking distance to Ob Bay shore;
- user working estimate: about 12M RUB.

Local source:

- `life/home-family-rest/country-house/control/source-data.md`
- `life/home-family-rest/country-house/control/current-plan.md`

Current status from local control layer:

- country-house source materials include project PDFs, estimates, Blender models and rendered outputs;
- current work is still active around water connection and temporary sanitary/water setup;
- therefore the object should be treated as property under construction / incomplete readiness, not as a fully finished liquid residential asset.

Public market reference:

- Yandex Realty public listing page for houses in Berdsk showed 485 active listings and confirms that common search attributes include electricity, heating, communications, gas, timber houses, and proximity to water.
- The public page has a very wide price-per-square-meter spread and does not substitute for an appraisal of this specific unfinished object.

Source URL:

- `https://realty.yandex.ru/berdsk/kupit/dom/`

### Tyumen Studio Apartment

User facts:

- family has a small studio apartment in Tyumen;
- address: Tyumen, Novgorodskaya 96, apt. 111;
- approximate area: about 24 sq m;
- building is fresh/new, likely built in 2024 or 2025;
- renovation was completed in the past winter;
- ownership share: 100%;
- apartment is mortgaged; mortgage is preferential/subsidized; exact mortgage terms are not yet captured, but mortgage-like payments are visible in ZenMoney under `Студия`;
- transferred to realtors who rent it out;
- contractual rent: 22K RUB/month;
- under the current arrangement, the family receives the contractual rent from the rental operator/realtors; how much they collect from end tenants is their operating concern;
- utility expenses by meters are on the operator/tenant side;
- non-metered communal expenses are on the family side;
- wife confirmed that realtors usually reimburse 2-2.5K RUB/month for коммуналка;
- these reimbursements must be matched before calculating net cashflow;
- actual net monthly amount fluctuates because additional expenses periodically arise.

Missing facts:

- exact building year;
- exact mortgage terms;
- typical monthly additional expenses;
- actual net cashflow history.

Related cashflow note:

- `finance/family-assets/tyumen-studio-cashflow.md`

Public market reference:

- Yandex Realty public listing page for studios in Tyumen showed 6,649 active listings, with overall price-per-square-meter range from 49,375 to 387,931 RUB.
- Exact-address public lookup did not produce a reliable valuation card in the current pass.
- With about 24 sq m, a fresh building, completed renovation and contractual rent of 22K RUB/month, the working valuation range is set at 3-4.5M RUB until a more direct market check or appraisal is done.

Source URL:

- `https://realty.yandex.ru/tyumen/kupit/kvartira/studiya/`

### Garage Near Sirenevaya

User facts:

- garage at Novosibirsk, Sirenevaya 29, physically next to the apartment entrance;
- very convenient location for residents of the same building, which increases practical value for a narrow buyer/user group;
- legal status: not a permitted/authorized structure; effectively self-built;
- there are about 15 similar structures near the house;
- approximate area: about 6 x 4 m;
- construction: sandwich panels;
- physical condition: good;
- electricity: available;
- security: none;
- practical demolition/removal risk: low under current conditions; the main plausible trigger would be construction in the nearby forest area, but that is unlikely because of major communications constraints;
- practical transferability: transferable, but most likely as part of the Sirenevaya apartment package rather than as a clean independent market sale;
- user working estimate: about 800K RUB.

Missing facts:

- none material for current management view.

Public market reference:

- Yandex Realty public listing page for garages in Novosibirsk showed 441 active listings, with broad market dispersion.
- Examples in the public listing include garage offers in the hundreds of thousands to around 1M RUB in ordinary segments, so the 800K RUB working estimate is plausible but not confirmed.
- Because this garage is not normal titled real estate, public garage listings are only a weak price reference. The asset has legal and liquidity risk and should not be valued like a registered owned garage. Operationally, however, the practical demolition risk is currently assessed as low by the user.

Source URL:

- `https://realty.yandex.ru/novosibirsk/kupit/garazh/`

## Current Working Asset View

Known preliminary values:

- Novosibirsk apartment: 13-18M RUB working range.
- Berdsk country house: 12M RUB working estimate.
- Tyumen studio apartment: 3-4.5M RUB working range.
- Garage near Sirenevaya: 0.8M RUB working estimate.

Blocked valuation:

- none fully blocked, but all values remain preliminary and non-formal.

Counting rule:

- The garage can be tracked as a separate useful asset, but for family balance-sheet purposes it should usually be treated as part of the Sirenevaya apartment value package to avoid double-counting.

Do not produce a final family balance sheet until:

- Tyumen studio net cashflow, recurring expense pattern, and 2-2.5K RUB/month коммуналка reimbursement matching are added;
- ownership and encumbrance/mortgage facts are checked;
- the Novosibirsk apartment is appraised more directly;
- country house completion status and remaining cost-to-finish are estimated.

## Next Questions

- What are the exact building year, preferential mortgage terms, recurring owner-side коммуналка above/below the 2-2.5K RUB reimbursement, actual rent receipt history and tax treatment for the Tyumen studio?
- Is the Novosibirsk apartment mortgage-free?
- Is the Berdsk land registered as ownership, long-term lease, СНТ/ЖСК membership, or another legal form?
- What is the remaining cost-to-finish for the Berdsk house?
- Should these assets be treated as shared family assets or split by legal owner?
