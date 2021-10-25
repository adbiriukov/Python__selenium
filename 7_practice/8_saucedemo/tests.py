import time

from saucedemo_pages import SaucedemoPages


# def test_open_main_page_logo_is_displayed(browser):
#     saucedemo_pages = SaucedemoPages(browser)
#     saucedemo_pages.go_to_site()
#     saucedemo_pages.logo_is_displayed()
#
# def test_login(browser):
#     saucedemo_pages = SaucedemoPages(browser)
#     saucedemo_pages.go_to_site()
#     saucedemo_pages.login()

def test_sorting(browser):
    saucedemo_pages = SaucedemoPages(browser)
    saucedemo_pages.go_to_site()
    saucedemo_pages.login()
    saucedemo_pages.sorting_by_price_low_to_high()





