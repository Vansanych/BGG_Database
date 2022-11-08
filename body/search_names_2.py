"""
Сравнивает первые слова названий из постов БНИ со списком первых слов из названий игр из Топ Тесеры.
Затем сравнивает вторые слова
"""

from filter_3 import filter_2, get_strings
import json

names = filter_2(get_strings(16))


def open_file(number, language):
    with open(fr'../TopList/{number}_name_{language}.json') as file:
        return json.load(file)


first_tesera_rus = open_file('first', 'rus')
second_tesera_rus = open_file('second', 'rus')
first_tesera_eng = open_file('first', 'eng')
second_tesera_eng = open_file('second', 'eng')

names_list = []
trash_list = []
for name in names:
    if name[0] in first_tesera_rus or name[0] in first_tesera_eng:
        if name[1].capitalize() in second_tesera_rus or name[1].capitalize() in second_tesera_eng:
            names_list.append([name[0], name[1]])
        else:
            names_list.append(name[0])
    else:
        trash_list.append(name)



# if __name__ == '__main__':
    # print("names: ", names_list)
    # print("trash: ", trash_list)
