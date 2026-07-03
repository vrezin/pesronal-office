#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
SITE_PACKAGE_CANDIDATES = [
    *sorted((REPO_ROOT / ".runtime" / "job-search-venv" / "lib").glob("python*/site-packages")),
    *sorted((REPO_ROOT / "tools" / "linkedin-mcp" / ".venv" / "lib").glob("python*/site-packages")),
]
for site_packages in SITE_PACKAGE_CANDIDATES:
    if site_packages.exists():
        sys.path.insert(0, str(site_packages))
        break

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


def to_plain(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump()
    if isinstance(value, dict):
        return {k: to_plain(v) for k, v in value.items()}
    if isinstance(value, list):
        return [to_plain(v) for v in value]
    return value


async def run() -> int:
    parser = argparse.ArgumentParser(description="LinkedIn MCP client helper")
    parser.add_argument(
        "--url",
        default=os.environ.get("LINKEDIN_MCP_URL", "http://127.0.0.1:8000/mcp"),
        help="LinkedIn MCP streamable-http endpoint",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list-tools", help="List available MCP tools")

    job = sub.add_parser("job-details", help="Fetch LinkedIn job details by job id")
    job.add_argument("job_id")

    search = sub.add_parser("search-jobs", help="Search LinkedIn jobs")
    search.add_argument("keywords")
    search.add_argument("--location")
    search.add_argument("--max-pages", type=int, default=3)
    search.add_argument("--date-posted")
    search.add_argument("--job-type")
    search.add_argument("--experience-level")
    search.add_argument("--work-type")
    search.add_argument("--sort-by")
    search.add_argument("--easy-apply", action="store_true")

    call = sub.add_parser("call", help="Call an arbitrary MCP tool")
    call.add_argument("tool_name")
    call.add_argument("--json", dest="json_args", default="{}")

    args = parser.parse_args()

    async with streamable_http_client(args.url) as (read_stream, write_stream, _get_session_id):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            if args.command == "list-tools":
                result = await session.list_tools()
                print(json.dumps(to_plain(result), ensure_ascii=False, indent=2))
                return 0

            if args.command == "job-details":
                result = await session.call_tool("get_job_details", {"job_id": args.job_id})
                print(json.dumps(to_plain(result), ensure_ascii=False, indent=2))
                return 0

            if args.command == "search-jobs":
                arguments: dict[str, Any] = {
                    "keywords": args.keywords,
                    "location": args.location,
                    "max_pages": args.max_pages,
                    "date_posted": args.date_posted,
                    "job_type": args.job_type,
                    "experience_level": args.experience_level,
                    "work_type": args.work_type,
                    "easy_apply": args.easy_apply,
                    "sort_by": args.sort_by,
                }
                clean_arguments = {k: v for k, v in arguments.items() if v is not None}
                result = await session.call_tool("search_jobs", clean_arguments)
                print(json.dumps(to_plain(result), ensure_ascii=False, indent=2))
                return 0

            if args.command == "call":
                try:
                    arguments = json.loads(args.json_args)
                except json.JSONDecodeError as exc:
                    raise SystemExit(f"Invalid JSON for --json: {exc}") from exc
                result = await session.call_tool(args.tool_name, arguments)
                print(json.dumps(to_plain(result), ensure_ascii=False, indent=2))
                return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(run()))
