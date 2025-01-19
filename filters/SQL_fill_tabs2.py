"""
Модуль для заполнения таблиц для каждой игры.
Заполняет столбцы с датой, ценой, и текстом поста.
"""

import sqlite3
from body.searching_prices4 import full_dict

base = sqlite3.connect('../SQL/Tesera_Top3.db')  # соединение с базой Top900
base2 = sqlite3.connect('Games5_3.db')  # соединение с базой по продаже игр
cur = base.cursor()
cur2 = base2.cursor()

for post_id in full_dict:
    for game in full_dict[post_id][1]:
        f_n_game = game.split()[0]
        cur.execute(f'SELECT title FROM data WHERE (title LIKE "%{f_n_game}%") OR (title2 LIKE "%{f_n_game}%")')
        # выборка из базы Тесера по названию игры
        name_tuple = cur.fetchone()  # находит первое совпадение
        if name_tuple:
            name = name_tuple[0]
            date = full_dict[post_id][0]
            price = full_dict[post_id][1][game][0]
            text = full_dict[post_id][1][game][1]
            try:
                cur2.execute('CREATE TABLE IF NOT EXISTS "{}" (id PRIMARY KEY, name, price, date, town, text)'
                             .format(name))
                cur2.execute(f'INSERT INTO "{name}" (id, name, price, date, text) '
                             f'VALUES ("{post_id}", "{name}", "{price}", "{date}", "{text}")')
            except Exception as ex:
                print(ex)
        else:
            print(game, "нет в Топ 900 Тесеры")

base2.commit()  # запись изменений
