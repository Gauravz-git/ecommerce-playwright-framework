from playwright.sync_api import sync_playwright

class DriverFactory:
    def __init__(self, browser="chromium", headless=False):
        self.browser_name = browser
        self.headless = headless

    def launch_browser(self):
        self.playwright = sync_playwright().start()
        browser = getattr(self.playwright, self.browser_name).launch(headless=self.headless)
        context = browser.new_context()
        page = context.new_page()
        return page, browser, self.playwright