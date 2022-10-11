"""
Заполняет словарь недостающими парами
"""

import json

with open(fr'../TopList/Top900.json') as file:
    g = json.load(file)
base_key_list = [key for key in g[0].keys()]
for number, game in enumerate(g):
    key_list = [key for key in game]
    if len(key_list) != 31:
        new_dict = {}
        for key in g[0].keys():
            game[key] = game.get(key)  # заполнение пропущенных пар
        for key in base_key_list:
            new_dict[key] = game[key]  # составление нового словаря с одинаковым порядком ключей
        game.clear()
        for key in base_key_list:
            game[key] = new_dict[key]
        print(number)

with open(fr'../TopList/Top900_2.json', 'w+') as file:
    file.write(json.dumps(g, indent=4))
