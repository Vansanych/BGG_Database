"""Модуль форматирует json-файл.
С помощью параметра indent разбивает json-файл на строки, содержащие одну пару ключ:значение"""

import json

# name = 'TeseraTop1000.txt'
name = 'TeseraTop1000.txt'
with open(fr'..\body\{name}') as g:
    g1 = json.load(g)
    print(type(g1))
    # print(g1["response"]["items"][TeseraTop1000]["text"])

with open(fr'..\body\{name}_formated.json', 'w+') as f:
    f.write(json.dumps(g1, indent=4))
