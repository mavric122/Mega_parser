from tkinter import ttk, BOTH, scrolledtext
import tkinter as tk
import time
from SQL.sql_func import view_base

from parser.megamarket.parser_megamarket import parser_megamarket



def create_treeview(data):
    # Создание главного окна
    root = tk.Tk()
    root.title("Database Viewer")
    root.geometry("800x600")

    # Создание Treeview
    tree = ttk.Treeview(root)

    # Определение столбцов
    tree['columns'] = ('id', 'name', 'price', 'cashback', 'url')

    # Форматирование столбцов
    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('id', anchor=tk.CENTER, width=50)
    tree.column('name', anchor=tk.W, width=200)
    tree.column('price', anchor=tk.CENTER, width=100)
    tree.column('cashback', anchor=tk.CENTER, width=100)
    tree.column('url', anchor=tk.W, width=300)

    # Заголовки столбцов
    tree.heading('#0', text='', anchor=tk.CENTER)
    tree.heading('id', text='ID', anchor=tk.CENTER)
    tree.heading('name', text='Name', anchor=tk.CENTER)
    tree.heading('price', text='Price', anchor=tk.CENTER)
    tree.heading('cashback', text='Cashback', anchor=tk.CENTER)
    tree.heading('url', text='URL', anchor=tk.CENTER)

    # Вставка данных в Treeview
    for row in data:
        tree.insert('', tk.END, values=row)

    tree.pack(expand=True, fill=tk.BOTH)

    root.mainloop()


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
        data = view_base(search_query)
        print(data)
        create_treeview(data)
        # Кнопка "Поиск"

    button_search = tk.Button(shop, text="Поиск", command=search_function)
    button_search.grid(row=0, column=2, padx=10, pady=10, sticky="ew")  # Размещаем в третьей строке, первом столбце
