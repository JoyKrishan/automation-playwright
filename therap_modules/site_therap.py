from playwright.sync_api import  Page

class Site:
    site_name = None
    page = None

    def __init__(self, page :Page) -> None:
        self.page = page
        self.page.click("a[href='/ma/admin2/site']")

    def fill_input(self,**kwargs):
        for id, value in kwargs.items():
            if id == "name":
                self.site_name = value
            self.page.fill(f"input#{id}", value)

    def fill_selectors(self, **kwargs):
        for id, value in kwargs.items():
            if id == 'state' or id == 'country':
                id = f'address.{id}'
            self.page.select_option(f'select[name="{id}"]',value)

    def save(self):                
        self.page.click("input[type='submit']")
        self.page.wait_for_load_state()
        self.page.click("button.btn-prompt-yes")
    
    def get_site_name(self):
        return self.site_name