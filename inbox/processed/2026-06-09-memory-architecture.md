# 2026-06-09 - Memory Architecture Decision

## Decision

Personal Office will use a hybrid file-backed memory architecture:

- short-term working memory;
- episodic dated memory;
- semantic topic memory;
- entity memory;
- procedural memory through `.codex/skills/`;
- retrieval/RAG rules;
- machine-readable wiki maps;
- file-backed knowledge graph.

## Rationale

The repository should act as a personal operating system. Agents need a way to find relevant context without reading every document or relying on chat history.

## Implementation Direction

- `AGENTS.md` becomes a bootloader.
- `wiki/maps/` routes agents to relevant sources, skills, memory, and safety rules.
- `memory/` stores recall and relations.
- Source-of-truth artifacts remain in their domain folders.
- Knowledge graph starts as markdown/jsonl in git before adding external indexing infrastructure.

## Follow-Up

- Periodically consolidate short-term and episodic memory into semantic topics, entities, and graph edges.
- Later evaluate whether BM25, vector search, or a graph database is worth adding.
