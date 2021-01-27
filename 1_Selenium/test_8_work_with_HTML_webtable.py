# from selenium import webdriver
#
#
# driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
# driver.get("https://www.w3schools.com/html/html_tables.asp")
#
# # to get all rows just delete [1] from /tbody/tr[1], same for columns
# rows = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr'))
# print(rows)  # how many rows we have
# columns = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr[1]/th'))
# print(columns)  # how many columns
#
# # print header of table
# print("Company"+"        "+"Contact"+"        "+"Country")
#
# for r in range(2, rows+1):
#     for c in range(1, columns+1):
#         value = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
#         print(value.text, end='        ')
#     print()
#
#
# driver.close()
