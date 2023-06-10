from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://cn.bing.com/")
    page.get_by_role("searchbox", name="输入搜索词").click()
    page.get_by_role("searchbox", name="输入搜索词").click()
    page.get_by_role("searchbox", name="输入搜索词").fill("yu")
    page.get_by_role("option", name="语雀").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="语雀 - 用语雀，构建你的数字花园 · 语雀").click()
    page1 = page1_info.value
    page1.locator("div").filter(has_text=re.compile(r"^语雀，团队和企业的在线文档协同平台文档协作与分享 · 企业知识管理 · 产研团队协同联系我们企业/团队购买咨询使用微信扫码开始使用$")).get_by_role("link", name="开始使用").click()
