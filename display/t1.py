from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.bilibili.com/")
    page.locator("#nav-searchform div").first.click()
    page.locator("#nav-searchform div").first.click()
    page.get_by_role("textbox").fill("高考2023")
    with page.expect_popup() as page1_info:
        page.get_by_role("textbox").press("Enter")
    page1 = page1_info.value
    with page1.expect_popup() as page2_info:
        page1.get_by_role("link", name="【2023高考】“一段考后对话，但是全输出”", exact=True).click()
    page2 = page2_info.value
    with page2.expect_popup() as page3_info:
        page2.locator(".up-name").click()
    page3 = page3_info.value
    page3.locator("#navigator").get_by_role("link", name=" 合集和列表 9").click()
