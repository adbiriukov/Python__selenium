import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="../chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.maximize_window()
        titleOfWebPage = driver.title
        self.assertEqual("Google", titleOfWebPage, "web page title is not same (writing when assertion failed")

        self.assertNotEqual("Google123", titleOfWebPage)


if __name__ == '__main__':
    unittest.main
