import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(executable_path="../../chromedriver")
    yield driver
    time.sleep(5)
    driver.quit()
