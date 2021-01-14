from selenium import webdriver
from selenium.webdriver.common.by import By


# Navigate to url
driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.get("https://crossbrowsertesting.github.io/drag-and-drop")

# Store 'box A' as source element
sourceEle = driver.find_element(By.ID, "draggable")
# Store 'box B' as source element
targetEle = driver.find_element(By.ID, "droppable")
# Performs drag and drop action of sourceEle onto the targetEle
webdriver.ActionChains(driver).drag_and_drop(sourceEle, targetEle).perform()
