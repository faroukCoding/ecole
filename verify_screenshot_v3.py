import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.goto('file://' + os.path.abspath('index.html'))
        # Wait for the course area to be visible to ensure the page has loaded
        await page.wait_for_selector('.rts-course-area', timeout=10000)
        await page.screenshot(path="verification_screenshot_v3.png", full_page=True)
        await browser.close()

asyncio.run(main())
