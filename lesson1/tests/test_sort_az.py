# автотест для проверки сортировки A-Z на сайте https://www.saucedemo.com/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import espected_conditions as EC
import time

BASE_URL = 'https://www.saucedemo.com/' # для этого сайта у нас есть данные для авторизации:
                                        # username = 'standart_user'
                                        # password = 'secret_sauce'
login = 'standard_user' # валидный логин 
password = 'secret_sauce' # валидный пароль



driver = webdriver.Chrome() # создаем новый элемент веб-драйвера 
                            # для браeзера Chrome. Можно выбрать любой другой браузер

def test_sort_az():
    driver.get(BASE_URL) # подгружаем данные страницы

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]') # находим поля ввода имени пользоватля на странице
    username_field.send_keys('standard_user') # даем команду на заполнение имени пользователя

    userpassword_field = driver.find_element(By.XPATH, '//input[@data-test = "password"]') # находим поле ввода пароля
    userpassword_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, '//input[@data-test = "login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html' # проверяем что мы зашли на страиницу, которая открывается при учпешной авторизации

    sort_button = driver.find_element(By.XPATH, "//span[@class='select_container']")#"//select[@class='product_sort_container']")
    sort_button.click()
   # sort_button.send_keys(Keys.DOWN)
    time.sleep(3)
    #sort_button.send_keys(Keys.DOWN)
    # time.sleep(3)
    #sort_button.send_keys(Keys.ENTER)
    az_button=driver.find_element(By.XPATH, "//option[@value='az']") # находим кнопку сортировки A-Z
    az_button.click() # кликаем по ней
    #az_button=driver.find_element(By.XPATH, "//option[@value='za']")
    #az_button.click()
    
    time.sleep(3)
    item_1 = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    lst = []
    for i in item_1:
        lst.append(i.text)
    #lst_1 = lst
    #lst.sort(reverse=True)
    #print(lst)
    assert lst == sorted(lst) # проверяем равен ли список каталога отсортированному списку
    #assert lst_1 == lst
    driver.quit()
