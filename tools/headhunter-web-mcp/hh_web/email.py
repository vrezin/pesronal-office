from __future__ import annotations

import re
from urllib.parse import urlparse

from .models import DigestVacancyLink, EmailClassification
from .pages import extract_vacancy_id

_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
_CHAT_ID_RE = re.compile(r"[?&]chat_id=(\d+)")
_VACANCY_URL_RE = re.compile(r"https?://(?:[\w.-]+\.)?hh\.ru/vacancy/\d+[^\s)]*")


def _normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\xa0", " ")).strip()


def classify_hh_email(body: str, subject: str = "") -> EmailClassification:
    """Classify HH notification emails from subject/body text."""
    text = f"{subject}\n{body}"
    lowered = text.lower()
    reasons: list[str] = []
    email_type = "unknown"
    confidence = 0.3

    chat_id = ""
    chat_match = _CHAT_ID_RE.search(text)
    if chat_match:
        chat_id = chat_match.group(1)

    vacancy_id = ""
    vacancy_url_match = _VACANCY_URL_RE.search(text)
    if vacancy_url_match:
        vacancy_id = re.search(r"/vacancy/(\d+)", vacancy_url_match.group(0)).group(1)  # type: ignore[union-attr]

    if "новые вакансии для резюме" in lowered or "подходящие вакансии для резюме" in lowered:
        email_type = "vacancy_digest"
        confidence = 0.95
        reasons.append("contains HH suitable-vacancy digest wording")
    elif "ваши резюме вчера просматривали" in lowered or "вчера ваше резюме привлекло внимание" in lowered:
        email_type = "resume_view"
        confidence = 0.95
        reasons.append("contains resume-view notification wording")
    elif "новое сообщение в чате" in lowered or chat_id:
        email_type = "chat_message"
        confidence = 0.9
        reasons.append("contains HH chat message or chat_id")
    elif "работодатель не готов" in lowered and "вакансия:" in lowered:
        email_type = "explicit_rejection"
        confidence = 0.95
        reasons.append("contains explicit employer rejection and vacancy label")
    elif "отклик" in lowered or "пригласить" in lowered or "собеседован" in lowered:
        email_type = "application_status"
        confidence = 0.65
        reasons.append("contains application-status wording")

    vacancy_title = ""
    company = ""
    title_match = re.search(r"Вакансия:\s*(.+)", body)
    if title_match:
        vacancy_title = _normalize_space(title_match.group(1))
    company_match = re.search(r"компани[ия]:\s*(.+)", body)
    if company_match:
        company = _normalize_space(company_match.group(1))

    return EmailClassification(
        email_type=email_type,
        confidence=confidence,
        reasons=reasons,
        chat_id=chat_id,
        vacancy_id=vacancy_id,
        vacancy_title=vacancy_title,
        company=company,
    )


async def parse_hh_digest_links(body: str) -> tuple[list[DigestVacancyLink], list[str]]:
    """Extract and de-duplicate vacancy links from an HH digest email body."""
    warnings: list[str] = []
    raw_links: list[tuple[str, str]] = []
    for title, url in _MD_LINK_RE.findall(body):
        parsed = urlparse(url)
        if "hh.ru" not in parsed.netloc or "/vacancy/" not in parsed.path:
            continue
        raw_links.append((_normalize_space(title), url))

    if not raw_links:
        for url in _VACANCY_URL_RE.findall(body):
            raw_links.append(("", url))

    seen: set[str] = set()
    links: list[DigestVacancyLink] = []
    lines = [_normalize_space(line) for line in body.splitlines() if _normalize_space(line)]
    for title, url in raw_links:
        vacancy_id = await extract_vacancy_id(url)
        if not vacancy_id or vacancy_id in seen:
            continue
        seen.add(vacancy_id)

        company = ""
        salary_hint = ""
        try:
            title_index = next(i for i, line in enumerate(lines) if line == title)
            for candidate in lines[title_index + 1:title_index + 8]:
                if candidate.startswith("[") or "http" in candidate:
                    continue
                if any(symbol in candidate for symbol in ("₽", "$", "€")) or candidate.lower().startswith(("от ", "до ")):
                    salary_hint = candidate
                    continue
                if not company and candidate not in {"за месяц", "вакансии от проверенных работодателей"}:
                    company = candidate
                    break
        except StopIteration:
            warnings.append(f"Could not infer company for vacancy {vacancy_id}")

        links.append(DigestVacancyLink(
            vacancy_id=vacancy_id,
            url=f"https://hh.ru/vacancy/{vacancy_id}",
            title=title,
            company=company,
            salary_hint=salary_hint,
        ))

    duplicate_count = len(raw_links) - len(links)
    if duplicate_count > 0:
        warnings.append(f"Deduplicated {duplicate_count} repeated vacancy links in email body")

    return links, warnings


async def count_digest_vacancy_mentions(body: str) -> tuple[int, int, int]:
    """Return raw vacancy link count, unique vacancy ids, and duplicate count."""
    urls = [url for _title, url in _MD_LINK_RE.findall(body) if "/vacancy/" in url]
    if not urls:
        urls = _VACANCY_URL_RE.findall(body)
    ids = [await extract_vacancy_id(url) for url in urls]
    unique = {item for item in ids if item}
    return len(ids), len(unique), max(0, len(ids) - len(unique))
