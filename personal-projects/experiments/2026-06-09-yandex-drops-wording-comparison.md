# Yandex Drops Wording Comparison

- Created: 2026-06-09
- Area: personal-projects / experiments / secretar_bot
- Purpose: compare public Yandex Drops / Alice AI "My Memory" wording with local `secretar_bot` investor/product materials.
- Related review: `2026-06-09-secretar-bot-repositioning-review.md`

## Sources Checked

External:

- Yandex official news, 2025-12-18: `https://yandex.ru/company/news/18-12-2025-01`
- RBC Trends article, updated 2025-12-22: `https://trends.rbc.ru/trends/innovation/694558409a79479619a953fc`
- Forbes sales article shared by user, 2026-06-09: `https://www.forbes.ru/tekhnologii/562601-andeks-nacal-prodavat-nausniki-s-alisoj-ai`

Local `secretar_bot` materials:

- `README.ru.md`
- `для инвесторов.md`
- `corporateus.md`
- `userstory.md`
- `agent/prompt/secretary.md`

Outbound investor email:

- Gmail sent email dated 2025-03-14 with subject `An AI-Based “Intelligent Referent”: A New Opportunity for Our Next Success`

## Short Verdict

I do not see evidence of copied wording from the local materials into the Yandex/RBC wording.

I do see strong conceptual overlap in the product verbs:

- capture/fix thoughts or ideas;
- use voice or chat;
- structure the input;
- keep records available later;
- turn captured material into reminders, summaries, recommendations, or plans.

The overlap is strongest at the product-loop level, not at the literal phrase level.

## External Wording Clusters

Yandex official wording centers on:

- wearable AI device;
- voice access on the go;
- "My Memory";
- personal affairs and thoughts;
- fixing and returning to records by voice command;
- plans, tasks/affairs, random thoughts;
- structured records and reminders;
- returning through Alice chat or headphones voice interface.

RBC restates the same public story with:

- saving thoughts, plans, and reminders;
- everything the user asks to fix becomes saved in assistant chat;
- records are automatically structured;
- records may become reminders;
- return through chat or headphones voice interface.

## Local Wording Clusters

### README.ru.md

Closest local cluster:

- Telegram bot as virtual secretary;
- receives voice and text messages;
- converts them into structured notes using speech recognition and GPT;
- generates Markdown final summary;
- summary has topic, date, brief description for reminder, tags, full description;
- supports automatic session closure and summary delivery.

This is close to the "voice/text -> structured note -> later use" loop, but it is session/document based, not continuous memory.

### userstory.md

Closest local cluster:

- centralized storage of ideas and insights;
- ML/Big Data structuring and analysis;
- voice or text input through Telegram;
- final summary export;
- idea export to Joplin/Evernote;
- note saving to Yandex.Disk or Google Keep;
- calendar item creation for planning and tasks.

This is the closest local artifact to the Alice "My Memory" loop because it already combines ideas, storage, structure, external note systems, and calendar/tasks.

### agent/prompt/secretary.md

Closest local cluster:

- hold the idea in memory;
- catch the idea, hold it, clarify it, and format it into a document;
- any input, even one word, is a piece of an idea;
- persistent backend state;
- update idea summary, elements, keywords, and questions;
- final output includes key idea elements, structure, risks, recommendations, action plan, and keywords.

This is semantically very close to an AI memory assistant, especially in "chaotic input -> retained structured idea -> action-oriented document." It is not close in public marketing phrasing.

### corporateus.md

Closest local cluster:

- employees send proposals, ideas, complaints, or feedback;
- messages accumulate in a single database;
- AI agents analyze data, identify key insights, and generate recommendations;
- support text, files/screenshots, and voice messages;
- reports with insights and recommendations for leadership.

This is a corporate/organizational version of the "collect unstructured input -> aggregate -> structure -> extract insight" loop.

### для инвесторов.md

Closest local cluster:

