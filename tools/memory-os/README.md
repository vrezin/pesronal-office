# Memory OS Tool

Local validator and inspector for protocol-managed Personal Office memory.

The tool is intentionally standard-library only.

## Commands

Validate protocol-managed memory and graph files:

```bash
python3 tools/memory-os/memory_os.py validate
```

List concepts:

```bash
python3 tools/memory-os/memory_os.py list --status active
python3 tools/memory-os/memory_os.py list --type ContextCard
```

Show stale review candidates:

```bash
python3 tools/memory-os/memory_os.py stale
```

Check graph JSONL:

```bash
python3 tools/memory-os/memory_os.py graph-check
```

Dry-run retirement checklist:

```bash
python3 tools/memory-os/memory_os.py retire memory/semantic/topics/example.md --reason "Superseded by updated topic card"
```

## Scope

The validator checks files under `memory/protocol/`, `memory/templates/`, and `tools/personal-office-owner-operator-pack/`.

Existing memory files without frontmatter remain valid until they are migrated or touched.
