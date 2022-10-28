from sorting_posts import sell_posts_list
from search_names_2 import names_list
import re

post = sell_posts_list[7]  # выбираем номер поста
post_clear = re.sub("\W", " ", post)  # удаляет знаки препинания
digits = re.findall('\d+', post_clear)  # находим цифры в посте
prices = [price for price in digits if int(price) // 50 and int(price) < 100_000]  # составляем список цен
price_list = {}
for name in names_list:
    print(name)
    for price in prices:
        print(price)
        post_clear = re.sub(f'{price}\S', f'{price}', post_clear)  # убираем знаки после цены в посте
        words = post_clear.split()
        # print(price, post_clear.index(price), name[0], post_clear.index(name[0]))
        if type(name) == list:  # проверка количества слов в названии (одно или два)
            if words.index(price) > words.index(name[0]):  # Здесь ошибка. Находит первое совпадение.
                # нужно удалять из поста неподходящие цены
                price_list[name[0] + ' ' + name[1]] = price  # присваиваем названию игры стоимость, ближайшую по тексту
                prices.pop(prices.index(price))
                break
            else:
                words.pop(words.index(price))
                post_clear = " ".join(words)
                prices.pop(prices.index(price))
        else:
            if post_clear.index(price) > post_clear.index(name):
                price_list[name] = price  # присваиваем названию игры стоимость, ближайшую по тексту
                prices.pop(prices.index(price))
                break

print(post)
print(names_list)
print(prices)
print(price_list)
