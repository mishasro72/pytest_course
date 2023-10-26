# автотест для проверки сортировки price High - Low на сайте https://www.saucedemo.com/
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

def test_sort_hilo():
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
    
    time.sleep(3)
    lohi_button=driver.find_element(By.XPATH, "//option[@value='hilo']") # находим кнопку сортировки по цене по убыванию
    lohi_button.click() # кликаем по ней
    
    time.sleep(3)
    item_1 = driver.find_elements(By.CLASS_NAME, 'inventory_item_price') # находим все элементы каталога товаров     
    lst = [] # создаем пустой список, куда поместим навзание товаров в порядке их нахождения в каталоге
    for i in item_1:
        lst.append(float(i.text.replace("$", ""))) # добавляем в пустой список 
                                                    # цены, сразу переводя их из строк в флоат-числа
                                                    # и убирая знак $ 
    
    #lst_1 = []
    lst_1 = sorted(lst, reverse=True) # создаем список и передаем значения списка католога товаров, отстортированный в обратном порядке
    assert lst == lst_1 # проверяем равен ли список каталога отсортированному по убыванию цены списку каталога
    
    driver.quit()
