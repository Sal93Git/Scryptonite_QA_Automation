from behave import *
import time
from behave.api.async_step import async_run_until_complete
import asyncio


@Given('i go to url "{url}"')
@async_run_until_complete
async def go_to_url(context, url):
    await context.page_objects['BasePage'].navigate(url)
    # await context.page_objects['BasePage'].is_title_contains("google")
    time.sleep(3)