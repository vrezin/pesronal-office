# Job Search Business Contour Target

- Date: 2026-07-01
- Runtime target: Raspberry Pi OpenClaw
- Agent: `job-search`
- Status: target architecture / process contract
- Storage decision: `tools/raspberrypi-openclaw/personal-office-shared-storage-decision-2026-07-01.md`

## Target Outcome

Build a standalone job-search business contour, not a workstation-dependent demo.

The job-search contour is domain-specific. It should depend on the shared Personal Office base layer rather than owning its own private copy of general `wiki/`, `memory/`, and `tools/` rules.

Shared base layer on Pi:

```text
/home/openclaw/personal-office-agent/cookbooks/personal-office/
```

Domain/runtime layer on Pi:

```text
/home/openclaw/personal-office-agent/job-search-contour/
```

The contour must continuously process job-search signals from HH, LinkedIn, Gmail, Google Calendar, and Telegram, then produce actionable Telegram bot outputs:

- interesting vacancies found;
- fit/no-fit verdict;
- recommended CV;
- recommended cover letter;
- next action: send / clarify / skip / wait.

The workstation Codex environment can remain a development/operator surface, but the production-like runtime should not depend on the laptop being powered on.

Personal Office itself should be Pi-primary: the full canonical working tree and always-on automations live on the Raspberry Pi. The workstation can initiate requests, review changes, and sync, but it should not own part of the operating state.

## Scenario 1 - Scheduled Mail Intake

Background schedule runs on the Pi.

1. A scheduled job starts the `job-search` agent.
2. The agent reads Pi-local state and last processed Gmail ids.
3. The agent searches Gmail through Pi-local `google_workspace` MCP:
   - HH / HeadHunter messages;
   - LinkedIn job/recruiter/status messages.
4. The agent classifies each message:
   - `status_update`;
   - `invitation`;
   - `new_vacancy`;
   - `noise`.
5. For promising or actionable vacancies, the agent enriches:
   - HH through `headhunter_web`;
   - LinkedIn through `linkedin`;
   - Calendar context through `google_workspace` if scheduling/follow-up is involved.
6. The agent writes durable state/run logs and updates job-intake artifacts.
7. The Telegram bot sends a concise decision packet:
   - found vacancies;
   - why interesting or not;
   - selected CV;
   - cover letter draft;
   - recommended action.

## Scenario 2 - Telegram Ad-Hoc Vacancy Intake

User forwards a vacancy, recruiter message, HH link, LinkedIn link, or pasted JD to the bot.

1. Telegram receives the message and routes it to `job-search`.
2. The agent normalizes the input:
   - source: HH / LinkedIn / pasted JD / recruiter / unknown;
   - vacancy URL or job id;
   - company;
   - role;
   - evidence quality.
3. The agent enriches the vacancy through the relevant MCP where possible.
4. The agent evaluates:
   - fit;
   - effort class;
   - compensation and lifestyle constraints;
   - relocation/family logistics if relevant;
   - risk/noise/duplicate status.
5. If the role is not worth action, the bot replies with a short skip/no-go explanation.
6. If the role is worth action, the bot replies with:
   - verdict;
   - selected CV;
   - cover letter draft;
   - exact next action.

## State Boundary

The Pi contour must not rely on hidden workstation memory.

Accepted storage model:

- Git + Markdown is the canonical artifact layer;
- SQLite is the operational runtime state layer;
- private Git remote is the shared sync layer.
- Shared `wiki`, Memory OS protocol, Memory OS validator, and owner/operator pack live in the Personal Office cookbook layer for all agents.

Required Pi-accessible state:

- Gmail monitor state:
  - last processed HH Gmail id/date;
  - last processed LinkedIn Gmail id/date;
  - overlap window policy;
  - duplicate ids seen in recent runs.
- Job-intake index or a synchronized subset:
  - known companies;
  - known roles;
  - previous decisions;
  - current waiting/active statuses.
- Run logs:
  - scheduled run logs;
  - ad-hoc Telegram intake logs;
  - blocked/error logs.
- CV registry:
  - available final CVs;
  - selection rules;
  - links/paths to CV files the bot can offer.
- Cover-letter templates and generated drafts.

The source of truth is the Personal Office repository, with the primary working tree on the Pi. A smoke test that supplies known duplicate ids in the prompt is not enough for unattended operation.

## Artifact Contract

Durable writes belong in the Personal Office source-of-truth structure:

- run logs: `automation/runs/`;
- monitor state: `automation/state/`;
- active actions: `tasks/active/`;
- waiting items: `tasks/waiting/`;
- raw/processed intake traces: `inbox/raw/` and `inbox/processed/`;
- career artifacts: `personal-projects/personal-brand/workspace/job-intake/`;
- targeted CV/CL outputs: `personal-projects/personal-brand/workspace/job-intake/targeted-resumes/` or a dedicated generated-output subfolder.

The Pi runtime should write to the Pi-primary Personal Office working tree. Git remote sync is for backup/history and workstation review, not for splitting the source of truth.

## Telegram Output Contract

For each actionable vacancy, the bot reply should be concise and decision-first:

```text
Found: <company> - <role>
Verdict: send / maybe / skip
Why: <1-3 bullets>
CV: <selected CV name/path>
Cover letter: <draft or link>
Next action: <send now / ask question / wait / ignore>
```

For non-actionable input:

```text
Verdict: skip/no-op
Reason: <short reason>
Stored: <trace path if created>
```

## Current Proven Pieces

- Pi OpenClaw agent `job-search` exists.
- HH MCP is healthy through Pi.
- LinkedIn MCP is healthy through Pi and authenticated.
- Google Workspace MCP `google_workspace` is healthy through Pi and authenticated read-only for Gmail/Calendar.
- Pi-local Gmail E2E smoke passed over archived HH/LinkedIn mail.
- Job-search runtime SQLite schema/tooling exists under `tools/job-search-runtime/`.
- Pi sync wrapper skeleton exists at `automation/scripts/run-pi-job-search-sync.sh`.
- Pi runtime DB initialized at `automation/state/job-search-runtime.sqlite` inside `job-search-contour`.
- Baseline duplicate ids seeded from Markdown monitor state: 5 HH ids and 2 LinkedIn ids.
- Pi-primary Gmail monitor exists, is scheduled by systemd user timer, and has a successful Pi-local smoke run.
- Telegram intake wrapper, prompt, SQLite update dedupe commands, setup script, and disabled systemd templates exist. Live Telegram E2E remains pending because no OpenClaw chat channel is configured yet.

## Remaining Build Work

1. Done: Create or promote a full Personal Office working tree on Pi as the primary repo.
2. Done: Configure private Git remote backup/sync for Pi.
3. Done: Decide Pi Git identity and deploy key.
4. Done for first slice: Adapt HH/LinkedIn Gmail monitor prompts to use Pi-local `google_workspace`.
5. Done for Gmail: Create Pi-side scheduled wrappers/systemd timers.
6. In progress: Add Telegram inbound routing to `job-search`; wrapper/prompt/setup path exists, live channel configuration is pending.
7. In progress: Add Telegram outbound decision packets; output contract exists, live send is pending channel configuration.
8. Done for Gmail and scaffolded for Telegram: Extend duplicate-state handling from seeded baseline to normal scheduled writes.
9. Run a fresh Inbox E2E test when the next HH/LinkedIn message arrives.
10. Run an ad-hoc Telegram vacancy intake test.
