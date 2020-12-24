from selenium import webdriver
import unittest
import time

class AssertionTest(unittest.TestCase):
    URL = "https://www.google.com/"
    def setUp(self):
        self.driver.implicitly_wait(30)
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get(self.URL)

    def test_assert_title_and_url(self):
        assert self.driver.title == "Google"
        assert self.driver.current_url == "https://www.google.com/"

    def test_search(self):
        search = self.driver.find_element_by_name("q")
        search.clear()
        search.send_keys("phones")
        search.submit()
        time.sleep(1)
        assert "phones" in self.driver.title

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main(verbosity=2)
