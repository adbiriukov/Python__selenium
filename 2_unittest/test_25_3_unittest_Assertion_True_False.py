import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(
            executable_path="../chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.maximize_window()
        titleOfWebPage = driver.title

        # assert True
        self.assertTrue(titleOfWebPage == "Google")  # if True then Pass

        # assert False
        self.assertFalse(titleOfWebPage == "Google1")  # if False then pass



if __name__ == '__main__':
    unittest.main