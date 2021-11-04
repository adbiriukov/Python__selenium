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

    def add_all_items_to_cart(self):
        self.find_element(SaucedemoLocators.L_BACKPACK_ADD).click()
        self.find_element(SaucedemoLocators.L_BIKE_LIGHT_ADD).click()
        self.find_element(SaucedemoLocators.L_TSHIRT_ADD).click()
        self.find_element(SaucedemoLocators.L_JACKET_ADD).click()
        self.find_element(SaucedemoLocators.L_ONESIE_ADD).click()
        self.find_element(SaucedemoLocators.L_RED_TSHIRT_ADD).click()

    def number_of_items_in_cart(self):
        try:
            cart_number = self.find_element(SaucedemoLocators.L_IN_CART_NUMBER)
            return cart_number.text
        except:
            return ''

    def delete_all_items_from_cart(self):
        self.find_element(SaucedemoLocators.L_BACKPACK_REMOVE).click()
        self.find_element(SaucedemoLocators.L_BIKE_LIGHT_REMOVE).click()
        self.find_element(SaucedemoLocators.L_TSHIRT_REMOVE).click()
        self.find_element(SaucedemoLocators.L_JACKET_REMOVE).click()
        self.find_element(SaucedemoLocators.L_ONESIE_REMOVE).click()
        self.find_element(SaucedemoLocators.L_RED_TSHIRT_REMOVE).click()

    def reset_app_state(self):
        self.find_element(SaucedemoLocators.L_MENU_IN_LEFT_UP_CORNER).click()
        self.find_element(SaucedemoLocators.L_MENU_RC_RESET_APP).click()

    def logout(self):
        self.find_element(SaucedemoLocators.L_MENU_IN_LEFT_UP_CORNER).click()
        # 1 sec wait because straight throws 'element not interactable'
        time.sleep(1)
        self.find_element(SaucedemoLocators.L_MENU_RC_LOGOUT).click()
        return self.find_element(SaucedemoLocators.L_LOGIN_BT).is_displayed()

    def cart_checkout(self):
        self.find_element(SaucedemoLocators.L_CART).click()
        self.find_element(SaucedemoLocators.L_CHECKOUT).click()
        self.find_element(SaucedemoLocators.L_FIRST_NAME_F).send_keys('FirstName')
        self.find_element(SaucedemoLocators.L_LAST_NAME_F).send_keys('LastName')
        self.find_element(SaucedemoLocators.L_POSTALCODE).send_keys('123456')
        self.find_element(SaucedemoLocators.L_CHECKOUT_CONTINUE_BT).click()
        self.find_element(SaucedemoLocators.L_CHECKOUT_FINISH).click()
        return self.find_element(SaucedemoLocators.L_CHECKOUT_FINISH_TEXT).is_displayed()

    def footer_links_is_displayed(self):
        tw = self.find_element(SaucedemoLocators.L_FOOTER_TW_LINK).is_displayed()
        fb = self.find_element(SaucedemoLocators.L_FOOTER_FB_LINK).is_displayed()
        td = self.find_element(SaucedemoLocators.L_FOOTER_LD_LINK).is_displayed()
        if tw and fb and td is True:
            return True
        else:
            return False
