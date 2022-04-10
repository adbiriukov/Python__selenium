from opencart_pages import OpencartHeaderAndTabs
import time

# Register: After clicking register with all fields empty all error messages are displayed
def test_register_all_error_messages_displayed(browser):
    np = OpencartHeaderAndTabs(browser)
    # get number of all users before registration
    number_of_users = np.get_number_of_register_users()
    np.go_to_site()
    np.register()
    # get number of all users after registration
    number_of_users_after_reg = np.get_number_of_register_users()
    assert number_of_users+1 == number_of_users_after_reg
    print(number_of_users)
    np.sql_delete_test_user()
    number_of_users = np.get_number_of_register_users()
    print(number_of_users)


    # np.open_register_page()
    # np.click_register_bt()
    # # all error messages is appeared
    # np.click_register_all_error_messages_appeared()