- intelligent feedback bot in dialog format;
- embedded into messengers, websites, or mobile apps;
- collects reviews, ratings, and proposals;
- open answers are analyzed by AI for themes, sentiment, complaints, and suggestions;
- real-time contextual feedback;
- templates including idea collection;
- integrations, reports, AI analytics, and future voice-bot module.

This file is less close to "personal memory" and more close to "conversational feedback / CX analytics." It still shares the AI-dialogue and unstructured-input-to-insight pattern.

### 2025-03-14 `Intelligent Referent` investor email

Closest email cluster:

- digital assistant for instant capture of ideas or tasks through voice or text;
- dialogue-based follow-up questions instead of only recording or formatting;
- suggestions for structure and deeper thought refinement;
- raw thoughts transformed into structured documents or plans;
- company use cases around conversations, meetings, directives, unified information space, topic modeling, sentiment analysis, clustering, and insights;
- MVP-ready status, subscription tiers, corporate licensing / on-premise deployment, and approximately `$200K` investment ask.

This email is closer to the personal memory/idea-capture side than the local `для инвесторов.md` file, while still carrying a corporate analytics expansion path.

## Comparison Table

| Product idea | Yandex / RBC | Local materials | Match type |
|---|---|---|---|
| Voice capture on the go | headphones and voice commands | voice input through Telegram; later voice-bot plans | strong concept, different channel |
| Save thoughts/ideas | thoughts, plans, tasks, notes | ideas, insights, proposals, notes, histories | strong concept |
| Structure captured input | structured records; automatically structured | structured notes, summaries, state fields, reports | strong concept |
| Persistent memory | Alice chat and "My Memory" | DB sessions/messages, centralized idea storage, backend state | medium concept; different persistence model |
| Return later / retrieve | return through chat or headphones | export files, external note systems, summaries; no clear search loop in core MVP | partial |
| Reminders / tasks | reminders | calendar records, plans/recommendations, suggested actions | partial to strong |
| Personal UX | personal affairs and thoughts | mostly bot secretary and B2B/corporate feedback | weaker in investor doc, stronger in README/prompt/userstory |
| Enterprise/feedback analytics | not central in Yandex wording | central in investor/corporate docs | local-only emphasis |
| Dialogue-based refinement | not central in public Yandex wording | central in the 2025-03-14 investor email and agent prompt | local-only emphasis |

## Interpretation

The local materials and Yandex wording share a broad product grammar:

> unstructured human speech/thought -> AI structuring -> durable record -> later retrieval/action.

But the market-facing package differs:

- Yandex: personal consumer memory, always-available wearable voice interface, Alice ecosystem.
- `secretar_bot`: Telegram secretary, session summaries, idea/document capture, B2B feedback and insight analytics, future integrations.

The painful overlap is real at the category level. The literal wording overlap is not strong enough to support a claim of copied text or direct borrowing from the local documents.

## Strongest Honest Claim

Best defensible framing:

> The local `secretar_bot` materials contained an earlier adjacent implementation and packaging of AI-assisted voice/text capture, structuring, idea storage, and action-oriented summaries. Yandex later publicly validated a neighboring consumer category: personal AI memory through voice-first devices.

After the Gmail check, this can be strengthened:

> By 2025-03-14, the user had sent an investor-facing `Intelligent Referent` proposal describing an MVP-ready voice/text AI assistant for capturing ideas and tasks, refining them through dialogue, and turning raw thoughts into structured documents or plans.

Avoid claiming:

> Yandex copied our wording or stole the idea.

Because the checked materials do not support that.

## Most Useful Next Move

If this becomes a portfolio or commercial artifact, use the comparison to say:

- "I built an early Telegram/YandexGPT prototype of voice-to-structured-memory workflows."
- "The original packaging over-indexed on B2B feedback analytics."
- "The market later validated the adjacent consumer memory category."
- "The strongest current wedge is private, owned, Telegram-first memory that exports to files/tasks/calendar."
