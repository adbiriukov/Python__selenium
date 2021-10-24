from selenium.webdriver.common.by import By

class SaucedemoLocators:
    """Locators for Saucedemo"""
    # main page
    L_USERNAME_FIELD = (By.ID, 'user-name')
    L_PASSWORD_FIELD = (By.ID, 'password')
    L_LOGIN_BT = (By.ID, 'login-button')
    L_LOGO_IMG = (By.XPATH, '//*[@id="root"]/div/div[1]')


    # products page
    L_BACKPACK_ADD = (By.ID, 'add-to-cart-sauce-labs-backpack')
    L_BIKE_LIGHT_ADD = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    L_TSHIRT_ADD = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    L_JACKET_ADD = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    L_ONESIE_ADD = (By.ID, 'add-to-cart-sauce-labs-onesie')
    L_RED_TSHIRT = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')

