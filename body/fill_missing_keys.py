"""
Заполняет словарь недостающими парами
"""

import json

with open(fr'../TopList/Top900.json') as file:
    g = json.load(file)
    for number, game in enumerate(g):
        key_list = [key for key in game]
        if len(key_list) != 31:
            new_dict = {}
            for key in g[0].keys():
                game[key] = game.get(key)
            value_list = [value for value in game.values()]
            key_list = [key for key in g[0].keys()]
            for i in range(len(key_list)):
                new_dict[key_list[i]] = game[key_list[i]]
            game = new_dict

            print(number, [x for x in g[0].keys() if x not in game.keys()])

with open(fr'../TopList/Top900_2.json', 'w+') as file:
    file.write(json.dumps(g, indent=4))
