from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("THERE WRITE FILE PATH, FOR EXMPL. C://SelenPractice/inputfiles.exmple.jpg")
