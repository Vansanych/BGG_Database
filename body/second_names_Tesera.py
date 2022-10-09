"""
read_json модуль забирает второе слово из названия игры Тесеры.
Полные названия игр в json-файлах по 15 игр с Топ Тесеры.
JSON-файлы формируются в модуле TeseraTop1000.
Формирует словарь вторых слов из названий игр на русском и на английском
"""

import json
import re

second_name_rus = []
second_name_eng = []
for name in range(60):
    with open(fr'../TeseraTop1000/{name}.json') as file:
        g = json.load(file)
        for r in range(len(g)):
            try:
                f_n_r = g[r]['title'].split()[1]
                f_n_r = re.sub(r'\W', '', f_n_r)
                second_name_rus.append(f_n_r)
            except Exception as ex1:
                print(g[r]['title'], "have no second name")
            # print(g[r]['title'])
            try:
                f_n_e = g[r]['title2'].split()[1]
                f_n_e = re.sub(r'\W', '', f_n_e)
                second_name_eng.append(f_n_e)
            except Exception as ex:
                print(g[r]['title'], "have no title2")

            # print(g[r].keys())
    # print(g['id'], g['testerId'], g['title'], g['title2'])

with open(fr'../TopList/second_name_rus.json', 'w+') as file:
    file.write(json.dumps(second_name_rus, indent=4))

with open(fr'../TopList/second_name_eng.json', 'w+') as file:
    file.write(json.dumps(second_name_eng, indent=4))


# with open(fr'../TopList/first_name_rus.json') as file:
#     g = json.load(file)
# print([(x, y) for x, y in enumerate(g)])
# print(g)

# with open(fr'../TopList/first_name_eng.json') as file:
#     g = json.load(file)
# print([(x, y) for x, y in enumerate(g)])

