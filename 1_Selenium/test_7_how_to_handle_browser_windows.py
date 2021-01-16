from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print("handle 1: " + driver.current_window_handle)  # this command give you handle value of the window
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print("handle 2: " + driver.current_window_handle)

handles = driver.window_handles  # Return all the handle values of opened browser windows
for handle in handles:
    driver.switch_to.window(handle)
    print("Open page: " + driver.title)
    time.sleep(3)
    if driver.title == "Frames & windows":
        driver.close()  # Close only parent window


driver.quit()  # Quit will close all windows (close will close only 1 window)
