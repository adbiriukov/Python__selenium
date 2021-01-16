import unittest
from selenium import webdriver


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://www.google.com/")

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()
        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_id("result-stats")
        for product in products:
            self.assertTrue('Результатов: примерно' in product.text)

    def test_search_by_pagetitle(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("python")
        self.search_field.submit()
        # get all the anchor elements which have
        # product names displayed
        # currently on result page using
        # find_elements_by_xpath method
        self.assertIn("python", self.driver.title)



    @classmethod
    def tearDownClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../chromedriver.exe")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
