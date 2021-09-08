from locators_form_fields import Fields
from element import BasePageElement_1

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="../../../../chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://itera-qa.azurewebsites.net/home/automation")


# # Fields
driver.find_element_by_id(Fields.name).send_keys('Name')
driver.find_element_by_id(Fields.phone).send_keys('12345678')
driver.find_element_by_id(Fields.email).send_keys('email@gmail.com')
driver.find_element_by_id(Fields.password).send_keys('password')
driver.find_element_by_id(Fields.address).send_keys('Some address')



class SearchTextElement(BasePageElement_1):
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    # Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    # def is_title_matches(self):
    #     """Verifies that the hardcoded text "Python" appears in page title"""
    #     return "Python" in self.driver.title
    #
    # def click_go_button(self):
    #     """Triggers the search"""
    #     element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
    #     element.click()



































# # # Radio Button
# action = ActionChains(driver)
# radio = driver.find_element_by_id('male')
# action.click(radio).perform()
# radio.is_selected()
#
# # CheckBox
# cbox1 = driver.find_element_by_id('monday')
# cbox2 = driver.find_element_by_id('friday')
# action.click(cbox1).click(cbox2).perform()
# cbox1.is_selected()
# cbox2.is_selected()
#
# # DropDown
# dd_menu = driver.find_element_by_class_name('custom-select')
# ddm = Select(dd_menu)
# ddm.select_by_visible_text('Norway')
# # print(dd_menu.get_attribute("value"))
#
# # CheckBox & Radio Button practice Xpath
# radio_xpath = driver.find_element_by_xpath('/html/body/div/div[5]/div[2]/div[1]/div[2]/label')
# action.click(radio_xpath).perform()
# radio_xpath.is_selected()
#
# cbox = driver.find_element_by_xpath('/html/body/div/div[5]/div[2]/div[2]/div[1]/label')
# action.click(cbox).perform()
# cbox.is_selected()
#
# # Close browser
# driver.close()
