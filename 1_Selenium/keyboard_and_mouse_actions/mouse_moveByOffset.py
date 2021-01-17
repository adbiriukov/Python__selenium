from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)


# Set x and y offset positions of element
xOffset = 100
yOffset = 100
# Performs mouse move action onto the element
webdriver.ActionChains(driver).move_by_offset(xOffset, yOffset).perform()
driver.close()
