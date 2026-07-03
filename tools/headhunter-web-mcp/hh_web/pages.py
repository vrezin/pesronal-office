from __future__ import annotations

import os
import re
from urllib.parse import urlencode, urlparse

from playwright.async_api import Page

from .models import ApplicationStatus, ResumeCard, ResumeDetails, VacancyCard


def _nav_timeout(default: int = 15000) -> int:
    value = os.environ.get("HH_WEB_NAV_TIMEOUT_MS", "")
    return int(value) if value else default


def _wait_until(default: str = "commit") -> str:
    return os.environ.get("HH_WEB_WAIT_UNTIL", default)


async def goto_hh(page: Page, url: str, *, timeout: int | None = None) -> None:
    await page.goto(url, wait_until=_wait_until(), timeout=timeout or _nav_timeout())


async def check_logged_in(page: Page) -> tuple[bool, str]:
    """Check if the user is logged in on hh.ru."""
    try:
        await goto_hh(page, "https://hh.ru/applicant/resumes")
        await page.wait_for_timeout(3000)
        url = page.url
        if "auth.hh.ru" in url or "/login" in url:
            return False, "Redirected to login page"
        title = (await page.title()).lower()
        if "авторизуйтесь" in title or "войдите" in title or "sign in" in title:
            return False, "Login page detected in title"

        user_menu = page.locator("[data-qa='user-menu-toggle'], [data-qa='user-photo'], nav[data-qa='header-user-menu']")
        if await user_menu.count() > 0:
            return True, "Session active (user menu found)"

        resume_list = page.locator("[data-qa='resume-list'], [data-qa='resume-card']")
        if await resume_list.count() > 0:
            return True, "Session active (resumes page loaded)"

        content = await page.content()
        if "my(resume" in content or "applicant/resumes" in content:
            return True, "Session active (resumes content)"

        return True, "Session appears active (no auth redirect)"
    except Exception as e:
        return False, f"Error checking login: {e}"


async def extract_vacancy_id(url_or_id: str) -> str:
    """Extract vacancy ID from a URL or return as-is if already an ID."""
    if url_or_id.isdigit():
        return url_or_id
    parsed = urlparse(url_or_id)
    path_parts = [p for p in parsed.path.split("/") if p]
    if "vacancy" in path_parts:
        idx = path_parts.index("vacancy")
        if idx + 1 < len(path_parts):
            return path_parts[idx + 1].split("?")[0]
    return url_or_id


def normalize_vacancy_url(vacancy_id: str) -> str:
    return f"https://hh.ru/vacancy/{vacancy_id}"


async def navigate_to_vacancy(page: Page, vacancy_id_or_url: str) -> str:
    """Navigate to a vacancy page. Returns the final URL."""
    vid = await extract_vacancy_id(vacancy_id_or_url)
    url = normalize_vacancy_url(vid)
    await goto_hh(page, url)
    await page.wait_for_timeout(1500)
    return page.url


