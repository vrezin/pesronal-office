# Personal Office Agent Protocol

This repository is a private operating system for personal life, family matters, finances, projects, companies, meetings, tasks, and memory.

## Prime Directive

Important outcomes must not remain only in chat.

If an input contains a decision, promise, deadline, meeting, amount of money, obligation, risk, opportunity, person, or next step, create or update the relevant artifact in this repository.

## Routing

Start with `wiki/README.md`.

Use `wiki/maps/` to choose the smallest relevant set of source documents and local skills for the task. Do not read the whole repository by default.

For routing new incoming information into artifacts, use `secretaries/routing-map.md`.

- Raw unprocessed input belongs in `inbox/raw/`.
- Processed input should leave a trace in `inbox/processed/`.
- Meetings belong in `calendar/meetings/`.
- Active next actions belong in `tasks/active/`.
- Waiting items belong in `tasks/waiting/`.
- Personal and family matters belong in `life/`.
- Health facts belong in `life/health-lifestyle/health-facts/`.
- Lifestyle facts belong in `life/health-lifestyle/lifestyle-facts/`.
- Money, assets, obligations, taxes, investments, and major financial decisions belong in `finance/`.
- Profi.ru, consulting, experiments, and personal opportunities belong in `personal-projects/`.
- Company matters belong in `companies/<company>/`.
- People, relationship context, and follow-ups belong in `people/`.
- Local tools, MCP servers, helper services, and personal automation belong in `tools/`.
- Memory summaries, entity facts, retrieval notes, and knowledge graph records belong in `memory/`.
- Machine-readable task/domain navigation belongs in `wiki/`.

If the target is unclear, create `inbox/processed/needs-clarification-YYYY-MM-DD.md` with the specific question that blocks routing.

## Artifact Rules

- Use stable filenames: `YYYY-MM-DD-topic.md`.
- Do not invent missing facts.
- Keep sensitive details minimal; follow `secretaries/privacy-rules.md`.
- When a note implies a task, create or update the task file.
- When a meeting changes a project, company, finance item, or personal commitment, update that target artifact too.

## Path Aliases

Do not write machine-specific absolute paths in repository documents.

Use:

- `<repo-root>` for this repository root.
- `<aistudio-root>` for the neighboring AI Studio workspace.
- `<fincom-root>` for the neighboring Fincom workspace.
- `<external-downloads>` for source files outside the repository.

## Health And Life Planning Safety

For medications, health constraints, diet, and training, agents must not invent recommendations. Use only user-provided facts, doctor instructions, or source documents. If a health input is unclear, create a clarification note instead of making a medical decision.

## Local Skills

Repo-local Codex skills live in `.codex/skills/`.

For memory and wiki work, prefer these skills:

- `wiki-routing` - choose the relevant wiki map and minimum source set before reading.
- `memory-retrieval` - search memory, entities, graph, and source artifacts before answering or planning.
- `memory-capture` - capture durable facts, decisions, events, and relations from new intake.
- `memory-consolidation` - periodically compress episodic memory into semantic memory, entity records, and graph edges.
- `knowledge-graph-indexing` - update the file-backed knowledge graph from repository artifacts.

For personal brand / career work, prefer these skills instead of copying long process rules into chat:

- `personal-brand-routing` - route career, CV, HH, JD, and personal portfolio work.
- `job-intake-analysis` - archive and analyze pasted vacancies/JDs.
- `cv-selection` - choose the best final CV for a role.
- `cover-letter-screening` - draft cover letters, recruiter replies, and screening answers.
- `final-cv-pdf-review` - validate and register final PDF resumes.

For life planning, prefer these skills:

- `life-intake-router` - route raw life inputs into facts, tasks, calendar, and plans.
- `weekly-life-plan` - build weekly life plans from facts and current obligations.
- `medication-schedule-planning` - plan medication reminders from saved instructions only.
- `meal-grocery-planning` - plan weekly menu and Saturday groceries.
- `life-plan-maintenance` - rebalance daily, weekly, and monthly plans after new intake.

## Local Tools

Personal-office tools live in `tools/`.

Use this directory for local MCP servers, helper services, and automation that support personal life, finance, calendar, inbox, or personal projects. Do not place these tools in company repositories.

`tools/zenmoney-mcp/` is the ZenMoney MCP server for personal finance history. Treat it as sensitive. Prefer `ZENMONEY_READ_ONLY=1` unless the user explicitly asks to create, update, or delete transactions.

## Working Style

Before closing a request, state what files were created or updated and what still needs attention.
