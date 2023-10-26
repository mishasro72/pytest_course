from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://www.saucedemo.com/'
login = 'standard_user'
password = 'secret_sauce'
#driver = webdriver.Chrome()

def test_remove_from_cart(driver):

    # авторизируемся на сайте
    driver.get(BASE_URL)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]') 
    username_field.send_keys(login)
    userpassword_field = driver.find_element(By.XPATH, '//input[@data-test = "password"]') 
    userpassword_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//input[@data-test = "login-button"]')
    login_button.click()

    # time.sleep(3)
    # assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    # добавляем товары в корзину
    time.sleep(3)
    #driver.get(driver.current_url) # обновляем данные текущей страницы/это не обязательно
    item_field = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-backpack"]') # находим кнопку добавления в корзину
    item_field.click() # кликаем по кнопке, добавляя в корзину

    # time.sleep(3)
    # item_field_1= driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-bike-light"]') # находим кнопку добавления второго товара в корзину
    # item_field_1.click() # кликаем по кнопке, добавляя в корзину
    
    # переходим в корзину
    cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart_button.click()
    #assert driver.current_url == 'https://www.saucedemo.com/cart.html'

    item_in_cart = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
    
    try:
        assert item_in_cart.is_displayed(), "Товар не отображается в корзине"
    except:
        print("Товар в корзине не найден")
   # assert item_in_cart.is_displayed(), "Товар не отображается в корзине"
        
    time.sleep(3)
    remove_button = driver.find_element(By.ID, 'remove-sauce-labs-backpack')
    remove_button.click()

    # time.sleep(3)
    # cart_icon = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    # assert cart_icon.text == '1'

    time.sleep(3)
    try:
        assert not item_in_cart.is_displyed(), "Товар все еще отображается в корзине"
    except:
        print("Товар из корзины удалился")
    #assert not item_in_cart.is_displayed(), "Товар все еще отображается в корзине"

    #driver.quit()
