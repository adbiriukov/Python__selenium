# test login with multiple account, and we store data in xlsc file. If pass it give PASS message,
# if failed give FAILED message
from selenium import webdriver
from selenium.webdriver import ActionChains
import test_24_DDT_1_using_Excel
import time

driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
path = "C://Users/User/PycharmProjects/LastTry_1220/selenium_logs/xlsx_files/111.xlsx"

# Get row count
# Sheet1 is name if the sheet (page in excel)
row = test_24_DDT_1_using_Excel.getRowCount(path, "Sheet1")
for r in range(2, row+1):
    username = test_24_DDT_1_using_Excel.readData(path, "Sheet1", r, 1) # 1 is column number where username
    password = test_24_DDT_1_using_Excel.readData(path, "Sheet1", r, 2) # 2 is column number where we store password

    driver.find_element_by_name("txtUsername").send_keys(username)
    driver.find_element_by_name("txtPassword").send_keys(password)
    driver.find_element_by_name("txtPassword").submit()
    if driver.current_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
        print("test is passed")
        test_24_DDT_1_using_Excel.writeData(path, "Sheet1", r, 3, "test passed")   # we pass data to the excel

        admin = driver.find_element_by_id('welcome')
        action = ActionChains(driver)
        action.move_to_element(admin).click().perform()
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]/a').click()
    else:
        print('Test failed')
        test_24_DDT_1_using_Excel.writeData(path, "Sheet1", r, 3, "Test failed")
