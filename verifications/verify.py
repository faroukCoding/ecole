
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Construct the absolute file path
        html_file = os.path.abspath('index.html')

        # Load the local HTML file
        await page.goto(f'file://{html_file}')

        # Wait for the page to load completely
        await page.wait_for_load_state('networkidle')

        # Take a screenshot
        screenshot_path = 'verifications/screenshot.png'
        await page.screenshot(path=screenshot_path)

        print(f"Screenshot saved to {screenshot_path}")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
