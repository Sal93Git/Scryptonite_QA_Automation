from playwright.async_api import Page, async_playwright
import asyncio
from features.Actions.BasePage import BasePage
from features.Page_Objects import samplePageObjects
from features.Page_Objects.samplePageObjects import SampleElements
import time


class LoginPage(BasePage):
    # def __init__(self,  page: Page):
        # super().__init__(page)
    def __init__(self):
        super().__init__()
        # self.username = page.locator("[id='name']")
        # self.password = page.locator("[id='password']")
        # self.submit = page.get_by_role('button', name='Submit')
        # self.reset_password = page.get_by_role('button', name='Forgot Password')
        self.loop = asyncio.get_event_loop()

    # async def fill_username(self, text):
    #     await self.username.fill(text)

    async def open_login_url_action(self):
        await self.navigate("https://www.ebgames.com.au/")  # Call the navigate method with await
        print(f"Pausing execution for {3} seconds...")
        time.sleep(3)
        print("Delay complete.")
        await self.page.click(SampleElements.EB_SITE_MENU)
        await self.page.click(SampleElements.EB_PLAYSTATION_SELECT)
        await self.page.click(SampleElements.EB_VIDEO_GAMES)
        time.sleep(3)


