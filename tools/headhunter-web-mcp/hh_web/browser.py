from __future__ import annotations

import asyncio
import logging
import os
from pathlib import Path

from playwright.async_api import async_playwright, Browser, BrowserContext, Page, Playwright

logger = logging.getLogger("hh_web.browser")

_STORAGE_STATE_DEFAULT = (
    Path(__file__).resolve().parent.parent / ".local" / "state" / "hh-storage-state.json"
)


def _env(name: str, default: str = "") -> str:
    return os.environ.get(name, default)


def _env_int(name: str, default: int = 0) -> int:
    v = os.environ.get(name, "")
    return int(v) if v else default


class BrowserSession:
    def __init__(self) -> None:
        self._pw: Playwright | None = None
        self._browser: Browser | None = None
        self._context: BrowserContext | None = None
        self._page: Page | None = None
        self._storage_state_path = Path(_env("HH_WEB_STORAGE_STATE", str(_STORAGE_STATE_DEFAULT)))
        self._headless = _env("HH_WEB_HEADLESS", "1") == "1"
        self._slowmo = _env_int("HH_WEB_SLOWMO_MS", 0)
        self._timeout = _env_int("HH_WEB_TIMEOUT_MS", 15000)
        self._user_agent = _env("HH_WEB_USER_AGENT", "")

    @property
    def storage_state_path(self) -> Path:
        return self._storage_state_path

    def has_storage_state(self) -> bool:
        return self._storage_state_path.exists()

    async def _ensure_playwright(self) -> Playwright:
        if self._pw is None:
            self._pw = await async_playwright().start()
        return self._pw

    async def _ensure_context(self) -> BrowserContext:
        if self._context is not None:
            return self._context
        pw = await self._ensure_playwright()
        self._browser = await pw.chromium.launch(
            headless=self._headless,
            slow_mo=self._slowmo,
        )
        launch_args: dict = {}
        if self._user_agent:
            launch_args["user_agent"] = self._user_agent
        if self.has_storage_state():
            launch_args["storage_state"] = str(self._storage_state_path)
        self._context = await self._browser.new_context(**launch_args)
        self._context.set_default_timeout(self._timeout)
        return self._context

    async def get_page(self) -> Page:
        if self._page is not None and not self._page.is_closed():
            return self._page
        ctx = await self._ensure_context()
        self._page = await ctx.new_page()
        return self._page

    async def new_page(self) -> Page:
        ctx = await self._ensure_context()
        return await ctx.new_page()

    async def save_storage_state(self) -> None:
        ctx = await self._ensure_context()
        self._storage_state_path.parent.mkdir(parents=True, exist_ok=True)
        await ctx.storage_state(path=str(self._storage_state_path))
        logger.info("Storage state saved to %s", self._storage_state_path)

    async def close(self) -> None:
        if self._page and not self._page.is_closed():
            await self._page.close()
            self._page = None
        if self._context:
            await self._context.close()
            self._context = None
        if self._browser:
            await self._browser.close()
            self._browser = None
        if self._pw:
            await self._pw.stop()
            self._pw = None

    async def __aenter__(self) -> BrowserSession:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()


_session: BrowserSession | None = None


def get_session() -> BrowserSession:
    global _session
    if _session is None:
        _session = BrowserSession()
    return _session
