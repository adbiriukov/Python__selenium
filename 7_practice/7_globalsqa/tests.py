from globalsqa_pages import GlobalsqaPages
import pytest
import time

def test_hero_add_remove_elements(browser):
    globalsqa_automation_page = GlobalsqaPages(browser)
    globalsqa_automation_page.go_to_site()
    # Open 'Add/Remove Elements' page
    # //*[@id="post-2715"]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a
    # //*[@id="post-2715"]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a
    # First enter column and then row (row + 1 than actual)
    globalsqa_automation_page.open_page_by_xpath(1, 2)
    globalsqa_automation_page.tabs_text_is_present()
