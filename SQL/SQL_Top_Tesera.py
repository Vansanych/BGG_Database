import sqlite3
import json
# from logpas import x

base = sqlite3.connect('Tesera_Top.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}(idBGG, title)'.format('data'))
base.commit()

# cur.executemany('INSERT INTO data VALUES(?, ?)', (x))
# base.commit()

for name in range(60):
    with open(fr'../TeseraTop1000/{name}.json') as file:
        g = json.load(file)
        for r in range(len(g)):
            cur.execute('INSERT INTO data VALUES(?, ?)', (g[r]['bggId'], g[r]['title']))
            base.commit()
