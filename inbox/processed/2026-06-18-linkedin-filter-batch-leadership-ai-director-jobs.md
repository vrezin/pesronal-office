# LinkedIn Filter Batch - Leadership / AI / Director Jobs

- Created: 2026-06-18
- Source: user-pasted LinkedIn search/filter URLs
- Status: processed
- Enrichment: LinkedIn MCP `get_job_details` succeeded for 25 unique job IDs
- Raw local capture: `/tmp/linkedin_job_details_2026-06-18.jsonl`

## Source Filters

The pasted links represented LinkedIn job-alert/search collections for:

- `Технический директор`
- `Director of Software Engineering`
- `Главный инженер`
- recommended / similar jobs collections
- `Software Engineering Director`

## First-Pass Shortlist

| Priority | Job ID | Company | Role | Location / format from LinkedIn | First-pass verdict |
|---|---:|---|---|---|---|
| High | 4389271882 | Umain | AI Tech Director | Stockholm, Sweden | Strong AI Solution Architect / AI Transformation fit. Consulting, client strategy, AI solution architecture, QA/delivery, commercial shaping. Needs location/legal/remote check. |
| High | 4427006978 | The Agile Monkeys | General Manager, AI Software Services | Spain / US, hybrid or remote with US client time | Strong AI services + regulated industries + P&L ownership. Less pure hands-on engineering, but very aligned to AI-first services and mature-company implementation. |
| Medium-high | 4414371021 | Anyfin | We're not looking for a traditional CTO | Stockholm, Sweden; remote/hybrid signals in page | Interesting non-traditional CTO: fintech, AI-in-workflow, business/tech ownership. Needs eligibility/location check and likely very competitive. |
| Medium | 4427354856 | the LEGO Group | Director of Engineering, Customer Data Foundation | Copenhagen, Denmark; hybrid | Strong data/platform director role, but less AI-first and likely relocation/hybrid gate. |
| Medium | 4399281818 | Vinted | Director of Engineering, Foundations | Vilnius, Lithuania; hybrid/relocation signals | Strong infrastructure/platform leadership, but not current AI-first focus. More Heavy Enterprise / Platform. |

## Duplicates / Already Known

| Job ID | Company | Role | Status |
|---:|---|---|---|
| 4424899985 | Oyster | Senior Director, Data Platform and AI | Already applied / waiting; do not duplicate. |
| 4423658753 | Vyking | Head of Engineering | Already applied / recorded from prior LinkedIn digest. |
| 4417656397 | Selby Jennings | Head of engineering | Already analyzed / prior LinkedIn intake. |
| 4398385667 | Last Mile Solutions | Head of Engineering | Already appeared in Vyking-related digest trace. |
| 4423694387 | Superhuman | Director, Engineering | Already appeared in Vyking-related digest trace. |
| 4424862632 | Socium | Director of Engineering | Already appeared in Vyking-related digest trace. |
| 4426100284 | Tide | Director of Client Engineering | Already appeared in Vyking-related digest trace. |
| 4426624244 | Signify Technology | Head of Software Engineering (Europe) | Already appeared in Vyking-related digest trace. |
| 4427992541 | Presight | Engineering Director | Already appeared in Oyster-related digest trace. |
| 4427200231 | Halliburton | Head of Developer Experience | Already appeared in Oyster-related digest trace. |
| 4424875313 | Collinson Group | Director of Engineering | Already appeared in Oyster-related digest trace. |

## Low-Priority / Practical Gates

| Job ID | Company | Role | Reason |
|---:|---|---|---|
| 4429945542 | vialytics | VP of Engineering | LinkedIn MCP only returned header/no useful JD; remote Germany signal but not enough evidence. |
| 4429946376 | vialytics | VP of Engineering | Same role as above, duplicate location variant. |
| 4429969346 | OptiComm.ai | Head of Artificial Intelligence | Title fit, but LinkedIn MCP returned header/no JD; onsite Bucharest. |
| 4406147415 | Lovol Global | Senior Director of Engineering | Engineering director signal, but not obviously AI-first and likely Germany/onsite-heavy. |
| 4423141698 | Stealth Startup | Chief Technology Officer [33188] | Could be hands-on sales/solutions CTO, but stealth/early-stage risk and Sweden location gate. |
| 4426853443 | Mastercard | Director, Software Engineering | Dublin hybrid; user already treats Ireland/UK as low-probability / low-interest. |
| 4417881460 | Kraken | Staff React Native Engineer - Pro | Downlevel / IC mobile role; skip. |
| 4427018551 | ASMALLWORLD | CTO | Spain travel/lifestyle CTO; not AI-first enough from first pass. |
| 4425765279 | Tribe | Head of development | Cyprus; not enough JD text and likely generic head-of-development. |

## Recommendation

Do not process all 25 into full job-intake artifacts. Create full analyses only for:

1. Umain - `AI Tech Director`
2. The Agile Monkeys - `General Manager, AI Software Services`
3. Anyfin - `We're not looking for a traditional CTO`

Optionally review LEGO/Vinted later only if the search shifts back toward platform/director roles with relocation.

## Notes

- LinkedIn MCP is usable when the local server is run in a foreground host session on `127.0.0.1:8019`.
- The Codex sandbox cannot see that host loopback endpoint directly; host-level command execution was needed for MCP JSON-RPC calls.
