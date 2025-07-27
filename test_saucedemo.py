import re
import asyncio
import pytest
from playwright.async_api import async_playwright, expect, Page
import helpers
from helpers import login
import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")


@pytest.mark.asyncio
async def test_login_succeeds(page):
    await helpers.login(page)

    # verify inventory page
    await expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    await expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    await expect(page.locator("[data-test=\"product-sort-container\"]")).to_be_visible()