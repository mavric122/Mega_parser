from logging import getLogger

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import sqlite3


logger = getLogger(__name__)

def find_url_cart_megamarket(element):
    # Ищем первый тег 'a' внутри переданного элемента
    link = element.find('a')
    # Проверяем, что тег 'a' был найден и это действительно тег, а не что-то другое
    if link and hasattr(link, 'get'):
        href = link.get('href')
        if href:  # Проверяем, что атрибут 'href' существует
            # print(f"Ссылка - {href}")
            href = f"https://megamarket.ru{href}"
            return href


def find_name_cart_megamarket(element):
    names = element.select('.item-block .item-info .item-title:not(.empty)')
    for name in names:
        # Для каждого элемента в списке извлекаем текст с помощью метода get_text()
        name = name.get_text(strip=True)
        return name


def find_price_cart_megamarket(element):
    prices = element.select('.item-block .item-info .inner.catalog-item-mobile__prices-container .item-price')
    if prices:
        for price in prices:
            price_item = price.get_text(strip=True)
            price_item = price_item.replace(" ", "")
            price_item = price_item.replace('xa0', '').replace('₽', '')
            # Преобразование строки в float
            price_item = float(price_item)
            return price_item
    else:
        return 0


def find_cashback_cart_megamarket(element):
    cashbacks = element.select('.item-block .item-info .inner.catalog-item-mobile__prices-container .item-bonus')
    if cashbacks:
        for cashback in cashbacks:
            cashback_item = cashback.get_text(strip=True)
            cashback_item = cashback_item.replace(" ", "")
            # Преобразование строки в число с плавающей точкой
            cashback_item = float(cashback_item)
            return cashback_item
    else:
        return 0

def find_dublicate(name_bd, name, price, cashback, url):
    # Подключаемся к базе данных
    bd_name = name_bd.replace(" ", "_")
    conn = sqlite3.connect(f'temp/{bd_name}.db')
    cursor = conn.cursor()

    try:
        # Формируем SQL-запрос для поиска записи с такими же значениями
        query = """
        SELECT id, name FROM bd
        WHERE name = ? AND price = ? AND cashback = ? AND url = ?
        """

        # Выполняем запрос
        cursor.execute(query, (name, price, cashback, url))

        # Получаем результат
        result = cursor.fetchone()

        # Проверяем наличие записи
        if result:
            # print("Запись с такими же данными уже существует в базе данных.")
            return True
        else:
            # print("Запись не найдена в базе данных.")
            return False
    except sqlite3.Error as e:
        logger.error(f"Ошибка при работе с базой данных: {e}")
        return False
    finally:
        # Закрываем соединение с базой данных
        cursor.close()
        conn.close()