async def parse_vacancy_page(page: Page) -> dict:
    """Parse a vacancy page that is already loaded."""
    result: dict = {}
    content = await page.content()
    text = await page.inner_text("body")

    if "auth" in page.url or "login" in page.url:
        result["_auth_required"] = True
        return result

    if "captcha" in text.lower() or "robot" in text.lower():
        result["_challenge"] = True
        return result

    lowered_text = text.lower()
    if "вам недоступна эта вакансия" in lowered_text:
        result["_access_denied"] = True
        result["_access_denied_reason"] = "Vacancy is not available to this user"
        vid_match = re.search(r"/vacancy/(\d+)", page.url)
        result["vacancy_id"] = vid_match.group(1) if vid_match else ""
        result["url"] = page.url
        return result

    vid_match = re.search(r"/vacancy/(\d+)", page.url)
    result["vacancy_id"] = vid_match.group(1) if vid_match else ""
    result["url"] = page.url

    for selector, key in [
        ("h1[data-qa='vacancy-title']", "title"),
        ("h1", "title"),
    ]:
        el = page.locator(selector).first
        if await el.count() > 0:
            result["title"] = (await el.inner_text()).strip()
            break

    for selector in [
        "[data-qa='vacancy-company-name'] a",
        "[data-qa='vacancy-company-name']",
        "a[data-qa='vacancy-company-name']",
    ]:
        el = page.locator(selector).first
        if await el.count() > 0:
            result["company"] = (await el.inner_text()).strip()
            break

    for selector in [
        "[data-qa='vacancy-salary']",
        "p[data-qa='vacancy-salary']",
    ]:
        el = page.locator(selector).first
        if await el.count() > 0:
            result["salary"] = (await el.inner_text()).strip()
            break

    meta_items = await page.locator("[data-qa='vacancy-serp__vacancy-compensation']").all()
    if not meta_items:
        meta_items = await page.locator(".vacancy-serp-feature__item").all()

    for item in meta_items:
        item_text = (await item.inner_text()).strip().lower()
        if any(kw in item_text for kw in ["удалённ", "удаленн", "remote", "гибрид", "hybrid"]):
            result["work_format"] = (await item.inner_text()).strip()
        elif any(kw in item_text for kw in ["опыт", "experience"]):
            result["experience"] = (await item.inner_text()).strip()
        elif any(kw in item_text for kw in ["график", "schedule", "полная", "частичн"]):
            result["schedule"] = (await item.inner_text()).strip()

    for selector in [
        "[data-qa='vacancy-address-with-map']",
        "[data-qa='vacancy-view-raw-address']",
    ]:
        try:
            loc_el = page.locator(selector).first
            if await loc_el.count() > 0:
                location = (await loc_el.inner_text()).strip()
                if location:
                    result["location"] = location
                    break
        except Exception:
            pass

    date_el = page.locator("[data-qa='vacancy-serp__vacancy-date']").first
    if await date_el.count() > 0:
        result["published_at"] = (await date_el.inner_text()).strip()

    jd_section = page.locator("[data-qa='vacancy-description']").first
    if await jd_section.count() > 0:
        result["raw_jd_markdown"] = (await jd_section.inner_text()).strip()
    else:
        alt = page.locator(".vacancy-section").first
        if await alt.count() > 0:
            result["raw_jd_markdown"] = (await alt.inner_text()).strip()
        else:
            result["raw_jd_markdown"] = text[:10000] if len(text) > 10000 else text

    apply_btn = page.locator("[data-qa='vacancy-response-button-top']")
    if await apply_btn.count() > 0:
        btn_text = (await apply_btn.inner_text()).strip().lower()
        if "откликнуться" in btn_text:
            result["application_status"] = "not_applied"
    else:
        applied_indicators = page.locator("[data-qa='vacancy-response-success']")
        if await applied_indicators.count() > 0:
            result["application_status"] = "applied"

    screening = []
    try:
        questions = await page.locator("[data-qa='screening-question']").all()
        for q in questions:
            q_text = (await q.inner_text()).strip()
            if q_text:
                screening.append(q_text)
    except Exception:
        pass
    result["screening_questions"] = screening

    return result


async def build_search_url(
    text: str | None = None,
    area: str | None = None,
    remote: bool | None = None,
    experience: str | None = None,
    salary_from: int | None = None,
    page: int = 0,
) -> str:
    """Build hh.ru search URL from parameters."""
    params: dict[str, str] = {}
    if text:
        params["text"] = text
    if area:
        params["area"] = area
    if remote is not None:
        params["schedule"] = "remote" if remote else "full_day"
    if experience:
        exp_map = {
            "noExperience": "noExperience",
            "between1And3": "between1And3",
            "between3And6": "between3And6",
            "moreThan6": "moreThan6",
            "1-3": "between1And3",
            "3-6": "between3And6",
            "6+": "moreThan6",
        }
        exp_val = exp_map.get(experience, experience)
        params["experience"] = exp_val
    if salary_from:
        params["salary"] = str(salary_from)
        params["only_with_salary"] = "true"
    if page > 0:
        params["page"] = str(page)
    params["order_by"] = "relevance"
    return "https://hh.ru/search/vacancy?" + urlencode(params)


