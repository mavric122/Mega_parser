import tkinter as tk
from tkinter import ttk, BOTH, messagebox
from logging import getLogger

from GUI.gui_func import label_find_name, dinamic_text, create_treeview, view_base

logger = getLogger(__name__)

def main_menu():
    # Создание главного окна
    root = tk.Tk()
    root.title("MegaParser")
    root.geometry("800x600")

    # Приветствие
    label = tk.Label(root, text="Добро пожаловать в MegaParser!", font=("Arial", 18))
    label.pack(pady=20)

    # создаем набор вкладок
    notebook = ttk.Notebook()
    notebook.pack(expand=True, fill=BOTH)

    # создаем пару фреймвов
    all_shop_frame = ttk.Frame(notebook)
    megamarket_frame = ttk.Frame(notebook)
    yandex_frame = ttk.Frame(notebook)
    ozon_frame = ttk.Frame(notebook)
    wb_frame = ttk.Frame(notebook)

    all_shop_frame.pack(fill=BOTH, expand=True)
    megamarket_frame.pack(fill=BOTH, expand=True)
    yandex_frame.pack(fill=BOTH, expand=True)
    ozon_frame.pack(fill=BOTH, expand=True)
    wb_frame.pack(fill=BOTH, expand=True)

    # добавляем фреймы в качестве вкладок
    notebook.add(all_shop_frame, text="Все магазины")
    notebook.add(megamarket_frame, text="Мегамаркет")
    notebook.add(yandex_frame, text="Яндекс")
    notebook.add(ozon_frame, text="OZON")
    notebook.add(wb_frame, text="Wildberries")

    # Вкладка все магазины label_find_name
    label_find_name(all_shop_frame)


    label_find_name(megamarket_frame)


    root.mainloop()


if __name__ == "__main__":
    main_menu()
