from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
# driver.get("https://edadeal.ru/")
# driver.maximize_window()
# driver.implicitly_wait(30)
#
# action = ActionChains(driver)
# rollout = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]')
# action.move_to_element(rollout).click().perform()
#
# # alert = driver.switch_to.alert
# # alert.accept()
# try:
#     alert = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div')
#     action.move_to_element(alert).click().perform()
# except:
#     print('error')
#
# time.sleep(1)
# search1 = driver.find_element_by_xpath('/html/body/div[7]/div/header/span/div/div/div/div')
# search1.click()
# time.sleep(1)
# search2 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/form/div/div/div/input')
# search2.send_keys('Крабовые палочки')
# search2.submit()



# time.sleep(1)
# all_stores = driver.find_element_by_xpath('//*[@id="view"]/div[1]/div/header/span[1]/span')
# all_stores.click()
# time.sleep(1)
# verny = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div[2]')
# verny.click()
# five_ka = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[10]/div[2]')
# five_ka.click()
# kirov_sky = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[25]/div[2]/div[1]')
# kirov_sky.click()
# magnit = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[29]/div[2]/div[1]')
# magnit.click()
# monetka = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[36]/div[2]/div[1]')
# monetka.click()
#
# show = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/span')
# show.click()


driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.get("https://edadeal.ru/ekaterinburg/offers?search=%D0%BA%D1%80%D0%B0%D0%B1%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BF%D0%B0%D0%BB%D0%BE%D1%87%D0%BA%D0%B8&title=%D0%BA%D1%80%D0%B0%D0%B1%D0%BE%D0%B2%D1%8B%D0%B5%20%D0%BF%D0%B0%D0%BB%D0%BE%D1%87%D0%BA%D0%B8/")
driver.maximize_window()
driver.implicitly_wait(30)
action = ActionChains(driver)
rollout = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]')
action.move_to_element(rollout).click().perform()




time.sleep(1)
good1 = driver.find_element_by_xpath('//*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[1]/div/div/div/div[1]/div[2]/div[1]/div')
print(good1.text)
price1 = driver.find_element_by_xpath('//*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[1]/div/div/div/div[1]/div[2]/div[3]/div[1]/div')
print(price1.text)

good2 = driver.find_element_by_xpath('//*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[2]/div/div/div/div[1]/div[2]/div[1]/div')
print(good2.text)
price2 = driver.find_element_by_xpath('//*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[2]/div/div/div/div[1]/div[2]/div[3]/div[1]/div')
print(price2.text)

good3 = driver.find_element_by_xpath('//*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[3]/div/div/div/div[1]/div[2]/div[1]/div')
print(good3.text)
price3 = driver.find_element_by_xpath('//*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[3]/div/div/div/div[1]/div[2]/div[3]/div[1]/div')
print(price3.text)

# # text
# //*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[1]/div/div/div/div[1]/div[2]/div[1]/div
# //*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[2]/div/div/div/div[1]/div[2]/div[1]/div
# //*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[3]/div/div/div/div[1]/div[2]/div[1]/div
# # price
# //*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[1]/div/div/div/div[1]/div[2]/div[3]/div[1]/div
# //*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[2]/div/div/div/div[1]/div[2]/div[3]/div[1]/div
# //*[@id="view"]/div[1]/div/div[2]/div/div/div/section[2]/a[3]/div/div/div/div[1]/div[2]/div[3]/div[1]/div




