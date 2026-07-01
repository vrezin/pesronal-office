# Personal Office Minimal Context Pack

- Created: 2026-06-25
- Purpose: give the Raspberry Pi OpenClaw agent enough non-sensitive orientation to route requests without pretending it knows the full Personal Office world.
- Audience: `default` / `po-router` OpenClaw agents running from the cookbook-only bundle.

## Status

This is a context map, not a data mirror.

It may be used for routing, clarification, and patch drafting. It must not be treated as current source truth for private facts, finances, health, relationships, contracts, meetings, or project internals.

## Prime Model

Personal Office is the owner-side operating system for:

- personal life and family matters;
- work and company obligations;
- projects and project contours;
- people and relationships;
- money and obligations;
- decisions, risks, ideas, memory, and next actions.

The agent should convert messy input into structured context, then decide whether it can draft from the provided input or must request a narrow context handoff.

## What The Agent Knows Up Front

Known from cookbooks:

- repository routing protocol;
- artifact locations and naming rules;
- Personal Office versus project-workspace boundary;
- known high-level route aliases;
- safe/unsafe access boundaries;
- extraction schema for facts, hypotheses, ideas, weak signals, risks, people, projects, and next actions.

Not known from cookbooks:

- current private facts;
- current personal commitments;
- current people/contact details;
- live finance, health, calendar, inbox, memory, or company internals;
- whether an old project state is still true.

If a response needs these, request a narrow context handoff.

## Route Aliases

Use these as starting points, not as proof that a route is final.

| Alias / signal | Likely contour | Owner-side Personal Office route | Project/source truth |
|---|---|---|---|
| Personal Office / intake / routing / tasks / memory / wiki | Personal Office itself | relevant `inbox/`, `tasks/`, `wiki/`, `memory/`, `tools/` artifact | `<repo-root>` after explicit handoff |
| AI Studio | AI Studio company contour | `companies/ai-studio/` management trace | `<aistudio-root>` |
| MedVoice | AI Studio project/product contour | `companies/ai-studio/` owner trace and handoff | `<aistudio-root>` |
| Fincom / FinSOK | Fincom company contour | `companies/fincom/` management trace | `<fincom-root>` |
| Setronica / agentic-first development / SOW / CSA / Task-to-Handoff | Setronica work contour | `companies/setronica/` owner trace and handoff | `<setronica-root>` |
| Career / HH / CV / vacancies / personal brand | Personal brand contour | `personal-projects/personal-brand/` | Personal Office after explicit handoff |
| Profi.ru / personal consulting | Personal opportunity contour | `personal-projects/profi-ru/` or `personal-projects/consulting/` | Personal Office after explicit handoff |
| New sustained activity / new project / new business | Project bootstrap contour | owner envelope first, then optional project space | user-confirmed project path or generated contour |
| Person / relationship / intro / promise involving a person | People contour plus target domain | `people/contacts/` plus task/company/project artifact | Personal Office after explicit handoff |
| Automation / cron / monitors / local tools / MCP | Tools/automation contour | `tools/` and/or `automation/` | Personal Office tools area |

## Boundary Rules

Personal Office keeps:

- owner intent;
- route and management state;
- cross-project memory;
- people and relationship pointers;
- obligations, decisions, risks, and waiting state;
- handoff envelopes.

Project workspaces keep:

- implementation truth;
- source code;
- project-local specifications;
- deep domain artifacts;
- project execution state.

Do not mirror project internals into Personal Office. Do not push Personal Office private concerns into company repositories.

## Mixed-Context Meeting Pattern

One source can produce several routes.

A meeting, transcript, email thread, or messy note may contain multiple independent lanes. Do not force the whole source into a single route just because one company, person, or project is prominent.

For each meaningful lane, identify:

- topic;
- owner contour;
- what stays in Personal Office;
- what belongs in a project/company workspace;
- people involved;
- facts and evidence;
- hypotheses or weak signals;
- next action;
- missing context;
- target artifact or "no artifact yet".

If lanes may be mixed, split first and route second.

Example pattern:

```yaml
source:
  type: meeting
  summary:
lanes:
  - topic: Setronica execution / legacy migration
    owner_contour: Setronica work contour
    personal_office_role: owner obligations, meeting trace, waiting items, people, handoff state
    project_workspace_role: technical discovery, client-facing project prep, implementation truth
  - topic: Private AI Office product feedback
    owner_contour: unresolved personal/product/future-solution contour
    personal_office_role: product insight, hypothesis update, possible future contour decision
    project_workspace_role: none unless a project contour is explicitly created
  - topic: public writing / personal brand
    owner_contour: personal brand/content contour
    personal_office_role: guardrails, content ideas, approval constraints
    project_workspace_role: none unless a separate content project exists
```

If the agent suspects it has mixed unrelated lanes, it should say so and ask the user to confirm the split before drafting or applying changes.

## Validator Is Not Owner Contour

A person, company, customer, partner, or project can validate an idea without owning that idea's route.

Treat validators as evidence sources, relationship context, market signals, or channel hypotheses unless the user explicitly says they own, sponsor, fund, or operate the work.

Do not route an idea into a company's contour merely because someone from that company reacted to it.

Use this distinction:

```yaml
validator_context:
  person_or_company:
  what_they_validated:
  evidence_from_input:
  confidence:
owner_contour:
  current:
  status: confirmed|unresolved|needs_user_decision
  why:
must_not_assume:
  - validator owns the project
  - validator's company is the source of truth
  - product feedback belongs inside the validator's company workspace
```

