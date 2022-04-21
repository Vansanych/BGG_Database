from sorting_posts import sell_posts_list
import re

post = sell_posts_list[9]
print(post)
positions = post.split('\n')

for position in positions:
    integers = re.findall('(\d+)', position)
    if integers:
        for integer in integers:
            if int(integer) < 100:
                    position = position.replace(integer, '', 1).replace('.', '', 1)
            else:
                if int(integer) < 100000:
                    price = integer
                    print(price)
                    if "-" in position:
                        list_from_position = position.split('-')
                    else:
                        list_from_position = position.split('.')
                    print("name", list_from_position[0])

