from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.maximize_window()

# Capture all the cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))  # Print number of cookies have been created
print(cookies)  # Print all the cookie pairs

# Adding new cookie to the browser
cookie = {'name': 'Mycookies', 'value': '1111111123'}
driver.add_cookie(cookie)

# Number of cookies after adding cookie
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
print('------------')
# Deleting cookie
driver.delete_cookie('Mycookies')

# Number of cookies after deleting
time.sleep(3)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()  # Capture all cookies after deleting
print(len(cookies))

driver.close()
