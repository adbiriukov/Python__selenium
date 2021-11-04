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

# def test_sorting(browser):
#     saucedemo_pages = SaucedemoPages(browser)
#     saucedemo_pages.go_to_site()
#     saucedemo_pages.login()
#     saucedemo_pages.sorting_by_price_low_to_high()

# def test_cart_number_add(browser):
#     saucedemo_pages = SaucedemoPages(browser)
#     saucedemo_pages.go_to_site()
#     saucedemo_pages.login()
#     saucedemo_pages.add_all_items_to_cart()
#     assert saucedemo_pages.number_of_items_in_cart() == '6'

# def test_cart_delete_all(browser):
#     saucedemo_pages = SaucedemoPages(browser)
#     saucedemo_pages.go_to_site()
#     saucedemo_pages.login()
#     saucedemo_pages.add_all_items_to_cart()
#     assert saucedemo_pages.number_of_items_in_cart() == '6'
#     saucedemo_pages.delete_all_items_from_cart()
#     # saucedemo_pages.refresh_page()
#     assert saucedemo_pages.number_of_items_in_cart() == ''

# def test_logout(browser):
#     saucedemo_pages = SaucedemoPages(browser)
#     saucedemo_pages.go_to_site()
#     saucedemo_pages.login()
#     time.sleep(3)
#     assert saucedemo_pages.logout() is True

# def test_cart_checkout(browser):
#     saucedemo_pages = SaucedemoPages(browser)
#     saucedemo_pages.go_to_site()
#     saucedemo_pages.login()
#     saucedemo_pages.add_all_items_to_cart()
#     assert saucedemo_pages.cart_checkout() is True

def test_footer_links_displayed(browser):
    saucedemo_pages = SaucedemoPages(browser)
    saucedemo_pages.go_to_site()
    saucedemo_pages.login()
    assert saucedemo_pages.footer_links_is_displayed() is True







