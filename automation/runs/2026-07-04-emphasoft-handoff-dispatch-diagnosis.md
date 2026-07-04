# Emphasoft Handoff Dispatch Diagnosis

- Created: 2026-07-04T18:08:00+07:00
- Status: fixed wrapper / handoff blocked on source data
- Area: automation / personal-brand / job-search
- Handoff: `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-hh-rukovoditel-proektnogo-ofisa-emphasoft-handoff.md`

## User Input

Telegram intake received a forwarded HH recommendation:

- Role: `Руководитель Проектного офиса`
- Company: `Emphasoft`
- URL: `https://my.hh.ru/b/1m1omhr`

The intake agent created the handoff and replied that async analysis was
accepted, but the user did not receive the expected follow-up.

## Failure

The initial async run created:

- `automation/runs/2026-07-04-175846-pi-job-search-handoff-async.md`
- `automation/runs/2026-07-04-175846-pi-job-search-handoff-async-dispatch.md`
- `automation/runs/2026-07-04-1758-pi-job-search-handoff-dispatch.md`

The async dispatch output was empty and the dispatch run log stopped after the
header with `Status: running`. The `pi-job-search-handoff-dispatch` SQLite lock
was not active afterward, and the worker PIDs listed in the async log were no
longer alive.

A direct dispatcher retry before the fix wrote
`automation/runs/2026-07-04-1802-pi-job-search-handoff-dispatch.md` and showed:

```text
env: 'node': No such file or directory
```

## Fix

Updated both handoff wrappers to include the Pi-local Node/OpenClaw PATH in
non-login environments:

- `automation/scripts/dispatch-pi-job-search-handoff.sh`
- `automation/scripts/enqueue-pi-job-search-handoff.sh`

## Verified Retry

After the PATH fix, a manual dispatcher run completed:

- Wrapper run log: `automation/runs/2026-07-04-1804-pi-job-search-handoff-dispatch.md`
- Job-search evidence note: `automation/runs/2026-07-04-180555-pi-job-search-handoff-dispatch.md`
- Dispatcher status: `completed`
- Job-search verdict: `clarify`

Job-search found only:

- the intake handoff;
- `inbox/processed/2026-07-04-hh-ai-solution-architect-thin-digest.md`, which
  lists `Emphasoft | Руководитель Проектного офиса | not shown`.

No full JD, stable HH vacancy id, JD archive, analysis, CV decision, or cover
letter artifact was available.

The runtime did not expose `headhunter_web` as a callable tool, so job-search
correctly did not invent JD details and did not update `INDEX.md` or
`COMPANY_NOTES.md`.

## User Follow-Up

Sent Telegram follow-up through `personal-office-intake-telegram`:

- Target: `113174019`
- Message id: `393`

The follow-up said the bot did not fully die, but the async dispatch failed on
PATH; after the fix, Emphasoft remains blocked/clarify until either full HH JD
text is provided or `headhunter_web` is available in the job-search runtime.

## Remaining Attention

- Investigate why `headhunter_web` is not exposed to the `job-search` handoff
  runtime even though the Pi HH Web contour exists.
- Consider making the async wrapper write a final blocked status if a background
  worker exits before populating dispatch output.
