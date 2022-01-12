from selenium.webdriver.common.by import By


class NopcommerceLocators:
    """Locators for OrangeHRM"""
    # header
    L_HEADER_REGISTER_BT = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a')
    L_HEADER_LOGIN_BT = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')
    L_HEADER_WISHLIST_BT = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[3]/a/span[1]')
    L_HEADER_SHOPPING_CART_BT = (By.XPATH, '//*[@id="topcartlink"]/a/span[1]')
    L_HEADER_LOGOUT_BT = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')

    # Register page
    L_REGISTER_GENDER_MALE_RADIO = (By.ID, 'gender-male')
    L_REGISTER_GENDER_FEMALE_RADIO = (By.ID, 'gender-female')
    L_REGISTER_FIRSTNAME_FIELD = (By.ID, 'FirstName')
    L_REGISTER_LASTNAME_FIELD = (By.ID, 'LastName')
    L_REGISTER_DATEofBIRTHDAY_SELECT = (By.NAME, 'DateOfBirthDay')
    L_REGISTER_MONTHofBIRTHDAY_SELECT = (By.NAME, 'DateOfBirthMonth')
    L_REGISTER_YEARofBIRTHDAY_SELECT = (By.NAME, 'DateOfBirthYear')
    L_REGISTER_EMAIL_FIELD = (By.ID, 'Email')
    L_REGISTER_COMPANY_NAME_FIELD = (By.ID, 'Company')
    L_REGISTER_NEWSLETTER_CHECKBOX = (By.ID, 'Newsletter')
    L_REGISTER_PASSWORD_FIELD = (By.ID, 'Password')
    L_REGISTER_CONFIRM_PASSWORD_FIELD = (By.ID, 'ConfirmPassword')
    L_REGISTER_REGISTER_BT = (By.ID, 'register-button')
    # Register page messages
    L_REGISTER_FIRSTNAME_REQUIRED_MS = (By.CLASS_NAME, 'field-validation-error')
    L_REGISTER_LASTNAME_REQUIRED_MS = (By.CLASS_NAME, 'field-validation-error')
    L_REGISTER_EMAIL_REQUIRED_MS = (By.ID, 'Email-error')
    L_REGISTER_PASSWORD_REQUIRED_MS = (By.ID, 'Password-error')
    L_REGISTER_CONFIRM_PASSWORD_REQUIRED_MS = (By.ID, 'ConfirmPassword-error')
    L_REGISTER_EMAIL_EXIST_MS = (By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/ul/li')

    # Login page
    L_LOGIN_EMAIL_FIELD = (By.ID, 'Email')
    L_LOGIN_PASSWORD_FIELD = (By.ID, 'Password')
    L_LOGIN_REMEMBER_ME_CHECKBOX = (By.ID, 'RememberMe')
    L_LOGIN_FORGET_PASSWORD_LINK = (By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div[3]/span/a')
    L_LOGIN_LOGIN_BT = (By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button')


