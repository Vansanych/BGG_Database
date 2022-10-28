from sorting_posts import sell_posts_list
from search_names_2 import names_list
import re

post = sell_posts_list[7]  # выбираем номер поста
post_clear = re.sub("\W", " ", post)  # удаляет знаки препинания
digits = re.findall('\d+', post_clear)  # находим цифры в посте
prices = [price for price in digits if int(price) // 50 and int(price) < 100_000]  # составляем список цен
price_list = {}
for name in names_list:
    words = post_clear.split()
    words = words[words.index(name[0])::]
    post_clear = " ".join(words)
    match = re.search('\d+', post_clear)[0]
    if match in prices:
        price_list[name[0] + ' ' + name[1]] = match  # присваиваем названию игры стоимость, ближайшую по тексту
print(price_list)
