"""
Функция filter22 выполняет поиск максимального совпадения названия игры БНИ с названием игр Тесеры.
Сравнивает первые слова названий из постов БНИ со списком первых слов из названий игр из Топ Тесеры.
Затем сравнивает вторые слова
"""

from body.filter_3 import filter_22, get_strings
from body.sorting_posts import sell_posts_dict
import json
import sqlite3


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


def search_matches_from_sql(table, words):
    """Функция для поиска слова из названия игры среди названий игр ТОП 900 Тесеры.
    Выдает кортеж из названий игр содержащих искомое слово"""
    base = sqlite3.connect('../SQL/Tesera_Top3.db')  # соединение с базой Top900
    cur = base.cursor()
    cur.execute(f'SELECT "{table}" FROM data WHERE "{table}" LIKE "%{words[0]}%"')
    # выборка из базы Тесера по названию игры
    name_tuple = cur.fetchall()  # находит все совпадения
    return name_tuple


def search_words_in_tuple(names_tuple, words):
    names_list = [words[0]]
    new_words_list = names_list  # нужно для дальнейшего сравнения длин списков
    for name_t in names_tuple:
        names_list = [words[0]]
        for word in words[1:]:
            if word.capitalize() in name_t[0].split():  # name_t[0] индекс нужен потому что это кортеж
                names_list.append(word)
            # else:
            #     print(word, 'not in ', name_t)
        if len(names_list) > len(new_words_list):
            new_words_list = names_list
    if len(new_words_list) < 2:  # нужно проверить необходимость этого условия
        new_words_list.append('')
    return new_words_list


def search_names_from_dict2(names_list):
    """Функция составляет список слов названий из одного поста"""
    # print(names_list, '\n')
    new_names_list = []
    for words in names_list:
        names_tuple = search_matches_from_sql('title', words)
        if names_tuple:
            new_names_list.append(search_words_in_tuple(names_tuple, words))
        else:
            names_tuple = search_matches_from_sql('title2', words)
            if names_tuple:
                new_names_list.append(search_words_in_tuple(names_tuple, words))
    return new_names_list


def create_names_list(x):
    post = sell_posts_dict[x][1]
    strings = post.split('\n')
    names_list = filter_22(strings)
    # print(1, search_names_from_dict(names_list))
    # print(2, search_names_from_dict2(names_list))
    return search_names_from_dict2(names_list)


full_dict = {}
# post_id = 414882
for post_id in sell_posts_dict:
    print(post_id, 'body.search_names_2')
    if create_names_list(post_id):
        full_dict[post_id] = [sell_posts_dict[post_id][0], create_names_list(post_id), sell_posts_dict[post_id][1]]

if __name__ == '__main__':
    pass
    # print("names: ", search_names(25)[0])
    # print("trash: ", search_names(25)[1])
    # print('full_dict:', full_dict)
    # first_tesera_rus = open_file('first', 'rus')
    # print(first_tesera_rus)
