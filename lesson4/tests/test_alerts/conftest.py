import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from faker import Faker

@pytest.fixture # фикстура настройк иобций браузера
def chrome_opt():
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--window-size=2880,1800')
    return options

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=15)
    return wait


@pytest.fixture# фикстура подгрузки драйвера Хром
def driver(chrome_opt): # перелаем фикустуру опции в наш вебдрайвер
    driver = webdriver.Chrome(options=chrome_opt) # передаем опции при инициализации драйвера
    print('Начало теста')
    yield driver
    print('\nQuit browser')
    driver.quit()

@pytest.fixture
def fake():
    fake = Faker()
    return fake


