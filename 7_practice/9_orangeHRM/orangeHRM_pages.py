from base_page import BasePage
from locators import OrangeHRMLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time


class OrangeHRMPages(BasePage):
    def login(self):
        self.find_element(OrangeHRMLocators.L_LOGIN_FIELD).send_keys('Admin')
        self.find_element(OrangeHRMLocators.L_PASSWORD_FIELD).send_keys('admin123')
        self.find_element(OrangeHRMLocators.L_LOGIN_BT).click()
        time.sleep(30)

    def logout(self):
        action = ActionChains(self.driver)
        # click welcome message
        welcome_ms = self.find_element(OrangeHRMLocators.L_HEADER_WELCOME_MS)
        welcome_ms.click()
        # click logout
        # logout_bt = self.find_element(OrangeHRMLocators.L_HEADER_WELCOME_LOGOUT)
        # logout_bt.click()
        # action.move_to_element(welcome_ms).click().perform()
        # action.move_to_element(logout_bt).click().perform()
        # time.sleep(3)

    def forgot_password(self):
        self.find_element(OrangeHRMLocators.L_FORGOT_PASS_LINK).click()
        self.find_element(OrangeHRMLocators.L_FORGOT_PASS_USERNAME_F).send_keys('Admin123')
        self.find_element(OrangeHRMLocators.L_FORGOT_PASS_RESET_BT).click()
        self.find_element(OrangeHRMLocators.L_FORGOT_PASS_MESSAGE_BT).is_displayed()

    def footer_links_displayed(self):
        self.find_element(OrangeHRMLocators.L_FOOTER_LINK_LD).is_displayed()
        self.find_element(OrangeHRMLocators.L_FOOTER_LINK_FB).is_displayed()
        self.find_element(OrangeHRMLocators.L_FOOTER_LINK_TW).is_displayed()
        self.find_element(OrangeHRMLocators.L_FOOTER_LINK_YT).is_displayed()

    def upper_logo_displayed(self):
        self.find_element(OrangeHRMLocators.L_UPPER_LOGO).is_displayed()

    def main_header_notification_bell_ms_displayed(self):
        self.find_element(OrangeHRMLocators.L_HEADER_NOTIFICATION_BELL).click()
        self.find_element(OrangeHRMLocators.L_HEADER_NOTIFICATION_BELL_MS).is_displayed()




