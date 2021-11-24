import time
from orangeHRM_pages import OrangeHRMPages


# def test_login(browser):
#     orangehrm_pages = OrangeHRMPages(browser)
#     orangehrm_pages.go_to_site()
#     orangehrm_pages.login()

# def test_reset_password(browser):
#     orangehrm_pages = OrangeHRMPages(browser)
#     orangehrm_pages.go_to_site()
#     orangehrm_pages.forgot_password()

# def test_footer_links_displayed(browser):
#     orangehrm_pages = OrangeHRMPages(browser)
#     orangehrm_pages.go_to_site()
#     orangehrm_pages.footer_links_displayed()

# def test_upper_logo_displayed(browser):
#     orangehrm_pages = OrangeHRMPages(browser)
#     orangehrm_pages.go_to_site()
#     orangehrm_pages.upper_logo_displayed()

def test_logout(browser):
    orangehrm_pages = OrangeHRMPages(browser)
    orangehrm_pages.go_to_site()
    orangehrm_pages.login()
    orangehrm_pages.main_header_notification_bell_ms_displayed()

##
# def test_logout(browser):
#     orangehrm_pages = OrangeHRMPages(browser)
#     orangehrm_pages.go_to_site()
#     orangehrm_pages.login()
#     orangehrm_pages.logout()
#     # orangehrm_pages.footer_links_displayed()



















