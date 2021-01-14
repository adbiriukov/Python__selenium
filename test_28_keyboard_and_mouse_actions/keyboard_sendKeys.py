from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.get("http://www.google.com")
driver.maximize_window()

# Enter "webdriver" text and perform "ENTER" keyboard action

driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)
