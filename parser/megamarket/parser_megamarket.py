import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from SQL.sql_func import *
from .func_parser_megamarket import *

# Коммент для теста

def parser_megamarket(search):
    # Создаём экземпляр веб-драйвера
    driver = webdriver.Chrome()

    # SQL
    create_base(search)
    count_elements = 1
    count_url = 0
    while count_elements != 0:

        count_url += 1
        new_url = search.replace(" ", "%20")
        print(new_url)
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
        count_elements = 0
        # Поиск данных на странице
        for element in elements:
            count_elements += 1
            url = find_url_cart_megamarket(element)
            name = find_name_cart_megamarket(element)
            price = find_price_cart_megamarket(element)
            cashback = find_cashback_cart_megamarket(element)
            final_price = price - cashback
            write_in_bd(search, url, name, price, cashback, final_price)
        print(f"Количество элементов на странице {count_url} - {count_elements}")
    # Закрываем драйвер браузера
    driver.quit()

    print(f"Функция парсера мегамаркета отработала")
