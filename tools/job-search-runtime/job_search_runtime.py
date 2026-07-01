#!/usr/bin/env python3
"""Operational SQLite state for the Personal Office job-search contour."""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_DB = Path("automation/state/job-search-runtime.sqlite")
SCHEMA_PATH = Path(__file__).with_name("schema.sql")


@dataclass(frozen=True)
class SeededMessage:
    source: str
    gmail_message_id: str
    internal_date: str | None
    notes: str


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: Path) -> None:
    schema = SCHEMA_PATH.read_text(encoding="utf-8")
    with connect(db_path) as conn:
        conn.executescript(schema)
        conn.commit()


def _extract_last_processed_id(text: str) -> str | None:
    match = re.search(r"Last processed Gmail message id:\s*`?([0-9a-fA-F]+)`?", text)
    return match.group(1) if match else None


def _extract_last_internal_date(text: str) -> str | None:
    match = re.search(r"Last processed Gmail internal date:\s*([^\n]+)", text)
    return match.group(1).strip() if match else None


def _extract_backtick_ids(text: str) -> set[str]:
    return {
        value
        for value in re.findall(r"`([0-9a-fA-F]{12,})`", text)
        if not value.startswith("2026")
    }


def _monitor_state_candidates(repo_root: Path) -> Iterable[tuple[str, Path]]:
    yield "hh", repo_root / "automation/state/hh-gmail-monitor-state.md"
    yield "linkedin", repo_root / "automation/state/linkedin-gmail-monitor-state.md"


def read_seed_messages(repo_root: Path) -> list[SeededMessage]:
    messages: list[SeededMessage] = []
    for source, path in _monitor_state_candidates(repo_root):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        internal_date = _extract_last_internal_date(text)
        ids = _extract_backtick_ids(text)
        last_id = _extract_last_processed_id(text)
        if last_id:
            ids.add(last_id)
        for gmail_id in sorted(ids):
            messages.append(
                SeededMessage(
                    source=source,
                    gmail_message_id=gmail_id,
                    internal_date=internal_date if gmail_id == last_id else None,
                    notes=f"seeded from {path.as_posix()}",
                )
            )
    return messages


def seed_monitor_state(db_path: Path, repo_root: Path) -> int:
    init_db(db_path)
    messages = read_seed_messages(repo_root)
    with connect(db_path) as conn:
        for msg in messages:
            conn.execute(
                """
                INSERT INTO processed_messages (
                    source,
                    gmail_message_id,
                    internal_date,
                    status,
                    notes
                )
                VALUES (?, ?, ?, 'seeded_from_markdown_state', ?)
                ON CONFLICT(source, gmail_message_id) DO UPDATE SET
                    internal_date = COALESCE(excluded.internal_date, processed_messages.internal_date),
                    last_seen_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now'),
                    notes = excluded.notes
                """,
                (msg.source, msg.gmail_message_id, msg.internal_date, msg.notes),
            )
        conn.commit()
    return len(messages)


def print_status(db_path: Path) -> None:
    if not db_path.exists():
        print(f"Database missing: {db_path}")
        return
    with connect(db_path) as conn:
        migrations = conn.execute(
            "SELECT version, name, applied_at FROM schema_migrations ORDER BY version"
        ).fetchall()
        print(f"Database: {db_path}")
        for row in migrations:
            print(f"Schema: v{row['version']} {row['name']} applied_at={row['applied_at']}")
        rows = conn.execute(
            """
            SELECT source, status, COUNT(*) AS count
            FROM processed_messages
            GROUP BY source, status
            ORDER BY source, status
            """
        ).fetchall()
        if not rows:
            print("Processed messages: none")
        else:
            print("Processed messages:")
            for row in rows:
                print(f"- {row['source']} {row['status']}: {row['count']}")
        locks = conn.execute("SELECT COUNT(*) AS count FROM run_locks").fetchone()["count"]
        print(f"Run locks: {locks}")


