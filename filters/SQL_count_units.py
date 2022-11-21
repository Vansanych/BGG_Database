"""
Модуль для заполнения таблиц для каждой игры
"""

import sqlite3

base2 = sqlite3.connect('Games4.db')  # соединение с базой по продаже игр
cur2 = base2.cursor()
cur2.execute("SELECT name FROM sqlite_master WHERE type='table'")
all_names = cur2.fetchall()
# base2.commit()  # запись изменений
for name in all_names:
    # print(name[0])
    cur2.execute('SELECT id FROM "{}" '.format(name[0]))
    count = cur2.fetchall()
    if count:
        print(name[0], len(count))


