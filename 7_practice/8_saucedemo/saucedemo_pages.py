from base_page import BasePage
from locators import SaucedemoLocators

import time

class SaucedemoPages(BasePage):
    def login(self):
        self.find_element(SaucedemoLocators.L_USERNAME_FIELD).send_keys('standard_user')
        self.find_element(SaucedemoLocators.L_PASSWORD_FIELD).send_keys('secret_sauce')
        self.find_element(SaucedemoLocators.L_LOGIN_BT).click()
        time.sleep(5)


    def logo_is_displayed(self):
        self.find_element(SaucedemoLocators.L_LOGO_IMG).is_displayed()