from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

# driver.switch_to_alert().accept()   # closes alert window using OK button
# driver.switch_to_alert().dismiss()    # closes alert windows using cancel button
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(3)
driver.close()
