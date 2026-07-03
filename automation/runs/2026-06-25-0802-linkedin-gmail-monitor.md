# LinkedIn Gmail Monitor Run - 2026-06-25 08:02

Status: success

Started from state:

- Last successful scan: 2026-06-24 22:01:52 +07
- Last processed Gmail message id: `19efa0a9ac916376`
- Last processed Gmail internal date: `2026-06-24T14:30:57`

Gmail query:

`from:linkedin.com after:2026/6/22 -in:spam -in:trash`

Gmail returned 7 messages in the overlap. Messages newer than the previous internal-date marker were processed; older overlap messages were kept as already-processed context.

## Classification

| Gmail id | Time | Subject | Classification | Action |
|---|---:|---|---|---|
| `19efb64ec236ac2b` | 2026-06-24T20:49:15 | IT Consulting request from VISHWARADHYA YADRAMI and other clients are available. Show Requests. | invitation / service-lead signal | Created `tasks/active/2026-06-25-review-linkedin-service-request-vishwaradhya-yadrami.md`. No Gmail mutation. |
| `19efb4f420ca3235` | 2026-06-24T20:25:35 | Suleiman replied to your InMail | noise | Promotional/community access reply. No task. No Gmail mutation. |
| `19efa9b6ee459dd0` | 2026-06-24T17:09:02 | New jobs similar to Amazon Software Development Manager, ICON | new_vacancy digest | Enriched selected job ids via registered `linkedin` MCP and wrote job-intake artifacts. |
| `19efa8b2dd7e1943` | 2026-06-24T16:31:03 | n8n is hiring Director of Engineering Europe Remote / jobs that may interest you | new_vacancy digest | Amendment after consistency check: enriched selected job ids and added FYST / Pipekit artifacts. n8n/Jobgether treated as duplicate evidence. |
| `19ef99cbe907c49b` | 2026-06-24T12:30:57 | Director of Software Engineering at OAG | already processed overlap | Existing OAG task/analysis from 2026-06-24 remains current. |
| `19ef92ee1992ed1c` | 2026-06-24T10:30:57 | Azure Cloud Engineering Team Lead at MUFG Investor Services | already processed overlap | Existing parked MUFG analysis from 2026-06-24 remains current. |
| `19eed83e76c11897` | 2026-06-22T04:08:22 | Kirill sent you a message | already processed overlap | Prior KLEVRS overlap/noise. |

## LinkedIn MCP Enrichment

Registered local MCP server `linkedin` was available. No daemon fallback was started.

Enriched job ids:

- `4428908413` - Discovered MENA, Head of Delivery - AI Programme.
- `4420918427` - Nearform, Technical Director (Ireland remote).
- `4432243019` - Elevate Partners, Head of Digital & AI Design / Head of AI Transformation.
- `4428949152` - Zebra People, VP of Artificial Intelligence.
- `4427335027` - Surge Group, CTO / Head of Trading Engineering.
- `4432027209` - n8n, Director of Engineering Europe Remote duplicate.
- `4432022043` - FYST, Head of Engineering / CTO partner company.
- `4413246249` - Pipekit, Head of Engineering.
- `4430852805` - Jobgether, Director of Engineering, likely n8n mirror/partner listing.
- `4423631732` - RecT Solutions, Founding Head of AI.
- `4402513814` - Ataccama, Head of AI.
- `4432022223` - n8n, Director of Engineering Europe Remote duplicate.

## Vacancy Outcomes

- Discovered MENA: B-class / maybe, active review task created, Abu Dhabi relocation gate.
- Nearform: B-class / maybe, active clarification task created, Ireland residency/right-to-work gate.
- Elevate Partners: B/C-class / maybe, active clarification task created, Ireland hybrid/on-site gate.
- Zebra People: C-class parked, no active task, hard Graph ML player-coach screen.
- Surge Group: C-class closed, no active task, applications closed and HFT hard screen.
- n8n: duplicate signal only; existing waiting task updated, no duplicate lane.
- FYST: B+ / maybe, active clarification task created, compensation/legal/hands-on gate.
- Pipekit: B-class / maybe, active clarification task created, high-compensation workflow-infrastructure signal.
- Jobgether: treated as likely n8n mirror/partner listing; no duplicate lane.
- RecT Solutions: parked; strong e-commerce AI-agent product signal, but Lisbon on-site blocks default action.
- Ataccama: parked; useful agentic data-trust product signal, but Prague hybrid and product-management shape make it low priority.

## Files Created

- `tasks/active/2026-06-25-review-linkedin-service-request-vishwaradhya-yadrami.md`
- `tasks/active/2026-06-25-review-discovered-mena-head-ai-delivery.md`
- `tasks/active/2026-06-25-clarify-fyst-head-engineering-cto.md`
- `tasks/active/2026-06-25-clarify-pipekit-head-engineering.md`
- `tasks/active/2026-06-25-clarify-nearform-technical-director-ireland.md`
- `tasks/active/2026-06-25-clarify-elevate-partners-head-digital-ai-design.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-25-discovered-mena-head-ai-delivery.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-25-nearform-technical-director-ireland-remote.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-25-elevate-partners-head-digital-ai-design.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-25-zebra-people-vp-artificial-intelligence.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-25-surge-group-cto-head-trading-engineering.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-25-fyst-head-engineering-cto-partner-company.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-25-pipekit-head-engineering.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-25-discovered-mena-head-ai-delivery-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-25-nearform-technical-director-ireland-remote-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-25-elevate-partners-head-digital-ai-design-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/summaries/2026-07-01-closed-parked-vacancies-rollup.md`
- `personal-projects/personal-brand/workspace/job-intake/summaries/2026-07-01-closed-parked-vacancies-rollup.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-25-fyst-head-engineering-cto-partner-company-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-25-pipekit-head-engineering-analysis.md`

## Files Updated

- `automation/state/linkedin-gmail-monitor-state.md`
- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-24-n8n-director-engineering-europe-remote-analysis.md`
- `tasks/waiting/2026-06-24-n8n-director-engineering-linkedin-status-confirmation.md`

## Limitations

- Gmail cleanup policy followed: no labels, stars, archive state, importance, or messages were mutated.
- Live market-salary web search returned no usable result in this unattended environment. Analyses mark market benchmarks as unverified rather than inventing numbers.
- No mutating Git command was attempted by policy. A read-only `git status --short` inspection was run during verification and did not block the monitor.
