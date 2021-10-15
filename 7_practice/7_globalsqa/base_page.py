from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import GlobalsqaLocators
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """Base page methods for globalsqa"""
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.globalsqa.com/demo-site/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def close_adv(self):
        try:
            self.driver.find_element_by_xpath(GlobalsqaLocators.LOCATOR_CLOSE_ADV).click()
            self.driver.execute_script("""var element = arguments[0];
                    element.parentNode.removeChild(element);
                    """, self.driver.find_element_by_xpath(GlobalsqaLocators.LOCATOR_DELETE_ADV))
            print('Adv Deleted')
        except:
            pass


    # First enter column and then row (row + 1 than actual)
    def open_page_by_xpath(self, column, row):
        self.driver.find_element_by_xpath(
            "//*[@id='post-2715']/div[2]/div/div/div[2]/div["+str(column)+"]/ul/li["+str(row)+"]/a").click()

