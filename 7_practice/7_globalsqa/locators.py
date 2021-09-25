from selenium.webdriver.common.by import By


class GlobalsqaLocators:
    """Locators for HeroPage"""
    #
    LOCATOR_PAGE_BASE_SCROLL = (By.XPATH, '//*[@id="post-2715"]/div[3]/a')
    #
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

    #
    # page slider
    LOCATOR_PAGE_1_3_RED_SLIDER = (By.XPATH, '//*[@id="red"]/span')
    LOCATOR_PAGE_1_3_GREEN_SLIDER = (By.XPATH, '//*[@id="green"]/span')
    LOCATOR_PAGE_1_3_BLUE_SLIDER = (By.XPATH, '//*[@id="blue"]/span')

    LOCATOR_PAGE_1_3_IFRAME = (By.CSS_SELECTOR, '#post-2673 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p > iframe')
    LOCATOR_PAGE_1_3_DESTINATION_ELEMENT_FOR_SLIDER = (By.XPATH, '//*[@id="menu-item-2802"]/a/span[2]')

    #
    # tooltip
    # ui-corner-all
    LOCATOR_PAGE_1_4_IMAGE = (By.CLASS_NAME, 'ui-corner-all')
    LOCATOR_PAGE_1_4_IMAGE_x = (By.XPATH, '/html/body/div[1]/a/img')
    LOCATOR_PAGE_1_4_IFRAME = (By.CSS_SELECTOR, '#post-2679 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p:nth-child(2) > iframe')
    LOCATOR_PAGE_1_4_TOOLTIP = (By.CLASS_NAME, 'ui-tooltip-content')

    # dialog boxes
    LOCATOR_PAGE_1_6_IFRAME = (By.CSS_SELECTOR, '#post-2663 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p:nth-child(1) > iframe')
    LOCATOR_PAGE_1_6_CREATE_NEW_USER = (By.ID, 'create-user')
    LOCATOR_PAGE_1_6_NAME = (By.ID, 'name')
    LOCATOR_PAGE_1_6_EMAIL = (By.ID, 'email')
    LOCATOR_PAGE_1_6_PASSWORD = (By.ID, 'password')
    LOCATOR_PAGE_1_6_CREATE_AN_ACC_BT = (By.XPATH, '/html/body/div[3]/div[3]/div/button[1]')
    LOCATOR_PAGE_1_6_USER_CREATED = (By.XPATH, '//*[@id="users"]/tbody/tr[2]/td[2]')

    # Progress Bar
    LOCATOR_PAGE_1_7_IFRAME = (By.CSS_SELECTOR, '#post-2671 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p > iframe')
    LOCATOR_PAGE_1_7_START_DOWNLOAD = (By.ID, 'downloadButton')
    LOCATOR_PAGE_1_7_PROGRESS_LABEL = (By.XPATH, '//*[@id="dialog"]/div[1]')

    # Dropdown menu
    LOCATOR_PAGE_2_5_DROPDOWN = (By.XPATH, '//*[@id="post-2646"]/div[2]/div/div/div/p/select')

    # Select Elements
    LOCATOR_PAGE_2_7_IFRAME = (By.CSS_SELECTOR, '#post-2649 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p > iframe')
    LOCATOR_PAGE_2_7_ITEM_1 = (By.XPATH, '//*[@id="selectable"]/li[1]')
    LOCATOR_PAGE_2_7_ITEM_2 = (By.XPATH, '//*[@id="selectable"]/li[2]')
    LOCATOR_PAGE_2_7_ITEM_3 = (By.XPATH, '//*[@id="selectable"]/li[3]')

    # sorting elements
    LOCATOR_PAGE_3_2_IFRAME = (By.CSS_SELECTOR, '#post-2675 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p > iframe')
    LOCATOR_PAGE_3_2_ELEMENT_1 = (By.XPATH, '/html/body/div[1]/div[1]')
    LOCATOR_PAGE_3_2_ELEMENT_2 = (By.XPATH, '/html/body/div[3]/div[2]/div[2]')

    # Spiner
    LOCATOR_PAGE_3_3_IFRAME = (By.CSS_SELECTOR, '#post-2677 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p > iframe')
    LOCATOR_PAGE_3_3_SPINER_FIELD = (By.ID, 'spinner')




