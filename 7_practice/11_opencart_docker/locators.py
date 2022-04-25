from selenium.webdriver.common.by import By


class OpencartLocators:
    """Locators for opencart"""
    # header
    L_HEADER_MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown > a')
    L_HEADER_REGISTER_BT = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a')
    L_HEADER_WISHLIST_LINK = (By.CSS_SELECTOR, '#wishlist-total > span')
    L_HEADER_SHOPPING_CART_LINK = (By.CSS_SELECTOR, '#top-links > ul > li:nth-child(4) > a > span')
    L_HEADER_CHECKOUT = (By.CSS_SELECTOR, '#top-links > ul > li:nth-child(5) > a > span')

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

    L_REGISTER_POLICY_WARNING = (By.CSS_SELECTOR, '#account-register > div.alert.alert-danger.alert-dismissible')
    L_REGISTER_FNAME_WARNING = (By.CSS_SELECTOR, '#account > div:nth-child(3) > div > div')
    L_REGISTER_LNAME_WARNING = (By.CSS_SELECTOR, '#account > div:nth-child(4) > div > div')
    L_REGISTER_EMAIL_WARNING = (By.CSS_SELECTOR, '#account > div:nth-child(5) > div > div')
    L_REGISTER_TELEPHONE_WARNING = (By.CSS_SELECTOR, '#account > div:nth-child(6) > div > div')
    L_REGISTER_PASSWORD_WARNING = (By.CSS_SELECTOR, '#content > form > fieldset:nth-child(2) > div.form-group.required.has-error > div > div')


    # Shopping cart page
    L_SHOPPING_CART_CART_IS_EMPTY = (By.CSS_SELECTOR, '#content > p')
    L_SHOPPING_CART_CART_CONTINUE_BT = (By.CSS_SELECTOR, '#content > div > div > a')

    # Tabs
    L_TAB_DESKTOPS = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(1) > a')
    L_TAB_LAPTOPS_AND_NOTEBOOKS = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(2) > a')
    L_TAB_COMPONENTS = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(3) > a')
    L_TAB_TABLETS = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(4) > a')
    L_TAB_SOFTWARE = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(5) > a')
    L_TAB_PHONE_AND_PDAS = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(6) > a')
    L_TAB_CAMERAS = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(7) > a')
    L_TAB_MP3_PLAYERS = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(8) > a')

    # Product compare
    PAGE_MESSAGE_COMPARE = (By.CSS_SELECTOR, '#product-category > div.alert.alert-success.alert-dismissible > a:nth-child(3)')
    PRODUCT_COMPARE1 = (By.CSS_SELECTOR, '#content > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(3) > i')
    PRODUCT_COMPARE2 = (By.CSS_SELECTOR, '#content > div:nth-child(3) > div:nth-child(2) > div > div:nth-child(2) > div.button-group > button:nth-child(3) > i')

    PRODUCT_COMPARISON_PAGE_PRODUCT1 = (By.CSS_SELECTOR, '#content > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')
    PRODUCT_COMPARISON_PAGE_PRODUCT2 = (By.CSS_SELECTOR, '#content > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')

