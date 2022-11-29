from playwright.sync_api import  Page


class Login:
    page = None

    def __init__(self, page: Page) -> None:
        self.page = page

    def get_page(self):
        return self.page      
    
    def with_input_credentials(self, **kwargs):
        for id, value in kwargs.items():
            self.page.fill(f"input#{id}", value)
    
    def with_click_submit(self, id):
        self.page.click(f"input#{id}")
