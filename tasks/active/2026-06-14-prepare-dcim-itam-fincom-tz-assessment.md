# Prepare DCIM/ITAM Fincom ТЗ Assessment

- Created: 2026-06-14
- Status: active
- Priority: high
- Due: 2026-06-15
- Area: companies / fincom / presale
- Related inbox note: `inbox/processed/2026-06-14-dcim-itam-fincom-tz-assessment.md`
- Raw source:
  - `inbox/raw/2026-03-23_Проект ТЗ на поставку и внедрение Системы DCIM с модулем ITAM. v.docx`
  - `inbox/raw/2026-06-14-dcim-itam-correspondence.md`
- Company context: `companies/fincom/context.md`
- Handoff envelope: `companies/fincom/handoffs/2026-06-14-dcim-itam-tz-assessment.md`
- Formal counterparty card: `companies/fincom/contacts/2026-06-14-it2bsns.md`
- Working destination: Fincom project entrypoint in `<fincom-root>`
- Fincom entrypoint assignment: `<fincom-root>/processes/agent-workflows/project-entrypoint-contract.md`

## Current State

The intake is classified as a Fincom request to assess a customer ТЗ for DCIM/ITAM. Personal Office has captured the management trace and sent a normalized handoff envelope. The Fincom-side project-entrypoint agent has accepted the handoff into the Fincom workspace.

Clarification update from user:

- Formal counterparty/customer for the contract path: АйТуБи / `https://it2bsns.ru/`.
- Real end customer: Ростелеком.
- Fincom-side owner: Виктор Геронимус.
- Deadline: 2026-06-15.
- Required by deadline: say whether Fincom can take the project; if yes, provide indicative price and schedule.
- Evidence for registry/SCADA/integration/visualization/estimate claims remains blocked until current Fincom capability data is provided and project-side gates run.

Project response:

- Project-local entrypoint: `<fincom-root>/processes/entrypoint/README.md`
- Project-local intake log: `<fincom-root>/processes/entrypoint/intake-log.md`
- Project status: `routed`
- Assigned process: `<fincom-root>/processes/presale/` first-pass realization assessment
- Active project-local trace: `<fincom-root>/clients/pao-rostelekom/analytics/2026-06-14-dcim-itam-entrypoint-trace.md`
- Presale management summary: `<fincom-root>/clients/pao-rostelekom/analytics/2026-06-14-dcim-itam-tz-summary.md`
- Summary status: `conditional-go`
- Superseded placeholder trace: `<fincom-root>/clients/unknown-dcim-itam-2026-06/analytics/2026-06-14-entrypoint-trace.md`

## Next Step

Continue through the Fincom presale workflow:

- run the internal presale first-pass realization assessment for go/no-go;
- provide/upload current Fincom capability data for DCIM, ITAM, SCADA, registry status, integrations, and visualization claims;
- use the rebuilt Fincom product frame to split ТЗ requirements into: covered by current Fincom contour, partially covered / major customization, not covered / needs market or open-source search;
- treat `Финкомтех.ERP` as the only currently registry-backed product assumption; other systems are assumed to require registration during the project until evidence says otherwise;
- for ITAM / asset management, start from `Финкомтех.ERP` / Odoo-based modules and extensions in the unified ERP database; do not route to generic open-source asset-management systems unless an ERP/Odoo gap is proven;
- get Human Approval for the safe 2026-06-15 external answer;
- confirm whether Артем is technical owner or consulted specialist;
- confirm phase-1 scope and what is roadmap;
- keep evidence-gated claims blocked until user provides Fincom capability data and Human Approval Gate is reached.

## Open Questions

- What internal opportunity name should the Fincom-side workflow use: АйТуБи / Ростелеком DCIM-ITAM, or another name?
- Is Артем technical owner/reviewer or consulted specialist?
- What output should be prepared for 2026-06-15: go/no-go memo, internal risk brief, customer questions, indicative price/schedule range, КП skeleton, technical feasibility note, or another artifact?
