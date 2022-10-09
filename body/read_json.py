"""
read_json модуль забирает первое слово из названия игры Тесеры.
Полные названия игр в json-файлах по 15 игр с Топ Тесеры.
JSON-файлы формируются в модуле TeseraTop1000.
Формирует словарь первых слов из названий игр на русском и на английском
"""

import json
import re

first_name_rus = []
first_name_eng = []
for name in range(60):
    with open(fr'../TeseraTop1000/{name}.json') as file:
        g = json.load(file)
        for r in range(len(g)):
            f_n_r = g[r]['title'].split()[0]
            f_n_r = re.sub(r'\W', '', f_n_r)
            first_name_rus.append(f_n_r)
            # print(g[r]['title'])
            try:
                f_n_e = g[r]['title2'].split()[0]
                f_n_e = re.sub(r'\W', '', f_n_e)
                first_name_eng.append(f_n_e)
            except Exception as ex:
                print(g[r]['title'], "have no title2")

            # print(g[r].keys())
    # print(g['id'], g['testerId'], g['title'], g['title2'])

with open(fr'../TopList/first_name_rus.json', 'w+') as file:
    file.write(json.dumps(first_name_rus, indent=4))

with open(fr'../TopList/first_name_eng.json', 'w+') as file:
    file.write(json.dumps(first_name_eng, indent=4))


# with open(fr'../TopList/first_name_rus.json') as file:
#     g = json.load(file)
# print([(x, y) for x, y in enumerate(g)])
# print(g)

# with open(fr'../TopList/first_name_eng.json') as file:
#     g = json.load(file)
# print([(x, y) for x, y in enumerate(g)])

