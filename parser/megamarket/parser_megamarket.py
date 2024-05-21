import  requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from SQL.sql_func import view_base, create_base
import time

from SQL.sql_func import *
from .func_parser_megamarket import *


# Коммент для теста

def parser_megamarket(search):
    # Создаём экземпляр веб-драйвера
    driver = webdriver.Chrome()
    all_elemenets = 0
    # SQL
    create_base(search)
    count_elements = 1
    count_url = 0
    redirect_fact = 0
    dublicate = 0
    while count_elements != 0:
        search = search.replace(" ", "%20")
        count_url += 1
        if redirect_fact == 0 or redirect_fact == False:
            url = (f'https://megamarket.ru/catalog/page-{count_url}/?q={search}')

        # Открываем страницу с помощью Selenium
        driver.get(url)

        # Ожидаем несколько секунд, чтобы убедиться, что страница полностью загружена
        time.sleep(1)  # Пауза в  секунд

        # Получаем исходный код страницы
        html = driver.page_source

        # Проверка на редирект
        current_url = driver.current_url

        if redirect_fact == 0:
            url_space = url.replace(" ", "%20")
            # print("url_space = ", url_space)
            # print(url)
            if url == current_url or url == url_space:
                print("Страница совпадает")
                redirect_fact = False
            else:
                print("Был редирект")
                # count_url += 1
                parts = current_url.split("#")

                url = f"{parts[0]}page-{count_url}/#{parts[1]}"
                redirect_fact = True
                continue
        if redirect_fact == True:
            parts = current_url.split("/")
            for i, part in enumerate(parts):
                if part.startswith("page-"):
                    parts[i] = f"page-{count_url}"
                    break
            else:
                parts.insert(-1, f"page-{count_url}")
            url = "/".join(parts)

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
            url_card = find_url_cart_megamarket(element)
            name = find_name_cart_megamarket(element)
            price = find_price_cart_megamarket(element)
            if price == 0:
                continue
            cashback = find_cashback_cart_megamarket(element)
            final_price = price - cashback
            search_bd = search.replace("%20", "_")

            # Проверка на дубликат в БД
            if find_dublicate(search_bd, name, price, cashback, url_card):
                dublicate += 1
                if dublicate == 10:
                    break
            else:
                write_in_bd(search_bd, url_card, name, price, cashback, final_price)
                count_elements += 1
                all_elemenets += 1

        print(f"Количество элементов на странице {count_url} - {count_elements}")

    # Закрываем драйвер браузера
    driver.quit()
    print(f"Функция парсера мегамаркета отработала")
    message = f"Поиск по Мегамаркету выполнен, найдено {all_elemenets} товара \n Дубликатов найдено {dublicate}"
    return message
