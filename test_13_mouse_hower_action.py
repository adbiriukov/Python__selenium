# Here we perform Mouse hover action
from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermgmt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

action = ActionChains(driver)

action.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()
try:
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers'
    print('True')
except:
    print('False')
driver.close()
