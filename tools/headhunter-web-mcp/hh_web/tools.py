from __future__ import annotations

import asyncio
import logging
import random
import re

from .browser import get_session
from .email import classify_hh_email, count_digest_vacancy_mentions, parse_hh_digest_links
from .job_intake import mark_duplicate_links, slugify_task_hint
from .models import (
    ApplicationStatus,
    ChatDetails,
    DigestEmailReport,
    DigestResult,
    SearchResult,
    ToolError,
    VacancyFull,
)
from .pages import (
    build_search_url,
    build_suitable_vacancies_url,
    check_logged_in,
    extract_vacancy_id,
    navigate_to_vacancy,
    parse_applications,
    parse_resume_details,
    parse_resumes,
    parse_search_results,
    parse_vacancy_page,
    resolve_resume_id,
)
from .parser import raw_to_vacancy_full, vacancy_to_job_intake

logger = logging.getLogger("hh_web.tools")


async def healthcheck() -> dict:
    session = get_session()
    has_state = session.has_storage_state()
    hh_reachable = False
    logged_in = False
    identity = ""
    limitations: list[str] = []

    if not has_state:
        limitations.append("No storage state found. Run scripts/auth.sh first.")
        return {
            "storage_state_exists": False,
            "hh_reachable": False,
            "logged_in": False,
            "identity": "",
            "limitations": limitations,
        }

    try:
        page = await session.get_page()
        await page.goto("https://hh.ru", wait_until="domcontentloaded", timeout=15000)
        await page.wait_for_timeout(2000)
        hh_reachable = True

        logged_in, msg = await check_logged_in(page)
        limitations.append(msg)

        if logged_in:
            try:
                avatar = page.locator("[data-qa='user-photo-alt']").first
                if await avatar.count() > 0:
                    alt = await avatar.get_attribute("alt") or ""
                    if alt and len(alt) > 3:
                        identity = alt[:2] + "***"
            except Exception:
                pass
            try:
                nav_items = await page.locator("[data-qa='navigation-item-user']").all()
                if nav_items:
                    nav_text = (await nav_items[0].inner_text()).strip()
                    if nav_text:
                        identity = nav_text[:2] + "***"
            except Exception:
                pass

    except Exception as e:
        limitations.append(f"Error during healthcheck: {e}")

    limitations.append("Phase 1: read-only tools only")
    limitations.append("Phase 2 write tools not yet implemented")

    return {
        "storage_state_exists": has_state,
        "hh_reachable": hh_reachable,
        "logged_in": logged_in,
        "identity": identity or "(not detected)",
        "limitations": limitations,
    }


async def get_vacancy(vacancy_id_or_url: str) -> dict:
    session = get_session()
    if not session.has_storage_state():
        return {"error": ToolError(code="AUTH_REQUIRED", message="No storage state. Run scripts/auth.sh.").model_dump()}

    page = await session.new_page()
    try:
        final_url = await navigate_to_vacancy(page, vacancy_id_or_url)
        raw = await parse_vacancy_page(page)

        if raw.get("_auth_required"):
            return {"error": ToolError(code="AUTH_REQUIRED", message="Session expired. Run scripts/auth.sh.").model_dump()}
        if raw.get("_challenge"):
            return {"error": ToolError(code="CHALLENGE_REQUIRED", message="Captcha/challenge detected.").model_dump()}
        if raw.get("_access_denied"):
            return {
                "error": ToolError(
                    code="ACCESS_DENIED",
                    message=raw.get("_access_denied_reason", "Vacancy is not available to this user."),
                    details={
                        "vacancy_id": raw.get("vacancy_id", ""),
                        "url": raw.get("url", ""),
                    },
                ).model_dump()
            }

        vacancy = raw_to_vacancy_full(raw)
        return vacancy_to_job_intake(vacancy)
    except Exception as e:
        return {"error": ToolError(code="EXTRACTION_FAILED", message=str(e)).model_dump()}
    finally:
        await page.close()


async def search_vacancies(
    text: str | None = None,
    area: str | None = None,
    remote: bool | None = None,
    experience: str | None = None,
    salary_from: int | None = None,
    page_num: int = 0,
    limit: int = 20,
) -> dict:
    session = get_session()
    if not session.has_storage_state():
        return {"error": ToolError(code="AUTH_REQUIRED", message="No storage state. Run scripts/auth.sh.").model_dump()}

    search_url = await build_search_url(
        text=text, area=area, remote=remote, experience=experience,
        salary_from=salary_from, page=page_num,
    )

    pg = await session.new_page()
    try:
        await pg.goto(search_url, wait_until="domcontentloaded", timeout=15000)
        await pg.wait_for_timeout(2000)

        cards, total, warnings = await parse_search_results(pg)

        if any("AUTH_REQUIRED" in w for w in warnings):
            return {"error": ToolError(code="AUTH_REQUIRED", message="Session expired.").model_dump()}

        if len(cards) > limit:
            cards = cards[:limit]

        result = SearchResult(
            vacancies=cards,
            total_visible=total,
            search_url=search_url,
            warnings=warnings,
        )
        return result.model_dump()
    except Exception as e:
        return {"error": ToolError(code="SEARCH_FAILED", message=str(e)).model_dump()}
    finally:
        await pg.close()


