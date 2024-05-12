import sqlite3
import os


def create_base(search):
    # Подключаемся к базе данных (если файла нет, он будет создан)
    conn = sqlite3.connect(f"{search}.db")  # Исправленное подключение к базе данных
    cursor = conn.cursor()

    # Создаем новую таблицу (если она уже существует, SQLite не будет ничего делать)
    cursor.execute('''CREATE TABLE IF NOT EXISTS bd (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        cashback REAL,
        final_price REAL,
        url TEXT)''')
    conn.commit()

    # Закрываем соединение
    conn.close()


def write_in_bd(search, url, name, price, cashback, final_price):
    conn = sqlite3.connect(f'{search}.db')
    cursor = conn.cursor()
    # Убедитесь, что final_price преобразуется в float корректно, иначе очистите строку от нечисловых символов
    cursor.execute("INSERT INTO bd (name, price, cashback, url, final_price) VALUES (?, ?, ?, ?,?)",
                   (name, price, cashback, url, final_price))
    conn.commit()
    conn.close()