If owner contour is unclear, keep it unresolved and ask the user.

## Existing Project Contours

### AI Studio / MedVoice

Use for AI Studio management attention and MedVoice owner-side routing.

Personal Office role:

- track owner obligations, follow-ups, people, and handoff state;
- preserve business/product signals that affect the user;
- route official product/project work to `<aistudio-root>`.

Do not assume current MedVoice implementation state from this pack.

### Fincom / FinSOK

Use for Fincom management attention, presale, customer signals, company obligations, and handoffs.

Personal Office role:

- capture owner-side signals, obligations, and next actions;
- keep management trace in `companies/fincom/`;
- route official company/project work to `<fincom-root>`.

If an opportunity could be Fincom, personal consulting, or research, stop for clarification.

### Setronica

Use for Setronica contract/work context, agentic-first development, Task-to-Handoff, Stage 1 / Stage 2, SOW / CSA, and related owner obligations.

Personal Office role:

- keep contract pointers, owner obligations, current-stage summaries, people, and handoff envelopes;
- route implementation/spec/project truth to `<setronica-root>`;
- use Setronica-style source -> understanding -> specification -> evidence -> handoff discipline when generating new project spaces.

## Unknown Or New Contours

If the input implies a project/business/customer route that is not listed:

1. Extract what is known.
2. Identify plausible contours.
3. Ask whether to create a new contour, hold it inside Personal Office, or park/close it.
4. If useful, draft an owner-level project/activity envelope.

Never invent a project route just because the input resembles a known contour.

## Intake Extraction Contract

For messy input, separate:

- facts with confidence/evidence level;
- hypotheses;
- feelings / intuitions / weak signals;
- ideas;
- risks;
- opportunities;
- people and relationship context;
- project/business/customer links;
- decisions, promises, dates, deadlines, tasks, and waiting items.

Facts must be grounded in the user input or handed context. Hypotheses and weak signals must be labeled as such.

## Context Handoff Request Contract

When context is missing, ask for the smallest useful handoff.

Detailed template: `tools/raspberrypi-openclaw/templates/narrow-context-handoff-template.md`.

Use this shape:

```yaml
related_context_to_request:
  - why_needed:
    preferred_source:
    minimum_fields:
    safe_alternative_if_not_available:
blocked_until:
  - exact missing fact or decision
must_not_do_yet:
  - action that would be unsafe or speculative
```

Good handoff requests:

- "Please provide the owner-level active summary for `companies/ai-studio/`, not the whole AI Studio repo."
- "Please provide the contact dossier summary for this person, not the full `people/` directory."
- "Please provide the current task/waiting items linked to this topic."
- "Please confirm whether this belongs to Fincom, personal consulting, or a new research contour."

Bad handoff requests:

- "Give me the whole repo."
- "Let me inspect all people/finance/calendar folders."
- "I will assume this belongs to Fincom."

## Output Contract

For non-trivial requests, return:

```yaml
route:
facts:
hypotheses:
ideas:
weak_signals:
risks:
people:
project_or_business_links:
related_context_to_request:
target_artifact:
next_action:
open_questions:
can_draft_patch_from_current_input: true|false
```

If the user asks for a direct answer and no artifact is needed, keep the same discipline but answer briefly.

## Draft Patch Bundle Contract

When asked to prepare changes, draft a bundle before live writes.

Detailed template: `tools/raspberrypi-openclaw/templates/draft-patch-bundle-template.md`.

A draft patch bundle must include:

- proposed target paths;
- operation for each path: create, update, move, or no-op;
- rationale;
- source evidence;
- facts versus hypotheses;
- open questions;
- risks;
- apply status: `draft_only`, `ready_for_user_review`, or `approved_to_apply`;
- what must not be applied yet.

Default status is `draft_only` unless the user explicitly approves live writes.

Before a bundle can become apply-ready, validate paths:

- unknown top-level directories are invalid;
- known lanes with unclear exact paths should return the valid route only and use `blocked_until_route_confirmed`;
- project workspace paths such as `<setronica-root>` are handoff envelopes until the user explicitly approves project-side writes;
- do not invent a deeper filename just to make the bundle look complete.

## Router Output Review Checklist

Before presenting or applying routed work, check output quality.

Detailed checklist: `tools/raspberrypi-openclaw/review-checklists/router-output-review-checklist.md`.

Minimum review questions:

- Did the agent invent any facts?
- Did it separate facts, hypotheses, ideas, weak signals, and risks?
- Did it recognize distinct topics/lanes inside one source?
- Did it ask the user when it suspected routes or topics were mixed?
- Did it keep validator context separate from owner contour?
- Did it identify what context is missing before changes?
- Did it avoid broad raw/private data access?
- Did it keep the next action safe and reviewable?

## Safe First Behavior

The agent may:

- classify a request using this context pack;
- say which contour likely applies and why;
- ask for missing context before routing;
- draft a patch or handoff envelope from user-provided context;
- explain what it cannot know yet.

The agent must not:

- claim it knows current state beyond this pack;
- read raw Personal Office data unless explicitly handed;
- write live artifacts without explicit approval;
- use credentials, browser profiles, finance tokens, or external accounts;
- route sensitive or company-confidential work based only on vibes.
