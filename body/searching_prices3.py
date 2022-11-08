"""
Модуль выполняет поиск цен.
Затем объединяет в словарь с названием игры.
Вариант, где первым шагом происходит удаление всех ненужных чисел из поста.
"""

from sorting_posts import sell_posts_list
from search_names_2 import names_list
import re


post = sell_posts_list[16]  # выбираем номер поста
print(post, '\n')
post_clear = re.sub("\W", " ", post)  # удаляет знаки препинания
digits = re.findall('\d+', post_clear)  # находим цифры в посте
prices = [price for price in digits if int(price) // 50 and int(price) < 100_000]  # составляем список цен
odd_digits = [digit for digit in digits if digit not in prices]
price_list = {}
words = post_clear.split()


def searching_function(first_name, lst, price):
    lst = lst[lst.index(first_name)::]  # поиск начинается с названия игры
    text = " ".join(lst)  # объединяем список из слов в текст
    # print(price, text[:200:], '\n')
    try:
        match = re.search(f'{price}', text)[0]  # выполняем поиск цифр
        return match
    except Exception as ex:
        return 0


for name in names_list:
    print(name)
    if type(name) == list:  # проверка количества слов в названии
        for any_price in prices:
            price = searching_function(name[0], words, any_price)
            if price in prices:
                price_list[name[0] + ' ' + name[1]] = price  # присваиваем названию игры стоимость, ближайшую по тексту
                prices.pop(prices.index(price))
                break
            else:
                post_clear = re.sub(f'{price}\S+', f'{price}', post_clear)
                words = post_clear.split()
                words.pop(words.index(price))
                price = searching_function(name[0], words, any_price)
                price_list[name[0] + ' ' + name[1]] = price  # присваиваем названию игры стоимость, ближайшую по тексту
    else:
        for any_price in prices:
            price = searching_function(name, words, any_price)
            while price not in prices:
                words.pop(words.index(price))
                price = searching_function(name, words, any_price)
            price_list[name] = price  # присваиваем названию игры стоимость, ближайшую по тексту


print(price_list)
