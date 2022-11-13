"""
Модуль для запуска процесса формирования словарей из игр и цен
"""

from searching_prices3 import search_prices
from sorting_posts import sell_posts_list


def dict_games_with_prices():
    games_dict = {}
    for post in range(len(sell_posts_list)):
        try:
            if search_prices(post):
                games_dict[post] = search_prices(post)
        except Exception as ex:
            print('initialize module', ex)
    return games_dict
