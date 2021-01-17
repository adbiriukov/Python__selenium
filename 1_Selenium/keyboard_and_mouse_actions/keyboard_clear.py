from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.get("http://www.google.com")
driver.maximize_window()

SearchInput = driver.find_element(By.NAME, "q")
SearchInput.send_keys("selenium")

# Clears the entered text
time.sleep(3)
SearchInput.clear()
