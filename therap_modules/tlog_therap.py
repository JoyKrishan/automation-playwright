from playwright.sync_api import  Page

class TLog:
    page = None

    def __init__(self, page: Page) -> None:
        self.page = page

    def __select_individual(self, lastName):
        self.page.get_by_placeholder("Filter").fill(lastName)
        self.page.get_by_role("row").nth(1).click()

    #TODO -> fix date    
    def searchAll(self, date = None):
        self.page.get_by_role("row", name="T-Log New | Search | Archive").get_by_role("link", name="Search").click()

    def create(self, tlog_type : list, summary: str, description : str, lastName : str, notification_level = 'LOW'):
        self.page.get_by_role("row", name="T-Log New | Search | Archive").get_by_role("link", name="New").click()
        self.__select_individual(lastName)
        # tlog_type
        for typ in tlog_type:
            self.page.get_by_label(typ).check()   
        # notification level
        self.page.get_by_role("combobox", name="Notification Level").select_option(notification_level)
        # summary 
        self.page.fill('input#summary', summary)
        # description
        self.page.get_by_label("Description").fill(description)
        # submit_form
        self.page.get_by_role("button", name="Submit").click()

    
    