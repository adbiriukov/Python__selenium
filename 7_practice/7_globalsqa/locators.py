from selenium.webdriver.common.by import By


class GlobalsqaLocators:
    """Locators for HeroPage"""
    # page Accordion And Tabs
    LOCATOR_PAGE_1_2_SECTION_1_TEXT = (By.XPATH, '//*[@id="ui-id-2"]/p')
    LOCATOR_PAGE_1_2_SECTION_2 = (By.XPATH, '//*[@id="ui-id-3"]')
    LOCATOR_PAGE_1_2_SECTION_2_TEXT = (By.XPATH, '//*[@id="ui-id-4"]/p')

    LOCATOR_PAGE_1_2_SECTION_1_TAB2_TEXT = (By.XPATH, '//*[@id="ui-id-2"]')
    LOCATOR_PAGE_1_2_SECTION_2_TAB2 = (By.XPATH, '//*[@id="ui-id-3"]')
    LOCATOR_PAGE_1_2_SECTION_2_TAB2_TEXT = (By.CSS_SELECTOR, '#ui-id-4 > p')


    LOCATOR_PAGE_1_2_IFRAME_1 = (By.CSS_SELECTOR, '#post-2654 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p > iframe')
    LOCATOR_PAGE_1_2_TAB_2 = (By.ID, 'Re-Size Accordion')
    LOCATOR_PAGE_1_2_RESIZE_ACCORDION = (By.ID, 'accordion-resizer')
    # post-2654 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p:nth-child(2) > iframe
    # post-2654 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p > iframe









