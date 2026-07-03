#!/usr/bin/env python3
"""Operational SQLite state for the Personal Office job-search contour."""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
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


@dataclass(frozen=True)
class VacancyBackfillEntry:
    vacancy_id: str
    origin: str
    source: str
    date: str
    company: str
    role: str
    status: str
    verdict: str
    effort_class: str | None
    analysis_path: str | None
    task_path: str | None
    selected_cv_path: str | None
    artifact_links: tuple[dict[str, str], ...]


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


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _slugify(value: str, *, max_length: int = 96) -> str:
    translit = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "sch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }
    lowered = value.lower()
    converted = "".join(translit.get(ch, ch) for ch in lowered)
    slug = re.sub(r"[^a-z0-9]+", "-", converted).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return slug[:max_length].strip("-") or "unknown"


def _strip_markdown(value: str) -> str:
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return value.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ").strip()


def _split_markdown_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def _parse_index_rows(index_path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None
    for line in index_path.read_text(encoding="utf-8").splitlines():
        cells = _split_markdown_row(line)
        if not cells:
            continue
        if headers is None:
            if cells[:4] == ["Date", "Company", "Role", "Track"]:
                headers = cells
            continue
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        if len(cells) < len(headers):
            cells.extend([""] * (len(headers) - len(cells)))
        rows.append(dict(zip(headers, cells, strict=False)))
    return rows


def _extract_code_path(value: str) -> str | None:
    match = re.search(r"`([^`]+)`", value)
    if match:
        return match.group(1)
    link = re.search(r"\[[^\]]+\]\(([^)]+)\)", value)
    if link:
        return link.group(1)
    text = value.strip()
    if text and ("/" in text or text.endswith(".md")):
        return text
    return None


def _find_effort_class(*values: str) -> str | None:
    text = " ".join(values)
    match = re.search(r"\b([ABC][+-]?(?:-content)?-class)\b", text, flags=re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"\b([ABC][+-]?)-class\b", text, flags=re.IGNORECASE)
    if match:
        return f"{match.group(1).upper()}-class"
    return None


def _is_job_search_task(path: Path, text: str) -> bool:
    haystack = f"{path.name}\n{text}".lower()
    markers = [
        "vacancy",
        "ваканс",
        "job-intake",
        "employer",
        "recruiter",
        "linkedin",
        "hh",
        "cv",
        "interview",
        "screening",
        "application",
        "отклик",
        "собесед",
    ]
    return any(marker in haystack for marker in markers)


def _load_task_index(repo_root: Path) -> dict[str, list[tuple[Path, str]]]:
    tasks: dict[str, list[tuple[Path, str]]] = {"active": [], "waiting": []}
    for status in tasks:
        task_dir = repo_root / "tasks" / status
        if not task_dir.exists():
            continue
        for path in sorted(task_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            if _is_job_search_task(path, text):
                tasks[status].append((path, text))
    return tasks


def _task_matches_entry(task_path: Path, task_text: str, row: dict[str, str]) -> bool:
    company = _strip_markdown(row.get("Company", ""))
    role = _strip_markdown(row.get("Role", ""))
    stopwords = {
        "analysis",
        "application",
        "architect",
        "company",
        "consultancy",
        "cto",
        "development",
        "digital",
        "director",
        "engineering",
        "global",
        "group",
        "dubai",
        "cyprus",
        "ireland",
        "irish",
        "latvia",
        "london",
        "moscow",
        "remote",
        "head",
        "international",
        "lead",
        "manager",
        "partner",
        "product",
        "recruitment",
        "role",
        "senior",
        "software",
        "technical",
        "technology",
        "technologies",
        "unnamed",
        "unknown",
        "анализ",
        "ваканс",
        "директор",
        "команд",
        "компани",
        "разработ",
        "руковод",
        "техничес",
    }
    primary_company = company.split("/")[0]
    company_tokens = {
        token
        for token in re.findall(r"[a-zа-я0-9]{4,}", primary_company.lower(), flags=re.IGNORECASE)
        if token not in stopwords
    }
    role_tokens = {
        token
        for token in re.findall(r"[a-zа-я0-9]{4,}", role.lower(), flags=re.IGNORECASE)
        if token not in stopwords
    }
    if not company_tokens or not role_tokens:
        return False
    stem = task_path.stem.lower()
    haystack = stem
    company_match = any(token in haystack for token in company_tokens)
    role_match = any(token in stem for token in role_tokens)
    return company_match and role_match


def _infer_historical_status(row: dict[str, str], task_status: str | None) -> str:
    if task_status:
        return task_status
    text = " ".join(
        _strip_markdown(row.get(key, ""))
        for key in ("Decision", "Priority", "Next")
    ).lower()
    if any(marker in text for marker in ["waiting", "viewed", "sent", "interview", "screening", "in progress"]):
        return "waiting"
    if any(marker in text for marker in ["rejected", "closed", "archived", "expired", "skip"]):
        return "historical_closed"
    if any(marker in text for marker in ["parked", "market signal", "no active", "no action", "no by default"]):
        return "historical_no_action"
    if any(marker in text for marker in ["clarify", "maybe", "yes", "apply"]):
        return "historical_open"
    return "historical_backfill"


def _resolve_artifact_path(repo_root: Path, path_value: str | None) -> str | None:
    if not path_value:
        return None
    raw = path_value.strip()
    if not raw:
        return None
    candidates = []
    if raw.startswith("personal-projects/") or raw.startswith("tasks/") or raw.startswith("inbox/"):
        candidates.append(repo_root / raw)
    else:
        candidates.append(repo_root / "personal-projects/personal-brand/workspace/job-intake" / raw)
        candidates.append(repo_root / raw)
    root_resolved = repo_root.resolve()
    for candidate in candidates:
        if candidate.exists():
            resolved = candidate.resolve()
            try:
                return resolved.relative_to(root_resolved).as_posix()
            except ValueError:
                return resolved.as_posix()
    return raw


def _artifact_type(path: str) -> str:
    if "/analyses/" in path:
        return "analysis"
    if "/jd-archive/" in path:
        return "jd"
    if "/search-runs/" in path:
        return "search_run"
    if "/prep/" in path:
        return "prep"
    if path.startswith("tasks/"):
        return "task"
    if path.startswith("inbox/"):
        return "processed_trace"
    if "/summaries/" in path:
        return "summary"
    return "artifact"


def _build_backfill_entries(repo_root: Path, origin: str) -> tuple[list[VacancyBackfillEntry], dict[str, int]]:
    index_path = repo_root / "personal-projects/personal-brand/workspace/job-intake/INDEX.md"
    task_index = _load_task_index(repo_root)
    entries: list[VacancyBackfillEntry] = []
    stats = {"index_rows": 0, "active_tasks": 0, "waiting_tasks": 0, "missing_artifacts": 0}
    used_ids: set[str] = set()
    for row in _parse_index_rows(index_path):
        stats["index_rows"] += 1
        date = _strip_markdown(row.get("Date", ""))
        company = _strip_markdown(row.get("Company", ""))
        role = _strip_markdown(row.get("Role", ""))
        verdict = _strip_markdown(row.get("Decision", ""))
        selected_cv = _strip_markdown(row.get("CV", "")) or None
        analysis = _resolve_artifact_path(repo_root, _extract_code_path(row.get("Analysis", "")))
        task_status = None
        task_path = None
        for status, tasks in task_index.items():
            for path, text in tasks:
                if _task_matches_entry(path, text, row):
                    task_status = status
                    task_path = path.relative_to(repo_root).as_posix()
                    stats[f"{status}_tasks"] += 1
                    break
            if task_path:
                break
        status = _infer_historical_status(row, task_status)
        vacancy_id_base = f"backfill-{date}-{_slugify(company)}-{_slugify(role)}"
        vacancy_id = vacancy_id_base
        suffix = 2
        while vacancy_id in used_ids:
            vacancy_id = f"{vacancy_id_base}-{suffix}"
            suffix += 1
        used_ids.add(vacancy_id)
        links: list[dict[str, str]] = []
        for path_value in (analysis, task_path):
            if not path_value:
                continue
            if not (repo_root / path_value).exists() and not path_value.startswith("../../"):
                stats["missing_artifacts"] += 1
            links.append({"path": path_value, "type": _artifact_type(path_value)})
        entries.append(
            VacancyBackfillEntry(
                vacancy_id=vacancy_id,
                origin=origin,
                source=f"backfill:{origin}",
                date=date,
                company=company,
                role=role,
                status=status,
                verdict=verdict,
                effort_class=_find_effort_class(row.get("Priority", ""), row.get("Next", "")),
                analysis_path=analysis,
                task_path=task_path,
                selected_cv_path=selected_cv,
                artifact_links=tuple(links),
            )
        )
    return entries, stats


def generate_vacancy_backfill_manifest(repo_root: Path, output_path: Path, origin: str) -> None:
    entries, stats = _build_backfill_entries(repo_root, origin)
    payload = {
        "schema_version": 1,
        "kind": "job_search_vacancy_backfill",
        "origin": origin,
        "generated_at": _utc_now(),
        "source_index": "personal-projects/personal-brand/workspace/job-intake/INDEX.md",
        "policy": {
            "mode": "registry_plus_active",
            "pi_state_wins": True,
            "processed_messages": "do_not_write_without_real_gmail_message_id",
        },
        "stats": stats | {"entries": len(entries)},
        "entries": [
            {
                "vacancy_id": entry.vacancy_id,
                "source": entry.source,
                "date": entry.date,
                "company": entry.company,
                "role": entry.role,
                "status": entry.status,
                "verdict": entry.verdict,
                "effort_class": entry.effort_class,
                "analysis_path": entry.analysis_path,
                "task_path": entry.task_path,
                "selected_cv_path": entry.selected_cv_path,
                "artifact_links": list(entry.artifact_links),
            }
            for entry in entries
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {"generated": str(output_path), "entries": len(entries), "stats": payload["stats"]},
            ensure_ascii=False,
            sort_keys=True,
        )
    )


def _load_backfill_manifest(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise ValueError("manifest schema_version must be 1")
    if payload.get("kind") != "job_search_vacancy_backfill":
        raise ValueError("manifest kind must be job_search_vacancy_backfill")
    if not isinstance(payload.get("entries"), list):
        raise ValueError("manifest entries must be a list")
    for index, entry in enumerate(payload["entries"]):
        for key in ("vacancy_id", "source", "company", "role", "status"):
            if not entry.get(key):
                raise ValueError(f"entry {index} missing required field {key}")
        if not str(entry["source"]).startswith("backfill:"):
            raise ValueError(f"entry {index} source must start with backfill:")
    return payload


def _existing_vacancy(conn: sqlite3.Connection, entry: dict) -> sqlite3.Row | None:
    return conn.execute(
        """
        SELECT vacancy_id, source, status, verdict, effort_class, analysis_path, task_path
        FROM vacancies
        WHERE vacancy_id = ?
        """,
        (entry["vacancy_id"],),
    ).fetchone()


def _should_update_existing(row: sqlite3.Row, entry: dict) -> bool:
    if entry.get("status") in {"active", "waiting"}:
        return True
    return str(row["source"]).startswith("backfill:")


def _entry_matches_existing(row: sqlite3.Row, entry: dict) -> bool:
    fields = (
        "status",
        "verdict",
        "effort_class",
        "analysis_path",
        "task_path",
    )
    return all((row[field] or None) == (entry.get(field) or None) for field in fields)


def import_vacancy_backfill(db_path: Path, manifest_path: Path, mode: str) -> int:
    payload = _load_backfill_manifest(manifest_path)
    entries = payload["entries"]
    counters = {
        "entries": len(entries),
        "would_insert": 0,
        "would_update": 0,
        "would_noop": 0,
        "would_skip_existing": 0,
        "inserted": 0,
        "updated": 0,
        "noop": 0,
        "skipped_existing": 0,
        "artifact_links": 0,
        "conflicts": 0,
    }
    conflicts: list[dict[str, str]] = []
    if mode == "dry-run":
        if not db_path.exists():
            counters["would_insert"] = len(entries)
        else:
            with connect(db_path) as conn:
                for entry in entries:
                    existing = _existing_vacancy(conn, entry)
                    if existing is None:
                        counters["would_insert"] += 1
                    elif _entry_matches_existing(existing, entry):
                        counters["would_noop"] += 1
                    elif _should_update_existing(existing, entry):
                        counters["would_update"] += 1
                        if existing["status"] != entry["status"]:
                            counters["conflicts"] += 1
                            conflicts.append(
                                {
                                    "vacancy_id": entry["vacancy_id"],
                                    "existing_status": existing["status"],
                                    "incoming_status": entry["status"],
                                }
                            )
                    else:
                        counters["would_skip_existing"] += 1
        print(json.dumps({"mode": mode, "db": str(db_path), "counters": counters, "conflicts": conflicts[:50]}, ensure_ascii=False, sort_keys=True))
        return 0

    init_db(db_path)
    with connect(db_path) as conn:
        for entry in entries:
            existing = _existing_vacancy(conn, entry)
            if existing is not None and _entry_matches_existing(existing, entry):
                counters["noop"] += 1
                continue
            if existing is not None and not _should_update_existing(existing, entry):
                counters["skipped_existing"] += 1
                continue
            values = (
                entry["vacancy_id"],
                entry["source"],
                None,
                None,
                entry.get("company"),
                entry.get("role"),
                entry.get("verdict"),
                entry.get("effort_class"),
                entry.get("status"),
                entry.get("analysis_path"),
                entry.get("task_path"),
                entry.get("selected_cv_path"),
                None,
            )
            conn.execute(
                """
                INSERT INTO vacancies (
                    vacancy_id,
                    source,
                    external_id,
                    source_url,
                    company,
                    role,
                    verdict,
                    effort_class,
                    status,
                    analysis_path,
                    task_path,
                    selected_cv_path,
                    cover_letter_path
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(vacancy_id) DO UPDATE SET
                    company = COALESCE(excluded.company, vacancies.company),
                    role = COALESCE(excluded.role, vacancies.role),
                    verdict = COALESCE(excluded.verdict, vacancies.verdict),
                    effort_class = COALESCE(excluded.effort_class, vacancies.effort_class),
                    status = excluded.status,
                    analysis_path = COALESCE(excluded.analysis_path, vacancies.analysis_path),
                    task_path = COALESCE(excluded.task_path, vacancies.task_path),
                    selected_cv_path = COALESCE(excluded.selected_cv_path, vacancies.selected_cv_path),
                    updated_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
                """,
                values,
            )
            if existing is None:
                counters["inserted"] += 1
            else:
                counters["updated"] += 1
                if existing["status"] != entry["status"]:
                    counters["conflicts"] += 1
                    conflicts.append(
                        {
                            "vacancy_id": entry["vacancy_id"],
                            "existing_status": existing["status"],
                            "incoming_status": entry["status"],
                        }
                    )
            conn.execute(
                "DELETE FROM artifact_links WHERE source = ? AND source_id = ?",
                (entry["source"], entry["vacancy_id"]),
            )
            for link in entry.get("artifact_links", []):
                conn.execute(
                    """
                    INSERT INTO artifact_links (artifact_path, artifact_type, source, source_id)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(artifact_path, source, source_id) DO UPDATE SET
                        artifact_type = excluded.artifact_type
                    """,
                    (link["path"], link["type"], entry["source"], entry["vacancy_id"]),
                )
                counters["artifact_links"] += 1
        conn.commit()
    print(json.dumps({"mode": mode, "db": str(db_path), "counters": counters, "conflicts": conflicts[:50]}, ensure_ascii=False, sort_keys=True))
    return 0


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
        locks = conn.execute(
            """
            SELECT lock_name, owner, acquired_at, expires_at
            FROM run_locks
            ORDER BY lock_name
            """
        ).fetchall()
        if not locks:
            print("Run locks: 0")
        else:
            print(f"Run locks: {len(locks)}")
            for row in locks:
                print(
                    f"- {row['lock_name']} owner={row['owner']} "
                    f"acquired_at={row['acquired_at']} expires_at={row['expires_at']}"
                )
        vacancy_rows = conn.execute(
            """
            SELECT source, status, COUNT(*) AS count
            FROM vacancies
            GROUP BY source, status
            ORDER BY source, status
            """
        ).fetchall()
        if not vacancy_rows:
            print("Vacancies: none")
        else:
            print("Vacancies:")
            for row in vacancy_rows:
                print(f"- {row['source']} {row['status']}: {row['count']}")


def acquire_lock(db_path: Path, lock_name: str, owner: str, ttl_seconds: int) -> int:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            """
            DELETE FROM run_locks
            WHERE lock_name = ?
              AND expires_at <= strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
            """,
            (lock_name,),
        )
        try:
            conn.execute(
                """
                INSERT INTO run_locks (lock_name, owner, acquired_at, expires_at, heartbeat_at)
                VALUES (
                    ?,
                    ?,
                    strftime('%Y-%m-%dT%H:%M:%fZ', 'now'),
                    strftime('%Y-%m-%dT%H:%M:%fZ', 'now', ?),
                    strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
                )
                """,
                (lock_name, owner, f"+{ttl_seconds} seconds"),
            )
        except sqlite3.IntegrityError:
            row = conn.execute(
                "SELECT owner, acquired_at, expires_at FROM run_locks WHERE lock_name = ?",
                (lock_name,),
            ).fetchone()
            print(
                json.dumps(
                    {
                        "acquired": False,
                        "lock_name": lock_name,
                        "existing": dict(row) if row else None,
                    },
                    sort_keys=True,
                )
            )
            conn.commit()
            return 1
        conn.commit()
    print(json.dumps({"acquired": True, "lock_name": lock_name, "owner": owner}, sort_keys=True))
    return 0


def release_lock(db_path: Path, lock_name: str, owner: str | None) -> int:
    init_db(db_path)
    with connect(db_path) as conn:
        if owner:
            cursor = conn.execute(
                "DELETE FROM run_locks WHERE lock_name = ? AND owner = ?",
                (lock_name, owner),
            )
        else:
            cursor = conn.execute("DELETE FROM run_locks WHERE lock_name = ?", (lock_name,))
        conn.commit()
    print(json.dumps({"released": cursor.rowcount, "lock_name": lock_name}, sort_keys=True))
    return 0


def lock_status(db_path: Path, lock_name: str, active_exit_code: int) -> int:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            """
            DELETE FROM run_locks
            WHERE lock_name = ?
              AND expires_at <= strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
            """,
            (lock_name,),
        )
        row = conn.execute(
            """
            SELECT lock_name, owner, acquired_at, expires_at, heartbeat_at
            FROM run_locks
            WHERE lock_name = ?
            """,
            (lock_name,),
        ).fetchone()
        conn.commit()
    if row is None:
        print(json.dumps({"active": False, "lock_name": lock_name}, sort_keys=True))
        return 0
    print(json.dumps({"active": True, **dict(row)}, sort_keys=True))
    return active_exit_code


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


def telegram_update_status(db_path: Path, update_id: str) -> int:
    init_db(db_path)
    with connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT update_id, chat_id, message_id, received_at, status,
                   run_id, artifact_path, summary
            FROM telegram_updates
            WHERE update_id = ?
            """,
            (update_id,),
        ).fetchone()
    if row is None:
        print(json.dumps({"processed": False, "update_id": update_id}))
    else:
        payload = dict(row)
        payload["processed"] = True
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


def mark_telegram_update(
    db_path: Path,
    *,
    update_id: str,
    chat_id: str | None,
    message_id: str | None,
    received_at: str,
    status: str,
    run_id: str | None,
    artifact_path: str | None,
    summary: str | None,
) -> None:
    init_db(db_path)
    with connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO telegram_updates (
                update_id,
                chat_id,
                message_id,
                received_at,
                status,
                run_id,
                artifact_path,
                summary
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(update_id) DO UPDATE SET
                chat_id = COALESCE(excluded.chat_id, telegram_updates.chat_id),
                message_id = COALESCE(excluded.message_id, telegram_updates.message_id),
                received_at = excluded.received_at,
                status = excluded.status,
                run_id = COALESCE(excluded.run_id, telegram_updates.run_id),
                artifact_path = COALESCE(excluded.artifact_path, telegram_updates.artifact_path),
                summary = COALESCE(excluded.summary, telegram_updates.summary)
            """,
            (update_id, chat_id, message_id, received_at, status, run_id, artifact_path, summary),
        )
        conn.commit()
    print(f"Marked telegram update {update_id} status={status}")


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
    manifest_parser = sub.add_parser(
        "generate-vacancy-backfill-manifest",
        help="Generate a job-intake history backfill manifest from local Markdown",
    )
    manifest_parser.add_argument(
        "--output",
        required=True,
        help="Manifest JSON path to write",
    )
    manifest_parser.add_argument(
        "--origin",
        default="local-personal-office-job-intake",
        help="Backfill origin label used in vacancy source",
    )
    import_parser = sub.add_parser(
        "import-vacancy-backfill",
        help="Validate or apply a vacancy backfill manifest into SQLite",
    )
    import_parser.add_argument("--manifest", required=True)
    import_parser.add_argument("--mode", required=True, choices=["dry-run", "apply"])
    lock_parser = sub.add_parser("acquire-lock", help="Acquire a TTL run lock")
    lock_parser.add_argument("--lock-name", required=True)
    lock_parser.add_argument("--owner", required=True)
    lock_parser.add_argument("--ttl-seconds", type=int, default=3600)
    release_parser = sub.add_parser("release-lock", help="Release a run lock")
    release_parser.add_argument("--lock-name", required=True)
    release_parser.add_argument("--owner")
    lock_status_parser = sub.add_parser("lock-status", help="Print JSON status for one run lock")
    lock_status_parser.add_argument("--lock-name", required=True)
    lock_status_parser.add_argument(
        "--active-exit-code",
        type=int,
        default=1,
        help="Exit code to return when the lock is active",
    )
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
    telegram_status_parser = sub.add_parser(
        "telegram-update-status",
        help="Print JSON status for one Telegram update id",
    )
    telegram_status_parser.add_argument("--update-id", required=True)
    telegram_mark_parser = sub.add_parser(
        "mark-telegram-update",
        help="Record or update one Telegram update id",
    )
    telegram_mark_parser.add_argument("--update-id", required=True)
    telegram_mark_parser.add_argument("--chat-id")
    telegram_mark_parser.add_argument("--message-id")
    telegram_mark_parser.add_argument("--received-at", required=True)
    telegram_mark_parser.add_argument("--status", default="processed")
    telegram_mark_parser.add_argument("--run-id")
    telegram_mark_parser.add_argument("--artifact-path")
    telegram_mark_parser.add_argument("--summary")
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
    elif args.command == "generate-vacancy-backfill-manifest":
        generate_vacancy_backfill_manifest(repo_root, Path(args.output), args.origin)
    elif args.command == "import-vacancy-backfill":
        return import_vacancy_backfill(db_path, Path(args.manifest), args.mode)
    elif args.command == "acquire-lock":
        return acquire_lock(db_path, args.lock_name, args.owner, args.ttl_seconds)
    elif args.command == "release-lock":
        return release_lock(db_path, args.lock_name, args.owner)
    elif args.command == "lock-status":
        return lock_status(db_path, args.lock_name, args.active_exit_code)
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
    elif args.command == "telegram-update-status":
        return telegram_update_status(db_path, args.update_id)
    elif args.command == "mark-telegram-update":
        mark_telegram_update(
            db_path,
            update_id=args.update_id,
            chat_id=args.chat_id,
            message_id=args.message_id,
            received_at=args.received_at,
            status=args.status,
            run_id=args.run_id,
            artifact_path=args.artifact_path,
            summary=args.summary,
        )
    else:
        raise AssertionError(args.command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