async def list_resumes() -> dict:
    session = get_session()
    if not session.has_storage_state():
        return {"error": ToolError(code="AUTH_REQUIRED", message="No storage state. Run scripts/auth.sh.").model_dump()}

    page = await session.new_page()
    try:
        resumes, warnings = await parse_resumes(page)
        if any("AUTH_REQUIRED" in w for w in warnings):
            return {"error": ToolError(code="AUTH_REQUIRED", message="Session expired.").model_dump()}
        return {
            "resumes": [resume.model_dump() for resume in resumes],
            "count": len(resumes),
            "warnings": warnings,
        }
    except Exception as e:
        return {"error": ToolError(code="RESUMES_FAILED", message=str(e)).model_dump()}
    finally:
        await page.close()


async def get_resume(resume: str | None = None) -> dict:
    session = get_session()
    if not session.has_storage_state():
        return {"error": ToolError(code="AUTH_REQUIRED", message="No storage state. Run scripts/auth.sh.").model_dump()}

    page = await session.new_page()
    try:
        details, warnings = await parse_resume_details(page, resume)
        if any("AUTH_REQUIRED" in w for w in warnings):
            return {"error": ToolError(code="AUTH_REQUIRED", message="Session expired.").model_dump()}
        if details is None:
            return {"error": ToolError(code="RESUME_NOT_FOUND", message="Could not resolve resume.").model_dump()}
        return {
            "resume": details.model_dump(),
            "warnings": warnings,
        }
    except Exception as e:
        return {"error": ToolError(code="RESUME_FAILED", message=str(e)).model_dump()}
    finally:
        await page.close()


async def get_suitable_vacancies(
    resume: str | None = None,
    page_num: int = 0,
    limit: int = 20,
    remote: bool | None = None,
    salary_from: int | None = None,
    text: str | None = None,
    include_applications: bool = True,
) -> dict:
    session = get_session()
    if not session.has_storage_state():
        return {"error": ToolError(code="AUTH_REQUIRED", message="No storage state. Run scripts/auth.sh.").model_dump()}

    resolve_page = await session.new_page()
    search_page = await session.new_page()
    try:
        resume_id, resume_title, warnings = await resolve_resume_id(resolve_page, resume)
        if any("AUTH_REQUIRED" in w for w in warnings):
            return {"error": ToolError(code="AUTH_REQUIRED", message="Session expired.").model_dump()}
        if not resume_id:
            return {"error": ToolError(code="RESUME_NOT_FOUND", message="Could not resolve resume.").model_dump()}

        search_url = build_suitable_vacancies_url(
            resume_id,
            page=page_num,
            remote=remote,
            salary_from=salary_from,
            text=text,
        )
        await search_page.goto(search_url, wait_until="domcontentloaded", timeout=15000)
        await search_page.wait_for_timeout(2500)

        cards, total, search_warnings = await parse_search_results(search_page)
        warnings.extend(search_warnings)

        if any("AUTH_REQUIRED" in w for w in warnings):
            return {"error": ToolError(code="AUTH_REQUIRED", message="Session expired.").model_dump()}

        if include_applications and cards:
            app_page = await session.new_page()
            try:
                applications, application_warnings = await parse_applications(app_page, max_pages=4)
                warnings.extend(application_warnings)
                application_by_vacancy = {
                    item.get("vacancy_id", ""): item
                    for item in applications
                    if item.get("vacancy_id")
                }
                for card in cards:
                    application = application_by_vacancy.get(card.vacancy_id)
                    if application:
                        try:
                            card.application_status = ApplicationStatus(application.get("status", "unknown"))
                        except ValueError:
                            card.application_status = ApplicationStatus.UNKNOWN
            finally:
                await app_page.close()

        if len(cards) > limit:
            cards = cards[:limit]

        result = SearchResult(
            vacancies=cards,
            total_visible=total,
            search_url=search_url,
            warnings=warnings,
            resume_id=resume_id,
            resume_title=resume_title,
        )
        return result.model_dump()
    except Exception as e:
        return {"error": ToolError(code="SUITABLE_SEARCH_FAILED", message=str(e)).model_dump()}
    finally:
        await search_page.close()
        await resolve_page.close()


