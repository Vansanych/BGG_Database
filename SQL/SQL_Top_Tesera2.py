import sqlite3
import json


base = sqlite3.connect('Tesera_Top2.db')
cur = base.cursor()

with open(fr'../TopList/Top900_1.json') as file:
    games = json.load(file)
str_key_list = ', '.join([x for x in games[0].keys()])

base.execute(f'CREATE TABLE IF NOT EXISTS data ({str_key_list})')
base.commit()

for number, game in enumerate(games):
    print(number)
    cur.execute(f'INSERT INTO data VALUES({", ".join("?"*len(game))})', [value for value in game.values()])
    base.commit()
