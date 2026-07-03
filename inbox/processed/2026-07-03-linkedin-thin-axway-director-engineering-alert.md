# LinkedIn Thin Job Alert - Axway - Director, Engineering

- Date captured: 2026-07-03
- Source: Pi-local Gmail via `google_workspace`
- Gmail message id: `19f233dc54d1f2ba`
- Classification: `new_vacancy`
- Runtime status: `processed`
- Job source: LinkedIn job alert for `Director of Software Engineering` in Dublin
- LinkedIn job id: `4435338298`
- Company: Axway
- Role: Director, Engineering
- Location: Dublin
- Gmail was read-only; no labels, read state, archive state, stars, or importance were changed.

## Source Summary

The email is a thin LinkedIn job alert. It exposes the company, title, location, and LinkedIn job id, but does not include a full job description, compensation, remote/legal setup, relocation support, team scope, or requirements.

## LinkedIn MCP Enrichment

- Checked: 2026-07-03
- Tool path: `automation/scripts/linkedin-mcp-client.py job-details 4435338298`
- MCP endpoint: `http://127.0.0.1:8019/mcp`
- Result: live LinkedIn source still exposes only a posting shell.

The LinkedIn MCP returned:

- Company: Axway
- Role: Director, Engineering
- Location: Dublin, Ireland
- Posted: 2 days ago
- Signal: 34 people clicked Apply
- Application flow: outside LinkedIn
- Type: full-time

The live source did not expose full JD text, responsibilities, requirements, compensation, remote/legal setup, relocation support, team scope, or hiring-manager details. Treat this as a source limitation, not as a skipped enrichment.

## Routing Decision

Do not create a full JD archive or analysis from this email alone.

This is only a thin market signal unless a later operator action retrieves the full job description from another source. The existing `Director of Software Engineering` Dublin/Ireland cluster already notes that Ireland/UK legal setup and relocation economics are first gates.

## Handoff

```yaml
handoff_type: user_reply
source_agent: job-search
domain: personal-brand/job-search
priority: normal
user_intent: vacancy_review
summary: Thin LinkedIn alert for Axway Director, Engineering in Dublin; not enough JD detail to analyze or recommend an application.
verdict: no-op
reasons:
  - Email contains only title, company, location, and LinkedIn job id.
  - LinkedIn MCP enrichment was attempted and also returned only a posting shell.
  - Dublin/Ireland roles are already gated by legal setup, relocation interest, and compensation.
cv: null
cover_letter: null
next_action: ignore unless the full LinkedIn JD is retrieved later or the user explicitly asks to review Axway.
artifacts:
  - inbox/processed/2026-07-03-linkedin-thin-axway-director-engineering-alert.md
blocked_on: []
```
