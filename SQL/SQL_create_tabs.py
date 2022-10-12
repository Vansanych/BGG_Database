import sqlite3

base = sqlite3.connect('Tesera_Top2.db')  # соединение с исходной базой
cur = base.cursor()
cur.execute('SELECT title FROM data')
all_names = cur.fetchall()
for game in all_names:
    alias = game[0].split()
    print(alias)
    base.execute(f'CREATE TABLE IF NOT EXISTS {alias} (id PRIMARY KEY, name, price, date, town, text)')
    # создание столбцов таблицы
base.commit()


