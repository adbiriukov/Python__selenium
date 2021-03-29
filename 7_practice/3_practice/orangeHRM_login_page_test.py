import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()

    # def test_correct_login(self):
    #     self.driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
    #     self.driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
    #     self.driver.find_element_by_xpath("//*[@id='btnLogin']").click()
    #     self.assertTrue(self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').is_displayed())
    #     cook = self.driver.get_cookies()
    #     print(cook)
    #
    # def test_login_with_wrong_password(self):
    #     self.driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
    #     self.driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("Admin")
    #     self.driver.find_element_by_xpath("//*[@id='btnLogin']").click()
    #     self.assertTrue(self.driver.find_element_by_id('spanMessage').is_displayed())
    #
    # def test_login_with_empty_field(self):
    #     self.driver.find_element_by_xpath("//*[@id='btnLogin']").click()
    #     self.assertEqual(self.driver.find_element_by_id('spanMessage').text, 'Username cannot be empty')

    def test_by_login_using_cookies(self):
        self.driver.delete_all_cookies()
        cookie = {'domain': 'opensource-demo.orangehrmlive.com', 'httpOnly': True, 'name': 'orangehrm', 'path': '/', 'secure': True, 'value': 'f4263d38b6a887a40dbaa7267fdabc40'}
        self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').is_displayed())

    # def test_logout(self):
    #     self.driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
    #     self.driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
    #     self.driver.find_element_by_xpath("//*[@id='btnLogin']").click()
    #     self.assertTrue(self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').is_displayed())
    #     self.driver.find_element_by_id('welcome').click()
    #     self.driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]/a').click()
    #     self.assertTrue(self.driver.find_element_by_xpath("//*[@id='txtUsername']").is_displayed())
    #
    # def test_facebook_link(self):
    #     self.driver.find_element_by_xpath('//*[@id="social-icons"]/a[2]/img').click()
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     self.assertEqual(self.driver.current_url, 'https://www.facebook.com/OrangeHRM')
    #
    # def test_forget_password_option(self):
    #     self.driver.find_element_by_xpath('//*[@id="forgotPasswordLink"]/a').click()
    #     self.assertTrue(self.driver.find_element_by_id('securityAuthentication_userName').is_displayed())
    #     self.driver.find_element_by_id('btnCancel').click()
    #     self.assertTrue(self.driver.find_element_by_id('txtUsername').is_displayed())

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
