from base_page import BasePage
from locators import NopcommerceLocators

from selenium.webdriver.support.ui import Select
import time


class NopcommerceHeaderAndTabs(BasePage):
    def login(self):
        # open login page
        self.find_element(NopcommerceLocators.L_HEADER_LOGIN_BT).click()
        # enter email and password
        self.find_element(NopcommerceLocators.L_LOGIN_EMAIL_FIELD).send_keys('some_mail@mail.com')
        self.find_element(NopcommerceLocators.L_LOGIN_PASSWORD_FIELD).send_keys('qwerty')
        # click login button and check that logout button displayed
        self.find_element(NopcommerceLocators.L_LOGIN_LOGIN_BT).click()
        self.find_element(NopcommerceLocators.L_HEADER_LOGOUT_BT).is_displayed()

    def logout_is_displayed(self):
        # logout is displayed in the header after login
        self.find_element(NopcommerceLocators.L_HEADER_LOGOUT_BT).is_displayed()

    def go_to_default_page_by_logo(self):
        self.find_element(NopcommerceLocators.L_HEADER_LOGO_LINK).click()

    def open_register_page(self):
        # open register page
        self.find_element(NopcommerceLocators.L_HEADER_REGISTER_BT).click()

    def open_login_page(self):
        # open login page
        self.find_element(NopcommerceLocators.L_HEADER_LOGIN_BT).click()

    def open_wishlist_page(self):
        # open wishlist page
        self.find_element(NopcommerceLocators.L_HEADER_WISHLIST_BT).click()

    def open_shopping_cart_page(self):
        # open shopping cart page
        self.find_element(NopcommerceLocators.L_HEADER_SHOPPING_CART_BT).click()

    def open_computers_tab(self):
        # open computers tab
        self.find_element(NopcommerceLocators.L_TAB_COMPUTERS_BT).click()
        # return tab name
        return self.find_element(NopcommerceLocators.L_TAB_NAME_OF_CHOSEN_CATEGORY).text

    def open_electronics_tab(self):
        # open electronics tab
        self.find_element(NopcommerceLocators.L_TAB_ELECTRONICS_BT).click()
        # return tab name
        return self.find_element(NopcommerceLocators.L_TAB_NAME_OF_CHOSEN_CATEGORY).text

    def open_apparel_tab(self):
        # open apparel tab
        self.find_element(NopcommerceLocators.L_TAB_APPAREL_BT).click()
        # return tab name
        return self.find_element(NopcommerceLocators.L_TAB_NAME_OF_CHOSEN_CATEGORY).text

    def open_digital_downloads_tab(self):
        # open Digital downloads tab
        self.find_element(NopcommerceLocators.L_TAB_DIGITAL_DOWNLOADS_BT).click()
        # return tab name
        return self.find_element(NopcommerceLocators.L_TAB_NAME_OF_CHOSEN_CATEGORY).text

    def open_books_tab(self):
        # open Books tab
        self.find_element(NopcommerceLocators.L_TAB_BOOKS_BT).click()
        # return tab name
        return self.find_element(NopcommerceLocators.L_TAB_NAME_OF_CHOSEN_CATEGORY).text

    def open_jewelry_tab(self):
        # open Jewelry tab
        self.find_element(NopcommerceLocators.L_TAB_JEWELRY).click()
        # return tab name
        return self.find_element(NopcommerceLocators.L_TAB_NAME_OF_CHOSEN_CATEGORY).text

    def open_gift_cards_tab(self):
        # open Gift Cards tab
        self.find_element(NopcommerceLocators.L_TAB_GIFT_CARDS).click()
        # return tab name
        return self.find_element(NopcommerceLocators.L_TAB_NAME_OF_CHOSEN_CATEGORY).text



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












