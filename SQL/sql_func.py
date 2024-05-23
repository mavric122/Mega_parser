import logging
import sqlite3
import os
from logging import getLogger
from openpyxl import Workbook
import shutil

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
    logger.info("БД создана")

def write_in_bd(bd_name, url, name, price, cashback, final_price):
    bd_name = bd_name.replace(" ", "_")
    conn = sqlite3.connect(f'temp/{bd_name}.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bd (name, price, cashback, url, final_price) VALUES (?, ?, ?, ?, ?)",
                   (name, price, cashback, url, final_price))
    conn.commit()
    conn.close()

def view_base_in_table(bd_name):
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



def clear_folder(folder_path):
  """Удаляет все файлы и подпапки внутри указанной папки.

  Args:
    folder_path: Путь к папке, которую нужно очистить.
  """

  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
      if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)  # Удаляем файл или символическую ссылку
      elif os.path.isdir(file_path):
        shutil.rmtree(file_path)  # Удаляем подпапку и её содержимое
    except Exception as e:
      print(f"Ошибка при удалении {file_path}: {e}")

def create_excel_from_sql(bd_name):
    # Подключение к базе данных
    bd_name = bd_name.replace(" ", "_")
    conn = sqlite3.connect(f'temp/{bd_name}.db')

    # Создание курсора
    cursor = conn.cursor()

    # Выполнение запроса к БД
    cursor.execute("SELECT * FROM bd")  # замените 'table_name' на имя вашей таблицы

    # Получение результатов запроса
    results = cursor.fetchall()

    # Создание книги Excel
    workbook = Workbook()
    sheet = workbook.active

    # Заполнение шапки таблицы с названиями столбцов
    columns = [i[0] for i in cursor.description]
    sheet.append(columns)

    # Заполнение данных
    for row in results:
        sheet.append(row)

    # Сохранение файла Excel
    # Формирование пути к папке "Результаты" на один уровень выше
    results_folder = os.path.join("Результат")
    # Сохранение файла
    workbook.save(os.path.join(results_folder, f"{bd_name}.xlsx"))
    logger.info(f"Файл {bd_name}.xlsx сохранён.")

    # Закрытие соединения с БД
    cursor.close()
    conn.close()
    message = f"Данные сохранены в {bd_name} в папку /Результат/"
    clear_folder("temp")
    logger.info("БД удалены")
    return message

