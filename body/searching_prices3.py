"""
Модуль выполняет поиск цен.
Затем объединяет в словарь с названием игры.
"""

from sorting_posts import sell_posts_list
from search_names_2 import names_list
import re


post = sell_posts_list[20]  # выбираем номер поста
print(post, '\n')
post_clear = re.sub("\W", " ", post)  # удаляет знаки препинания
price_list = {}
words = post_clear.split()


def searching_function(first_name, lst):
    lst = lst[lst.index(first_name)::]  # поиск начинается с названия игры
    text = " ".join(lst)  # объединяем список из слов в текст
    print(text[:150:], '\n')
    try:
        match = re.search('\d{3,5}', text)[0]  # выполняем поиск цифр
        return match
    except Exception as ex:
        return 0


for name in names_list:
    if type(name) == list:  # проверка количества слов в названии
        price = searching_function(name[0], words)
        price_list[name[0] + ' ' + name[1]] = price  # присваиваем названию игры стоимость, ближайшую по тексту
    else:
        price = searching_function(name, words)
        price_list[name] = price  # присваиваем названию игры стоимость, ближайшую по тексту


print(price_list)
