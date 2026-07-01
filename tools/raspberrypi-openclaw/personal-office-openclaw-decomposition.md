# Personal Office OpenClaw Decomposition

- Created: 2026-06-25
- Status: to-be decomposition
- Inputs:
  - `wiki/personal-office-concept.md`
  - `tools/raspberrypi-openclaw/openclaw-personal-office-operating-model.md`
  - `tools/raspberrypi-openclaw/personal-office-agent-cookbook.md`

## Target Shape

OpenClaw should operate Personal Office as a set of bounded workflows over a controlled context map.

The agent should not start as "one big assistant with all files".

It should be composed from:

- protocol/cookbook layer;
- context map layer;
- context budget and slimming layer;
- intake extraction layer;
- enrichment layer;
- routing layer;
- artifact writer layer;
- project contour / handoff layer;
- queue/state layer;
- memory/wiki link layer;
- review and approval layer.

## Components

### 1. Cookbook Runtime

Purpose:

- teach OpenClaw how Personal Office works before giving access to private data.

Inputs:

- `AGENTS.md`
- `wiki/personal-office-concept.md`
- `wiki/README.md`
- `secretaries/routing-map.md`
- `.codex/skills/`
- `wiki/playbooks/`
- `tools/raspberrypi-openclaw/`

OpenClaw shape:

- one dedicated agent workspace;
- read-only cookbook bundle;
- no raw Personal Office data by default.

### 2. Context Map

Purpose:

- know project/business/customer/person contours and routes.

Needs to represent:

- contour id/name;
- type: project, business, company, customer, personal area, opportunity;
- source of truth path;
- what belongs inside the contour;
- what stays in Personal Office;
- related people;
- related companies/customers;
- readiness/access state;
- handoff protocol.

Initial source:

- `wiki/maps/`
- `companies/`
- `people/`
- `memory/knowledge-graph/`
- future dedicated `wiki/contours/` or `memory/entities/projects/` index.

OpenClaw skill:

- `personal-office-context-map`

First behavior:

- answer "what context does this belong to?"
- list likely related contours and confidence;
- ask for missing context if confidence is low.

### 2a. Context Budget And Slimming Gate

Purpose:

- keep local installation responsive by preventing unnecessary prompt/context bloat.

Why it matters:

- local deployment protects ownership and privacy, but it does not automatically make bloated prompts fast;
- small tasks should not pay for unrelated identity files, unused skills, broad tool schemas, stale context, or raw data;
- context overload makes routing noisier and harder to trust.

Controls:

- define a default context budget per agent/workflow;
- keep `AGENTS.md` as a short bootloader;
- load playbooks only when a skill/workflow needs them;
- use narrow handoff files instead of broad repo reads;
- validate paths with routing excerpts rather than full office context;
- keep tool exposure and skill allowlists per workflow;
- log prompt/input/output/cache usage for test runs.

OpenClaw skill:

- `personal-office-context-budget-gate`

First behavior:

- report which files/skills/tools are loaded by default;
- flag context that is not needed for the current task;
- recommend a slimmer agent or workspace profile;
- block apply-ready status if the task relied on broad, unjustified context.

### 3. Intake Extractor

Purpose:

- turn messy input into structured meaning before routing.

Extract:

- facts;
- fact confidence / evidence level;
- hypotheses;
- feelings / weak signals;
- ideas;
- risks;
- opportunities;
- decisions;
- promises;
- deadlines;
- people;
- projects/business links;
- next actions.

OpenClaw skill:

- `personal-office-intake-extractor`

Output shape:

```yaml
facts:
  - text:
    confidence: high|medium|low
    evidence: user_provided|source_document|inference|memory
hypotheses:
  - text:
    basis:
ideas:
  - text:
    status: seed|candidate|validated|parked
weak_signals:
  - text:
    why_it_may_matter:
links:
  people: []
  projects: []
  companies: []
actions: []
open_questions: []
```

### 4. Context Enricher

Purpose:

- pull in known related context before deciding the route.

Looks up:

- related people;
- related projects;
- related companies;
- existing active/waiting tasks;
- prior processed notes;
- memory summaries;
- knowledge graph links;
- known business/customer routes.

OpenClaw skill:

- `personal-office-context-enrichment`

Safety:

- starts from cookbook + indexes;
- asks for narrow context handoff before reading sensitive source folders;
- does not infer private facts from missing data.

### 5. Router

Purpose:

- choose where the intake belongs.

Routes to:

