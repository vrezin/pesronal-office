# Design Company Signal Intake Orchestration

- Created: 2026-06-09
- Status: active
- Area: personal-office / companies / automation
- Related company index: `companies/ai-studio/active.md`

## Context

Personal Office needs a reusable way to process incoming company/project signals.

Example input:

> Dasha talked to a clinic about MedVoice and reports the result.

This must not become a Dasha-specific or MedVoice-specific workflow. Dasha is only an example of a human source. The real problem is a general intake and orchestration layer for company/project signals.

## Desired Outcome

Design and implement a workflow where a user can forward or dictate a company/project signal, and the system:

- captures raw input;
- extracts facts, decisions, people, risks, promises, deadlines, and next steps;
- creates Personal Office owner-level tasks, waiting items, calendar notes, and memory updates;
- routes official project/company facts to the correct company repository or company subsystem;
- emits a handoff/request for AI Studio, Fincom, or other company agents instead of directly editing their domain as if Personal Office owned it;
- supports future orchestration through n8n, Make, or another scheduler/orchestrator.

## Boundary

Personal Office should answer:

> What do I, as owner/founder/person, need to remember, decide, do, delegate, or wait for?

Company repositories and company agent systems should answer:

> What is the official project/company truth, and what should domain agents do with it?

## Design Questions

- What is the canonical artifact for a company/project signal in Personal Office?
- What is the handoff contract from Personal Office into AI Studio / ai-board / company subagents?
- Should handoffs be markdown files, JSON/YAML envelopes, Git commits, GitHub/Linear issues, n8n webhooks, Make scenarios, or a mix?
- How does the system avoid Personal Office directly becoming the source of truth for company projects?
- How does it track whether a company-side agent accepted, rejected, or needs clarification on the handoff?
- How should calendar events, tasks, and waiting items be created from the same signal?
- How should people/contact facts be stored without leaking unnecessary sensitive context?

## Candidate Architecture

1. `inbox/raw/` receives raw signal.
2. Personal Office signal router extracts owner-level facts and obligations.
3. Personal Office creates:
   - processed trace;
   - owner tasks;
   - waiting items;
   - calendar/meeting artifacts;
   - people/memory updates if needed.
4. Router emits company handoff envelope:
   - target company;
   - target project/domain;
   - signal summary;
   - extracted facts;
   - requested action;
   - urgency;
   - links to Personal Office context;
   - privacy/sensitivity level.
5. Company-side orchestrator or subagent consumes handoff and updates official project/company artifacts.
6. Personal Office records handoff status.

## Orchestration Candidates

- Local `codex exec` scheduled/triggered jobs for MVP.
- n8n for webhook/event routing, Gmail/Telegram/Calendar integrations, and visible workflow state.
- Make for lighter no-code glue if n8n is too heavy.
- Direct repo-file queue as the lowest-friction first version.

## First Implementation Slice

- Define a generic `company-signal-intake` skill.
- Define a machine-readable handoff envelope template.
- Add routing rules for company/project signals.
- Add an AI Studio handoff queue/index in Personal Office.
- Add an AI Studio-side receiving convention later, without hardcoding MedVoice or Dasha into the generic skill.

## Next Step

Draft the `company-signal-intake` skill and handoff envelope contract, then decide whether MVP handoff is repo-file queue, n8n webhook, or both.
