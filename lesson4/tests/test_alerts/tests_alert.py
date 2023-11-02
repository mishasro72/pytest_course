import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import *
from locators import *
import time
from conftest import *
from faker import Faker
 

def test_alert_button(driver, wait):
   # driver = webdriver.Chrome()
    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable(ALERT_BUTTON)).click()
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(2)
    assert alert.text == 'You clicked a button'
    alert.accept()

def test_time_alert_button(driver, wait):
    #driver = webdriver.Chrome()
    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable(TIME_ALERT_BUTTON)).click()
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(1)
    assert alert.text == 'This alert appeared after 5 seconds'
    alert.accept()

def test_cancel_alert_button(driver, wait):
    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable(CONFIRM_BUTTON)).click()
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(1)
    assert alert.text == "Do you confirm action?"
    alert.dismiss()
    wait.until(EC.text_to_be_present_in_element((CONFIRM_RESULT), 'You selected Cancel'))

def test_yes_alert_button(driver, wait):
    #driver = webdriver.Chrome()
    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable(CONFIRM_BUTTON)).click()
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "Do you confirm action?"
    #time.sleep(2)
    alert.accept()
    #time.sleep(2)
    wait.until(EC.text_to_be_present_in_element((CONFIRM_RESULT), "You selected Ok"))
               
def test_promt_alert_button(driver, wait, fake):
    #driver = webdriver.Chrome()
    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable(PROMT_BUTTON)).click()
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "Please enter your name"
    text = fake.name()
    alert.send_keys(text)
    time.sleep(3)
    alert.accept()
    wait.until(EC.text_to_be_present_in_element((PROMT_RESULT), f"You entered {text}"))
    time.sleep(2)








