
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Set a larger viewport to ensure all content is visible
        await page.set_viewport_size({"width": 1920, "height": 1080})

        await page.goto("http://localhost:8000")

        # Wait for the page to be fully loaded
        await page.wait_for_load_state("networkidle")

        await page.screenshot(path="card_colors_final.png")
        await browser.close()

asyncio.run(main())
