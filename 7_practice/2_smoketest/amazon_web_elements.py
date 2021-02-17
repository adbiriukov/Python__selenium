from selenium.webdriver.common.by import By


class WebElements(object):
    # ID  of web elements
    search_field = (By.ID, 'twotabsearchtextbox')
    deliver_country = (By.ID, 'glow-ingress-line2')
    cart = (By.ID, "nav-cart")
    banner_list = (By.ID, 'desktop-banner')