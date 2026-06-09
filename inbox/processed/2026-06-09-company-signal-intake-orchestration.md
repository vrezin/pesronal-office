# Company Signal Intake Orchestration

Date: 2026-06-09

## Input

The user wants to handle a scenario where someone reports a company/project update, for example:

> Dasha talked to a clinic about MedVoice and reports the result.

The workflow should not be Dasha-specific or MedVoice-specific. AI Studio has its own ai-board and potential subagents, so Personal Office should route and hand off company signals rather than owning the full company/project truth.

## Decision

Create an implementation task for a generic company/project signal intake and orchestration layer.

The design should include:

- Personal Office owner-level extraction;
- official company/project handoff;
- company-side agent compatibility;
- calendar/task/waiting/memory routing;
- possible n8n or Make orchestration.

## Created Artifacts

- `tasks/active/2026-06-09-design-company-signal-intake-orchestration.md`
