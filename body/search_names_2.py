"""
Функция filter22 выполняет поиск максимального совпадения названия игры БНИ с названием игр Тесеры.
Сравнивает первые слова названий из постов БНИ со списком первых слов из названий игр из Топ Тесеры.
Затем сравнивает вторые слова
"""

from body.filter_3 import filter_22
from body.sorting_posts import sell_posts_dict
import sqlite3
import re


def search_matches_from_sql(column, words):
    """Функция для поиска слова из названия игры среди названий игр ТОП 5000 Тесеры.
    Выдает кортеж из названий игр содержащих искомое слово"""
    base = sqlite3.connect('../filters/Tesera_Top5000.db')  # соединение с базой Top5000
    cur = base.cursor()
    cur.execute(f'SELECT "{column}" FROM data WHERE "{column}" LIKE "{words[0]}%"')
    # выборка из базы Тесера по названию игры
    name_tuple = cur.fetchall()  # выдает все совпадения в виде списка list[(tuple,), (tuple,)...]
    return name_tuple


def search_words_in_tuple(names_tuple, words):
    """Поиск совпадений между словами из строчки БНИ и словами кортежа из SQL"""
    names_list = [words[0]]
    words_in_name_list = str(names_tuple[0]).replace(':', ' ').replace('.', ' ').split()
    # name_tuple[0] индекс нужен потому что это кортеж
    for word in words[1:]:
        if (word.capitalize() in words_in_name_list) or (word.lower() in words_in_name_list):
            # поиск слов с заглавной и прописной букв
            names_list.append(word)
    return names_list


def search_names_from_dict2(strings):
    """Функция составляет список слов названий из одного поста"""
    new_names_list = []
    best_match = None
    columns_list = ['title', 'title2', 'title3']
    for words in strings:  # words = []
        name_words_list = []
        for column in columns_list:
            names_tuples_from_column = search_matches_from_sql(column, words)
            # search_matches_from_sql(column, words) = [tuples]
            if names_tuples_from_column:
                for name_tuple in names_tuples_from_column:
                    name_words_list_new = search_words_in_tuple(name_tuple, words)
                    if len(name_words_list_new) > len(name_words_list):
                        name_words_list = name_words_list_new
                        best_match = name_tuple[0]
        if name_words_list:
            new_names_list.append([best_match, name_words_list])
    return new_names_list


def create_strings_list(x):
    post = sell_posts_dict[x][1]
    post = re.sub(',', ' ', post)
    strings = post.split('\n')
    strings = filter_22(strings)  # list[lists]
    return strings


full_dict = {}
for number, post_id in enumerate([i for i in sell_posts_dict.keys()]):
    print(number+1, 'из', len(sell_posts_dict), post_id, 'body.search_names_2')
    strings_list = create_strings_list(post_id)
    words_in_name = search_names_from_dict2(strings_list)
    if words_in_name:
        full_dict[post_id] = [sell_posts_dict[post_id][0], words_in_name, sell_posts_dict[post_id][1]]
print('full_dict:', full_dict)
