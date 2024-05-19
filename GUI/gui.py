import tkinter as tk
from tkinter import ttk, BOTH
from tkinter import messagebox


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

    root.mainloop()

    label = tk.Label(root, text="Добро пожаловать в MegaParser!", font=("Arial", 18), anchor="w")
    label.pack(pady=40, fill="x")  # Расширение виджета по горизонтали

    # Пример виджета Button
    button = tk.Button(root, text="Начать парсинг", command=lambda: print("Парсинг начат"))
    button.pack(pady=10)

    # Запуск главного цикла обработки событий
    root.mainloop()

    # Вызов функции main_menu, если этот файл запускается как основной


if __name__ == "__main__":
    main_menu()