# Current Agent Rules Validation Against Setronica Standard

## Purpose

Validate current Personal Office agent rules against the Setronica `Task-to-Handoff` concepts and identify proposed improvements.

## Sources Reviewed

- `AGENTS.md`
- `wiki/README.md`
- `wiki/maps/setronica.md`
- `secretaries/routing-map.md`
- `companies/setronica/active.md`
- `inbox/processed/2026-06-23-setronica-engineering-bootstrapper-map.md`
- `<setronica-root>/engineering-task-to-handoff-standard` read-only review from 2026-06-23

## Verdict

Current Personal Office rules are strong as an intake and routing operating system.

They already enforce:

- important outcomes must become artifacts;
- routing starts from a wiki/map layer;
- company truth and Personal Office management context stay separated;
- next actions become `tasks/active/` or `tasks/waiting/`;
- processed inputs leave a trace;
- machine-readable navigation belongs in `wiki/`.

The gap is not basic discipline.

The gap is that non-trivial project work is not yet explicitly modeled as:

`source -> understanding -> specification -> implementation -> evidence -> handoff`

That chain exists informally in good runs, but it is not yet a first-class Personal Office rule.

## Alignment With Setronica Concepts

### Already Aligned

- `Prime Directive` matches the artifact-first principle.
- `wiki/README.md` and `wiki/maps/` match the idea of a thin routing layer before broad search.
- `secretaries/routing-map.md` matches source intake and target artifact routing.
- `companies/<company>/` boundary matches Setronica's distinction between project truth and management context.
- `tasks/active/` and `tasks/waiting/` provide visible next-action state.

### Partially Aligned

- Personal Office creates tasks, but tasks are not required to contain separate `Understanding / Intake` and `Change Specification`.
- Personal Office records many outcomes, but does not always require explicit verification evidence before marking work done.
- Personal Office has wiki maps, but not yet a standard machine-readable project route contract equivalent to generated `wiki/wiki.yaml`.
- Company project intake exists in practice, but there is no explicit "new project bootstrap" standard for creating a clean project envelope from a meeting or opportunity.

### Missing Or Under-Specified

- Non-trivial work gate.
- Understanding confirmation.
- Specification confirmation or explicit waiver.
- Evidence model for closeout.
- Handoff package shape.
- Project-bootstrap manifest.
- Deferred-artifacts register.
- Project profile selection.
- Scriptable project generation contract.

## Proposed Rule Improvements

### 1. Add A Non-Trivial Work Rule

For non-trivial work, require one canonical task/project artifact that links:

`source -> understanding -> specification -> plan -> execution -> evidence -> closeout`

This should apply when a request changes:

- code;
- company workflow;
- public position;
- finance commitment;
- client/project obligations;
- durable repository structure;
- automation behavior.

### 2. Add Understanding / Specification Separation

Before implementation or final advice, distinguish:

- `Understanding / Intake`: what we believe the request means;
- `Change Specification`: what we choose to do about it.

For small tasks this can be brief.
For project work it should be explicit.

### 3. Add A Closeout Evidence Rule

Before calling non-trivial work done, record:

- changed artifacts;
- commands/checks run;
- checks not run and why;
- residual risk;
- follow-up tasks or waiting items.

### 4. Add A Project Bootstrap Rule

When a meeting or opportunity implies a new project, create a project envelope with:

- source trace;
- current status;
- owner/stakeholders;
- current understanding;
- missing inputs;
- active next action;
- recommended first artifact;
- links to tasks/waiting items.

### 5. Add Machine-Readable Route Maps For Generated Projects

For new software projects, require a `wiki/wiki.yaml` or equivalent route map:

- entrypoints;
- source-of-truth hierarchy;
- routes by work type;
- required reads before broad search;
- update rules when durable paths move.

### 6. Add Bootstrap Manifest As A Required Artifact

Every automatically generated project should include a `bootstrap-manifest.md` with:

- profile used;
- questions/answers;
- generated artifacts;
- deferred artifacts;
- selected gates;
- evidence expectations;
- validation result.

## Suggested Personal Office Changes

Do not immediately overload `AGENTS.md`.

Preferred sequence:

1. Add a focused playbook: `wiki/playbooks/project-bootstrap.md`.
2. Add a map route or extend `wiki/maps/tools.md` / `wiki/maps/setronica.md` for project bootstrap work.
3. Add `companies/setronica/standards/` as the owner-level standards/application index.
4. Only after the shape stabilizes, add a short rule to `AGENTS.md`.

## Open Questions

- Should the project-bootstrap standard live in Personal Office, Setronica repo, or both?
- Should generated projects use `tasks/` as mandatory workflow state or as advisory bootstrap default?
- Which profiles are needed beyond `python-service-project`?
- Should project generation create only a local operating layer, or also initialize git/remote/CI integrations?
