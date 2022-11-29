from playwright.sync_api import  Page

class Program:
    page = None

    def __init__(self, page: Page) -> None:
        self.page = page
        self.page.click('a[href="/ma/admin2/program"]')

    def fill_input(self, **kwargs):
        for id, value in kwargs.items():
            self.page.fill(f"input#{id}", value)

    def fill_selectors(self, **kwargs):
        self.page.select_option('select#programType', label=kwargs['programType'])
        self.page.select_option('select#site', label=kwargs['site'])

    def save(self):                
        self.page.click("input[type='submit']")
        self.page.wait_for_load_state()