from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# upload file
driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame(0)
# send_keys("THERE WRITE FILE PATH, FOR EXMPL. C:///input_files/example.jpg")
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:/Users/User/Downloads/test.log")
driver.switch_to.frame('frame-one1434677811')
print(driver.find_element_by_class_name('content').text)
driver.close()


# download files
# from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\User\Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(executable_path="../chromedriver.exe",
                          options=chromeOptions)
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
driver.close()
