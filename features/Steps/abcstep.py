from behave import Given, When, Then
from playwright._impl._playwright import Playwright
from playwright.sync_api import sync_playwright

from features.Actions._incrementor import incrementor


@Given("a new incrementor of size {stride}")
def given_incrementor(context, stride: str):
    context.incrementor = incrementor(int(stride))


@When("we increment {num}")
def when_increment(context, num: str):
    context.results = context.incrementor(int(num))


@Then("we should see {results}")
def then_resuults(context, results: str):
    assert (context.results == int(results))


@Then("web test")
def webrun(playwright: Playwright) -> None:
    with sync_playwright() as playwright:
     browser = playwright.chromium.launch(headless=False)
     context = browser.new_context()
    # Open new page
     page = context.new_page()
    # Go to https://www.wikipedia.org/
     page.goto("https://www.wikipedia.org/")
    # Click input[name="search"]
     page.locator("input[name=\"search\"]").click()
    # Fill input[name="search"]
     page.locator("input[name=\"search\"]").fill("lancia")
    # Click text=LanciaAutomobile brand manufacturing subsidiary of Stellantis >> em
     page.locator("text=LanciaAutomobile brand manufacturing subsidiary of Stellantis >> em").click()
     page.wait_for_url("https://en.wikipedia.org/wiki/Lancia")
    # ---------------------
     context.close()
     browser.close()
     print('end of web test')
