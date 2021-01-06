from selenium import webdriver
import unittest
import time


class AssertionTest(unittest.TestCase):
    URL = "https://www.google.com/"

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.get(self.URL)

    def test_assert_title_and_url(self):
        assert self.driver.title == "Google"
        assert self.driver.current_url == "https://www.google.com/"

    def test_search(self):
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()
        # check maxlength attribute is set to 2048
        self.assertEqual("2048", search_field.get_attribute("maxlength"))
        search_field.send_keys("phones")
        search_field.submit()
        time.sleep(1)
        assert "phones" in self.driver.title

    def test_account_displayed(self):
        account_link_button = self.driver.find_element_by_link_text("Войти")
        self.assertTrue(account_link_button.is_displayed())
        self.assertTrue(account_link_button.is_enabled())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
