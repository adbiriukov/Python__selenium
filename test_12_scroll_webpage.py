from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
# 1 Scroll down the page by pixel
# driver.execute_script("window.scrollBy (0, 1000)", "")
#
# 2 Scroll down page till the element is visible
# flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[35]/td[1]/img")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# time.sleep(3)
#
# # Scroll down the page till end
driver.execute_script("window.scrollBy (0, document.body.scrollHeight)")
driver.close()
