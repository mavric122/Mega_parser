import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def parser_megamarket(name):
    # Создаём экземпляр веб-драйвера
    driver = webdriver.Chrome()

    # URL веб-страницы
    url = 'https://megamarket.ru/catalog/?q=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA'

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

    for element in elements:
        # Ищем первый тег 'a' внутри текущего элемента
        link = element.find('a')
        # Проверяем, что тег 'a' был найден и это действительно тег, а не что-то другое
        if link and hasattr(link, 'get'):
            href = link.get('href')
            if href:  # Проверяем, что атрибут 'href' существует
                print(href)

        print("++++++++++++++++++++++++++++")

    # Закрываем драйвер браузера
    driver.quit()

    print(f"Функция парсера мегамаркета отработала")
