# First Secretaries Operating Model

This document defines the first Personal Office secretary roles.

A secretary is a role and operating contract, not necessarily a separate
runtime process. One OpenClaw agent can perform several secretary roles, and one
business contour can compose several roles.

## Core Principle

Secretaries turn incoming life/work signals into durable Personal Office state:

- routed notes;
- tasks and waiting items;
- calendar artifacts;
- finance records;
- project/company updates;
- memory updates;
- run logs and summaries.

Important outcomes must not remain only in chat.

## Roles

| Secretary | Primary job | Main artifacts | First runtime shape |
|---|---|---|---|
| Intake secretary | Разбирает входящий поток и выбирает маршрут. | `inbox/raw/`, `inbox/processed/`, `secretaries/routing-map.md` | Always-on router for Telegram, Gmail, and manual input. |
| Calendar secretary | Ведет встречи, планы, напоминания, подготовку. | `calendar/`, `tasks/active/`, `tasks/waiting/` | Calendar-aware workflow, initially read-only Google Calendar plus repo artifacts. |
| Task secretary | Превращает договоренности в задачи и follow-ups. | `tasks/active/`, `tasks/waiting/`, `tasks/done/` | Shared role used by all domain agents. |
| Finance secretary | Ведет деньги, активы, обязательства и крупные решения. | `finance/`, finance tasks, source summaries | Separate cautious contour; default read-only tools. |
| Project secretary | Ведет личные проекты и возможности. | `personal-projects/`, project tasks, project notes | Specialized domain agents; `job-search` is the first live example. |
| Company secretary | Ведет контуры компаний. | `companies/`, company handoffs, company tasks | Owner-side state only; do not mirror full company repos. |
| Archivist | Закрывает недели, чистит inbox, делает summaries. | weekly summaries, cleanup logs, memory updates | Scheduled maintenance agent after core intake is stable. |

## Composition

Business contours should compose roles instead of inventing separate operating
rules.

Example: `job-search`

- Intake secretary: receives Gmail and Telegram job-search signals.
- Project secretary: owns `personal-projects/personal-brand/` routing.
- Task secretary: creates follow-ups and waiting items.
- Calendar secretary: handles interview/prep scheduling when needed.
- Archivist: folds repeated digests/noise into run logs and summaries.

## Runtime Boundary

The Pi-primary Personal Office host is the preferred always-on runtime for
secretary loops.

The workstation is an operator surface: it can initiate requests, review
changes, and sync, but should not own always-on Personal Office state.

## Pi Intake Secretary

The Pi should have a general `intake` secretary for non-domain-specific incoming
messages.

`job-search` is the first proven downstream contour, but it is not the universal
front door. General Personal Office input should first go to `intake`, then be
routed to the smallest responsible secretary/domain.

Safe first Telegram topology:

- `personal-office-intake-telegram` -> `intake`;
- `job-search-telegram` -> `job-search`.

This keeps the proven job-search channel working while the general intake router
is tested.

## Routing Rules

Every new input starts with the smallest useful route:

1. Use `secretaries/routing-map.md`.
2. Read the relevant `wiki/maps/` domain map.
3. Update the owning artifact.
4. Create tasks/waiting items when there is an action or dependency.
5. Leave a processed trace when the input materially changed state.

If the route is unclear, create a clarification note instead of guessing.

## Priority Order

First live/runtime priorities:

1. Intake secretary for Telegram/Gmail/manual messages.
2. Project secretary for `job-search`, because it is already Pi-primary.
3. Task secretary as shared follow-up layer.
4. Calendar secretary for interview/prep and daily planning.
5. Archivist for weekly close and inbox cleanup.
6. Finance secretary after read-only finance tooling is stable.
7. Company secretary as owner-side routing for AI Studio, Fincom, and Setronica.

## Non-Goals

- Do not make one giant agent that reads the whole repository by default.
- Do not split Personal Office state between workstation and Pi.
- Do not store secrets or tokens in Git.
- Do not let SQLite become the canonical record of decisions; SQLite is runtime
  state, Markdown artifacts are durable operating state.
