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


# ## Multiple tabs/windows ##
# #
# # first window and tab are same, second every widow has a handle that can be used
# # to switch to that window, we can perform actions only in current window
# driver.get('http://demo.automationtesting.in/Windows.html')
# # show the handle of our current focused window
# print('current window handle', driver.current_window_handle)
# time.sleep(3)
#
# # show the handles of all windows in our browser, firstly let's open a new window
# driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()
# print('all handles', driver.window_handles)
#
# # so once we obtained the window handle, we can switch to it and can fetch like a new page or perform other action
# print("current window title:", driver.title)
#
# sec_window_handle = driver.window_handles[1]
# driver.switch_to.window(sec_window_handle)
# print("switched to second window:", driver.title)
# # closes only focued window
# driver.close()