def build_suitable_vacancies_url(
    resume_id: str,
    page: int = 0,
    *,
    remote: bool | None = None,
    salary_from: int | None = None,
    text: str | None = None,
) -> str:
    """Build a search URL for HH vacancies suitable for a specific resume."""
    params: dict[str, str] = {
        "resume": resume_id,
        "from": "resumelist",
        "hhtmFromLabel": "apply_x_more_times",
        "hhtmFrom": "resume_list",
    }
    if page > 0:
        params["page"] = str(page)
    if remote is not None:
        params["schedule"] = "remote" if remote else "full_day"
    if salary_from:
        params["salary"] = str(salary_from)
        params["only_with_salary"] = "true"
    if text:
        params["text"] = text
    return "https://hh.ru/search/vacancy?" + urlencode(params)


def _line_looks_like_salary(line: str) -> bool:
    lowered = line.lower()
    return any(symbol in line for symbol in ["₽", "$", "€"]) or lowered.startswith(("от ", "до "))


def _line_looks_like_experience(line: str) -> bool:
    return "опыт" in line.lower()


def _line_looks_like_work_format(line: str) -> bool:
    lowered = line.lower()
    return any(token in lowered for token in ["удалён", "удален", "гибрид", "на месте работодателя"])


def _line_is_noise(line: str) -> bool:
    lowered = line.lower()
    if not line:
        return True
    if line in {"•"}:
        return True
    if re.fullmatch(r"\d+(?:[.,]\d+)?", line):
        return True
    return any(token in lowered for token in ["отзыв", "откликнуться", "интервью о жизни", "карьерный рост", "дружный коллектив"])


def _parse_vacancy_card_lines(title: str, lines: list[str]) -> dict[str, str]:
    salary = ""
    experience = ""
    work_format = ""
    company = ""
    location = ""

    tail = lines[1:] if lines and lines[0] == title else lines
    cleaned = [line for line in tail if not _line_is_noise(line)]

    for line in cleaned:
        if not salary and _line_looks_like_salary(line):
            salary = line
            continue
        if not experience and _line_looks_like_experience(line):
            experience = line
            continue
        if not work_format and _line_looks_like_work_format(line):
            work_format = line
            continue
        if not company:
            company = line
            continue
        if not location:
            location = line
            break

    return {
        "salary": salary,
        "experience": experience,
        "work_format": work_format,
        "company": company,
        "location": location,
    }


async def parse_search_results(page: Page) -> tuple[list[VacancyCard], int | None, list[str]]:
    """Parse search results page. Returns (cards, total, warnings)."""
    warnings: list[str] = []
    cards: list[VacancyCard] = []

    if "auth" in page.url or "login" in page.url:
        return [], None, ["AUTH_REQUIRED: redirect to login"]

    total: int | None = None
    try:
        body_text = await page.inner_text("body")
        m = re.search(r"Найден[ао]?\s+([\d\s]+)\s+(?:подходящ\w+\s+)?ваканс", body_text)
        if m:
            total = int(m.group(1).replace("\xa0", "").replace(" ", ""))
    except Exception:
        warnings.append("Could not parse total count")

    title_links = await page.locator("[data-qa='serp-item__title']").all()

    for title_el in title_links:
        try:
            title = (await title_el.inner_text()).strip()
            href = await title_el.get_attribute("href") or ""
            vid = ""
            if href:
                vm = re.search(r"/vacancy/(\d+)", href)
                if vm:
                    vid = vm.group(1)

            card_text = ""
            try:
                card_text = await title_el.locator("xpath=ancestor::*[@data-qa='vacancy-serp__vacancy'][1]").inner_text()
            except Exception:
                try:
                    card_text = await title_el.locator("xpath=ancestor::div[contains(@class, 'vacancy-card')][1]").inner_text()
                except Exception:
                    card_text = ""

            lines = [_normalize_space(line) for line in card_text.splitlines() if _normalize_space(line)]
            parsed = _parse_vacancy_card_lines(_normalize_space(title), lines)

            if vid and title:
                cards.append(VacancyCard(
                    vacancy_id=vid,
                    url=f"https://hh.ru/vacancy/{vid}",
                    title=title,
                    company=parsed["company"],
                    salary=parsed["salary"],
                    location=parsed["location"],
                    work_format=parsed["work_format"],
                    experience=parsed["experience"],
                ))
        except Exception as e:
            warnings.append(f"Failed to parse item: {e}")

    return cards, total, warnings


