from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.get("https://crossbrowsertesting.github.io/drag-and-drop")
driver.maximize_window()
time.sleep(3)

# Store 'box A' as source element
sourceEle = driver.find_element(By.ID, "draggable")
# Store 'box B' as source element
targetEle = driver.find_element(By.ID, "droppable")

# Performs dragAndDropBy onto the target element offset position
webdriver.ActionChains(driver).click_and_hold(sourceEle).move_to_element(targetEle).perform()
# Performs release event
webdriver.ActionChains(driver).release().perform()
