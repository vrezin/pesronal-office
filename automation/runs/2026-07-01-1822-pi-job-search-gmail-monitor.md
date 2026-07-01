# Pi Job Search Gmail Monitor Run

- Timestamp: 2026-07-01 18:22:15 +0700
- Trigger: scheduled task, Pi Job Search Gmail Monitor
- Repo root: `/home/openclaw/personal-office-agent/personal-office`
- Gmail account: configured Pi-local Google Workspace account
- Gmail mutation: none; read-only scan
- Git mutation: none

## Runtime

- Ran `python3 tools/job-search-runtime/job_search_runtime.py init`.
- Ran `python3 tools/job-search-runtime/job_search_runtime.py seed-monitor-state`.
- Checked every seen Gmail id with `message-status` before reading/routing.
- SQLite was the operational dedupe source. The local `sqlite3` shell is not installed, so inspection stayed through the runtime CLI.

## Gmail Queries

- HH primary: `from:(hh.ru OR notification@hh.ru OR no-reply@hh.ru OR noreply@hh.ru) newer_than:7d`
- HH fallback: `(hh.ru OR HeadHunter) newer_than:7d`
- LinkedIn: `from:linkedin.com newer_than:7d`

## Message IDs Seen

### HH

- `19f191abaf5759ab` / thread `19f191abaf5759ab`
- `19f12cd62b56bebe` / thread `19f12cd62b56bebe`
- `19f0d7d179bacbb7` / thread `19f0d7d179bacbb7`

The HH fallback query returned the same three ids.

### LinkedIn

- `19f1ccd893dd5007` / thread `19f1ccd893dd5007`
- `19f1c5f9c902533e` / thread `19f1c5f9c902533e`
- `19f19cc71bda9b7d` / thread `19f19cc71bda9b7d`
- `19f17a756395463d` / thread `19f17a756395463d`
- `19f1739460e5ee68` / thread `19f1739460e5ee68`

## Duplicate / No-op IDs

- None. The new SQLite runtime reported all eight seen ids as `processed: false`.

## Processed Items

All eight messages were thin automated job digests/alerts with no application status change, recruiter invitation, employer reply, or full JD text. They were collapsed as `noise` and marked in SQLite with no message-specific job-intake artifact.

### HH Noise

- `19f191abaf5759ab`: HH similar-vacancies digest for `AI Solution Architect / Head of AI Implementation`; titles included MTS IT Senior Technical Product Owner, Bgstaff Архитектор, DigiKey CTO / Technical Director, AI Automation Developer, Andersen Lead AI & Data Scientist.
- `19f12cd62b56bebe`: HH similar-vacancies digest for the same resume; titles included Algonova Senior AI Engineer, Циан Engineering Manager (Data Platform), Syberry AI Software Engineer, Andersen Lead AI & Data Scientist.
- `19f0d7d179bacbb7`: HH similar-vacancies digest for the same resume; titles included Spice IT Solution Architect, StoneTreeGroup Head of IT Direction, Simplenight Senior Technical Product Manager, Точка Lead Research Engineer, Softline technical leader.

### LinkedIn Noise

- `19f1ccd893dd5007`: LinkedIn alert, single thin card for Confidential `Group Chief Engineer`, Limassol, job id `4431595886`.
- `19f1c5f9c902533e`: LinkedIn alert for Cyprus technical director roles: Arnold Ash Group `Group Technology Director` job id `4434490240`, Work Channel `Head of Enterprise Architecture` job id `4431586790`, Confidential `Group Chief Engineer` job id `4431595886`.
- `19f19cc71bda9b7d`: LinkedIn recommended-jobs digest including Jobgether `Director of Engineering`, Arnold Ash Group `Group Technology Director`, Explore Group `Chief Technology Officer`, Evantis `Director of Engineering`, TIENS `Regional AI Project Manager`, Netex `Senior AI Implementation Strategist`.
- `19f17a756395463d`: LinkedIn alert for Cyprus/Limassol engineering roles: Kraken `Data Platform Engineering Manager` job id `4405362009`, Pepperstone `Engineering Manager - Trading Platforms` job id `4414605769`.
- `19f1739460e5ee68`: LinkedIn EMEA software engineering director alert including JPMorganChase `Applied AI ML Director`, hackajob `Head of Integration, Data & GenAI Engineering`, Yotpo `Head of Engineering`, Yael Group `Head of AI Center of Excellence`, Scale AI `Director, Forward Deployed Engineering`, Gotfriends `Director of Engineering`.

## Blocked Items

- None. Gmail search/read via Pi-local `google_workspace` succeeded after retrying the post-restart message reads.

## Artifacts

- Run log: `automation/runs/2026-07-01-1822-pi-job-search-gmail-monitor.md`
- Message-specific artifacts: none; all routed items were noise.

## Legacy State

- Updated `automation/state/hh-gmail-monitor-state.md` after successful scan.
- Updated `automation/state/linkedin-gmail-monitor-state.md` after successful scan.
