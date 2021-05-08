import pytest



def test_open_page(web_driver):
    web_driver.get("https://www.google.com/")
    print(web_driver.title)

