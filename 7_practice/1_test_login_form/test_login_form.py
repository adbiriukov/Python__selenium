import unittest
from selenium import webdriver
from web_elements import RegFormElements
import time


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

    # Positive test
    # Test with correct login
    def test_correct_login(self):
        self.driver.find_element(*RegFormElements.name).send_keys('Admin')
        self.driver.find_element(*RegFormElements.password).send_keys('admin123')
        self.driver.find_element(*RegFormElements.button).click()
        assert self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').is_displayed()

    # Negative tests
    # login with empty login and password fields
    def test_empty_login_and_password(self):
        self.driver.find_element(*RegFormElements.button).click()
        error_message = self.driver.find_element(*RegFormElements.message)
        assert error_message.text == RegFormElements.empty_username

    # login with password field
    def test_empty_password_field(self):
        self.driver.find_element(*RegFormElements.name).send_keys('Admin')
        self.driver.find_element(*RegFormElements.button).click()
        error_message = self.driver.find_element(*RegFormElements.message)
        assert error_message.text == RegFormElements.empty_password

    # login with incorrect password
    def test_incorrect_password(self):
        self.driver.find_element(*RegFormElements.name).send_keys('Admin')
        self.driver.find_element(*RegFormElements.password).send_keys('Admin')
        self.driver.find_element(*RegFormElements.button).click()
        error_message = self.driver.find_element(*RegFormElements.message)
        assert error_message.text == RegFormElements.invalid_credentials
        time.sleep(3)

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
