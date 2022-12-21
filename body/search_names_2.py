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
    cur.execute(f'SELECT "{column}" FROM data WHERE "{column}" LIKE "{words[0]}%"')
    # выборка из базы Тесера по названию игры
    name_tuple = cur.fetchall()  # выдает все совпадения в виде списка list[(tuple,), (tuple,)...]
    return name_tuple


def search_words_in_tuple(names_tuple, words):
    """Поиск совпадений между словами из строчки БНИ и словами кортежа из SQL"""
    names_list = [words[0]]
    for name_t in names_tuple[0].split():  # name_t[0] индекс нужен потому что это кортеж
        name_t = str(name_t).replace(':', ' ').replace('.', ' ')
        for word in words[1:]:
            if (word.capitalize() in name_t) or (word.lower() in name_t):
                # поиск слов с заглавной и прописной букв
                names_list.append(word)
    return names_list


def search_names_from_dict2_old(strings):
    """Функция составляет список слов названий из одного поста"""
    new_names_list = []
    columns_list = ['title', 'title2', 'title3']
    for words in strings:  # words = []
        print(words)
        name_tuples_list = []
        for column in columns_list:
            name_tuples_list.append(search_matches_from_sql(column, words))
            # search_matches_from_sql(column, words) = [tuples], name_tuples_list = [list[tuples]]
        if name_tuples_list:
            list_words_lists_title = []
            for words_list_title in name_tuples_list:
                name_words_list = search_words_in_tuple(words_list_title, words)
                list_words_lists_title.append(name_words_list)
            if len(list_words_lists_title) > 1:
                list_len_words_list_title = [len(lst) for lst in list_words_lists_title]  # список длин списков
                ind_list_len = max(list_len_words_list_title)  # поиск максимальной длины списка
                words_list_title = list_words_lists_title[list_len_words_list_title.index(ind_list_len)]
                print(words_list_title)
                if words_list_title:
                    new_names_list.append(words_list_title)
    return new_names_list


def search_names_from_dict2(strings):
    """Функция составляет список слов названий из одного поста"""
    new_names_list = []
    columns_list = ['title', 'title2', 'title3']
    for words in strings[4:6]:  # words = []
        name_words_list = []
        print(words)
        for column in columns_list:
            names_tuples_from_column = search_matches_from_sql(column, words)
            # search_matches_from_sql(column, words) = [tuples]
            if names_tuples_from_column:
                for name_tuple in names_tuples_from_column:
                    name_words_list_new = search_words_in_tuple(name_tuple, words)
                    if len(name_words_list_new) > len(name_words_list):
                        name_words_list = name_words_list_new
        print(name_words_list)
        if name_words_list:
            new_names_list.append(name_words_list)
    return new_names_list


def create_names_list(x):
    post = sell_posts_dict[x][1]
    post = re.sub(',', ' ', post)
    strings = post.split('\n')
    # for number, words in enumerate(strings):
    #     print(number, words)
    # print(strings)
    strings = filter_22(strings)  # list[lists]
    # print(names_list)
    # print(1, search_names_from_dict(names_list))
    # print(2, search_names_from_dict2(names_list))
    return search_names_from_dict2(strings)


full_dict = {}
for post_id in range(414134, 414135):
# for number, post_id in enumerate(sell_posts_dict):
#     print(number+1, 'из', len(sell_posts_dict), post_id, 'body.search_names_2')
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
