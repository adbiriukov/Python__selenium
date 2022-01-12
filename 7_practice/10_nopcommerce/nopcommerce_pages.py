from base_page import BasePage
from locators import NopcommerceLocators

from selenium.webdriver.support.ui import Select
import time


class NopcommercePages(BasePage):
    def login(self):
        # open login page
        self.find_element(NopcommerceLocators.L_HEADER_LOGIN_BT).click()
        # enter email and password
        self.find_element(NopcommerceLocators.L_LOGIN_EMAIL_FIELD).send_keys('kalter5@yandex.ru')
        self.find_element(NopcommerceLocators.L_LOGIN_PASSWORD_FIELD).send_keys('kalter5')
        # click login button and check that logout button displayed
        self.find_element(NopcommerceLocators.L_LOGIN_LOGIN_BT).click()
        self.find_element(NopcommerceLocators.L_HEADER_LOGOUT_BT).is_displayed()


class NopcommerceRegisterPage(BasePage):
    def open_register_page(self):
        # open register page
        self.find_element(NopcommerceLocators.L_HEADER_REGISTER_BT).click()

    def click_register_bt(self):
        # click register button
        self.find_element(NopcommerceLocators.L_REGISTER_REGISTER_BT).click()

    def click_register_all_error_messages_appeared(self):
        # all messages is display when click register with all fields empty
        self.find_element(NopcommerceLocators.L_REGISTER_FIRSTNAME_REQUIRED_MS).is_displayed()
        self.find_element(NopcommerceLocators.L_REGISTER_LASTNAME_REQUIRED_MS).is_displayed()
        self.find_element(NopcommerceLocators.L_REGISTER_EMAIL_REQUIRED_MS).is_displayed()
        self.find_element(NopcommerceLocators.L_REGISTER_PASSWORD_REQUIRED_MS).is_displayed()
        self.find_element(NopcommerceLocators.L_REGISTER_CONFIRM_PASSWORD_REQUIRED_MS).is_displayed()

    def select_gender(self, gender):
        # select gender
        if gender == 'Male':
            self.find_element(NopcommerceLocators.L_REGISTER_GENDER_MALE_RADIO).click()
            return True
        elif gender == "Female":
            self.find_element(NopcommerceLocators.L_REGISTER_GENDER_FEMALE_RADIO).click()
            return True
        else:
            return False

    def enter_first_name(self, firstName):
        # enter first name
        self.find_element(NopcommerceLocators.L_REGISTER_FIRSTNAME_FIELD).send_keys(firstName)

    def enter_last_name(self, lastName):
        # enter last name
        self.find_element(NopcommerceLocators.L_REGISTER_LASTNAME_FIELD).send_keys(lastName)

    def select_date_of_birth(self, date, month, year):
        # Select date
        dd_menu = self.find_element(NopcommerceLocators.L_REGISTER_DATEofBIRTHDAY_SELECT)
        ddm = Select(dd_menu)
        ddm.select_by_visible_text(date)
        # Select month
        dd_menu = self.find_element(NopcommerceLocators.L_REGISTER_MONTHofBIRTHDAY_SELECT)
        ddm = Select(dd_menu)
        ddm.select_by_visible_text(month)
        # # Select year
        dd_menu = self.find_element(NopcommerceLocators.L_REGISTER_YEARofBIRTHDAY_SELECT)
        ddm = Select(dd_menu)
        ddm.select_by_visible_text(year)

    def enter_email(self, email):
        # enter email
        self.find_element(NopcommerceLocators.L_REGISTER_EMAIL_FIELD).send_keys(email)

    def enter_company_name(self, company_name):
        # enter company name
        self.find_element(NopcommerceLocators.L_REGISTER_COMPANY_NAME_FIELD).send_keys(company_name)

    def newsletter_uncheck(self):
        # uncheck newsletter checkbox
        self.find_element(NopcommerceLocators.L_REGISTER_NEWSLETTER_CHECKBOX).click()

    def enter_password_filed(self, password):
        # enter password
        self.find_element(NopcommerceLocators.L_REGISTER_PASSWORD_FIELD).send_keys(password)

    def enter_confirm_password(self, conf_password):
        # enter conform password
        self.find_element(NopcommerceLocators.L_REGISTER_CONFIRM_PASSWORD_FIELD).send_keys(conf_password)

    def email_exist_error_appeared(self):
        # Message "The specified email already exists" appears
        self.find_element(NopcommerceLocators.L_REGISTER_EMAIL_EXIST_MS).is_displayed()









