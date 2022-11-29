from playwright.sync_api import Playwright, sync_playwright, expect, Page

class Dashboard:

    def __init__(self) -> None:
        pass

    @staticmethod
    def skip_personal_details(page: Page):
        page.click("input[name='_action_cancel']")
        page.wait_for_load_state()

    @staticmethod
    def agree_signup(page: Page):
        if page.locator("input[name='_action_agree']").count() < 1:
            return 
        page.click("input[name='_action_agree']")
        page.wait_for_load_state()
        Dashboard.agree_signup(page)

    @staticmethod
    def goto(page: Page):
        page.click('a[href="/ma/newfpage/switchFirstPage"]')
    
    @staticmethod
    def click_on_individual_tab(page : Page):
        page.click('a[href="/ma/newfpage/switchFirstPage?fpmode=individual"]')