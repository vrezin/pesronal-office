# Yuliya Draft Bundle Path Validation Test

- Date: 2026-06-25
- OpenClaw session: `agent:default:yuliya-path-validation`
- Run id: `35f7a775-64b8-4a83-be4c-a4fb9a8a8229`
- Purpose: test whether the Raspberry Pi Personal Office router can validate previously proposed artifact paths against a narrow routing-map excerpt without repeating the full meeting analysis or applying changes.

## Input Given To Agent

Explicit handoff file copied into the Pi workspace:

- `handoffs/2026-06-25-yuliya-path-validation-routing-excerpt.md`

Source file in Personal Office:

- `tools/raspberrypi-openclaw/handoffs/2026-06-25-yuliya-path-validation-routing-excerpt.md`

The handoff excerpt contained:

- proposed Personal Office paths from the previous draft bundle test;
- proposed `<setronica-root>` handoff envelope paths;
- narrow routing rules from `secretaries/routing-map.md`;
- expected compact validation output contract.

## Prompt Constraint

The agent was instructed to:

- read only the one handoff file;
- avoid other raw/private directories;
- avoid writes and live apply;
- validate only proposed paths using the narrow routing rules;
- return a compact validation bundle;
- avoid repeating full meeting analysis.

## Result

Pass.

The agent returned a compact YAML validation bundle and did not repeat the full meeting analysis.

It classified:

- valid Personal Office paths:
  - `companies/setronica/active.md`
  - `companies/setronica/projects/2026-06-23-legacy-migration-modernization.md`
  - `people/contacts/yuliya-malinina.md`
  - `companies/future-companies/2026-06-21-private-ai-office-product-one-pager.md`
  - `tasks/active/2026-06-24-support-setronica-task-to-handoff-stage-2-proof-of-value.md`
- invalid path:
  - `content/personal-brand/setronica-publicity-guardrail.md`
- partial / requires explicit approval:
  - `<setronica-root>/engineering-task-to-handoff-standard/rollout-stages/stage-2/ru/reports/stage-2-proof-of-value-executive-summary.md`
  - `<setronica-root>/remote-landlord-migration-discovery/roundtable/one-page-summary-and-questions.md`

## Important Output

The invalid path was corrected to the route:

- `personal-projects/personal-brand/`

The agent correctly did not invent a deeper filename and marked the exact route as requiring user confirmation:

- `apply_status: blocked_until_route_confirmed`

For `<setronica-root>` paths, the agent marked:

- `route_valid: partial`
- `apply_status: draft_only_requires_explicit_user_approval`

## Good Behavior Observed

- It obeyed the narrow one-file context constraint.
- It stayed compact.
- It validated paths instead of redoing the meeting analysis.
- It caught the invalid `content/` top-level directory.
- It treated project-side `<setronica-root>` paths as handoff envelopes, not as automatic apply targets.
- It did not invent a filename for the public-content guardrail when the route was only partially known.

## Issue Found

The OpenClaw run still had a large injected prompt overhead from the default workspace/system context:

- agent-reported input: `1362`
- output: `1030`
- cache read: `17792`
- total: `20184`
- prompt tokens: `19154`

The task itself was compact, but the baseline agent harness remains heavy. Future optimization should look at the default workspace prompt, injected files, and enabled skills/tools.

## Assessment

This is the desired third-stage behavior: path validation as a narrow skill-like operation. The agent can correct routing after being given a small excerpt, while preserving the draft-only and approval-before-apply boundary.

## Next Useful Step

Add a reusable path-validation pattern to the Personal Office router cookbook/template:

- never propose unknown top-level directories;
- if a lane is valid but the exact path is unclear, return route-only with `blocked_until_route_confirmed`;
- require routing-map excerpt or explicit path confirmation before an apply-ready bundle;
- keep validation output compact.
