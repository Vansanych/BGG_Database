"""
Модуль выполняет поиск цен.
Затем объединяет в словарь с названием игры.
"""
import json
import re
# from body.search_names_2 import full_dict


def searching_function(first_name, next_name, lst):
    """Функция для поиска цен игр в посте, кроме последней"""
    first_word = first_name[0]
    last_word = first_name[-1]
    next_word = next_name[0]
    first_word = re.sub('[.!:]', '', first_word)
    last_word = re.sub('[.!:]', '', last_word)
    next_word = re.sub('[.!:]', '', next_word)
    try:
        txt = lst[lst.index(last_word):lst.index(next_word)]
        txt_for_dict = lst[lst.index(first_word):lst.index(next_word)]
        # поиск начинается с названия игры и заканчивается названием следующей
        match = re.search('\d{1,3}[0|5][0]', txt)[0]
        # выполняем поиск первой попавшейся цены между двумя названиями игр (3-5 значных с нолем в конце)
        return match, txt_for_dict
    except Exception as ex:
        return 0, 0


def searching_function_last_name(first_name, lst):
    """Функция для поиска цен игр в посте, кроме последней"""
    first_word = first_name[0]
    last_word = first_name[-1]
    first_word = re.sub('[.!:]', '', first_word)
    last_word = re.sub('[.!:]', '', last_word)
    try:
        txt = lst[lst.index(last_word):]
        txt_for_dict = lst[lst.index(first_word):]
        # поиск начинается с названия игры и заканчивается названием следующей
        match = re.search('\d{1,3}[0|5][0]', txt)[0]
        # выполняем поиск первой попавшейся цены между двумя названиями игр (3-5 значных с нолем в конце)
        return match, txt_for_dict
    except Exception as ex:
        return 0, 0


def searching_function_last_name_old(first_name, lst):
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
    for name in names_list[:-1]:  # перебор названий из списка, за исключением последнего
        founded_price = searching_function(name[1], names_list[names_list.index(name) + 1][1], post)
        price_list[name[0]] = founded_price  # присваиваем названию игры стоимость, ближайшую по тексту
    name = names_list[-1]  # поиск цены для последнего названия из списка
    last_price = searching_function_last_name(name[1], post)
    price_list[name[0]] = last_price  # присваиваем названию игры стоимость, ближайшую по тексту

    return price_list


# print(full_dict[[i for i in full_dict.keys()][0]])
with open(r'C:\Users\Иван\Desktop\Иван\python\pythonProject\BG_database\body\dict.json') as f:
    full_dict = json.load(f)

# for post_id in full_dict:
for post_id in ['452157']:
    names = full_dict[post_id][1]
    text = full_dict[post_id][2]
    full_dict[post_id][1] = search_prices(names, text)
    del (full_dict[post_id][2])  # (?) удаляем текст поста он типа больше не нужен
    # print(search_prices(names, text))
    # print(full_dict[[i for i in full_dict.keys()][0]])
    print(full_dict[post_id])

counter = 0
for post_id in ['452157']:
# for post_id in full_dict:
    # print(post_id)
    for game in full_dict[post_id][1]:
        counter += 1
        price = full_dict[post_id][1][game][0]
        text = full_dict[post_id][1][game][1]
        # print(counter, game, price, '\n', '<', text, '>')

# print(full_dict[[i for i in full_dict.keys()][0]])
# print(full_dict[[i for i in full_dict.keys()][0]][1])
# print(full_dict[[i for i in full_dict.keys()][0]][1]['Meeple war'][0])
# print(full_dict[[i for i in full_dict.keys()][0]][1]['Meeple war'][1])

print(len(full_dict))
