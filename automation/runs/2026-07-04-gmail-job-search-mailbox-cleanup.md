# Gmail Job Search Mailbox Cleanup

- Timestamp: 2026-07-04 20:00 +07
- Gmail account: `v.rezin@gmail.com`
- Scope: recent LinkedIn and HH/HeadHunter job-search messages in Gmail Inbox
- Operator action: manual verification after Pi `job-search` monitor repair and rerun

## Verification

Pi monitor was rerun manually with the same PATH used by the systemd service after an initial manual shell failed with `env: 'node': No such file or directory`.

Evidence:

- `automation/runs/2026-07-04-1942-pi-job-search-gmail-monitor.md` - failed manual run caused by missing `node` in non-service PATH.
- `automation/runs/2026-07-04-1943-pi-job-search-gmail-monitor.md` - successful wrapper run.
- `automation/runs/2026-07-04-1948-pi-job-search-gmail-monitor.md` - agent-level scan log.

The successful scan saw 5 HH messages and 5 LinkedIn messages. HH was duplicate/no-op. LinkedIn processed two new messages:

- `19f2d1c823d560e7` - Work Channel `Head of Enterprise Architecture` repost; matched existing analysis.
- `19f2cae6dd121264` - Software Engineering Director digest; enriched via LinkedIn MCP and wrote search-run notes.

One older LinkedIn application confirmation was still missing from SQLite and was processed manually:

- `19f219d6bc5fd147` - GRS Recruitment `Head of Enterprise Architecture`, LinkedIn job id `4436190323`; added to `inbox/processed/2026-07-02-linkedin-application-status-updates.md` and marked `status=processed`.

## Gmail Messages Moved To Trash

LinkedIn processed messages:

- `19f2d1c823d560e7`
- `19f2cae6dd121264`
- `19f2bd2bad14dacf`
- `19f28d26975fcb14`
- `19f286471ebc8e9f`
- `19f278839f48b6ab`
- `19f271b115d348ff`
- `19f26ac5a3077aa0`
- `19f233dc54d1f2ba`
- `19f21faa18a56d48`
- `19f21f3f0697f7ec`
- `19f21e3d77f5ca26`
- `19f21ba7638665c1`
- `19f219e32a21d867`
- `19f219d6bc5fd147`
- `19f21181ab1eddb0`
- `19f1e8510ae13eee`

HH processed messages:

- `19f2c6c6fcd8df94`
- `19f280e04b9071b0`
- `19f2742d8e53cee3`
- `19f222a760eeb4d3`

## Left In Inbox

HH Tensor/Saby ambiguous threads were left in Inbox because runtime has `needs_human` items and the thread context should not be split:

- `19f248268018bf80`
- `19f24808a3ca3ecc`
- `19f2344884afb3be`
- `19f2342b5904a58d`

Control Gmail search after cleanup:

- LinkedIn Inbox query returned no messages.
- HH Inbox query returned only the four messages listed above.

## Follow-Up

- Resolve `inbox/processed/needs-clarification-2026-07-03-hh-gmail.md` before deleting or archiving the remaining HH thread messages.
- Consider adding the service PATH to manual run documentation so ad-hoc SSH runs do not fail before OpenClaw starts.
