from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
import time


class AssertionTest(unittest.TestCase):
    URL = "https://testautomationpractice.blogspot.com/"

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.URL)

    def test_1_assert_title_and_url(self):
        assert self.driver.title == "Automation Testing Practice"
        assert self.driver.current_url == "https://testautomationpractice.blogspot.com/"

    def test_2_wiki_search_field(self):
        wiki_field = self.driver.find_element_by_id("Wikipedia1_wikipedia-search-input")
        wiki_field.send_keys("something")
        self.driver.find_element_by_xpath('//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input')\
            .click()

        wiki_result = self.driver.find_element_by_id("Wikipedia1_wikipedia-search-results")
        wiki_result.is_displayed()

    def test_3_alert_accept(self):
        alert_button = self.driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button')
        alert_button.click()
        alert = self.driver.switch_to.alert
        self.assertEqual("Press a button!", alert.text)
        alert.accept()
        alert_text = self.driver.find_element_by_id("demo")
        self.assertEqual("You pressed OK!", alert_text.text)

    def test_4_alert_dismiss(self):
        alert_button = self.driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button')
        alert_button.click()
        alert = self.driver.switch_to.alert
        self.assertEqual("Press a button!", alert.text)
        alert.dismiss()
        alert_text = self.driver.find_element_by_id("demo")
        self.assertEqual("You pressed Cancel!", alert_text.text)

    def test_5_double_click(self):
        field1 = self.driver.find_element_by_xpath('//*[@id="field1"]')
        field1.clear()
        send_keys = "something"
        field1.send_keys(send_keys)
        double_click_button = self.driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
        action = ActionChains(self.driver)
        action.double_click(double_click_button).perform()

    def test_6_perform_drag_and_drop(self):
        draggable = self.driver.find_element_by_id('draggable')
        target = self.driver.find_element_by_id('droppable')
        self.assertEqual("Drop here", target.text)
        time.sleep(3)
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable, target).perform()
        assert "Dropped!" in target.text

    def test_7_drop_down_menu(self):
        element1 = self.driver.find_element_by_id("speed")
        ddm = Select(element1)
        ddm.select_by_visible_text("Fast")
        element2 = self.driver.find_element_by_id("files")
        ddm = Select(element2)
        ddm.select_by_visible_text("PDF file")
        element3 = self.driver.find_element_by_id("number")
        ddm = Select(element3)
        ddm.select_by_visible_text("5")
        element4 = self.driver.find_element_by_id("products")
        ddm = Select(element4)
        ddm.select_by_visible_text("Google")
        element5 = self.driver.find_element_by_id("animals")
        ddm = Select(element5)
        ddm.select_by_visible_text("Avatar")

    # def test_8_radio_button(self):
    #     # not always work
    #     self.driver.switch_to.frame('frame-one1434677811')
    #
    #     action = ActionChains(self.driver)
    #     time.sleep(10)
    #     # radio = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located
    #     ((By.NAME, "RESULT_RadioButton-7")))
    #     radio = self.driver.find_element_by_id('RESULT_RadioButton-7_0')
    #     radio.is_displayed()
    #     action.click(radio).perform()
    #
    #     self.assertTrue(radio.is_selected())
    #     time.sleep(5)

    def test_9_link_displayed(self):
        submit_link_button = self.driver.find_element_by_link_text("Tooltips")
        self.assertTrue(submit_link_button.is_displayed())

    def test_10_tool_tip(self):
        # driver = self.driver
        # frame_elm = driver.find_element_by_class_name("demo-frame")
        # driver.switch_to.frame(frame_elm)
        age_field = self.driver.find_element_by_id("age")
        ActionChains(self.driver).move_to_element(age_field).perform()
        tool_tip_elm = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located
                                                            ((By.CLASS_NAME, "ui-tooltip-content")))
        # verify tooltip message
        self.assertEqual("We ask for your age only for statistical purposes.", tool_tip_elm.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
