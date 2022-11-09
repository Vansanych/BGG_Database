"""
Модуль для запуска процесса формирования словарей из игр и цен
"""

from searching_prices3 import search_prices
from sorting_posts import sell_posts_list


for post in range(len(sell_posts_list)):
    print(post, search_prices(post))
