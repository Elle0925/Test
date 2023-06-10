from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.bing.com/")
    page.get_by_placeholder("搜索网页").click()
    page.get_by_placeholder("搜索网页").fill("playwright")
    page.get_by_placeholder("搜索网页").click()
    page.get_by_placeholder("搜索网页").press("Enter")
    page.get_by_role("link", name="Playwright - End-to-end testing for web apps").click()
    page.get_by_role("link", name="Get started").click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
