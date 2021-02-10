from selenium import webdriver


# set up
driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.get("https://www.avito.ru/ekaterinburg?q=ps+vita&s=2")
driver.maximize_window()
driver.implicitly_wait(5)

ids = ['i1918812077', '2039972848', 'i2082445324', 'i2064424452', 'i2051859285',
       'i2051859285', 'i2087452552', 'i2108706905', 'i2057260668', 'i2057260668',
       'i2003648803', 'i2039972848', 'i2050021595', '11112']

for element_id in ids:
    try:
        element = driver.find_element_by_id(element_id)
        driver.execute_script("""var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)
    except Exception:
        # print('Can\'t find id = ' + element_id)
        pass
