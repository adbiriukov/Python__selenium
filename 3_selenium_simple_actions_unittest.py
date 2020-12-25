from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
import time


class AssertionTest(unittest.TestCase):
    URL = "https://testautomationpractice.blogspot.com/"

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.URL)

    # def test_assert_title_and_url(self):
    #     assert self.driver.title == "Automation Testing Practice"
    #     assert self.driver.current_url == "https://testautomationpractice.blogspot.com/"

    # def test_wiki_search_field(self):
    #     # not always work
    #     #
    #     wiki_field = self.driver.find_element_by_id("Wikipedia1_wikipedia-search-input")
    #     # self.assertTrue(wiki_field.is_displayed())
    #     # self.assertTrue(wiki_field.is_enabled())
    #     wiki_field.send_keys("something")
    #     wiki_button = self.driver.find_element_by_xpath(
    #         '//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]')
    #     wiki_button.submit()
    #     time.sleep(5)
    #     wiki_result_header = self.driver.find_element_by_id("Wikipedia1_wikipedia-search-results-header")
    #     self.assertTrue(wiki_result_header.is_displayed())
    #     wiki_result = self.driver.find_element_by_id("Wikipedia1_wikipedia-search-results")
    #     assert "Search results" in wiki_result.text

    # def test_alert_accept(self):
    #     alert_button = self.driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button')
    #     alert_button.click()
    #     alert = self.driver.switch_to.alert
    #     self.assertEqual("Press a button!", alert.text)
    #     alert.accept()
    #     alert_text = self.driver.find_element_by_id("demo")
    #     self.assertEqual("You pressed OK!", alert_text.text)
    #
    # def test_alert_dismiss(self):
    #     alert_button = self.driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button')
    #     alert_button.click()
    #     alert = self.driver.switch_to.alert
    #     self.assertEqual("Press a button!", alert.text)
    #     alert.dismiss()
    #     alert_text = self.driver.find_element_by_id("demo")
    #     self.assertEqual("You pressed Cancel!", alert_text.text)
    #
    # def test_double_click(self):
    #     field1 = self.driver.find_element_by_xpath('//*[@id="field1"]')
    #     field2 = self.driver.find_element_by_xpath('//*[@id="field2"]')
    #     field1.clear()
    #     send_keys = "something"
    #     field1.send_keys(send_keys)
    #     double_click_button = self.driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
    #     action = ActionChains(self.driver)
    #     action.double_click(double_click_button).perform()

    def test_perform_drag_and_drop(self):
        draggable = self.driver.find_element_by_id('draggable')
        target = self.driver.find_element_by_id('droppable')
        self.assertEqual("Drop here", target.text)
        time.sleep(3)
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable, target).perform()
        assert "Dropped!" in target.text









    # def test_search(self):
    #     search_field = self.driver.find_element_by_name("q")
    #     search_field.clear()
    #     # check maxlength attribute is set to 2048
    #     self.assertEqual("2048", search_field.get_attribute("maxlength"))
    #     search_field.send_keys("phones")
    #     search_field.submit()
    #     time.sleep(1)
    #     assert "phones" in self.driver.title
    #
    # def test_account_displayed(self):
    #     account_link_button = self.driver.find_element_by_link_text("Войти")
    #     self.assertTrue(account_link_button.is_displayed())
    #     self.assertTrue(account_link_button.is_enabled())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
