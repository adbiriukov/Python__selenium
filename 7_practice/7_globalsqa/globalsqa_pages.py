from base_page import BasePage
from locators import GlobalsqaLocators

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


class GlobalsqaPages(BasePage):
    # if advertisement block web element
    def scroll_page(self):
        # ActionChains(self.driver).key_down(Keys.SPACE).perform()
        # self.driver.execute_script("window.scrollBy (0, document.body.scrollHeight)")
        scroll_to = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_BASE_SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to)

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

    def sliders(self):
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_3_IFRAME))
        red = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_3_RED_SLIDER)
        red.is_displayed()
        # 1_Tried to change through JS styles, it's doesn't work
        # self.driver.execute_script("arguments[0].style = 'left: 0%;';", red)
        # self.driver.execute_script("arguments[0].style = 'width: 0%;';", red)
        # action = ActionChains(self.driver)
        # action.key_down(Keys.ARROW_LEFT).perform()
        #
        # 2_Action chains don't see destination element even if change to default content
        # action = ActionChains(self.driver)
        # action.click_and_hold(red)
        # self.driver.switch_to.default_content()
        # action.move_to_element(GlobalsqaLocators.LOCATOR_PAGE_1_3_DESTINATION_ELEMENT_FOR_SLIDER).perform()
        green = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_3_GREEN_SLIDER)
        green.is_displayed()

        blue = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_3_BLUE_SLIDER)
        blue.is_displayed()

    def tooltip(self):
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_4_IFRAME))
        # find By Class name doesn't work
        # image = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_4_IMAGE)
        image = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_4_IMAGE_x)
        ActionChains(self.driver).move_to_element(image).perform()
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_4_TOOLTIP).is_displayed()

    def dialog_boxes(self):
        time.sleep(2)
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_6_IFRAME))
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_6_CREATE_NEW_USER).click()
        name = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_6_NAME)
        name.clear()
        name.send_keys('Janee Smith')
        email = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_6_EMAIL)
        email.clear()
        email.send_keys('janee@smith.com')
        password = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_6_PASSWORD)
        password.clear()
        password.send_keys('password09')
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_6_CREATE_AN_ACC_BT).click()
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_6_USER_CREATED).is_displayed()

    def progress_bar(self):
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_7_IFRAME))
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_7_START_DOWNLOAD).click()
        time.sleep(10)
        progress = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_1_7_PROGRESS_LABEL)
        return progress.text

