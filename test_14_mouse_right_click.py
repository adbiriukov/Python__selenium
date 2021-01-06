from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions = ActionChains(driver)
# context_click  -- to perform right click action
actions.context_click(button).perform()
time.sleep(3)
