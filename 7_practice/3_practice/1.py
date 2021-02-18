import unittest
from selenium import webdriver
from amazon_web_elements import WebElements
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get("https://www.amazon.com/")

    # def test_language_options(self):
    #     # list of available languages
    #     exp_options = ["English - EN", "Español - ES", "简体中文 - ZH", "Deutsch - DE",
    #                    "Português - PT", "繁體中文 - ZH", "한국어 - KO"]
    #
    #     # make appear language menu
    #     language_option = self.driver.find_element_by_class_name('icp-nav-link-inner')
    #     action = ActionChains(self.driver)
    #     action.move_to_element(language_option).perform()
    #
    #     # grab list of items with tag 'span'
    #     links = self.driver.find_elements(By.TAG_NAME, "span")
    #
    #     # this is will check all options present on the page
    #     counter = -1
    #     try:
    #         for link in links:
    #             for option in exp_options:
    #                 if option == link.text:
    #                     counter += 1
    #     except Exception:
    #         pass
    #
    #     self.assertEqual(7, counter)

    # def test_language_option_is_worked(self):
    #     # cookies = self.driver.get_cookies()
    #
    #     # assert cookie is not present
    #     try:
    #         self.assertFalse(len(self.driver.get_cookie("lc-main")["value"]) > 0)
    #     except Exception:
    #         pass
    #
    #
    #     # change language
    #     self.driver.find_element_by_xpath('//*[@id="icp-nav-flyout"]/span/span[2]/span[1]').click()
    #     self.driver.find_element_by_xpath(
    #         '//*[@id="customer-preferences"]/div/div/form/div[1]/div[1]/div[4]/div/label/span').click()
    #     self.driver.find_element_by_xpath('//*[@id="icp-btn-save"]/span/input').click()
    #
    #     # cookies_2 = self.driver.get_cookies()
    #     # search for cookie that store language value
    #     # for cookie in cookies:
    #     #     for cookie_2 in cookies_2:
    #     #         if cookie != cookie_2:
    #     #             print(cookie)
    #     #             if cookie_2 != cookie:
    #     #                 print(cookie_2)
    #     #
    #     # print cookie to check value
    #     # print(driver.get_cookie("lc-main")["value"])
    #
    #     # assert cookie is present
    #     assert 'de_DE' == self.driver.get_cookie("lc-main")["value"]

    def test_css_for_home_page(self):
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="gw-layout"]/style/text()').is_displayed())
















    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