- `inbox/processed/`
- `tasks/active/`
- `tasks/waiting/`
- `calendar/meetings/`
- `people/`
- `finance/`
- `life/`
- `companies/<company>/`
- `personal-projects/`
- `tools/`
- `automation/`
- `memory/`
- project contour handoff;
- needs-clarification note.

OpenClaw skill:

- `personal-office-router`

Decision rule:

- choose smallest useful target;
- if unclear, create/prepare clarification;
- if the project does not exist, decide whether to propose creation, hold in Personal Office, or park.

### 6. Artifact Writer

Purpose:

- produce durable files/patches from routed decisions.

Writes or prepares:

- raw note;
- processed note;
- active task;
- waiting task;
- meeting note;
- contact dossier update;
- project/company index update;
- memory summary;
- wiki/navigation link;
- handoff envelope.

OpenClaw skill:

- `personal-office-artifact-writer`

First mode:

- draft patch only;
- no direct write to live Personal Office until approval path is tested.

### 7. Project Contour / Handoff Manager

Purpose:

- decide what stays in Personal Office and what moves to a project workspace.

For existing project:

- create owner-side trace;
- create handoff envelope;
- identify target repo/path;
- list expected project-side artifact;
- record waiting/active follow-up.

For non-existing project:

- propose project creation;
- create holding note in Personal Office;
- create validation/decision task;
- park or close if idea dies.

OpenClaw skill:

- `personal-office-project-contours`

Important:

- MedVoice, Fincom, Setronica are examples only.
- The contour map must be extensible.

### 8. Queue And State Manager

Purpose:

- keep visible now/waiting/blocked/stale/parked state.

Surfaces:

- `tasks/active/`
- `tasks/waiting/`
- `tasks/done/`
- `tasks/someday/`
- `automation/state/`
- `automation/runs/`
- calendar-derived commitments.

OpenClaw skill:

- `personal-office-queue-state`

Questions it answers:

- what needs attention now?
- what is blocked?
- what waits on someone else?
- what stale item should be closed or revived?

### 9. Memory And Wiki Linker

Purpose:

- preserve reusable context without copying raw data everywhere.

Updates/proposes:

- `memory/semantic/topics/`
- `memory/entities/`
- `memory/knowledge-graph/`
- `wiki/maps/`
- future contour indexes.

OpenClaw skill:

- `personal-office-memory-wiki-linker`

Rule:

- source-of-truth artifact first;
- memory/wiki link second.

### 10. Review And Approval Gate

Purpose:

- keep agent autonomy bounded.

Checks:

- did it read only allowed context?
- did it separate facts/hypotheses/ideas?
- did it label confidence?
- did it choose a route with evidence?
- did it avoid raw sensitive data unless approved?
- did it prepare patches instead of silently editing?
- did it identify open questions?

OpenClaw skill:

- `personal-office-review-gate`

## Workflows

### Workflow A: Raw Intake To Routed Artifact

```text
user input
-> intake extractor
-> context enricher
-> router
-> artifact writer
-> review gate
-> user approval / live write
```

First OpenClaw MVP:

- classify synthetic input;
- produce structured extraction;
- propose target artifact;
- no raw repo access.

### Workflow A0: Slim Context Utility Task

```text
small utility request
-> context budget gate
-> load only narrow handoff/routing excerpt/template
-> perform validation/review/formatting
-> report token/context usage
-> no live write
```

Examples:

- path validation;
- patch bundle format check;
- router output checklist review;
- apply-readiness check.

Success criteria:

- no full meeting re-analysis;
- no broad repo access;
- no irrelevant skill/tool load;
- compact result;
- prompt/context usage recorded.

### Workflow B: Intake With Related People/Project Lookup

```text
input mentions idea/person/project
-> extractor finds people/projects/ideas
-> context enricher checks known links
-> route changes based on discovered relation
-> artifact updates both intake and relationship/project map
```

Example:

- family-office idea;
- known person has family-office reporting link;
- route becomes product validation/channel hypothesis, not generic idea note.

### Workflow C: Existing Project Handoff

```text
input belongs to known project
-> context map identifies contour
-> decide owner-side vs project-side split
-> Personal Office records intent/context/commitment
-> handoff envelope points to target project workspace
-> task tracks follow-through
```

### Workflow D: New Project Discovery

```text
input implies sustained new activity
-> no existing contour found
-> create holding artifact
-> create decision task
-> ask user whether to create project contour
-> if yes, bootstrap project space
-> if no, keep/park/close in Personal Office
```

### Workflow E: Queue Review

```text
scan active/waiting/state surfaces
-> classify now/waiting/blocked/stale/parked
-> recommend next action
-> update task state after approval
```

