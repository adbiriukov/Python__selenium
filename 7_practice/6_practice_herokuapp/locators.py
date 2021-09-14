from selenium.webdriver.common.by import By

class HeroPagesLocators:
    # page Add/Remove Elements
    LOCATOR_PAGE_1_ADD_BT = (By.XPATH, '//*[@id="content"]/div/button')
    LOCATOR_PAGE_1_DEL_BT = (By.XPATH, '//*[@id="elements"]/button')

    # Basic Auth
    LOCATOR_PAGE_3_BASIC_AUTH = (By.XPATH, '//*[@id="content"]/div/p')

    # Broken images
    LOCATOR_PAGE_4_BROKEN_IMAGES = (By.CSS_SELECTOR, 'img')

    # Checkboxes
    LOCATOR_PAGE_6_CHECKBOX_1 = (By.XPATH, '//*[@id="checkboxes"]/input[1]')
    LOCATOR_PAGE_6_CHECKBOX_2 = (By.XPATH, '//*[@id="checkboxes"]/input[2]')

    # Context window
    LOCATOR_PAGE_7_CONTEXT_WINDOW = (By.ID, 'hot-spot')

    # Disappearing elements
    LOCATOR_PAGE_9_DISAPPEARING_ELEMENTS = (By.TAG_NAME, "a")

    # Drag and drop
    LOCATOR_PAGE_10_DND_1 = (By.ID, 'column-a')
    LOCATOR_PAGE_10_DND_2 = (By.ID, 'column-b')

    # Dropdown menu
    LOCATOR_PAGE_11_DROPDOWN = (By.ID, 'dropdown')

    # Dynamic content
    LOCATOR_PAGE_12_DYNAMIC_CONTENT_1 = (By.XPATH, '//*[@id="content"]/div[1]/div[2]')
    LOCATOR_PAGE_12_DYNAMIC_CONTENT_2 = (By.XPATH, '//*[@id="content"]/div[2]/div[2]')
    LOCATOR_PAGE_12_DYNAMIC_CONTENT_3 = (By.XPATH, '//*[@id="content"]/div[3]/div[2]')

    # Dynamic controls
    LOCATOR_PAGE_13_CHECKBOX = (By.XPATH, '//*[@id="checkbox"]/input')
    LOCATOR_PAGE_13_REMOVE_BT = (By.XPATH, '//*[@id="checkbox-example"]/button')
    LOCATOR_PAGE_13_ENABLE_BT = (By.XPATH, '//*[@id="input-example"]/button')
    LOCATOR_PAGE_13_TEXT_FIELD = (By.XPATH, '//*[@id="input-example"]/input')
    LOCATOR_PAGE_13_TEXT_FIELD_MESSAGE = (By.XPATH, '//*[@id="message"]')
    LOCATOR_PAGE_13_REMOVE_BT_MESSAGE = (By.XPATH, '//*[@id="message"]')

    # Adv entry
    LOCATOR_PAGE_15_CLOSE_AD = (By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p')

    # Floating menu
    LOCATOR_PAGE_19_HOME_BT = (By.XPATH, '//*[@id="menu"]/ul/li[1]/a')
    LOCATOR_PAGE_19_NEWS_BT = (By.XPATH, '//*[@id="menu"]/ul/li[2]/a')
    LOCATOR_PAGE_19_CONTACT_BT = (By.XPATH, '//*[@id="menu"]/ul/li[3]/a')
    LOCATOR_PAGE_19_ABOUT_BT = (By.XPATH, '//*[@id="menu"]/ul/li[4]/a')
