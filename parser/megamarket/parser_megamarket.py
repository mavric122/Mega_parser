import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

from .func_parser_megamarket import *


def parser_megamarket(search):
    # Создаём экземпляр веб-драйвера
    driver = webdriver.Chrome()
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

    # Закрываем драйвер браузера
    driver.quit()

    print(f"Функция парсера мегамаркета отработала")
