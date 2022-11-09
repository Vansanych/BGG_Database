"""
Модуль выполняет поиск цен.
Затем объединяет в словарь с названием игры.
"""

from sorting_posts import sell_posts_list
from search_names_2 import search_names
import re


def searching_function(first_name, lst):
    try:
        lst = lst[lst.index(first_name)::]  # поиск начинается с названия игры
    except Exception as ex:
        print(ex, first_name)
    try:
        match = re.search('\d{2,4}[0]', lst)[0]  # выполняем поиск цифр (3-5 значных с нолем в конце)
        return match
    except Exception as ex:
        return 0


def search_prices(post_number):
    names_list = search_names(post_number)[0]
    post = sell_posts_list[post_number]  # выбираем номер поста
    price_list = {}
    for name in names_list:
        if type(name) == list:  # проверка количества слов в названии
            price = searching_function(name[0], post)
            price_list[name[0] + ' ' + name[1]] = price  # присваиваем названию игры стоимость, ближайшую по тексту
        else:
            price = searching_function(name, post)
            price_list[name] = price  # присваиваем названию игры стоимость, ближайшую по тексту
    return price_list
