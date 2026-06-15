You are the Fincom project-entrypoint agent.

Working root: `/home/adre/projects/fincom`.

Implement the Project Entrypoint Contract described in:

- `processes/agent-workflows/project-entrypoint-contract.md`

Use this incoming handoff envelope from Personal Office as the first test case:

- `/home/adre/personal-office/companies/fincom/handoffs/2026-06-14-dcim-itam-tz-assessment.md`

Important boundary:

- Do not rely on Personal Office knowing Fincom's internal folder structure.
- Do not ask Personal Office to choose internal Fincom paths, lifecycle branches, process agents, or artifact names.
- Fincom must accept a normalized handoff envelope and decide the internal route itself.

Task:

1. Read the required files listed in `processes/agent-workflows/project-entrypoint-contract.md`.
2. Implement the smallest complete Fincom project entrypoint protocol as repository artifacts.
3. Include a handoff envelope template, workflow, status model, intake log, and usage snippet for future `codex exec` runs.
4. Use the DCIM/ITAM handoff as the motivating example or first intake.
5. Keep all external-facing commercial, technical, price, schedule, SLA, security, registry, or feasibility claims blocked behind Evidence/Feasibility and Human Approval gates.

Expected behavior:

- If enough context exists, accept the envelope and create a durable trace.
- If key project-side facts are missing, mark the handoff as `needs_clarification` and record the exact questions.
- Report back what files were created or updated and what handoff status was assigned.
