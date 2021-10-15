import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(executable_path="../../chromedriver", chrome_options=options)
    driver = webdriver.Chrome(executable_path="../../chromedriver")
    driver.maximize_window()
    yield driver
    driver.quit()
