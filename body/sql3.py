import sqlite3
from logpas import x

base = sqlite3.connect('../files/SQL4.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY, password)'.format('data'))
base.commit()

# cur.execute('INSERT INTO data VALUES(?, ?)', ('johnny123', '123456'))
# base.commit()
#
# cur.execute('INSERT INTO data VALUES(?, ?)', ('billy', '16'))
# base.commit()
#
# cur.executemany('INSERT INTO data VALUES(?, ?)', (x))
# base.commit()

cur.execute('INSERT INTO data VALUES(?, ?)', ('johnny123', '123456'))
base.commit()
