from selenium import webdriver
from selenium.webdriver import ActionChains
import openpyxl
import time


def search_for_right_price(request, sheet_number):
    # set up
    driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
    driver.get("https://edadeal.ru/")
    driver.maximize_window()
    driver.implicitly_wait(30)

    # close rollout banner
    action = ActionChains(driver)
    rollout = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]')
    action.move_to_element(rollout).click().perform()

    # close alert
    try:
        alert = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div')
        action.move_to_element(alert).click().perform()
    except:
        print('error')

    # search for results
    time.sleep(1)
    search1 = driver.find_element_by_xpath('/html/body/div[7]/div/header/span/div/div/div/div')
    search1.click()
    time.sleep(1)
    search2 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/form/div/div/div/input')
    search2.send_keys(request)
    search2.submit()

    # # # choose stores
    # time.sleep(1)
    # all_stores = driver.find_element_by_xpath('//*[@id="view"]/div[1]/div/header/span[1]/span')
    # all_stores.click()
    # time.sleep(1)
    # verny = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div[2]')
    # verny.click()
    # five_ka = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[10]/div[2]')
    # five_ka.click()
    # kirov_sky = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[25]/div[2]/div[1]')
    # kirov_sky.click()
    # magnit = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[29]/div[2]/div[1]')
    # magnit.click()
    # monetka = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[36]/div[2]/div[1]')
    # monetka.click()
    # show = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/span')
    # show.click()
    #
    # # # sort results by price
    # driver.find_element_by_xpath('//*[@id="view"]/div[1]/div/header/span[2]').click()
    # driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]').click()

    # create list to store data
    rows = []

    # get quantity of results
    quantity = driver.find_elements_by_class_name('b-offer__root')

    # check quantity, if > 7 set to 7
    if len(quantity) > 7:
        quantity = 7
    else:
        quantity = len(quantity)

    # gather results
    for r in range(1, quantity + 1):
        store = driver.find_element_by_xpath(
            "//*[@id='view']/div[1]/div/div[2]/div/div/div/section[2]/a["+str(r)+"]/div/div/div/div[1]/div[2]/div[1]/a/img")
        print(store.get_attribute("title"))
        good1 = driver.find_element_by_xpath(
            "//*[@id='view']/div[1]/div/div[2]/div/div/div/section[2]/a["+str(r)+"]/div/div/div/div[1]/div[2]/div[1]/div")
        # print(good1.text)
        price1 = driver.find_element_by_xpath(
            "//*[@id='view']/div[1]/div/div[2]/div/div/div/section[2]/a["+str(r)+"]/div/div/div/div[1]/div[2]/div[3]/div[1]/div")
        # print(price1.text)
        item = store.get_attribute("title") + " / " + good1.text + " / " + price1.text
        rows.append(item)

    print(rows, end='        ')

    path = "./prices_data.xlsx"
    workbook = openpyxl.load_workbook(path)
    workbook.active = sheet_number
    sheet = workbook.active
    sheet.append(rows)
    workbook.save(path)


search_for_right_price("Крабовые палочки", 1)
