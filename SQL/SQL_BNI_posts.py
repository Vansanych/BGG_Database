"""
Создает базу постов БНИ
"""

import sqlite3
from body.get_list_post_text import post_dict  # импорт текста постов

base = sqlite3.connect(fr'../SQL/BNI_posts.db')  # создание базы
cur = base.cursor()
base.execute(f'CREATE TABLE IF NOT EXISTS data (id PRIMARY KEY, date, post)')  # создание столбцов таблицы

for post in post_dict:
    try:
        cur.execute(f'INSERT INTO data (id, date, post) '
                    f'VALUES("{post}", "{post_dict[post][0]}", "{post_dict[post][1]}")')
    except Exception as ex:
        print(ex)
    # заполнение таблицы
base.commit()
