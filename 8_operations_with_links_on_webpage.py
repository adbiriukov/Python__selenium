# We can:
# - check how many links present on page
# - Capture links
# - Click on the links

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("https://www.google.com/")
links = driver.find_elements(By.TAG_NAME, "a")

print("Number of links present: ", len(links))  # How many links present on a page
for link in links:
    if len(link.text) > 0:
        print(link.text)

# to click on the link
# driver.find_element(By.LINK_TEXT, "Картинки").click()
# print('---------')
# print(driver.title)


# another way to click on link
driver.find_element(By.PARTIAL_LINK_TEXT, "Картин").click()
print('---------')
print(driver.title)
driver.close()
