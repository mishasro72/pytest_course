from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://www.saucedemo.com/'
login = 'standard_user'
password = 'secret_sauce'
driver = webdriver.Chrome()


def test_add_cart():
 
    driver.get(BASE_URL)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]') 
    username_field.send_keys(login)
    userpassword_field = driver.find_element(By.XPATH, '//input[@data-test = "password"]') 
    userpassword_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//input[@data-test = "login-button"]')
    login_button.click()

    time.sleep(3)
    item_field = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-backpack"]') # находим кнопку добавления в карзину
    item_field.click() # кликаем по кнопке, добавляя в корзину
    
    cart_field = driver.find_element(By.XPATH, '//*[@class ="shopping_cart_badge"]') # находим значек корзины
    assert cart_field.text == '1' # проверяем, что один товар добавился

    driver.quit()
 