async def get_applications(max_pages: int = 4) -> dict:
    session = get_session()
    if not session.has_storage_state():
        return {"error": ToolError(code="AUTH_REQUIRED", message="No storage state. Run scripts/auth.sh.").model_dump()}

    page = await session.new_page()
    try:
        entries, warnings = await parse_applications(page, max_pages=max_pages)
        if any("AUTH_REQUIRED" in w for w in warnings):
            return {"error": ToolError(code="AUTH_REQUIRED", message="Session expired.").model_dump()}
        counts: dict[str, int] = {}
        for entry in entries:
            status = entry.get("status", "unknown")
            counts[status] = counts.get(status, 0) + 1
        return {
            "applications": entries,
            "count": len(entries),
            "status_counts": counts,
            "warnings": warnings,
        }
    except Exception as e:
        return {"error": ToolError(code="APPLICATIONS_FAILED", message=str(e)).model_dump()}
    finally:
        await page.close()


async def extract_from_digest_urls(urls: list[str], limit: int = 10) -> dict:
    session = get_session()
    if not session.has_storage_state():
        return {"error": ToolError(code="AUTH_REQUIRED", message="No storage state. Run scripts/auth.sh.").model_dump()}

    results: list[dict] = []
    processed = 0

    for url in urls[:limit]:
        try:
            vid = await extract_vacancy_id(url.strip())
            page = await session.new_page()
            try:
                await navigate_to_vacancy(page, vid)
                raw = await parse_vacancy_page(page)

                if raw.get("_auth_required"):
                    results.append(DigestResult(
                        url=url, success=False, error="AUTH_REQUIRED", status="auth_required",
                        vacancy_id=vid,
                    ).model_dump())
                    processed += 1
                    continue
                if raw.get("_challenge"):
                    results.append(DigestResult(
                        url=url, success=False, error="CHALLENGE_REQUIRED", status="challenge_required",
                        vacancy_id=vid,
                    ).model_dump())
                    processed += 1
                    continue
                if raw.get("_access_denied"):
                    results.append(DigestResult(
                        url=url,
                        success=False,
                        error=raw.get("_access_denied_reason", "ACCESS_DENIED"),
                        status="access_denied",
                        vacancy_id=vid,
                    ).model_dump())
                    processed += 1
                    continue

                vacancy = raw_to_vacancy_full(raw)
                results.append(DigestResult(
                    url=url,
                    success=True,
                    vacancy=vacancy,
                    status="ok",
                    vacancy_id=vid,
                    title=vacancy.role_title,
                    company=vacancy.company,
                    salary=vacancy.salary,
                ).model_dump())
            finally:
                await page.close()

            processed += 1
            if processed < len(urls[:limit]):
                delay = random.uniform(1.0, 3.0)
                await asyncio.sleep(delay)
        except Exception as e:
            results.append(DigestResult(
                url=url, success=False, error=str(e), status="failed",
            ).model_dump())

    return {"results": results, "processed": processed, "total": len(urls[:limit])}


async def classify_email(body: str, subject: str = "") -> dict:
    return classify_hh_email(body=body, subject=subject).model_dump()


async def parse_digest_email(
    body: str,
    subject: str = "",
    *,
    fetch_details: bool = True,
    job_intake_index_path: str | None = None,
    limit: int = 10,
) -> dict:
    classification = classify_hh_email(body=body, subject=subject)
    links, warnings = await parse_hh_digest_links(body)
    raw_link_count, unique_link_count, duplicate_links_in_email = await count_digest_vacancy_mentions(body)
    marked_links = mark_duplicate_links(links, index_path=job_intake_index_path)

    existing_matches = [link for link in marked_links if link.duplicate]
    new_links = [link for link in marked_links if not link.duplicate]

    extracted_results: list[DigestResult] = []
    if fetch_details and new_links:
        raw_extract = await extract_from_digest_urls([link.url for link in new_links[:limit]], limit=limit)
        for result in raw_extract.get("results", []):
            digest_result = DigestResult(**result)
            matching_link = next(
                (link for link in new_links if link.vacancy_id == digest_result.vacancy_id),
                None,
            )
            if matching_link:
                digest_result.duplicate = matching_link.duplicate
                digest_result.duplicate_matches = matching_link.duplicate_matches
                if not digest_result.title:
                    digest_result.title = matching_link.title
                if not digest_result.company:
                    digest_result.company = matching_link.company
                if not digest_result.salary:
                    digest_result.salary = matching_link.salary_hint
            extracted_results.append(digest_result)

    new_successes = [item for item in extracted_results if item.success and item.status == "ok"]
    inaccessible = [item for item in extracted_results if item.status == "access_denied"]
    failed = [item for item in extracted_results if not item.success and item.status != "access_denied"]

    recommended_next_tasks: list[str] = []
    for item in new_successes:
        vacancy = item.vacancy
        if not vacancy:
            continue
        role = vacancy.role_title or item.vacancy_id
        company = vacancy.company or "unknown"
        slug = slugify_task_hint(f"{company}-{role}")
        recommended_next_tasks.append(
            f"Create job-intake analysis/task for {company} - {role} ({item.vacancy_id}); suggested slug: {slug}"
        )
    for item in inaccessible:
        recommended_next_tasks.append(
            f"Record inaccessible vacancy {item.vacancy_id} and avoid treating it as a parsed JD"
        )

    report = DigestEmailReport(
        email_type=classification.email_type,
        total_links=raw_link_count,
        unique_links=unique_link_count,
        duplicate_links_in_email=duplicate_links_in_email,
        links=marked_links,
        extracted_results=extracted_results,
        existing_matches=existing_matches,
        new_successes=new_successes,
        inaccessible=inaccessible,
        failed=failed,
        recommended_next_tasks=recommended_next_tasks,
        warnings=warnings,
    )
    return report.model_dump()


