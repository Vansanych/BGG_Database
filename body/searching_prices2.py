"""
Модуль выполняет поиск цен.
Затем объединяет в словарь с названием игры.
"""

from sorting_posts import sell_posts_list
from search_names_2 import names_list
import re


post = sell_posts_list[13]  # выбираем номер поста
print(post, '\n')
post_clear = re.sub("\W", " ", post)  # удаляет знаки препинания
digits = re.findall('\d+', post_clear)  # находим цифры в посте
prices = [price for price in digits if int(price) // 50 and int(price) < 100_000]  # составляем список цен
price_list = {}
words = post_clear.split()


def searching_function(first_name, lst):
    lst = lst[lst.index(first_name)::]  # поиск начинается с названия игры
    text = " ".join(lst)  # объединяем список из слов в текст
    match = re.search('\d+', text)[0]  # выполняем поиск цифр
    return match


for name in names_list:
    if type(name) == list:
        price = searching_function(name[0], words)
        if price in prices:
            price_list[name[0] + ' ' + name[1]] = price  # присваиваем названию игры стоимость, ближайшую по тексту
    else:
        price = searching_function(name, words)
        if price in prices:
            price_list[name] = price  # присваиваем названию игры стоимость, ближайшую по тексту


print(price_list)
