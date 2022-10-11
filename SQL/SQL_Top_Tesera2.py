import sqlite3
import json


base = sqlite3.connect('Tesera_Top2.db')
cur = base.cursor()

with open(fr'../TopList/Top900_1.json') as file:
    g = json.load(file)
key_list = [key for key in g[0].keys()]
str_key_list = ', '.join([x for x in key_list])

base.execute(f'CREATE TABLE IF NOT EXISTS data ({str_key_list})')
base.commit()

for r in range(len(g)):
    values_list = []
    for value in g[r].values():
        values_list.append(value)
    print(r)
    cur.execute(f'INSERT INTO data VALUES({", ".join("?"*len(g[r]))})', values_list)
    base.commit()
