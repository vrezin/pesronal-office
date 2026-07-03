# Closed And Parked Vacancy Compaction Rollup

- Created: 2026-07-01
- Scope: `job-intake` closed/parked JD and analysis files
- Action: compacted full dead-role artifacts into this rollup and preserved operating truth in `INDEX.md` and `COMPANY_NOTES.md`
- Rule: keep full files for active, waiting, interview, applied, A-class, or still-useful B-class roles; compact rejected, closed, expired, C-class, location-gated, duplicate, or no-action roles after the decision is represented elsewhere.

## Why This Exists

The old process treated every archived JD and analysis as permanent source evidence. That made `job-intake/` grow into a file dump even after vacancies were rejected, expired, parked, or no longer actionable. The useful layer is the decision memory: what was reviewed, why it was closed or parked, which CV track was chosen, and whether the company or market signal matters later.

For the compacted files below, detailed text is intentionally not preserved here. If a future role needs old wording, recover the deleted file from git history. Normal workflow should use:

- `INDEX.md` for the vacancy decision history.
- `COMPANY_NOTES.md` for company and market memory.
- `tasks/active/` and `tasks/waiting/` for live action.
- This rollup as the cleanup receipt for removed full artifacts.

## Compacted Analysis Files

### Closed

- `analyses/closed/2026-06-01-global-fintech-tech-lead-product-antifraud-analysis.md`
- `analyses/closed/2026-06-01-limassol-international-platform-cto-rejection-analysis.md`
- `analyses/closed/2026-06-01-sber-product-owner-ml-ai-nlp-llm-agents-analysis.md`
- `analyses/closed/2026-06-01-unknown-company-cto-head-of-engineering-stability-analysis.md`
- `analyses/closed/2026-06-01-unknown-fmcg-cto-product-tech-block-rejection-analysis.md`
- `analyses/closed/2026-06-02-innovative-people-cft-developer-analysis.md`
- `analyses/closed/2026-06-08-alfigroup-cio-analysis.md`
- `analyses/closed/2026-06-08-sber-business-process-transformation-ai-disrupt-pdlc-analysis.md`
- `analyses/closed/2026-06-09-infiniti-tech-lead-ai-engineer-analysis.md`
- `analyses/closed/2026-06-09-moex-delivery-lead-api-first-analysis.md`
- `analyses/closed/2026-06-09-pepperstone-head-of-product-engineering-analysis.md`
- `analyses/closed/2026-06-09-unknown-ai-native-product-technologist-analysis.md`
- `analyses/closed/2026-06-09-unknown-wholesale-it-head-1c-migration-analysis.md`
- `analyses/closed/2026-06-10-shaw-daniels-solutions-head-of-engineering-analysis.md`
- `analyses/closed/2026-06-12-faw-east-europe-it-head-analysis.md`
- `analyses/closed/2026-06-12-kdr-talent-solutions-head-of-engineering-ai-platform-analysis.md`
- `analyses/closed/2026-06-12-r7-project-manager-analysis.md`
- `analyses/closed/2026-06-12-riverhouse-pmo-lead-asana-analysis.md`
- `analyses/closed/2026-06-14-cdek-customer-journey-crm-head-analysis.md`
- `analyses/closed/2026-06-14-ey-engineering-lead-director-dublin-analysis.md`
- `analyses/closed/2026-06-14-oyster-senior-director-data-platform-ai-analysis.md`
- `analyses/closed/2026-06-14-totalmobile-platform-software-engineering-director-analysis.md`
- `analyses/closed/2026-06-14-unisys-senior-director-ai-platforms-analysis.md`
- `analyses/closed/2026-06-15-epam-technical-delivery-management-director-analysis.md`
- `analyses/closed/2026-06-15-ksky-software-development-head-analysis.md`
- `analyses/closed/2026-06-15-marsh-senior-it-director-global-value-streams-analysis.md`
- `analyses/closed/2026-06-15-positive-technologies-head-of-engineering-cybertesting-access-platform-analysis.md`
- `analyses/closed/2026-06-17-2gis-project-manager-ai-transformation-analysis.md`
- `analyses/closed/2026-06-18-anyfin-non-traditional-cto-analysis.md`
- `analyses/closed/2026-06-18-the-agile-monkeys-general-manager-ai-software-services-analysis.md`
- `analyses/closed/2026-06-19-gruppa-meta-project-office-head-analysis.md`
- `analyses/closed/2026-06-19-lovol-global-senior-director-engineering-analysis.md`
- `analyses/closed/2026-06-19-riverhouse-team-lead-it-ai-analysis.md`
- `analyses/closed/2026-06-20-alfa-bank-belarus-solution-architect-analysis.md`
- `analyses/closed/2026-06-23-gendir-ai-lead-ai-engineer-analysis.md`
- `analyses/closed/2026-06-23-vinted-senior-director-engineering-platform-analysis.md`
- `analyses/closed/2026-06-25-surge-group-cto-head-trading-engineering-analysis.md`

