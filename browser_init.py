from playwright.sync_api import Playwright

class BrowserIntializer:
    page =  None

    def __init__(self, playwright: Playwright) -> None:
        self.browser = playwright.firefox.launch(headless=False, slow_mo=500)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def get_page(self):
        return self.page