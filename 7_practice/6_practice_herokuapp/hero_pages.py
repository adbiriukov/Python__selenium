from base_page import BasePage
from locators import HeroPagesLocators

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


class HeroPages(BasePage):
    """'Methods' for work with HeroPage features"""
    # page Add/Remove Elements
    def page_add_remove_elements(self):
        # Find and click add element button
        add_element_bt = self.find_element(HeroPagesLocators.LOCATOR_PAGE_1_ADD_BT)
        add_element_bt.click()
        # Check that element is present, click and check that element isn't present
        del_element_bt = self.find_element(HeroPagesLocators.LOCATOR_PAGE_1_DEL_BT)
        del_displayed = del_element_bt.is_displayed()
        del_element_bt.click()
        del_not_displayed = False
        try:
            del_element_bt.is_displayed()
        except:
            del_not_displayed = True
        # Return test results
        return del_displayed, del_not_displayed

    # Open 'Basic Auth' page and check that element is present
    def enter_login_and_password(self):
        self.driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
        del_element_bt = self.find_element(HeroPagesLocators.LOCATOR_PAGE_3_BASIC_AUTH)
        return del_element_bt.is_displayed()

    def find_broken_images(self):
        images = self.find_elements(HeroPagesLocators.LOCATOR_PAGE_4_BROKEN_IMAGES)
        broken_images = []
        for image in images:
            a = image.get_attribute("naturalWidth")
            if int(a) == 0:
                b = image.get_attribute("outerHTML")
                broken_images.append(b)
        return broken_images

    def select_checkboxes(self):
        checkbox1 = self.find_element(HeroPagesLocators.LOCATOR_PAGE_6_CHECKBOX_1)
        checkbox1.click()
        return checkbox1.is_selected()

    def context_menu(self):
        actions = ActionChains(self.driver)
        context_window = self.find_element(HeroPagesLocators.LOCATOR_PAGE_7_CONTEXT_WINDOW)
        actions.context_click(context_window).perform()
        time.sleep(3)

    def disappearing_elements(self):
        # Will refresh page several times and collect number of links in a set
        elements_len = set()
        for x in range(3):
            elements = self.find_elements(HeroPagesLocators.LOCATOR_PAGE_9_DISAPPEARING_ELEMENTS)
            self.driver.refresh()
            elements_len.add(len(elements))
        # if number of links changed, return True
        if len(elements_len) == 2:
            return True
        else:
            return False

    def drag_and_drop(self):
        draggable = self.find_element(HeroPagesLocators.LOCATOR_PAGE_10_DND_1)
        droppable = self.find_element(HeroPagesLocators.LOCATOR_PAGE_10_DND_2)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

    def drop_down_menu(self, visible_text):
        dd_menu = self.find_element(HeroPagesLocators.LOCATOR_PAGE_11_DROPDOWN)
        ddm = Select(dd_menu)
        ddm.select_by_visible_text(visible_text)
        return ddm.first_selected_option.text

    def dynamic_content(self):
        texts_len = set()
        for x in range(3):
            self.driver.refresh()
            first_text = self.find_element(HeroPagesLocators.LOCATOR_PAGE_12_DYNAMIC_CONTENT_1)
            second_text = self.find_element(HeroPagesLocators.LOCATOR_PAGE_12_DYNAMIC_CONTENT_2)
            third_text = self.find_element(HeroPagesLocators.LOCATOR_PAGE_12_DYNAMIC_CONTENT_3)
            texts_len.add(first_text.text)
            texts_len.add(second_text.text)
            texts_len.add(third_text.text)
        if len(texts_len) > 3:
            return True
        else:
            return False

    def dynamic_controls(self):
        # Find and click checkbox
        checkbox = self.find_element(HeroPagesLocators.LOCATOR_PAGE_13_CHECKBOX)
        ActionChains(self.driver).move_to_element(checkbox).click().perform()
        # Find and click Remove button
        remove_bt = self.find_element(HeroPagesLocators.LOCATOR_PAGE_13_REMOVE_BT)
        ActionChains(self.driver).move_to_element(remove_bt).click().perform()
        # Find and click Enable button
        enable_bt = self.find_element(HeroPagesLocators.LOCATOR_PAGE_13_ENABLE_BT)
        enable_bt.click()
        # wait for field to be enabled and enter value. Explicit wait don't work and test return:
        # 'element not interactable'
        time.sleep(3)
        text_field = self.find_element(HeroPagesLocators.LOCATOR_PAGE_13_TEXT_FIELD)
        text_field.send_keys('Something')
        # Checking that both messages is present ant return True if true
        text_field_message_displayed = self.find_element(
            HeroPagesLocators.LOCATOR_PAGE_13_TEXT_FIELD_MESSAGE).is_displayed()
        remove_bt_message_displayed = self.find_element(
            HeroPagesLocators.LOCATOR_PAGE_13_REMOVE_BT_MESSAGE).is_displayed()
        if remove_bt_message_displayed and text_field_message_displayed is True:
            return True
        else:
            return False

    def close_entry_ad(self):
        # Wait for Modal Adv to show and close Adv window
        time.sleep(3)
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_15_CLOSE_AD).click()

    def floating_menu_click_at_each_bt(self):
        # click at each floating menu button
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_19_HOME_BT).click()
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_19_NEWS_BT).click()
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_19_CONTACT_BT).click()
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_19_ABOUT_BT).click()

    def form_authentication(self):
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_21_USERNAME_FIELD).send_keys('tomsmith')
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_21_PASSWORD_FIELD).send_keys('SuperSecretPassword!')
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_21_SUBMIT_BT).click()
        message = self.find_element(HeroPagesLocators.LOCATOR_PAGE_21_SUCCESS_MS)
        return message.text

    def ifames(self):
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_22_IFRAMES_LINK).click()

        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name('frame')[0])
        left = self.find_element(HeroPagesLocators.LOCATOR_PAGE_22_LEFT_IFRAME)
        middle = self.find_element(HeroPagesLocators.LOCATOR_PAGE_22_MIDDLE_IFRAME)
        right = self.find_element(HeroPagesLocators.LOCATOR_PAGE_22_RIGHT_IFRAME)
        left = left.is_displayed()
        middle = middle.is_displayed()
        right = right.is_displayed()

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name('frame')[1])
        bottom = self.find_element(HeroPagesLocators.LOCATOR_PAGE_22_BOTTOM_IFRAME)
        bottom = bottom.is_displayed()
        if left and middle and right and bottom is True:
            return True
        else:
            return False

    def horizontal_slider(self):
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_24_SLIDER).click()
        ActionChains(self.driver).key_down(Keys.ARROW_RIGHT).perform()
        text = self.find_element(HeroPagesLocators.LOCATOR_PAGE_24_SLIDER_NUMBER)
        if text.text == '3':
            return True
        else:
            return False

    def hover(self):
        user = self.find_element(HeroPagesLocators.LOCATOR_PAGE_25_HOVER_USER_1)
        view_profile = self.find_element(HeroPagesLocators.LOCATOR_PAGE_25_VIEW_PROFILE)
        ActionChains(self.driver).move_to_element(user).perform()
        ActionChains(self.driver).move_to_element(view_profile).click().perform()
        return self.find_element(HeroPagesLocators.LOCATOR_PAGE_25_VIEW_PROFILE_CODE).is_displayed()

    def infinite_scroll(self):
        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def input_numbers(self):
        input_field = self.find_element(HeroPagesLocators.LOCATOR_PAGE_27_INPUT_FIELD)
        input_field.click()
        ActionChains(self.driver).key_down(Keys.ARROW_UP).perform()

    def jquery_ui_menu(self):
        enabled = self.find_element(HeroPagesLocators.LOCATOR_PAGE_28_ENABLED_JQ)
        downloads = self.find_element(HeroPagesLocators.LOCATOR_PAGE_28_DOWNLOADS_JQ)
        pdf = self.find_element(HeroPagesLocators.LOCATOR_PAGE_28_PDF_JQ)
        ActionChains(self.driver).move_to_element(enabled).perform()
        time.sleep(1)
        ActionChains(self.driver).move_to_element(downloads).perform()
        time.sleep(1)
        ActionChains(self.driver).move_to_element(pdf).perform()
        time.sleep(1)

    def js_alerts(self):
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_29_JS_ALERT).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_29_JS_ALERT_CONFIRM).click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def key_presses(self):
        ActionChains(self.driver).key_down(Keys.CONTROL).perform()
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.SHIFT).perform()
        time.sleep(2)

    def large_page_dom(self):
        a = self.find_element(HeroPagesLocators.LOCATOR_PAGE_32_LARGE_PAGE_DOM)
        print(a.text)

    def browser_new_window(self):
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_33_OPEN_NEW_WINDOW).click()
        # Return all the handle values of opened browser windows
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)

    def notification_message(self):
        a = self.find_element(HeroPagesLocators.LOCATOR_PAGE_35_NOTIFICATION_MESSAGE)
        return a.text

    def sortable_data_tables(self):
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_41_TABLES_EMAIL).click()
        self.find_element(HeroPagesLocators.LOCATOR_PAGE_41_DUE).click()
