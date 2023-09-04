from playwright.async_api import Page


class BasePage:
    # def __init__(self, page: Page):
    #     self.page = page
    def __init__(self):
        self.page = None

    async def is_title_contains(self, text):
        title = await self.page.title()
        if title.find(text) == -1:
            return False
        else:
            return True

    def is_url_contains(self, text):
        if self.page.url.find(text) == -1:
            return False
        else:
            return True

    async def navigate(self, url):
        # await self.page.goto(url, timeout=5000)
        await self.page.goto(url, timeout=20000)

    def set_page(self, new_page):
        self.page = new_page
