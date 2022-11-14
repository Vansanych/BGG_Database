"""
Модуль для заполнения таблиц для каждой игры
"""

import sqlite3
from body.games_dict import dict_games_with_prices

base = sqlite3.connect('Tesera_Top2.db')  # соединение с базой Top900
base2 = sqlite3.connect('Games3.db')  # соединение с базой по продаже игр
cur = base.cursor()
cur2 = base2.cursor()

dict_games = dict_games_with_prices()
for post in dict_games:
    for game in dict_games[post]:
        cur.execute('SELECT title FROM data WHERE title LIKE "%{}%"'.format(game))
        # выборка из базы Тесера по названию игры
        name_tuple = cur.fetchone()  # находит первое совпадение
        price = dict_games[post][game]
        if name_tuple and price:
            print(game)
            name = name_tuple[0]
            print(name, price)

            cur2.execute(f'INSERT INTO "{name}" (name, price) VALUES ("{name}", "{price}")')
            # запись названия игры в таблицу data
base2.commit()  # запись изменений
