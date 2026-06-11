# LinkedIn Vacancy Scan

- Date: 2026-06-11
- Source: Gmail `from:linkedin.com` scan with LinkedIn MCP enrichment
- Scan window: messages newer than the previous successful marker, with a small overlap to avoid misses

## Messages Processed

1. Overstory - `Director of Platform Engineering`
   - Classification: `new_vacancy`
   - Result: archived and analyzed using LinkedIn MCP job details
   - LinkedIn job ids: `4398306884`, `4398320320`
   - Updated artifacts:
     - `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-11-overstory-director-of-platform-engineering.md`
     - `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-11-overstory-director-of-platform-engineering-analysis.md`
     - `tasks/active/2026-06-11-overstory-director-of-platform-engineering.md`

2. Revolut - `Applied AI Engineer`
   - Classification: `new_vacancy`
   - Result: archived and analyzed using LinkedIn MCP job details
   - LinkedIn job id: `4407473235`
   - Updated artifacts:
     - `personal-projects/personal-brand/workspace/job-intake/jd-archive/2026-06-11-revolut-applied-ai-engineer.md`
     - `personal-projects/personal-brand/workspace/job-intake/analyses/2026-06-11-revolut-applied-ai-engineer-analysis.md`
     - `tasks/active/2026-06-11-revolut-applied-ai-engineer.md`

3. Jobgether - `Director of Engineering`
   - Classification: overlap duplicate / already processed
   - Result: skipped without changing vacancy artifacts

## Follow-Up Notes

- No Gmail labels, stars, importance markers, archive state, or other mailbox state were changed during this unattended run.
- The previous Revolut thin-digest task was superseded by the full job-id-backed analysis.
