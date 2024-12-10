# import sqlite3
# # Путь к базе данных
# db_path = "C:\FAKE_BOT-main\main_db\confidence.db"
# # import top_authors
# # top_authors.checklist()
# # Подключение к базе данных
# connection = sqlite3.connect(db_path)
# cursor = connection.cursor()

# # Название таблицы
# table_name = "authors"

# # Запрос на выбор первых 1000 строк
# cursor.execute(f"SELECT * FROM {table_name} LIMIT 1000 OFFSET 0;")  # OFFSET 0 означает, что начинаем с первой записи
# rows = cursor.fetchall()

# # Вывод данных
# if rows:
#     print(f"Первые 1000 записей из таблицы '{table_name}':")
#     for row in rows:
#         print(row)
# else:
#     print(f"Таблица '{table_name}' пуста или запрос не дал результата.")

# # Закрываем соединение
# connection.close()

import sqlite3

# Путь к вашей базе данных
db_path = "C:\FAKE_BOT-main\main_db\confidence.db"

# Подключение к базе данных
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Название таблицы, которую вы хотите просмотреть
table_name = "authors"

# Запрос на получение данных из таблицы
cursor.execute(f"SELECT * FROM {table_name};")
rows = cursor.fetchall()

# Вывод содержимого таблицы
if rows:
    print(f"Содержимое таблицы '{table_name}':")
    for row in rows:
        print(row)
else:
    print(f"Таблица '{table_name}' пуста.")

# Закрываем соединение
connection.close()
