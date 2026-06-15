# DCIM/ITAM Correspondence Analysis

- Date: 2026-06-14
- Scope: analysis of user-provided correspondence around the DCIM/ITAM ТЗ
- Related handoff: `companies/fincom/handoffs/2026-06-14-dcim-itam-tz-assessment.md`
- External use: blocked

## Executive Read

The correspondence is useful as a presale signal, but it is not a decision-ready architecture or estimate.

It mixes four layers:

1. Real ТЗ pressure points: DCIM, ITAM, 3D visualization, cable/network topology, integrations, registry/compliance, operation without tribal knowledge.
2. Internal Fincom intuition: "assets management + SCADA + many integrations/customizations"; Артем is the likely SCADA feasibility touchpoint.
3. AI-generated technology options: NetBox, Odoo, Snipe-IT, Ralph, Zabbix, Three.js, Node-RED, Keycloak, Kubernetes, etc.
4. AI-generated estimate: team, hours, 12-15M RUB, 5-6 months.

Only layers 1 and 2 can currently steer routing and question design. Layers 3 and 4 require evidence checks before they can steer architecture, commercial position, or external commitments.

## Strong Signals

- The core pain is not just asset inventory. It is reduction of operational dependence on narrow experts who hold undocumented knowledge about network configuration, cable tracing, and equipment placement.
- Visualization of communication networks is a critical differentiator, not a cosmetic feature.
- The project likely sits at the intersection of DCIM, ITAM/CMDB, SCADA/MES/monitoring, integrations, and presale compliance.
- Registry status and open-source/third-party dependencies can become bid blockers.
- Integration risk is probably larger than base product fit risk.

## Weak Or Unverified Signals

- NetBox/Odoo/Snipe-IT/Ralph/Zabbix/Three.js architecture is a hypothesis, not a selected solution.
- "NetBox Visual Explorer closes most requirements" is not usable externally without product/license/availability verification.
- The estimate of 2460 hours and 12-15M RUB is a draft heuristic, not evidence-backed.
- The role split and timeline assume a custom 3D viewer plus substantial integrations, but the actual first-phase scope is not confirmed.
- Claims about Enterprise vs Community capabilities are not verified against current vendor docs.

## Main Decision Forks

| Fork | Why it matters | Required evidence |
|---|---|---|
| Fincom product-led vs open-source assembly | Determines whether this is a Fincom solution, integration project, or hybrid wrapper. | Product capability base from Fincom presentations and internal product owners. |
| Full DCIM/ITAM vs MVP/pilot | Determines whether price/schedule can be bounded. | Customer acceptance priorities and phase-1 scope. |
| 3D traceability required for acceptance vs roadmap | Determines frontend/3D cost and risk. | ТЗ clause mapping and customer confirmation. |
| Registry requirement applies to whole solution vs components | Determines feasibility and legal/commercial posture. | Procurement/legal clarification and Fincom registry evidence. |
| SCADA/MES integration vs SCADA product delivery | Determines Артем's role and feasibility burden. | Артем review and product boundary. |
| Customer provides source data vs contractor reconstructs model | Determines migration/discovery effort. | Availability and quality of rack, device, cable, power, floorplan, IPAM/VLAN data. |

## What The Product Base Must Answer

When the Fincom product presentations are processed, the presale workflow should map product facts against these questions:

- Which Fincom products are official source-of-truth candidates for ERP, assets, warehouse, monitoring, analytics, SCADA/MES, and ecosystem integration?
- Which products are registered or can be positioned for Russian software registry requirements?
- Which products already support asset hierarchy, equipment cards, locations, inventory numbers, movement lifecycle, maintenance, monitoring, or telemetry?
- What integration mechanisms are actually supported: REST API, message bus, import/export, connectors to 1C, ESMP, BPMN, monitoring, SCADA/MES?
- What visualization capabilities are native today, and what would require custom development?
- What scale claims are evidence-backed, especially against 600k devices / 35k rack places if that ТЗ requirement is confirmed?
- What implementation examples or references can support credibility for Ростелеком/АйТуБи?

## Presale Use

Safe internal use:

- Use the correspondence to build a risk register and customer question list.
- Use it to prioritize conversations with Виктор and Артем.
- Use the rough estimate only as a sanity-check range for internal discussion.

Unsafe external use:

- Do not quote the open-source stack as the proposed architecture.
- Do not quote the 12-15M RUB / 5-6 months estimate.
- Do not promise registry compliance, SCADA coverage, 3D traceability, integrations, SLA, or performance.

## Recommended Next Internal Step

After the Fincom product-truth wiki is created from presentations, run a first-pass realization assessment that produces:

- go/no-go / conditional-go;
- product-fit matrix against ТЗ blocks;
- evidence gaps;
- customer questions;
- Артем question list for SCADA/MES and industrial integration;
- a guarded indicative range only if enough capability evidence exists.
