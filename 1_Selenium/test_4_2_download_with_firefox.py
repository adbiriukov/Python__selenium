from selenium import webdriver
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.SaveToDisk", "text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "C:\DownloadedFiles")
fp.set_preference("browser.download.folderlist", 2)
fp.set_preference("pdfjs.disabled", True)


driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/last_try/pytest_start_2/geckodriver.exe",
                          forefox_profile=fp)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

# Download text file
driver.find_element_by_id("textbox").send_keys("testing download text file")
driver.find_element_by_id("createTxt").click()  # Generate file button
driver.find_element_by_id("link-to-download").click()

# Download pdf file
driver.find_element_by_id("pdfbox").send_keys("testing pdf file")
driver.find_element_by_id("createPdf").click()  # Generate file button
driver.find_element_by_id("pdf-link-to-download").click()
