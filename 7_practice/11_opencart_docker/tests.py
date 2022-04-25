from opencart_pages import OpencartHeaderAndTabs
import time

# # Register: After clicking register with all fields empty all error messages are displayed
# def test_register_all_error_messages_displayed(browser):
#     oc = OpencartHeaderAndTabs(browser)
#     oc.go_to_site()
#     oc.open_register_page()
#     oc.register_page_all_warnings_displayed()

# # Register and then delete the user through sql
# def test_register(browser):
#     oc = OpencartHeaderAndTabs(browser)
#     # get number of all users before registration
#     number_of_users = oc.get_number_of_register_users()
#     oc.go_to_site()
#     oc.register()
#     # get number of all users after registration
#     number_of_users_after_reg = oc.get_number_of_register_users()
#     assert number_of_users+1 == number_of_users_after_reg
#     print(number_of_users)
#     oc.sql_delete_test_user()
#     number_of_users = oc.get_number_of_register_users()
#     print(number_of_users)

# def test_cart_empty_message_displayed(browser):
#     oc = OpencartHeaderAndTabs(browser)
#     oc.go_to_site()
#     oc.click_shopping_cart_link()
#     oc.shopping_cart_is_empty_message()

def test_compare_two_products(browser):
    oc = OpencartHeaderAndTabs(browser)
    oc.go_to_site()
    oc.open_cameras_tab()
    oc.compare_two_first_products()
    time.sleep(3)
    oc.open_compare_page_ms()
    assert oc.find_number_of_products_present() == 2
