import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .func_parser_megamarket import *


def parser_megamarket_captcha(search):

    # Настраиваем опции Chrome для режима headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Указываем, что браузер должен быть headless
    chrome_options.add_argument("--disable-gpu")  # Эта опция обычно необходима для headless
    chrome_options.add_argument("--no-sandbox")  # Эта опция обходит операционную систему sandbox
    chrome_options.add_argument("--disable-dev-shm-usage")  # Эта опция предотвращает использование файловой системы /dev/shm

    # Создаём экземпляр веб-драйвера
    driver = webdriver.Chrome(options=chrome_options)
    count_url = 0
    while count_url < 10:

        count_url += 1

        # URL веб-страницы
        url = (f'https://megamarket.ru/catalog/page-{count_url}/?q={search}')
        print(url)

        # Открываем страницу с помощью Selenium
        driver.get(url)

        # Ожидаем несколько секунд, чтобы убедиться, что страница полностью загружена
        time.sleep(1)  # Пауза в  секунд

        # Получаем исходный код страницы
        html = driver.page_source

        # создание объекта BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        elements = soup.select(
            '.app-layout-default .app__main .catalog-default '
            '.catalog-default__container .catalog-default__department-container '
            '.catalog-listing .container .catalog-listing-content '
            '.r .catalog-items-list '
            '.catalog-item-mobile.ddl_product'
        )

        # Теперь используем эту функцию в цикле
        for element in elements:
            find_url_cart_megamarket(element)
            find_name_cart_megamarket(element)
            find_price_cart_megamarket(element)
            find_cashback_cart_megamarket(element)
            print("++++++++++++++++++++++++++++")
        with open('page.html', 'w', encoding='utf-8') as file:
            file.write(html)
            print("Файл сохранён")

    # Закрываем драйвер браузера
    driver.quit()

    print(f"Функция парсера мегамаркета отработала")
