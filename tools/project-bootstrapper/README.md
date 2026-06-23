# Project Bootstrapper

## Status

`prototype / usable locally`

## Purpose

Create project/activity spaces from Personal Office intake.

The tool should start from a real conversation, opportunity, or meeting trace and generate an operating layer for the new activity.

## Operating Model

Personal Office owns:

- raw intake;
- processed trace;
- people and relationship facts;
- context/artifact retrieval;
- candidate collaborator suggestions;
- owner-level activity envelope;
- project-space generation command.

Generated project spaces own:

- local `AGENTS.md`;
- local task lifecycle;
- local wiki routes;
- local bootstrap manifest;
- project-local evidence and handoff artifacts.

## Standards Source

The initial operating discipline is based on:

- `<setronica-root>/engineering-task-to-handoff-standard`
- `companies/setronica/standards/2026-06-23-new-project-bootstrap-framework-standard.md`
- `wiki/playbooks/project-bootstrap-control-center.md`

## Initial Profiles

- `documentation-first-repository`
- `python-service-project`
- `client-modernization-discovery`

## CLI

List profiles:

```bash
python3 tools/project-bootstrapper/bootstrap.py --list-profiles
```

Create a documentation-first project:

```bash
python3 tools/project-bootstrapper/bootstrap.py \
  --profile documentation-first-repository \
  --target /tmp/example-doc-project \
  --non-interactive \
  --source-reference "Personal Office intake"
```

Create a Python service project:

```bash
python3 tools/project-bootstrapper/bootstrap.py \
  --profile python-service-project \
  --target /tmp/example-python-service \
  --non-interactive \
  --answer project_name="Example Python Service" \
  --answer package_name="example_python_service"
```

Create a client modernization discovery project:

```bash
python3 tools/project-bootstrapper/bootstrap.py \
  --profile client-modernization-discovery \
  --target /tmp/example-modernization-discovery \
  --non-interactive \
  --source-reference "Personal Office meeting note"
```

Preview without writing:

```bash
python3 tools/project-bootstrapper/bootstrap.py \
  --profile client-modernization-discovery \
  --target /tmp/example-modernization-discovery \
  --non-interactive \
  --dry-run
```

Override answers:

```bash
python3 tools/project-bootstrapper/bootstrap.py \
  --profile client-modernization-discovery \
  --target /tmp/example-modernization-discovery \
  --non-interactive \
  --answer project_name="Legacy Payments Modernization" \
  --answer sponsor="Yuliya" \
  --answer source_reference="Personal Office processed trace"
```

## Prototype Requirements

- Profile-driven generation.
- Non-interactive and interactive modes.
- Dry-run mode.
- `--answer KEY=VALUE` overrides for Personal Office orchestration.
- `--source-reference` shortcut for intake/meeting trace linkage.
- No silent overwrite.
- Bootstrap manifest.
- Generated `wiki/wiki.yaml`.
- Explicit deferred artifacts.
- Validation of generated required files.

## First Implementation Note

Do not copy company-specific Setronica project facts into generated projects.

Use Setronica standard concepts as reusable operating discipline.
