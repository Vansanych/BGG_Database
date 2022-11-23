"""
Модуль для заполнения сводных данных (количество продаж, цены) для каждой игры по базе БНИ
"""

import sqlite3

base = sqlite3.connect('../SQL/Tesera_Top3.db')  # соединение с базой Top900
base2 = sqlite3.connect('Games4.db')  # соединение с базой по продаже игр
cur = base.cursor()
cur2 = base2.cursor()
cur2.execute("SELECT name FROM sqlite_master WHERE type='table'")  # выбор всех названий таблиц в базе
base.execute('CREATE TABLE IF NOT EXISTS summary (id PRIMARY KEY, name, amount, med_price)')
# создание сводной таблицы со средней ценой и количеством записей

all_names = cur2.fetchall()  # создание списка всех имен таблиц базы БНИ
for name in all_names:
    cur.execute(f'SELECT id FROM data WHERE title = "{name[0]}"')  # здесь нужно взять id из первой таблицы
    id1 = cur.fetchone()
    cur2.execute(f'SELECT * FROM "{name[0]}"')  # выбор всех записей из таблицы одной игры
    count = cur2.fetchall()  # создание списка записей из таблицы одной игры
    if count:
        amount = len(count)
        try:
            cur.execute(f'INSERT INTO summary (id, name, amount) VALUES ("{id1[0]}", "{name[0]}", "{amount}")')
        except:
            pass

base.commit()  # запись изменений
