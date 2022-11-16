"""
Модуль для заполнения таблиц для каждой игры
"""

import sqlite3
from body.games_dict import dict_games_with_prices
from body.search_names_2 import full_dict

base = sqlite3.connect('Tesera_Top2.db')  # соединение с базой Top900
base2 = sqlite3.connect('Games4.db')  # соединение с базой по продаже игр
cur = base.cursor()
cur2 = base2.cursor()

dict_games = full_dict
for post_id in dict_games:
    for game in dict_games[post_id][1][0]:
        cur.execute('SELECT title FROM data WHERE title LIKE "%{}%"'.format(game))
        # выборка из базы Тесера по названию игры
        name_tuple = cur.fetchone()  # находит первое совпадение
        if name_tuple:
            name = name_tuple[0]
            date = dict_games[post_id][0]
            text = dict_games[post_id][2]
            try:
                cur2.execute(f'INSERT INTO "{name}" (id, name, date, text) '
                             f'VALUES ("{post_id}", "{name}", "{date}", "{text}")')
            except Exception as ex:
                pass

        # запись названия игры в таблицу data
base2.commit()  # запись изменений
