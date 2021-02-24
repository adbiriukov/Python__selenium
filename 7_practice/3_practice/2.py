import unittest
from selenium import webdriver
from amazon_web_elements import WebElements
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.amazon.com/")


def test_css_for_home_page(self):
    self.assertTrue("http://g-ec2.images-amazon.com/images/G/01/social/api-share/amazon_logo_500500._V323939215_.png" in
                    self.driver.find_element_by_css_selector("div")
                    .value_of_css_property("background-image"))


driver.close()

