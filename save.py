import sqlite3

# Подключение к базе данных или создание новой базы данных, если она не существует
conn = sqlite3.connect('my_database.db')

# Создание курсора - это объект, который используется для взаимодействия с базой данных
cursor = conn.cursor()

# Создание таблицы, если она еще не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Пример данных, которые мы хотим сохранить
user_data = [
    ('Alice', 25),
    ('Bob', 30),
    ('Charlie', 22)
]

# Вставка данных в таблицу
cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', user_data)

# Сохранение изменений
conn.commit()

# Закрываем соединение с базой данных
conn.close()
