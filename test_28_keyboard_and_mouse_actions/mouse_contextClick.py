from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.get("http://www.google.com")
driver.implicitly_wait(10)
driver.maximize_window()

# Store 'google search' button web element
searchBtn = driver.find_element(By.LINK_TEXT, "Войти")

# Perform context-click action on the element
webdriver.ActionChains(driver).context_click(searchBtn).perform()
