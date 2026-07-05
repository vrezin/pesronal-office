# Job Search Open A/B No-Reply Summary

- Created: 2026-07-05
- Trigger: manual recovery after Telegram request produced no visible bot reply
- User request: `Сделай сводку: Выведи все вакансии а и б классов по которым у тебя не информации что я ответил`
- Source of truth: Pi `personal-projects/personal-brand/workspace/job-intake/INDEX.md`
- Filter: rows with A/B-class, B+-class, B-class, or A-content/B+ priority where `Decision` / `Next` do not show applied, waiting, viewed, rejected, closed, screening, or in-progress reply state.

## Findings

Telegram/Gateway health check:

- `openclaw-gateway.service` is active.
- `personal-office-intake-telegram` is configured, running, connected, and probe reports `works`.
- `openclaw channels status --probe` reported last inbound as `6h ago`, so the specific Telegram summary request did not appear in repo artifacts or recent run logs.
- No matching text was found in `automation/runs`, `inbox`, `personal-projects/personal-brand/workspace/job-intake`, or `tasks`.

Adjacent operational issues:

- `personal-office-pi-job-search-sync.service` is failing because disallowed path changes are present.
- Recent scheduled Gmail monitor blocked on an active runtime lock; the lock was clear by manual check.

## Summary For User

Нашел 17 A/B-ish вакансий, где в `INDEX.md` нет информации, что ты уже откликнулся или что пошел waiting/status thread:

1. iFuture — Solution Architect — B-class  
   Next: Apply with existing Stability & Governance CV; clarify remote from Novosibirsk, compensation, architecture decision authority.

2. Techmunity — Head of Software Engineering / route to CTO — B-class, low practical probability  
   Next: Clarify UK residence/right-to-work, London/Bristol days, B2B from Novosibirsk, hands-on coding screen.

3. Emphasoft — Руководитель Проектного офиса — B-class  
   Next: Clarify Novosibirsk remote/B2B, compensation, Алматы presence, PM team size, PMO authority vs firefighting.

4. Ingenio Global — Technical Delivery Director — B-class  
   Next: Clarify Ireland work authorization, relocation/remote-start, EUR 175k structure, end employer, consulting/pre-sales load.

5. MonetizeMore — Director of Engineering Remote — B-class  
   Next: Clarify whether remote includes Novosibirsk/Russia/UTC+7, salary, contract setup, ad-tech screen, TestDome friction.

6. Xapo Bank — Head of Engineering Remote / Work from Anywhere — A/B-class  
   Next: Clarify whether work from anywhere includes Novosibirsk/Russia/UTC+7, payment/legal setup, salary, Bitcoin/custody screen.

7. Ingenio Global — Transformation Program Director AI & Digital Transformation — B+-class  
   Next: Clarify UK/Ireland remote eligibility, work authorization, compensation, end employer, AI transformation vs pure programme management.

8. Work Channel — Head of Enterprise Architecture — B-class  
   Next: Clarify relocation/work authorization, Limassol timing, EUR 120k ceiling, domain/Mendix screens, architecture decision rights.

9. Evantis Technology — Director of Engineering — B-class  
   Next: Clarify Barcelona hybrid, relocation/work authorization, salary/bonus, end employer, hands-on architecture expectations.

10. Dash0 — Director of Engineering, AI — A/B-class  
    Next: Clarify non-Netherlands remote or relocation sponsorship, salary/equity, hands-on prototyping load, OpenTelemetry/APM screen.

11. Burns Sheehan — Director of Software Engineering, AI-native B2B SaaS — B+/A-content signal  
    Next: Ask whether non-UK remote/B2B from Novosibirsk is possible, who the end employer is, and whether current hands-on coding is expected.

12. RWB / Wildberries & Russ — Senior Project manager — B-class warm-channel check  
    Next: Ask Denis Emelin whether this is a meaningful delivery/process role and who can see the profile internally.

13. byteSpark.ai — Head of AI-Assisted Engineering — B+/A-content  
    Next: Clarify Dubai relocation package, school/housing, net compensation, stack, compliance expectations, hands-on agentic workflow load.

14. Squirro — Head of Engineering — B-class  
    Next: Clarify Zurich hybrid, sponsorship/relocation/cross-border setup, salary band, knowledge-graph/semantic-web screen.

15. Pipekit — Head of Engineering — B-class  
    Next: Clarify remote-country eligibility, contract/payment setup, timezone expectations, Argo/Kubernetes/open-source depth screen.

16. Discovered MENA — Head of Delivery, AI Programme — B-class  
    Next: Decide whether Abu Dhabi relocation is open; if yes, ask relocation, salary, contract, school/family support, role authority.

17. Nearform — Technical Director, Ireland Remote — B-class  
    Next: Clarify whether Ireland residency/right-to-work is mandatory and whether sponsorship/relocation exists.

Already not included because there is reply/application/status evidence: Норникель, Tensor/Saby Екатеринбург, GRS, Dr.Head, Jobgether Deputy CTO, MineHub, Selby Jennings, Альфа-Банк, РСХБ Факторинг, etc.

## Recommended Next

- If the user wants a strict action queue, prioritize: iFuture, Emphasoft, MonetizeMore, Xapo, Work Channel, Dash0.
- Fix intake routing for Telegram summary/report requests so they produce a report artifact and reply, not only vacancy handoffs.
