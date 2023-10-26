# тест проверки оформления заказа
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

BASE_URL = 'https://www.saucedemo.com/'
login = 'standard_user'
password = 'secret_sauce'
driver = webdriver.Chrome()
first_name = 'Ivan'
last_name = 'Bunin'
zip_code = '27523'


def test_checkout():
 
    driver.get(BASE_URL)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]') 
    username_field.send_keys(login)
    userpassword_field = driver.find_element(By.XPATH, '//input[@data-test = "password"]') 
    userpassword_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//input[@data-test = "login-button"]')
    login_button.click()

    time.sleep(3)
    item_field_1= driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]') # находим кнопку добавления второго товара в корзину
    name_item = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']").text # записываем имя товара, добавленного в корзину
    item_field_1.click() # кликаем по кнопке, добавляя товар в корзину

    cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart_button.click()

    #time.sleep(3)
    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="checkout"]')
    checkout_button.click()

    # заполнение данных для оформления покупки
    first_name_field = driver.find_element(By.ID,'first-name')
    first_name_field.send_keys(first_name)

    last_name_field = driver.find_element(By.ID,'last-name')
    last_name_field.send_keys(last_name)

    zip_code_field = driver.find_element(By.ID,'postal-code')
    zip_code_field.send_keys(zip_code)

    continue_button = driver.find_element(By.XPATH, "//input[@data-test='continue']")
    continue_button.click()

    current_item = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
    assert current_item.text == name_item # проверяем, что оформляемый товар соответсвует тому, что мы добавляли в корзину

    finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish_button.click()

    # проверка того, что Checkout: Complete!
    assert driver.find_element(By.XPATH, "//span[@class='title']").text == 'Checkout: Complete!'

    time.sleep(1)
    driver.quit()
