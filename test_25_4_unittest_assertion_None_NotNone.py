import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        # self.assertIsNone(driver)  # if contains value then NOT Pass
        self.assertIsNotNone(driver)  # if contains value then Pass

    def testName1(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.assertIsNone(driver)  # if contains value then NOT Pass
        # self.assertIsNotNone(driver)  # if contains value then Pass


if __name__ == '__main__':
    unittest.main
