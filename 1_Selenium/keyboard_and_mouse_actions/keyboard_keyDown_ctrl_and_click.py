import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.get('http://google.com')
element = driver.find_element_by_link_text('Картинки')

ActionChains(driver).key_down(Keys.CONTROL).click(element).perform()

time.sleep(3)
driver.quit()
