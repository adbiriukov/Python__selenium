from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass


#
# driver.find_element(By.XPATH, '//button[text()="Some text"]')


