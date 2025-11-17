from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000")

        # Take a screenshot of the "Blog et actualités" section
        blog_section_selector = ".rts-blog-area"
        page.wait_for_selector(blog_section_selector)
        blog_section = page.query_selector(blog_section_selector)
        if blog_section:
            blog_section.screenshot(path="verifications/blog_actualites_screenshot.png")

        browser.close()

if __name__ == "__main__":
    run()
