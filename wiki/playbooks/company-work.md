# Company Work Playbook

## Scope

Use for AI Studio, Fincom, Setronica, MedVoice management context, contracts, people, company signals, and owner-level obligations.

## Boundary

Personal Office tracks:

- owner decisions;
- tasks and waiting items;
- people and relationship context;
- contract pointers/copies;
- handoff requests to company/project systems.

Company repositories track official company/project truth.

## Company Signal Intake

For signals such as "someone talked to a client/clinic/partner":

1. Capture raw/processed trace.
2. Extract facts, decisions, risks, people, dates, promises, and next steps.
3. Create Personal Office tasks/waiting/calendar/people updates.
4. Emit a handoff artifact for the target company/project instead of directly owning company truth.
5. Track whether the handoff was accepted, rejected, or needs clarification.

## Known Workspaces

- AI Studio: `<aistudio-root>` and `companies/ai-studio/`.
- Fincom: `<fincom-root>` and `companies/fincom/`.
- Setronica: `<setronica-root>` and `companies/setronica/`.
