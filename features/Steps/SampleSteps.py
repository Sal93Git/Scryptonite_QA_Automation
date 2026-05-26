from behave import *
import time

# import config
from features.Page_Actions.BasePage import BasePage
from features.Page_Actions.TestPage import LoginPage
from behave.api.async_step import async_run_until_complete
# from config import *
import asyncio

@Given('i go to eb')
@async_run_until_complete
async def open_login_url(context):
    # login_page = LoginPage(context.page)
    # await login_page.open_login_url_action()
    # await context.loginpage.open_login_url_action()
    await context.page_objects['LoginPage'].open_login_url_action()


@Given('i go to go to URL')
@async_run_until_complete
async def open_login_url(context):
    context.test_data.set('site', 'https://www.apple.com/au/')
    # await base_page.navigate(context.test_data.get('site'))
    await context.page_objects['BasePage'].navigate(context.test_data.get('site'))
    context.test_data.set('site2', 'https://evercoreheroes.com/')
    await context.page_objects['LoginPage'].navigate(context.test_data.get('site2'))
    await context.page_objects['BasePage'].navigate('https://magic.wizards.com/en')


@Then('i go to youtube')
@async_run_until_complete
async def step_impl2(context):
    await context.page_objects['LoginPage'].navigate("https://www.youtube.com/")  # Call the navigate method with await
    print(f"Pausing execution for {3} seconds...")
    time.sleep(3)
    print("Delay complete.")
    # Trial
    context.test_data.settrial('https://www.udemy.com/')
    trial_value = context.test_data.trial()
    print("Trial value:", trial_value)
    await context.page_objects['LoginPage'].navigate(trial_value)
    print(f"Pausing execution for {3} seconds...")
    time.sleep(3)
    context.test_data.set('subaru site', 'https://www.subaru.com.au/')
    trial_value2 = context.test_data.get('subaru site')
    await context.page_objects['LoginPage'].navigate(trial_value2)


@Then('i test properties')
@async_run_until_complete
async def config_test(context):
    app_url1 = context.env_properties.get('app_url')
    # app_url1 = config.get_app_url(context.config.userdata.get("env_file", os.environ.get("DEFAULT_ENV_FILE")))
    # Use app_url in your step implementation
    await context.page_objects['LoginPage'].navigate(app_url1)

# @Then("web test")
# def webrun(playwright: Playwright) -> None:
#     with sync_playwright() as playwright:
#      browser = playwright.chromium.launch(headless=False)
#      context = browser.new_context()
#     # Open new page
#      page = context.new_page()
#     # Go to https://www.wikipedia.org/
#      page.goto("https://www.wikipedia.org/")
#     # Click input[name="search"]
#      page.locator("input[name=\"search\"]").click()
#     # Fill input[name="search"]
#      page.locator("input[name=\"search\"]").fill("lancia")
#     # Click text=LanciaAutomobile brand manufacturing subsidiary of Stellantis >> em
#      page.locator("text=LanciaAutomobile brand manufacturing subsidiary of Stellantis >> em").click()
#      page.wait_for_url("https://en.wikipedia.org/wiki/Lancia")
#     # ---------------------
#      context.close()
#      browser.close()
#      print('end of web test')

