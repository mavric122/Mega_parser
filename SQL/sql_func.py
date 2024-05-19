import sqlite3
import os

def find_name_db(search):
    search = search.replace(" ", "_")
    count = 0
    while True:
        bd = f"{search}_{count}" if count > 0 else search
        file_path = f"./temp/{bd}.db"
        full_file_path = os.path.abspath(file_path)

        if os.path.exists(full_file_path) and os.path.isfile(full_file_path):
            print(f"БД {bd}.db существует в поддиректории")
            count += 1  # Увеличиваем счетчик, чтобы попробовать следующее имя
        else:
            print(f"Создана БД {bd}.db")
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

def write_in_bd(bd_name, url, name, price, cashback, final_price):
    bd_name = bd_name.replace(" ", "_")
    conn = sqlite3.connect(f'temp/{bd_name}.db')
    cursor = conn.cursor()
    # Здесь должно быть преобразование final_price в float
    cursor.execute("INSERT INTO bd (name, price, cashback, url, final_price) VALUES (?, ?, ?, ?, ?)",
                   (name, price, cashback, url, final_price))
    conn.commit()
    conn.close()