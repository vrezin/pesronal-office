# Machine-Readable Wiki

This wiki is the agent navigation layer.

Agents should start here, choose a domain map, read only the relevant source artifacts and skills, then act.

## Operating Rule

`AGENTS.md` is a bootloader. `wiki/maps/` is the routing table.

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
3. Read only `source_of_truth`, `skills`, and `memory` entries needed for the task.
4. If routing is unclear, create a clarification note in `inbox/processed/`.