async def parse_resumes(page: Page) -> tuple[list[ResumeCard], list[str]]:
    """Parse the applicant resume list page."""
    warnings: list[str] = []
    resumes: list[ResumeCard] = []

    await goto_hh(page, "https://hh.ru/applicant/resumes")
    await page.wait_for_timeout(3000)

    if "auth" in page.url or "login" in page.url:
        return [], ["AUTH_REQUIRED"]

    links = await page.locator("a[data-qa^='resume-card-link-']").all()
    seen: set[str] = set()
    for link in links:
        try:
            href = await link.get_attribute("href") or ""
            parsed_url = urlparse(href)
            resume_id = parsed_url.path.rstrip("/").split("/")[-1]
            if not resume_id or resume_id in seen:
                continue

            text = await link.inner_text()
            lines = [_normalize_space(line) for line in text.splitlines() if _normalize_space(line)]
            if not lines:
                continue

            employment = lines[0] if len(lines) > 0 else ""
            title = lines[1] if len(lines) > 1 else lines[0]
            salary = ""
            work_format = ""
            if len(lines) > 2:
                details = lines[2]
                parts = [_normalize_space(part) for part in re.split(r"\s+·\s+", details) if _normalize_space(part)]
                if parts:
                    salary = parts[0]
                if len(parts) > 1:
                    work_format = parts[1]

            card_text = ""
            try:
                card_text = await link.locator("xpath=ancestor::*[@data-qa='resume'][1]").inner_text()
            except Exception:
                card_text = text
            card_lines = [_normalize_space(line) for line in card_text.splitlines() if _normalize_space(line)]

            views = ""
            new_views = ""
            invitations = ""
            lift_status = ""
            suitable_vacancies_url = build_suitable_vacancies_url(resume_id)
            for index, line in enumerate(card_lines):
                line_lower = line.lower()
                if line_lower == "просмотры" and index + 1 < len(card_lines):
                    views = card_lines[index + 1]
                    if index + 2 < len(card_lines) and card_lines[index + 2].startswith("+"):
                        new_views = card_lines[index + 2]
                elif line_lower == "приглашения" and index + 1 < len(card_lines):
                    invitations = card_lines[index + 1]
                elif line_lower.startswith("поднять"):
                    lift_status = line

            seen.add(resume_id)
            resumes.append(ResumeCard(
                resume_id=resume_id,
                title=title,
                url=f"https://hh.ru/resume/{resume_id}",
                employment=employment,
                salary=salary,
                work_format=work_format,
                views=views,
                new_views=new_views,
                invitations=invitations,
                lift_status=lift_status,
                suitable_vacancies_url=suitable_vacancies_url,
            ))
        except Exception as e:
            warnings.append(f"Failed to parse resume card: {e}")

    return resumes, warnings


async def resolve_resume_id(page: Page, resume: str | None) -> tuple[str, str, list[str]]:
    """Resolve a resume hash by exact hash or title substring."""
    warnings: list[str] = []
    resumes, parse_warnings = await parse_resumes(page)
    warnings.extend(parse_warnings)
    if not resumes:
        return "", "", warnings

    if resume:
        needle = resume.strip().lower()
        for candidate in resumes:
            if candidate.resume_id == resume:
                return candidate.resume_id, candidate.title, warnings
        title_matches = [candidate for candidate in resumes if needle in candidate.title.lower()]
        if len(title_matches) == 1:
            candidate = title_matches[0]
            return candidate.resume_id, candidate.title, warnings
        if len(title_matches) > 1:
            warnings.append(f"Multiple resumes match '{resume}': " + ", ".join(item.title for item in title_matches))
            candidate = title_matches[0]
            return candidate.resume_id, candidate.title, warnings
        warnings.append(f"No resume matched '{resume}', using the first resume from the list")

    candidate = resumes[0]
    return candidate.resume_id, candidate.title, warnings


def _extract_after_label(lines: list[str], label: str) -> str:
    target = label.lower()
    for index, line in enumerate(lines):
        if line.lower() == target and index + 1 < len(lines):
            return lines[index + 1]
    return ""


