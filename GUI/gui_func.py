import logging
from tkinter import ttk, BOTH, scrolledtext
import tkinter as tk
import time
import webbrowser
from logging import getLogger


from SQL.sql_func import view_base_in_table, create_excel_from_sql

from parser.megamarket.parser_megamarket import parser_megamarket


logger = getLogger(__name__)


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
        logger.info("Выполняем поиск по имени:", search_query)
        dinamic_text(shop, f"Выполнен поиск по имени: {search_query}")
        message = parser_megamarket(search_query)
        dinamic_text(shop, message)
        logger.info("Поиск выполнен")
        create_excel_from_sql(search_query)
        logger.info("Эксель типа сохранен")
        # dinamic_text(shop, message)
        # Функция показа таблицы
        # data = view_base(search_query)
        # create_treeview(data)
        # Кнопка "Поиск"

    button_search = tk.Button(shop, text="Поиск", command=search_function)
    button_search.grid(row=0, column=2, padx=10, pady=10, sticky="ew")  # Размещаем в третьей строке, первом столбце
#
# # Отрисовка таблицы
# def create_treeview(data):
#     root = tk.Tk()
#     root.title("Database Viewer")
#     root.geometry("800x600")
#
#     tree = ttk.Treeview(root)
#
#     tree['columns'] = ('id', 'name', 'price', 'cashback', 'final_price', 'url')
#
#     tree.column('#0', width=0, stretch=tk.NO)
#     tree.column('id', anchor=tk.CENTER, width=50)
#     tree.column('name', anchor=tk.W, width=200)
#     tree.column('price', anchor=tk.CENTER, width=100)
#     tree.column('cashback', anchor=tk.CENTER, width=100)
#     tree.column('final_price', anchor=tk.CENTER, width=100)
#     tree.column('url', anchor=tk.W, width=600)
#
#     tree.heading('#0', text='', anchor=tk.CENTER)
#     tree.heading('id', text='ID', anchor=tk.CENTER, command=lambda col='id': sort_column(tree, col, False))
#     tree.heading('name', text='Name', anchor=tk.CENTER, command=lambda col='name': sort_column(tree, col, False))
#     tree.heading('price', text='Price', anchor=tk.CENTER, command=lambda col='price': sort_column(tree, col, False))
#     tree.heading('cashback', text='Cashback', anchor=tk.CENTER,
#                  command=lambda col='cashback': sort_column(tree, col, False))
#     tree.heading('final_price', text='final_price', anchor=tk.CENTER,
#                  command=lambda col='final_price': sort_column(tree, col, False))
#     tree.heading('url', text='URL', anchor=tk.CENTER, command=lambda col='url': sort_column(tree, col, False))
#
#     for row in data:
#         id = tree.insert('', tk.END, values=row)
#         tree.tag_bind(id, '<1>', lambda event, row=row: open_url(row[-1]))
#         tree.tag_bind(id, '<3>', lambda event, row=row: copy_to_clipboard(row[-1]))
#
#     tree.pack(expand=True, fill=tk.BOTH)
#
#     root.mainloop()
#
# def sort_column(tv, col, reverse):
#     l = [(tv.set(k, col), k) for k in tv.get_children('')]
#     try:
#         l.sort(key=lambda t: float(t[0]), reverse=reverse)
#     except ValueError:
#         l.sort(reverse=reverse)
#
#     for index, (val, k) in enumerate(l):
#         tv.move(k, '', index)
#
#     tv.heading(col, command=lambda: sort_column(tv, col, not reverse))
#
# def open_url(url):
#     webbrowser.open_new(url)
#
# def copy_to_clipboard(url):
#     root.clipboard_clear()
#     root.clipboard_append(url)
#
# # Сортировка по полю
# def sort_column(tv, col, reverse):
#     l = [(tv.set(k, col), k) for k in tv.get_children('')]
#     try:
#         # Попробуйте преобразовать к float для числовой сортировки
#         l.sort(key=lambda t: float(t[0]), reverse=reverse)
#     except ValueError:
#         # Если не удается преобразовать к float, сортируем как строки
#         l.sort(reverse=reverse)
#
#     # переупорядочиваем элементы в дереве
#     for index, (val, k) in enumerate(l):
#         tv.move(k, '', index)
#
#     # меняем направление сортировки
#     tv.heading(col, command=lambda: sort_column(tv, col, not reverse))


