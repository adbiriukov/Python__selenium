from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
# Method 1
# driver.save_screenshot("C:/Users/User/Downloads/homepage.png")

# Method 2
driver.get_screenshot_as_file("C:/Users/User/Downloads/homepage2.png")

# To take full page screenshot
# JavaScript executor with starting node of DOM and the height [Note: Make sure the browser in headless mode ]
#
# or    pyautogui