def _extract_section(lines: list[str], start_label: str, stop_labels: set[str], max_lines: int = 40) -> str:
    target = start_label.lower()
    collected: list[str] = []
    in_section = False
    for line in lines:
        lowered = line.lower()
        if lowered == target:
            in_section = True
            continue
        if in_section:
            if lowered in {label.lower() for label in stop_labels}:
                break
            collected.append(line)
            if len(collected) >= max_lines:
                break
    return "\n".join(collected).strip()


async def parse_resume_details(page: Page, resume: str | None = None) -> tuple[ResumeDetails | None, list[str]]:
    """Open and parse one resume detail page."""
    warnings: list[str] = []
    resume_id, resume_title, resolve_warnings = await resolve_resume_id(page, resume)
    warnings.extend(resolve_warnings)
    if not resume_id:
        return None, warnings

    await goto_hh(page, f"https://hh.ru/resume/{resume_id}?hhtmFrom=resume_list")
    await page.wait_for_timeout(3000)

    if "auth" in page.url or "login" in page.url:
        return None, ["AUTH_REQUIRED"]

    body_text = await page.inner_text("body")
    lines = [_normalize_space(line) for line in body_text.splitlines() if _normalize_space(line)]

    title = ""
    try:
        title = _normalize_space(await page.locator("h1").first.inner_text())
    except Exception:
        title = resume_title
    if not title:
        title = resume_title

    salary = ""
    employment = ""
    work_format = ""
    for index, line in enumerate(lines):
        if line == title and index + 1 < len(lines):
            salary = lines[index + 1]
        if line.startswith("Тип занятости:"):
            employment = _normalize_space(line.removeprefix("Тип занятости:"))
        elif line.startswith("Формат работы:"):
            work_format = _normalize_space(line.removeprefix("Формат работы:"))

    contacts: list[str] = []
    for index, line in enumerate(lines):
        if "@" in line and "." in line:
            contacts.append(line)
        if re.search(r"\+?\d[\d\s().-]{7,}", line):
            contacts.append(line)
    contacts = list(dict.fromkeys(contacts))

    experience_total = ""
    for line in lines:
        if line.startswith("Опыт работы:"):
            experience_total = line.removeprefix("Опыт работы:").strip()
            break

    skills: list[str] = []
    try:
        skill_text = _extract_section(
            lines,
            "Навыки",
            {"Указать уровни", "Редактировать", "Образование", "Добавить"},
            max_lines=60,
        )
        skills = [
            item
            for item in skill_text.splitlines()
            if item and item not in {"Указать уровни", "Редактировать"}
        ]
    except Exception:
        pass

    about = _extract_section(
        lines,
        "О себе",
        {"По-русски", "Завершённость резюме", "Завершенность резюме"},
        max_lines=80,
    )

    completion_text = ""
    completion_index = next((i for i, line in enumerate(lines) if line.lower() in {"завершённость резюме", "завершенность резюме"}), -1)
    if completion_index >= 0:
        completion_text = "\n".join(lines[completion_index:completion_index + 10])

    lift_details = ""
    auto_raise = ""
    visibility = ""
    suitable_vacancies_count: int | None = None
    suitable_vacancies_url = build_suitable_vacancies_url(resume_id)
    for index, line in enumerate(lines):
        lowered = line.lower()
        if lowered == "поднятие резюме" and index + 1 < len(lines):
            lift_details = lines[index + 1]
        elif lowered == "поднимать автоматически" and not auto_raise:
            auto_raise = line
        elif lowered == "видимость резюме" and index + 1 < len(lines):
            visibility = lines[index + 1]
        elif "подобрали для вас" in lowered and "подходящ" in lowered:
            match = re.search(r"(\d[\d\s]*)", line)
            if match:
                suitable_vacancies_count = int(match.group(1).replace(" ", ""))

    language = "По-русски" if "По-русски" in lines else ""

    return ResumeDetails(
        resume_id=resume_id,
        title=title,
        url=f"https://hh.ru/resume/{resume_id}",
        employment=employment,
        salary=salary,
        work_format=work_format,
        lift_status=lift_details,
        suitable_vacancies_url=suitable_vacancies_url,
        search_status="",
        contacts=contacts,
        experience_total=experience_total,
        skills=skills,
        about=about,
        completion_text=completion_text,
        lift_details=lift_details,
        auto_raise=auto_raise,
        visibility=visibility,
        suitable_vacancies_count=suitable_vacancies_count,
        language=language,
        raw_summary="\n".join(lines[:120]),
    ), warnings


