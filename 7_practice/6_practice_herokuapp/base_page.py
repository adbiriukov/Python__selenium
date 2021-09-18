from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base page methods for HeroPage"""
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://the-internet.herokuapp.com/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def open_page_by_xpath(self, li):
        self.driver.find_element_by_xpath("// *[ @ id = 'content'] / ul / li["+str(li)+"] / a").click()
