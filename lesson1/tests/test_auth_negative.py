# автотест для негативной проверки авторизации пользователя на сайте https://www.saucedemo.com/
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://www.saucedemo.com/' # для этого сайта у нас есть данные для авторизации:
                                        # username = 'standart_user'
                                        # password = 'secret_sauce'
login = 'user'
password = 'user'

driver = webdriver.Chrome() # создаем новый элемент, загружая веб-драйвер 
                            # для браeзера Chrome. Можно выбрать любой другой браузер

def test_login_negative():
    driver.get(BASE_URL) # подгружаем данные страницы

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]') # находим поля ввода имени пользоватля на странице
    username_field.send_keys(login) # даем команду на заполнение некорректным имени пользователя

    userpassword_field = driver.find_element(By.XPATH, '//input[@data-test = "password"]') # находим поле ввода пароля
    userpassword_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//input[@data-test = "login-button"]')
    login_button.click()

    time.sleep(5)
    #assert driver.current_url == 'https://www.saucedemo.com/inventory.html' # проверяем что мы зашли на страиницу, которая открывается при учпешной авторизации
    log_error = driver.find_element(By.XPATH, '//*[@data-test="error"]')
    #print(log_error.text)
    assert log_error.text == 'Epic sadface: Username and password do not match any user in this service'
    driver.quit()

#login_negative
