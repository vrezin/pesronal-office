# Build Project Bootstrapper Standard And Tooling

## Source

- User clarified on 2026-06-23 that the goal is a framework standard for creating new projects and a set of rules/scripts/standards for automatic project generation.
- User clarified later on 2026-06-23 that Personal Office is the main control center: mobile/raw intake should be captured, enriched with people/context/artifacts, and then used to spawn a project space.
- Standards draft: `../../companies/setronica/standards/2026-06-23-new-project-bootstrap-framework-standard.md`.
- Rule validation proposal: `../../companies/setronica/standards/2026-06-23-current-agent-rules-validation.md`.
- Target playbook: `../../wiki/playbooks/project-bootstrap-control-center.md`.
- Setronica bootstrapper source: `<setronica-root>/engineering-task-to-handoff-standard/workspace/project-bootstrapper/`.

## Goal

Turn the project-bootstrapper concept into a practical reusable package.

## Expected Outputs

- Confirm canonical home for reusable tooling: Setronica repo, Personal Office tools, or split ownership. `done: Personal Office tooling first`
- Build the first prototype under `tools/project-bootstrapper/`. `done`
- Define initial profile set:
  - `documentation-first-repository` `done`
  - `python-service-project` `done`
  - `client-modernization-discovery` `done`
- Validate and refine generated artifact contracts:
  - `AGENTS.md` `done`
  - `tasks/` `done`
  - `wiki/index.md` `done`
  - `wiki/wiki.yaml` `done`
  - policies/standards `partial: Python profile only`
  - bootstrap manifest `done`
- Decide whether to update Setronica repo feature branch directly. `deferred`
- Keep Setronica repo as standards/reference source, not the orchestration home. `done`
- Produce an implementation plan for scripts/templates/profiles. `done in README and profile contracts`

## Current Status

`active / first CLI prototype implemented`

## Implemented

- `../../tools/project-bootstrapper/bootstrap.py`
- `../../tools/project-bootstrapper/profiles/documentation-first-repository.json`
- `../../tools/project-bootstrapper/profiles/python-service-project.json`
- `../../tools/project-bootstrapper/profiles/client-modernization-discovery.json`
- `../../tools/project-bootstrapper/templates/`

## Verification Evidence

- `python3 -m json.tool tools/project-bootstrapper/profiles/documentation-first-repository.json`
- `python3 -m json.tool tools/project-bootstrapper/profiles/python-service-project.json`
- `python3 -m json.tool tools/project-bootstrapper/profiles/client-modernization-discovery.json`
- `python3 tools/project-bootstrapper/bootstrap.py --list-profiles`
- `python3 -m py_compile tools/project-bootstrapper/bootstrap.py`
- Smoke generated `documentation-first-repository` into `/tmp/personal-office-bootstrap-smoke-doc-20260623`: validation passed.
- Smoke generated `client-modernization-discovery` into `/tmp/personal-office-bootstrap-smoke-discovery-20260623`: validation passed.
- Smoke generated `python-service-project` into `/tmp/personal-office-bootstrap-smoke-python-20260623`: validation passed.

## Remaining Work

- Add Personal Office enrichment wrapper that can take a processed intake/person/company context and call this CLI with prefilled answers.
- Decide whether to port improvements back to the Setronica reference branch.
- Add tests for CLI behavior beyond smoke generation.
