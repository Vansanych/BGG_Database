"""
Сравнивает первые слова названий из постов БНИ со списком первых слов из названий игр из Топ Тесеры.
Затем сравнивает вторые слова
"""

from body.filter_3 import filter_2, get_strings
from body.sorting_posts import sell_posts_dict
import json


def open_file(number, language):
    with open(fr'../TopList/{number}_name_{language}.json') as file:
        return json.load(file)


def search_names(post_number):
    names = filter_2(get_strings(post_number))

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
    return names_list, trash_list


def search_names_from_dict(names):
    first_tesera_rus = open_file('first', 'rus')
    second_tesera_rus = open_file('second', 'rus')
    first_tesera_eng = open_file('first', 'eng')
    second_tesera_eng = open_file('second', 'eng')

    names_list = []
    for name in names:
        if name[0] in first_tesera_rus or name[0] in first_tesera_eng:
            if name[1].capitalize() in second_tesera_rus or name[1].capitalize() in second_tesera_eng:
                names_list.append([name[0], name[1]])
            else:
                names_list.append([name[0], ''])
    return names_list


def create_names_list(x):
    post = sell_posts_dict[x][1]
    strings = post.split('\n')
    names = filter_2(strings)
    return search_names_from_dict(names)


# def create_full_dict(dict1, list1):
#     full_dict = {}
#     for post_id1 in dict1:
#         if list1(post_id1):
#             full_dict[post_id1] = [dict1[post_id1][0], list1post_id1)


full_dict = {}
for post_id in sell_posts_dict:
    if create_names_list(post_id):
        full_dict[post_id] = [sell_posts_dict[post_id][0], create_names_list(post_id), sell_posts_dict[post_id][1]]

if __name__ == '__main__':
    print("names: ", search_names(23)[0])
    print("trash: ", search_names(23)[1])
    print(full_dict)
