from selenium import webdriver
import time
import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import Select


class AssertionTest(unittest.TestCase):
    URL = "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(cls.URL)

    def test_1_fill_text_boxes(self):
        first_name = self.driver.find_element_by_id('RESULT_TextField-1')
        first_name.send_keys('Andrey')
        self.assertTrue(first_name.get_attribute('value') == 'Andrey')

    def test_2_radio_button(self):
        action = ActionChains(self.driver)
        radio = self.driver.find_element_by_id('RESULT_RadioButton-7_0')
        action.click(radio).perform()
        radio.is_selected()

    def test_3_check_boxes(self):
        action = ActionChains(self.driver)
        cbox = self.driver.find_element_by_id('RESULT_CheckBox-8_0')
        action.click(cbox).perform()
        cbox.is_selected()

    def test_4_drop_down_menu(self):
        dd_menu = self.driver.find_element_by_id('RESULT_RadioButton-9')
        ddm = Select(dd_menu)
        ddm.select_by_visible_text('Morning')
        self.assertTrue(dd_menu.get_attribute("value") == 'Radio-0')

    def test_5_click_submit_get_error(self):
        self.driver.find_element_by_id('FSsubmit').click()
        result = self.driver.find_element_by_class_name('segment_header')
        self.assertTrue(result.text == 'An error has occurred')
        print(result.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)



# Old test's
#
# check boxes
# def test_checkboxes(self):
#     self.driver.switch_to.frame('frame-one1434677811')
#
#     action = ActionChains(self.driver)
#     radio = self.driver.find_element_by_id('RESULT_CheckBox-8_0')
#     radio.is_displayed()
#     # action.click(radio)
#     # action.perform()
#
#     self.assertTrue(self.driver.find_element_by_id('RESULT_CheckBox-8_0').is_selected())
#     time.sleep(5)
#     # button = self.driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7_0"]')
#     # self.driver.execute_script("arguments[0].click();", button)



##########
# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")
# driver.switch_to.frame("iframeResult")
# driver.find_element_by_id("vehicle1").click()
# status = driver.find_element_by_id("vehicle1").is_selected()  # true/false
# print(status)
# driver.find_element_by_id("vehicle1").submit()
# time.sleep(30)
# result = driver.find_element_by_xpath('/html/body/div[1]')
# print("---")
# print(result.text)
# driver.close()
#
# driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
# driver.switch_to.frame("iframeResult")
# driver.find_element_by_id('male').click()
# driver.find_element_by_id('age1').click()
# driver.find_element_by_xpath('/html/body/form/input[7]').click()
# time.sleep(30)
# result = driver.find_element_by_xpath('/html/body/div[1]')
# print("---")
# print(result.text)
######################


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='vehicle1']"))).click()
