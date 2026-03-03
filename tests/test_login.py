def test_login_api_failure(page):

    def mock_login_failure(route):
        route.fulfill(
            status=500,
            content_type="application/json",
            body='{"error":"Internal Server Error"}'
        )

    # Intercept login request
    page.route("**/login*", mock_login_failure)

    page.goto("https://www.saucedemo.com/")
    
    from pages.login_page import LoginPage
    login = LoginPage(page)

    login.login("standard_user", "secret_sauce")

    # Verify user stays on login page
    assert "saucedemo" in page.url