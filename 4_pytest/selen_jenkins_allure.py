from selenium import webdriver
import pytest
import allure


@pytest.fixture()
def test_set_up():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    # navigate to the application home page
    driver.get("https://www.google.com/")
    yield
    driver.quit()

@allure.description('Test 1')
@allure.severity(severity_level="NORMAL")
def test_search_by_category(test_set_up):
    # get the search textbox
    search_field = driver.find_element_by_name("q")
    search_field.clear()
    # enter search keyword and submit
    search_field.send_keys("phones")
    search_field.submit()
    # get all the anchor elements which have product names
    # displayed currently on result page using
    # find_elements_by_xpath method
    products = driver.find_elements_by_id("result-stats")
    for product in products:
        assert 'Результатов: примерно' in product.text

@allure.description('Test 1')
@allure.severity(severity_level="NORMAL")
def test_search_by_pagetitle(test_set_up):
    # get the search textbox
    search_field = driver.find_element_by_name("q")
    search_field.clear()
    # enter search keyword and submit
    search_field.send_keys("python")
    search_field.submit()
    # get all the anchor elements which have
    # product names displayed
    # currently on result page using
    # find_elements_by_xpath method
    try:
        assert "python" in driver.title
    finally:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(),
                          name='invalid something', attachment_type=allure.attachment_type.PNG)



