from selenium import webdriver


driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame")    # first frame (it's name of the frame or id
driver.find_element_by_link_text("org.openqa.selenium").click()

# before change frame you must go to the main frame and then to the frame you needed. If you complete task and need to
# change frame again you must change back to the main frame and then to the frame you needed
driver.switch_to.default_content()  # this method change to default and this need to do to do before change frame
driver.switch_to.frame("packageFrame")  # Second frame
driver.find_element_by_link_text("WebDriver").click()

driver.switch_to.default_content()
driver.switch_to.frame("classFrame")  # Third frame
search = driver.find_element_by_id('search')
print(search.is_displayed())

driver.close()
