# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

success = True

@given('we have driver installed')
def step_impl(context):
    context.wd = webdriver.Remote("http://34.248.85.28:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX.copy())
    pass

@when('we implement a test')
def step_impl(context):
   def is_alert_present(wd):
     try:
        def step_impl(context):
            context.wd.switch_to_alert().text
            return True
     except:
        return False

@then('behave will test it for us!')
def step_impl(context):
   try:
           context.wd.get("https://www.gov.uk/search?q=home+office/")
           context.wd.find_element_by_xpath("//ol[@id='js-live-search-results']/li/h3/a/mark[2]").click()

           context.wd.get_screenshot_as_file('/behave/screenshot.png')

           assert context.failed is False

   finally:
        context.wd.quit()
        if not success:
            raise Exception("Test failed.")

