"""
Модуль выполняет поиск цен.
Затем объединяет в словарь с названием игры.
"""

from sorting_posts import sell_posts_list
from search_names_2 import names_list
import re


post = sell_posts_list[23]  # выбираем номер поста
price_list = {}


def searching_function(first_name, lst):
    lst = lst[lst.index(first_name)::]  # поиск начинается с названия игры
    try:
        match = re.search('\d{2,4}[0]', lst)[0]  # выполняем поиск цифр (3-5 значных с нолем в конце)
        return match
    except Exception as ex:
        return 0


for name in names_list:
    if type(name) == list:  # проверка количества слов в названии
        price = searching_function(name[0], post)
        price_list[name[0] + ' ' + name[1]] = price  # присваиваем названию игры стоимость, ближайшую по тексту
    else:
        price = searching_function(name, post)
        price_list[name] = price  # присваиваем названию игры стоимость, ближайшую по тексту

print(price_list)
