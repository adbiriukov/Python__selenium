# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# import time
#
# # set up
# driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
# driver.get("https://edadeal.ru/")
# driver.maximize_window()
# driver.implicitly_wait(5)
#
# # close rollout banner
# action = ActionChains(driver)
# rollout = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]')
# action.move_to_element(rollout).click().perform()
#
# # close alert
# try:
#     alert = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div')
#     action.move_to_element(alert).click().perform()
# except:
#     print('error')
#
#
requests = ('Куриная грудка', 'крабовые палочки', 'горбуша', 'тунец', 'морковь', 'греча', 'рис', 'кефир', 'творог')
count = 1
for request in requests:
    driver.execute_script("window.open('https://edadeal.ru/ekaterinburg/offers?q="+str(request)+"&retailer=5ka&retailer=kirmarket&retailer=magnit-univer&retailer=perekrestok&retailer=verno&sort=aprice', 'new_window +"+str(count)+"')")
    count += 1
    time.sleep(5)
