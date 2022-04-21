from sorting_posts import sell_posts_list
import re

counter = 0
counter_prices = 0

for post in sell_posts_list:
    positions = post.split('\n')
    prices = []

    for position in positions:
        del_spaces = position.replace(' ', '')
        integers = re.findall('(\\d+)', del_spaces)
        if integers:
            for integer in integers:
                if 100 < int(integer) < 100000:
                    if int(integer) % 10 == 0 or re.findall('\\d+[9]', integer):
                        prices.append(integer)
                        counter_prices += 1

    print(counter, prices)
    counter += 1
print(counter_prices)
