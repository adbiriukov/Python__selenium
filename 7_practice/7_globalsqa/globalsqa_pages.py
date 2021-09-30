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

    def dropdown(self, visible_text):
        dd_menu = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_2_5_DROPDOWN)
        ddm = Select(dd_menu)
        ddm.select_by_visible_text(visible_text)
        return ddm.first_selected_option.text

    def select_elements(self):
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_2_7_IFRAME))
        item_1 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_2_7_ITEM_1)
        item_2 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_2_7_ITEM_2)
        item_3 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_2_7_ITEM_3)
        ActionChains(self.driver).key_down(Keys.CONTROL).click(item_1).click(item_2).click(item_3).perform()

    def sorting_elements(self):
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_2_IFRAME))
        element_1 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_2_ELEMENT_1)
        element_2 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_2_ELEMENT_2)
        ActionChains(self.driver).click_and_hold(element_1).drag_and_drop(element_1, element_2).perform()
        time.sleep(3)

    def spiner_field(self):
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_3_IFRAME))
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_3_SPINER_FIELD).click()
        ActionChains(self.driver).key_down(Keys.ARROW_UP).perform()
        # without it throw error "Message: element not interactable"
        time.sleep(1)

    def drag_and_drop(self):
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_6_IFRAME))
        photo_1 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_6_PHOTO_1)
        photo_2 = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_6_PHOTO_2)
        trash = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_6_TRASH)
        ActionChains(self.driver).drag_and_drop(photo_1, trash).perform()
        ActionChains(self.driver).drag_and_drop(photo_2, trash).perform()

    def draggable_element(self):
        self.driver.switch_to.frame(self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_7_IFRAME))
        draggable = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_3_7_DRAGGABLE)
        ActionChains(self.driver).click_and_hold(draggable).move_by_offset(200, 200).pause(2).release().perform()

    def sample_page(self):
        # fill fields
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_4_2_NAME_FIELD).send_keys('SomeName')
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_4_2_EMAIL_FIELD).send_keys('some@some.com')
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_4_2_WEBSITE_FIELD).send_keys('https://www.some.com')
        # Select value in dropdown menu
        dd_menu = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_4_2_EXP_SELECTOR)
        ddm = Select(dd_menu)
        ddm.select_by_visible_text('1-3')
        # Select checkboxes
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_4_2_CB_FUNCT_TEST).click()
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_4_2_CB_AUTO_TEST).click()
        # Scroll to 500px down
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", 500)
        # Select radio button
        radio = self.find_element(GlobalsqaLocators.LOCATOR_PAGE_4_2_RADIO_EDU_OTHER)
        radio.click()
        # Write comment
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_4_2_COMMENT_FIELD).send_keys('Some comment')
        # Click submit button
        self.find_element(GlobalsqaLocators.LOCATOR_PAGE_4_2_SUBMIT_BT).click()

    # To enter angularjs pages
    # First enter column and then row (row + 1 than actual)
    def angularjs_open_page_by_xpath(self, column, row):
        self.driver.find_element_by_xpath(
            "//*[@id='post-2777']/div[2]/div/div/div[2]/div["+str(column)+"]/ul/li["+str(row)+"]/a").click()

    def multiform(self):
        self.find_element(GlobalsqaLocators.LP_4_3_1_2_NAME).send_keys('Something')
        self.find_element(GlobalsqaLocators.LP_4_3_1_2_EMAIL).send_keys('email@mail.com')
        self.find_element(GlobalsqaLocators.LP_4_3_1_2_NEXT_SECTION_BT).click()
        self.find_element(GlobalsqaLocators.LP_4_3_1_2_RADIO_PS4).click()
        self.find_element(GlobalsqaLocators.LP_4_3_1_2_NEXT_SECTION_BT_2).click()
        self.find_element(GlobalsqaLocators.LP_4_3_1_2_SUBMIT_BT).is_displayed()
        time.sleep(3)
