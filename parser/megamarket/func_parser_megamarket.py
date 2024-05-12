import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def find_url_cart_megamarket(element):
    # Ищем первый тег 'a' внутри переданного элемента
    link = element.find('a')
    # Проверяем, что тег 'a' был найден и это действительно тег, а не что-то другое
    if link and hasattr(link, 'get'):
        href = link.get('href')
        if href:  # Проверяем, что атрибут 'href' существует
            print(f"Ссылка - {href}")


def find_name_cart_megamarket(element):
    names = element.select('.item-block .item-info .item-title:not(.empty)')
    for name in names:
        # Для каждого элемента в списке извлекаем текст с помощью метода get_text()
        print(f"Название - {name.get_text(strip=True)}")


def find_price_cart_megamarket(element):
    prices = element.select('.item-block .item-info .inner.catalog-item-mobile__prices-container .item-price')
    if prices:
        for price in prices:
            print(f"Цена - {price.get_text(strip=True)}")
    else:
        print("Товара нет в наличии")


def find_cashback_cart_megamarket(element):
    cashbacks = element.select('.item-block .item-info .inner.catalog-item-mobile__prices-container .item-bonus')
    if cashbacks:
        for cashback in cashbacks:
            print(f"Кэшбек - {cashback.get_text(strip=True)}")
    else:
        print("Кэшбека нет!")

