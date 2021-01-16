from selenium import webdriver
import unittest


class AssertionTest(unittest.TestCase):
    URL = "https://www.google.com/"

    # Difference between setUp, tearDown method and class its:
    # method execute multiple time before and after each test,
    # class execute only once before and after
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.get(cls.URL)

    def test_assert_title_and_url(self):
        assert self.driver.title == "Google"
        assert self.driver.current_url == "https://www.google.com/"

    def test_search_field(self):
        # check search field exists on Home page
        self.driver.find_element_by_name("q").is_displayed()

    def test_search(self):
        search = self.driver.find_element_by_name("q")
        search.clear()
        search.send_keys("phones")
        search.submit()
        assert "phones" in self.driver.title

    def test_assert_results(self):
        search = self.driver.find_element_by_name("q")
        search.clear()
        search.send_keys("phones")
        search.submit()
        results = self.driver.find_elements_by_id("result-stats")
        for result in results:
            self.assertTrue('Результатов: примерно' in result.text)

    @classmethod
    def tearDown(cls):
        cls.driver = webdriver.Chrome(executable_path="../chromedriver.exe")
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
