# LinkedIn 4436302720 Pi Extraction Diagnosis

- Date: 2026-07-04
- Runtime: Raspberry Pi / OpenClaw job-search handoff
- LinkedIn job id: `4436302720`
- Status: Pi LinkedIn MCP extraction parity issue found

## Symptom

Telegram intake created:

- `personal-projects/personal-brand/workspace/job-intake/processed/2026-07-04-linkedin-job-alert-4436302720-handoff.md`

The async handoff completed technically, but the job-search agent returned
`wait` / `no-op` and said LinkedIn exposed only a posting shell.

Relevant Pi logs:

- `automation/runs/2026-07-04-185817-pi-job-search-handoff-async.md`
- `automation/runs/2026-07-04-1858-pi-job-search-handoff-dispatch.md`
- `automation/runs/2026-07-04-190623-pi-job-search-handoff-async.md`
- `automation/runs/2026-07-04-190737-pi-job-search-handoff-dispatch.md`

## What Was Checked

Pi OpenClaw MCP status:

- `linkedin`: `streamable-http`
- `openclaw mcp doctor linkedin`: `ok`
- `openclaw mcp probe linkedin --json`: exposed 17 tools, including
  `linkedin__get_job_details`

So this was not an MCP-not-started problem.

## Contradiction

The direct LinkedIn MCP connector available in the current Codex session returned
the full `sections.job_posting` body for job `4436302720`, including:

- "Head of Engineering (route to CTO)"
- UK AI startup led by Imperial and Cambridge-trained founders
- GBP 1M ARR before GBP 2.7M seed
- mobility data / geospatial / AI recommendations problem statement
- hands-on engineering leadership scope
- 7 IC team
- requirements around Seed-to-Series-A/B, data platforms, production AI, AI
  coding tools, React, TypeScript, Python, FastAPI, Dagster, dbt, Snowflake, AWS
- GBP 100,000-120,000 base and 0.5-0.75% equity
- UK-based remote with 2-4 London/Bristol team days per month

The Pi job-search agent, using the Pi LinkedIn MCP runtime, reported that its
`sections.job_posting` had no "About this job" / "Об этой вакансии" body.

## Immediate Mitigation

Created source-backed job-intake artifacts from the full direct LinkedIn MCP
result:

- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-07-04-techmunity-head-software-engineering.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-07-04-techmunity-head-software-engineering-analysis.md`

## Follow-Up

The remaining defect is Pi LinkedIn MCP extraction parity:

- either the Pi browser profile/session sees a reduced LinkedIn variant;
- or the Pi MCP extractor fails to expand/read the job body in headless mode;
- or the Pi job-search agent is reading an incomplete tool response while the
  direct connector can access the full posting.

The next repair should compare raw `linkedin__get_job_details` output from the
Pi MCP server against the direct connector output and then fix the Pi connector
or add a fallback source for LinkedIn jobs before returning `wait`.
