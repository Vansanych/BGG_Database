"""
Модуль для создания базы с пустыми таблицами для каждой игры
"""

import sqlite3

base = sqlite3.connect('Tesera_Top3.db')  # соединение с исходной базой
base2 = sqlite3.connect('../filters/Games4.db')  # соединение с новой базой
cur = base.cursor()
cur2 = base2.cursor()
cur.execute('SELECT title FROM data')  # выбирает все ячейки из колонки title на листе data
all_names = cur.fetchall()
for game in all_names:
    alias = game[0]
    print(alias)
    base2.execute('CREATE TABLE IF NOT EXISTS "{}" (id PRIMARY KEY, name, price, date, town, text)'.format(alias))
    # создание столбцов таблицы
    # cur2.execute(f'INSERT INTO {alias} VALUES({", ".join("?" * len(game))})', [value for value in game.values()])
base2.commit()


