# Yuliya Draft Bundle Path Validation Routing Excerpt

- Date: 2026-06-25
- Purpose: narrow routing-map excerpt for validating paths proposed by the Raspberry Pi OpenClaw Personal Office router.
- Apply policy: validation only. Do not write or apply live Personal Office or `<setronica-root>` artifacts.

## Source Test

Previous draft bundle session:

- `agent:default:yuliya-draft-patch-bundle`
- Run id: `1abe2fc0-e8c4-4ebb-bd78-535547edfafd`

Previous test result:

- The bundle correctly used `patch_bundle.status: draft_only`.
- The bundle correctly separated Setronica Stage 2, Remote Landlord / ManageGo, Yuliya contact context, Private AI Office product feedback, public-content guardrails, and weekly status routine.
- One proposed path was invalid for the current Personal Office repository map: `content/personal-brand/setronica-publicity-guardrail.md`.

## Proposed Paths To Validate

Personal Office proposed paths:

- `companies/setronica/active.md`
- `companies/setronica/projects/2026-06-23-legacy-migration-modernization.md`
- `people/contacts/yuliya-malinina.md`
- `companies/future-companies/2026-06-21-private-ai-office-product-one-pager.md`
- `tasks/active/2026-06-24-support-setronica-task-to-handoff-stage-2-proof-of-value.md`
- `content/personal-brand/setronica-publicity-guardrail.md`

Setronica handoff envelope paths:

- `<setronica-root>/engineering-task-to-handoff-standard/rollout-stages/stage-2/ru/reports/stage-2-proof-of-value-executive-summary.md`
- `<setronica-root>/remote-landlord-migration-discovery/roundtable/one-page-summary-and-questions.md`

## Narrow Routing Rules

Use only these route rules for this validation test:

- Setronica, agentic-first development, SOW, CSA contract, and Setronica work artifacts route to `companies/setronica/` for owner-level Personal Office state.
- Detailed Setronica execution artifacts route to `<setronica-root>` through handoff envelopes and require explicit user approval.
- New business / future company / product opportunity routes to `companies/future-companies/`.
- People, contacts, relationship context, public/private context, inferences, open questions, and follow-ups route to `people/`.
- Promises, next actions, deadlines, dependencies, and waiting states route to `tasks/active/` or `tasks/waiting/`.
- Personal brand, public positioning, CV, HH, career positioning, and public writing guardrails route to `personal-projects/personal-brand/`.
- If a proposed path starts with an unknown top-level directory, mark it invalid and propose the closest valid route, but do not invent a deeper filename unless enough context exists.
- If a lane is real but the exact path is unclear, mark `route_valid: partial`, ask a user question, and set `apply_status: blocked_until_route_confirmed`.

## Expected Output

Return a compact validation bundle, not a full new routing analysis.

For each proposed path include:

- `original_path`
- `route_valid`: `yes`, `no`, or `partial`
- `corrected_path_or_route`
- `reason`
- `owner_contour`
- `apply_status`

Also include:

- `invalid_paths`
- `paths_requiring_user_confirmation`
- `compact_patch_bundle_status`
- `human_summary`
