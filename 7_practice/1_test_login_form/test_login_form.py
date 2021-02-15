import unittest
from selenium import webdriver
from web_elements import LoginFormElements
import time


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

    # Positive test
    def test_correct_login(self):
        # Test with correct login
        self.driver.find_element(*LoginFormElements.name).send_keys(LoginFormElements.correct_login)
        self.driver.find_element(*LoginFormElements.password).send_keys(LoginFormElements.correct_password)
        self.driver.find_element(*LoginFormElements.button).click()
        assert self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').is_displayed()

    # Negative tests
    def test_empty_login_and_password(self):
        # login with empty login and password fields
        self.driver.find_element(*LoginFormElements.button).click()
        error_message = self.driver.find_element(*LoginFormElements.message)
        assert error_message.text == LoginFormElements.empty_username

    def test_empty_password_field(self):
        # login with password field
        self.driver.find_element(*LoginFormElements.name).send_keys(LoginFormElements.correct_login)
        self.driver.find_element(*LoginFormElements.button).click()
        error_message = self.driver.find_element(*LoginFormElements.message)
        assert error_message.text == LoginFormElements.empty_password

    def test_incorrect_password(self):
        # login with incorrect password
        self.driver.find_element(*LoginFormElements.name).send_keys(LoginFormElements.correct_login)
        self.driver.find_element(*LoginFormElements.password).send_keys(LoginFormElements.incorrect_password)
        self.driver.find_element(*LoginFormElements.button).click()
        error_message = self.driver.find_element(*LoginFormElements.message)
        assert error_message.text == LoginFormElements.invalid_credentials
        time.sleep(3)

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
