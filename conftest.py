# conftest.py
import pytest
import pytest_asyncio
from playwright.async_api import async_playwright

@pytest_asyncio.fixture(scope="function")
async def page():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await browser.close()
