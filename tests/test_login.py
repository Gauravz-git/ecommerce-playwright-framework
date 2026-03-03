from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

scenarios("../features/login.feature")


@given("user is on login page")
def user_is_on_login_page(page):
    page.goto("https://www.saucedemo.com/")


@when("user enters valid credentials")
def user_enters_valid_credentials(page):
    login = LoginPage(page)
    login.login("standard_user", "secret_sauce")


@then("user should land on inventory page")
def user_should_land_on_inventory_page(page):
    assert "inventory" in page.url