def _normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\xa0", " ")).strip()


def _application_status_from_text(status_text: str) -> ApplicationStatus:
    st = _normalize_space(status_text).lower()
    if "не просмотрен" in st:
        return ApplicationStatus.NOT_VIEWED
    if "просмотрен" in st:
        return ApplicationStatus.VIEWED
    if "отказ" in st or "отклонен" in st or "отклонён" in st:
        return ApplicationStatus.REJECTED
    if "приглаш" in st:
        return ApplicationStatus.INVITATION
    if "собеседован" in st or "интервью" in st:
        return ApplicationStatus.INTERVIEW
    if "выход на работу" in st:
        return ApplicationStatus.INTERVIEW
    if "ожидание" in st or "отклик" in st:
        return ApplicationStatus.APPLIED
    return ApplicationStatus.UNKNOWN


async def parse_applications(page: Page, max_pages: int = 4) -> tuple[list[dict], list[str]]:
    """Parse applications/negotiations pages from the applicant UI."""
    warnings: list[str] = []
    entries: list[dict] = []

    seen_vacancy_ids: set[str] = set()
    safe_max_pages = max(1, min(max_pages, 10))

    for page_num in range(safe_max_pages):
        url = "https://hh.ru/applicant/negotiations"
        if page_num > 0:
            url = f"{url}?page={page_num}"

        await goto_hh(page, url)
        await page.wait_for_timeout(2500)

        if "auth" in page.url or "login" in page.url:
            return [], ["AUTH_REQUIRED"]

        links = await page.locator("a[href*='/vacancy/'][href*='negotiation_list']").all()
        if not links:
            if page_num == 0:
                warnings.append("No negotiation vacancy links found on first page")
            break

        page_entries = 0
        for link in links:
            try:
                title = _normalize_space(await link.inner_text())
                href = await link.get_attribute("href") or ""
                vacancy_match = re.search(r"/vacancy/(\d+)", href)
                vacancy_id = vacancy_match.group(1) if vacancy_match else ""
                if not vacancy_id or vacancy_id in seen_vacancy_ids:
                    continue

                title_block_text = await link.locator("xpath=ancestor::div[1]").inner_text()
                title_lines = [
                    _normalize_space(line)
                    for line in title_block_text.splitlines()
                    if _normalize_space(line)
                ]

                company = ""
                date = ""
                if title in title_lines:
                    title_index = title_lines.index(title)
                    if title_index + 1 < len(title_lines):
                        company = title_lines[title_index + 1]
                    if title_index + 2 < len(title_lines):
                        date = title_lines[title_index + 2]

                card_text = await link.locator("xpath=ancestor::div[5]").inner_text()
                card_lines = [
                    _normalize_space(line)
                    for line in card_text.splitlines()
                    if _normalize_space(line)
                ]
                status_text = card_lines[0] if card_lines else ""
                status = _application_status_from_text(status_text)
                if status == ApplicationStatus.UNKNOWN:
                    continue

                online_text = ""
                response_rate_text = ""
                for line in card_lines:
                    line_lower = line.lower()
                    if "был онлайн" in line_lower or "была онлайн" in line_lower:
                        online_text = line
                    elif "разбирает" in line_lower and "отклик" in line_lower:
                        response_rate_text = line

                seen_vacancy_ids.add(vacancy_id)
                page_entries += 1
                entries.append({
                    "status": status.value,
                    "title": title,
                    "company": company,
                    "vacancy_id": vacancy_id,
                    "url": f"https://hh.ru/vacancy/{vacancy_id}",
                    "date": date,
                    "status_text": status_text,
                    "online_text": online_text,
                    "response_rate_text": response_rate_text,
                    "page": page_num,
                })
            except Exception as e:
                warnings.append(f"Failed to parse application link on page {page_num}: {e}")

        if page_entries == 0:
            break

    return entries, warnings
