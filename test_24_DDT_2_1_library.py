import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
import time

@ddt
class SeartchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://www.amazon.com/')
        # search value and expected count

    @data(('phone', 'results'), ('music', 'results'))
    @unpack
    def test_search(self, search_value, expected_count):
        search_field = self.driver.find_element_by_name('field-keywords')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()
        result = self.driver.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]')
        print(result.text)
        self.assertTrue(expected_count in result.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
