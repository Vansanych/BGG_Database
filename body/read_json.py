"""
модуль забирает первое слово из названия игры. Полные названия игр в json-файлах по 15 игр с Топ Тесеры.
JSON-файлы формируются в модуле TeseraTop1000

"""

import json

first_name_rus = []
for name in range(60):
    with open(fr'../TeseraTop1000/{name}.json') as file:
        g = json.load(file)
        for r in range(len(g)):
            first_name_rus.append(g[r]['title'].split()[0].replace('.', ''))

    # print(g.keys())
    # print(g['id'], g['testerId'], g['title'], g['title2'])

with open(fr'../TopList/first_name_rus.json', 'w+') as file:
    file.write(json.dumps(first_name_rus, indent=4))

with open(fr'../TopList/first_name_rus.json') as file:
    g = json.load(file)
print([(x, y) for x, y in enumerate(g)])
# print(g)
