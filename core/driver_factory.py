from playwright.sync_api import sync_playwright


class DriverFactory:
    def __init__(self, browser="chromium", headless=False, slow_mo=0):
        self.browser_name = browser
        self.headless = headless
        self.slow_mo = slow_mo
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def launch_browser(self):
        self.playwright = sync_playwright().start()

        browser_type = getattr(self.playwright, self.browser_name)

        self.browser = browser_type.launch(
            headless=self.headless,
            slow_mo=self.slow_mo
        )

        self.context = self.browser.new_context(
            record_video_dir="reports/videos/"
        )

        self.page = self.context.new_page()

        return self.page

    def quit_browser(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()