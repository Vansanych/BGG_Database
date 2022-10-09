from filter_2 import names
import json

with open(fr'../TopList/first_name_rus.json') as file:
    names_list_tesera = json.load(file)

names_list = []
trash_list = []
for name in names:
    if name in names_list_tesera:
        names_list.append(name)
    else:
        trash_list.append(name)
# print(names)
print("names: ", names_list)
print("trash: ", trash_list)
