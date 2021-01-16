# Explicit wait
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.implicitly_wait(30)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "RESULT_RadioButton-7_0'"))
    )
    element.click()
    result = element.is_selected()
    print(result)
finally:
    driver.quit()
