import pytest
from selenium import webdriver

# pytest --browser=chrome
# pytest --browser=firefox


def pytest_addoption(parser):
    """
    Метод добавляет кастомные ключи в запуск тестов
    Ключи:
    --browser: chrome/firefox - браузер для тестирования
    :param parser: парсер ключей pytest
    """
    parser.addoption('--browser', action='store',
                     default='chrome')


@pytest.fixture()
def web_driver(request):
    """
    Инициализация веб драйвера в зависимости от ключа "--browser"
    :return: объект класса webdriver
    """
    browser = request.config.getoption('--browser')

    if browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.implicitly_wait(20)
    request.addfinalizer(driver.quit)
    return driver
