import pytest
from selenium import webdriver

# pytest --browser=chrome
# pytest --browser=firefox


def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     default='chrome')
    parser.addoption('--url',
                     action='store',
                     default='https://www.google.com/')


@pytest.fixture()
def web_driver(request):
    browser = request.config.getoption('--browser')
    if browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(20)
    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption("--url"))
    return driver
