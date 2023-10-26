from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://www.saucedemo.com/'
login = 'standard_user'
password = 'secret_sauce'
driver = webdriver.Chrome()


def test_romove_item_from_card_item():
 
    driver.get(BASE_URL)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]') 
    username_field.send_keys(login)
    userpassword_field = driver.find_element(By.XPATH, '//input[@data-test = "password"]') 
    userpassword_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//input[@data-test = "login-button"]')
    login_button.click()

    time.sleep(3)
    #driver.get(driver.current_url) # обновляем данные текущей страницы/это не обязательно
    item_field = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-backpack"]') # находим кнопку добавления в корзину
    item_field.click() # кликаем по кнопке, добавляя в корзину

    time.sleep(3)
    item_field_1= driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-bike-light"]') # находим кнопку добавления второго товара в корзину
    item_field_1.click() # кликаем по кнопке, добавляя в корзину
    
    time.sleep(3)
    remove_button = driver.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']") # находим кнопку адаления товара из корзины
    remove_button.click() # кликаем по кнопке удаления товра из корзины
        
    cart_field = driver.find_element(By.XPATH, '//*[@class ="shopping_cart_link"]') # находим значек корзины
    assert cart_field.text == '1' # проверяем, что в корзине остался один товар

    driver.quit()
 




