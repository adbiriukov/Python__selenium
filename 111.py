import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('https://www.amazon.com/')
search_field = driver.find_element_by_name('field-keywords')
search_field.clear()
search_value.send_keys('phome')
search_field.submit()
