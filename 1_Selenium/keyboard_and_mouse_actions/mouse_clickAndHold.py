from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.get("http://www.google.com")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(3)

# Store 'google search' button web element
searchBtn = driver.find_element(By.LINK_TEXT, "Войти")

# Perform click-and-hold action on the element
webdriver.ActionChains(driver).click_and_hold(searchBtn).perform()
