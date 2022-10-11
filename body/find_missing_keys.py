"""
Ищет недостающие ключи
"""

import json

missing_keys = []
with open(fr'../TopList/Top900.json') as file:
    g = json.load(file)
    for lst in g:
        key_list = []
        for key in lst.keys():
            key_list.append(key)
        if len(key_list) != 31:
            missing_keys_in_one_game = [x for x in g[0].keys() if x not in lst.keys()]
            for key in missing_keys_in_one_game:
                if key not in missing_keys:
                    missing_keys.append(key)

print(missing_keys)
