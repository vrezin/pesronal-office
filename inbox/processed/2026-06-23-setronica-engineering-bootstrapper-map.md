# Setronica Engineering Standard Bootstrapper Map

## Source

- User asked to review `<setronica-root>/engineering-task-to-handoff-standard`.
- Branch reviewed: `feature/project-bootstrapper-python-service-profile`.
- Baseline refs reviewed:
  - `origin/main`
  - `origin/feature/project-bootstrapper-python-service-profile`
  - local `feature/project-bootstrapper-python-service-profile`

## Repository State Observed

- `origin/main` is the current main branch pointer.
- Local branch `feature/project-bootstrapper-python-service-profile` is checked out and is one commit ahead of `origin/feature/project-bootstrapper-python-service-profile`.
- Working tree had pre-existing deleted files:
  - `photo_2026-05-25_13-53-43.jpg`
  - `photo_2026-05-25_13-53-44.jpg`
- No Setronica repo edits were made during this review.

## What The Main Branch Contains

The repository is a documentation-first delivery-standard project.

Core framing:

`source intent -> understanding -> Change Specification -> implementation -> evidence -> handoff`

Main layers:

- `framework/` - current canonical framework surface.
- `rollout-stages/stage-1/` - current implementation package for Stage 1 / `Task-to-Handoff`.
- `workspace/` - design shelf, exploratory notes, bootstrapper PoC, and non-canonical working material.
- `.codex/skills/` - repository-local operational skills for working inside this repo.

The current standard is `Task-to-Handoff`:

- one canonical `working change document`;
- separate `Understanding / Intake` and `Change Specification`;
- explicit source reference;
- confirmed understanding before final specification;
- success checks and verification method before handoff;
- implementation and evidence linked before declaring handoff readiness;
- controlled AI usage where AI does not replace human ownership.

## What The Bootstrapper Branch Adds

The feature branch adds a portable `Project Bootstrapper` under:

- `workspace/project-bootstrapper/`

The bootstrapper is currently a workspace-level PoC, not canonical framework content.

It can initialize a project-local operating layer. Current profiles:

- `documentation-first-repository`
- `python-service-project`

The `python-service-project` profile generates a Python service baseline plus Setronica-style operating discipline:

- `AGENTS.md`
- `bootstrap-manifest.md`
- `pyproject.toml`
- `src/<package_name>/__init__.py`
- `tests/README.md`
- `tests/test_smoke.py`
- `tasks/README.md`
- `tasks/templates/task-template.md`
- task buckets under `tasks/backlog/`, `tasks/in-progress/`, `tasks/done/`
- `wiki/index.md`
- `wiki/conventions/source-of-truth.md`
- `wiki/navigation/repo-layout.md`
- `docs/policies/development-policy.md`
- `docs/policies/testing-policy.md`
- `docs/standards/architecture-principles.md`
- `docs/codex-skills/README.md`
- `docs/codex-skills/registry/skills.yaml`
- `.codex/skills/project-operating-context/SKILL.md`
- `.github/workflows/quality.yml`

## Local Unpushed Layer On The Feature Branch

The local branch adds or changes bootstrapper material beyond `origin/feature/project-bootstrapper-python-service-profile`.

Most important addition:

- `workspace/project-bootstrapper/templates/python/wiki.yaml.template`

This introduces a machine-readable wiki route map for generated projects.

Why it matters:

- it turns the standard from "documents a human can read" into a project-local routing contract an agent can follow;
- it matches the Personal Office pattern of starting from a small wiki/map layer before broad repository search;
- it makes the generated project more suitable as an AI-assisted software repo baseline.

## Practical Interpretation

The promising idea is not to copy the Setronica repository into every new software project.

The promising idea is to use it as a source of portable operating layers:

1. Thin `AGENTS.md` with invariants and routing.
2. One canonical task artifact per meaningful change.
3. Separate understanding from specification.
4. Require readiness gates before non-trivial implementation.
5. Preserve verification evidence and residual risk.
6. Keep wiki/navigation as a route map, not as runtime truth.
7. Keep project-local skills and machine-readable skill registry.
8. Keep bootstrap manifest and deferred artifacts explicit.

For software projects, especially Python services, the `python-service-project` profile is the first concrete packaging of that idea.

## Open Placement Question

Permanent home in Personal Office is not yet chosen.

Candidate homes:

- `companies/setronica/` if this remains owner-level Setronica engagement context.
- `memory/semantic/topics/setronica.md` if this should become retrievable long-term memory.
- a new `companies/setronica/standards/` or similar index if multiple standard/application maps will accumulate.

Until that is decided, this file is a processed trace rather than canonical placement.

## Next Action

Discuss and choose the permanent Personal Office home for this map, then move or summarize this processed trace into that home.
