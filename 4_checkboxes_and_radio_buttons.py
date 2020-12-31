from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")
driver.find_element_by_id('vehicle1').click()
status = driver.find_element_by_id('vehicle1').is_selected() # true/false
print(status)
time.sleep(1)

# def is_checked(driver, item):
#   checked = driver.execute_script(("return document.getElementById('%s').checked") % item)
#   print(checked)
#   return checked
#
# is_checked(driver, status)
# driver.close()

# driver.find_element_by_id("some id").click()
# print(status)
#
#
# # checkboxes
# driver.find_element_by_id("checkboxes id").click()
