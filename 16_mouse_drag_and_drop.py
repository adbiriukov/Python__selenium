from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element = driver.find_element_by_xpath("//*[@id='box6']")
target_element = driver.find_element_by_xpath("//*[@id='box106']")

actions = ActionChains(driver)

actions.drag_and_drop(source_element, target_element).perform()  # perform drag and drop actions
time.sleep(3)
driver.close()