### Parked

- `analyses/parked/2026-06-01-atb-head-of-middle-office-development-center-analysis.md`
- `analyses/parked/2026-06-03-selecta-ai-solutions-specialist-analysis.md`
- `analyses/parked/2026-06-10-redholt-vice-president-technology-dubai-analysis.md`
- `analyses/parked/2026-06-12-azimut-ai-project-lead-analysis.md`
- `analyses/parked/2026-06-12-greenmoney-cto-technical-leader-mfo-startup-analysis.md`
- `analyses/parked/2026-06-12-magnit-product-team-lead-analysis.md`
- `analyses/parked/2026-06-12-sber-ai-project-manager-analysis.md`
- `analyses/parked/2026-06-19-lego-director-engineering-customer-data-foundation-analysis.md`
- `analyses/parked/2026-06-19-medallion-director-engineering-ai-platform-analysis.md`
- `analyses/parked/2026-06-19-vialytics-vp-of-engineering-analysis.md`
- `analyses/parked/2026-06-19-wex-sr-director-engineering-agentic-ai-service-applications-analysis.md`
- `analyses/parked/2026-06-20-trt-systems-architect-gcp-analysis.md`
- `analyses/parked/2026-06-22-ford-credit-director-engineering-digital-products-analysis.md`
- `analyses/parked/2026-06-22-signify-technology-head-engineering-analysis.md`
- `analyses/parked/2026-06-23-dataleap-founding-deployment-strategist-analysis.md`
- `analyses/parked/2026-06-23-dataleap-role-cluster-analysis.md`
- `analyses/parked/2026-06-23-linkedin-director-software-engineering-dublin-selection-analysis.md`
- `analyses/parked/2026-06-23-lodgify-director-ai-enablement-analysis.md`
- `analyses/parked/2026-06-23-parsewise-forward-deployed-engineer-analysis.md`
- `analyses/parked/2026-06-23-severstal-it-project-manager-analysis.md`
- `analyses/parked/2026-06-23-viaquant-partners-director-data-engineering-analysis.md`
- `analyses/parked/2026-06-24-getmatch-hidden-ai-engineer-analysis.md`
- `analyses/parked/2026-06-24-mufg-azure-cloud-engineering-team-lead-analysis.md`
- `analyses/parked/2026-06-25-fewfar-head-engineering-ai-native-platform-analysis.md`
- `analyses/parked/2026-06-25-zebra-people-vp-artificial-intelligence-analysis.md`
- `analyses/parked/2026-06-26-harrington-starr-director-technology-fintech-saas-analysis.md`
- `analyses/parked/2026-06-26-unknown-ai-automation-engineer-content-author-evaluation-analysis.md`

## Compacted JD Archive Files

### Closed

