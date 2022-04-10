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

        time.sleep(5)



        # # enter email and password
        # self.find_element(NopcommerceLocators.L_LOGIN_EMAIL_FIELD).send_keys('some_mail@mail.com')
        # self.find_element(NopcommerceLocators.L_LOGIN_PASSWORD_FIELD).send_keys('qwerty')
        # # click login button and check that logout button displayed
        # self.find_element(NopcommerceLocators.L_LOGIN_LOGIN_BT).click()
        # self.find_element(NopcommerceLocators.L_HEADER_LOGOUT_BT).is_displayed()