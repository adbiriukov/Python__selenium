from selenium.webdriver.common.by import By


class LoginFormElements(object):
    # Registration form fields
    name = (By.NAME, 'txtUsername')
    password = (By.NAME, 'txtPassword')
    button = (By.XPATH, '//*[@id="btnLogin"]')
    message = (By.ID, 'spanMessage')

    # error message texts
    empty_username = 'Username cannot be empty'
    empty_password = 'Password cannot be empty'
    invalid_credentials = 'Invalid credentials'

    # correct login and password
    correct_login = 'Admin'
    correct_password = 'admin123'
    # incorrect password
    incorrect_password = 'Admin'
