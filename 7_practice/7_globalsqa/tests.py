from globalsqa_pages import GlobalsqaPages

import pytest
import time

# def test_globalsqa_tabs_and_iframes(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     # Open 'Add/Remove Elements' page
#     # //*[@id="post-2715"]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a
#     # //*[@id="post-2715"]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a
#     # First enter column and then row (row + 1 than actual)
#     globalsqa_automation_page.open_page_by_xpath(1, 2)
#     globalsqa_automation_page.tabs_text_is_present()


# def test_slider(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(1, 3)
#     globalsqa_automation_page.sliders()

# Tooltip
# def test_tooltip(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(1, 4)
#     globalsqa_automation_page.tooltip()

# Dialog Boxes
# def test_dialog_boxes(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(1, 6)
#     globalsqa_automation_page.dialog_boxes()

# # Progress bar
# def test_progress_bar(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.scroll_page()
#     globalsqa_automation_page.open_page_by_xpath(1, 7)
#     assert 'Complete!' == globalsqa_automation_page.progress_bar()

##
# # Dropdown menu
# def test_dropdown(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(2, 5)
#     assert 'Russian Federation' == globalsqa_automation_page.dropdown('Russian Federation')

# # Select Elements
# def test_select_elements(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.scroll_page()
#     globalsqa_automation_page.open_page_by_xpath(2, 7)
#     globalsqa_automation_page.select_elements()

# # Sortable
# def test_sorting_elements(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     time.sleep(2)
#     globalsqa_automation_page.open_page_by_xpath(3, 2)
#     globalsqa_automation_page.sorting_elements()

# def test_spiner_field(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(3, 3)
#     globalsqa_automation_page.spiner_field()
#
# def test_drag_and_drop(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(3, 6)
#     globalsqa_automation_page.drag_and_drop()

# def test_draggable_element(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.scroll_page()
#     globalsqa_automation_page.open_page_by_xpath(3, 7)
#     globalsqa_automation_page.draggable_element()

# def test_sample_page(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(4, 2)
#     globalsqa_automation_page.sample_page()
#
# def test_angularjs_multiform(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(4, 3)
#     time.sleep(3)
#     globalsqa_automation_page.angularjs_open_page_by_xpath(1, 2)
#     globalsqa_automation_page.multiform()


# def test_webtable(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(4, 3)
#     time.sleep(3)
#     globalsqa_automation_page.angularjs_open_page_by_xpath(1, 3)
#     globalsqa_automation_page.web_table()

# def test_search_filter(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(4, 3)
#     time.sleep(3)
#     globalsqa_automation_page.angularjs_open_page_by_xpath(1, 4)
#     globalsqa_automation_page.search_filter()

# def test_scrollable(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     globalsqa_automation_page.open_page_by_xpath(4, 3)
#     time.sleep(3)
#     globalsqa_automation_page.angularjs_open_page_by_xpath(2, 2)
#     globalsqa_automation_page.infinite_scroll()

# def test_registrationlogin(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     time.sleep(5)
#     globalsqa_automation_page.close_adv()
#     globalsqa_automation_page.open_page_by_xpath(4, 3)
#     time.sleep(5)
#     globalsqa_automation_page.close_adv()
#     globalsqa_automation_page.angularjs_open_page_by_xpath(2, 4)
#     # register on site
#     globalsqa_automation_page.registration_login()
#     # login and delete profile
#     globalsqa_automation_page.login_login()
#     globalsqa_automation_page.delete_login()

# def test_banking_withdraw(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     time.sleep(5)
#     globalsqa_automation_page.close_adv()
#     globalsqa_automation_page.open_page_by_xpath(4, 3)
#     time.sleep(5)
#     globalsqa_automation_page.close_adv()
#     globalsqa_automation_page.angularjs_open_page_by_xpath(3, 2)
#     globalsqa_automation_page.customer_withdraw()

# def test_banking_add_and_delete_customer(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     time.sleep(5)
#     globalsqa_automation_page.close_adv()
#     globalsqa_automation_page.open_page_by_xpath(4, 3)
#     time.sleep(5)
#     globalsqa_automation_page.close_adv()
#     globalsqa_automation_page.angularjs_open_page_by_xpath(3, 2)
#     globalsqa_automation_page.add_customer()
#     globalsqa_automation_page.delete_customer()

# def test_calculator(browser):
#     globalsqa_automation_page = GlobalsqaPages(browser)
#     globalsqa_automation_page.go_to_site()
#     time.sleep(5)
#     globalsqa_automation_page.close_adv()
#     globalsqa_automation_page.open_page_by_xpath(4, 3)
#     time.sleep(5)
#     globalsqa_automation_page.close_adv()
#     globalsqa_automation_page.angularjs_open_page_by_xpath(3, 3)
#     globalsqa_automation_page.calculator_addition()
#     globalsqa_automation_page.calculator_multiplication()

def test_consum_calculator(browser):
    globalsqa_automation_page = GlobalsqaPages(browser)
    globalsqa_automation_page.go_to_site()
    time.sleep(5)
    globalsqa_automation_page.close_adv()
    globalsqa_automation_page.open_page_by_xpath(4, 3)
    time.sleep(5)
    globalsqa_automation_page.close_adv()
    globalsqa_automation_page.angularjs_open_page_by_xpath(3, 4)
    globalsqa_automation_page.calculator_consumption()
