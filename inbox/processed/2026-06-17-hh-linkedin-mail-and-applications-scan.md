# HH / LinkedIn Mail And Applications Scan

- Created: 2026-06-17
- Source: Gmail MCP, HH web MCP
- Period checked: messages after the previous monitor state from 2026-06-15

## HH Mail Findings

- `К-Скай` / `134078723` / `Руководитель отдела разработки программного обеспечения`: rejection received on 2026-06-16.
- `Т1 ИИ` / `134167072` / `Руководитель разработки AI, ML, ITL.`: rejection received on 2026-06-16.
- `Клируэй Текнолоджис` / `133449648` / `Архитектор проектов внедрения`: rejection received on 2026-06-16.
- `Simple` / `130805881` / `СТО / Руководитель департамента`: rejection received on 2026-06-16.
- `ГК Компьютеры и сети` / `133124220` / `Руководитель проектного офиса`: rejection received on 2026-06-17.
- `БКС IT & Digital` / `134024015` / `IT-партнёр AI-департамента`: employer message says they will review the resume.
- `HRScan` / `134025820` / `Head of Development / CTO`: employer message says they will review the resume.
- HH API application registration request `23262` was rejected; HH says the described functionality is not realizable through the API.

## HH Application Status Snapshot

- Total applications visible in HH applicant UI: 57.
- Status counts: 20 rejected, 19 viewed, 15 not viewed, 3 interview.
- Checked via `hh_web_get_applications`; OAuth `hh_get_negotiations` is not usable in this session because it requires authentication.

## Most Relevant HH Signals

- `БКС IT & Digital` / `134191610` / `Руководитель центра внедрения AI`: viewed; strong match to AI adoption / AI Product / AI Solution positioning.
- `Восточная горнорудная компания` / `134051034` / `AI Product Lead`: viewed; strong match, still waiting.
- `БКС IT & Digital` / `134024015` / `IT-партнёр AI-департамента`: viewed and employer acknowledged review.
- `USETECH` / `133770883` / `Technical Product Owner (GenAI / Умный поиск)`: not viewed; good content fit, likely somewhat down-leveled.
- `SIA ELECTRONICS LATVIA` / `134179698` / `Automation & AI Specialist`: not viewed; useful consulting/service-offer signal, weaker employment target.

## LinkedIn Mail Findings

- Oyster saved-job reminder for `Senior Director, Data Platform and AI`; already applied / waiting in existing protocol.
- Ingenio Global `Technical Delivery Director (AI&Data) | Ireland | 175k EUR`: content and salary interesting, but Ireland relocation / visa-support probability is a practical gate.
- ASMALLWORLD digest includes `CTO (Chief Technology Officer)` remote Spain and several CTO/AI roles in Europe; mostly thin LinkedIn signals until full JDs are opened.
- LinkedIn Services notification says IT Consulting requests are available; not a vacancy, can be handled separately if consulting leads become a priority.

## Actions Taken

- Created full intake for `БКС IT & Digital - Руководитель центра внедрения AI`.
- Created full intake for `USETECH - Technical Product Owner (GenAI / Умный поиск)`.
- Created lightweight intake for `SIA ELECTRONICS LATVIA - Automation & AI Specialist`.
- Created fresh suitable-vacancy intake for `Rubius - AI Solutions Engineer`.
- Created fresh suitable-vacancy intake for `2ГИС.RnD - Project Manager AI-трансформации`.
- Created fresh suitable-vacancy intake for `AP Company / Mosco.ai - Senior AI Architect`.
- Updated vacancy index and company notes for the newly material statuses.
- Converted K-Скай waiting task into a closed rejection task.
- Converted BKS IT-partner apply task into waiting state after confirmed application / employer acknowledgment.
- Cleanup update: processed HH and LinkedIn Gmail messages from this scan were archived and marked read after user follow-up.

## Fresh HH Suitable Vacancies

- `Rubius` / `134218543` / `AI Solutions Engineer`: strongest new title/role fit; presale AI solutions, architecture, MVP/prototypes, LLM/RAG/agents, integrations, internal AI adoption and AI-for-SDLC tooling.
- `2ГИС.RnD` / `134215198` / `Project Manager AI-трансформации`: strong AI adoption and transformation content with remote/Novosibirsk logistics; risk is PM/downlevel title.
- `AP Company / Mosco.ai` / `134126614` / `Senior AI Architect`: strong agentic-systems architecture, remote and visible USD salary; risk is heavy hands-on backend/agent screening and possibly below target comp.
- `ITQuick` / `134214542` / `TechLead AI engineer`: HH web fetch returned captcha/challenge; not analyzed.
