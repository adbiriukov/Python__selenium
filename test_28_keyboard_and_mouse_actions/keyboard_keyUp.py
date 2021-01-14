from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.get("http://www.google.com")
driver.maximize_window()

# Store google search box WebElement
search = driver.find_element(By.NAME, "q")

# Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
action = webdriver.ActionChains(driver)
action.key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()
