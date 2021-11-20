from selenium.webdriver.common.by import By


class OrangeHRMLocators:
    """Locators for OrangeHRM"""
    # login page
    L_LOGIN_FIELD = (By.ID, 'txtUsername')
    L_PASSWORD_FIELD = (By.ID, 'txtPassword')
    L_LOGIN_BT = (By.ID, 'btnLogin')

    L_FORGOT_PASS_LINK = (By.XPATH, '//*[@id="forgotPasswordLink"]/a')
    L_FORGOT_PASS_USERNAME_F = (By.ID, 'securityAuthentication_userName')
    L_FORGOT_PASS_RESET_BT = (By.ID, 'btnSearchValues')
    L_FORGOT_PASS_MESSAGE_BT = (By.CLASS_NAME, 'messageCloseButton')

    L_FOOTER_LINK_LD = (By.XPATH, '//*[@id="social-icons"]/a[1]/img')
    L_FOOTER_LINK_FB = (By.XPATH, '//*[@id="social-icons"]/a[2]/img')
    L_FOOTER_LINK_TW = (By.XPATH, '//*[@id="social-icons"]/a[3]/img')
    L_FOOTER_LINK_YT = (By.XPATH, '//*[@id="social-icons"]/a[4]/img')

    L_UPPER_LOGO = (By.XPATH, '//*[@id="divLogo"]/img')

    # header
    L_HEADER_WELCOME_MS = (By.ID, 'welcome')
    L_HEADER_WELCOME_ABOUT = (By.XPATH, '//*[@id="aboutDisplayLink"]')
    L_HEADER_WELCOME_SUPPORT = (By.XPATH, '//*[@id="welcome-menu"]/ul/li[2]/a')
    L_HEADER_WELCOME_LOGOUT = (By.XPATH, '//*[@id="welcome-menu"]/ul/li[3]/a')












