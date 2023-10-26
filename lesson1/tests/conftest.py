import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = 'https://www.saucedemo.com/'

@pytest.fixture()
def driver():

    driver = webdriver.Chrome()
    yield driver
    print('\nQuit browser')
    driver.quit()

# def auth(driver):

#     driver.get(BASE_URL) # подгружаем данные страницы

#     username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]') # находим поля ввода имени пользоватля на странице
#     username_field.send_keys('standard_user') # даем команду на заполнение имени пользователя

#     userpassword_field = driver.find_element(By.XPATH, '//input[@data-test = "password"]') # находим поле ввода пароля
#     userpassword_field.send_keys('secret_sauce')

#     login_button = driver.find_element(By.XPATH, '//input[@data-test = "login-button"]')
#     login_button.click()

#     yield


