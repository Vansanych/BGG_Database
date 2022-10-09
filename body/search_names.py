"""
сравнивает первые слова из постов со словарем названий игр из Топ Тесеры
"""

from filter_2 import names
import json

with open(fr'../TopList/first_name_rus.json') as file:
    names_list_tesera_rus = json.load(file)

with open(fr'../TopList/first_name_eng.json') as file:
    names_list_tesera_eng = json.load(file)

names_list = []
trash_list = []
for name in names:
    if name in names_list_tesera_rus or name in names_list_tesera_eng:
        names_list.append(name)
    else:
        trash_list.append(name)
# print(names)
print("names: ", names_list)
print("trash: ", trash_list)
