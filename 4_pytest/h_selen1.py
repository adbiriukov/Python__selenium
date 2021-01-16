import pytest
from selenium import webdriver
import allure

@pytest.fixture()
def test_set_up():
    global driver # for using variable in all functions
    driver = webdriver.Chrome(executable_path="C:\\Some\\Path\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    # fixture use after each fact. for quit after complite function we use yield
    yield
    driver.quit()

@allure.description("Some description about test")
@allure.severity(severity_level="NORMAL")
def test_validLogin(test_set_up):
    driver.get("somelink")
    #enter user name by 'allur' function
    enter_username('admin')
    # enter user password by 'allur' function
    enter_password('password')
    driver.find_element_by_id("someid").click()
    try:
        assert "Something" in driver.title
    finally:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(),
                          name='invalid something', attachment_type=allure.attachment_type.PNG)

@allure.description("Some description about test")
@allure.severity(severity_level="NORMAL")
def test_invalidLogin(test_set_up):
    driver.get("somelink")
    driver.find_element_by_id("someid").send_keys("Some keys")
    driver.find_elements_by_name("somename").send_keys("Some keys")
    driver.find_element_by_id("someid").click()
    assert "Something" in driver.title

@allure.step('Entering username as {0}')
def enter_username(username):
    driver.find_elements_by_id('some id').send_keys(username)

@allure.step('Entering password as {0}')
def enter_password(password):
    driver.find_elements_by_id('some id').send_keys(password)


# in cmd # pytest -v -s  file.py --alluredir=name_of_folder (folder where we store reports) # after exec tests:: "allure serve name_of_folder"
#  allure-pytest ??library

# to save info about test's "allure serve reports"
#and it's start server and show results in browser

