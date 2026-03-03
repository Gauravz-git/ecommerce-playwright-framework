import pytest
from core.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chromium")
    parser.addoption("--headed", action="store_true")
    parser.addoption("--slow", action="store", default=0)


@pytest.fixture(scope="function")
def page(request):
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")
    slow = int(request.config.getoption("--slow"))

    driver = DriverFactory(
        browser=browser,
        headless=not headed,
        slow_mo=slow
    )

    page = driver.launch_browser()
    yield page
    driver.quit_browser()