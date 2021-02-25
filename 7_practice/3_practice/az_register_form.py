import unittest
from selenium import webdriver
from amazon_web_elements import WebElements
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get("https://www.amazon.com/")

    def test_signup(self):
        # test for signup form
        signin_menu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
        signup_button = self.driver.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a')
        # navigating to registration form
        action = ActionChains(self.driver)
        action.move_to_element(signin_menu).perform()
        action.move_to_element(signup_button).click().perform()
        # assert element is not displayed
        self.assertFalse(
            self.driver.find_element_by_xpath('//*[@id="auth-password-mismatch-alert"]/div/div').is_displayed())
        self.driver.find_element_by_id('ap_customer_name').send_keys('test123')
        self.driver.find_element_by_id('ap_email').send_keys('test123@gmail.com')
        self.driver.find_element_by_id('ap_password').send_keys('test123')
        self.driver.find_element_by_id('ap_password_check').send_keys('test321')
        self.driver.find_element_by_id('continue').click()
        # assert element is displayed
        self.assertTrue(
            self.driver.find_element_by_xpath('//*[@id="auth-password-mismatch-alert"]/div/div').is_displayed())

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
