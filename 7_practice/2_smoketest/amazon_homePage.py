import unittest
from selenium import webdriver
from amazon_web_elements import WebElements


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://www.amazon.com/")

    def test_search_field(self):
        # check search field exists on  page
        self.assertTrue(self.driver.find_element(*WebElements.search_field).is_displayed())

    def test_language_option(self):
        # check deliver to country is displayed
        self.assertTrue(self.driver.find_element(*WebElements.deliver_country).is_displayed())

    def test_shopping_cart_empty_message(self):
        # check content of Shopping Cart is empty
        cart_status = self.driver.find_element(*WebElements.cart).get_attribute('aria-label')
        self.assertEqual(cart_status, '0 items in cart')

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
