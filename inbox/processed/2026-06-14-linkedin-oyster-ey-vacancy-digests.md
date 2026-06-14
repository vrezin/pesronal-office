# LinkedIn Vacancy Digests - Oyster And EY

- Date processed: 2026-06-14
- Source: Gmail / LinkedIn job alerts
- Classification: `new_vacancy`
- Routing decision: two primary job-alert cards enriched through LinkedIn MCP and promoted into job intake

## Gmail Evidence

| Gmail id | Timestamp | Subject | Result |
|---|---:|---|---|
| `19ec543614d183c0` | 2026-06-14T08:33:05 | `Senior Director, Data Platform and AI в компании Oyster®` | Promoted to full job intake after LinkedIn MCP enrichment. |
| `19ec4d37face4463` | 2026-06-14T06:30:55 | `FS Technology Consulting - Engineering Lead, Features Team- Director - Dublin в компании EY` | Promoted to full job intake after LinkedIn MCP enrichment. |

## Oyster Digest Cards

The Oyster alert listed several cards. The primary card had the strongest AI-platform and workflow-transformation signal and was enriched:

- `Oyster` - `Senior Director, Data Platform and AI`, Barcelona remote, job id `4424899985`
- `Presight` - `Engineering Director`, Abu Dhabi onsite, job id `4427992541`
- `Selby Jennings` - `Head of engineering`, Amsterdam, job id `4417656397`
- `Halliburton` - `Head of Developer Experience`, Oslo, job id `4427200231`
- `Vinted` - `Director of Engineering, Foundations`, Vilnius hybrid, job id `4399281818`
- `Collinson Group` - `Director of Engineering`, Greater London hybrid, job id `4424875313`

Selby Jennings already exists in the job-intake workflow as an applied/waiting role. The remaining cards stayed trace-only in this unattended run because they did not include JD text in Gmail and were lower signal than Oyster.

## EY Digest Card

The EY alert contained one primary job card:

- `EY` - `FS Technology Consulting - Engineering Lead, Features Team- Director - Dublin`, Dublin hybrid, job id `4385040545`

LinkedIn MCP returned a full JD, so the role was promoted into job intake.

## Processing Notes

- LinkedIn MCP enrichment used the registered `mcp__linkedin` server.
- Oyster was ranked `interesting` because it directly matches AI platform, organizational AI adoption, knowledge architecture, LLM orchestration, and remote-first work.
- EY was ranked `maybe` because it is credible director-level engineering consulting with visa sponsorship, but weaker against the current AI-product / AI-solution direction and likely requires Dublin hybrid relocation.
- No Gmail labels, stars, read/unread state, or archive state were changed.

## Next Step

- Review the new active task for Oyster first.
- Review EY only if Dublin relocation / hybrid consulting remains acceptable.
