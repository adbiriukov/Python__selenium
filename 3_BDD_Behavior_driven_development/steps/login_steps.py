from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome Browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(
        executable_path="../chromedriver.exe")


@when(u'I open orange hrm homepage')
def open_home_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter username "{user}" and password "{pwd}"')
def enter_password(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when(u'Click on login button')
def click_on(context):
    context.driver.find_element_by_id("btnLogin").click()


@then(u'User must successfully login to the Dashboard page')
def assert_result(context):
    text = context.driver.find_element_by_link_text('Leave')
    assert text.is_displayed()
