# LinkedIn Similar Jobs Digest - Overstory Platform Engineering

- Date processed: 2026-06-14
- Source: Gmail / LinkedIn viewed-job reminder
- Gmail message id: `19ec465a43721708`
- Gmail timestamp: `2026-06-14T04:30:55`
- Classification: `new_vacancy`
- Routing decision: mixed: two enriched full-JD candidates promoted; remaining digest cards kept as trace only

## Summary

LinkedIn sent a similar-jobs digest for the previously reviewed `Overstory` / `Director of Platform Engineering` role, reference job id `4398306884`.

The digest listed these job cards:

- `Totalmobile Ltd` - `Platform Software Engineering Director`, United Kingdom remote, job id `4424231462`
- `hackajob` - `Platform Software Engineering Director`, United Kingdom remote, job id `4423987617`
- `Cleo` - `Engineering Director | UK (hybrid + remote) | Multiple roles`, United Kingdom remote, job id `4340952269`
- `Primer` - `Director of Engineering`, United Kingdom remote, job id `4421864484`
- `Pipekit` - `Head of Engineering`, United Kingdom remote, job id `4413252250`
- `La Fosse` - `Head of Engineering - Online Retailer - Hands off - Remote - GBP 140k`, United Kingdom remote, job id `4354498124`
- `Deel` - `Head of Engineering (FinTech)`, United Kingdom remote, job id `4399109246`
- `Stealth AI Company` - `Head of Engineering`, London onsite, job id `4406771873`
- `Unisys` - `Senior Director, Global Head of Solution Development & AI Platforms`, United Kingdom remote, job id `4418182935`
- `Harnham` - `Head of Engineering`, United Kingdom remote, job id `4417069156`

## Processing Note

The Gmail body itself was a thin card digest and did not include enough JD text for normal job-intake analysis.

LinkedIn MCP enrichment through the registered `mcp__linkedin` server succeeded for the strongest visible candidates:

- `4424231462` / Totalmobile returned a full Platform Software Engineering Director JD and was promoted into job intake.
- `4418182935` / Unisys returned a full Senior Director / AI Platforms JD and was promoted into job intake.

The remaining cards were not promoted during this unattended run because the run already found two full, higher-signal JDs and the other cards remained digest-level leads in the Gmail evidence. They can be fetched later by LinkedIn job id if the user wants a deeper UK/director batch review.

## Next Step

- Review the new active tasks for Totalmobile and Unisys.
- If UK remote roles remain strategically interesting, run a separate focused LinkedIn batch for the remaining job ids instead of expanding this cron run into a broad manual review.
