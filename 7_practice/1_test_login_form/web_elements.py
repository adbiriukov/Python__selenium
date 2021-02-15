from selenium.webdriver.common.by import By


class RegFormElements(object):
    # Registration form fields
    name = (By.NAME, 'txtUsername')
    password = (By.NAME, 'txtPassword')
    button = (By.XPATH, '//*[@id="btnLogin"]')
    message = (By.ID, 'spanMessage')

    # error message texts
    empty_username = 'Username cannot be empty'
    empty_password = 'Password cannot be empty'
    invalid_credentials = 'Invalid credentials'
