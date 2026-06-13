# LinkedIn Gmail Monitor Run

- Run started: 2026-06-13 16:03:00 +07
- State before run: last successful scan `2026-06-13 12:01:15 +07`; last processed Gmail message id `19ebed16cf95fd9f`; last processed internal date `2026-06-13T02:30:55`
- Gmail query: `from:linkedin.com newer_than:2d -in:spam -in:trash`
- Gmail cleanup: no labels, stars, importance, or archive state were changed.

## Result

Status: processed with repository commit limitation.

Six LinkedIn messages were returned by the overlap search. Three were older/already covered by the state marker, and three newer messages were processed.

## Processed Messages

| Gmail id | Timestamp | Subject | Classification | Action |
|---|---:|---|---|---|
| `19ebfad6cc4c3f36` | 2026-06-13T06:31:11 | `Head of Engineering в компании Vyking` | `new_vacancy` | Thin digest trace created; no full analysis because the email did not include enough JD text. |
| `19ec01c84fd1f9a8` | 2026-06-13T08:32:32 | `Head of Engineering в компании Vyking` | `new_vacancy` | Duplicate/overlap digest for the same Vyking job id `4423658753`; included in the same thin trace. |
| `19ec02d1e17a3e66` | 2026-06-13T08:50:42 | `Ваша заявка на вакансию «Head of Engineering» в компании Shaw Daniels Solutions` | `status_update` | Shaw Daniels application marked rejected and closed. |

## Artifact Updates

- Moved `tasks/waiting/2026-06-10-shaw-daniels-head-of-engineering-employer-response.md` to `tasks/done/2026-06-13-shaw-daniels-head-of-engineering-rejected.md`.
- Updated `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-10-shaw-daniels-solutions-head-of-engineering-analysis.md` with the rejection status.
- Updated `personal-projects/personal-brand/workspace/job-intake/INDEX.md` for Shaw Daniels from `applied / waiting for reply` to `rejected`.
- Created `inbox/processed/2026-06-13-linkedin-vyking-digest-thin-links.md`.

## LinkedIn MCP Enrichment

Enrichment was attempted for the new LinkedIn job ids, starting with `4423658753`.

- Registered/local client path failed before connection: `ModuleNotFoundError: No module named 'pydantic_core._pydantic_core'`.
- `tools/linkedin-mcp/scripts/start-daemon.sh` was run once, as required.
- The daemon did not become usable on port `8019`; its log showed an attempted FastMCP startup followed by `could not bind on any address out of [('127.0.0.1', 8019)]`.

Because enrichment was unavailable and the emails were thin digests, no new full JD analysis or job-intake index row was created for Vyking or the related digest links.

## Commit And State Update

The repository changes were left in place but not committed.

Commit could not be completed cleanly in this cron sandbox because `.git/index.lock` could not be created while selectively staging the Shaw Daniels row in `job-intake/INDEX.md`; the git metadata is not reliably writable in this environment. The worktree also already contained unrelated unstaged changes in `job-intake/INDEX.md`, so staging the whole file would have mixed this monitor run with unrelated work.

Following the monitor contract, `automation/state/linkedin-gmail-monitor-state.md` was left unchanged. The next run should rescan from:

- Last successful scan: 2026-06-13 12:01:15 +07
- Last processed Gmail message id: `19ebed16cf95fd9f`
- Last processed Gmail internal date: `2026-06-13T02:30:55`

If this run is later committed manually, the intended successful marker would be:

- Last successful scan: 2026-06-13 16:03:00 +07
- Last processed Gmail message id: `19ec02d1e17a3e66`
- Last processed Gmail internal date: `2026-06-13T08:50:42`
