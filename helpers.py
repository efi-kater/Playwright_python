from dotenv import load_dotenv
import os
from playwright.async_api import async_playwright, expect, Page


load_dotenv()
USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")

async def login(page):
    # go to base url
    await page.goto("https://www.saucedemo.com/", timeout=5000)
    await expect(page.locator(".login_logo")).to_contain_text("Swag Labs")
    await expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    await expect(page.locator("[data-test=\"password\"]")).to_be_visible()
    await expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()

    #login
    await page.locator("[data-test=\"username\"]").click()
    await page.locator("[data-test=\"username\"]").fill(USERNAME)
    await page.locator("[data-test=\"password\"]").click()
    await page.locator("[data-test=\"password\"]").fill(PASSWORD)
    await page.locator("[data-test=\"login-button\"]").click()

    #verify login
    await expect(page).to_have_url("https://www.saucedemo.com/inventory.html", timeout=5000)


