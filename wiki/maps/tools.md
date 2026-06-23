---
domain: tools
source_of_truth:
  - tools/
  - automation/
skills:
  - automation-monitoring
  - memory-system
memory:
  - memory/semantic/topics/tools.md
  - memory/entities/tools/
retrieval:
  - memory/retrieval/search-rules.md
  - memory/knowledge-graph/nodes.jsonl
  - memory/knowledge-graph/edges.jsonl
safety:
  - sensitive_tools_default_read_only
  - tools_belong_in_personal_office_tools
do_not_read_by_default:
  - finance/
---
# Tools Map

Use for local MCP servers, helper services, personal automation, and tool routing.

## Project Bootstrapper

Personal Office project-space generation lives under:

- `tools/project-bootstrapper/`

Use it when a Personal Office intake should become a generated project/activity space with local `AGENTS.md`, task lifecycle, wiki route map, bootstrap manifest, and Setronica-style Task-to-Handoff discipline.

## Automation

Scheduled prompts, wrappers, state markers, and run logs live in `automation/`.

HH Gmail monitoring uses:

- `automation/prompts/hh-gmail-monitor.md`;
- `automation/scripts/run-hh-gmail-monitor.sh`;
- `automation/systemd/`;
- `automation/cron/`;
- `automation/state/hh-gmail-monitor-state.md`;
- `automation/runs/`.
