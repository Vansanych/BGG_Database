"""
Модуль создания словаря из словарей игр с ценами
"""

from body.searching_prices3 import search_prices  # импорт функции создания словаря с игрой и ее ценой
from body.sorting_posts import sell_posts_list  # импорт списка постов


def dict_games_with_prices():
    games_dict = {}
    for post in range(len(sell_posts_list)):
        try:
            if search_prices(post):  # проверка на наличие записей в словаре
                games_dict[post] = search_prices(post)  # добавление словаря созданного из одного поста
        except Exception as ex:
            print('initialize module', ex)
    return games_dict
