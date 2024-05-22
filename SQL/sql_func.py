import logging
import sqlite3
import os
from logging import getLogger

logger = getLogger(__name__)

def find_name_db(search):
    search = search.replace(" ", "_")
    count = 0
    while True:
        bd = f"{search}_{count}" if count > 0 else search
        file_path = f"./temp/{bd}.db"
        full_file_path = os.path.abspath(file_path)

        if os.path.exists(full_file_path) and os.path.isfile(full_file_path):
            logger.info(f"БД {bd}.db существует в поддиректории")
            count += 1  # Увеличиваем счетчик, чтобы попробовать следующее имя
        else:
            logger.info(f"Создана БД {bd}.db")
            break  # Выходим из цикла, если файл не найден
    return bd

def create_base(bd_name):
    bd_name = find_name_db(bd_name)
    conn = sqlite3.connect(f"temp/{bd_name}.db")
    cursor = conn.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS bd (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        cashback REAL,
        final_price REAL,
        url TEXT)''')
    conn.commit()
    conn.close()
    logger.debug("БД создана")

def write_in_bd(bd_name, url, name, price, cashback, final_price):
    bd_name = bd_name.replace(" ", "_")
    conn = sqlite3.connect(f'temp/{bd_name}.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bd (name, price, cashback, url, final_price) VALUES (?, ?, ?, ?, ?)",
                   (name, price, cashback, url, final_price))
    conn.commit()
    conn.close()

def view_base(bd_name):
    bd_name = bd_name.replace(" ", "_")
    conn = sqlite3.connect(f'temp/{bd_name}.db')
    cursor = conn.cursor()
    # Формируем SQL-запрос для получения данных
    query = """
    SELECT * FROM bd;
    """
    # Выполняем запрос
    cursor.execute(query)
    data = cursor.fetchall()
    if data:
        logger.info("Данные из базы выведены")
    else:
        logger.error("База данных пуста.")
    cursor.close()
    conn.close()
    return data

