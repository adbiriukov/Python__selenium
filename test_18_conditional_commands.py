from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

time.sleep(3)
action = ActionChains(driver)
cbox = driver.find_element_by_id('RESULT_CheckBox-8_0')
print(cbox.is_selected())
action.click(cbox).perform()

print(cbox.is_enabled())     #
print(cbox.is_selected())    # all return true/false based on element status
print(cbox.is_displayed())   #


driver.close()
