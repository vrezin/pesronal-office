# Wiki Map Schema

Each `wiki/maps/*.md` file must start with YAML frontmatter.

## Required Fields

```yaml
domain: string
source_of_truth:
  - path
skills:
  - skill-name
memory:
  - path
retrieval:
  - path
safety:
  - rule-id
do_not_read_by_default:
  - path
```

## Field Meaning

- `domain` - stable machine-readable domain id.
- `source_of_truth` - authoritative artifacts for this domain.
- `skills` - local skills to prefer.
- `memory` - memory files useful for recall.
- `retrieval` - retrieval indexes or graph files.
- `safety` - domain-specific guardrails.
- `do_not_read_by_default` - large or sensitive areas to avoid unless needed.
