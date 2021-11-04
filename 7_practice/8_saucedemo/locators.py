from selenium.webdriver.common.by import By


class SaucedemoLocators:
    """Locators for Saucedemo"""
    # main page
    L_USERNAME_FIELD = (By.ID, 'user-name')
    L_PASSWORD_FIELD = (By.ID, 'password')
    L_LOGIN_BT = (By.ID, 'login-button')
    L_LOGO_IMG = (By.XPATH, '//*[@id="root"]/div/div[1]')

    # products page
    # add items
    L_BACKPACK_ADD = (By.ID, 'add-to-cart-sauce-labs-backpack')
    L_BIKE_LIGHT_ADD = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    L_TSHIRT_ADD = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    L_JACKET_ADD = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    L_ONESIE_ADD = (By.ID, 'add-to-cart-sauce-labs-onesie')
    L_RED_TSHIRT_ADD = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')

    # remove items
    L_BACKPACK_REMOVE = (By.ID, 'remove-sauce-labs-backpack')
    L_BIKE_LIGHT_REMOVE = (By.ID, 'remove-sauce-labs-bike-light')
    L_TSHIRT_REMOVE = (By.ID, 'remove-sauce-labs-bolt-t-shirt')
    L_JACKET_REMOVE = (By.ID, 'remove-sauce-labs-fleece-jacket')
    L_ONESIE_REMOVE = (By.ID, 'remove-sauce-labs-onesie')
    L_RED_TSHIRT_REMOVE = (By.ID, 'remove-test.allthethings()-t-shirt-(red)')

    # drop down menu for sorting items
    L_DROPDOWN_MENU = (By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select')
    # list of all products
    L_LIST_OF_PRODUCTS = (By.XPATH, '//*[@id="inventory_container"]/div/div[1]')

    # Cart, number items in cart
    L_IN_CART_NUMBER = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    L_CART = (By.ID, 'shopping_cart_container')

    # checkout fields and buttons
    L_CHECKOUT = (By.ID, 'checkout')
    L_FIRST_NAME_F = (By.ID, 'first-name')
    L_LAST_NAME_F = (By.ID, 'last-name')
    L_POSTALCODE = (By.ID, 'postal-code')
    L_CHECKOUT_CONTINUE_BT = (By.ID, 'continue')
    L_CHECKOUT_FINISH = (By.ID, 'finish')
    L_CHECKOUT_FINISH_TEXT = (By.XPATH, '//*[@id="checkout_complete_container"]/div')

    # Left up corner menu
    L_MENU_IN_LEFT_UP_CORNER = (By.ID, 'react-burger-menu-btn')
    L_MENU_RC_RESET_APP = (By.ID, 'reset_sidebar_link')
    L_MENU_RC_LOGOUT = (By.ID, 'logout_sidebar_link')

    # footer links
    L_FOOTER_TW_LINK = (By.CLASS_NAME, 'social_twitter')
    L_FOOTER_FB_LINK = (By.CLASS_NAME, 'social_facebook')
    L_FOOTER_LD_LINK = (By.CLASS_NAME, 'social_linkedin')
