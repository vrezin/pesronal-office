# LinkedIn Application Status Updates

- Source: Gmail / LinkedIn application notifications
- Date processed: 2026-07-02
- Classification: `status_update`
- Routing result: status notes only; no matched full JD analysis updated

## Updates

| Gmail id | Received | Company | Role | Status | LinkedIn job id | Artifact action |
|---|---|---|---|---|---|---|
| `19f21faa18a56d48` | 2026-07-02 08:38:19 UTC | Jobgether | Deputy CTO (AI Product) | Application submitted on 2026-07-02 | `4432340752` | Recorded status; no full analysis exists for this exact role. |
| `19f219d6bc5fd147` | 2026-07-02 06:56:32 UTC | GRS Recruitment | Head of Enterprise Architecture | Application submitted on 2026-07-02 | `4436190323` | Matched existing GRS analysis; later viewed status is already reflected in analysis/index. |
| `19f21e3d77f5ca26` | 2026-07-02 08:13:26 UTC | GRS Recruitment | Unknown from email body | Application viewed | unknown | Recorded thin status only; LinkedIn email body did not expose the role or job id. |
| `19f21ba7638665c1` | 2026-07-02 07:28:14 UTC | Techyons | Unknown from email body | Application viewed | unknown | Recorded thin status only; LinkedIn email body did not expose the role or job id. |
| `19f219e32a21d867` | 2026-07-02 06:57:21 UTC | Dr.Head | Директор по ИТ | Application submitted on 2026-07-02 | `4434956568` | Recorded status; no full JD analysis exists. |
| `19f2261db60003a6` | 2026-07-02 10:31:05 UTC | Dr.Head | Директор по ИТ | Duplicate LinkedIn job alert after application confirmation | `4434956568` | No new artifact beyond this note; same job id as the submitted application. |

## Triage

- These are real job-search status events, but they do not provide enough role detail to update a known `job-intake/analyses/*.md` file safely.
- Jobgether Deputy CTO also appears in a thin alert and is captured separately in `inbox/processed/2026-07-02-linkedin-thin-jobgether-deputy-cto-alert.md`.
- GRS Recruitment application confirmation exposes `Head of Enterprise Architecture`, job id `4436190323`, and is matched to the existing GRS analysis; the later viewed email exposes only company name but is consistent with the same tracked lane.
- Techyons viewed the application, but the email exposes only company name. Reopen manually only if LinkedIn or another source reveals the exact role.
- Dr.Head application confirmation is a concrete user commitment but the messages have no JD text beyond role/company/location. The later LinkedIn job alert repeats the same job id.

## Next

- No Telegram packet: no immediate action is required.
- Wait for employer/recruiter replies.
- If any company replies, create or update a matched analysis before preparing CV or reply text.
