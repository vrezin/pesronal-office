# LinkedIn Job Alert Handoff 4434956568

- Created: 2026-07-02
- Source: Telegram direct intake
- URL: `https://www.linkedin.com/comm/jobs/view/4434956568/?trackingId=cPmhpR%2FMuRGhFwa0pHTvSA%3D%3D&refId=ekEGRNqTXA%2B7GK7HRAwKyw%3D%3D&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BgwQnNkujTgSjEDMG7IfLgA%3D%3D&midToken=AQEzSot68OyD6w&midSig=0KkDqTcPrTrYk1&trk=eml-email_job_alert_digest_01-primary_job_list-0-jobcard_body_0-jobid_4434956568_ssid_4090828529_fmid_1peu9~mr3d66wv~tp&trkEmail=eml-email_job_alert_digest_01-primary_job_list-0-jobcard_body_0-jobid_4434956568_ssid_4090828529_fmid_1peu9~mr3d66wv~tp-null-1peu9~mr3d66wv~tp-null-null&eid=1peu9-mr3d66wv-tp&otpToken=MTAwZDE4ZTUxMDJhYzBjZWI1MjkwZGU4NGYxNmVmYjY4OWNiZDI0Nzk4YTQ4YTZmNzJjZTA4NmU0ODU5NWNmOWI3ODE4NDgzNzdlN2NmZTE4ODRkNzE2ZDQzMjVkNTA1Y2ViZjcyNjZmYzNlMTBiMiwxLDE%3D`
- Classification: `plain_linkedin_job_alert_link`
- Route: `personal-projects/personal-brand/workspace/job-intake/`
- Status: Routed to job-search contour; no deep JD analysis performed by intake

## Handoff

Treat this as a job-search intake item. Fetch the full posting and analyze it only inside the job-search contour if the user asks to review, apply, archive, or compare it.

## Next

Job-search contour should decide whether to fetch the vacancy details, archive the JD, and create a normal vacancy analysis.

## Dispatcher Result

- Checked: 2026-07-02
- Run log: `automation/runs/2026-07-02-1843-pi-job-search-handoff-dispatch.md`
- Result: `wait / no-op`
- Summary: LinkedIn job `4434956568` was already captured as Dr.Head `Директор по ИТ` application submitted on 2026-07-02; this later alert is a duplicate/no-op for the same LinkedIn job id.
- Live source: LinkedIn was reachable, but exposed only thin status/posting shell details and no full JD. It also showed that applications are no longer accepted.
- Next: wait for a Dr.Head reply. If they respond, fetch or request the full JD before preparing a normal analysis, CV decision, or reply text.
