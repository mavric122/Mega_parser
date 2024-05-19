from tkinter import ttk, BOTH, scrolledtext
import tkinter as tk
import time

from parser.megamarket.parser_megamarket import parser_megamarket


def dinamic_text(parent_widget, text):
    # Поле для вывода текста
    output_text = scrolledtext.ScrolledText(parent_widget, wrap=tk.WORD)
    output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10,
                     sticky="nse")  # Размещаем в четвертой строке, первом столбце
    output_text.insert(tk.END, text)  # Вставляем переданный текст
    output_text.configure(state='disabled')  # Делаем поле только для чтения


def label_find_name(shop):
    # виджет для поиска по имени
    label = ttk.Label(shop, text="Поиск по названию")
    label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  # Размещаем в первой строке, первом столбце

    # Поле ввода
    label_shop = tk.Entry(shop)
    label_shop.insert(0, "")
    label_shop.grid(row=0, column=1, padx=10, pady=10, sticky="ew")  # Размещаем во второй строке, первом столбце

    # функция поиска по кнопке
    def search_function():
        search_query = label_shop.get()
        print("Выполняем поиск по имени:", search_query)
        dinamic_text(shop, f"Выполнен поиск по имени: {search_query}")
        message = parser_megamarket(search_query)
        dinamic_text(shop, message)
        # Кнопка "Поиск"

    button_search = tk.Button(shop, text="Поиск", command=search_function)
    button_search.grid(row=0, column=2, padx=10, pady=10, sticky="ew")  # Размещаем в третьей строке, первом столбце
