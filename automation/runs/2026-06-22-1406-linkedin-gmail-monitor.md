# LinkedIn Gmail Monitor Run - 2026-06-22 14:06 +07

Status: success

## State Read

- Previous last successful scan: 2026-06-21 22:01:48 +07
- Previous last processed Gmail message id: `19eea97a7f12669f`
- Previous last processed Gmail internal date: `2026-06-21T14:31:06`

## Gmail Scan

Query used:

```text
from:linkedin.com after:2026/6/21 -in:spam -in:trash
```

Overlap was intentional because Gmail search by date is day-granular.

Found and read two LinkedIn messages:

| Gmail id | Timestamp | Subject | Classification | Action |
|---|---:|---|---|---|
| `19eee066f3ec2898` | 2026-06-22T06:30:57 | `Senior Director, Engineering в компании Relativity` | `new_vacancy` | Enriched job ids via LinkedIn MCP; created job-intake artifacts, tasks and processed note. |
| `19eed83e76c11897` | 2026-06-22T04:08:22 | `Kirill только что отправил(а) вам сообщение` | `noise` | Checked LinkedIn thread; recorded processed noise note. |

## LinkedIn MCP

Registered `mcp__linkedin` server was available. No fallback daemon start was needed.

Enriched job ids:

- `4371847609` - Relativity, Senior Director, Engineering.
- `4371856267` - Relativity duplicate city posting, covered by `4371847609`.
- `4422012219` - Signify Technology, Head of Engineering.
- `4430312912` - Jack & Jill / Model ML, Head of Platform Engineering; applications no longer accepted.
- `4399428033` - ServiceNow, Director, Impact Engineering.
- `4420985185` - Ford Credit, Director of Engineering - Digital Products.

Checked LinkedIn thread:

- Kirill Shpak thread `2-M2I0ZDllZDMtODliMC00ZWQ1LWE2ZDItNTJlMzhlMjZiNTJmXzEwMA==`.
- Result: cold outreach-plan follow-up for Hidden, not a vacancy, recruiter follow-up, paid lead, or useful job-search signal. User had already replied that it was not relevant.

## Vacancy Decisions

| Company | Role | Rank | Reason |
|---|---|---|---|
| ServiceNow | Director, Impact Engineering | interesting | Strongest content fit: enterprise AI product leadership, retrieval, recommendations, privacy, evaluation and engineering quality. Main gates are Ireland legal/location and compensation. |
| Relativity | Senior Director, Engineering | maybe / interesting after location check | Strong senior SaaS/AI leadership with visible 530,000-796,000 PLN compensation, but likely Poland-site leadership requirement. |
| Ford Credit | Director of Engineering - Digital Products | maybe / parked | Good enterprise finance/digital transformation fit, but Dunton 4-days/week campus expectation is a major family/lifestyle blocker. |
| Signify Technology | Head of Engineering | not interesting / weak signal | London hybrid, unnamed client and C++/low-latency hard-filter risk. |
| Jack & Jill / Model ML | Head of Platform Engineering | closed / no action | Salary signal is strong, but LinkedIn says applications are no longer accepted. |

## Artifacts Created

- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-22-servicenow-director-impact-engineering.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-22-servicenow-director-impact-engineering-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-22-relativity-senior-director-engineering.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-22-relativity-senior-director-engineering-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/parked/2026-06-22-ford-credit-director-engineering-digital-products.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/parked/2026-06-22-ford-credit-director-engineering-digital-products-analysis.md`
- `personal-projects/personal-brand/workspace/job-intake/jd-archive/parked/2026-06-22-signify-technology-head-engineering.md`
- `personal-projects/personal-brand/workspace/job-intake/analyses/parked/2026-06-22-signify-technology-head-engineering-analysis.md`
- `inbox/processed/2026-06-22-linkedin-software-engineering-director-alert.md`
- `inbox/processed/2026-06-22-linkedin-kirill-shpak-outreach-noise.md`
- `tasks/active/2026-06-22-servicenow-director-impact-engineering.md`
- `tasks/active/2026-06-22-relativity-senior-director-engineering.md`
- `tasks/active/2026-06-22-ford-credit-director-engineering-digital-products.md`
- `tasks/active/2026-06-22-signify-technology-head-engineering.md`

## Artifacts Updated

- `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- `personal-projects/personal-brand/workspace/job-intake/COMPANY_NOTES.md`
- `automation/state/linkedin-gmail-monitor-state.md`

## Limitations

- Gmail was read-only. No labels, stars, archive state, importance markers or messages were mutated by policy.
- No Git command was attempted by policy.
- External market salary search did not return usable benchmark sources in this unattended run. For postings without stated salary, analyses mark market salary as not live-verified and require compensation-band clarification.

## Recommended Gmail Actions

- Archive `19eee066f3ec2898` manually after review; useful vacancy data is captured.
- Archive `19eed83e76c11897` manually; it is cold outreach noise.
