from utils.logger import get_logger
from pages.login_page import LoginPage

logger = get_logger()

def test_successful_login(page):
    logger.info("Starting login test")

    page.goto("https://www.saucedemo.com/")

    login = LoginPage(page)
    login.login("standard_user", "secret_sauce")

    logger.info("Login successful")
    assert "inventory" in page.url