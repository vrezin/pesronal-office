---
source_system: personal-office
received_at: 2026-06-14
handoff_status: project_routed_presale_first_pass
customer_or_counterparty: АйТуБи / it2bsns.ru as formal counterparty; Ростелеком as real end customer
deadline_or_urgency: 2026-06-15 initial go/no-go plus indicative price and schedule
external_claim_status: draft_only_not_external
---

# Handoff Envelope - DCIM/ITAM ТЗ Assessment

## Source Pointers

- `inbox/raw/2026-03-23_Проект ТЗ на поставку и внедрение Системы DCIM с модулем ITAM. v.docx`
- `inbox/raw/2026-06-14-dcim-itam-correspondence.md`
- `inbox/processed/2026-06-14-dcim-itam-fincom-tz-assessment.md`
- `tasks/active/2026-06-14-prepare-dcim-itam-fincom-tz-assessment.md`
- `companies/fincom/contacts/2026-06-14-it2bsns.md`

## Why Fincom

This is a Fincom request to assess a customer ТЗ. The input asks for a safe path to evaluate DCIM/ITAM feasibility, architecture, risks, estimate shape, and possible response strategy.

## Requested Outcome

Accept this handoff through the Fincom project entrypoint and create the appropriate project-local trace for a first-pass assessment.

The Fincom-side workflow should decide the internal destination, process, skills, gates, and artifacts.

## People

- Vladimir: source/router owner in Personal Office context.
- Артем: internal Fincom SCADA/СКАДА specialist and stakeholder for technical feasibility.
- Виктор Геронимус: Fincom-side owner.
- АйТуБи / `it2bsns.ru`: formal customer/counterparty for Fincom contract path.
- Ростелеком: real end customer for the opportunity.

## Visible Risks

- Russian software registry requirement for the system.
- SCADA/СКАДА registration or product status is not confirmed.
- Open-source and third-party library acceptability is unclear.
- Complex integrations are expected.
- 3D/network/cable/power visualization may be a critical delivery risk.
- Any estimate, schedule, SLA, compliance, security, registry, or feasibility statement requires evidence checks before external use.

## Open Questions

- What internal opportunity name should Fincom use for the АйТуБи / Ростелеком DCIM/ITAM assessment?
- Should Артем be the technical owner/reviewer for SCADA feasibility, or only a consulted specialist?
- What first output should be prepared by 2026-06-15: go/no-go memo, internal risk brief, customer questions, indicative price/schedule range, КП skeleton, technical feasibility note, or another artifact?
- Which process/gates should Fincom run for DCIM/ITAM ТЗ assessment?
- What can be stated externally only after Evidence/Feasibility and Human Approval gates?

## Notes For Project Entrypoint Agent

- Do not assume NetBox, Odoo, SCADA, open-source components, cost, timeline, or architecture are approved.
- Do not create an external-facing commercial or technical promise from the chat draft.
- Treat the existing chat estimate as internal draft material only.
- Report handoff status back in a durable artifact that Personal Office can reference.

## Project Response

- Fincom entrypoint assignment was executed on 2026-06-14 via `codex exec`.
- Project-local entrypoint: `<fincom-root>/processes/entrypoint/README.md`
- Project-local intake log: `<fincom-root>/processes/entrypoint/intake-log.md`
- Local normalized envelope: `<fincom-root>/processes/entrypoint/incoming/2026-06-14-dcim-itam-tz-assessment.md`
- Project-local trace: `<fincom-root>/clients/unknown-dcim-itam-2026-06/analytics/2026-06-14-entrypoint-trace.md`
- Initial assigned project status: `needs_clarification`
- Initial reason: customer/opportunity name, Fincom-side owner, deadline, and evidence for registry/SCADA/integration/visualization/estimate claims were missing. External-facing claims were blocked behind Evidence/Feasibility and Human Approval gates.

## Clarification Update - 2026-06-14

- Formal customer/counterparty: АйТуБи / `https://it2bsns.ru/`.
- Real end customer: Ростелеком.
- Fincom-side owner: Виктор Геронимус.
- Deadline: 2026-06-15.
- Needed by deadline: say whether Fincom can take the project; if yes, provide indicative price and schedule.
- Evidence for registry, SCADA, integration, visualization, and estimate claims remains blocked until the user provides data about current Fincom capabilities and the project-side evidence/human approval gates run.

## Project Response Update - 2026-06-14

- Clarification update was passed to the Fincom project entrypoint via `codex exec`.
- Assigned project status: `routed`.
- Assigned lifecycle: `clients/pao-rostelekom/` as pre-contract client work, with АйТуБи tracked as formal counterparty for the contract path.
- Assigned process: `processes/presale/` first-pass realization assessment.
- Active project-local trace: `<fincom-root>/clients/pao-rostelekom/analytics/2026-06-14-dcim-itam-entrypoint-trace.md`.
- Superseded placeholder trace: `<fincom-root>/clients/unknown-dcim-itam-2026-06/analytics/2026-06-14-entrypoint-trace.md`.
- Next project action: run internal presale first-pass realization assessment for go/no-go. If positive, prepare only an internally reviewed indicative price/schedule range after capability data and gates.
- External use remains blocked: no answer, price, schedule, SLA, registry, SCADA, compliance, integration, or feasibility promise may be produced before Evidence/Feasibility and Human Approval gates close.

## Product Frame Update - 2026-06-14

- Fincom product-frame artifacts have been rebuilt in `<fincom-root>` from product presentations.
- The next Fincom-side step should compare the customer ТЗ against the rebuilt product frame:
  - identify what is explicitly covered by the existing Fincom contour;
  - identify what is partially covered but requires major customization;
  - identify what is not covered and requires market/open-source option search;
  - keep all external-facing claims behind Evidence/Feasibility and Human Approval gates.
- Registry constraint: current working assumption is that only `Финкомтех.ERP` has Минцифры registry status now. Other Fincom systems should be treated as not yet registered and potentially registered during the project, subject to evidence and feasibility checks.

## ITAM / Asset Management Correction - 2026-06-14

- For ITAM / asset management, the Fincom-side default should start from the existing `Финкомтех.ERP` / Odoo-based contour and available Odoo modules/extensions, because they preserve a unified database and business-process model.
- Generic open-source asset-management systems such as Snipe-IT, GLPI, Ralph, or similar tools should not be searched or selected as the primary route before checking Odoo/ERP fit.
- External asset-management tools may still be considered only if the Odoo/ERP contour has a confirmed functional gap that cannot be covered safely by module extension or customization.
- This correction does not remove the need for evidence checks around registry status, licenses, customization scope, integrations, and data model fit.

## Project Summary Response - 2026-06-14

- Fincom project agent created presale management summary: `<fincom-root>/clients/pao-rostelekom/analytics/2026-06-14-dcim-itam-tz-summary.md`.
- Client README was updated to reference the summary: `<fincom-root>/clients/pao-rostelekom/README.md`.
- Summary status: `conditional-go`.
- Core conclusion: Fincom has a relevant ERP/Odoo-first ITAM base through `Финкомтех.ERP`, but the DCIM-heavy scope is not proven as existing product coverage and requires feasibility/evidence work.
- External position remains blocked until Evidence/Feasibility and Human Approval gates close.
