from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

scenarios("../features/login.feature")

@given("user is on login page")
def open_login(page):
    page.goto("https://www.saucedemo.com/")

@when("user enters valid credentials")
def login(page):
    LoginPage(page).login("standard_user", "secret_sauce")

@then("user should land on inventory page")
def verify_login(page):
    assert "inventory" in page.url