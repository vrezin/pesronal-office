from __future__ import annotations

import re
from pathlib import Path

from .models import DigestVacancyLink


def default_job_intake_index_path() -> Path:
    return (
        Path(__file__).resolve().parents[3]
        / "personal-projects"
        / "personal-brand"
        / "workspace"
        / "job-intake"
        / "INDEX.md"
    )


def _read_optional(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def find_job_intake_matches(
    vacancy_id: str,
    *,
    title: str = "",
    company: str = "",
    index_path: str | None = None,
) -> list[str]:
    """Find likely existing job-intake records for a vacancy."""
    target = Path(index_path).expanduser() if index_path else default_job_intake_index_path()
    job_intake_root = target.parent
    haystacks: list[tuple[str, str]] = []
    haystacks.append((str(target), _read_optional(target)))

    for subdir in ("analyses", "jd-archive"):
        folder = job_intake_root / subdir
        if folder.exists():
            for path in folder.glob("*.md"):
                text = _read_optional(path)
                if vacancy_id and vacancy_id in text:
                    haystacks.append((str(path), text))

    matches: list[str] = []
    for label, text in haystacks:
        if not text:
            continue
        lowered = text.lower()
        if vacancy_id and vacancy_id in text:
            matches.append(label)
            continue

        # Fallback matching is intentionally conservative. Generic titles such
        # as "Unknown", "CTO" or "Project Manager" otherwise create noisy false
        # duplicates against the aggregate INDEX.
        if (
            not vacancy_id
            and title
            and company
            and title.lower() in lowered
            and company.lower() in lowered
        ):
            matches.append(label)

    return sorted(set(matches))


def mark_duplicate_links(
    links: list[DigestVacancyLink],
    *,
    index_path: str | None = None,
) -> list[DigestVacancyLink]:
    """Return copies of links annotated with local job-intake duplicate matches."""
    marked: list[DigestVacancyLink] = []
    for link in links:
        matches = find_job_intake_matches(
            link.vacancy_id,
            title=link.title,
            company=link.company,
            index_path=index_path,
        )
        data = link.model_dump()
        data["duplicate"] = bool(matches)
        data["duplicate_matches"] = matches
        marked.append(DigestVacancyLink(**data))
    return marked


def slugify_task_hint(value: str) -> str:
    lowered = value.lower()
    translit = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
        "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
        "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
        "ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "sch",
        "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
    }
    asciiish = "".join(translit.get(ch, ch) for ch in lowered)
    asciiish = re.sub(r"[^a-z0-9]+", "-", asciiish).strip("-")
    return asciiish[:80] or "hh-vacancy"
