from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000")
        element = page.locator('.rts-course-area.style-2')
        screenshot_path = 'verifications/cours_populaires_screenshot.png'
        element.screenshot(path=screenshot_path)
        browser.close()

run()
