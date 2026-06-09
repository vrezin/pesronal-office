# Askona - CTO AI Department - Analysis

## Metadata

- Date: 2026-06-03
- Source: HH / AI assistant screening chat
- Company: Askona
- Role title: CTO департамента AI / технический лидер AI
- Location / format: гибрид, Москва, 5/2
- Salary: не указана
- Link:
- Archive file: `personal-brand-vladimir-rezin/job-intake/jd-archive/2026-06-03-askona-cto-ai.md`

## Raw JD Summary

Федеральная retail/manufacturing компания ищет CTO AI-департамента: архитектура ML/AI-решений, review моделей и сервисов перед запуском, внедрение новых инструментов, развитие команды. Требуют 8+ лет в IT/Data Engineering/ML, 3+ года tech lead/CTO, LLM, ML-платформы, облака.

## Classification

- Primary track: AI Transformation
- Secondary track: Heavy Enterprise / Digital Transformation
- Seniority: CTO / technical leader
- Role shape: AI platform and implementation leader with hands-on technical screening
- Business context: retail/manufacturing enterprise, likely applied AI and data/ML platformization

## Match Score

- Overall: medium-high
- Leadership: high
- Architecture: high
- Delivery / operations: high
- Domain: medium
- Tech stack: medium
- Hands-on: medium
- Risk: medium-high because they may expect deep ML/DL model ownership, not only LLM application architecture and AI implementation governance.

## Best CV

- Recommended CV: `AI Transformation Lead - AI Automation Architect.pdf`
- Use as-is / tailor: use as-is for first response; tailor if recruiter confirms ML-platform/deep ML ownership is central.
- Tailoring notes: emphasize AI/LLM production implementation, cloud infrastructure leadership, platform architecture, quality gates, model/service review, human-in-the-loop, team leadership. Do not claim deep ML training/GPU/model research ownership.

## Evidence To Use

- Production GenAI/LLM support automation: LLM orchestration, internal APIs, quality control, escalation, measurable economic effect.
- Enterprise engineering leadership: 200+ engineers, 14 teams/leads, high-load e-commerce/delivery platform.
- Cloud infrastructure optimization: reduced infrastructure costs more than 2x while load and product scope grew.
- Data/transaction systems: 1M+ financial transactions/day, reliability, idempotency, consistency, payment/settlement/accounting workflows.
- Quality and review practices: unit testing, SonarQube, quality gates, code review acceleration, production defect reduction.

## Risks

- Deep ML/DL expectation: direct model training/research ownership is not canonical.
- Python/SQL screening: SQL is stronger historically; Java is the main practical engineering language; Python should be positioned as junior/junior+ hands-on, enough to read/write code and prototype, not as fast senior-level production Python.
- Cloud platform: Arameem / ToYou used AWS; position AWS experience as architecture, operations, capacity/cost management and DevOps/SRE leadership rather than daily cloud engineer work.

## Risk Mitigation

- Phrase Python as junior/junior+ hands-on: can read/write code, build simple prototypes/automation and understand LLM/AI workflows, but not as the primary production language.
- Phrase SQL as strong due to long background in Oracle PL/SQL, PostgreSQL/MySQL, high-load transactional systems, data quality/performance.
- For clouds, name AWS directly for Arameem / ToYou; avoid claiming Azure/GCP hands-on unless user confirms.

## Cover Letter

```text
Вижу хороший матч с задачей CTO AI-департамента: мне близка роль, где AI нужно не просто запустить как пилот, а встроить в бизнес-процессы, архитектуру, качество, эксплуатацию и работу команды.

Что могу быть полезно для «Асконы»:
- внедрял GenAI/LLM-автоматизацию поддержки в production: LLM-оркестрация, внутренние API, контроль качества, эскалация человеку, измеримый экономический эффект;
- руководил engineering-организацией 200+ человек и 14 командами/лидами;
- управлял high-load e-commerce/delivery платформой с 300k DAU, 100k+ заказов в день и до 1M+ финансовых транзакций в день;
- оптимизировал AWS-облачную инфраструктуру и снизил стоимость более чем в 2 раза при росте нагрузки;
- внедрял quality gates, unit testing, SonarQube и практики ревью, снижая production defects и ручную нагрузку QA.

Отдельно честно отмечу: моя сильная зона - AI/LLM implementation, архитектура платформ и production governance, а не исследовательская ML/DL-разработка с обучением моделей с нуля.

Буду рад обсудить, какой основной вызов у AI-департамента сейчас: ML-платформа, внедрение LLM в бизнес-процессы, качество моделей/сервисов перед запуском или масштабирование команды.
```

## Screening Answer

```text
Если честно калибровать уровень: основная практическая инженерная база у меня - Java; по текущему hands-on уровню это ближе к middle. Python я читаю и могу писать код, но это не мой основной production-язык: оценил бы себя примерно как junior / junior+. Могу делать прототипы, автоматизацию, интеграции, разбираться в LLM/AI-сценариях и обсуждать архитектуру с командой, но не стал бы позиционировать себя как быстрого senior Python/ML developer.

SQL - сильная зона. У меня большой опыт с transactional/data-heavy системами: Oracle PL/SQL, PostgreSQL/MySQL, высоконагруженные контуры, оптимизация запросов, согласованность данных, финансовые транзакции, reporting/analytics-запросы. В CDEK, банковских проектах и ToYou это было важной частью архитектуры и эксплуатации.

По облакам: основной практический опыт был с AWS в Arameem / ToYou. Работал на уровне архитектуры, эксплуатации, capacity/cost management и взаимодействия с DevOps/SRE-командами. В ToYou занимался оптимизацией AWS-инфраструктуры и сократил расходы более чем в 2 раза при росте нагрузки. Azure/GCP как daily hands-on опыт себе не приписываю, но уверенно работаю с cloud architecture, инфраструктурными решениями, DevOps-процессами и cost/reliability trade-offs.
```

## Screening Answer - Code Review / Architecture Review

```text
Code review и архитектурные ревью были регулярной частью работы, но формат зависел от масштаба команды.

В Финкомтехе, где команда была небольшой, я участвовал в code review на постоянной основе: смотрел ключевые изменения, архитектурные решения, качество реализации, интеграции и риски перед релизом.

В Arameem / ToYou при масштабе 200+ инженеров я не был человеком, который ежедневно ревьюит все pull request'ы. Там процесс был организован через тимлидов, senior-инженеров и архитекторов. Моя зона была скорее CTO/Director-level architecture review: разбор решений по результатам работы архитекторов и команд, согласование ключевых архитектурных изменений, проверка влияния на reliability, scalability, cost, security, payments/settlements и production operations.

То есть hands-on code review у меня был регулярным в компактных командах, а в крупной организации - регулярный архитектурный governance и review наиболее значимых технических решений.
```

## Questions For Recruiter / Hiring Manager

- Что для роли важнее в первые 3-6 месяцев: построить ML-платформу, ускорить внедрение LLM use cases, выстроить review/governance моделей или усилить команду?
- Насколько роль hands-on в Python/ML code review, а насколько это CTO-level architecture, delivery and team leadership?
- Какие cloud/data/ML платформы уже используются внутри «Асконы»?

## Decision

- Apply: yes
- Priority: medium-high
- Next action: answer screening question with calibrated Python/SQL/cloud positioning.