- `jd-archive/closed/2026-06-01-global-fintech-tech-lead-product-antifraud.md`
- `jd-archive/closed/2026-06-01-sber-product-owner-ml-ai-nlp-llm-agents.md`
- `jd-archive/closed/2026-06-01-unknown-company-cto-head-of-engineering-stability.md`
- `jd-archive/closed/2026-06-02-innovative-people-cft-developer.md`
- `jd-archive/closed/2026-06-08-alfigroup-cio.md`
- `jd-archive/closed/2026-06-08-sber-business-process-transformation-ai-disrupt-pdlc.md`
- `jd-archive/closed/2026-06-09-infiniti-tech-lead-ai-engineer.md`
- `jd-archive/closed/2026-06-09-moex-delivery-lead-api-first.md`
- `jd-archive/closed/2026-06-09-pepperstone-head-of-product-engineering.md`
- `jd-archive/closed/2026-06-09-unknown-ai-native-product-technologist.md`
- `jd-archive/closed/2026-06-09-unknown-wholesale-it-head-1c-migration.md`
- `jd-archive/closed/2026-06-10-shaw-daniels-solutions-head-of-engineering.md`
- `jd-archive/closed/2026-06-12-faw-east-europe-it-head.md`
- `jd-archive/closed/2026-06-12-kdr-talent-solutions-head-of-engineering-ai-platform.md`
- `jd-archive/closed/2026-06-12-r7-project-manager.md`
- `jd-archive/closed/2026-06-12-riverhouse-pmo-lead-asana.md`
- `jd-archive/closed/2026-06-14-cdek-customer-journey-crm-head.md`
- `jd-archive/closed/2026-06-14-ey-engineering-lead-director-dublin.md`
- `jd-archive/closed/2026-06-14-totalmobile-platform-software-engineering-director.md`
- `jd-archive/closed/2026-06-14-unisys-senior-director-ai-platforms.md`
- `jd-archive/closed/2026-06-15-epam-technical-delivery-management-director.md`
- `jd-archive/closed/2026-06-15-ksky-software-development-head.md`
- `jd-archive/closed/2026-06-15-marsh-senior-it-director-global-value-streams.md`
- `jd-archive/closed/2026-06-15-positive-technologies-head-of-engineering-cybertesting-access-platform.md`
- `jd-archive/closed/2026-06-17-2gis-project-manager-ai-transformation.md`
- `jd-archive/closed/2026-06-18-anyfin-non-traditional-cto.md`
- `jd-archive/closed/2026-06-18-the-agile-monkeys-general-manager-ai-software-services.md`
- `jd-archive/closed/2026-06-19-gruppa-meta-project-office-head.md`
- `jd-archive/closed/2026-06-19-lovol-global-senior-director-engineering.md`
- `jd-archive/closed/2026-06-19-riverhouse-team-lead-it-ai.md`
- `jd-archive/closed/2026-06-20-alfa-bank-belarus-solution-architect.md`
- `jd-archive/closed/2026-06-23-gendir-ai-lead-ai-engineer.md`
- `jd-archive/closed/2026-06-23-vinted-senior-director-engineering-platform.md`

### Parked

- `jd-archive/parked/2026-06-01-atb-head-of-middle-office-development-center.md`
- `jd-archive/parked/2026-06-03-selecta-ai-solutions-specialist.md`
- `jd-archive/parked/2026-06-10-redholt-vice-president-technology-dubai.md`
- `jd-archive/parked/2026-06-12-azimut-ai-project-lead.md`
- `jd-archive/parked/2026-06-12-greenmoney-cto-technical-leader-mfo-startup.md`
- `jd-archive/parked/2026-06-12-magnit-product-team-lead.md`
- `jd-archive/parked/2026-06-12-sber-ai-project-manager.md`
- `jd-archive/parked/2026-06-19-lego-director-engineering-customer-data-foundation.md`
- `jd-archive/parked/2026-06-19-medallion-director-engineering-ai-platform.md`
- `jd-archive/parked/2026-06-19-vialytics-vp-of-engineering.md`
- `jd-archive/parked/2026-06-19-wex-sr-director-engineering-agentic-ai-service-applications.md`
- `jd-archive/parked/2026-06-20-trt-systems-architect-gcp.md`
- `jd-archive/parked/2026-06-22-ford-credit-director-engineering-digital-products.md`
- `jd-archive/parked/2026-06-22-signify-technology-head-engineering.md`
- `jd-archive/parked/2026-06-23-dataleap-founding-deployment-strategist.md`
- `jd-archive/parked/2026-06-23-dataleap-role-cluster.md`
- `jd-archive/parked/2026-06-23-linkedin-director-software-engineering-dublin-selection.md`
- `jd-archive/parked/2026-06-23-lodgify-director-ai-enablement.md`
- `jd-archive/parked/2026-06-23-parsewise-forward-deployed-engineer.md`
- `jd-archive/parked/2026-06-23-severstal-it-project-manager.md`
- `jd-archive/parked/2026-06-23-viaquant-partners-director-data-engineering.md`
- `jd-archive/parked/2026-06-24-getmatch-hidden-ai-engineer.md`
- `jd-archive/parked/2026-06-24-mufg-azure-cloud-engineering-team-lead.md`
- `jd-archive/parked/2026-06-26-harrington-starr-director-technology-fintech-saas.md`
- `jd-archive/parked/2026-06-26-unknown-ai-automation-engineer-content-author-evaluation.md`
