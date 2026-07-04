# LinkedIn MCP Job Body Extraction Repair

- Date: 2026-07-04
- Runtime: Raspberry Pi / OpenClaw LinkedIn MCP
- LinkedIn job id used for verification: `4436302720`
- Status: repaired and verified after clean restart

## Problem

Pi OpenClaw `linkedin` MCP was running and exposed `linkedin__get_job_details`,
but job-search received only the LinkedIn top-card shell for job `4436302720`.
The agent therefore returned `wait` / `no-op` with "posting shell only" even
though a full JD existed.

This was not an async failure and not an MCP-not-started failure.

## Root Cause

The Pi LinkedIn MCP runtime used the generic page extractor for
`/jobs/view/<id>/`. On LinkedIn job pages, the top card renders first and the
actual "About this job" / `Об этой вакансии` body often appears only after
wheel or inner-container scrolling and expansion controls.

The generic extractor used `window.scrollTo(document.body.scrollHeight)`, which
can miss LinkedIn's job detail body in headless mode.

Trace evidence showed short `after-goto` snapshots for `4436302720`, while later
page state could contain a longer body.

## Repair

Patched the Pi runtime extractor:

- Runtime file:
  `.runtime/job-search-venv/lib/python3.13/site-packages/linkedin_mcp_server/scraping/extractor.py`
- Durable patch file:
  `tools/linkedin-mcp/patches/2026-07-04-job-posting-lazy-body-extraction.patch`
- Startup durability:
  `tools/linkedin-mcp/scripts/start-local.sh` now applies the patch to the
  LinkedIn MCP runtime if the venv is rebuilt and the marker method is missing.

The patch adds job-specific extraction:

- waits for `<main>`;
- clicks visible `Show more` / `See more` / `Read more` / `развернуть` /
  `показать еще` controls;
- scrolls by mouse wheel;
- scrolls the largest scrollable region inside `<main>`;
- captures multiple snapshots;
- returns the richest job posting text.

## Verification

After patching and restarting the Pi LinkedIn MCP server through
`tools/linkedin-mcp/scripts/start-daemon.sh`, raw MCP call:

```bash
LINKEDIN_MCP_URL=http://127.0.0.1:8019/mcp \
  python3 automation/scripts/linkedin-mcp-client.py job-details 4436302720
```

returned full-body markers:

- `Об этой вакансии`: true
- `Head of Engineering (route to CTO)`: true
- `FastAPI`: true
- response length: about 14k chars

After a clean restart, the same markers remained true.

## End-To-End Handoff Verification

Re-ran the original intake handoff:

```bash
automation/scripts/enqueue-pi-job-search-handoff.sh \
  personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md
```

Result:

- Async log:
  `automation/runs/2026-07-04-191958-pi-job-search-handoff-async.md`
- Dispatch output:
  `automation/runs/2026-07-04-191958-pi-job-search-handoff-async-dispatch.md`
- Wrapper dispatch:
  `automation/runs/2026-07-04-1919-pi-job-search-handoff-dispatch.md`
- Agent run log:
  `automation/runs/2026-07-04-192220-pi-job-search-handoff-dispatch.md`
- Telegram follow-up: sent, message id `405`

The agent no longer reported `posting shell only`. It returned:

- `Status: processed; full JD already archived/analyzed, no duplicate artifacts created.`
- `verdict: maybe`
- correct JD archive and analysis artifact paths.

## Remaining Follow-Up

There is a minor async log race: the systemd worker can start appending `## Worker`
before the enqueue wrapper finishes writing `## Enqueue Result`, so those two
blocks can interleave. This does not affect completion, but should be cleaned up
later for readability.
