from sorting_posts import sell_posts_list
from search_names_2 import names_list
import re

post = sell_posts_list[2]  # выбираем номер поста
post_clear = re.sub("\W", " ", post)  # удаляет знаки препинания
words_list = post_clear.split()  # разбивает пост на отдельные слова
digits = re.findall('\d+', post_clear)  # находим цифры в посте
prices = [price for price in digits if int(price) // 50]  # составляем список цен
price_list = {}
for name in names_list:
    for price in prices:
        if words_list.index(price) > words_list.index(name[0]):
            price_list[name[0] + ' ' + name[1]] = price  # присваиваем названию игры стоимость, ближайшую по тексту
            break

print(post)
print(price_list)
