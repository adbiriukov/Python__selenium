from base_page import BasePage
from locators import SaucedemoLocators

from selenium.webdriver.support.ui import Select
import time

class SaucedemoPages(BasePage):
    def login(self):
        self.find_element(SaucedemoLocators.L_USERNAME_FIELD).send_keys('standard_user')
        self.find_element(SaucedemoLocators.L_PASSWORD_FIELD).send_keys('secret_sauce')
        self.find_element(SaucedemoLocators.L_LOGIN_BT).click()

    def logo_is_displayed(self):
        self.find_element(SaucedemoLocators.L_LOGO_IMG).is_displayed()

    def sorting_by_price_low_to_high(self):
        # before_sorting = self.find_elements(SaucedemoLocators.L_LIST_OF_PRODUCTS)
        time.sleep(3)
        dd_menu = self.find_element(SaucedemoLocators.L_DROPDOWN_MENU)
        ddm = Select(dd_menu)
        ddm.select_by_visible_text('Price (low to high)')
        # after_sorting = self.find_elements(SaucedemoLocators.L_LIST_OF_PRODUCTS)
        # for x in before_sorting:
        #     for y in after_sorting:
        #         if x.text == y.text:
        #             print(x.text)
        #             print('++++++++++++++')
        #             print(y.text)
        #             return False
        #         else:
        #             return True


# //*[@id="remove-sauce-labs-backpack"]
# //*[@id="add-to-cart-sauce-labs-backpack"]






















