from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.get("http://www.google.com/")

time.sleep(2)
#open tab
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# You can use (Keys.CONTROL + 't') on other OSs

# Load a page
driver.get('http://stackoverflow.com/')
# Make the tests...

# close the tab
# (Keys.CONTROL + 'w') on other OSs.
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')


driver.close()