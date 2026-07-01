# Personal Office Shared Storage Decision

- Date: 2026-07-01
- Status: Accepted
- Scope: Personal Office primary storage on Raspberry Pi and job-search business contour

## Decision

Use the Raspberry Pi as the primary Personal Office home.

The workstation is an operator/client surface that can initiate requests, review changes, and pull/push as needed, but the long-running Personal Office runtime should not depend on the workstation being powered on.

Use a three-layer storage model on the Pi:

1. Git + Markdown as the canonical artifact layer.
2. SQLite as the operational runtime state layer.
3. Git remote/backup as the sync and recovery layer.

## Canonical Artifact Layer

Git-tracked Markdown remains the human-readable source of truth.

Canonical artifacts include:

- `automation/runs/` run logs;
- `automation/state/` durable monitor state snapshots;
- `tasks/active/` and `tasks/waiting/`;
- `inbox/raw/` and `inbox/processed/`;
- `personal-projects/personal-brand/workspace/job-intake/`;
- CV and cover-letter selection notes;
- wiki maps and playbooks.

Important outcomes must still land in these files, not only in SQLite, Telegram, or chat.

## Memory OS Layer

Memory OS is the navigation and compression layer over canonical artifacts, not a separate source-of-truth store.

On the Raspberry Pi, Memory OS belongs to the shared Personal Office cookbook/base layer, not to any single business contour:

```text
/home/openclaw/personal-office-agent/cookbooks/personal-office/
```

Business contours such as `job-search` may use these rules and validators, but they should not become the owner of general `wiki/`, `memory/`, or `tools/memory-os` infrastructure.

Use it for:

- context cards;
- semantic topics;
- entity summaries;
- decisions;
- handoffs;
- workflows;
- validation signals;
- retirement notes;
- retrieval and graph navigation.

Rules:

- domain source artifacts still own facts and decisions;
- Memory OS links to source artifacts instead of copying raw private content;
- if Memory OS disagrees with a source artifact, the source artifact wins;
- job-search automation may enrich Memory OS only when a source-backed reusable route or concept is created;
- routine Gmail dedupe and run coordination belong in SQLite, not Memory OS.

When Pi changes protocol-managed memory, the sync gate should run:

```bash
python3 tools/memory-os/memory_os.py validate
python3 tools/memory-os/memory_os.py graph-check
python3 tools/memory-os/memory_os.py stale
```

## Operational State Layer

Use SQLite for high-frequency machine state that needs transactions, locks, and fast duplicate checks.

Recommended path:

```text
automation/state/job-search-runtime.sqlite
```

Runtime state may include:

- processed Gmail ids;
- Telegram update/message ids;
- vacancy fingerprints;
- source URLs and external ids;
- run locks;
- retry/backoff state;
- routing status;
- artifact path mappings;
- last successful poll cursors.

SQLite is not the human-facing source of truth. Important conclusions, decisions, and next actions must be exported to Markdown artifacts.

Initial implementation decision:

- do not commit `job-search-runtime.sqlite`, `-wal`, or `-shm`;
- seed/rebuild baseline duplicate state from Markdown monitor state when needed;
- back up or export runtime state separately once unattended scheduling is active.

## Shared Sync Layer

Use Git to synchronize and back up the Personal Office artifact layer, but the primary working copy should live on the Raspberry Pi.

Primary direction:

- Pi hosts the canonical Personal Office working tree.
- Scheduled jobs, Telegram handlers, and business contours run on the Pi.
- The workstation acts as a client/operator:
  - SSH into Pi;
  - call OpenClaw agents;
  - pull/review repo state;
  - initiate manual jobs;
  - edit locally only when explicitly chosen, then sync back.
- Git remote is used for backup, history, and optional workstation checkout, not as a split-brain source of truth.

Target behavior:

1. Pi pulls/reconciles before scheduled work if an upstream remote exists.
2. Pi writes Personal Office artifacts as the primary runtime.
3. Pi commits and pushes successful unattended output to backup/private remote.
4. Workstation pulls/reviews or initiates requests against Pi.
5. Workstation-originated changes must sync back to Pi before they are considered operationally current.

Initial write allowlist should be narrow:

- `automation/runs/`;
- `automation/state/`;
- `inbox/processed/`;
- `tasks/active/`;
- `tasks/waiting/`;
- `personal-projects/personal-brand/workspace/job-intake/`.

Secrets, OAuth tokens, browser profiles, `.env` files, and local credential stores must not be committed.

## Repository Shape Options

### Option 1 - Pi-Primary Full Personal Office Repo

The full Personal Office repository lives on Pi as the primary working tree. A private remote backs it up and lets the workstation pull/review/initiate work.

Pros:

- matches the desired operating model: Personal Office lives on the always-on Pi;
- no split-brain source of truth;
- Markdown artifacts stay in canonical paths;
- scheduled jobs and Telegram flows can write directly to the real operating system.

Cons:

- Pi becomes a sensitive primary host and needs backup/security discipline;
- agent permissions must be bounded by workflow, not by assuming the repo is partial;
- workstation changes need sync hygiene.

### Option 2 - Separate Job Search Contour Repo

Rejected as the main Personal Office architecture for now.

This may still be useful later as a product/runtime package, but it creates the distributed Personal Office shape the user does not want.

It would contain only:

- job-search runtime tooling;
- allowed `automation/state` and `automation/runs` projections;
- job-intake subset or generated job-search artifacts;
- Telegram interaction logs;
- handoff patches/exports back to canonical Personal Office.