### Workflow F: Memory/Wiki Consolidation

```text
repeated or reusable insight appears
-> confirm source artifact
-> summarize without raw sensitive detail
-> link from wiki/map/graph
-> future agents can retrieve it
```

### Workflow G: Automation Run

```text
scheduled prompt/run
-> produce run log
-> update state only after success
-> create active/waiting tasks for real actions
-> do not require git commit
```

## Proposed OpenClaw Skills

### MVP Skills

1. `personal-office-cookbook-router`
   - reads cookbooks;
   - explains applicable route;
   - asks for narrow context.

2. `personal-office-intake-extractor`
   - separates facts, confidence, hypotheses, ideas, weak signals, actions.

3. `personal-office-context-map`
   - maps input to known contours;
   - identifies missing contour/project.

4. `personal-office-artifact-drafter`
   - drafts raw/processed/task/handoff artifacts as patches.

5. `personal-office-review-gate`
   - checks safety and completeness before write.

6. `personal-office-context-budget-gate`
   - checks prompt/context budget;
   - identifies unnecessary injected files, skills, and tools;
   - recommends slim agent/workspace profile for utility tasks.

### Next Skills

7. `personal-office-context-enrichment`
   - controlled lookup of people/projects/tasks/memory.

8. `personal-office-project-contours`
   - existing project handoff and new contour creation.

9. `personal-office-queue-state`
   - action/waiting/blocked/stale review.

10. `personal-office-memory-wiki-linker`
   - wiki/memory/graph updates.

11. `personal-office-automation-operator`
    - run logs, state markers, scheduled jobs.

## OpenClaw Agent Layout

OpenClaw supports multiple isolated agents in one Gateway. Each agent can have its own workspace, state directory, auth profiles, model registry/config, session store, skills, and channel bindings.

This means Personal Office should be mapped to agent lanes, not only abstract components. See:

- `tools/raspberrypi-openclaw/openclaw-capabilities-and-best-practices.md`

### Agent 1: `po-cookbook`

Purpose:

- safe first agent.

Access:

- cookbook bundle only.

Can:

- classify input;
- explain routes;
- draft patches;
- request context.

Cannot:

- read raw private data;
- write live repo;
- use external accounts;
- execute broad shell commands.

### Agent 2: `po-operator`

Purpose:

- later real Personal Office operator.

Access:

- approved narrow source paths;
- patch/write after approval;
- queue and artifact update.

Requires:

- sandbox/tool policy;
- audit logs;
- explicit user approval.

### Agent 3: `po-automation`

Purpose:

- scheduled runs and monitors.

Access:

- specific prompts/scripts/state/runs;
- narrow connector tools.

Requires:

- run logs;
- idempotency state;
- no broad write authority.

## Data/Index Needs

To make this work, Personal Office likely needs a compact contour index.

Candidate file:

```text
wiki/contours/index.md
```

or:

```text
memory/entities/projects/
memory/entities/businesses/
```

Each contour record should include:

- name;
- aliases;
- type;
- source-of-truth;
- Personal Office holding path;
- project workspace path;
- related people;
- related companies/customers;
- status;
- handoff rules;
- do-not-read-by-default notes.

## Rollout Plan

### Phase 0: Current State

- OpenClaw installed on Pi.
- Cookbook bundle synced.
- Gateway not running.
- No raw-data access.
- Too-wide partial copy exists and must be removed/quarantined.

### Phase 1: Cookbook-Only Agent

- Create OpenClaw workspace from cookbooks.
- Test synthetic intakes.
- Agent outputs route/extraction/context request only.

### Phase 2: Drafting Agent

- Allow agent to draft artifacts/patches.
- User applies patches manually.
- No direct writeback.

### Phase 3: Controlled Context Enrichment

- Add narrow lookup bundles or scripts.
- Agent can request specific context, not browse everything.
- Start building contour index.

### Phase 4: Approved Writeback

- Agent writes to approved paths after review gate.
- Logs every action.
- No finance/health/external-account writes without special approval.

### Phase 5: Channels And Automation

- Add Telegram or local dashboard.
- Add systemd user service.
- Add scheduled automation only after audit.

## Design Guardrails

- Cookbooks before data.
- Small default context before rich context.
- Facts separate from hypotheses and feelings.
- Confidence labels for facts.
- Related context lookup before routing.
- Project contours are extensible.
- Unknown project means create/hold/park, not guess.
- Source of truth first, memory/wiki second.
- Personal Office keeps owner-side context, not full project internals.
- No public Gateway without exposure runbook.
- No broad credentials or browser profiles.
- Patches before autonomous writes.
