# 2026-06-25 Anthropic Knowledge Work Plugins / Personal Office Analysis

- Source request: analyze Habr article and related Anthropic workflow artifacts.
- Raw note: `inbox/raw/2026-06-25-habr-anthropic-knowledge-work-plugins.md`
- Related local context:
  - `wiki/personal-office-concept.md`
  - `tools/raspberrypi-openclaw/personal-office-context-pack.md`
  - `inbox/processed/2026-06-25-private-ai-office-vs-pi-personal-office-gap-analysis.md`
  - `tasks/active/2026-06-21-validate-premium-personal-ai-cloud-offer.md`
  - `tasks/active/2026-06-25-prototype-personal-office-role-workflow-pack.md`

## External Sources Reviewed

- Habr article: `https://habr.com/ru/articles/1042576/`
- Anthropic Knowledge Work Plugins repository: `https://github.com/anthropics/knowledge-work-plugins`
- Productivity plugin README: `https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/productivity/README.md`
- Enterprise Search plugin README: `https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/enterprise-search/README.md`
- Product Management plugin README: `https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/product-management/README.md`
- Small Business plugin README: `https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/small-business/README.md`
- Sales plugin README: `https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/sales/README.md`
- Finance plugin README: `https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/finance/README.md`
- Operations plugin README: `https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/operations/README.md`
- Claude for Small Business announcement: `https://www.anthropic.com/news/claude-for-small-business`
- Small Business plugin marketplace page: `https://claude.com/plugins/small-business`

## Core Takeaway

Anthropic's useful idea is not "install plugins".

The useful idea is packaging work as:

```text
router -> command/workflow -> skills -> connectors -> human approval checkpoints -> durable output
```

This is very close to what Personal Office is becoming:

```text
chaotic input -> extract -> enrich -> route -> artifact/task/handoff -> review loop
```

The strongest import for Personal Office is to separate:

- small router skills;
- explicit named workflows / commands;
- reusable atomic skills;
- connector boundaries;
- approval checkpoints;
- durable artifacts as the final output.

## What Maps Directly To Personal Office

### 1. Productivity Plugin

Anthropic's productivity plugin has task management, workplace memory and a dashboard.

Personal Office already has a stronger file-backed version:

- `tasks/active/`
- `tasks/waiting/`
- `memory/`
- `people/`
- `calendar/`
- `wiki/`
- daily plans and processed intake traces.

Useful import:

- define explicit commands around existing structures:
  - `/po:start-day`
  - `/po:inbox-triage`
  - `/po:update`
  - `/po:waiting-review`
  - `/po:stale-scan`
  - `/po:weekly-control`
- make each command produce or update canonical artifacts, not only chat.

Do not import:

- a separate `TASKS.md` board as source of truth;
- a broad always-on memory scan that loads too much private context by default.

### 2. Enterprise Search Plugin

This is highly relevant.

Anthropic's enterprise-search pattern decomposes a query across chat, email, docs, wiki, project trackers and CRM, then synthesizes an answer with source attribution and confidence.

Personal Office version should be:

```text
/po:find-decision
/po:find-context
/po:catch-up
/po:who-knows
```

Local adaptation:

- search across `inbox/processed/`, `tasks/`, `calendar/meetings/`, `people/`, `companies/`, `memory/`, and project handoff notes;
- return source paths and freshness;
- separate facts, hypotheses and stale assumptions;
- ask for narrow context handoff before reading sensitive areas.

This is probably the highest-value workflow for the owner-control contour.

### 3. Small Business Plugin

Anthropic's small-business plugin is useful because it exposes a packaging pattern:

- natural-language router;
- 15 commands;
- 15 skills;
- approval checkpoints;
- graceful degradation when connectors are missing;
- onboarding workflow that captures business context and tool availability.

Most relevant commands for Personal Office:

- `/monday-brief` -> `weekly-control` / `start-week`;
- `/friday-brief` -> `week-close`;
- `/handle-complaint` -> `relationship / conflict / customer issue intake`;
- `/review-contract` -> `document risk triage, not legal advice`;
- `/crm-cleanup` -> `people/company context cleanup`;
- `/call-list` -> `relationship follow-up priorities`.

Most relevant skills:

- `business-pulse`;
- `crm-maintenance`;
- `contract-review`;
- `customer-pulse`;
- `lead-triage`;
- `job-post-builder` only for hiring/project staffing scenarios.

Do not copy finance/tax workflows directly for Personal Office until ZenMoney / finance rules and review boundaries are much clearer.

### 4. Product Management Plugin

Very useful for Personal Office as owner/project-router, not as generic PM tooling.

Relevant commands:

- `/write-spec` -> turn source/understanding into change spec or project envelope;
- `/stakeholder-update` -> weekly Setronica / Fincom / AI Studio status updates;
- `/synthesize-research` -> product validation conversations, market signals, transcript synthesis;
- `/competitive-brief` -> Private AI Office market and positioning research;
- `/metrics-review` -> only after the metric source is known.

This overlaps strongly with:

- Setronica Task-to-Handoff discipline;
- project-bootstrapper;
- Private AI Office validation;
- company handoff envelopes.

### 5. Sales Plugin

Useful, but only as a narrow relationship/opportunity layer.

Relevant commands:

- `/call-summary` -> meeting transcript to follow-up, tasks and contact update;
- `/pipeline-review` -> career/opportunity/customer pipeline review;
- `/call-prep` -> meeting prep for validators, recruiters, prospects and partner calls;
- `draft-outreach` -> warm outreach drafts.

