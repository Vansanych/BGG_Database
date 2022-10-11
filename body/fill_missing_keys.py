"""
Заполняет словарь недостающими парами
"""

import json

with open(fr'../TopList/Top900.json') as file:
    g = json.load(file)
    for r in range(len(g)):
        key_list = []
        for key in g[r].keys():
            key_list.append(key)
        if len(key_list) != 31:
            g[r]['title2'] = g[r].get('title2')
            g[r]['title3'] = g[r].get('title2')
            g[r]['descriptionShort'] = g[r].get('descriptionShort')
            g[r]['description'] = g[r].get('description')
            print(r, [x for x in g[0].keys() if x not in g[r].keys()])

with open(fr'../TopList/Top900_1.json', 'w+') as file:
    file.write(json.dumps(g, indent=4))
