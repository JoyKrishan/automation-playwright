from playwright.sync_api import sync_playwright
from therap_modules.dashboard import Dashboard
from therap_modules.site_therap import Site
from therap_modules.program_therap import Program
from therap_modules.tlog_therap import TLog
from therap_modules.login_therap import Login
from browser_init import BrowserIntializer
from csv_reader_therap import LOGIN_SHEET, ExcelValueGetter, SITE_SHEET, PROGRAM_SHEET, TLOG_SHEET

URL = 'https://qa01.therapbd.net/'

with sync_playwright() as playwright:
    page1 = BrowserIntializer(playwright).get_page()
    page1.goto(URL)

    login = Login(page1)
    login_values = ExcelValueGetter(LOGIN_SHEET)
    login.with_input_credentials(loginName=login_values.get_first_value_wrt_col('loginName'), password=login_values.get_first_value_wrt_col(
        'password'), providerCode=login_values.get_first_value_wrt_col('providerCode'))
    login.with_click_submit("submitButton")

    # Agree Sign Up Agreements
    Dashboard.agree_signup(page1)

    # Skip Personal details
    Dashboard.skip_personal_details(page1)

    # site_values = ExcelValueGetter(SITE_SHEET)
    # for row in range(site_values.get_total_rows()):  # 1
    #     # Create a Site
    #     site1 = Site(page1)
    #     site1.fill_input(name=site_values.get_value_wrt_col_row('name', row))
    #     site1.fill_selectors(tz=site_values.get_value_wrt_col_row(
    #         'timezone', row), state=site_values.get_value_wrt_col_row('state', row))
    #     site1.save()
    #     Dashboard.goto(page1)

    program_values = ExcelValueGetter(PROGRAM_SHEET)
    for row in range(program_values.get_total_rows()):
        # Create a Program
        program1 = Program(page1)
        program1.fill_input(name = program_values.get_value_wrt_col_row(
            'name', row), rdid = program_values.get_value_wrt_col_row('programID', row))
        program1.fill_selectors(
            programType='15 min. units', site=program_values.get_value_wrt_col_row('site', row))
        program1.save()
        Dashboard.goto(page1)

    Dashboard.click_on_individual_tab(page1)

    tlog_values = ExcelValueGetter(TLOG_SHEET)
    for row in range(tlog_values.get_total_rows()):
        # Create a T-Log
        tlog1 = TLog(page1)
        tlog1.create(tlog_type=tlog_values.get_value_wrt_col_row('T-log type', row).split(","), lastName=tlog_values.get_value_wrt_col_row(
            'Individual search name', row), summary=tlog_values.get_value_wrt_col_row("Summary", row), description=tlog_values.get_value_wrt_col_row("Description", row))
        
    