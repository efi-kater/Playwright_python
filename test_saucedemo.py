import pytest
from playwright.async_api import async_playwright, expect, Page
import helpers

async def test_login_succeeds(page):
    await helpers.login(page)

    # verify inventory page
    await expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    await expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    await expect(page.locator("[data-test=\"product-sort-container\"]")).to_be_visible()

async def test_add_product_to_cart(page):
    await helpers.login(page)

    # select inventory item
    item_name = await page.locator('[data-test="inventory-item-name"]').first.text_content()
    await expect(page.locator("[data-test=\"item-4-title-link\"] [data-test=\"inventory-item-name\"]")).to_contain_text(item_name)
    await page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    await expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("1")
    await page.locator("[data-test=\"shopping-cart-link\"]").click()
    await expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text(item_name)