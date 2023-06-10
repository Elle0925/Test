from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.bilibili.com/")
    page.get_by_placeholder("高考分数线预测").click()
    page.get_by_placeholder("高考分数线预测").click()
    page.get_by_placeholder("高考分数线预测").click()
    page.get_by_placeholder("高考分数线预测").fill("高考2023")
    with page.expect_popup() as page1_info:
        page.get_by_placeholder("高考分数线预测").press("Enter")
    page1 = page1_info.value
