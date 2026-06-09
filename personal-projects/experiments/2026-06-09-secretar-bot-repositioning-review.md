# Secretar Bot Repositioning Review

- Created: 2026-06-09
- Area: personal-projects / experiments
- Trigger: Yandex Drops / Alice AI "My Memory" sales signal
- Reviewed source: local `secretar_bot` checkout outside Personal Office
- Related signal: `2026-06-09-yandex-drops-secretar-bot-market-signal.md`
- Wording comparison: `2026-06-09-yandex-drops-wording-comparison.md`
- Investor email evidence: `2026-06-09-intelligent-referent-investor-email-evidence.md`
- Messenger evidence: `2026-06-09-leonid-goldort-messenger-evidence.md`

## Short Verdict

`secretar_bot` is not a failed empty idea. It is a real prototype of a voice/text Telegram AI secretary with speech recognition, YandexGPT processing, structured Markdown outputs, sessions, roles, balance, metrics, Docker, database persistence, Redis-backed session state, and a later LangGraph-based idea-capture agent.

The market signal from Yandex Drops does not mean the project was worthless. It means the underlying category was real, but the prototype was not packaged as a continuous personal memory product with retrieval, editing, integrations, and daily action routing.

## What Already Exists

- Telegram interface for voice and text input.
- Yandex SpeechKit transcription pipeline.
- YandexGPT handler with retry-oriented completion flow.
- Final Markdown summary generation.
- Session lifecycle: start, finish, automatic finalization after inactivity.
- User roles, balance, tariffs/cost accounting, request limits.
- PostgreSQL/SQLite storage for users, sessions, and messages.
- Redis/in-memory session state.
- Prometheus metrics for messages, errors, sessions, summaries, tokens, voice minutes, and agent activity.
- Docker and docker-compose deployment path.
- Multilingual support.
- Tests across handlers, voice processing, database, GPT handling, and e2e paths.
- LangGraph secretary agent with persistent structured state: idea summary, questions, keywords, goal, audience, value, format, structure, tone, and risks.
- Corporate concept notes for anonymous feedback, employee ideas, insight extraction, and management reports.
- Investor-facing packaging in `для инвесторов.md`: product description, market and competitor framing, monetization, go-to-market, pilot plan, and investment-use framing.
- Corporate/intranet positioning in `corporateus.md`: employee feedback, idea collection, AI insight extraction, and management reporting.

## Commercialization History From User

User reports that `secretar_bot` / the related AI feedback-secretary idea was packaged and shown to potential investors, who did not reply.

Additional earlier evidence from the user shows that the first working commercial wedge existed by 2025-02-13: a voice bot for CRM discussed with Yuliya Malinina. The user reported that an MVP was ready and that a video/demo showed a dictated salesperson report generating a sales opportunity/deal in Odoo CRM. In that dialogue, the user explicitly contrasted meeting-secretary tools with the missing next step: accepted action points and meeting outcomes should enter execution-control or CRM/task systems and be assigned or routed.

Gmail evidence found on 2026-06-09 strengthens this history: a sent email dated 2025-03-14 with subject `An AI-Based “Intelligent Referent”: A New Opportunity for Our Next Success` pitched an MVP-ready AI digital assistant that captures ideas/tasks by voice or text, asks follow-up questions, suggests structure, turns raw thoughts into documents/plans, and supports corporate conversation/meeting/directive capture with topic modeling, sentiment analysis, clustering, and insights. The email also included a roughly `$200K` investment ask, subscription and corporate/on-premise monetization, and demo/investment next steps.

Important clarification from the user: the March 2025 outreach involved at least two different people who could plausibly provide or support funding:

- Mohamed Fahad: recipient of the 2025-03-14 investor-style email;
- Leonid Goldort: recipient of a separate 2025-03-28 messenger pitch.

The Leonid Goldort messenger evidence adds a second independent timeline point. In that thread, the user described the second idea as already partially implemented, shared the Telegram demonstrator `https://t.me/swarmadviserbot`, and summarized the implemented core as voice -> text -> structuring -> clarifying questions -> summary. The user also described commercialization steps around monetization, landing page, UI polish, legal documents, payment integration, and later B2B on-premise/cloud direction. On 2025-04-01, Leonid replied that it was not interesting for now because he was busy, but that he understood the idea and would keep it in mind.

User then used the available Moscow partner/channel, Viktor Geronimus. Important historical context from the user: at that time personal projects and Fincomtech were not cleanly separated, and the Moscow access path was effectively one shared channel rather than separate project-specific partner tracks. According to the user:

