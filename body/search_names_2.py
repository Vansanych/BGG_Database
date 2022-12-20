"""
Функция filter22 выполняет поиск максимального совпадения названия игры БНИ с названием игр Тесеры.
Сравнивает первые слова названий из постов БНИ со списком первых слов из названий игр из Топ Тесеры.
Затем сравнивает вторые слова
"""

from body.filter_3 import filter_22, get_strings
from body.sorting_posts import sell_posts_dict
import json
import sqlite3
import re


def open_file(number, language):
    with open(fr'../TopList/{number}_name_{language}.json') as file:
        return json.load(file)


def search_names(post_number):
    names = filter_22(get_strings(post_number))

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


def search_matches_from_sql(column, words):
    """Функция для поиска слова из названия игры среди названий игр ТОП 900 Тесеры.
    Выдает кортеж из названий игр содержащих искомое слово"""
    base = sqlite3.connect('../filters/Tesera_Top5000.db')  # соединение с базой Top900
    cur = base.cursor()
    cur.execute(f'SELECT "{column}" FROM data WHERE "{column}" LIKE "%{words[0]}%"')
    # выборка из базы Тесера по названию игры
    name_tuple = cur.fetchall()  # находит все совпадения
    return name_tuple


def search_words_in_tuple(names_tuple, words):
    names_list = []
    new_words_list = names_list  # нужно для дальнейшего сравнения длин списков
    for name_t in names_tuple:
        name_t = str(name_t[0]).replace(':', ' ').replace('.', ' ')  # name_t[0] индекс нужен потому что это кортеж
        names_list = [words[0]]
        for word in words[1:]:
            if (word.capitalize() in name_t.split()) or (word.lower() in name_t.split()):
                # поиск слов с заглавной и прописной букв
                names_list.append(word)
        if len(names_list) > len(new_words_list):
            new_words_list = names_list
    return new_words_list


def search_names_from_dict2(names_list):
    """Функция составляет список слов названий из одного поста"""
    new_names_list = []
    columns_list = ['title', 'title2', 'title3']
    for words in names_list:
        names_tuple_list = []
        for column in columns_list:
            names_tuple_list.append(search_matches_from_sql(column, words))
        if names_tuple_list:
            list_words_lists_title = []
            for words_list_title in names_tuple_list:
                name_words_list = search_words_in_tuple(words_list_title, words)
                list_words_lists_title.append(name_words_list)
            if len(list_words_lists_title) > 1:
                list_len_words_list_title = [len(lst) for lst in list_words_lists_title]  # список длин списков
                ind_list_len = max(list_len_words_list_title)  # поиск максимальной длины списка
                words_list_title = list_words_lists_title[list_len_words_list_title.index(ind_list_len)]
                if words_list_title:
                    new_names_list.append(words_list_title)
    return new_names_list


def create_names_list(x):
    post = sell_posts_dict[x][1]
    post = re.sub(',', ' ', post)
    strings = re.split(r'\d\d\d+', post)
    # for number, words in enumerate(strings):
    #     print(number, words)
    # print(strings[0])
    names_list = filter_22(strings)
    # print(1, search_names_from_dict(names_list))
    # print(2, search_names_from_dict2(names_list))
    return search_names_from_dict2(names_list)


full_dict = {}
for post_id in range(414134, 414135):
# for post_id in sell_posts_dict:
    print(post_id, 'body.search_names_2')
    words_in_name = create_names_list(post_id)
    if words_in_name:
        full_dict[post_id] = [sell_posts_dict[post_id][0], words_in_name, sell_posts_dict[post_id][1]]
        print(full_dict[post_id][1])
        print(full_dict[post_id][2])

if __name__ == '__main__':
    pass
    # print("names: ", search_names(25)[0])
    # print("trash: ", search_names(25)[1])
    # print('full_dict:', full_dict)
    # first_tesera_rus = open_file('first', 'rus')
    # print(first_tesera_rus)
