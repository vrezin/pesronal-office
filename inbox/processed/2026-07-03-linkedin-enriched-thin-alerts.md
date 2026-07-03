# LinkedIn Enriched Thin Alerts

- Date captured: 2026-07-03
- Source: Pi-local Gmail via `google_workspace`
- Gmail message ids:
  - `19f271b115d348ff`
  - `19f26ac5a3077aa0`
- Classification: `new_vacancy`
- Runtime status: `processed`
- Enrichment path: registered OpenClaw LinkedIn MCP `get_job_details`
- Gmail was read-only; no labels, read state, archive state, stars, or importance were changed.

## Email Alerts

### Revolut - Applied AI Engineer

- Gmail id: `19f271b115d348ff`
- LinkedIn job id: `4407473235`
- Email subject: `Applied AI Engineer в компании Revolut`
- Email-visible location: Cyprus

Live LinkedIn enrichment result:

- URL: `https://www.linkedin.com/jobs/view/4407473235/`
- Company: Revolut
- Title: Applied AI Engineer
- Location/status shell: Cyprus; remote; full-time; reposted 1 day ago; more than 100 applicants/clicks; applications managed outside LinkedIn.
- Full JD details: not returned by MCP.

Routing:

- This is not enough for a new analysis because the repo already has a full Revolut Applied AI Engineer analysis: `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-11-revolut-applied-ai-engineer-analysis.md`.
- No index/company-note change was made. The existing decision still stands: maybe / lower priority until Cyprus economics and official channel are clear.

### Ingenio Global - Technical Delivery Director (Bespoke Software Solutions)

- Gmail id: `19f26ac5a3077aa0`
- LinkedIn job id: `4435558976`
- Email subject lead: `Technical Delivery Director (Bespoke Software Solutions) | Ireland | €175k в компании Ingenio Global`
- Email-visible location: Dublin

Live LinkedIn enrichment result:

- URL: `https://www.linkedin.com/jobs/view/4435558976/`
- Company: Ingenio Global
- Title: Technical Delivery Director (Bespoke Software Solutions) | Ireland | €175k
- Location/status shell: Dublin, Ireland; hybrid; full-time; 175K EUR/year; Easy Apply; more than 100 candidates; 4 of 8 skill matches.
- Full JD details: not returned by MCP.

Routing:

- This is a potentially relevant delivery/director salary signal, but the MCP result returned only a shell. No full JD archive or analysis was created.
- Existing Ingenio context in `job-intake/INDEX.md` and `COMPANY_NOTES.md` is for a different Transformation Program Director / AI & Digital Transformation signal. This alert was not merged into that analysis without a full JD.

### Salesforce - Director, Software Engineering

- Gmail id: `19f26ac5a3077aa0`
- LinkedIn job id: `4435869405`
- Email-visible location: Dublin

Live LinkedIn enrichment result:

- URL: `https://www.linkedin.com/jobs/view/4435869405/`
- Company: Salesforce
- Title: Director, Software Engineering
- Location/status shell: Dublin, Ireland; hybrid; full-time; 13 applicants/clicks; applications no longer accepted.
- Full JD details: not returned by MCP.

Routing:

- No analysis was created because the role is already not accepting applications and the enrichment did not return a JD.

## Handoff

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: low
user_intent: vacancy_review
summary: Two LinkedIn alert emails were enriched through LinkedIn MCP, but all returned only title/company/location/status shells rather than full JDs.
verdict: no-op
reasons:
  - Revolut is already tracked in a full existing analysis.
  - Ingenio Global showed a useful 175K EUR Dublin hybrid shell, but no JD details.
  - Salesforce was already not accepting applications.
cv: null
cover_letter: null
next_action: wait for full JD/source text before any new analysis or CV selection.
artifacts:
  - inbox/processed/2026-07-03-linkedin-enriched-thin-alerts.md
  - personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-11-revolut-applied-ai-engineer-analysis.md
blocked_on: []
```