- Geronimus took the idea to Rostelecom;
- Geronimus took the idea to MTS;
- both companies reportedly said the product/category was not needed and they would not invest;
- Viktor also took the idea to Yandex.

This changes the interpretation of the earlier rejection. The project was not only an unpackaged technical prototype. There was at least one investor/corporate-facing packaging attempt, routed through the then-shared Fincomtech/personal-project Moscow channel. The unresolved question is whether the package targeted the wrong buyer, wrong category, wrong timing, wrong wedge, or failed to prove immediate business value.

## Gap Versus Alice "My Memory"

The prototype is strongest at capturing a session and producing a final document. The Yandex-style product category is stronger at continuous memory:

- save many small thoughts without explicit session management;
- search, edit, delete, and add entries later;
- preserve memory as a durable user-owned knowledge base;
- continue across devices and interfaces;
- convert notes into tasks, reminders, calendar items, and structured plans;
- make the capture loop feel instant and always available.

In `secretar_bot`, the missing product loop is:

> quick capture -> durable memory item -> search/retrieve/edit -> route to task/calendar/project -> periodic review.

## Best Repositioning

Do not position this as "another Alice" or "AI headphones without headphones."

The better angle is:

> Private AI secretary for people who need their chaotic voice notes to become files, tasks, decisions, and project memory they actually own.

Possible niches:

- founders and solo consultants who dictate thoughts between calls;
- small teams collecting ideas, complaints, and process pain;
- private Telegram-first life/work secretary;
- portfolio case showing early implementation of voice-to-structured-memory before major-platform validation;
- paid setup/customization service for a private secretary workflow.

## Why Earlier Rejection May Have Happened

The old rejection likely does not prove "nobody needs this." It may show:

- the buyer did not feel the capture pain strongly enough;
- the corporate pitch framed it as feedback/insight infrastructure, while the market signal now validates a more personal continuous-memory loop;
- the output was a Markdown summary, not an action surface;
- trust/privacy questions were unresolved;
- no narrow paying user was selected;
- distribution was weak compared with a platform assistant bundled into hardware and existing chat surfaces.
- large telco/platform buyers may have rejected investment in an external early-stage idea while still considering the category strategically useful later.

## Emotional Reality

This episode is legitimately painful: user reports that the idea was dismissed by investors/corporates and later Yandex launched a visible product in a neighboring category. The useful working frame is not "the old feedback was correct"; it is "the old route to capital and enterprise buy-in failed, while the underlying category now has stronger external validation."

Important boundary from the user: this is not a claim that Yandex stole the idea. The user explicitly recognizes that the idea was "in the air." The pain is still real because the user's adjacent, earlier, packaged work was rejected while a major platform later validated a neighboring category.

Further boundary added by the user: going to court would be pointless because proving anything would be practically impossible, and the user's own estimate is that the probability of actual idea theft tends toward zero. The honest use of this material is therefore retrospective evidence of early execution, packaging, and category instinct, not a legal accusation path.

## Practical Next Slice

If reviving, do not rebuild everything.

Build one thin wedge:

1. Telegram voice/text capture.
2. Store each capture as a durable memory item with title, date, tags, summary, source text, and suggested next action.
3. Add `/remember`, `/find`, `/today`, `/tasks`, `/export`.
4. Export into Personal Office-style Markdown artifacts or a simple local folder.
5. Make a 2-minute demo: "I rant into Telegram, and it becomes decisions, tasks, and searchable memory."

## Commercial Reality

This is not a guaranteed startup. But it is absolutely enough for:

- a portfolio case;
- a consulting demo;
- a private productivity tool;
- a small paid implementation offer;
- a concrete proof that the user can build real agentic workflows, not only talk about them.

## Verification Notes

- `uv run pytest -q` was attempted on 2026-06-09.
- Test run did not execute because `fakeredis` is missing from the current environment.
- `requirements-test.txt` does include `fakeredis==2.31.0`, so this is an environment/setup blocker, not a discovered test failure.
- Repo search found investor/corporate package files: `для инвесторов.md` and `corporateus.md`.
- Wording comparison against Yandex/RBC public materials found strong category-level overlap but no clear evidence of copied wording from local documents.
- Gmail search found the 2025-03-14 investor-style email `An AI-Based “Intelligent Referent”: A New Opportunity for Our Next Success`, providing outbound chronology evidence for the March 2025 packaging.
- User-provided messenger evidence shows a separate 2025-03-28 outreach to Leonid Goldort with a working Telegram demonstrator and the explicit implemented loop: voice -> text -> structuring -> clarifying questions -> summary.
