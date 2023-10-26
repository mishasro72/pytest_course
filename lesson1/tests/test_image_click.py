# автотест для проверки перехода к карточке товара по клику по его картинке на сайте https://www.saucedemo.com/
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://www.saucedemo.com/' # для этого сайта у нас есть данные для авторизации:
                                       
login = 'standard_user' # валидный логин 
password = 'secret_sauce' # валидный пароль

driver = webdriver.Chrome() # создаем новый элемент веб-драйвера 
                            # для браузера Chrome. Можно выбрать любой другой браузер

def test_image_click():
    driver.get(BASE_URL) # подгружаем данные страницы

    # авторищация на сайте
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]') # находим поля ввода имени пользоватля на странице
    username_field.send_keys('standard_user') # даем команду на заполнение имени пользователя

    userpassword_field = driver.find_element(By.XPATH, '//input[@data-test = "password"]') # находим поле ввода пароля
    userpassword_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@data-test = "login-button"]')
    login_button.click()

    # клик по картинке изображения

    img_button = driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Bolt T-Shirt"]')
    img_button.click()

    time.sleep(3)
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=1'

    driver.quit()