Pros:

- clean trust boundary;
- Pi deploy key only accesses job-search material;
- easier to reason about the business contour as a product/runtime.

Cons:

- requires an import/export or handoff bridge to the canonical Personal Office repo;
- canonical paths may need projection or patch application;
- more moving parts than a full mirror.

### Option 3 - Bare Remote Full Mirror Plus Pi Sparse Checkout

Rejected for the primary Personal Office home.

The remote contains the full Personal Office repo, but the Pi worktree uses sparse checkout for only allowed paths.

Pros:

- simple to start;
- Pi local disk stays narrow.

Cons:

- not a strong security boundary: the remote still contains all data and the key may fetch it.

Current accepted direction:

Use a Pi-primary full Personal Office working tree, with agents constrained by workflow permissions, skills, prompts, and wrappers. The workstation should be able to initiate requests, but should not be required for scheduled or Telegram-driven operation.

## One Repo Vs Many Repos

This is a separate architectural axis from Pi-primary hosting.

The right model is not "one repository forever" and not "a repository per tiny workflow". Use a layered repository topology:

1. One Pi-primary Personal Office core repo.
2. Separate contour repos only for domains that have a distinct lifecycle, runtime, security boundary, or product-like deployment.
3. Clear handoff/sync contracts between core and contour repos.

### Core Repo

The Personal Office core repo should own:

- wiki maps and playbooks;
- Memory OS protocol, retrieval, and graph;
- owner/operator workflow pack;
- cross-domain tasks, waiting items, and decisions;
- people/company/project routing;
- shared automation conventions;
- source-of-truth artifacts that are not isolated into a separate contour.

Core is the navigation and ownership layer. It should answer where something belongs and preserve the owner-side state.

### Contour Repos

Create a separate repo only when a contour needs one or more of these:

- its own runtime dependencies or services;
- its own deploy keys, OAuth scopes, browser profiles, or credentials;
- independent schedule/daemon lifecycle;
- product-like packaging or possible reuse outside this Personal Office;
- large generated artifacts or binaries;
- different security boundary;
- many domain-specific tests/tools that would pollute the core repo;
- conflict-prone high-frequency writes.

Examples that may deserve contour repos:

- `personal-office-job-search`;
- `personal-office-finance-runtime`;
- `personal-office-telegram-gateway`;
- company/project workspaces such as AI Studio, Fincom, Setronica remain separate company repos.

### Avoid Repo Explosion

Do not create a repo for every prompt, small workflow, or agent persona.

Keep small workflows in the core repo as:

- `automation/prompts/`;
- `automation/scripts/`;
- `wiki/playbooks/`;
- `.codex/skills/`;
- `tools/<small-tool>/`.

A new repo is justified only when the contour has enough runtime, security, or lifecycle weight to deserve its own boundary.

### Sync Contract

When a contour repo exists, it must not become an untraceable fork of Personal Office truth.

It must define:

- what it imports from core;
- what it exports back to core;
- where canonical artifacts live;
- how duplicate state is handled;
- what gets committed automatically;
- what requires human review;
- how secrets stay out of Git.

Default contract:

- core owns owner-side decisions and durable summaries;
- contour repo owns runtime state, domain tooling, generated drafts, logs, and service wrappers;
- important outcomes are exported back to core Markdown artifacts.

### Current Recommendation

Start with one Pi-primary Personal Office core repo plus the current `job-search-contour` runtime directory.

Promote `job-search-contour` to a separate repo only after the scheduled Gmail and Telegram loops are working and the boundary is clear enough to avoid premature repo fragmentation.

### Current Implementation

As of 2026-07-01, the Pi-primary Personal Office working tree exists at:

- `/home/openclaw/personal-office-agent/personal-office`

It is owned by the Pi `openclaw` user, tracks:

- `git@github.com:vrezin/pesronal-office.git`

Initial push was performed from the Raspberry Pi using the Pi-side GitHub SSH key:

- branch: `main`
- commit: `f7f447d` (`Add Pi Personal Office storage foundation`)

Note: the GitHub repository name is currently spelled `pesronal-office`.

## Why Not Only Markdown/Git

Markdown/Git is excellent for reviewable artifacts but weak for:

- concurrent or repeated scheduled writes;
- idempotency;
- Gmail/Telegram duplicate detection;
- locks;
- retry/backoff;
- frequent small state updates.

SQLite covers this operational surface without replacing the artifact layer.

## Why Not Only Database

A database-only Personal Office would make the system less inspectable and less portable.

The user-facing operating system must remain readable as files, diffs, and repo history. SQLite supports the runtime; it does not replace the repo.

## Implications For Job Search

The standalone job-search contour should:

- read/write canonical artifacts through the Personal Office repo;
- use SQLite for dedupe and run coordination;
- sync artifacts through the private Git remote;
- send Telegram bot summaries as interaction output;
- never treat Telegram messages, transient model context, or hidden prompt-provided ids as authoritative state.

## Open Implementation Questions

1. Done 2026-07-01: full Personal Office working tree created on Pi as the primary repo.
2. Done 2026-07-01: private Git remote selected and pushed from Pi.
3. Done 2026-07-01: Pi-side GitHub SSH key works for push.
4. Define workstation-as-client workflow and conflict policy.
5. Add scheduled sync wrappers with pull/run/commit/push phases.
6. Decide the backup/export policy for SQLite after unattended scheduling is active.
7. Revisit whether `job-search-contour` should become a separate contour repo after the first scheduled and Telegram E2E loops pass.
