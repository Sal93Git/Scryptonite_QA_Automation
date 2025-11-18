import sys
import time
import json
import playwright
from playwright._impl._playwright import Playwright
from playwright.sync_api import sync_playwright
from behave import fixture, use_fixture
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright
from testCaseData import TestCaseData
import os
# import newRelicEventLogging
import configparser

from features.Page_Actions.BasePage import BasePage
from features.Page_Actions.TestPage import LoginPage


# List of page object classes to initialize
# Add other page classes to the list
page_classes = [LoginPage, BasePage]


@async_run_until_complete
async def before_all(context):
    env_file_path = context.config.userdata.get("env_file", os.environ.get("DEFAULT_ENV_FILE"))
    # Read the environment properties file
    properties = {}
    with open(env_file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=",1)
                properties[key.strip()] = value.strip()
    # Save the properties into context for reuse in steps
    context.env_properties = properties

    # Start a new Chrome browser and add it to context
    p = await async_playwright().start()
    context.browser = await p.chromium.launch(headless=True, slow_mo=1000, channel="chrome", args=['--incognito'])
    context.browserContext = await context.browser.new_context(ignore_https_errors=True)
    print("Browser Started!")
    context.test_data = TestCaseData()
    # Initialize page object instances using a loop and add them to the dictionary
    context.page_objects = {}
    for page_class in page_classes:
        page_name = page_class.__name__
        context.page_objects[page_name] = page_class()


@fixture
async def browser_chrome_page(context):
    # create new page
    context.page = await context.browserContext.new_page()
    
    # # Initialize page object instances using a loop
    for page_name, page_instance in context.page_objects.items():
        # Call a common function on each page object
        page_instance.set_page(context.page)
        page_instance.set_context(context)
    return context.page


@async_run_until_complete
async def before_scenario(context, scenario):
    await use_fixture(browser_chrome_page, context)
    # Set any initial data if needed
    # context.test_data.set('key', 'value')
    print("Starting Scenario : " + str(scenario))


@async_run_until_complete
async def after_all(context):
    # Close the browser at the end
    print("End of Regression Run")
    await context.browser.close()


@fixture
async def take_screenshot(context, scenario):
    if scenario.status=="failed":
        screenshot_path = os.path.join("../","SCRYPTONITE_QA","screenshots", f"{scenario.name}_failure.png")
        await context.page.screenshot(path=screenshot_path)

@fixture
async def log_to_newRelic(context, scenario):
    print("Attempting to log event to NewRelic")
    failed_step = "N/A"
    if scenario.status=="failed":
        for step in scenario.steps:
            if step.status == "failed":
                failed_step = str(step.name)

    # newRelicEventLogging.create_new_relic_event(scenario.name, scenario.status, failed_step)


@async_run_until_complete
async def after_scenario(context, scenario):
    # await context.session.tracing.stop(path="trace.zip")
    await use_fixture(take_screenshot, context, scenario)
    await use_fixture(log_to_newRelic, context, scenario)
    await context.page.close()
    # await context.session.close()
    # del context.test_data
    print("Ending Scenario: " + str(scenario))
    # Add a delay if needed for the screenshot to be captured before closing the browser
    time.sleep(3)