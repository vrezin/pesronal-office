#!/usr/bin/env python3
"""Personal Office Memory OS validator.

Standard-library only so the tool can run in the repository without setup.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
from typing import Any


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
MANAGED_ROOTS = [
    REPO_ROOT / "memory" / "protocol",
    REPO_ROOT / "memory" / "templates",
    REPO_ROOT / "tools" / "personal-office-owner-operator-pack",
]
GRAPH_FILES = [
    REPO_ROOT / "memory" / "knowledge-graph" / "nodes.jsonl",
    REPO_ROOT / "memory" / "knowledge-graph" / "edges.jsonl",
]
TEMPLATE_ROOT = REPO_ROOT / "memory" / "templates"

KNOWN_TYPES = {
    "ApprovalRule",
    "Command",
    "Company",
    "Connector",
    "Contact",
    "ContextCard",
    "Decision",
    "Handoff",
    "Playbook",
    "ProductFrame",
    "ProjectContour",
    "Risk",
    "RouteMap",
    "Runbook",
    "Skill",
    "Tool",
    "ValidationSignal",
    "Workflow",
}
KNOWN_STATUSES = {"active", "stale", "superseded", "retired", "archived"}
KNOWN_CONFIDENCE = {"high", "medium", "low", "unknown"}
KNOWN_SENSITIVITY = {"public", "internal", "sensitive", "restricted"}
REQUIRED_FIELDS = {
    "id",
    "type",
    "title",
    "description",
    "status",
    "created",
    "updated",
    "source_refs",
    "confidence",
    "sensitivity",
    "tags",
}


class Finding:
    def __init__(self, path: pathlib.Path, message: str) -> None:
        self.path = path
        self.message = message

    def __str__(self) -> str:
        return f"{self.path.relative_to(REPO_ROOT)}: {self.message}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate and inspect Personal Office memory.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="Validate protocol-managed memory files.")
    sub.add_parser("graph-check", help="Validate knowledge graph JSONL files.")

    list_parser = sub.add_parser("list", help="List protocol-managed concepts.")
    list_parser.add_argument("--status", help="Filter by status.")
    list_parser.add_argument("--type", help="Filter by type.")
    list_parser.add_argument("--tag", help="Filter by tag.")

    sub.add_parser("stale", help="List review candidates past review_after.")

    retire_parser = sub.add_parser("retire", help="Print a retirement checklist for a memory file.")
    retire_parser.add_argument("path", help="Memory file path.")
    retire_parser.add_argument("--reason", required=True, help="Retirement reason.")
    retire_parser.add_argument("--superseded-by", help="Replacement id or path.")

    return parser.parse_args()


def managed_markdown_files() -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for root in MANAGED_ROOTS:
        if root.exists():
            files.extend(path for path in root.rglob("*.md") if path.is_file())
    return sorted(files)


def parse_frontmatter(path: pathlib.Path) -> tuple[dict[str, Any] | None, list[str]]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text.splitlines()
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text.splitlines()
    raw = text[4:end].splitlines()
    return parse_simple_yaml(raw), text[end + 5 :].splitlines()


def parse_simple_yaml(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None
    for line in lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(clean_scalar(line[4:].strip()))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value == "[]":
            data[key] = []
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [] if not inner else [clean_scalar(item.strip()) for item in inner.split(",")]
        elif value == "":
            data[key] = []
        elif value in {"true", "false"}:
            data[key] = value == "true"
        else:
            data[key] = clean_scalar(value)
    return data


def clean_scalar(value: str) -> str:
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def valid_iso_date(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    try:
        dt.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def is_external_ref(value: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", value)) or value.startswith("external:")


def validate_file(path: pathlib.Path) -> list[Finding]:
    findings: list[Finding] = []
    frontmatter, _ = parse_frontmatter(path)
    if frontmatter is None:
        return [Finding(path, "missing or invalid frontmatter block")]

    missing = sorted(field for field in REQUIRED_FIELDS if field not in frontmatter)
    for field in missing:
        findings.append(Finding(path, f"missing required field: {field}"))

    concept_type = frontmatter.get("type")
    if concept_type and concept_type not in KNOWN_TYPES:
        findings.append(Finding(path, f"unknown type: {concept_type}"))
    status = frontmatter.get("status")
    if status and status not in KNOWN_STATUSES:
        findings.append(Finding(path, f"unknown status: {status}"))
    confidence = frontmatter.get("confidence")
    if confidence and confidence not in KNOWN_CONFIDENCE:
        findings.append(Finding(path, f"unknown confidence: {confidence}"))
    sensitivity = frontmatter.get("sensitivity")
    if sensitivity and sensitivity not in KNOWN_SENSITIVITY:
        findings.append(Finding(path, f"unknown sensitivity: {sensitivity}"))

    for field in ("created", "updated", "review_after"):
        if field in frontmatter and frontmatter.get(field) and not valid_iso_date(frontmatter[field]):
            findings.append(Finding(path, f"{field} must be ISO date YYYY-MM-DD"))

    source_refs = frontmatter.get("source_refs")
    if source_refs is not None:
        if not isinstance(source_refs, list):
            findings.append(Finding(path, "source_refs must be a list"))
        else:
            for ref in source_refs:
                if not ref:
                    continue
                if is_external_ref(str(ref)):
                    continue
                if not (REPO_ROOT / str(ref)).exists():
                    findings.append(Finding(path, f"source_ref does not exist: {ref}"))

    tags = frontmatter.get("tags")
    if tags is not None and not isinstance(tags, list):
        findings.append(Finding(path, "tags must be a list"))

    if status == "superseded" and not frontmatter.get("superseded_by"):
        findings.append(Finding(path, "superseded status requires superseded_by"))
    if status in {"retired", "archived"} and not frontmatter.get("retired_reason"):
        findings.append(Finding(path, f"{status} status requires retired_reason"))

    if sensitivity in {"sensitive", "restricted"} and frontmatter.get("do_not_load_raw") is False:
        findings.append(Finding(path, "sensitive/restricted memory cannot set do_not_load_raw: false"))

    return findings


def command_validate() -> int:
    findings: list[Finding] = []
    for path in managed_markdown_files():
        findings.extend(validate_file(path))
    findings.extend(validate_graph_files())
    if findings:
        for finding in findings:
            print(f"ERROR {finding}")
        return 1
    print(f"OK validated {len(managed_markdown_files())} protocol-managed markdown files")
    return 0


def validate_graph_files() -> list[Finding]:
    findings: list[Finding] = []
    for path in GRAPH_FILES:
        if not path.exists():
            findings.append(Finding(path, "graph file missing"))
            continue
        with path.open(encoding="utf-8") as handle:
            for idx, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    json.loads(line)
                except json.JSONDecodeError as exc:
                    findings.append(Finding(path, f"line {idx}: invalid JSON: {exc.msg}"))
    return findings


def command_graph_check() -> int:
    findings = validate_graph_files()
    if findings:
        for finding in findings:
            print(f"ERROR {finding}")
        return 1
    print("OK graph JSONL files parse")
    return 0


def load_concepts() -> list[tuple[pathlib.Path, dict[str, Any]]]:
    concepts: list[tuple[pathlib.Path, dict[str, Any]]] = []
    for path in managed_markdown_files():
        if TEMPLATE_ROOT in path.parents:
            continue
        frontmatter, _ = parse_frontmatter(path)
        if frontmatter:
            concepts.append((path, frontmatter))
    return concepts


def command_list(args: argparse.Namespace) -> int:
    for path, concept in load_concepts():
        if args.status and concept.get("status") != args.status:
            continue
        if args.type and concept.get("type") != args.type:
            continue
        if args.tag and args.tag not in concept.get("tags", []):
            continue
        print(
            "{id}\t{type}\t{status}\t{path}".format(
                id=concept.get("id", ""),
                type=concept.get("type", ""),
                status=concept.get("status", ""),
                path=path.relative_to(REPO_ROOT),
            )
        )
    return 0


def command_stale() -> int:
    today = dt.date.today()
    found = False
    for path, concept in load_concepts():
        review_after = concept.get("review_after")
        if not review_after or not valid_iso_date(review_after):
            continue
        if dt.date.fromisoformat(review_after) <= today:
            found = True
            print(f"{review_after}\t{concept.get('id', '')}\t{path.relative_to(REPO_ROOT)}")
    if not found:
        print("OK no protocol-managed memory is past review_after")
    return 0


def command_retire(args: argparse.Namespace) -> int:
    path = (REPO_ROOT / args.path).resolve()
    if not path.exists():
        print(f"ERROR path not found: {args.path}", file=sys.stderr)
        return 1
    try:
        display_path = path.relative_to(REPO_ROOT)
    except ValueError:
        print("ERROR path is outside repository", file=sys.stderr)
        return 1

    print(f"Retirement checklist for {display_path}:")
    print("- Verify source truth no longer supports active use.")
    print("- Set status to retired or superseded.")
    print(f"- Set retired_reason: {args.reason}")
    if args.superseded_by:
        print(f"- Set superseded_by: {args.superseded_by}")
    print("- Update updated date.")
    print("- Update retrieval index or graph if this item was a route.")
    print("- Do not delete the file in v1.")
    return 0


def main() -> int:
    args = parse_args()
    if args.command == "validate":
        return command_validate()
    if args.command == "graph-check":
        return command_graph_check()
    if args.command == "list":
        return command_list(args)
    if args.command == "stale":
        return command_stale()
    if args.command == "retire":
        return command_retire(args)
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
