"""
Создает базу игр по ТОП Тесеры (без дубликатов)
"""

import sqlite3
import json

base = sqlite3.connect(fr'../filters/Tesera_Top5000_1.db')  # создание базы
cur = base.cursor()

with open(fr'../TopList/Top5000_2.json') as file:
    games = json.load(file)
str_key_list = ', '.join([x for x in games[0].keys()][1:])
# создание строки с именами ключей для названия столбцов таблицы

base.execute(f'CREATE TABLE IF NOT EXISTS data (id PRIMARY KEY, {str_key_list})')  # создание столбцов таблицы

for number, game in enumerate(games):
    print(number)
    try:
        cur.execute(f'INSERT INTO data VALUES({", ".join("?"*len(game))})', [value for value in game.values()])
    except Exception as ex:
        print(ex)
    # заполнение таблицы
base.commit()
