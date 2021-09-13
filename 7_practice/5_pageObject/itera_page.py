from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class IteraPageLocators:
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


class IteraPage(BasePage):

    def enter_words(self, name, phone, email, password, address):
        name_field = self.find_element(IteraPageLocators.LOCATOR_NAME_FIELD)
        name_field.send_keys(name)

        phone_field = self.find_element(IteraPageLocators.LOCATOR_PHONE_FIELD)
        phone_field.send_keys(phone)
        email_field = self.find_element(IteraPageLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.find_element(IteraPageLocators.LOCATOR_PASSW0RD_FIELD)
        password_field.send_keys(password)
        address_field = self.find_element(IteraPageLocators.LOCATOR_ADDRESS_FIELD)
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