This should live under Personal Office relationship / personal-brand / company-work routing, not become a generic CRM replacement.

### 6. Operations Plugin

Useful for making Personal Office more sellable and operable.

Relevant commands:

- `/process-doc` -> turn recurring Personal Office behavior into playbook;
- `/runbook` -> operational runbooks for automation, Raspberry Pi, monitors, backup/restore;
- `/status-report` -> owner-level cross-company status;
- `/change-request` -> controlled changes to automations/tools;
- `/vendor-review` -> evaluate tools/providers such as RTCloud, OpenClaw, model providers.

This is directly useful for the "client-controlled but supportable" product frame.

### 7. Finance Plugin

Useful as structure, not as immediate automation.

Relevant concepts:

- reconciliation workflow;
- variance analysis;
- close checklist;
- review by qualified professional;
- source data + workpaper + approval packet.

Personal Office adaptation should be conservative:

- finance outputs are decision-support only;
- read-only by default;
- use ZenMoney / statements / user-provided facts as sources;
- produce "finance control packet" rather than financial advice.

## What Should Become Personal Office Workflows

Priority 1:

```text
/po:weekly-control
```

Purpose:

- owner-control brief across active tasks, waiting items, meetings, people, company signals and stale decisions.

Output:

- `calendar/daily/` or weekly note;
- updated `tasks/active/` / `tasks/waiting/`;
- flagged stale decisions and promises;
- context handoff requests.

Why:

- closest to the AI Chief of Staff promise;
- matches the "tool for the trusted assistant/operator" framing;
- easy to validate.

Priority 2:

```text
/po:find-context
```

Purpose:

- enterprise-search-like retrieval across Personal Office artifacts with source attribution.

Output:

- answer with source paths;
- confidence/freshness;
- missing context request;
- no write unless explicitly requested.

Why:

- solves real owner pain: reconstructing the working picture.

Priority 3:

```text
/po:meeting-to-state
```

Purpose:

- meeting/transcript/email thread -> lanes -> facts/hypotheses/risks/people/tasks/handoffs.

Output:

- meeting note or processed trace;
- contact updates;
- active/waiting tasks;
- company/project handoff envelope.

Why:

- matches actual Personal Office usage and the Pi mixed-context routing tests.

Priority 4:

```text
/po:project-envelope
```

Purpose:

- messy new activity -> owner envelope -> optional generated project space / handoff.

Output:

- owner-side project/activity note;
- route decision;
- task;
- optional call to `tools/project-bootstrapper/`.

Why:

- directly supports Personal Office as control center.

Priority 5:

```text
/po:operator-onboard
```

Purpose:

- equivalent of Anthropic's `smb-onboard`, but for a trusted assistant / operator.

Output:

- what sources the operator can access;
- what they must never access;
- review/approval rules;
- weekly cadence;
- route map;
- escalation rules.

Why:

- key for the "tool for Lyubochka" pricing/packaging question.

## What Should Become Atomic Skills

Keep skills short and router-like.

Recommended local skills or playbook-backed skills:

- `owner-context-search`
- `weekly-control`
- `meeting-to-state`
- `relationship-follow-up`
- `company-signal-routing`
- `project-envelope`
- `operator-onboarding`
- `finance-control-packet`
- `document-risk-triage`
- `runbook-maintenance`

Do not create a giant "Personal Office super-skill".

Anthropic's structure reinforces the current Personal Office direction:

> small skill files + detailed playbooks + explicit commands + narrow context handoffs.

## Connector Lessons

Connectors should be introduced by risk level:

1. Read-only local repository search.
2. Gmail / calendar read-only summaries.
3. Google Drive read-only for selected folders/docs.
4. ZenMoney read-only.
5. Write actions only as draft patch bundles or human-approved changes.
6. External sends/payments/signatures remain human-confirmed.

Anthropic's repeated pattern is important:

> agent drafts and prepares, human approves before money, customers, legal commitments, publications, or external sends.

That should be an explicit Personal Office product rule.

## Product Implication For Private AI Office

This article supports the current product thesis.

The market is moving from:

```text
general chatbot
```

to:

```text
role/workflow agent with connectors, commands, skills and approval rules
```

Private AI Office should not try to compete as another chatbot.

Its differentiated version is:

```text
client-controlled owner-context operating system
```

where:

- workflows are explicit;
- sources and rights are known;
- sensitive context stays under client control;
- provider does not need content access;
- human/operator approval is built in;
- durable artifacts are the output.

## Recommended Next Step

Prototype one local Personal Office role-workflow pack:

```text
personal-office-owner-operator-pack
```

Contents:

- `commands/weekly-control.md`
- `commands/find-context.md`
- `commands/meeting-to-state.md`
- `commands/project-envelope.md`
- `commands/operator-onboard.md`
- `skills/weekly-control/SKILL.md`
- `skills/owner-context-search/SKILL.md`
- `skills/meeting-to-state/SKILL.md`
- `skills/operator-onboarding/SKILL.md`
- `CONNECTORS.md`
- `APPROVALS.md`

Do this as a Personal Office-native pattern first, not as a Claude plugin install.

Then decide whether to:

- implement as local Codex skills;
- expose through OpenClaw as commands;
- package later as Private AI Office demo/workflow bundle.

