import sqlite3
import json


base = sqlite3.connect('Tesera_Top.db')
cur = base.cursor()

with open(fr'../TeseraTop1000/{0}.json') as file:
    g = json.load(file)
key_list = []
for key in g[0].keys():
    key_list.append(key)
values_list = []
for value in g[0].values():
    values_list.append(value)
print(', '.join([x for x in key_list]))

base.execute('CREATE TABLE IF NOT EXISTS {}(id, teseraId, bggId, title, title2, title3, alias, descriptionShort, '
             'description, modificationDateUtc, creationDateUtc, photoUrl, year, ratingUser, n10Rating, n20Rating, '
             'bggRating, bggGeekRating, bggNumVotes, numVotes, playersMin, playersMax, playersMinRecommend, '
             'playersMaxRecommend, playersAgeMin, timeToLearn, playtimeMin, playtimeMax, commentsTotal, '
             'commentsTotalNew, isAddition)'.format('data'))
base.commit()

# cur.executemany('INSERT INTO data VALUES(?, ?)', (x))
# base.commit()

for name in range(60):
    with open(fr'../TeseraTop1000/{name}.json') as file:
        g = json.load(file)
        for r in range(len(g)):
            values_list = []
            for value in g[r].values():
                values_list.append(value)
            print(name, r)
            cur.execute('INSERT INTO data VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                        ' ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', values_list)
            base.commit()
