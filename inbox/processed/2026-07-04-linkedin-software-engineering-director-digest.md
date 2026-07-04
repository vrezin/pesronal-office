# LinkedIn Software Engineering Director Digest

- Date processed: 2026-07-04
- Gmail message id: `19f2cae6dd121264`
- Source: LinkedIn job alert
- Classification: `new_vacancy`
- Runtime status: `processed`
- Search-run analysis: `personal-projects/personal-brand/workspace/job-intake/search-runs/2026-07-04-linkedin-software-engineering-director-digest.md`

## Summary

The email contained a LinkedIn `Software Engineering Director` digest with six job cards. LinkedIn MCP enrichment returned full JDs for all checked job ids.

## Enriched Job IDs

| LinkedIn id | Company | Role | Routing |
|---|---|---|---|
| `4436302720` | Techmunity | Head of Software Engineering | Already analyzed; UK logistics gate remains. |
| `4436316766` | Dawn Health | Director of Engineering | Park / C-B; Copenhagen on-site. |
| `4432797122` | El Corte Ingles | Head of Agentic SDLC | Strong market signal; clarify Madrid hybrid and salary before action. |
| `4433161733` | MRJ Recruitment / unnamed Manchester SaaS | Head of Engineering route to CTO | Interesting content; clarify UK remote legality and compensation. |
| `4432772384` | SETESCA / unnamed industrial company | Head of Digital Solutions & AI | Useful Microsoft/AI governance signal; Spanish hybrid/on-site gate. |
| `4436341024` | ReasonLabs | Director of Engineering | Strong AI fraud-prevention signal; Israel hybrid and domain screens block default action. |

## Routing

Created a batch search-run and updated `job-intake/INDEX.md` / `COMPANY_NOTES.md`. No CV, cover letter, application, Gmail mutation, or Telegram send was made.

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: LinkedIn Software Engineering Director digest produced several enriched senior AI/engineering roles.
verdict: maybe
reasons:
  - El Corte Ingles and MRJ have strong AI-first engineering leadership language.
  - Every role has a location/legal blocker before application effort.
  - Existing Techmunity analysis remains the source of truth for the top card.
cv: null
cover_letter: null
next_action: Treat as sourcing; clarify only El Corte Ingles or MRJ if the user wants to reopen Spain/UK lanes.
artifacts:
  - inbox/processed/2026-07-04-linkedin-software-engineering-director-digest.md
  - personal-projects/personal-brand/workspace/job-intake/search-runs/2026-07-04-linkedin-software-engineering-director-digest.md
blocked_on:
  - Whether Spain hybrid, UK remote/legal setup, Israel hybrid, or Copenhagen on-site are worth pursuing.
```
