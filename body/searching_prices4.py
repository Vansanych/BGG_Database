"""
Модуль выполняет поиск цен.
Затем объединяет в словарь с названием игры.
"""

from body.search_names_2 import full_dict
import re


def searching_function(first_name, next_name, lst):
    """Функция для поиска цен игр в посте, кроме последней"""
    ex_list = []
    try:
        lst = lst[lst.index(first_name):lst.index(next_name[0]):]
        # поиск начинается с названия игры и заканчивается названием следующей
    except Exception as ex:
        ex_list.append(first_name)
    try:
        match = re.search('\d{1,3}[0|5][0]', lst)[0]  # выполняем поиск цифр (3-5 значных с нолем в конце)
        return match, lst
    except Exception as ex:
        return 0, 0


def searching_function_last_name(first_name, lst):
    """Функция для поиска цен последней игры в посте"""
    ex_list = []
    try:
        lst = lst[lst.index(first_name)::]
    # поиск начинается с названия игры и заканчивается в конце поста
    except Exception as ex:
        ex_list.append(first_name)
    try:
        match = re.search('\d{1,3}[0|5][0]', lst)[0]  # выполняем поиск цифр (3-5 значных с нолем в конце)
        return match, lst
    except Exception as ex:
        return 0, 0


def search_prices(names_list, post):
    price_list = {}
    for name in names_list:
        if names_list.index(name) != len(names_list)-1:
            price = searching_function(name[0], names_list[names_list.index(name)+1], post)
            price_list[name[0] + ' ' + str(name[1])] = price  # присваиваем названию игры стоимость, ближайшую по тексту
        else:
            price = searching_function_last_name(name[0], post)
            price_list[name[0] + ' ' + str(name[1])] = price  # присваиваем названию игры стоимость, ближайшую по тексту

    return price_list


# print(full_dict[[i for i in full_dict.keys()][0]])

for post_id in full_dict:
    names = full_dict[post_id][1]
    text = full_dict[post_id][2]
    full_dict[post_id][1] = search_prices(names, text)
    del(full_dict[post_id][2])
    # print(search_prices(names, text))

counter = 0
dict_games = full_dict
for post_id in dict_games:
    # print(post_id)
    for game in dict_games[post_id][1]:
        counter += 1
        # print(counter, game)
        price = dict_games[post_id][1][game][0]
        # print(price)

# print(full_dict[[i for i in full_dict.keys()][0]])
# print(full_dict[[i for i in full_dict.keys()][0]][1])
# print(full_dict[[i for i in full_dict.keys()][0]][1]['Meeple war'][0])
# print(full_dict[[i for i in full_dict.keys()][0]][1]['Meeple war'][1])
