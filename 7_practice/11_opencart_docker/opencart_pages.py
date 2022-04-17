from base_page import BasePage
from locators import OpencartLocators
import pymysql

from selenium.webdriver.support.ui import Select
import time


class OpencartHeaderAndTabs(BasePage):
    def get_number_of_register_users(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='bn_opencart', password='', db='bitnami_opencart')
        cursor = conn.cursor()
        cursor.execute('select * from oc_customer')
        table = cursor.fetchall()
        conn.close()
        return len(table)

    def sql_delete_test_user(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='bn_opencart', password='', db='bitnami_opencart')
        cursor = conn.cursor()
        cursor.execute('delete from oc_customer where email="some_mail@mail.com";')
        conn.close()

    def register(self):
        # open register page
        self.find_element(OpencartLocators.L_HEADER_MY_ACCOUNT_DROPDOWN).click()
        self.find_element(OpencartLocators.L_HEADER_REGISTER_BT).click()

        self.find_element(OpencartLocators.L_REGISTER_FNAME).send_keys('test_fname')
        self.find_element(OpencartLocators.L_REGISTER_LNAME).send_keys('test_lname')
        self.find_element(OpencartLocators.L_REGISTER_EMAIL).send_keys('some_mail@mail.com')
        self.find_element(OpencartLocators.L_REGISTER_TELEPHONE).send_keys('999999999')

        self.find_element(OpencartLocators.L_REGISTER_PASSWORD).send_keys('qwerty')
        self.find_element(OpencartLocators.L_REGISTER_CONF_PASSWORD).send_keys('qwerty')
        self.find_element(OpencartLocators.L_REGISTER_RADIO_SUBSCRIBE_TO_NEWSLETTER).click()
        self.find_element(OpencartLocators.L_REGISTER_CONF_POLICY).click()
        self.find_element(OpencartLocators.L_REGISTER_CONTINUE_BT).click()

    def open_register_page(self):
        # open register page
        self.find_element(OpencartLocators.L_HEADER_MY_ACCOUNT_DROPDOWN).click()
        self.find_element(OpencartLocators.L_HEADER_REGISTER_BT).click()

    def register_page_all_warnings_displayed(self):
        self.find_element(OpencartLocators.L_REGISTER_CONTINUE_BT).click()
        assert self.find_element(OpencartLocators.L_REGISTER_POLICY_WARNING).text == \
               'Warning: You must agree to the Privacy Policy!'
        assert self.find_element(OpencartLocators.L_REGISTER_FNAME_WARNING).text == \
               'First Name must be between 1 and 32 characters!'
        assert self.find_element(OpencartLocators.L_REGISTER_LNAME_WARNING).text == \
               'Last Name must be between 1 and 32 characters!'
        assert self.find_element(OpencartLocators.L_REGISTER_EMAIL_WARNING).text == \
               'E-Mail Address does not appear to be valid!'
        assert self.find_element(OpencartLocators.L_REGISTER_TELEPHONE_WARNING).text == \
               'Telephone must be between 3 and 32 characters!'
        assert self.find_element(OpencartLocators.L_REGISTER_PASSWORD_WARNING).text == \
               'Password must be between 4 and 20 characters!'


    def click_shopping_cart_link(self):
        self.find_element(OpencartLocators.L_HEADER_SHOPPING_CART_LINK).click()

    def shopping_cart_is_empty_message(self):
        assert self.find_element(OpencartLocators.L_SHOPPING_CART_CART_IS_EMPTY).text == 'Your shopping cart is empty!'

