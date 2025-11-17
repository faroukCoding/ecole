
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000")

        # Scroll down to ensure all cards are visible
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        await page.screenshot(path="card_colors_scrolled.png")
        await browser.close()

asyncio.run(main())
