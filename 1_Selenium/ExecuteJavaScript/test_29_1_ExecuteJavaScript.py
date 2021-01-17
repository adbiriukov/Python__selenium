from selenium import webdriver


driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.get('http://google.com')
driver.implicitly_wait(3)

js = 'alert("Hello World")'
driver.execute_script(js)
