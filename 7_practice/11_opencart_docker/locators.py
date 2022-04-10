from selenium.webdriver.common.by import By


class OpencartLocators:
    """Locators for opencart"""
    # header
    L_HEADER_MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown > a')
    L_HEADER_REGISTER_BT = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a')

    # register page
    L_REGISTER_FNAME = (By.CSS_SELECTOR, '#input-firstname')
    L_REGISTER_LNAME = (By.CSS_SELECTOR, '#input-lastname')
    L_REGISTER_EMAIL = (By.CSS_SELECTOR, '#input-email')
    L_REGISTER_TELEPHONE = (By.CSS_SELECTOR, '#input-telephone')
    L_REGISTER_PASSWORD = (By.CSS_SELECTOR, '#input-password')
    L_REGISTER_CONF_PASSWORD = (By.CSS_SELECTOR, '#input-confirm')
    L_REGISTER_RADIO_SUBSCRIBE_TO_NEWSLETTER = (By.CSS_SELECTOR, '#content > form > fieldset:nth-child(3) > div > div > label:nth-child(2) > input[type=radio]')
    L_REGISTER_CONF_POLICY= (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
    L_REGISTER_CONTINUE_BT = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')



