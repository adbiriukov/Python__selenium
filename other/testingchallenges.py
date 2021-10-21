from selenium import webdriver
import unittest
import time


class AssertionTest(unittest.TestCase):
    URL = "http://testingchallenges.thetestingmap.org/index.php"

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.get(cls.URL)

    def test_first_name_field(self):
        # 1 Average value
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('Name')
        first_name.submit()
        time.sleep(1)
        # 2 Minimum value
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('f')
        first_name.submit()
        time.sleep(1)
        # 3 Maximum values
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('aaaaaaaaaabbbbbbbbbbcccccccccc')
        first_name.submit()
        time.sleep(1)
        # 4 More than maximum values
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('aaaaaaaaaabbbbbbbbbbccccccccccd')
        first_name.submit()
        time.sleep(1)
        # 5 Other chars then alphabetic
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('1')
        first_name.submit()
        time.sleep(1)
        # 6 used html tags
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('<h1></h1>')
        first_name.submit()
        time.sleep(1)
        # 7 Basic XSS
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('<script></script>')
        first_name.submit()
        time.sleep(1)
        # 8 Space values at the beginning
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys(' Name')
        first_name.submit()
        time.sleep(1)
        # 9 Space in the middle
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('Na me')
        first_name.submit()
        time.sleep(1)
        # 10 Space values at the end
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('Name ')
        first_name.submit()
        time.sleep(1)
        # 11 Non ASCII
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('平仮名')
        first_name.submit()
        time.sleep(1)
        # 12 Space
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys(' ')
        first_name.submit()
        time.sleep(1)
        # 13 Empty value
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('')
        first_name.submit()
        time.sleep(1)
        # 14 Basic Sql injection
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys("test'test;")
        first_name.submit()
        time.sleep(1)
        # 15 Missing css
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('detailsoverviewnow.css')
        first_name.submit()
        time.sleep(1)
        # 16 looked at the page source
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('dfjwGGe82H43g3uRiy53h')
        first_name.submit()
        time.sleep(1)
        # 17 looked at the cookie
        first_name = self.driver.find_element_by_id('firstname')
        first_name.send_keys('oi32jnxd42390slk345')
        first_name.submit()
        time.sleep(1)


    # stop traffic by fiddler and change user right as admin to 1

    # dufferebt browsers
    # browser zoom in and out
    # extremely big requests
    # nasty words

    # @classmethod
    # def tearDown(cls):
    #     cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
    #     cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)




