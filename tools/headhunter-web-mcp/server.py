from __future__ import annotations

import asyncio
import logging
import sys

from mcp.server.fastmcp import FastMCP

from hh_web.browser import get_session
from hh_web.tools import (
    classify_email,
    extract_from_digest_urls,
    get_applications,
    get_resume,
    get_suitable_vacancies,
    get_vacancy,
    healthcheck,
    list_resumes,
    open_chat_by_chat_id,
    parse_digest_email,
    search_vacancies,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger("hh_web.server")

mcp = FastMCP("headhunter-web-mcp")


@mcp.tool()
async def hh_web_healthcheck() -> str:
    """Verify browser/session health. Returns login status and limitations."""
    import json
    result = await healthcheck()
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def hh_web_get_vacancy(vacancy_id_or_url: str) -> str:
    """Get full vacancy details by HH id or URL. Returns normalized JD as JSON."""
    import json
    result = await get_vacancy(vacancy_id_or_url)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def hh_web_search_vacancies(
    text: str | None = None,
    area: str | None = None,
    remote: bool | None = None,
    experience: str | None = None,
    salary_from: int | None = None,
    page: int = 0,
    limit: int = 20,
) -> str:
    """Search HH vacancies. Returns list of vacancy cards as JSON."""
    import json
    result = await search_vacancies(
        text=text, area=area, remote=remote, experience=experience,
        salary_from=salary_from, page_num=page, limit=limit,
    )
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def hh_web_list_resumes() -> str:
    """List applicant resumes available in the authenticated HH account."""
    import json
    result = await list_resumes()
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def hh_web_get_resume(resume: str | None = None) -> str:
    """Get details and management state for a resume hash or title substring."""
    import json
    result = await get_resume(resume=resume)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def hh_web_get_suitable_vacancies(
    resume: str | None = None,
    page: int = 0,
    limit: int = 20,
    remote: bool | None = None,
    salary_from: int | None = None,
    text: str | None = None,
    include_applications: bool = True,
) -> str:
    """Get HH vacancies suitable for a resume hash or title substring."""
    import json
    result = await get_suitable_vacancies(
        resume=resume,
        page_num=page,
        limit=limit,
        remote=remote,
        salary_from=salary_from,
        text=text,
        include_applications=include_applications,
    )
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def hh_web_get_applications(max_pages: int = 4) -> str:
    """Get sent applications and their statuses from applicant UI."""
    import json
    result = await get_applications(max_pages=max_pages)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def hh_web_extract_from_digest_urls(urls: list[str]) -> str:
    """Batch-open HH vacancy URLs from Gmail digests. Returns per-URL results as JSON."""
    import json
    result = await extract_from_digest_urls(urls)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def hh_web_classify_email(body: str, subject: str = "") -> str:
    """Classify an HH email body into vacancy_digest/resume_view/explicit_rejection/chat_message/application_status."""
    import json
    result = await classify_email(body=body, subject=subject)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def hh_web_parse_digest_email(
    body: str,
    subject: str = "",
    fetch_details: bool = True,
    job_intake_index_path: str | None = None,
    limit: int = 10,
) -> str:
    """Parse an HH vacancy digest email body, de-duplicate vacancies, optionally fetch details, and return a processing report."""
    import json
    result = await parse_digest_email(
        body=body,
        subject=subject,
        fetch_details=fetch_details,
        job_intake_index_path=job_intake_index_path,
        limit=limit,
    )
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def hh_web_open_chat_by_chat_id(chat_id: str) -> str:
    """Open an HH applicant chat by chat_id and infer company, vacancy, latest message, and status when visible."""
    import json
    result = await open_chat_by_chat_id(chat_id)
    return json.dumps(result, ensure_ascii=False, indent=2)


async def _shutdown() -> None:
    session = get_session()
    await session.close()


def main() -> None:
    try:
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        pass
    finally:
        asyncio.run(_shutdown())


if __name__ == "__main__":
    main()
