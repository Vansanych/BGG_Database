"""
получает json-файлы по 15 игр из Топ Тесеры
"""


import requests
import json

for name in range(60):
    url = fr'https://api.tesera.ru/games?offset={name}&limit=15&sort=-ratingn10'
    res = requests.get(url).json()
    print(f'parsing {name} page is running')
    with open(fr'../TeseraTop1000/{name}.json', 'w+') as file:
        file.write(json.dumps(res, indent=4))
