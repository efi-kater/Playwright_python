import re
import asyncio
import pytest
from playwright.async_api import async_playwright, expect, Page



async def run_login_flow(headless=True):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=headless)
        context = await browser.new_context()
        page = await context.new_page()
        #go to base url
        await page.goto("https://www.saucedemo.com/", timeout=5000)
        await expect(page.locator(".login_logo")).to_contain_text("Swag Labs")
        await expect(page.locator("[data-test=\"username\"]")).to_be_visible()
        await expect(page.locator("[data-test=\"password\"]")).to_be_visible()
        await expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()

       #enter login creds
        await page.locator("[data-test=\"username\"]").click()
        await page.locator("[data-test=\"username\"]").fill("standard_user")
        await page.locator("[data-test=\"password\"]").click()
        await page.locator("[data-test=\"password\"]").fill("secret_sauce")
        await page.locator("[data-test=\"login-button\"]").click()

        #verify inventory page
        await expect(page).to_have_url("https://www.saucedemo.com/inventory.html", timeout=5000)
        await expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
        await expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
        await expect(page.locator("[data-test=\"product-sort-container\"]")).to_be_visible()

        #close browser
        await browser.close()


@pytest.mark.asyncio
async def test_login_succeeds():
    await run_login_flow(headless=True)