from selenium.webdriver.common.by import By

class HeroPagesLocators:
    """Locators for HeroPage"""
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

    # Form authentication
    LOCATOR_PAGE_21_USERNAME_FIELD = (By.NAME, 'username')
    LOCATOR_PAGE_21_PASSWORD_FIELD = (By.NAME, 'password')
    LOCATOR_PAGE_21_SUBMIT_BT = (By.XPATH, '//*[@id="login"]/button/i')
    LOCATOR_PAGE_21_SUCCESS_MS = (By.XPATH, '//*[@id="flash"]')

    # iframes
    LOCATOR_PAGE_22_IFRAMES_LINK = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/a')
    LOCATOR_PAGE_22_LEFT_IFRAME = (By.XPATH, '/html/frameset/frame[1]')
    LOCATOR_PAGE_22_MIDDLE_IFRAME  = (By.XPATH, '/html/frameset/frame[2]')
    LOCATOR_PAGE_22_RIGHT_IFRAME = (By.XPATH, '/html/frameset/frame[3]')
    LOCATOR_PAGE_22_BOTTOM_IFRAME = (By.XPATH, '/html/body')

    # Slider
    LOCATOR_PAGE_24_SLIDER = (By.XPATH, '//*[@id="content"]/div/div/input')
    LOCATOR_PAGE_24_SLIDER_NUMBER = (By.XPATH, '//*[@id="range"]')

    # Hover
    LOCATOR_PAGE_25_HOVER_USER_1 = (By.XPATH, '//*[@id="content"]/div/div[1]/img')
    LOCATOR_PAGE_25_VIEW_PROFILE = (By.XPATH, '//*[@id="content"]/div/div[1]/div/a')
    LOCATOR_PAGE_25_VIEW_PROFILE_CODE = (By.XPATH, '/html/body/h1')

    # input
    LOCATOR_PAGE_27_INPUT_FIELD = (By.XPATH, '//*[@id="content"]/div/div/div/input')

    # jquery ui menu
    LOCATOR_PAGE_28_ENABLED_JQ = (By.XPATH, '//*[@id="ui-id-3"]/a')
    LOCATOR_PAGE_28_DOWNLOADS_JQ = (By.XPATH, '//*[@id="ui-id-4"]/a')
    LOCATOR_PAGE_28_PDF_JQ = (By.XPATH, '//*[@id="ui-id-5"]/a')

    # JavaScript Alerts
    LOCATOR_PAGE_29_JS_ALERT = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
    LOCATOR_PAGE_29_JS_ALERT_CONFIRM = (By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')

    # Large & Deep DOM
    LOCATOR_PAGE_32_LARGE_PAGE_DOM = (By.XPATH, '//*[@id="large-table"]/tbody/tr[11]/td[16]')

    # Opening a new window
    LOCATOR_PAGE_33_OPEN_NEW_WINDOW = (By.XPATH, '//*[@id="content"]/div/a')
    LOCATOR_PAGE_33_NEW_WINDOW_TEXT = (By.XPATH, '/html/body/div/h3')

    # Notification Message
    LOCATOR_PAGE_35_NOTIFICATION_MESSAGE = (By.ID, 'flash')

    # Sortable data tables
    LOCATOR_PAGE_41_TABLES_EMAIL = (By.XPATH, '//*[@id="table1"]/thead/tr/th[3]/span')
    LOCATOR_PAGE_41_DUE = (By.XPATH, '//*[@id="table1"]/thead/tr/th[4]')

