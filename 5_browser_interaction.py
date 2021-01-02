from selenium import webdriver
import time
import unittest


class AssertionTest(unittest.TestCase):
    URL = "https://www.google.com/"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(cls.URL)

    def test_1_search(self):
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()
        # check maxlength attribute is set to 2048
        self.assertEqual("2048", search_field.get_attribute("maxlength"))
        search_field.send_keys("phones")
        search_field.submit()
        time.sleep(1)
        assert "phones" in self.driver.title
        time.sleep(3)

    def test_2_back(self):
        self.driver.back()
        self.assertTrue(self.driver.current_url == 'https://www.google.com/')
        time.sleep(3)

    def test_3_forward(self):
        self.driver.forward()
        assert "phones" in self.driver.title
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
