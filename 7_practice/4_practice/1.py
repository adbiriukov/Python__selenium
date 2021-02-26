# welcome_text_elm = driver.find_element_by_tag_name("h1")
# welcome_text = welcome_text_elm.text
#
# assert "Congratulations! You have successfully registered!" == welcome_text


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.get('https://formy-project.herokuapp.com/form')


def form_submission_test():
    before()
    submit_form()
    wait_until_alert()
    assert get_text().text == 'The form was successfully submitted!'
    time.sleep(5)
    tear_down()


def submit_form():
    driver.find_element_by_id('first-name').send_keys('test1')
    driver.find_element_by_id('last-name').send_keys('test2')
    driver.find_element_by_id('job-title').send_keys('tester')
    driver.find_element_by_id('radio-button-3').click()
    driver.find_element_by_id('checkbox-1').click()
    driver.find_element_by_id('select-menu').click()
    driver.find_element_by_xpath('//*[@id="select-menu"]/option[3]').click()
    driver.find_element_by_id('datepicker').send_keys('01/11/2020')
    driver.find_element_by_id('datepicker').send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/form/div/div[8]/a').click()


def wait_until_alert():
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div/div')))


def get_text():
    return driver.find_element_by_xpath('/html/body/div/div')


def before():
    driver.maximize_window()


def tear_down():
    driver.quit()


if __name__ == '__main__':
    form_submission_test()
