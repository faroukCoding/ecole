
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.set_viewport_size({"width": 1920, "height": 1080})

        await page.goto("http://localhost:8000")

        # Wait for the page to be fully loaded
        await page.wait_for_load_state("load")
        await page.wait_for_timeout(2000) # wait for 2 seconds

        await page.screenshot(path="card_colors_final_v2.png")
        await browser.close()

asyncio.run(main())
