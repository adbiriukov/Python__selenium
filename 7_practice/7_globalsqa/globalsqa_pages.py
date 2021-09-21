from base_page import BasePage
from locators import GlobalsqaLocators

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


class GlobalsqaPages(BasePage):
    def tabs_text_is_present(self):
        # Check section 1,2 text on the first tab
        # Change frame and find and check elements
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_2_IFRAME_1))
        section1 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_2_SECTION_1_TEXT)
        if 'Mauris' in section1.text:
            section1 = True

        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_2_SECTION_2).click()
        section2 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_2_SECTION_2_TEXT)
        if 'Sed' in section2.text:
            section2 = True
        # Switch to default frame to change tab
        self.driver.switch_to.default_content()

        # Change tab
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_2_TAB_2).click()
        # Change frame
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_2_IFRAME_1))
        # Size of accordion
        accordion_size = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_2_RESIZE_ACCORDION)
        self.driver.execute_script("arguments[0].style = 'width: 600px; height: 300px;';", accordion_size)
        # Check section 1,2 text on the second tab
        section1_tab2 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_2_SECTION_1_TAB2_TEXT)
        print(section1_tab2.text)
        print('-------')
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_2_SECTION_2_TAB2).click()
        time.sleep(1)
        section2_tab2 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_2_SECTION_2_TAB2_TEXT)
        print(section2_tab2.text)


