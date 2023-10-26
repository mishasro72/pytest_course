# автотест для проверки авторизации пользователя на сайте https://www.saucedemo.com/
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://www.saucedemo.com/' # для этого сайта у нас есть данные для авторизации:
                                        # username = 'standart_user'
                                        # password = 'secret_sauce'
login = 'standard_user' # валидный логин 
password = 'secret_sauce' # валидный пароль

driver = webdriver.Chrome() # создаем новый элемент веб-драйвера 
                            # для браeзера Chrome. Можно выбрать любой другой браузер

def test_login_positive():
    driver.get(BASE_URL) # подгружаем данные страницы

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]') # находим поля ввода имени пользоватля на странице
    username_field.send_keys('standard_user') # даем команду на заполнение имени пользователя

    userpassword_field = driver.find_element(By.XPATH, '//input[@data-test = "password"]') # находим поле ввода пароля
    userpassword_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@data-test = "login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html' # проверяем что мы зашли на страиницу, которая открывается при учпешной авторизации

    driver.quit()
