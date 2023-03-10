"""
Модуль для заполнения таблиц для каждой игры.
Заполняет столбцы с датой, ценой, и текстом поста.
"""

import sqlite3
from body.searching_prices4 import full_dict

base = sqlite3.connect('../SQL/Tesera_Top3.db')  # соединение с базой Top900
base2 = sqlite3.connect('Games4.db')  # соединение с базой по продаже игр
cur = base.cursor()
cur2 = base2.cursor()

dict_games = full_dict
for post_id in dict_games:
    for game in dict_games[post_id][1]:
        cur.execute('SELECT title FROM data WHERE title LIKE "%{}%"'.format(game[0]))
        # выборка из базы Тесера по названию игры
        name_tuple = cur.fetchall()  # находит первое совпадение
        if name_tuple:
            pass
            # print(1, game, name_tuple)
        else:
            cur.execute('SELECT title FROM data WHERE title2 LIKE "%{}%"'.format(game[0]))
            name_tuple = cur.fetchall()  # находит первое совпадение
            if name_tuple:
                pass
                # print(2, game, name_tuple)
            else:
                pass
                print(2, post_id, game, 'нет совпадений')



#             name = name_tuple[0]
#             date = dict_games[post_id][0]
#             price = dict_games[post_id][1][game][0]
#             text = dict_games[post_id][1][game][1]
#             try:
#                 cur2.execute(f'INSERT INTO "{name}" (id, name, price, date, text) '
#                              f'VALUES ("{post_id}", "{name}", "{price}", "{date}", "{text}")')
#             except Exception as ex:
#                 print(ex)
#         else:
#             print(game, "нет в Топ 900 Тесеры")
#
# # base2.commit()  # запись изменений
