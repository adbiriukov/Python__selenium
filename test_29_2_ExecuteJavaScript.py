from selenium import webdriver


driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("http://stackoverflow.com/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
