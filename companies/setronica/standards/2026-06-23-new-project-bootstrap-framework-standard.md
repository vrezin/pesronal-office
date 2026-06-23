# New Project Bootstrap Framework Standard

## Status

`draft / proposed`

## Purpose

Define a standard for creating a new project operating layer when a new activity starts from a meeting, opportunity, client request, or repository creation.

This standard is inspired by the Setronica `Task-to-Handoff` standard and the `Project Bootstrapper` PoC in `<setronica-root>/engineering-task-to-handoff-standard`.

## Core Principle

A new project should not start as only a folder, repo, chat, or codebase.

It should start as a traceable operating envelope:

`source -> project understanding -> project profile -> generated operating layer -> bootstrap manifest -> first task / discovery artifact`

## Personal Office Control Center Model

Personal Office is the main control center for project creation.

Target scenario:

- Vladimir enters a quick mobile note after a live conversation.
- The note says that he spoke with a person and agreed to start an activity.
- Personal Office captures the input and processes it by its own routing rules.
- The agent finds involved people and records interaction facts.
- The agent searches for related people, companies, meetings, tasks, documents, contracts, prior decisions, and reusable standards.
- The agent proposes who else could be pulled in, who may be interested, and which artifacts should be attached.
- The agent creates an owner-level project/activity envelope.
- The agent generates a project space that follows the Setronica-style engineering standard.

This makes Personal Office the orchestrator.

Setronica standard remains the source of project operating discipline.

Generated project spaces remain the source of execution truth for their own work.

## When To Use

Use this standard when:

- a new client stream appears;
- a new software repository is created;
- a new internal tool or automation project starts;
- a meeting creates a sustained workstream;
- a company asks Vladimir to join a new project;
- a project needs AI-assisted implementation discipline from the beginning.

## Required Inputs

Minimum:

- source reference;
- project name or temporary codename;
- sponsor/requester;
- primary objective;
- current known scope;
- current known non-goals;
- missing inputs;
- initial owner;
- target project type.

If any of these are missing, create the project envelope anyway, but mark the missing fields explicitly.

## Project Profile Model

Every generated project should select a profile.

Profile fields:

- `name`
- `project_type`
- `repository_shape`
- `delivery_profile`
- `task_to_handoff_required`
- `ai_readiness_gate_required`
- `spec_quality_review_required`
- `minimum_evidence_model`
- `allowed_integrations`
- `disallowed_integrations`
- `selected_gates`
- `generated_artifacts`
- `deferred_artifacts`
- `known_gaps`

Initial profiles:

- `documentation-first-repository`
- `python-service-project`
- `client-modernization-discovery`

## Minimum Generated Operating Layer

Every generated project should include:

- `AGENTS.md`
- `bootstrap-manifest.md`
- `tasks/README.md`
- `tasks/templates/task-template.md`
- `tasks/backlog/`
- `tasks/in-progress/`
- `tasks/done/`
- `wiki/index.md`
- `wiki/wiki.yaml`
- `wiki/conventions/source-of-truth.md`
- `workspace/registers/current-focus.md`
- `workspace/registers/decisions.md`
- `.codex/skills/project-operating-context/SKILL.md`

Software profiles may additionally include:

- runtime skeleton;
- test skeleton;
- development policy;
- testing policy;
- architecture principles;
- skill registry;
- CI starter workflow.

## Generated `AGENTS.md` Contract

Generated `AGENTS.md` should be thin.

It should contain:

- source-of-truth hierarchy;
- mandatory non-trivial task flow;
- routing entrypoints;
- project-specific invariants;
- AI-assisted work boundary;
- verification expectations;
- escalation triggers.

It should not contain:

- full task procedures;
- full architecture docs;
- hidden project facts;
- duplicated wiki content.

## Task Artifact Contract

For every meaningful change, generated projects should use one task artifact containing:

- `Source / Request Reference`
- `Understanding / Intake`
- `Question Ledger`
- `Change Specification`
- `Architecture / Policy Gate`
- `Implementation Plan`
- `Verification Evidence`
- `Handoff / Closeout`

The task artifact is the local form of `Verified Change`.

## Machine-Readable Wiki Contract

Every generated project should include `wiki/wiki.yaml`.

It should define:

- project metadata;
- entrypoints;
- source-of-truth hierarchy;
- routes by work type;
- read-first files;
- candidate paths;
- update-required files;
- known gaps.

This makes the project friendly to agents without forcing them to read the whole repository.

## Bootstrap Manifest Contract

Every generated project should include `bootstrap-manifest.md`.

It should record:

- profile used;
- bootstrap date;
- source package/version;
- answers collected;
- generated artifacts;
- selected gates;
- evidence expectations;
- deferred artifacts;
- manual follow-up;
- known gaps;
- validation result.

## Script Requirements

The bootstrapper script should:

- use profiles as data, not hard-coded behavior;
- support non-interactive mode;
- support dry run;
- support force overwrite only explicitly;
- render templates into the target project;
- create missing directories;
- never silently overwrite existing files;
- validate that required artifacts exist after generation;
- write `bootstrap-manifest.md`;
- keep deferred artifacts explicit.

For portability, the first version should use only Python standard library.

## Tooling Home Decision

The next prototype should live in Personal Office tooling:

- `tools/project-bootstrapper/`

Reason:

- Personal Office owns intake, people context, artifact retrieval, and project-spawning decisions.
- Setronica repo owns the evolving engineering standard and bootstrapper reference concepts.
- Generated project spaces should be created from Personal Office context, not from a company repo acting alone.

## Personal Office CLI Prototype

Implemented first local CLI prototype:

- `tools/project-bootstrapper/bootstrap.py`

Supported profiles:

- `documentation-first-repository`
- `python-service-project`
- `client-modernization-discovery`

Supported modes:

- `--list-profiles`
- `--non-interactive`
- `--dry-run`
- `--force`
- `--answer KEY=VALUE`
- `--source-reference`

The CLI generates project-local operating layers and writes `bootstrap-manifest.md`.

## New Client Activity Profile: `client-modernization-discovery`

Purpose:

Initialize a discovery/control package for legacy modernization or migration work before implementation starts.

Suggested artifacts:

- `AGENTS.md`
- `bootstrap-manifest.md`
- `discovery/README.md`
- `discovery/source-materials.md`
- `discovery/system-inventory.md`
- `discovery/business-critical-flows.md`
- `discovery/risk-register.md`
- `discovery/migration-options.md`
- `discovery/ai-assisted-work-boundary.md`
- `tasks/templates/task-template.md`
- `wiki/index.md`
- `wiki/wiki.yaml`
- `workspace/registers/current-focus.md`
- `workspace/registers/decisions.md`

First task:

- create a discovery document from provided source materials;
- separate business-critical unknowns from implementation options;
- define validation strategy before recommending migration path.

## Application To Current Setronica Activity

The 2026-06-22 Yuliya legacy migration signal should become a new project envelope first, not a code-first effort.

Current project envelope:

- `../projects/2026-06-23-legacy-migration-modernization.md`

Recommended next step:

- when source materials arrive, create the first discovery artifact using `client-modernization-discovery` shape.

## Open Questions

- Which project profile should be implemented after `python-service-project`?
- How much collaborator/artifact recommendation should be automatic in the first prototype?
- What should count as enough evidence to create a full project space versus only an activity envelope?
