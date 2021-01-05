from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
action = ActionChains(driver)
action.double_click(element).perform()  # Double click on button
time.sleep(3)
driver.close()