def message_status(db_path: Path, source: str, gmail_message_id: str) -> int:
    init_db(db_path)
    with connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT source, gmail_message_id, gmail_thread_id, internal_date,
                   sender, subject, classification, status, artifact_path,
                   run_id, first_seen_at, last_seen_at, notes
            FROM processed_messages
            WHERE source = ? AND gmail_message_id = ?
            """,
            (source, gmail_message_id),
        ).fetchone()
    if row is None:
        print(json.dumps({"processed": False, "source": source, "gmail_message_id": gmail_message_id}))
    else:
        payload = dict(row)
        payload["processed"] = True
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


def mark_message(
    db_path: Path,
    *,
    source: str,
    gmail_message_id: str,
    gmail_thread_id: str | None,
    internal_date: str | None,
    header_date: str | None,
    sender: str | None,
    subject: str | None,
    classification: str | None,
    status: str,
    artifact_path: str | None,
    run_id: str | None,
    notes: str | None,
) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO processed_messages (
                source,
                gmail_message_id,
                gmail_thread_id,
                internal_date,
                header_date,
                sender,
                subject,
                classification,
                status,
                artifact_path,
                run_id,
                notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(source, gmail_message_id) DO UPDATE SET
                gmail_thread_id = COALESCE(excluded.gmail_thread_id, processed_messages.gmail_thread_id),
                internal_date = COALESCE(excluded.internal_date, processed_messages.internal_date),
                header_date = COALESCE(excluded.header_date, processed_messages.header_date),
                sender = COALESCE(excluded.sender, processed_messages.sender),
                subject = COALESCE(excluded.subject, processed_messages.subject),
                classification = COALESCE(excluded.classification, processed_messages.classification),
                status = excluded.status,
                artifact_path = COALESCE(excluded.artifact_path, processed_messages.artifact_path),
                run_id = COALESCE(excluded.run_id, processed_messages.run_id),
                last_seen_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now'),
                notes = COALESCE(excluded.notes, processed_messages.notes)
            """,
            (
                source,
                gmail_message_id,
                gmail_thread_id,
                internal_date,
                header_date,
                sender,
                subject,
                classification,
                status,
                artifact_path,
                run_id,
                notes,
            ),
        )
        conn.commit()
    print(f"Marked {source}:{gmail_message_id} status={status}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--db",
        default=os.environ.get("JOB_SEARCH_RUNTIME_DB", str(DEFAULT_DB)),
        help=f"SQLite database path (default: {DEFAULT_DB})",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init", help="Initialize or migrate the runtime database")
    sub.add_parser(
        "seed-monitor-state",
        help="Seed processed Gmail ids from Markdown monitor state files",
    )
    sub.add_parser("status", help="Print a compact runtime database status")
    message_status_parser = sub.add_parser(
        "message-status",
        help="Print JSON status for one Gmail message id",
    )
    message_status_parser.add_argument("--source", required=True, choices=["hh", "linkedin"])
    message_status_parser.add_argument("--gmail-message-id", required=True)
    mark_parser = sub.add_parser(
        "mark-message",
        help="Record or update one processed Gmail message id",
    )
    mark_parser.add_argument("--source", required=True, choices=["hh", "linkedin"])
    mark_parser.add_argument("--gmail-message-id", required=True)
    mark_parser.add_argument("--gmail-thread-id")
    mark_parser.add_argument("--internal-date")
    mark_parser.add_argument("--header-date")
    mark_parser.add_argument("--sender")
    mark_parser.add_argument("--subject")
    mark_parser.add_argument("--classification")
    mark_parser.add_argument("--status", default="processed")
    mark_parser.add_argument("--artifact-path")
    mark_parser.add_argument("--run-id")
    mark_parser.add_argument("--notes")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    db_path = Path(args.db)
    repo_root = Path.cwd()
    if args.command == "init":
        init_db(db_path)
        print(f"Initialized {db_path}")
    elif args.command == "seed-monitor-state":
        count = seed_monitor_state(db_path, repo_root)
        print(f"Seeded {count} processed Gmail ids into {db_path}")
    elif args.command == "status":
        print_status(db_path)
    elif args.command == "message-status":
        return message_status(db_path, args.source, args.gmail_message_id)
    elif args.command == "mark-message":
        mark_message(
            db_path,
            source=args.source,
            gmail_message_id=args.gmail_message_id,
            gmail_thread_id=args.gmail_thread_id,
            internal_date=args.internal_date,
            header_date=args.header_date,
            sender=args.sender,
            subject=args.subject,
            classification=args.classification,
            status=args.status,
            artifact_path=args.artifact_path,
            run_id=args.run_id,
            notes=args.notes,
        )
    else:
        raise AssertionError(args.command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
