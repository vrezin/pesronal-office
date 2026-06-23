# Machine-Readable Wiki

This wiki is the agent navigation layer.

Agents should start here, choose a domain map, read only the relevant source artifacts and domain-router skills, then act.

## Operating Rule

`AGENTS.md` is a bootloader. `wiki/maps/` is the routing table. `wiki/playbooks/` contains detailed procedures that should be read only when needed.

## Maps

- `maps/life-planning.md`
- `maps/health.md`
- `maps/finance.md`
- `maps/personal-brand.md`
- `maps/ai-studio.md`
- `maps/fincom.md`
- `maps/tools.md`
- `maps/inbox-tasks-calendar.md`
- `maps/memory-system.md`

## Playbooks

- `playbooks/personal-office-intake.md`
- `playbooks/project-bootstrap-control-center.md`
- `playbooks/memory-system.md`
- `playbooks/personal-brand-career.md`
- `playbooks/life-planning.md`
- `playbooks/company-work.md`
- `playbooks/automation-monitoring.md`

## Map Contract

Each map uses YAML frontmatter:

```yaml
domain:
source_of_truth: []
skills: []
memory: []
retrieval: []
safety: []
do_not_read_by_default: []
```

## Workflow

1. Identify the domain.
2. Open the matching map.
3. Read only `source_of_truth`, `skills`, `memory`, and playbook sections needed for the task.
4. If routing is unclear, create a clarification note in `inbox/processed/`.
