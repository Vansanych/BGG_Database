import sqlite3
from BNI import list_main

base = sqlite3.connect('../files/Data_BNI.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS data(ID PRIMARY KEY, Text)')
base.commit()

cur.executemany('INSERT INTO data VALUES(?, ?)', (list_main))
base.commit()
