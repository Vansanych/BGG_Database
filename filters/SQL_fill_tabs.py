import sqlite3

base = sqlite3.connect('Tesera_Top2.db')  # соединение с базой Top900
base2 = sqlite3.connect('Games3.db')  # соединение с базой по продаже игр
cur = base.cursor()
cur2 = base2.cursor()
cur.execute('SELECT title FROM data')
all_names = cur.fetchall()
for game in all_names:
    alias = game[0].replace('"', '')
    print(alias)
    # base2.execute('CREATE TABLE IF NOT EXISTS "{}" (id PRIMARY KEY, name, price, date, town, text)'.format(alias))
    # создание столбцов таблицы
    # cur2.execute(f'INSERT INTO {alias} VALUES({", ".join("?" * len(game))})', [value for value in game.values()])
base.commit()


