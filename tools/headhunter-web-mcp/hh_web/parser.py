from __future__ import annotations

import re

from .models import ApplicationStatus, VacancyFull


def _clean_text(text: str) -> str:
    lines = text.split("\n")
    cleaned = []
    seen = set()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if cleaned and cleaned[-1] != "":
                cleaned.append("")
            continue
        if stripped in seen:
            continue
        seen.add(stripped)
        cleaned.append(stripped)
    return "\n".join(cleaned)


def _extract_salary(text: str) -> str:
    patterns = [
        r"(?:зарплата|salary|от)\s*[:\s]*(\d[\d\s]*(?:–|-)\d[\d\s]*\s*\S*)",
        r"(\d[\d\s]*(?:–|-)\d[\d\s]*\s*(?:₽|руб|RUB|USD|\$|€))",
        r"(?:от|from)\s+(\d[\d\s]*\s*(?:₽|руб|RUB))",
        r"(\d[\d\s]*\s*(?:₽|руб|RUB|USD|\$|€)\s*(?:на руки|gross|net)?)",
    ]
    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            return m.group(0).strip()
    return ""


def raw_to_vacancy_full(raw: dict) -> VacancyFull:
    """Convert raw page parse dict to VacancyFull model."""
    warnings: list[str] = []
    confidence = 1.0

    title = raw.get("title", "")
    if not title:
        warnings.append("Title not found")
        confidence -= 0.2

    company = raw.get("company", "")
    if not company:
        warnings.append("Company not found")
        confidence -= 0.1

    jd_text = raw.get("raw_jd_markdown", "")
    if not jd_text:
        warnings.append("JD text not found")
        confidence -= 0.3

    salary = raw.get("salary", "")
    if not salary and jd_text:
        salary = _extract_salary(jd_text)
        if salary:
            warnings.append("Salary extracted from JD text, not structured field")

    status_str = raw.get("application_status", "unknown")
    try:
        app_status = ApplicationStatus(status_str)
    except ValueError:
        app_status = ApplicationStatus.UNKNOWN

    return VacancyFull(
        vacancy_id=raw.get("vacancy_id", ""),
        url=raw.get("url", ""),
        role_title=title,
        company=company,
        location_format=raw.get("location", ""),
        salary=salary,
        experience=raw.get("experience", ""),
        schedule=raw.get("schedule", ""),
        work_format=raw.get("work_format", ""),
        published_at=raw.get("published_at", ""),
        raw_jd_markdown=_clean_text(jd_text),
        screening_questions=raw.get("screening_questions", []),
        application_status=app_status,
        extraction_warnings=warnings,
        extraction_confidence=max(0.0, confidence),
    )


def vacancy_to_job_intake(v: VacancyFull) -> dict:
    """Convert VacancyFull to the job-intake JSON shape."""
    return {
        "source": v.source,
        "vacancy_id": v.vacancy_id,
        "url": v.url,
        "company": v.company,
        "role_title": v.role_title,
        "location_format": v.location_format,
        "salary": v.salary,
        "experience": v.experience,
        "schedule": v.schedule,
        "raw_jd_markdown": v.raw_jd_markdown,
        "screening_questions": v.screening_questions,
        "application_status": v.application_status.value,
        "extraction_warnings": v.extraction_warnings,
    }
