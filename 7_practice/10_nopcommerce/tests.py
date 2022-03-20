from nopcommerce_pages import NopcommerceHeaderAndTabs
from nopcommerce_pages import NopcommerceRegisterPage
import time

# # Register: After clicking register with all fields empty all error messages are displayed
# def test_register_all_error_messages_displayed(browser):
#     np = NopcommerceRegisterPage(browser)
#     np.go_to_site()
#     np.open_register_page()
#     np.click_register_bt()
#     # all error messages is appeared
#     np.click_register_all_error_messages_appeared()

# # Register: Message "The specified email already exists" appears, when try use same email for registration
# def test_user_already_exist_message(browser):
#     np = NopcommerceRegisterPage(browser)
#     np.go_to_site()
#     np.open_register_page()
#     # Select gender: 'Male' or 'Female'
#     gender = np.select_gender('Male')
#     assert gender is True
#     # Enter first name and last name
#     np.enter_first_name('First_Name')
#     np.enter_last_name('Last_name')
#     # # Select date of birth: provide (Date, Month, Year), (Example: ('23', 'May', '1993'))
#     # np.select_date_of_birth('23', 'May', '1993')
#     # Enter email
#     np.enter_email('some_mail@mail.com')
#     # Enter company name
#     np.enter_company_name('Company name')
#     # Uncheck news letter option
#     np.newsletter_uncheck()
#     # enter password and confirm password
#     np.enter_password_filed('qwerty')
#     np.enter_confirm_password('qwerty')
#     # Click register button
#     np.click_register_bt()
#     # Message "The specified email already exists" appears
#     np.email_exist_error_appeared()

# # User can login with correct login and password
# def test_login(browser):
#     np = NopcommerceHeaderAndTabs(browser)
#     np.go_to_site()
#     np.login()
#     time.sleep(5)
#     np.logout_is_displayed()

# # Unauthorized user can open all links in header from main page
# def test_unauthorized_user_can_open_all_links_in_header(browser):
#     np = NopcommerceHeaderAndTabs(browser)
#     np.go_to_site()
#     # open register page
#     np.open_register_page()
#     np.go_to_default_page_by_logo()
#     # open login page
#     np.open_login_page()
#     np.go_to_default_page_by_logo()
#     # open wishlist page
#     np.open_wishlist_page()
#     np.go_to_default_page_by_logo()
#     # open shopping cart page
#     np.open_shopping_cart_page()
#     np.go_to_default_page_by_logo()

# Unauthorized user can open all tabs from main page
def test_unauthorized_user_can_open_all_tabs(browser):
    np = NopcommerceHeaderAndTabs(browser)
    np.go_to_site()
    # Open all tabs, and make sure that name of category is displayed
    assert np.open_computers_tab() == 'Computers'
    assert np.open_electronics_tab() == 'Electronics'
    assert np.open_apparel_tab() == 'Apparel'
    assert np.open_digital_downloads_tab() == 'Digital downloads'
    assert np.open_books_tab() == 'Books'
    assert np.open_jewelry_tab() == 'Jewelry'
    assert np.open_gift_cards_tab() == 'Gift Cards'

















