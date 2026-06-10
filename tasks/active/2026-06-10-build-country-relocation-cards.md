# Build Country Relocation Cards

- Created: 2026-06-10
- Status: active
- Area: personal-projects / personal-brand / job-search economics
- Related workspace: `personal-projects/personal-brand/workspace/job-intake/relocation/`

## Context

Job intake already needs relocation-aware filtering, but the country economics are still spread across individual analyses.

We need a reusable country-card layer that can be refreshed periodically and reused in every vacancy decision.

## Desired Outcome

Create a stable relocation/card framework that lets us quickly compare:

- remote vs relocation;
- company-sponsored relocation vs self-relocation;
- rent;
- school fit for two daughters;
- safety;
- healthcare;
- education quality;
- one-time and monthly cost deltas.

New country rule:

- when a new country appears, create the card first;
- gather baseline figures from the internet immediately;
- store source URLs and retrieval date in the card;
- leave unknown numbers as `TBD`.

## Deliverables

1. `personal-projects/personal-brand/workspace/job-intake/relocation/README.md`
2. `personal-projects/personal-brand/workspace/job-intake/relocation/country-index.md`
3. `personal-projects/personal-brand/workspace/job-intake/relocation/country-card-template.md`
4. Country cards for the active relocation shortlist.
5. A repeatable update rule for monthly refreshes and pre-application refreshes.

## Next Step

Populate the first live country cards for Portugal, Cyprus, Hungary, and the Netherlands, then wire the new filter into job-intake analysis notes and rules.
