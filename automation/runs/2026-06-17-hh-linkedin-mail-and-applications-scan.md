# HH / LinkedIn Mail And Applications Scan Run

- Run time: 2026-06-17 08:52:52 +0700
- Trigger: manual user request
- Tools: Gmail MCP, HH web MCP, HH suitable vacancies MCP
- Status: completed

## Inputs Checked

- LinkedIn Gmail messages after 2026-06-15.
- HH Gmail messages after 2026-06-15.
- HH applicant UI applications, 3 pages / 57 visible applications.
- HH full JDs for:
  - `134191610` - БКС IT & Digital - Руководитель центра внедрения AI;
  - `133770883` - USETECH - Technical Product Owner (GenAI / Умный поиск);
  - `134179698` - SIA ELECTRONICS LATVIA - Automation & AI Specialist.
- HH suitable-vacancy full JDs for:
  - `134215198` - 2ГИС.RnD - Project Manager AI-трансформации;
  - `134218543` - Rubius - AI Solutions Engineer;
  - `134126614` - AP Company / Mosco.ai - Senior AI Architect.
- HH suitable-vacancy fetch for `134214542` - ITQuick - TechLead AI engineer returned captcha/challenge.

## Result

HH application state:

- Rejected: 20
- Viewed: 19
- Not viewed: 15
- Interview: 3

Most interesting active signals:

- `134191610` - БКС IT & Digital - Руководитель центра внедрения AI - viewed - high priority.
- `134051034` - Восточная горнорудная компания - AI Product Lead - viewed - high priority.
- `134024015` - БКС IT & Digital - IT-партнёр AI-департамента - viewed / employer acknowledged review - high priority but likely less ideal than BKS AI Center.
- `133770883` - USETECH - Technical Product Owner (GenAI / Умный поиск) - not viewed - medium-high content fit, possible downlevel risk.
- `134179698` - SIA ELECTRONICS LATVIA - Automation & AI Specialist - not viewed - low employment priority, good consulting signal.

Most interesting fresh HH opportunities:

- `134218543` - Rubius - AI Solutions Engineer - high priority; strongest target-title fit.
- `134215198` - 2ГИС.RnD - Project Manager AI-трансформации - high content fit; title/downlevel risk.
- `134126614` - AP Company / Mosco.ai - Senior AI Architect - medium-high; strong agentic architecture but hands-on screening and comp risk.

Recent rejections captured:

- `134078723` - К-Скай - Руководитель отдела разработки программного обеспечения.
- `134167072` - Т1 ИИ - Руководитель разработки AI, ML, ITL.
- `133449648` - Клируэй Текнолоджис - Архитектор проектов внедрения.
- `130805881` - Simple - СТО / Руководитель департамента.
- `133124220` - ГК Компьютеры и сети - Руководитель проектного офиса.

## Mail Cleanup

After user follow-up, the processed HH and LinkedIn Gmail messages from this scan were archived and marked read. This includes the HH status/message/digest/API emails and the LinkedIn job/reminder/services emails reviewed in the scan.

## Tool Limitations

`mcp__headhunter.hh_get_negotiations` requires OAuth authentication in this session, so application statuses were checked through `mcp__headhunter_web.hh_web_get_applications`.
