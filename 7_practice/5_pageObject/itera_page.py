from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Itera_page_locators:
    # text fields
    LOCATOR_NAME_FIELD = (By.ID, 'name')
    LOCATOR_PHONE_FIELD = (By.ID, 'phone')
    LOCATOR_EMAIL_FIELD = (By.ID, 'email')
    LOCATOR_PASSW0RD_FIELD = (By.ID, 'password')
    LOCATOR_ADDRESS_FIELD = (By.ID, 'address')

    # checkboxes and radio buttons ID
    # LOCATOR_RADIO_FEMALE = (By.ID, 'female')
    # LOCATOR_RADIO_MALE = (By.ID, 'male')
    # LOCATOR_CHECKBOX_MONDAY = (By.ID, 'monday')
    # LOCATOR_CHECKBOX_WEDNESDAY = (By.ID, 'wednesday')
    # LOCATOR_CHECKBOX_FRIDAY = (By.ID, 'friday')

    #
    # LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    # LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    # LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")

class IteraPage(BasePage):

    def enter_words(self, name, phone, email, password, address):
        name_field = self.find_element(Itera_page_locators.LOCATOR_NAME_FIELD)
        name_field.send_keys(name)

        phone_field = self.find_element(Itera_page_locators.LOCATOR_PHONE_FIELD)
        phone_field.send_keys(phone)
        email_field = self.find_element(Itera_page_locators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.find_element(Itera_page_locators.LOCATOR_PASSW0RD_FIELD)
        password_field.send_keys(password)
        address_field = self.find_element(Itera_page_locators.LOCATOR_ADDRESS_FIELD)
        address_field.send_keys(address)

    def choose_radio_button_by_id(self, id_radio_or_checkboxes):
        a = self.find_element((By.ID, id_radio_or_checkboxes))
        a.click()
        return a

    def choose_dropdown(self, visible_text):
        dd_menu = self.find_element((By.CLASS_NAME, 'custom-select'), time=2)
        ddm = Select(dd_menu)
        ddm.select_by_visible_text(visible_text)
        return ddm.first_selected_option.text

# /html/body/div/div[5]/div[2]/div[1]/div[3]/label
    def choose_radio_button_by_xpath(self, id_radio_or_xpath):
        a = self.find_element((By.XPATH, id_radio_or_xpath))
        a.click()
        return a





    # class IteraPage(BasePage):
    #
    #     def enter_word(self, word):
    #         search_field = self.find_element(Itera_page_locators.LOCATOR_YANDEX_SEARCH_FIELD)
    #         search_field.click()
    #         search_field.send_keys(word)
    #         return search_field

    # def click_on_the_search_button(self):
    #     return self.find_element(Itera_page_locators.LOCATOR_YANDEX_SEARCH_BUTTON,time=2).click()
    #
    # def check_navigation_bar(self):
    #     all_list = self.find_elements(Itera_page_locators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
    #     nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
    #     return nav_bar_menu
