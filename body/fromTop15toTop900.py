"""
Объединяет файлы по 15 игр в один файл
"""

import json

f = []
for name in range(60):
    with open(fr'../TeseraTop1000/{name}.json') as file:
        g = json.load(file)
        for r in range(len(g)):
            f.append(g[r])


with open(fr'../TopList/Top900.json', 'w+') as file:
    file.write(json.dumps(f, indent=4))
