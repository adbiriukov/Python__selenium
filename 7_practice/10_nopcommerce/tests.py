from nopcommerce_pages import NopcommercePages
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

# Login
def test_login(browser):
    np = NopcommercePages(browser)
    np.go_to_site()
    np.login()
    time.sleep(5)

























