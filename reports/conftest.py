import pytest
from core.driver_factory import DriverFactory

@pytest.fixture(scope="function")
def page():
    factory = DriverFactory(browser="chromium", headless=False)
    page, browser, playwright = factory.launch_browser()
    yield page
    browser.close()
    playwright.stop()