def _infer_status_from_message(text: str) -> ApplicationStatus:
    lowered = text.lower()
    if "не готовы пригласить" in lowered or "не готов пригласить" in lowered or "к сожалению" in lowered:
        return ApplicationStatus.REJECTED
    if "зарплат" in lowered or "ожидания по зарплате" in lowered:
        return ApplicationStatus.APPLIED
    if "приглас" in lowered or "собеседован" in lowered:
        return ApplicationStatus.INVITATION
    return ApplicationStatus.UNKNOWN


async def open_chat_by_chat_id(chat_id: str) -> dict:
    session = get_session()
    if not session.has_storage_state():
        return {"error": ToolError(code="AUTH_REQUIRED", message="No storage state. Run scripts/auth.sh.").model_dump()}

    page = await session.new_page()
    warnings: list[str] = []
    try:
        url = f"https://hh.ru/applicant/resumes?dl_command=open_chat&chat_id={chat_id}"
        await page.goto(url, wait_until="domcontentloaded", timeout=15000)
        await page.wait_for_timeout(3500)

        body = await page.inner_text("body")
        if "auth" in page.url or "login" in page.url:
            return {"error": ToolError(code="AUTH_REQUIRED", message="Session expired.").model_dump()}
        if "ddos-guard" in (await page.title()).lower() or "ddos-guard" in body.lower():
            return {"error": ToolError(code="CHALLENGE_REQUIRED", message="DDOS-GUARD/challenge detected.").model_dump()}

        lines = [line.strip() for line in body.splitlines() if line.strip()]
        latest_message = ""
        quote_matches = re.findall(r"«([^»]{10,})»", body, flags=re.S)
        message_markers = (
            "здравствуйте",
            "зарплат",
            "ожидания",
            "приглас",
            "к сожалению",
            "спасибо",
            "интерес",
            "свяжемся",
            "собесед",
            "этап",
        )
        likely_messages = [
            " ".join(match.split())
            for match in quote_matches
            if any(marker in match.lower() for marker in message_markers)
        ]
        if likely_messages:
            latest_message = likely_messages[-1]

        vacancy_id = ""
        vacancy_title = ""
        company = ""
        vacancy_url = ""
        links = await page.locator("a[href*='/vacancy/']").all()
        if links:
            href = await links[0].get_attribute("href") or ""
            vacancy_id = await extract_vacancy_id(href)
            vacancy_url = f"https://hh.ru/vacancy/{vacancy_id}" if vacancy_id else href
            try:
                vacancy_title = (await links[0].inner_text()).strip()
            except Exception:
                pass
        else:
            warnings.append("No vacancy link found in chat page")

        # Best-effort company extraction from visible chat text.
        for index, line in enumerate(lines):
            if vacancy_title and line == vacancy_title and index + 1 < len(lines):
                company = lines[index + 1]
                break

        resolved = bool(vacancy_id or latest_message)
        if not resolved:
            warnings.append("Chat content was not visible or could not be resolved from the opened page")

        details = ChatDetails(
            chat_id=chat_id,
            status="ok" if resolved else "not_resolved",
            company=company,
            vacancy_title=vacancy_title,
            vacancy_id=vacancy_id,
            vacancy_url=vacancy_url,
            latest_message_text=latest_message,
            inferred_status=_infer_status_from_message(latest_message),
            warnings=warnings,
        )
        return details.model_dump()
    except Exception as e:
        return {"error": ToolError(code="CHAT_OPEN_FAILED", message=str(e), details={"chat_id": chat_id}).model_dump()}
    finally:
        await page.close()
