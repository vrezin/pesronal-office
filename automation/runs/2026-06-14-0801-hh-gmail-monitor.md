# HH Gmail Monitor Run

- Run started: 2026-06-14 08:01 +07
- State marker before run: 2026-06-14 04:00:00 +07
- Last processed Gmail message id before run: `19ec0d3d9c40220d`
- Last processed Gmail internal date before run: 2026-06-13T11:52:49
- Gmail access: available
- Repository write access: available
- Git commit access: unavailable (`fatal: Unable to create '/home/adre/personal-office/.git/index.lock': Read-only file system`)

## Search

- Overlap query: HH.ru / HeadHunter messages after 2026-06-13, excluding spam/trash.
- Freshness query: HH.ru / HeadHunter messages newer than 2 days, excluding spam/trash.

## Results

- Messages returned by overlap search: 1
- Messages returned by freshness search: 1
- New messages after the stored state marker: 0
- Re-seen overlap message: `19ec0d3d9c40220d`, `2026-06-13T11:52:49`, subject `Подходящие вакансии для резюме: «Директор по разработке / Технический лидер бизнес-юнита»`.

## Classification

| Message id | Classification | Action |
|---|---|---|
| `19ec0d3d9c40220d` | already_processed / overlap | No artifact updates; already covered by previous successful run. |

## Artifact Updates

- No vacancy, task, analysis, company-note, or index artifacts were changed.
- State file left unchanged because the required commit failed in this cron/sandbox context.

## Gmail Actions

- No Gmail labels, stars, importance markers, archive state, or deletion state were changed.
- Recommended Gmail action: none.

## Commit

- Commit attempted with message `chore: record hh gmail monitor run`.
- Commit failed: `.git/index.lock` could not be created because the Git metadata directory is read-only.
- Per monitor rules, repository changes were left in place where possible and the successful scan marker was not advanced.

## Outcome

Blocked after successful Gmail scan: Gmail scan completed and no new HH.ru / HeadHunter messages required processing, but the required repository commit was unavailable. State marker remains at the previous successful scan.
